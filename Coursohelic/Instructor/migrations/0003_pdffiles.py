# Generated by Django 4.1.1 on 2022-11-10 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Instructor", "0002_course_outcome_total_marks"),
    ]

    operations = [
        migrations.CreateModel(
            name="PdfFiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                (
                    "filepath",
                    models.FileField(null=True, upload_to="files/", verbose_name=""),
                ),
                (
                    "c_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Instructor.course_outcome",
                    ),
                ),
            ],
        ),
    ]