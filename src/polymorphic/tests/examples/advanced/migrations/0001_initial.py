from django.db import migrations, models
import django.db.models.deletion
import polymorphic.models
import polymorphic.showfields


class Migration(migrations.Migration):
    initial = True

    dependencies = [("contenttypes", "0002_remove_content_type_name")]

    operations = [
        migrations.CreateModel(
            name="ModelA",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("field1", models.CharField(max_length=10)),
                ("polymorphic_ctype", models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="polymorphic_example_advanced.modela_set+", to="contenttypes.contenttype")),
            ],
            bases=(polymorphic.showfields.ShowFieldType, polymorphic.models.PolymorphicModel),
        ),
        migrations.CreateModel(
            name="ModelB",
            fields=[
                ("modela_ptr", models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to="example_advanced.modela")),
                ("field2", models.CharField(max_length=10)),
            ],
            bases=("example_advanced.modela",),
        ),
        migrations.CreateModel(
            name="ModelC",
            fields=[
                ("modelb_ptr", models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to="example_advanced.modelb")),
                ("field3", models.CharField(max_length=10)),
            ],
            bases=("example_advanced.modelb",),
        ),
        migrations.CreateModel(
            name="RelatingModel",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("many2many", models.ManyToManyField(to="example_advanced.modela")),
            ],
        ),
    ]
