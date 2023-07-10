from django.db import models

# Create your models here.


class Empresas(models.Model):
    nombre_empresa = models.CharField(max_length=150)
    direccion_empresa = models.CharField(max_length=200)
    rut_empresa = models.CharField(max_length=12)
    telefono = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.nombre_empresa
 
class Empleados(models.Model):
    nombre_empleado = models.CharField(max_length=150)
    rut_empleado = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_empleado
    

      