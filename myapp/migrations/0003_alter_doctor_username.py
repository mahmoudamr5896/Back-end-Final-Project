# Generated by Django 5.0.3 on 2024-03-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_doctor_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="username",
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]