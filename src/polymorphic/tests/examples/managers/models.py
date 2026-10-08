from django.db import models
from polymorphic.managers import PolymorphicManager
from polymorphic.models import PolymorphicModel
from polymorphic.query import PolymorphicQuerySet


class TimeOrderedManager(PolymorphicManager):
    def get_queryset(self):
        return super().get_queryset().order_by("-start_date")

    def most_recent(self):
        return self.get_queryset()[:10]


class Project(PolymorphicModel):
    objects = PolymorphicManager()
    objects_ordered = TimeOrderedManager()
    start_date = models.DateTimeField()


class ArtProject(Project):
    artist = models.CharField(max_length=30)


class MyQuerySet(PolymorphicQuerySet):
    def started_after(self, dt):
        return self.filter(start_date__gt=dt)


class MyModel(PolymorphicModel):
    my_objects = PolymorphicManager.from_queryset(MyQuerySet)()
    topic = models.CharField(max_length=40)


class MyOtherModel(PolymorphicModel):
    my_objects = MyQuerySet.as_manager()
    topic = models.CharField(max_length=40)
