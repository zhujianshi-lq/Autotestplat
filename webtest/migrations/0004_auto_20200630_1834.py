# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-06-30 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0003_webcasestep_order_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcasestep',
            name='asset_data',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='element_value',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='locate_method',
            field=models.IntegerField(choices=[(0, ''), (1, 'id'), (2, 'xpath'), (3, 'linktext'), (4, 'css')], default=0, verbose_name='元素定位方法'),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='operate_method',
            field=models.IntegerField(choices=[(1, 'open_brower'), (2, 'open_url'), (3, 'send_keys'), (4, 'click'), (5, 'switch_window'), (6, 'alert'), (7, 'switch_frame'), (8, 'switch_default_content')], default=4, verbose_name='操作方法'),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='test_data',
            field=models.CharField(max_length=200, null=True),
        ),
    ]