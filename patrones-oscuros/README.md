# Patrones de diseño engañosos: taxonomía en español

Treinta y cinco tipos de patrones de diseño engañosos («patrones oscuros», *dark patterns*) recogidos de tres textos oficiales europeos, con una descripción en español, un ejemplo genérico y una alternativa de diseño respetuosa para cada uno:

- Las **Directrices 03/2022 del Comité Europeo de Protección de Datos (EDPB)** sobre patrones de diseño engañosos en interfaces de redes sociales, versión 2.0 adoptada el 14 de febrero de 2023: 6 categorías y 16 tipos.
- El **artículo 25 y el considerando 67 del Reglamento (UE) 2022/2065 de Servicios Digitales (DSA)**: 6 prácticas.
- El **anexo I de la Directiva 2005/29/CE de prácticas comerciales desleales**, con los puntos que añadió la Directiva (UE) 2019/2161: 13 prácticas que se dan con frecuencia en interfaces digitales.

Lo he preparado para equipos de producto, UX, marketing y cumplimiento que necesitan hablar de estos patrones con el mismo vocabulario que usan los reguladores, y en castellano.

> **No es asesoramiento jurídico.** Es una herramienta de trabajo para diseñar y auditar interfaces. Si una práctica concreta te preocupa, consulta con un abogado especializado.

## Archivos

| Archivo | Contenido |
|---|---|
| [`patrones-oscuros.csv`](patrones-oscuros.csv) | Datos en CSV (UTF-8, separador coma, cabecera en la primera línea) |
| [`patrones-oscuros.json`](patrones-oscuros.json) | Los mismos registros como lista de objetos JSON; campos vacíos como `null` |
| [`datapackage.json`](datapackage.json) | Descriptor [Frictionless Data](https://specs.frictionlessdata.io/) con el esquema de cada columna |

## Diccionario de datos

| Columna | Tipo | Obligatoria | Significado |
|---|---|---|---|
| `id` | texto | sí | Identificador estable: fuente y apartado (`EDPB-4.1.1`, `DSA-25.3.a`, `DSA-C67-…`, `UCPD-AI-7`). |
| `fuente` | texto (lista cerrada) | sí | `EDPB`, `DSA` o `Directiva 2005/29/CE`. |
| `nombre_es` | texto | sí | Nombre breve en español. En las filas del EDPB es traducción mía: el EDPB no ha publicado versión oficial en español de estas directrices. |
| `nombre_original` | texto | sí | En el EDPB, el nombre inglés del documento. En el DSA y la Directiva, una cita literal de la versión española oficial; `[...]` indica que he abreviado la cita. |
| `idioma_nombre_original` | texto (`en`, `es`) | sí | Idioma de `nombre_original`. |
| `categoria_edpb` | texto (lista cerrada) | no | Categoría oficial del EDPB (`Overloading`, `Skipping`, `Stirring`, `Obstructing`, `Fickle`, `Left in the dark`). Solo en filas del EDPB. |
| `categoria_edpb_es` | texto | no | Traducción propia de la categoría. Solo en filas del EDPB. |
| `categoria_edpb_afin` | texto (lista cerrada) | sí | Categoría del EDPB más próxima. En filas del DSA y de la Directiva es **correspondencia editorial mía**, no oficial. |
| `descripcion` | texto | sí | Descripción en español, parafraseada de la fuente. |
| `ejemplo_generico` | texto | sí | Ejemplo genérico redactado para este conjunto. No describe ningún caso real ni ninguna empresa. |
| `norma_relacionada` | texto | sí | Disposiciones que cita la fuente. En las filas del EDPB, los artículos del RGPD que el anexo I asocia a cada tipo. |
| `referencia_fuente` | texto | sí | Documento y apartado exactos. |
| `url_fuente` | URL | sí | Texto oficial consultado. |
| `alternativa_etica` | texto | sí | Alternativa de diseño que evita el patrón. |
| `alternativa_fuente` | texto | sí | De dónde sale la alternativa: buena práctica del anexo II del EDPB (con su nombre original en inglés) o redacción editorial. |

Traducción de las categorías del EDPB que uso: *Overloading* = sobrecarga; *Skipping* = omisión inducida; *Stirring* = agitación emocional; *Obstructing* = obstrucción; *Fickle* = inconstancia; *Left in the dark* = a oscuras.

## Metodología

1. **EDPB.** Tomé las seis categorías y los dieciséis tipos del anexo I de las Directrices 03/2022 v2.0 (págs. 65-71 del PDF), con los artículos del RGPD que el propio anexo asocia a cada tipo. Las alternativas proceden, cuando existe una equivalente, de las buenas prácticas del anexo II; si no, son redacción mía y así lo indica `alternativa_fuente`.
2. **DSA.** Incluí las tres prácticas que el art. 25.3 enumera como posibles objetos de directrices de la Comisión y las tres prácticas adicionales que menciona el considerando 67. Las citas proceden del texto en español publicado en el DOUE (copia del BOE).
3. **Directiva 2005/29/CE.** Del anexo I (prácticas desleales «en cualquier circunstancia») seleccioné los puntos que se presentan con frecuencia en interfaces digitales: publicidad señuelo, urgencia y escasez falsas, falsos «gratis», reseñas falsas, publicidad encubierta, insistencia comercial, suministro no solicitado y premios falsos. Los puntos 11 bis, 23 ter y 23 quater los añadió la Directiva (UE) 2019/2161. No incluí los puntos sin relación con el diseño de interfaces (por ejemplo, ventas piramidales o visitas a domicilio).
4. Comprobé de forma automática que cada cita literal del DSA y de la Directiva aparece en el texto oficial descargado.
5. Las descripciones son paráfrasis; para cualquier uso jurídico manda el texto oficial enlazado.

## Fuentes

- EDPB, [*Guidelines 03/2022 on deceptive design patterns in social media platform interfaces: how to recognise and avoid them*, versión 2.0, adoptada el 14-02-2023](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-032022-deceptive-design-patterns-social-media_en) ([PDF](https://www.edpb.europa.eu/system/files/documents/2023-02/edpb_03-2022_guidelines_on_deceptive_design_patterns_in_social_media_platform_interfaces_v2_en_0.pdf)).
- [Reglamento (UE) 2022/2065 del Parlamento Europeo y del Consejo, de 19 de octubre de 2022, relativo a un mercado único de servicios digitales](https://www.boe.es/buscar/doc.php?id=DOUE-L-2022-81573), DO L 277 de 27-10-2022. También en [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2065/oj).
- [Directiva 2005/29/CE, de 11 de mayo de 2005, relativa a las prácticas comerciales desleales](https://www.boe.es/doue/2005/149/L00022-00039.pdf), DO L 149 de 11-06-2005.
- [Directiva (UE) 2019/2161, de 27 de noviembre de 2019](https://www.boe.es/doue/2019/328/L00007-00028.pdf), DO L 328 de 18-12-2019, art. 3.7 (modifica el anexo I de la Directiva 2005/29/CE).

## Limitaciones

- Las directrices del EDPB se refieren a interfaces de **redes sociales** y al RGPD; muchos tipos se aplican igual a cualquier web o app, pero el documento no lo dice para todos los casos.
- El EDPB y el anexo I de la Directiva advierten que sus listas **no son exhaustivas**. Este conjunto tampoco.
- Hay solapamientos: la insistencia continua del EDPB y la solicitud reiterada del DSA describen conductas muy parecidas desde normas distintas. Las mantengo separadas porque la base jurídica cambia. El art. 25.2 del DSA excluye de su prohibición las prácticas ya cubiertas por la Directiva 2005/29/CE o el RGPD.
- `categoria_edpb_afin`, los ejemplos y parte de las alternativas son **interpretación editorial**.
- Los nombres en español de los tipos del EDPB son traducción propia, no oficial.
- La Directiva 2005/29/CE está transpuesta en España principalmente en la Ley 3/1991 de Competencia Desleal; aquí cito la Directiva, no la ley española.

## Fecha de corte

20 de noviembre de 2026. Textos consultados en esa fecha.

## Cómo citar

> Menéndez Granda, N. (2026). *Patrones de diseño engañosos: taxonomía en español* (versión 0.9.0) [Conjunto de datos]. Datos abiertos de Nacho MG. https://github.com/NachoMeGran/datos-abiertos/tree/main/patrones-oscuros. Licencia CC BY 4.0.

Más contexto sobre marketing y diseño responsables en [nachomg.com/branding-y-marketing/](https://nachomg.com/branding-y-marketing/).
