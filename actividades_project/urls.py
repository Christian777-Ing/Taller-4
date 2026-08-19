"""
URL configuration for actividades_project project.
"""
from django.urls import path, include
from actividades.views import actividades_dashboard

urlpatterns = [
    path("", actividades_dashboard, name="actividades-dashboard"),
    path("actividades-dashboard/", actividades_dashboard, name="actividades-dashboard-page"),
    path("api/", include(("actividades.urls", "actividades"), namespace="actividades")),
]