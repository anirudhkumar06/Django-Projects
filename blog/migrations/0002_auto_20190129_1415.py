# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-29 08:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(max_length=25)),
                ('trainer_age', models.IntegerField(max_length=3)),
                ('trainer_contact', models.CharField(max_length=10)),
                ('trainer_address', models.TextField()),
                ('trainer_joining_date', models.DateField(default=datetime.datetime.now)),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Technology')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
