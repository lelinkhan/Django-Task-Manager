# Generated by Django 4.2.3 on 2024-02-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='photos',
            field=models.JSONField(default=list),
        ),
        migrations.DeleteModel(
            name='TaskPhoto',
        ),
    ]
