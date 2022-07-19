
from rest_framework import serializers,pagination

from .models import Persona,Estudios

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields=("__all__")


#Serializador de persona
class PersonaSerializer2(serializers.Serializer):
    nombre=serializers.CharField()
    apellido_paterno=serializers.CharField()
    correo=serializers.SerializerMethodField()

    def get_correo(self,obj):
        return str(obj.nombre.lower())+"."+str(obj.apellido_paterno.lower())+"."+str(obj.apellido_materno[0].lower())+"@gmail.com"

#Serializador de estudios
class EstudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudios
        fields=('id',
        'nombre_carrera',
        'nivel_estudios',
        'promedio',
        'estudiante')
#----------------------------------------------------------------------------------------------
#SERIALIZER.SERIALIZAR
#serializador con metodo(managers )
class PersonaSerializerCount(serializers.Serializer):
    apellido_paterno=serializers.CharField()
    cantidad=serializers.IntegerField()
#-----------------------------------------------------------------------------------------------
#Serializador relacional
class Estudios_Persona(serializers.ModelSerializer):
    estudiante=PersonaSerializer()
    class Meta:
        model=Estudios
        fields=('id',
        'nombre_carrera',
        'nivel_estudios',
        'promedio',
        'estudiante')

#Serializador con hiperlink
class Estudios_Personalink(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Estudios
        fields=('id',
        'nombre_carrera',
        'nivel_estudios',
        'promedio',
        'estudiante')
        extra_kwargs={
            'estudiante':{'view_name': 'app1_app:buscar_persona', 'lookup_field':'pk'}
        }


#-----------------------------------------------------------------------------------------------
#Paginacion
class PersonPagination(pagination.PageNumberPagination):
    page_size=5
    max_page_size=100
#-----------------------------------------------------------------------------------------------

