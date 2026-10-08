from django.db import models
from polymorphic.models import PolymorphicModel


class ModelA(PolymorphicModel):
    field1 = models.CharField(max_length=10)


class ModelB(ModelA):
    field2 = models.CharField(max_length=10)


class ModelC(ModelA):
    field3 = models.CharField(max_length=10)
