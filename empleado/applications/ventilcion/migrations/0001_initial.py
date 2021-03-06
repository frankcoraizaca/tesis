# Generated by Django 3.2.6 on 2021-08-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tramo', models.CharField(max_length=50, verbose_name='Tramo')),
                ('Dfinal', models.BooleanField(default=False, verbose_name='dfinal')),
                ('de1', models.CharField(blank=True, max_length=50, verbose_name='D1')),
                ('de2', models.CharField(blank=True, max_length=50, verbose_name='D2')),
                ('d1distancia', models.IntegerField(blank=True, verbose_name='D1[m]')),
                ('Ntramo', models.IntegerField(blank=True, verbose_name='N.Tramo')),
                ('accesorios', models.CharField(blank=True, max_length=50, verbose_name='Accesorios')),
                ('Darea', models.FloatField(blank=True, max_length=4, null=True, verbose_name='area[m]')),
            ],
        ),
    ]
