# Generated by Django 4.2.1 on 2023-06-04 01:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Audiobase', '0016_alter_song_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='pubdate',
            field=models.IntegerField(default='0', verbose_name='Release year'),
        ),
    ]
