# Generated by Django 2.1.1 on 2018-10-26 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0013_auto_20181025_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlcalidad',
            name='createUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_user', to='GestiRED.User'),
        ),
        migrations.AlterField(
            model_name='controlcalidad',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assign_user', to='GestiRED.User'),
        ),
    ]