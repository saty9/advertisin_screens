# Generated by Django 3.2.4 on 2021-08-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0015_source_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='parents',
            field=models.ManyToManyField(blank=True, help_text='All sources that would be played by these playlists will be included in this one too.', related_name='children', to='screens.Playlist'),
        ),
    ]
