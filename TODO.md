# TODO

1. Implementar el resto de metodos de la API
2. Obtener los listados de equivalencias de vias
3. Obtener los tipos de error de la API
4. Realizar cientos de peticiones masivas a la API hasta:
  * Conseguir la respuesta de errores, y modelarla segun models.py
  * Aproximarnos al rate limit, y configurar el objeto para que no se supere, por defecto.
5. Mejorar el method chaining, para conseguir combinaciones faciles de concatenaciones. Ejemplos:
  * Obtener las provincias, sus municipios, y sus calles con 3 encadenamientos de metodos
  * Obtener datos de unas fincas, y posteriormente obtener sus coordenadas geograficas
6. Los metodos de GEO, permitir los distintos EPSG usando un ENUM (para que asi no se salgan de los requeridos)
7. (Si se puede), descartar *requests* y utilizar urllib de la libreria estandar
