# Generated by Django 3.0.7 on 2020-07-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0010_auto_20200630_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=512),
        ),
    ]
