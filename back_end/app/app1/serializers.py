
from rest_framework import serializers,pagination

from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields=("__all__")



class PersonaSerializer2(serializers.Serializer):
    nombre=serializers.CharField()
    apellido_paterno=serializers.CharField()
    correo=serializers.SerializerMethodField()

    def get_correo(self,obj):
        return str(obj.nombre.lower())+"."+str(obj.apellido_paterno.lower())+"."+str(obj.apellido_materno[0].lower())+"@gmail.com"


class PersonaSerializerCount(serializers.Serializer):
    apellido_paterno=serializers.CharField()
    cantidad=serializers.IntegerField()

#-----------------------------------------------------------------------------------------------
class PersonPagination(pagination.PageNumberPagination):
    page_size=2
    max_page_size=100