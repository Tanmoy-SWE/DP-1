# Generated by Django 4.1.1 on 2022-10-19 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Coordinator", "0005_course_course_outline"),
    ]

    operations = [
        migrations.RemoveField(model_name="course", name="course_outline",),
    ]
