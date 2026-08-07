from datetime import datetime, timedelta

from django.test import TestCase

from .models import ArtProject, MyModel, MyOtherModel, Project


class ManagerExamplesTests(TestCase):
    def test_custom_manager_and_inheritance(self):
        now = datetime(2026, 1, 1, 8, 0, 0)
        Project.objects.create(start_date=now - timedelta(days=1))
        art = ArtProject.objects.create(start_date=now, artist="A")

        ordered = list(ArtProject.objects_ordered.all())
        assert ordered == [art]
        assert list(Project.objects_ordered.most_recent())[0] == art

    def test_custom_queryset_manager_patterns(self):
        MyModel.my_objects.create(topic="a")
        MyOtherModel.my_objects.create(topic="b")

        assert MyModel.my_objects.count() == 1
        assert MyOtherModel.my_objects.count() == 1
