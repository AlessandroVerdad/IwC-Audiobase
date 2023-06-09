# Generated by Django 4.2.1 on 2023-06-04 00:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Audiobase', '0004_alter_album_bname_alter_artist_aname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='birth',
            field=models.DateField(verbose_name='Birth'),
        ),
        migrations.AlterField(
            model_name='song',
            name='length',
            field=models.IntegerField(max_length=100, verbose_name='Length in [seconds]'),
        ),
        migrations.AlterField(
            model_name='song',
            name='pubdate',
            field=models.DateTimeField(verbose_name='Release date'),
        ),
        migrations.AlterField(
            model_name='song',
            name='spoty_str',
            field=models.IntegerField(max_length=100, verbose_name='Thousands of streams [x1000]'),
        ),
    ]
