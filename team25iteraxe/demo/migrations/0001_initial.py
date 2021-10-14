# Generated by Django 3.2.8 on 2021-10-14 15:03

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=200, null=None)),
                ('last_name', models.CharField(default=None, max_length=200, null=None)),
                ('matricule', models.CharField(default=None, max_length=200, null=None)),
                ('description', models.CharField(max_length=3000, null=True)),
                ('first_day', models.DateTimeField(default=django.utils.timezone.now)),
                ('state', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(1)])),
                ('image', models.ImageField(default=None, null=None, upload_to='subjects_images')),
                ('virus_name', models.CharField(default=None, max_length=200, null=None)),
                ('cure', models.CharField(default=None, max_length=200, null=None)),
            ],
        ),
    ]
