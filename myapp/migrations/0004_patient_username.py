# Generated by Django 5.0.3 on 2024-03-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_alter_doctor_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="username",
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
