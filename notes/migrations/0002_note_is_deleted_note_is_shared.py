# Generated by Django 4.2.9 on 2024-01-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='note',
            name='is_shared',
            field=models.BooleanField(default=False),
        ),
    ]