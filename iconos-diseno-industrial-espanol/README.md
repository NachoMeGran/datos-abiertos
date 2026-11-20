# Iconos del diseño industrial español del siglo XX

Doce objetos de diseño industrial español del siglo XX, de la silla Pedrera (1955) a la silla Toledo (1988), con año, autoría, fabricantes, premios y una columna que precisa **qué parte es española**: el diseño, el desarrollo técnico, la fabricación o todo a la vez.

Es una lista corta a propósito. Solo entran objetos cuya ficha he podido leer en el catálogo de un museo: once en el [Museu del Disseny de Barcelona](https://cataleg.museudeldisseny.cat/) y uno, la Montesa Impala, en el Museu de la Ciència i de la Tècnica de Catalunya (mNACTEC). Prefiero doce registros que aguanten una revisión a cincuenta copiados de listas de internet.

## Archivos

| Archivo | Contenido |
|---|---|
| [`iconos-diseno-industrial-espanol.csv`](iconos-diseno-industrial-espanol.csv) | Datos en CSV (UTF-8, separador coma). |
| [`iconos-diseno-industrial-espanol.json`](iconos-diseno-industrial-espanol.json) | Los mismos registros en JSON; vacíos como `null`. |
| [`datapackage.json`](datapackage.json) | Descriptor [Frictionless Data](https://specs.frictionlessdata.io/) con el esquema. |

## Diccionario de datos

| Columna | Tipo | Obligatoria | Significado |
|---|---|---|---|
| `id` | texto | sí | Identificador estable (`minipimer-mr1`, `lampara-tmc`…). |
| `objeto` | texto | sí | Tipo de objeto. |
| `modelo` | texto | sí | Nombre del modelo. |
| `anio` | entero | sí | Año de diseño o datación que da la ficha del museo. |
| `disenador` | texto | sí | Autoría según la fuente principal; varias personas, separadas por punto y coma. |
| `fabricante_original` | texto | no | Primer productor documentado. Vacío si la ficha no lo identifica. |
| `produccion_original` | texto | sí | Lugar y periodo de la primera producción (o del diseño, si no hay más datos). |
| `otros_fabricantes` | texto | no | Productores y reediciones posteriores que recoge la ficha. |
| `categoria` | texto (lista cerrada) | sí | `mobiliario`, `mobiliario urbano`, `iluminación`, `menaje`, `pequeño electrodoméstico` o `vehículo`. |
| `premios` | texto | no | Premios o selecciones que cita la ficha (Delta ADI-FAD y otros). |
| `que_es_espanol` | texto | sí | Qué parte del objeto es española. |
| `coleccion` | texto | sí | Museo que conserva y documenta el objeto. |
| `numero_registro` | texto | no | Número de registro en la colección, si se publica. |
| `url_fuente` | URL | sí | Ficha del museo usada como fuente principal. |
| `url_fuente_2` | URL | no | Fuente complementaria. |
| `url_nachomg` | URL | no | Artículo relacionado en nachomg.com. |
| `nota` | texto | no | Precisiones y discrepancias entre fuentes. |

## Metodología

1. Elegí objetos que la propia literatura del museo considera emblemáticos del diseño industrial en España y comprobé que estuvieran catalogados con ficha pública.
2. Copié de cada ficha el año, la autoría, los productores con sus fechas y los premios. No he añadido datos que la ficha no diga.
3. La columna `que_es_espanol` resume lo que dice la ficha sobre dónde se diseñó y fabricó el objeto.
4. Cuando otra institución seria da una versión distinta, la anoto en `nota` y la explico abajo.

## Dos casos que merecen explicación

### Minipimer MR1 (1959)

La ficha del Museu del Disseny (MADB 135611) atribuye el diseño a Gabriel Lluelles i Rabadà y la producción a **Industrias Pimer**, en Esplugues de Llobregat, de 1959 a c. 1969, y la describe como la primera batidora eléctrica de mano del mercado español. Según la [biografía de Lluelles en la Viquipèdia](https://ca.wikipedia.org/wiki/Gabriel_Lluelles_Rabad%C3%A0), que remite al antiguo Disseny Hub Barcelona, Lluelles trabajó en Pimer de 1947 a 1962 y, de 1962 a 1970, dirigió el Departamento de Desarrollo y Construcción de **Braun Española, S. A.**, la empresa que nació de la fusión de Industrias Pimer con Braun AG en 1962. La evolución del modelo, la Minipimer MR2 de 1964, ya figura en el museo como producción de Braun Española (Esplugues, 1964-1984; [ficha MADB 135438](https://cataleg.museudeldisseny.cat/detall/madb/H294073)). El [mNACTEC](https://mnactec.cat/en/the-museum/press-detail/exhibition-gabriel-lluelles-industrial-designer) le dedicó la exposición «Gabriel Lluelles, industrial designer» (abierta hasta el 13 de enero de 2026), que recuerda que diseñó 33 electrodomésticos para Pimer, Braun y Taurus.

Escribí sobre ella en [«Minipimer: historia de un icono del diseño»](https://nachomg.com/minipimer-de-gabriel-lluelles/).

### Braun Citromatic MPZ-2 (1970)

Es alemana por la marca y española por buena parte de su origen, y las fuentes serias no cuentan lo mismo:

- **Museu del Disseny de Barcelona** ([ficha MADB 135610](https://cataleg.museudeldisseny.cat/detall/madb/H300347)): diseño de Gabriel Lluelles y Dieter Rams, producción de **Braun Española** en Esplugues de Llobregat de 1970 a 1994, Delta de Oro ADI-FAD 1970. Según el texto de la ficha (firmado por Andrés Alfaro-Hoffmann), a mediados de 1969 se acordó que el nuevo exprimidor se proyectaría y fabricaría en Barcelona, sin intervención de Braun AG, por el Departamento de Desarrollo y Construcción de Braun Española que dirigía Lluelles; una vez hecho el prototipo, el equipo de Dieter Rams rediseñó la forma exterior. Braun Española fabricaba para España y los países de habla hispana y enviaba el resto a Alemania para su distribución mundial.
- **Victoria and Albert Museum** ([ficha CIRC.344 to D-1974](https://collections.vam.ac.uk/item/O1227044/)): atribuye el diseño a Dieter Rams y Jürgen Greubel, sitúa el diseño en Kronberg en 1972 y la fabricación en Barcelona en 1972-1974, y lo describe como pensado para el mercado español.
- **Acción Cultural Española**, en la ficha de la exposición «Tapas. Spanish Design for Food» publicada en [Google Arts & Culture](https://artsandculture.google.com/asset/citromatic-mpz-2-citrus-juicer/dgGr60dRaJO4cg), da Dieter Rams y Gabriel Lluelles, 1970, inventado en España.

En el conjunto sigo al Museu del Disseny, que documenta el proceso con más detalle y conserva un ejemplar donado por el propio Lluelles, y dejo constancia de la versión del V&A. Lo que sí coinciden en afirmar todas: **se fabricó en Barcelona**. No he podido localizar el artículo de El Español (sección La Jungla, 2021) sobre el origen español del exprimidor, así que no lo cito.

Conté la historia en [«Exprimidor Braun Citromatic: la historia de un clásico»](https://nachomg.com/exprimidor-braun-citromatic/).

## Fuentes

- Museu del Disseny de Barcelona, [catálogo en línea de la colección](https://cataleg.museudeldisseny.cat/). Una ficha por objeto, enlazada en `url_fuente`.
- Victoria and Albert Museum, [MPZ 2, juicer](https://collections.vam.ac.uk/item/O1227044/).
- mNACTEC, [Montesa Impala 175](https://artsandculture.google.com/asset/motorcycle-montesa-impala-175/KAGjJr5LrnJ8Uw) en Google Arts & Culture, y [nota de prensa de la exposición sobre Gabriel Lluelles](https://mnactec.cat/en/the-museum/press-detail/exhibition-gabriel-lluelles-industrial-designer).
- Acción Cultural Española, fichas de [la aceitera antigoteo](https://artsandculture.google.com/asset/aceitera-antigoteo/kQErLT_Q1LFZzQ) y [el Citromatic MPZ-2](https://artsandculture.google.com/asset/citromatic-mpz-2-citrus-juicer/dgGr60dRaJO4cg) en Google Arts & Culture.

Los textos del catálogo del Museu del Disseny se publican con licencia CC BY-NC-ND; aquí solo se reproducen datos factuales (fechas, nombres, premios) y paráfrasis breves, con enlace a cada ficha.

## Limitaciones

- La muestra es pequeña y está sesgada hacia Cataluña, porque la colección pública de diseño de producto más completa del país está en Barcelona. Faltan objetos importantes que no he podido verificar en una ficha de museo.
- La Montesa Impala procede de la ficha del mNACTEC, que menciona el Delta de Oro sin año.
- La silla Pedrera se diseñó para un edificio concreto; la ficha no identifica al fabricante de la serie original y solo documenta la reedición de Galeria H2O desde 1995.
- Las fechas son las de la ficha (año de diseño o de datación del ejemplar). Otras fuentes dan años distintos para algunos objetos, por ejemplo 1958 o 1961 para la TMC.
- De Braun solo entra el Citromatic MPZ-2, por su vínculo documentado con Braun Española; otros productos de Braun AG diseñados en Alemania quedan fuera.

## Fecha de corte

20 de noviembre de 2026. Fichas consultadas en esa fecha.

## Cómo citar

> Menéndez Granda, N. (2026). *Iconos del diseño industrial español del siglo XX* (versión 0.9.0) [Conjunto de datos]. Datos abiertos de Nacho MG. https://github.com/NachoMeGran/datos-abiertos/tree/main/iconos-diseno-industrial-espanol. Licencia CC BY 4.0.

Más sobre objetos y diseño en la guía de [diseño de producto](https://nachomg.com/diseno-de-producto/).
