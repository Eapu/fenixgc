# Generated by Django 2.2.2 on 2019-11-28 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_auto_20191128_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='totem',
            field=models.CharField(choices=[('La_Cilla', 'Mirador de La Cilla'), ('Galaz', 'Mesas de Galaz'), ('Fuente_Fria', 'Fuente Fría'), ('Montaña_Pajaritos', 'Montaña Pajaritos'), ('Doña Paca', 'Doña Pacas'), ('Mirador_de_Tejeda', 'Mirador de Tejeda'), ('Cuevas_del_Caballero', 'Cuevas_del_Caballero'), ('Las_Hoyas', 'Las Hoyas'), ('Acusa', 'Acusa'), ('Degollada_del_Sargento', 'Degollada del Sargento'), ('Lugarejos', 'Lugarejos'), ('Degollada_del_Humo', 'Degollada del Humo'), ('Cruz de María', 'Cruz de María'), ('Área Recreativa Tamadaba', 'Área Recreativa Tamadaba'), ('Fin del Mundo', 'Fin del Mundo')], default='Mirador de La Cilla', max_length=50),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='user',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
