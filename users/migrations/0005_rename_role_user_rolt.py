# Generated by Django 5.0.3 on 2024-03-14 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_mobile_remove_user_profile_picture_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role',
            new_name='rolt',
        ),
    ]
