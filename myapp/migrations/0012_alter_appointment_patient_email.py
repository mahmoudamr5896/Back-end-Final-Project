# Generated by Django 5.0.3 on 2024-03-20 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_appointment_patient_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient_email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]