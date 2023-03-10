# Generated by Django 4.1.6 on 2023-02-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=9999, verbose_name='Description')),
                ('image', models.ImageField(upload_to='static/img', verbose_name='Image')),
                ('url', models.URLField(blank=True, verbose_name='Url')),
            ],
        ),
    ]
