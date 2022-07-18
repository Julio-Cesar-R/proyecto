#---------------------------------------LIBRERIAS---------------------------------------------
#BASE DE DATOS Demostracion
from .models import Persona,Estudios
# Create your views here.

#--------------------------------SERIALIZERS VIEWS----------------------------------
#Serializadores vistas genericas
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
    
    
    )
#Serializadores
from .serializers import (
    PersonaSerializer,
    PersonaSerializer2,
    PersonaSerializerCount,
    PersonPagination,
    EstudiosSerializer,
    Estudios_Persona,
    Estudios_Personalink
)
#Serializadores , paginacion y managers
class PersonaAPIView(ListAPIView):
    serializer_class=PersonaSerializer
    pagination_class=PersonPagination
    def get_queryset(self):
         
        return Persona.objects.buscar_todo()
        
class PersonaAPISearch (RetrieveAPIView):
    serializer_class=PersonaSerializer
    queryset=Persona.objects.buscar_todo()
        

class PersonaAPICreatee(CreateAPIView):
    serializer_class=PersonaSerializer

class PersonaAPIUpdate(RetrieveUpdateAPIView):
    
    serializer_class=PersonaSerializer
    queryset=Persona.objects.buscar_todo()

class PersonaAPIDelete(RetrieveDestroyAPIView):
    serializer_class=PersonaSerializer
    queryset=Persona.objects.buscar_todo()
#-------------------------------------------------------------------------------
#Serializador con managers
class PersonaAPISSView(ListAPIView):
    serializer_class=PersonaSerializer2
    pagination_class=PersonPagination
    def get_queryset(self):
        return Persona.objects.buscar_apellido()

class PersonaAPISSCount(ListAPIView):
    serializer_class=PersonaSerializerCount
    def get_queryset(self):
        
        return Persona.objects.cantidad_apellidos_paternos()
#----------------------------------------------------------------------
#Serializador relacional
class EstudiosAPPIView(ListAPIView):
    serializer_class=EstudiosSerializer
    queryset=Persona.objects.all()

class Estudios_PersonaAPIView(ListAPIView):
    pagination_class=PersonPagination
    serializer_class=Estudios_Persona
    queryset=Estudios.objects.all()


class PersonakAPIview(ListAPIView):
    #formato json
    serializer_class=Estudios_Personalink
    queryset=Estudios.objects.all()

#-----------------------------------------------------------------
#CONSULTA DE APIS


