# Generated by Django 2.2.6 on 2019-11-01 00:05

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('green', '0012_las_hoyas_lugarejos_tamadaba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cruz_de_Maria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('place', models.TextField(blank=True, max_length=20, null=True)),
                ('body', models.TextField(blank=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Cruz_de_Maria',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Cueva_Corcho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('place', models.TextField(blank=True, max_length=20, null=True)),
                ('body', models.TextField(blank=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Cueva Corcho',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Cuevas_del_Caballero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('place', models.TextField(blank=True, max_length=20, null=True)),
                ('body', models.TextField(blank=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Cuevas_del_Caballero',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Degollada_del_Sargento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('place', models.TextField(blank=True, max_length=20, null=True)),
                ('body', models.TextField(blank=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Degollada_del_Sargento',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Doña_Paca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('place', models.TextField(blank=True, max_length=20, null=True)),
                ('body', models.TextField(blank=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Doña Paca',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Fin_del_Mundo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('place', models.TextField(blank=True, max_length=20, null=True)),
                ('body', models.TextField(blank=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Fin_del_Mundo',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Fuentefria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('place', models.TextField(blank=True, max_length=20, null=True)),
                ('body', models.TextField(blank=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Fuentefria',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Galaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('place', models.TextField(blank=True, max_length=20, null=True)),
                ('body', models.TextField(blank=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Galaz',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Pajaritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('place', models.TextField(blank=True, max_length=20, null=True)),
                ('body', models.TextField(blank=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Pajaritos',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
