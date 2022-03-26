# Generated by Django 4.0.2 on 2022-03-26 13:22

from django.db import migrations, models
import screens.models.source


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0017_auto_20210902_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='file',
            field=models.FileField(blank=True, help_text='videos must be mp4', null=True, upload_to=screens.models.source.get_file_path),
        ),
    ]
