# Generated by Django 3.1.5 on 2021-03-01 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieuniverse', '0002_auto_20210301_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
