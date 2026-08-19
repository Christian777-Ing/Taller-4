"""
Views for the actividades app.
Handles HTTP requests and responses.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from actividades.serializers import ActividadSerializer
from actividades.firebase_service import FirebaseService


def actividades_dashboard(request):
    return render(request, 'actividades/index.html')


class ActividadListCreateView(APIView):
    """
    API endpoint for listing all activities and creating new ones.
    GET: Returns all activities
    POST: Creates a new activity
    """

    def get(self, request):
        """
        Retrieve all activities from Firebase.
        """
        try:
            firebase_service = FirebaseService()
            actividades = firebase_service.get_all_actividades()
            
            serializer = ActividadSerializer(actividades, many=True)
            return Response(
                {
                    'status': 'success',
                    'message': f'Se encontraron {len(actividades)} actividades',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    'status': 'error',
                    'message': f'Error al recuperar actividades: {str(e)}'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        """
        Create a new activity in Firebase.
        Expected JSON body:
        {
            "titulo": "string",
            "descripcion": "string",
            "responsable": "string"
        }
        """
        serializer = ActividadSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {
                    'status': 'error',
                    'message': 'Datos inválidos',
                    'errors': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            firebase_service = FirebaseService()
            nueva_actividad = firebase_service.create_actividad(serializer.validated_data)
            
            return Response(
                {
                    'status': 'success',
                    'message': 'Actividad creada exitosamente',
                    'data': nueva_actividad
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {
                    'status': 'error',
                    'message': f'Error al crear actividad: {str(e)}'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ActividadDetailView(APIView):
    """
    API endpoint for retrieving, updating, and deleting a specific activity.
    GET: Returns a specific activity
    PUT: Updates a specific activity
    DELETE: Deletes a specific activity
    """

    def get(self, request, activity_id):
        """
        Retrieve a specific activity by ID.
        """
        try:
            firebase_service = FirebaseService()
            actividad = firebase_service.get_actividad(activity_id)
            
            if actividad is None:
                return Response(
                    {
                        'status': 'error',
                        'message': f'Actividad con ID {activity_id} no encontrada'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = ActividadSerializer(actividad)
            return Response(
                {
                    'status': 'success',
                    'message': 'Actividad recuperada exitosamente',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    'status': 'error',
                    'message': f'Error al recuperar actividad: {str(e)}'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, activity_id):
        """
        Update a specific activity.
        """
        try:
            firebase_service = FirebaseService()
            actividad = firebase_service.get_actividad(activity_id)
            
            if actividad is None:
                return Response(
                    {
                        'status': 'error',
                        'message': f'Actividad con ID {activity_id} no encontrada'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = ActividadSerializer(data=request.data)
            
            if not serializer.is_valid():
                return Response(
                    {
                        'status': 'error',
                        'message': 'Datos inválidos',
                        'errors': serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            actividad_actualizada = firebase_service.update_actividad(
                activity_id,
                serializer.validated_data
            )
            
            return Response(
                {
                    'status': 'success',
                    'message': 'Actividad actualizada exitosamente',
                    'data': actividad_actualizada
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    'status': 'error',
                    'message': f'Error al actualizar actividad: {str(e)}'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, activity_id):
        """
        Delete a specific activity.
        """
        try:
            firebase_service = FirebaseService()
            deleted = firebase_service.delete_actividad(activity_id)
            
            if not deleted:
                return Response(
                    {
                        'status': 'error',
                        'message': f'Actividad con ID {activity_id} no encontrada'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            return Response(
                {
                    'status': 'success',
                    'message': 'Actividad eliminada exitosamente'
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                {
                    'status': 'error',
                    'message': f'Error al eliminar actividad: {str(e)}'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
