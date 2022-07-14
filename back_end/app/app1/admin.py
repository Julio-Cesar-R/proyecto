from django.contrib import admin

# Register your models here.
from .models import Persona,Estudios
admin.site.register(Persona)
admin.site.register(Estudios)

