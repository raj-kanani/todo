# Generated by Django 4.0.3 on 2022-03-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_todos_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='date',
            field=models.DateField(),
        ),
    ]
