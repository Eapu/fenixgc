# Generated by Django 2.2.6 on 2019-11-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green', '0017_auto_20191102_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cruz_de_maria',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='cueva_corcho',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='cuevas_del_caballero',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='degollada_del_humo',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='degollada_del_sargento',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='doña_paca',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='fin_del_mundo',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='fuentefria',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='galaz',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='la_cilla',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='las_hoyas',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='lugarejos',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='pajaritos',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='tamadaba',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='tejeda',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
    ]
