# Generated by Django 4.1.7 on 2023-03-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_alter_examplemodel_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='contact',
            field=models.PositiveIntegerField(help_text='Please Enter 12 digits Contact Number'),
        ),
    ]
