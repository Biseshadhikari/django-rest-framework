# Generated by Django 3.2.25 on 2024-08-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20240812_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='is_completed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
