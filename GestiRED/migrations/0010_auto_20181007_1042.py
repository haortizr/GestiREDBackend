# Generated by Django 2.1.1 on 2018-10-07 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0009_auto_20181007_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='fases',
        ),
        migrations.AddField(
            model_name='fase',
            name='resource',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GestiRED.Resource'),
            preserve_default=False,
        ),
    ]
