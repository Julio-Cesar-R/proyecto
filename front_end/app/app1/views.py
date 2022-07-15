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

import requests,json

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
        respuesta=requests.get("https://jsonplaceholder.typicode.com/posts/1")
        print(f"El codigo de espuesta de la api es {respuesta.status_code}")
        respuesta=json.loads(respuesta.text)
        print("****************")
        print(respuesta)
        print(respuesta["title"])
        return respuesta