# Actividades API - Django REST Framework + Firebase

API REST para la gestión de actividades académicas utilizando Django REST Framework y Firebase Realtime Database.

## Estructura del Proyecto

```
Taller-4/
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── firebase_credentials.json       # Firebase credentials (not included in repo)
├── actividades_project/           # Django project folder
│   ├── __init__.py
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Project URL configuration
│   └── wsgi.py                   # WSGI application
└── actividades/                  # Django app for activities
    ├── __init__.py
    ├── models.py                 # Data models
    ├── serializers.py            # DRF serializers
    ├── views.py                  # API views
    ├── urls.py                   # App URL configuration
    ├── firebase_service.py       # Firebase integration
    ├── apps.py                   # App configuration
    ├── admin.py                  # Django admin
    └── tests.py                  # Unit tests
```

## Requisitos Previos

- Python 3.8+
- Virtual environment (ya incluido en `env/`)
- Cuenta de Firebase con Realtime Database

## Instalación

### 1. Activar el entorno virtual

```bash
source env/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar Firebase

1. Descarga las credenciales de Firebase desde la consola de Firebase
2. Guarda el archivo como `firebase_credentials.json` en la raíz del proyecto
3. Actualiza las variables de entorno en tu `.env`:

```bash
FIREBASE_DATABASE_URL=https://tu-proyecto.firebaseio.com
FIREBASE_CREDENTIALS_PATH=firebase_credentials.json
```

### 4. Ejecutar el servidor

```bash
python manage.py runserver
```

El servidor estará disponible en `http://localhost:8000`

## Endpoints de la API

### Base URL
```
http://localhost:8000/api/v1/
```

### 1. Listar todas las actividades

**Solicitud:**
```bash
GET /actividades/
```

**Respuesta exitosa (200):**
```json
{
    "status": "success",
    "message": "Se encontraron 2 actividades",
    "data": [
        {
            "id": "abc123",
            "titulo": "Taller de Python",
            "descripcion": "Introducción a Python",
            "responsable": "Juan Pérez",
            "fecha_creacion": "2024-01-15T10:30:00"
        },
        {
            "id": "def456",
            "titulo": "Seminario de Bases de Datos",
            "descripcion": "Diseño de bases de datos relacionales",
            "responsable": "María García",
            "fecha_creacion": "2024-01-16T14:45:00"
        }
    ]
}
```

### 2. Crear una nueva actividad

**Solicitud:**
```bash
POST /actividades/
Content-Type: application/json

{
    "titulo": "Taller de Python",
    "descripcion": "Introducción a Python",
    "responsable": "Juan Pérez"
}
```

**Respuesta exitosa (201):**
```json
{
    "status": "success",
    "message": "Actividad creada exitosamente",
    "data": {
        "id": "abc123",
        "titulo": "Taller de Python",
        "descripcion": "Introducción a Python",
        "responsable": "Juan Pérez",
        "fecha_creacion": "2024-01-15T10:30:00"
    }
}
```

**Respuesta error (400):**
```json
{
    "status": "error",
    "message": "Datos inválidos",
    "errors": {
        "titulo": ["Este campo es obligatorio."],
        "descripcion": ["Este campo es obligatorio."]
    }
}
```

### 3. Obtener una actividad específica

**Solicitud:**
```bash
GET /actividades/{activity_id}/
```

**Respuesta exitosa (200):**
```json
{
    "status": "success",
    "message": "Actividad recuperada exitosamente",
    "data": {
        "id": "abc123",
        "titulo": "Taller de Python",
        "descripcion": "Introducción a Python",
        "responsable": "Juan Pérez",
        "fecha_creacion": "2024-01-15T10:30:00"
    }
}
```

**Respuesta error (404):**
```json
{
    "status": "error",
    "message": "Actividad con ID abc123 no encontrada"
}
```

### 4. Actualizar una actividad

**Solicitud:**
```bash
PUT /actividades/{activity_id}/
Content-Type: application/json

{
    "titulo": "Taller de Python Avanzado",
    "descripcion": "Programación orientada a objetos en Python",
    "responsable": "Juan Pérez"
}
```

**Respuesta exitosa (200):**
```json
{
    "status": "success",
    "message": "Actividad actualizada exitosamente",
    "data": {
        "id": "abc123",
        "titulo": "Taller de Python Avanzado",
        "descripcion": "Programación orientada a objetos en Python",
        "responsable": "Juan Pérez",
        "fecha_creacion": "2024-01-15T10:30:00"
    }
}
```

### 5. Eliminar una actividad

**Solicitud:**
```bash
DELETE /actividades/{activity_id}/
```

**Respuesta exitosa (204):**
```json
{
    "status": "success",
    "message": "Actividad eliminada exitosamente"
}
```

## Códigos de Estado HTTP

- `200 OK`: La solicitud fue exitosa
- `201 Created`: La actividad fue creada exitosamente
- `204 No Content`: La actividad fue eliminada exitosamente
- `400 Bad Request`: Datos inválidos o campos requeridos faltantes
- `404 Not Found`: La actividad no fue encontrada
- `500 Internal Server Error`: Error en el servidor

## Estructura de Datos

### Actividad

| Campo | Tipo | Descripción | Requerido |
|-------|------|-------------|----------|
| id | string | Identificador único generado por Firebase | No (read-only) |
| titulo | string | Título de la actividad | Sí |
| descripcion | string | Descripción detallada de la actividad | Sí |
| responsable | string | Persona responsable de la actividad | Sí |
| fecha_creacion | datetime | Fecha y hora de creación (ISO 8601) | No (read-only) |

## Testing

Ejecutar las pruebas unitarias:

```bash
python manage.py test actividades
```

## Notas Importantes

1. **Firebase Credentials**: El archivo `firebase_credentials.json` no debe ser incluido en el repositorio. Utiliza variables de entorno para configuraciones sensibles.

2. **Base de Datos**: Esta aplicación utiliza Firebase Realtime Database. Django's SQLite se mantiene para compatibilidad pero los datos principales se almacenan en Firebase.

3. **Seguridad**: En producción:
   - Cambia `SECRET_KEY` en settings.py
   - Establece `DEBUG = False`
   - Configura `ALLOWED_HOSTS` apropiadamente
   - Utiliza variables de entorno para datos sensibles
   - Implementa autenticación y autorización

4. **CORS**: Para consumir esta API desde aplicaciones web/móviles en diferentes dominios, considera instalar `django-cors-headers`.

## Ejemplo de uso con cURL

```bash
# Crear una actividad
curl -X POST http://localhost:8000/api/v1/actividades/ \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Taller de Django",
    "descripcion": "Introducción a Django",
    "responsable": "Carlos López"
  }'

# Listar todas las actividades
curl http://localhost:8000/api/v1/actividades/

# Obtener una actividad específica
curl http://localhost:8000/api/v1/actividades/abc123/

# Actualizar una actividad
curl -X PUT http://localhost:8000/api/v1/actividades/abc123/ \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Taller de Django Avanzado",
    "descripcion": "Patrones y mejores prácticas en Django",
    "responsable": "Carlos López"
  }'

# Eliminar una actividad
curl -X DELETE http://localhost:8000/api/v1/actividades/abc123/
```

## Autor

Christian Ing - Taller 4

## Licencia

MIT
