"""
URL configuration for the actividades app.
"""
from django.urls import path
from actividades.views import ActividadListCreateView, ActividadDetailView

app_name = 'actividades'

urlpatterns = [
    # GET all activities or POST a new activity
    path('actividades/', ActividadListCreateView.as_view(), name='actividad-list-create'),
    
    # GET, PUT, DELETE a specific activity
    path('actividades/<str:activity_id>/', ActividadDetailView.as_view(), name='actividad-detail'),
]
