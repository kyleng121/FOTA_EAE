# Generated by Django 4.0 on 2023-08-14 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfacesApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='deleted',
        ),
    ]