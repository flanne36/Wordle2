# Generated by Django 4.1 on 2022-08-09 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordsdata',
            old_name='words',
            new_name='word',
        ),
    ]