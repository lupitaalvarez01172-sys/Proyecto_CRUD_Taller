# Pruebas unitarias

Las pruebas usan un repositorio falso para ser rápidas, aisladas y repetibles;
por eso no necesitan que MySQL esté encendido. Todas siguen el patrón AAA:
Arrange, Act y Assert.

Desde la carpeta principal del proyecto ejecuta:

```bash
pytest -v
```

Se comprueban costos válidos, datos obligatorios, registros duplicados y las
operaciones de registrar, consultar, actualizar y eliminar.

