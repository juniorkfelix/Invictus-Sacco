# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-15 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import invictus.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('invictus', '0006_auto_20180214_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploads',
            name='KRA',
            field=models.FileField(upload_to=invictus.helpers.RandomFileName('/home/gathage/jungle/Sacco/invictus/static/invictus/uploads/kra/')),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='id_back',
            field=models.ImageField(upload_to=invictus.helpers.RandomFileName('/home/gathage/jungle/Sacco/invictus/static/invictus/uploads/ids/')),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='id_front',
            field=models.ImageField(upload_to=invictus.helpers.RandomFileName('/home/gathage/jungle/Sacco/invictus/static/invictus/uploads/ids/')),
        ),
    ]
