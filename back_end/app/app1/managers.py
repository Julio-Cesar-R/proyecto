import imp
from django.db import models

from django.db.models import Q,Count



class PersonaManager(models.Manager):
    """ managers para el modelo autor """

    def buscar_todo(self):
        resultado = self.all()
        return resultado
    

    def buscar_apellido(self):
        resultado=self.filter(
            Q(apellido_paterno__contains="Perez")|Q(apellido_materno__contains="Perez")
        ).order_by("nombre").exclude(nombre__contains="Luis")
        return resultado
  
    def cantidad_apellidos_paternos(self):
        resultado = self.values('apellido_paterno').annotate(
            cantidad=Count('id')
        )
      
        return resultado