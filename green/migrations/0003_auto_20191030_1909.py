# Generated by Django 2.2.6 on 2019-10-30 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green', '0002_auto_20191030_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='min_body',
            new_name='place',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
