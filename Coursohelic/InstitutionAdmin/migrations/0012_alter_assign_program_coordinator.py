# Generated by Django 4.1.1 on 2022-10-18 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('InstitutionAdmin', '0011_assign_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign_program',
            name='coordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
