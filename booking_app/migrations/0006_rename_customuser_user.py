# Generated by Django 5.0.1 on 2024-03-22 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('booking_app', '0005_customuser_alter_booking_user_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='User',
        ),
    ]
