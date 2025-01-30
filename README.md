# certificacion

## Ejecutar el proyecto

- descargar archivo Jorge_Valdes_0075.zip
- crear un entorno virtual llamado "venv"
- activar el entorno virtual y instalar los siguientes modulos: Django y spycopg2

- descomprimir el archivo Jorge_Valdes_0075.zip
- entrar a la carpeta Jorge_Valdes_0075
- cargar el dump llamado dato.dump en una base de datos postgres llamada "db_final_orm"
- configurar el archivo setting.py del sistema ubicada en certificacion/proyecto/setting.py

``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_final_orm',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
- clave de superusuario y usuario en entorno django es matri
- administrador en entorno jorge clave root
- ejecutar el programa con el siguiente comando python manage.py runserver en certificacion/
- url github https://github.com/Jorge-Valdes-Pinochet/drill_m7.git

## Usuarios por rol





