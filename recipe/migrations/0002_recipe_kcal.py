# Generated by Django 4.0.4 on 2022-04-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='kcal',
            field=models.IntegerField(default=0),
        ),
    ]