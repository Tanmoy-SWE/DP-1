# Generated by Django 4.1.1 on 2022-10-18 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_remove_course_coordinator_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='opened_by',
        ),
        migrations.RemoveField(
            model_name='course',
            name='department',
        ),
        migrations.RemoveField(
            model_name='course_session',
            name='coordinator',
        ),
        migrations.RemoveField(
            model_name='course_session',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='program_outcome',
            name='department',
        ),
        migrations.DeleteModel(
            name='Course_Coordinator',
        ),
        migrations.DeleteModel(
            name='Course_Instructor',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='institutionAdmin',
        ),
    ]