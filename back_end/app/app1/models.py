#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria models ORM
from django.db import models
from model_utils.models import TimeStampedModel
from .managers import *
#----------------------------------------------------------------------------------------------
# Create your models here.

#Tabla de empleados
class Persona(TimeStampedModel):
    
    
    nombre = models.CharField("nombre", max_length=50)
    apellido_paterno = models.CharField("Apellido paterno", max_length=50)
    apellido_materno= models.CharField("Apellido materno", max_length=120,blank=True)
    objects=PersonaManager()


    #Clase meta modifica las vistas de Django admin dentro de esta tabla
    class Meta:
        verbose_name="Persona"
        verbose_name_plural="Personas"
        ordering=["id"] 
        
        

    #La funcion __str__ es el mensaje de salida que tendra la tabla Empleado 
    def __str__(self):
        return str(self.id)+" "+self.nombre+" "+self.   apellido_paterno+" "+self.apellido_materno
#---------------------------------------------------------------------------------------------- 

