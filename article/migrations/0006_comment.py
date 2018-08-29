# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20180821_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=20, default='匿名')),
                ('content', models.CharField(verbose_name='内容', max_length=300)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('blog', models.ForeignKey(verbose_name='博客', to='article.Article')),
            ],
            options={
                'verbose_name': '博客评论',
                'verbose_name_plural': '博客评论',
            },
        ),
    ]
