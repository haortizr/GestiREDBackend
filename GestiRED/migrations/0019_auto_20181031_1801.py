# Generated by Django 2.1.1 on 2018-10-31 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0018_auto_20181026_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualitycontrol',
            name='observation',
            field=models.CharField(max_length=400),
        ),
    ]
