# Generated by Django 4.1.1 on 2022-10-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstitutionAdmin', '0002_program_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='p_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
