# Generated by Django 4.0.3 on 2022-03-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mytodo', '0002_rename_task_todo_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
