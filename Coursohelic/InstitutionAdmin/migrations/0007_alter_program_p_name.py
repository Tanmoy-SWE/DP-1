# Generated by Django 4.1.1 on 2022-10-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("InstitutionAdmin", "0006_remove_all_coordinators_p_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="p_name",
            field=models.CharField(default=None, max_length=200),
        ),
    ]
