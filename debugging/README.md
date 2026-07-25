# Debugging con pdb

Se colocó `pdb.set_trace()` antes de validar un servicio y antes de buscar un
registro en la base de datos. Así se pueden inspeccionar los valores antes de
que se ejecute la función crítica.

Ejecutar:

```bash
python debugging/debug_servicio.py
```

Comandos utilizados:

- `p servicio`: muestra el objeto y sus valores.
- `p servicio.costo`: inspecciona el costo.
- `n`: avanza a la siguiente línea.
- `s`: entra a la función que se va a ejecutar.
- `c`: continúa hasta terminar.
- `q`: sale del depurador.

Ejemplo de salida:

```text
> debug_servicio.py(9)revisar_servicio()
-> servicio.validar()
(Pdb) p servicio.costo
1200
(Pdb) n
Servicio válido: Servicio(...)
```

Durante la revisión se comprobó que el costo llegaba como número y que los
campos obligatorios no estaban vacíos. Esto permitió confirmar que la
validación se ejecutaba con los datos correctos.

