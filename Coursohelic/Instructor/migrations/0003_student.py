# Generated by Django 4.1.1 on 2022-12-29 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coordinator', '0011_assignedcourses_is_mapped'),
        ('Instructor', '0002_remove_mapping_weight_course_outcome_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default=None, max_length=20)),
                ('student_name', models.CharField(default=None, max_length=100)),
                ('a_year', models.CharField(default=None, max_length=20)),
                ('course_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Coordinator.assignedcourses')),
            ],
        ),
    ]
