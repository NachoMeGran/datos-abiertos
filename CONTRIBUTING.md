# Cómo contribuir

Las correcciones son bienvenidas, sobre todo las que vienen con fuente.

## Para proponer una corrección

1. Abre una incidencia (*issue*) indicando el conjunto, el `id` del registro, el campo, el valor actual, el valor propuesto y **un enlace a la fuente** que lo respalda.
2. Si prefieres hacer tú el cambio, envía un *pull request* que modifique a la vez el CSV y el JSON del conjunto y ejecuta antes:

   ```bash
   python3 scripts/validar.py
   ```

   El PR no se aceptará si la validación falla.

## Criterios

- **Fuente primaria o seria.** Textos oficiales (EUR-Lex, BOE, EDPB), fichas de museo, créditos de la propia producción o bases de datos de referencia. No sirven blogs sin fuentes ni contenido generado sin verificar.
- **Nada inventado.** Si un dato no se puede verificar, se deja vacío y se explica en `nota` o en el README.
- **Interpretación separada de los hechos.** Las columnas editoriales (temas de Black Mirror, categorías afines, ejemplos y alternativas) admiten debate: argumenta la propuesta en la incidencia.
- **Español de España** en descripciones y documentación.

Las contribuciones se publican con la misma licencia que el conjunto (CC BY 4.0 para datos y textos; MIT para `scripts/`).
