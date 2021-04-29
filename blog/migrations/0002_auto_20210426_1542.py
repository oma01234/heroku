# Generated by Django 3.2 on 2021-04-26 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email_address',
            field=models.CharField(default=datetime.datetime(2021, 4, 26, 14, 41, 41, 820833, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='password',
            field=models.CharField(default=datetime.datetime(2021, 4, 26, 14, 42, 22, 786634, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(default=datetime.datetime(2021, 4, 26, 14, 42, 32, 177876, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
