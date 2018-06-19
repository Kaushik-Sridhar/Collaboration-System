# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BasicArticle', '0015_auto_20180613_0511'),
        ('Community', '0025_communitycourses_community'),
        ('voting', '0017_auto_20180614_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_report', models.PositiveIntegerField(default=0)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BasicArticle.Articles')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Community.Community')),
            ],
        ),
        migrations.AddField(
            model_name='articlevotes',
            name='report',
            field=models.PositiveIntegerField(default=0),
        ),
    ]