# Generated by Django 3.2.7 on 2021-12-29 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventilcion', '0013_auto_20211229_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ashrae',
            name='LParea',
        ),
        migrations.RemoveField(
            model_name='ashrae',
            name='LPpersona',
        ),
    ]
