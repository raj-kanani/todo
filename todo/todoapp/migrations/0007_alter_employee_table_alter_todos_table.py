# Generated by Django 4.0.3 on 2022-03-10 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_alter_todos_date'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee',
            table='Employee',
        ),
        migrations.AlterModelTable(
            name='todos',
            table='Todos',
        ),
    ]
