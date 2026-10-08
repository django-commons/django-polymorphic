from django.contrib import admin

from polymorphic.admin import (
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter,
    PolymorphicInlineSupportMixin,
    PolymorphicParentModelAdmin,
    StackedPolymorphicInline,
)

from .models import (
    BankPayment,
    CreditCardPayment,
    ModelA,
    ModelB,
    ModelC,
    Order,
    Payment,
    SepaPayment,
    StandardModel,
)


class ModelAChildAdmin(PolymorphicChildModelAdmin):
    base_model = ModelA


@admin.register(ModelB)
class ModelBAdmin(ModelAChildAdmin):
    base_model = ModelB


@admin.register(ModelC)
class ModelCAdmin(ModelBAdmin):
    base_model = ModelC
    show_in_index = True


@admin.register(ModelA)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    base_model = ModelA
    child_models = (ModelB, ModelC)
    list_filter = (PolymorphicChildModelFilter,)


class PaymentInline(StackedPolymorphicInline):
    class CreditCardPaymentInline(StackedPolymorphicInline.Child):
        model = CreditCardPayment

    class BankPaymentInline(StackedPolymorphicInline.Child):
        model = BankPayment

    class SepaPaymentInline(StackedPolymorphicInline.Child):
        model = SepaPayment

    model = Payment
    child_inlines = (
        CreditCardPaymentInline,
        BankPaymentInline,
        SepaPaymentInline,
    )


@admin.register(Order)
class OrderAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = (PaymentInline,)


class ModelBInline(admin.StackedInline):
    model = ModelB
    fk_name = "standard_model"
    readonly_fields = ["modela_ptr"]


@admin.register(StandardModel)
class StandardModelAdmin(admin.ModelAdmin):
    inlines = [ModelBInline]
