# Generated by Django 2.1.1 on 2018-10-26 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0014_auto_20181025_2324'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ControlCalidad',
            new_name='QualityControl',
        ),
        migrations.RenameModel(
            old_name='Evento',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Fase',
            new_name='Phase',
        )
    ]
