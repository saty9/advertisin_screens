# Generated by Django 2.2.1 on 2019-07-08 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulebuilderdirective',
            name='ends',
        ),
    ]
