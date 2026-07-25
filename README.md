# Sistema CRUD del taller mecánico

Proyecto de la Unidad 4 desarrollado con Python, Tkinter, MySQL, programación
orientada a objetos y separación de responsabilidades basada en SOLID.

## Estructura

- `CRUD`: entidad, repositorio, controlador, interfaz, `main.py` y script SQL.
- `tests`: pruebas unitarias con pytest y patrón AAA.
- `exceptions`: excepciones personalizadas y casos de estudio.
- `debugging`: ejemplos y documentación de pdb.

## 1. Preparar la base de datos

1. Inicia Apache y MySQL desde XAMPP.
2. Abre `http://localhost/phpmyadmin`.
3. Selecciona **Importar**.
4. Elige `CRUD/db_taller.sql` y presiona **Importar**.

La conexión usa estos datos:

```text
host: localhost
usuario: root
contraseña: vacía
base de datos: taller_mecanico
```

Si tu MySQL tiene contraseña, cambia el valor de `password` en el constructor
de `RepositorioServicios`, dentro de `CRUD/repositorio_servicios.py`.

## 2. Instalar dependencias

Abre una terminal dentro de `proyecto_u4` y ejecuta:

```bash
python -m pip install -r requirements.txt
```

## 3. Ejecutar la aplicación

Desde la carpeta `proyecto_u4`:

```bash
python -m CRUD.main
```

La interfaz permite registrar, consultar, actualizar y eliminar servicios.

## 4. Ejecutar las pruebas

```bash
pytest -v
```

Las pruebas no modifican la base de datos real porque usan datos simulados.

## Principios SOLID aplicados

- Responsabilidad única: cada clase tiene una función específica.
- Abierto/cerrado: se pueden agregar nuevas validaciones o repositorios.
- Sustitución: el repositorio real puede cambiarse por uno falso en pruebas.
- Segregación: el controlador solo utiliza las operaciones necesarias.
- Inversión de dependencias: el controlador recibe el repositorio desde fuera.

## Git sugerido

```bash
git init
git add .
git commit -m "Crear estructura inicial del proyecto"
git commit -am "Agregar CRUD de servicios"
git commit -am "Agregar pruebas, excepciones y debugging"
```
