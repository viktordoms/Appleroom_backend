# Generated by Django 4.0 on 2022-04-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номери',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Місто')),
                ('slug', models.SlugField(max_length=160, unique=True)),
                ('number', models.ManyToManyField(null=True, to='contact_info.Number', verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Місто',
                'verbose_name_plural': 'Міста',
            },
        ),
    ]