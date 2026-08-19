"""
Models for the actividades app.
Note: These models are for reference and serialization.
Actual data storage is handled by Firebase Realtime Database.
"""
from django.db import models
from datetime import datetime


class Actividad(models.Model):
    """
    Represents an academic activity.
    Data is stored in Firebase, not in Django's database.
    """
    id = models.CharField(max_length=100, primary_key=True, default='')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    responsable = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'actividades'

    def __str__(self):
        return self.titulo
