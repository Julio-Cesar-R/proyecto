#---------------------------------------LIBRERIAS---------------------------------------------
#BASE DE DATOS Demostracion
from re import A
from .models import Demostracion
# Create your views here.
#IMPORTAR FORMS
from .forms import DemostracionForm,PersonaForm
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
#VISTA LISTA CON API
#-----------------------------------------------

class Lista_personasListView(ListView):
 
    template_name = "app1/lista_personas.html"
    context_object_name="personas"

    def get_queryset(self):
        url="http://127.0.0.1:8000/persona/api_view/"
        respuesta=apilist(url)
        return respuesta


class ConsultaApi(ListView):
    #Template donde se pintara la informacion
    template_name= "app1/consulta.html"
    context_object_name= "consulta"
    
    def get_queryset(self):
        url="http://127.0.0.1:8000/estudios_persona/api_view/"
        respuesta=apilist(url)
        return respuesta


#VISTA DETALLE CON API
class DetalleListView(ListView):
    context_object_name="persona"
    template_name = "app1/vistadetalle.html"
    def get_queryset(self):
        clave=self.kwargs["pk"]
        respuesta=api_detail(clave)
        print("------------------------")
        print(respuesta)

        return respuesta


#VISTA CREATE CON API
class CrearPersonaCreateView(FormView):
    form_class=PersonaForm
    template_name = "app1/persona_create.html"
    success_url=reverse_lazy("app1_app:consulta_api_post")
    def form_valid(self,form):
        '''
        recupera la informacion del formulario 
        y lo ingresa en dos tablas diferentes
        '''
       
    
        name=form.cleaned_data["nombre"],
        apellido_p=form.cleaned_data["apellido_paterno"],
        apellido_m=form.cleaned_data["apellido_materno"],
        edad=form.cleaned_data["edad"],
        email=form.cleaned_data["email"],
        telefono=form.cleaned_data["telefono"],
        

        respuesta=api_create("".join(name),
                            "".join(apellido_p),
                            "".join(apellido_m),
                            int(''.join(map(str, edad))),
                            "".join(email),
                            "".join(telefono))
        return super(CrearPersonaCreateView,self).form_valid(form)
  
