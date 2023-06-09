# Generated by Django 4.2.1 on 2023-06-04 01:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Audiobase', '0013_alter_song_pubdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album_name',
            field=models.CharField(default='def', max_length=100, verbose_name='Album name will appear here...'),
        ),
        migrations.AddField(
            model_name='song',
            name='artist_name',
            field=models.CharField(default='def', max_length=100, verbose_name='Artist name will appear here...'),
        ),
        migrations.AlterField(
            model_name='song',
            name='pubdate',
            field=models.IntegerField(verbose_name='Same as the album...'),
        ),
    ]
