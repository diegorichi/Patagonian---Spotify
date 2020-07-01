# Generated by Django 3.0.7 on 2020-06-29 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_song_external_urls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='external_urls',
        ),
        migrations.AddField(
            model_name='artist',
            name='external_urls',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='songs.Url'),
        ),
        migrations.RemoveField(
            model_name='song',
            name='external_urls',
        ),
        migrations.AddField(
            model_name='song',
            name='external_urls',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='songs.Url'),
        ),
    ]