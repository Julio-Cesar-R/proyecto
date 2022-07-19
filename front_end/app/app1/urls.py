#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria path
from django.urls import path


#Importar el archivo donde se encuentran las vistas
from .  import views
#----------------------------------------------------------------------------------------------

app_name="app1_app"

urlpatterns = [
    #Urls Template view (pagina comun) 
    path('demostracion/', views.DemostracionCreateView.as_view(), name='create_demostracion'),
    path('consulta_api/', views.ConsultaApi.as_view(), name='consulta_api'),
    path('consulta_api_detalle/<pk>',views.DetalleListView.as_view(), name='consulta_api_detalle'),
    path('consulta_api_post/', views.CrearPersonaCreateView.as_view(), name='consulta_api_post'),
    path('consulta_api_personas/', views.Lista_personasListView.as_view(), name='consulta_api_personas'),
    
  
]