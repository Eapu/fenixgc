# Generated by Django 2.2.2 on 2020-04-24 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200313_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_me',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
