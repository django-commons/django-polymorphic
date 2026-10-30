from django.test import TestCase

from polymorphic.formsets import PolymorphicFormSetChild, polymorphic_modelformset_factory

from .models import ModelA, ModelB, ModelC


ModelAFormSet = polymorphic_modelformset_factory(
    ModelA,
    fields=("field1",),
    extra=0,
    formset_children=(
        PolymorphicFormSetChild(ModelB, fields=("field1", "field2")),
        PolymorphicFormSetChild(ModelC, fields=("field1", "field3")),
    ),
)


class FormsetsExamplesTests(TestCase):
    def test_formset_factory_and_save(self):
        ModelB.objects.create(field1="b1", field2="b2")
        formset = ModelAFormSet(queryset=ModelA.objects.all())
        assert formset.total_form_count() == 1

        payload = {
            "form-TOTAL_FORMS": "1",
            "form-INITIAL_FORMS": "1",
            "form-MIN_NUM_FORMS": "0",
            "form-MAX_NUM_FORMS": "1000",
            "form-0-id": str(ModelA.objects.first().pk),
            "form-0-polymorphic_ctype": str(ModelB.objects.first().polymorphic_ctype_id),
            "form-0-field1": "b1-updated",
        }
        post_formset = ModelAFormSet(payload, queryset=ModelA.objects.all())
        assert post_formset.is_valid(), post_formset.errors
        post_formset.save()
        updated = ModelB.objects.get()
        assert updated.field1 == "b1-updated"
        assert updated.field2 == "b2"
