# Generated by Django 2.2.2 on 2020-04-24 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200424_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_me',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]