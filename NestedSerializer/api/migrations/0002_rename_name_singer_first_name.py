# Generated by Django 4.1.7 on 2023-04-08 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singer',
            old_name='name',
            new_name='first_name',
        ),
    ]