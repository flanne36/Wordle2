# Generated by Django 4.1 on 2022-08-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_alter_scoreboard_day1_alter_scoreboard_day2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreboard',
            name='day1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scoreboard',
            name='day2',
            field=models.IntegerField(),
        ),
    ]
