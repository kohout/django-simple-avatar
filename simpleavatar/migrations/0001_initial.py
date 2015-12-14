# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import simpleavatar.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(max_length=1024, upload_to=simpleavatar.models.upload_avatar_file_path, blank=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(related_name='avatar', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
