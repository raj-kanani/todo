# Generated by Django 4.0.3 on 2022-03-09 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Employee',
        ),
    ]
