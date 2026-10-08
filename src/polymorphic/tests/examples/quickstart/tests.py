from django.db.models import Q
from django.test import TestCase

from .models import ArtProject, Project, ResearchProject


class QuickstartExamplesTests(TestCase):
    def test_create_objects_and_polymorphic_queries(self):
        Project.objects.create(topic="Department Party")
        ArtProject.objects.create(topic="Painting with Tim", artist="T. Turner")
        ResearchProject.objects.create(topic="Swallow Aerodynamics", supervisor="Dr. Winter")
        ResearchProject.objects.create(topic="Color Use in Late Cubism", supervisor="T. Turner")

        projects = list(Project.objects.all())
        assert len(projects) == 4
        assert isinstance(projects[0], Project)
        assert isinstance(projects[1], ArtProject)
        assert isinstance(projects[2], ResearchProject)

        assert list(Project.objects.instance_of(ArtProject)) == [projects[1]]

        combined = Project.objects.instance_of(ArtProject) | Project.objects.instance_of(
            ResearchProject
        )
        assert combined.count() == 3

        filtered = Project.objects.filter(
            Q(ArtProject___artist="T. Turner") | Q(ResearchProject___supervisor="T. Turner")
        )
        assert filtered.count() == 2
