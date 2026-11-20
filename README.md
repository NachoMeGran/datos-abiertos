# Datos abiertos de Nacho MG

Conjuntos de datos pequeños, verificados y reutilizables sobre ética digital, cultura pop y diseño. Cada dato lleva su fuente enlazada, cada conjunto explica su método y sus límites, y un script comprueba que el CSV y el JSON dicen exactamente lo mismo.

Los preparo para mi trabajo como [consultor de marketing digital](https://nachomg.com/consultor-de-marketing-freelance-en-barcelona/) y para mis clases, y los publico porque buena parte de lo que circula sobre estos temas es imposible de rastrear hasta un origen. Si un dato no lo he podido comprobar en una fuente seria, no está.

## Conjuntos

| Carpeta | Qué contiene | Registros |
|---|---|---|
| [`patrones-oscuros/`](patrones-oscuros/) | Taxonomía en español de patrones de diseño engañosos según las Directrices 03/2022 del EDPB (v2.0), el art. 25 y el considerando 67 del Reglamento de Servicios Digitales y el anexo I de la Directiva 2005/29/CE, con ejemplo genérico y alternativa ética. | 35 |
| [`black-mirror-tecnologia-y-etica/`](black-mirror-tecnologia-y-etica/) | Todos los títulos de Black Mirror hasta la temporada 7 (2025), con créditos verificados, título en España, tecnología central y temas éticos. | 34 |
| [`iconos-diseno-industrial-espanol/`](iconos-diseno-industrial-espanol/) | Objetos de diseño industrial español del siglo XX documentados en fichas de museo: Minipimer, Citromatic MPZ-2, TMC, aceitera Marquina, Tatú, Toledo… | 12 |

Cada carpeta contiene:

- los datos en **CSV** (UTF-8, separador coma, cabecera en la primera línea) y en **JSON** (lista de objetos);
- un **README** con descripción, diccionario de datos, metodología, fuentes, limitaciones, fecha de corte y forma de citar;
- un **`datapackage.json`** conforme a la especificación [Frictionless Data](https://specs.frictionlessdata.io/), con el esquema de cada columna.

## Cómo usarlos

Con Python y la biblioteca estándar:

```python
import csv

with open("patrones-oscuros/patrones-oscuros.csv", encoding="utf-8") as fh:
    for fila in csv.DictReader(fh):
        print(fila["id"], fila["nombre_es"])
```

Con pandas:

```python
import pandas as pd

episodios = pd.read_json("black-mirror-tecnologia-y-etica/black-mirror.json")
episodios.explode("temas_eticos").groupby("temas_eticos").size().sort_values()
```

Con las herramientas de Frictionless (`pip install frictionless`):

```bash
frictionless validate iconos-diseno-industrial-espanol/datapackage.json
```

## Validación

[`scripts/validar.py`](scripts/validar.py) usa solo la biblioteca estándar de Python. Comprueba en cada conjunto que la cabecera del CSV coincide con el esquema, que no faltan campos obligatorios, que los tipos, las listas cerradas y los valores únicos se respetan y que el JSON contiene los mismos registros que el CSV.

```bash
python3 scripts/validar.py
```

## Licencias

| Qué | Licencia |
|---|---|
| Datos y documentación (todas las carpetas salvo `scripts/`) | [Creative Commons Atribución 4.0 Internacional (CC BY 4.0)](LICENSE) |
| Código de [`scripts/`](scripts/) | [MIT](scripts/LICENSE) |

Puedes copiar, adaptar y usar los datos con cualquier fin, también comercial, siempre que cites la autoría y enlaces la licencia. Los textos legales citados (Reglamentos y Directivas de la UE) y los datos factuales tomados de fichas de museo pertenecen a sus fuentes; aquí se reproducen como cita, con enlace.

> Los conjuntos que tratan normativa son material de trabajo y divulgación. **No son asesoramiento jurídico.**

## Cómo citar

> Menéndez Granda, N. (2026). *Datos abiertos de Nacho MG* (versión 0.9.0) [Conjunto de datos]. https://github.com/NachoMeGran/datos-abiertos. Licencia CC BY 4.0.

Cada carpeta indica además cómo citar ese conjunto concreto. GitHub muestra la cita en formato APA y BibTeX a partir de [`CITATION.cff`](CITATION.cff).

## Correcciones

Si encuentras un error, abre una incidencia con el conjunto, el `id` del registro y un enlace a la fuente que lo corrige. Los criterios están en [`CONTRIBUTING.md`](CONTRIBUTING.md) y los cambios de cada versión en [`CHANGELOG.md`](CHANGELOG.md).

## Autoría

Nacho Menéndez Granda, consultor de marketing digital en Barcelona. Escribo sobre marketing ético, uso responsable de la IA y cultura pop en [nachomg.com](https://nachomg.com/) y envío cada dos semanas la newsletter [Life on marketing](https://nachomg.com/life-on-marketing/). Más sobre mí en [nachomg.com/nacho-menendez/](https://nachomg.com/nacho-menendez/).

**Estado: borrador en revisión.** La recopilación y verificación de fuentes, la estructura y las tareas mecánicas (formato, validación de datos, pruebas) se hicieron con apoyo de herramientas de IA, el uso que defiendo para esta tecnología. Cada dato se ha contrastado con la fuente enlazada. El texto definitivo de la documentación lo estoy reescribiendo a mano; hasta entonces, trata este material como un documento de trabajo.
