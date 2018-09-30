# Generated by Django 2.1.1 on 2018-09-30 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControlCalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicial', models.DateTimeField(verbose_name='Date')),
                ('fechaFinal', models.DateTimeField(verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('etiquetas', models.CharField(max_length=2000)),
                ('fechaRegistro', models.DateTimeField(verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('etiquetas', models.CharField(max_length=2000)),
                ('fechaRegistro', models.DateTimeField(verbose_name='Date')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('privileges', models.ManyToManyField(to='GestiRED.Privilege')),
            ],
        ),
        migrations.CreateModel(
            name='TipoFase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRecurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('fechaRegistro', models.DateTimeField(verbose_name='Date')),
                ('perfiles', models.ManyToManyField(to='GestiRED.Perfil')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='responsables',
            field=models.ManyToManyField(to='GestiRED.User'),
        ),
        migrations.AddField(
            model_name='resource',
            name='tipoRecurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestiRED.TipoRecurso'),
        ),
        migrations.AddField(
            model_name='project',
            name='resources',
            field=models.ManyToManyField(to='GestiRED.Resource'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestiRED.Rol'),
        ),
        migrations.AddField(
            model_name='fase',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestiRED.Resource'),
        ),
        migrations.AddField(
            model_name='fase',
            name='tipoFase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestiRED.TipoFase'),
        ),
        migrations.AddField(
            model_name='controlcalidad',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestiRED.Resource'),
        ),
        migrations.AddField(
            model_name='controlcalidad',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestiRED.User'),
        ),
    ]
