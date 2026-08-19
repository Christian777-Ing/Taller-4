# Guía Rápida de Inicio

## 1. Preparación del Entorno

### Activar el entorno virtual
```bash
source env/bin/activate
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

## 2. Configurar Firebase

### Opción A: Si tienes un proyecto Firebase existente
1. Ve a [Firebase Console](https://console.firebase.google.com)
2. Selecciona tu proyecto
3. Navega a Project Settings → Service Accounts
4. Haz clic en "Generate New Private Key"
5. Guarda el archivo como `firebase_credentials.json` en la raíz del proyecto
6. Copia tu Database URL desde Realtime Database

### Opción B: Crear un nuevo proyecto Firebase (si no tienes uno)
1. Ve a [Firebase Console](https://console.firebase.google.com)
2. Haz clic en "Add Project"
3. Sigue los pasos para crear un nuevo proyecto
4. Habilita Realtime Database en Develop → Realtime Database
5. Descarga las credenciales como se describe en la Opción A

### Actualizar archivo `.env`
```bash
# Copia del archivo .env.example a .env
cp .env.example .env

# Edita .env y actualiza:
FIREBASE_DATABASE_URL=https://tu-proyecto.firebaseio.com
```

## 3. Ejecutar el Servidor

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`

## 4. Probar los Endpoints

### Crear una actividad
```bash
curl -X POST http://localhost:8000/api/v1/actividades/ \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Mi Primera Actividad",
    "descripcion": "Descripción de la actividad",
    "responsable": "Tu Nombre"
  }'
```

### Listar todas las actividades
```bash
curl http://localhost:8000/api/v1/actividades/
```

## 5. Estructura de Respuestas

### Respuesta exitosa (GET all)
```json
{
    "status": "success",
    "message": "Se encontraron X actividades",
    "data": [
        {
            "id": "id_generado_firebase",
            "titulo": "Título",
            "descripcion": "Descripción",
            "responsable": "Responsable",
            "fecha_creacion": "2024-01-15T10:30:00"
        }
    ]
}
```

### Respuesta exitosa (POST)
```json
{
    "status": "success",
    "message": "Actividad creada exitosamente",
    "data": {
        "id": "id_generado_firebase",
        "titulo": "Título",
        "descripcion": "Descripción",
        "responsable": "Responsable",
        "fecha_creacion": "2024-01-15T10:30:00"
    }
}
```

## 6. Troubleshooting

### Error: "Firebase credentials file not found"
- Verifica que `firebase_credentials.json` está en la raíz del proyecto
- Verifica que la ruta en `.env` es correcta

### Error: "Couldn't import Django"
- Asegúrate de haber activado el entorno virtual: `source env/bin/activate`
- Instala las dependencias: `pip install -r requirements.txt`

### Error: "Connection refused" (Firebase)
- Verifica que tu Database URL es correcta en `.env`
- Verifica que Firebase Realtime Database está habilitada en tu proyecto

### Port 8000 already in use
```bash
python manage.py runserver 8080  # Usar un puerto diferente
```

## 7. Próximos Pasos

- Implementar autenticación (JWT tokens)
- Agregar validación de datos más robusta
- Implementar paginación
- Agregar filtros y búsqueda
- Implementar CORS para aplicaciones web/móviles
- Agregar documentación interactiva con Swagger/OpenAPI
- Tests más completos

## 8. Recursos Útiles

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Firebase Admin Python SDK](https://firebase.google.com/docs/database/admin/start)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

**¡Listo para empezar! 🚀**
