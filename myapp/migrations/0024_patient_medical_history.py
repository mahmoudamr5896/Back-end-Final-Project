# Generated by Django 5.0.2 on 2024-03-24 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_remove_patient_medical_history_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='medical_history',
            field=models.TextField(blank=True, null=True),
        ),
    ]
