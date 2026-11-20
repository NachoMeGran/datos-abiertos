# Black Mirror: tecnología y ética episodio a episodio

Todos los títulos de *Black Mirror* estrenados hasta la fecha de corte: los 33 episodios numerados de las temporadas 1 a 7 (incluido el especial «White Christmas», de 2014) y la película interactiva «Bandersnatch» (2018). En total, 34 registros. Para cada uno: fecha de estreno, guion, dirección, título en España, la tecnología que mueve la trama y los dilemas éticos que plantea, clasificados con una lista cerrada de temas.

Sirve para clases de ética tecnológica, talleres sobre IA y privacidad o para quien quiera recorrer la serie por temas. Yo la uso para buscar el episodio adecuado cuando explico por qué ciertas decisiones de producto tienen consecuencias.

## Archivos

| Archivo | Contenido |
|---|---|
| [`black-mirror.csv`](black-mirror.csv) | Datos en CSV (UTF-8, separador coma). `temas_eticos` separa los temas con punto y coma. |
| [`black-mirror.json`](black-mirror.json) | Los mismos registros en JSON; `temas_eticos` es un array y los vacíos son `null`. |
| [`datapackage.json`](datapackage.json) | Descriptor [Frictionless Data](https://specs.frictionlessdata.io/) con el esquema. |

## Diccionario de datos

| Columna | Tipo | Obligatoria | Significado |
|---|---|---|---|
| `id` | texto | sí | `s01e01`…`s07e06`, `white-christmas` o `bandersnatch`. |
| `tipo` | texto (lista cerrada) | sí | `episodio`, `especial` o `pelicula-interactiva`. |
| `temporada` | entero | no | Temporada (1-7). Vacío en «White Christmas» y «Bandersnatch». |
| `numero` | entero | no | Número dentro de la temporada. Vacío en los dos especiales. |
| `numero_global` | entero | no | Orden global de la lista de Wikipedia en inglés: «White Christmas» es el 7; «Bandersnatch» no lleva número. |
| `titulo_original` | texto | sí | Título original en inglés. |
| `titulo_es` | texto | sí | Título en España según la ficha en español de España (es-ES) de TMDB. Si no se traduce, igual al original. |
| `nota_titulo_es` | texto | no | Discrepancias con Wikipedia en español. |
| `fecha_estreno` | fecha (AAAA-MM-DD) | sí | Primera emisión (Channel 4) o publicación (Netflix). |
| `plataforma_estreno` | texto (lista cerrada) | sí | `Channel 4` (temporadas 1-2 y «White Christmas») o `Netflix` (desde la temporada 3). |
| `guion` | texto | sí | Créditos de guion. Cuando la fuente distingue historia y guion, se indica entre paréntesis. |
| `direccion` | texto | sí | Créditos de dirección. |
| `tecnologia_central` | texto | sí | Descripción breve, mía, de la tecnología o el mecanismo central. |
| `temas_eticos` | lista de texto | sí | Temas de la lista controlada (abajo). |
| `url_analisis_nachomg` | URL | no | Análisis del episodio o de su temporada en nachomg.com. |
| `url_fuente_creditos` | URL | sí | Fuente principal de fechas y créditos. |

### Lista controlada de `temas_eticos`

| Valor | Qué recoge |
|---|---|
| `privacidad` | Exposición de datos, imágenes o vida íntima sin control de la persona. |
| `vigilancia` | Observación sistemática por parte de Estados, empresas, parejas o familias. |
| `identidad-digital` | Copias, avatares o réplicas de una persona y quién controla su imagen. |
| `ia-y-conciencia` | Inteligencias artificiales o copias digitales que parecen sentir; su estatus moral. |
| `castigo-y-justicia` | Castigos, venganzas o justicia ejercida mediante tecnología. |
| `adiccion` | Uso compulsivo, diseño que captura la atención. |
| `consentimiento` | Decisiones tomadas sin consentimiento libre e informado, o con términos que nadie lee. |
| `desinformacion` | Manipulación de la verdad, de la memoria colectiva o del debate público. |
| `desigualdad` | Tecnología que reparte derechos, servicios o dignidad según el dinero o la posición. |
| `memoria` | Grabación, alteración o borrado de recuerdos. |
| `reputacion-y-redes-sociales` | Puntuaciones, viralidad y linchamientos en redes. |
| `espectaculo-y-violencia` | Sufrimiento convertido en entretenimiento o contenido. |
| `duelo-y-muerte` | Tecnologías que prometen prolongar o sustituir a quien ha muerto. |
| `autonomia-y-control` | Sistemas que deciden por las personas o limitan su capacidad de elegir. |
| `guerra-y-deshumanizacion` | Uso militar o policial de la tecnología para deshumanizar al otro. |
| `relaciones-y-sexualidad` | Pareja, deseo e intimidad mediados por tecnología. |
| `poder-corporativo` | Empresas tecnológicas con poder desproporcionado sobre sus usuarios o empleados. |

## Metodología

1. **Lista de títulos y créditos.** Partí de la [lista de episodios de Wikipedia en inglés](https://en.wikipedia.org/wiki/List_of_Black_Mirror_episodes), que cita como referencia general el libro *Inside Black Mirror* (Brooker, Jones y Arnopp, 2018) y prensa especializada para fechas. Contrasté cada fecha, director y guionista con las fichas de [The Movie Database (TMDB)](https://www.themoviedb.org/tv/42009-black-mirror) y con el [anexo de episodios de Wikipedia en español](https://es.wikipedia.org/wiki/Anexo:Episodios_de_Black_Mirror). TMDB coincide con Wikipedia en inglés en las fechas y la dirección de los 34 títulos. En guion, TMDB añade dos créditos de idea original que no recojo en la columna: Chris Morris en «The Waldo Moment» y Penn Jillette en «Black Museum».
2. **Créditos de guion.** Sigo la forma de Wikipedia en inglés. En «Fifteen Million Merits» la coguionista figura en pantalla como Kanak Huq (Konnie Huq). En «Nosedive» y «Common People» distingo historia y guion, como hace la fuente.
3. **Temporada 7.** Seis episodios publicados en Netflix el 10 de abril de 2025: «Common People», «Bête Noire», «Hotel Reverie», «Plaything», «Eulogy» y «USS Callister: Into Infinity».
4. **Títulos en España.** Tomé el título de la ficha es-ES de TMDB, que coincide con el que usan medios españoles para la temporada 7. Cuando Wikipedia en español da otro, lo anoto en `nota_titulo_es`.
5. **Tecnología y temas.** `tecnologia_central` y `temas_eticos` son **interpretación editorial mía**. Asigné de dos a cinco temas por título, empezando por el que considero dominante.
6. **Análisis en nachomg.com.** Enlacé los análisis existentes: «Hang the DJ», «Hated in the Nation», «Bandersnatch» y los artículos de conjunto sobre las temporadas 5 y 6, que se asignan a todos sus episodios.

## Fuentes

- Wikipedia (en), [List of Black Mirror episodes](https://en.wikipedia.org/wiki/List_of_Black_Mirror_episodes), consultada el 20-11-2026, y sus referencias.
- The Movie Database, [Black Mirror](https://www.themoviedb.org/tv/42009-black-mirror) (temporadas 1-7, idioma es-ES y en-US) y [Black Mirror: Bandersnatch](https://www.themoviedb.org/movie/569547-black-mirror-bandersnatch).
- Wikipedia (es), [Anexo:Episodios de Black Mirror](https://es.wikipedia.org/wiki/Anexo:Episodios_de_Black_Mirror).

## Limitaciones

- La clasificación temática y las descripciones de tecnología son una lectura editorial, discutible por definición. Si crees que falta o sobra un tema, abre una incidencia.
- TMDB cuenta «White Christmas» como cuarto episodio de la temporada 2; Wikipedia lo trata como especial. Aquí sigo a Wikipedia.
- Los títulos en España dependen de la ficha es-ES de TMDB, mantenida por su comunidad. No he podido contrastarlos con el catálogo de Netflix España, que exige iniciar sesión. Las diferencias con Wikipedia en español quedan anotadas en `nota_titulo_es`.
- «Demon 79» no gira en torno a ninguna tecnología; se incluye por completitud.
- No incluye audiencias, repartos ni valoraciones.

## Fecha de corte

20 de noviembre de 2026. Cubre hasta la temporada 7 (abril de 2025).

## Cómo citar

> Menéndez Granda, N. (2026). *Black Mirror: tecnología y ética episodio a episodio* (versión 1.0.0) [Conjunto de datos]. Datos abiertos de Nacho MG. https://github.com/NachoMeGran/datos-abiertos/tree/main/black-mirror-tecnologia-y-etica. Licencia CC BY 4.0.

Más análisis de series y cine en la guía de [cultura pop](https://nachomg.com/cultura-pop/).
