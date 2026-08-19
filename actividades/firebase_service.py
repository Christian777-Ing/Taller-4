"""
Firebase Realtime Database service module.
Handles all CRUD operations with Firebase.
"""
import firebase_admin
from firebase_admin import credentials, db
from django.conf import settings
from datetime import datetime
import json
import os


class FirebaseService:
    """Service to interact with Firebase Realtime Database."""

    _instance = None

    def __new__(cls):
        """Singleton pattern to ensure only one Firebase app is initialized."""
        if cls._instance is None:
            cls._instance = super(FirebaseService, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize Firebase Admin SDK."""
        cred_path = settings.FIREBASE_CREDENTIALS
        
        if not os.path.exists(cred_path):
            raise FileNotFoundError(
                f"Firebase credentials file not found at {cred_path}. "
                "Please download it from Firebase Console and place it in the project root."
            )

        try:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(
                cred,
                {'databaseURL': settings.FIREBASE_CONFIG['DATABASE_URL']}
            )
        except ValueError:
            # Firebase app already initialized
            pass

    def create_actividad(self, actividad_data):
        """
        Create a new activity in Firebase.
        
        Args:
            actividad_data (dict): Dictionary containing titulo, descripcion, responsable
            
        Returns:
            dict: Created activity with id and fecha_creacion
        """
        ref = db.reference('actividades')
        
        # Create new activity with timestamp
        nueva_actividad = {
            'titulo': actividad_data.get('titulo'),
            'descripcion': actividad_data.get('descripcion'),
            'responsable': actividad_data.get('responsable'),
            'fecha_creacion': datetime.now().isoformat()
        }
        
        # Push new child to Firebase (generates unique ID)
        new_ref = ref.push(nueva_actividad)
        nueva_actividad['id'] = new_ref.key
        
        return nueva_actividad

    def get_all_actividades(self):
        """
        Retrieve all activities from Firebase.
        
        Returns:
            list: List of all activities with their IDs
        """
        ref = db.reference('actividades')
        data = ref.get()
        
        if data is None:
            return []
        
        actividades = []
        for activity_id, activity_data in data.items():
            activity_data['id'] = activity_id
            actividades.append(activity_data)
        
        return actividades

    def get_actividad(self, activity_id):
        """
        Retrieve a single activity by ID.
        
        Args:
            activity_id (str): The ID of the activity
            
        Returns:
            dict: Activity data or None if not found
        """
        ref = db.reference(f'actividades/{activity_id}')
        data = ref.get()
        
        if data is None:
            return None
        
        data['id'] = activity_id
        return data

    def update_actividad(self, activity_id, actividad_data):
        """
        Update an existing activity.
        
        Args:
            activity_id (str): The ID of the activity
            actividad_data (dict): Updated data
            
        Returns:
            dict: Updated activity data or None if not found
        """
        ref = db.reference(f'actividades/{activity_id}')
        
        if ref.get() is None:
            return None
        
        ref.update(actividad_data)
        actividad_data['id'] = activity_id
        return actividad_data

    def delete_actividad(self, activity_id):
        """
        Delete an activity.
        
        Args:
            activity_id (str): The ID of the activity
            
        Returns:
            bool: True if deleted successfully, False if not found
        """
        ref = db.reference(f'actividades/{activity_id}')
        
        if ref.get() is None:
            return False
        
        ref.delete()
        return True
