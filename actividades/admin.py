"""
Admin configuration for the actividades app.
"""
from django.contrib import admin
from actividades.models import Actividad


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'responsable', 'fecha_creacion')
    list_filter = ('fecha_creacion', 'responsable')
    search_fields = ('titulo', 'descripcion', 'responsable')
    readonly_fields = ('id', 'fecha_creacion')
