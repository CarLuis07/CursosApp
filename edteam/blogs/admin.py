from django.contrib import admin
from .models import Articulo

# Register your models here.


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen', 'autor', 'fecha_creacion', 'fecha_modificacion')