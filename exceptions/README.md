# Manejo de excepciones

El proyecto incluye tres excepciones personalizadas:

- `CostoInvalidoError`: aparece si el costo es cero o negativo.
- `ServicioNoEncontradoError`: aparece al buscar, actualizar o eliminar un ID inexistente.
- `ServicioDuplicadoError`: evita registrar dos veces el mismo servicio.

Para ejecutar los casos de estudio, desde la carpeta principal:

```bash
python exceptions/ejemplos_excepciones.py
```

Mensajes esperados:

```text
Caso 1: El costo debe ser mayor a cero. Valor recibido: -200.0
Caso 2: No se encontró el servicio con ID 999
```

