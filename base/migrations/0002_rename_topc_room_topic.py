# Generated by Django 5.1.2 on 2024-11-06 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='Topc',
            new_name='topic',
        ),
    ]
