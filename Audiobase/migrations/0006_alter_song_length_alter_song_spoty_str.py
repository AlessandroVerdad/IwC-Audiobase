# Generated by Django 4.2.1 on 2023-06-04 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audiobase', '0005_alter_artist_birth_alter_song_length_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='length',
            field=models.IntegerField(verbose_name='Length in [seconds]'),
        ),
        migrations.AlterField(
            model_name='song',
            name='spoty_str',
            field=models.IntegerField(verbose_name='Thousands of streams [x1000]'),
        ),
    ]