# Generated by Django 4.1.7 on 2023-03-26 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplemodel',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
