# Generated by Django 4.1.1 on 2022-12-27 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coordinator', '0009_program_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program_outcome',
            name='description',
            field=models.TextField(default=None, max_length=300, null=True),
        ),
    ]
