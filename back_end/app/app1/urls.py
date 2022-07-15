#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria path
from django.urls import path


#Importar el archivo donde se encuentran las vistas
from .  import views
#----------------------------------------------------------------------------------------------

app_name="app1_app"

urlpatterns = [
  
    #Urls APIs genericas
    path('persona/api_view/',views.PersonaAPIView.as_view(), name='listar_personas'),
    path('persona/api_buscar_pk/<pk>/', views.PersonaAPISearch.as_view(), name='buscar_persona'),
    path('persona/api_create/',views.PersonaAPICreatee.as_view(), name='crear_persona'),
    path('persona/api_actualizar/<pk>/',views.PersonaAPIUpdate.as_view(), name='actualizar_persona'),
    path('persona/api_eliminar/<pk>/', views.PersonaAPIDelete.as_view(), name='eliminar_persona'),
#---------------------------------------------------------------------------------------------------
    #Serializadores con metodo
    path('persona/api_view_serializer/', views.PersonaAPISSView.as_view(), name='listar_personas_2'),
    path('persona/api_view_serializer_count/', views.PersonaAPISSCount.as_view(), name='cantidad_apellidos'),
#-------------------------------------------------------------------------------------------------------
    #Serializadores con 2 tablas
    path('estudios/api_view/',views.EstudiosAPPIView.as_view(), name='persona_estudios_create'),
    path('estudios_persona/api_view/',views.Estudios_PersonaAPIView.as_view(), name='estudios_persona_view'),
    path('estudios_persona_link/api_view/', views.PersonakAPIview.as_view(), name='estudios_persona_link'),
]