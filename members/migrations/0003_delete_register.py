# Generated by Django 3.2 on 2021-05-01 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_register_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
    ]
