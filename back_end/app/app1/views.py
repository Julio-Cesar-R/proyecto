#---------------------------------------LIBRERIAS---------------------------------------------
#BASE DE DATOS Demostracion
from .models import Persona
# Create your views here.

#--------------------------------SERIALIZERS VIEWS----------------------------------
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
    
    
    )

from .serializers import (
    PersonaSerializer,
    PersonaSerializer2,
    PersonaSerializerCount,
    PersonPagination
)

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

class PersonaAPISSView(ListAPIView):
    serializer_class=PersonaSerializer2
    pagination_class=PersonPagination
    def get_queryset(self):
        return Persona.objects.buscar_apellido()

class PersonaAPISSCount(ListAPIView):
    serializer_class=PersonaSerializerCount
    def get_queryset(self):
        
        return Persona.objects.cantidad_apellidos_paternos()