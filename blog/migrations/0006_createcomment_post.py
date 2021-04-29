# Generated by Django 3.2 on 2021-04-27 17:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_createcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='createcomment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.post'),
            preserve_default=False,
        ),
    ]
