# Generated by Django 3.2.6 on 2021-08-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipounion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('union', models.CharField(max_length=60, verbose_name='Area')),
            ],
        ),
    ]