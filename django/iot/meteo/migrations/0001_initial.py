# Generated by Django 4.2.5 on 2023-12-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meteo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('temperaature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('pressure', models.FloatField()),
            ],
        ),
    ]
