# Generated by Django 4.0.8 on 2023-08-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_season_thumbnail_remove_series_thumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='thumbnail_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]