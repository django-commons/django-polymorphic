from django.db.models import Q
from django.test import TestCase

from polymorphic.utils import prepare_for_copy

from .models import ModelA, ModelB, ModelC, RelatingModel


class AdvancedExamplesTests(TestCase):
    def setUp(self):
        self.a = ModelA.objects.create(field1="A1")
        self.b = ModelB.objects.create(field1="B1", field2="B2")
        self.c = ModelC.objects.create(field1="C1", field2="C2", field3="C3")

    def test_instance_of_and_q(self):
        assert list(ModelA.objects.instance_of(ModelB)) == [self.b, self.c]
        assert list(ModelA.objects.filter(Q(instance_of=ModelB))) == [self.b, self.c]

    def test_polymorphic_field_filtering(self):
        result = ModelA.objects.filter(Q(ModelB___field2="B2") | Q(ModelC___field3="C3"))
        assert list(result) == [self.b, self.c]

    def test_many_to_many_returns_real_instances(self):
        rel = RelatingModel.objects.create()
        rel.many2many.add(self.a, self.b, self.c)
        items = list(rel.many2many.all())
        assert isinstance(items[0], ModelA)
        assert isinstance(items[1], ModelB)
        assert isinstance(items[2], ModelC)

    def test_copy_and_non_polymorphic(self):
        original = ModelB.objects.first()
        prepare_for_copy(original)
        original.save()

        qs = ModelA.objects.non_polymorphic().all()
        assert all(type(item) is ModelA for item in qs)
        real = ModelA.objects.get_real_instances(qs)
        assert any(type(item) is ModelB for item in real)
