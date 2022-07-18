#---------------------------------------LIBRERIAS---------------------------------------------
#BASE DE DATOS Demostracion
from .models import Demostracion
# Create your views here.
#IMPORTAR FORMS
from .forms import DemostracionForm
#IMPORTA VISTAS GENERICAS
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView,FormView
#Importa redireccionamiento de urls
from django.urls import reverse_lazy

from .services import *

#-----------------------VISTAS------------------------------------
class DemostracionCreateView(CreateView):
    #Modelo
    model = Demostracion
    #Template
    template_name = "app1/demostracion.html"
    form_class= DemostracionForm
    #Campos
    #fields=["first_name","last_name","job","departamento","departamento","image","habilidades","hoja_vida"]
    #fields=("__all__") 
    success_url=reverse_lazy("app1_app:create_demostracion")
#--------------------------------------------------------------------------------------------
#--------------------------------SERIALIZERS VIEWS----------------------------------
class ConsultaApi(ListView):
    #Template donde se pintara la informacion
    template_name= "app1/consulta.html"
    context_object_name= "consulta"
    
    def get_queryset(self):
        url="http://127.0.0.1:8000/estudios_persona/api_view/"
        respuesta=apilist(url)
        return respuesta



class DetalleListView(ListView):
    context_object_name="persona"
    template_name = "app1/vistadetalle.html"
    def get_queryset(self):
        clave=self.kwargs["pk"]
        respuesta=api_detail(clave)
        print("------------------------")
        print(respuesta)

        return respuesta


