# Generated by Django 4.0.3 on 2022-03-14 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_alter_employee_table_alter_todos_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
