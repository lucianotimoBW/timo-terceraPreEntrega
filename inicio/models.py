from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField(default=18)
    
    def __str__(self):
        return f'Usuario = Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}'