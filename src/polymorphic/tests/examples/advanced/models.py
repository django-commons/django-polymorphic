from django.db import models
from polymorphic.models import PolymorphicModel
from polymorphic.showfields import ShowFieldType


class ModelA(ShowFieldType, PolymorphicModel):
    field1 = models.CharField(max_length=10)


class ModelB(ModelA):
    field2 = models.CharField(max_length=10)


class ModelC(ModelB):
    field3 = models.CharField(max_length=10)


class RelatingModel(models.Model):
    many2many = models.ManyToManyField(ModelA)
