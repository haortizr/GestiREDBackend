from django.db import models
from django.utils import timezone

# Create your models here.

class Privilege(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name


class Rol(models.Model):
    name = models.CharField(max_length=200)
    privileges = models.ManyToManyField(Privilege)

    def __str__(self):
        return '%s' % self.name


class User(models.Model):
        name = models.CharField(max_length=200)
        apellido = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        password = models.CharField(max_length=200)
        fechaRegistro = models.DateTimeField(default=timezone.now)
        roles =  models.ManyToManyField(Rol)

        def __str__(self):
            return '%s %s' % (self.name, self.apellido)


class TipoRecurso(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.nombre


class Resource(models.Model):
    nombre = models.CharField(max_length=200)
    etiquetas = models.CharField(max_length=2000)
    fechaRegistro = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=200)
    tipoRecurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)
    responsables = models.ManyToManyField('User')

    def save(self, *args, **kwargs):
        if self.id is None or self.nombre not in self.etiquetas:
            self.etiquetas = self.nombre + ' ' + self.etiquetas
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return '%s' % self.nombre


class ControlCalidad(models.Model):
    observacion = models.CharField(max_length=200)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


class TipoFase(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.nombre


class Fase(models.Model):
    fechaInicial = models.DateTimeField(default=timezone.now)
    fechaFinal = models.DateTimeField()
    tipoFase =  models.ForeignKey(TipoFase, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=200)
    etiquetas = models.CharField(max_length=2000)
    fechaRegistro = models.DateTimeField(default=timezone.now)
    resources = models.ManyToManyField(Resource)

    def save(self, *args, **kwargs):
        if self.id is None or self.name not in self.etiquetas:
            self.etiquetas = self.name + ' ' + self.etiquetas
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return '%s' % self.name

