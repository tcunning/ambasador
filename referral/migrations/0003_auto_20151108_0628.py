# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import referral.models


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0002_auto_20151105_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'name', validators=[referral.models.validate_referral_name]),
        ),
    ]
