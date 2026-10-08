from django.db import migrations, models
import django.db.models.deletion
import polymorphic.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("topic", models.CharField(max_length=30)),
                ("polymorphic_ctype", models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="polymorphic_example_quickstart.project_set+", to="contenttypes.contenttype")),
            ],
            options={},
            bases=(polymorphic.models.PolymorphicModel,),
        ),
        migrations.CreateModel(
            name="ArtProject",
            fields=[
                ("project_ptr", models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to="example_quickstart.project")),
                ("artist", models.CharField(max_length=30)),
            ],
            options={},
            bases=("example_quickstart.project",),
        ),
        migrations.CreateModel(
            name="ResearchProject",
            fields=[
                ("project_ptr", models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to="example_quickstart.project")),
                ("supervisor", models.CharField(max_length=30)),
            ],
            options={},
            bases=("example_quickstart.project",),
        ),
    ]
