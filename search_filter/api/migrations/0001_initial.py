# Generated by Django 4.1.7 on 2023-04-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('phone_number', models.CharField(help_text='Please Enter 11 Digits Phone Number', max_length=11, null=True)),
            ],
        ),
    ]
