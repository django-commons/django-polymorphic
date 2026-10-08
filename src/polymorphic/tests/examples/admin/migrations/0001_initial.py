from django.db import migrations, models
import django.db.models.deletion
import polymorphic.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("contenttypes", "0002_remove_content_type_name")]

    operations = [
        migrations.CreateModel(
            name="ModelA",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("field1", models.CharField(max_length=10)),
                ("polymorphic_ctype", models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="polymorphic_example_admin.modela_set+", to="contenttypes.contenttype")),
            ],
            bases=(polymorphic.models.PolymorphicModel,),
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="ModelB",
            fields=[
                ("modela_ptr", models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to="example_admin.modela")),
                ("field2", models.CharField(max_length=10)),
            ],
            bases=("example_admin.modela",),
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount", models.DecimalField(decimal_places=2, max_digits=8)),
                ("polymorphic_ctype", models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="polymorphic_example_admin.payment_set+", to="contenttypes.contenttype")),
                ("order", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="payments", to="example_admin.order")),
            ],
            bases=(polymorphic.models.PolymorphicModel,),
        ),
        migrations.CreateModel(
            name="ModelC",
            fields=[
                ("modelb_ptr", models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to="example_admin.modelb")),
                ("field3", models.CharField(max_length=10)),
            ],
            bases=("example_admin.modelb",),
        ),
        migrations.CreateModel(
            name="BankPayment",
            fields=[
                ("payment_ptr", models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to="example_admin.payment")),
                ("bank_name", models.CharField(max_length=40)),
            ],
            bases=("example_admin.payment",),
        ),
        migrations.CreateModel(
            name="CreditCardPayment",
            fields=[
                ("payment_ptr", models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to="example_admin.payment")),
                ("card_type", models.CharField(max_length=20)),
            ],
            bases=("example_admin.payment",),
        ),
        migrations.CreateModel(
            name="SepaPayment",
            fields=[
                ("payment_ptr", models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to="example_admin.payment")),
                ("iban", models.CharField(max_length=34)),
            ],
            bases=("example_admin.payment",),
        ),
        migrations.CreateModel(
            name="StandardModel",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name="modelb",
            name="standard_model",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="modelb_items", to="example_admin.standardmodel"),
        ),
    ]
