# Generated by Django 4.0 on 2022-04-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, verbose_name='Опис'),
        ),
    ]
