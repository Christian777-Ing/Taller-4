"""
Serializers for the actividades app.
Converts between JSON and Python objects.
"""
from rest_framework import serializers
from datetime import datetime


class ActividadSerializer(serializers.Serializer):
    """Serializer for Actividad model."""
    id = serializers.CharField(read_only=True, required=False)
    titulo = serializers.CharField(max_length=255, required=True)
    descripcion = serializers.CharField(required=True)
    responsable = serializers.CharField(max_length=255, required=True)
    fecha_creacion = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create a new Actividad instance.
        This method is called by the view when processing POST requests.
        """
        return validated_data

    def update(self, instance, validated_data):
        """
        Update an existing Actividad instance.
        """
        instance.update(validated_data)
        return instance
