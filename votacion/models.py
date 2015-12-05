import datetime
from django.db import models
from django.utils import timezone
from datetime import datetime  
from django.contrib.auth.models import User


class Universidad(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    logo = models.ImageField("Logo",upload_to="logos",blank=True)

    def __str__(self):            
        return self.nombre

class Unidad(models.Model):
    nombre= models.CharField(max_length=50)
    universidad = models.ForeignKey(Universidad)

    def __str__(self):   
        return self.nombre

class Profesor(models.Model):
    Estados=((1,'Confirmado'),(2,'No Confirmado'))
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apodo = models.CharField(max_length=50,blank=True)
    foto = models.ImageField("Foto",upload_to="fotos",blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    confirmado_flag = models.IntegerField(choices=Estados,default=2)
    universidad = models.ForeignKey(Universidad,blank=False)
    unidad = models.ForeignKey(Unidad,blank=False)
    user = models.ForeignKey(User,default='')

    def __str__(self):
        return u'%s %s' % (self.nombre, self.apellido)

class Calificacion(models.Model):
    puntaje = models.IntegerField(default=1)
    comentario = models.TextField(max_length=200,blank=True)
    pub_date = models.DateTimeField(default=datetime.now())
    profesor = models.ForeignKey(Profesor,blank=False)
    user = models.ForeignKey(User,default='')

    def __int__(self):           
        return self.puntaje

class Config_pagina(models.Model):
    paginacion = models.IntegerField(default=5)
    top = models.IntegerField(default=5)
    recientes = models.IntegerField(default=5)
    populares = models.IntegerField(default=5)

    def __int__(self):           
        return self.paginacion