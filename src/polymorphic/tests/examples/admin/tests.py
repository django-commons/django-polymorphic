from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from polymorphic.admin import PolymorphicChildModelFilter

from .admin import ModelAParentAdmin, ModelCAdmin, OrderAdmin, PaymentInline
from .models import (
    BankPayment,
    CreditCardPayment,
    ModelA,
    ModelB,
    ModelC,
    Order,
    SepaPayment,
    StandardModel,
)


class AdminExamplesTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpass"
        )

    def test_parent_child_admin_configuration(self):
        parent_admin = ModelAParentAdmin(ModelA, admin.site)
        assert parent_admin.base_model is ModelA
        assert tuple(parent_admin.get_child_models()) == (ModelB, ModelC)
        assert parent_admin.list_filter == (PolymorphicChildModelFilter,)
        assert ModelCAdmin.show_in_index is True

    def test_polymorphic_inline_models(self):
        order = Order.objects.create(number="ORD-1")
        CreditCardPayment.objects.create(order=order, amount="10.00", card_type="visa")
        BankPayment.objects.create(order=order, amount="20.00", bank_name="ABC")
        SepaPayment.objects.create(order=order, amount="30.00", iban="DE02120300000000202051")

        inline = PaymentInline(Order, admin.site)
        child_models = [child.model for child in inline.get_child_inline_instances()]
        assert set(child_models) == {CreditCardPayment, BankPayment, SepaPayment}

        order_admin = OrderAdmin(Order, admin.site)
        assert PaymentInline in order_admin.inlines

    def test_standard_model_inline_admin_renders_and_saves(self):
        self.client.force_login(self.user)
        add_url = reverse("admin:example_admin_standardmodel_add")

        response = self.client.get(add_url)
        assert response.status_code == 200

        post_data = {
            "title": "Inline Parent",
            "modelb_items-TOTAL_FORMS": "0",
            "modelb_items-INITIAL_FORMS": "0",
            "modelb_items-MIN_NUM_FORMS": "0",
            "modelb_items-MAX_NUM_FORMS": "1000",
            "_save": "Save",
        }
        response = self.client.post(add_url, data=post_data)
        assert response.status_code == 302
        assert StandardModel.objects.filter(title="Inline Parent").exists()
