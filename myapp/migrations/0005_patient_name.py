# Generated by Django 5.0.3 on 2024-03-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_patient_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]