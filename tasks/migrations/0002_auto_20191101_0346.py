# Generated by Django 2.2.4 on 2019-11-01 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemModel',
            new_name='Item',
        ),
    ]