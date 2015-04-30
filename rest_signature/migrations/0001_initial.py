# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('key', models.CharField(max_length=40)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='signature', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False, default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=32, verbose_name='站点名称')),
                ('name', models.CharField(max_length=32, verbose_name='系统名称', validators=[django.core.validators.RegexValidator('^[a-z1-9]+$', '系统名称只能为小写字母或者数字', 'invalid')])),
            ],
        ),
        migrations.AddField(
            model_name='signature',
            name='site',
            field=models.ForeignKey(related_name='signature', to='rest_signature.Site'),
        ),
    ]
