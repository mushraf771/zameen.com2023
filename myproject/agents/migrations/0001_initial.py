# Generated by Django 4.2.7 on 2023-11-15 04:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('top_seller', models.BooleanField(default=False)),
                ('date_hired', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
