# Generated by Django 4.2.13 on 2024-06-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0007_rename_frofile_pic_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
