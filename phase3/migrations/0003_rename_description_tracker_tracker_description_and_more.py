# Generated by Django 4.0.1 on 2022-02-06 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phase3', '0002_cargo_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='description',
            new_name='tracker_description',
        ),
        migrations.RenameField(
            model_name='tracker',
            old_name='owner',
            new_name='tracker_owner',
        ),
    ]
