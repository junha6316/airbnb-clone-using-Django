# Generated by Django 2.2.5 on 2020-09-10 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='creaated',
            new_name='created',
        ),
    ]
