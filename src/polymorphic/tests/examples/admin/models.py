from django.db import models
from polymorphic.models import PolymorphicModel


class ModelA(PolymorphicModel):
    field1 = models.CharField(max_length=10)


class ModelB(ModelA):
    standard_model = models.ForeignKey(
        "StandardModel",
        on_delete=models.CASCADE,
        related_name="modelb_items",
        null=True,
        blank=True,
    )
    field2 = models.CharField(max_length=10)


class ModelC(ModelB):
    field3 = models.CharField(max_length=10)


class StandardModel(models.Model):
    title = models.CharField(max_length=40, blank=True)


class Order(models.Model):
    number = models.CharField(max_length=20)


class Payment(PolymorphicModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=8, decimal_places=2)


class CreditCardPayment(Payment):
    card_type = models.CharField(max_length=20)


class BankPayment(Payment):
    bank_name = models.CharField(max_length=40)


class SepaPayment(Payment):
    iban = models.CharField(max_length=34)
