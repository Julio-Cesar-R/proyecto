#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria models ORM
from django.db import models
from model_utils.models import TimeStampedModel
from .managers import *
#----------------------------------------------------------------------------------------------
# Create your models here.

#Tabla de empleados
class Persona(TimeStampedModel):
    
    
    nombre = models.CharField("Nombre", max_length=50)
    apellido_paterno = models.CharField("Apellido paterno", max_length=50)
    apellido_materno= models.CharField("Apellido materno", max_length=120,blank=True)
    edad = models.PositiveIntegerField("Edad")
    email = models.EmailField("E-mail", max_length=254)
    telefono = models.CharField("Telefono", max_length=50)
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

class Estudios(TimeStampedModel):
    ESTUDIOS_CHOICES=(
        ("0","Bachillerato"),
        ("1","Licenciatura"),
        ("2","Maestria"),
        ("3","Doctorado"),
        ("4","Otro"),
    )   

    estudiante= models.ForeignKey(
        Persona, 
        on_delete=models.CASCADE,
        #Referencia de la relacion Libro y categoria
        related_name='persona_estudios'
    )
    nombre_carrera = models.CharField("Carrera", max_length=50)
    nivel_estudios=models.CharField("Nivel de estudios", max_length=50,choices=ESTUDIOS_CHOICES)
    promedio = models.PositiveIntegerField("Promedio")

    class Meta:
        verbose_name="Estudios"
        verbose_name_plural="Estudios"
        ordering=["id"] 
        
    def __str__(self):
        return str(self.id)+" "+self.nombre_carrera+" "+self.   nivel_estudios+" "+str(self.promedio)