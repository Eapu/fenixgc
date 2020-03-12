# Generated by Django 2.2.2 on 2020-02-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200208_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('avatar', models.FileField(blank=True, null=True, upload_to='')),
                ('body', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'About_me',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]
