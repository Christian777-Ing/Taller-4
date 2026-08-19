"""
Tests for the actividades app.
"""
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class ActividadAPITestCase(TestCase):
    """Test cases for Actividad API endpoints."""

    def setUp(self):
        """Set up test client."""
        self.client = APIClient()
        self.base_url = '/api/v1/actividades/'

    def test_get_all_actividades(self):
        """Test retrieving all activities."""
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.data)

    def test_create_actividad(self):
        """Test creating a new activity."""
        data = {
            'titulo': 'Test Activity',
            'descripcion': 'This is a test activity',
            'responsable': 'Test User'
        }
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('data', response.data)

    def test_create_actividad_missing_fields(self):
        """Test creating activity with missing required fields."""
        data = {
            'titulo': 'Test Activity'
        }
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
