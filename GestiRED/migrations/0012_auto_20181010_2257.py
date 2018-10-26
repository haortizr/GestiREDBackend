# Generated by Django 2.1.1 on 2018-10-10 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0011_remove_evento_fechafinal'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='artefacto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='descripcion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='GestiRED.User'),
        ),
    ]