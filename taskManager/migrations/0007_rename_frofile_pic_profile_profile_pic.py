# Generated by Django 5.0.6 on 2024-05-20 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0006_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='frofile_pic',
            new_name='profile_pic',
        ),
    ]
