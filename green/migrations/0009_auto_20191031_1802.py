# Generated by Django 2.2.6 on 2019-10-31 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green', '0008_degollada_del_humo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LaCilla',
            new_name='La_Cilla',
        ),
        migrations.AlterModelOptions(
            name='la_cilla',
            options={'verbose_name_plural': 'La_Cilla'},
        ),
    ]
