# Generated by Django 3.1.5 on 2021-03-03 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieuniverse', '0007_auto_20210303_0525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='IMDb Rating',
            new_name='IMDb_rating',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Rotten Tomatoes Rating',
            new_name='Rotten_Tomatoes_rating',
        ),
    ]
