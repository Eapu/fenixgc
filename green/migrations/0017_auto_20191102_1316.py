# Generated by Django 2.2.6 on 2019-11-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green', '0016_auto_20191102_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acusa',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
    ]
