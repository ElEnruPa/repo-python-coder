from pyexpat import model
from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Familiares(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
