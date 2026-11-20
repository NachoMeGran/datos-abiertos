#!/usr/bin/env python3
"""Valida los conjuntos de datos del repositorio.

Para cada carpeta con un datapackage.json comprueba que:

1. El descriptor tiene los campos básicos (name, licenses, resources) y que los
   archivos de cada recurso existen.
2. La cabecera del CSV coincide con los campos del esquema y en el mismo orden.
3. Cada fila cumple el esquema: campos obligatorios, tipos (integer, date),
   formato uri, listas cerradas (enum), mínimos, máximos y unicidad.
4. El JSON contiene exactamente los mismos registros que el CSV, en el mismo
   orden y con los mismos valores.

Solo usa la biblioteca estándar de Python (3.8 o superior).

Uso:
    python3 scripts/validar.py              # valida todo el repositorio
    python3 scripts/validar.py patrones-oscuros

Devuelve 0 si todo es correcto y 1 si encuentra algún error.
"""

import csv
import datetime
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Informe:
    def __init__(self):
        self.errores = []

    def error(self, carpeta, mensaje):
        self.errores.append(f"[{carpeta}] {mensaje}")


def valor_vacio(v):
    return v is None or v == "" or v == []


def comprobar_tipo(campo, valor):
    """Devuelve un mensaje de error o None. `valor` es el texto del CSV, no vacío."""
    tipo = campo.get("type", "string")
    if tipo == "integer":
        try:
            int(valor)
        except ValueError:
            return f"«{valor}» no es un entero"
    elif tipo == "date":
        try:
            datetime.date.fromisoformat(valor)
        except ValueError:
            return f"«{valor}» no es una fecha AAAA-MM-DD"
    if campo.get("format") == "uri" and not valor.startswith(("https://", "http://")):
        return f"«{valor}» no es una URL"
    restr = campo.get("constraints", {})
    if "enum" in restr and "separador" not in campo and valor not in restr["enum"]:
        return f"«{valor}» no está en la lista cerrada {restr['enum']}"
    if tipo == "integer":
        n = int(valor)
        if "minimum" in restr and n < restr["minimum"]:
            return f"{n} es menor que el mínimo {restr['minimum']}"
        if "maximum" in restr and n > restr["maximum"]:
            return f"{n} es mayor que el máximo {restr['maximum']}"
    return None


def csv_a_json(campo, texto):
    """Convierte un valor del CSV al valor esperado en el JSON."""
    if "separador" in campo:
        return [x for x in texto.split(campo["separador"]) if x] if texto else []
    if texto == "":
        return None
    if campo.get("type") == "integer":
        return int(texto)
    return texto


def validar_carpeta(carpeta, informe):
    ruta = os.path.join(RAIZ, carpeta)
    with open(os.path.join(ruta, "datapackage.json"), encoding="utf-8") as fh:
        paquete = json.load(fh)

    for clave in ("name", "licenses", "resources"):
        if clave not in paquete:
            informe.error(carpeta, f"datapackage.json sin «{clave}»")
    for recurso in paquete.get("resources", []):
        if not os.path.isfile(os.path.join(ruta, recurso.get("path", ""))):
            informe.error(carpeta, f"no existe el archivo {recurso.get('path')}")

    tabulares = [r for r in paquete["resources"] if r.get("profile") == "tabular-data-resource"]
    for recurso in tabulares:
        esquema = recurso["schema"]
        campos = esquema["fields"]
        nombres = [c["name"] for c in campos]
        por_nombre = {c["name"]: c for c in campos}

        with open(os.path.join(ruta, recurso["path"]), encoding="utf-8", newline="") as fh:
            lector = csv.reader(fh, delimiter=recurso.get("dialect", {}).get("delimiter", ","))
            cabecera = next(lector)
            filas = [dict(zip(cabecera, f)) for f in lector]
            longitudes = {len(f) for f in filas}

        if cabecera != nombres:
            informe.error(carpeta, f"la cabecera del CSV {cabecera} no coincide con el esquema {nombres}")
            continue

        vistos = {n: set() for n in nombres if por_nombre[n].get("constraints", {}).get("unique")}
        claves = set()
        for i, fila in enumerate(filas, start=2):
            if len(fila) != len(nombres):
                informe.error(carpeta, f"CSV, línea {i}: número de columnas incorrecto")
                continue
            for n in nombres:
                campo = por_nombre[n]
                valor = fila[n]
                restr = campo.get("constraints", {})
                if valor == "":
                    if restr.get("required"):
                        informe.error(carpeta, f"CSV, línea {i}: falta el campo obligatorio «{n}»")
                    continue
                if "separador" in campo:
                    partes = [p for p in valor.split(campo["separador"]) if p]
                    enum = campo.get("enum_elementos")
                    for p in partes:
                        if enum and p not in enum:
                            informe.error(carpeta, f"CSV, línea {i}, «{n}»: «{p}» no está en la lista controlada")
                else:
                    msg = comprobar_tipo(campo, valor)
                    if msg:
                        informe.error(carpeta, f"CSV, línea {i}, «{n}»: {msg}")
                if n in vistos:
                    if valor in vistos[n]:
                        informe.error(carpeta, f"CSV, línea {i}: valor repetido en «{n}»: {valor}")
                    vistos[n].add(valor)
            clave = tuple(fila[k] for k in esquema.get("primaryKey", []))
            if clave and clave in claves:
                informe.error(carpeta, f"CSV, línea {i}: clave primaria repetida {clave}")
            claves.add(clave)

        # Comparación con el JSON equivalente
        ruta_json = os.path.join(ruta, os.path.splitext(recurso["path"])[0] + ".json")
        if not os.path.isfile(ruta_json):
            informe.error(carpeta, f"falta el JSON equivalente {os.path.basename(ruta_json)}")
            continue
        with open(ruta_json, encoding="utf-8") as fh:
            datos = json.load(fh)
        if not isinstance(datos, list):
            informe.error(carpeta, "el JSON no es una lista de objetos")
            continue
        if len(datos) != len(filas):
            informe.error(carpeta, f"el CSV tiene {len(filas)} registros y el JSON {len(datos)}")
        for i, (fila, obj) in enumerate(zip(filas, datos), start=1):
            if list(obj.keys()) != nombres:
                informe.error(carpeta, f"JSON, registro {i}: claves {list(obj.keys())} distintas del esquema")
                continue
            for n in nombres:
                esperado = csv_a_json(por_nombre[n], fila[n])
                if obj[n] != esperado:
                    informe.error(carpeta, f"registro {i}, «{n}»: CSV={esperado!r} JSON={obj[n]!r}")
                if por_nombre[n].get("constraints", {}).get("required") and valor_vacio(obj[n]):
                    informe.error(carpeta, f"JSON, registro {i}: falta el campo obligatorio «{n}»")

        print(f"  {carpeta}/{recurso['path']}: {len(filas)} registros, {len(nombres)} campos")


def main(argv):
    if len(argv) > 1:
        carpetas = argv[1:]
    else:
        carpetas = sorted(
            d for d in os.listdir(RAIZ)
            if os.path.isfile(os.path.join(RAIZ, d, "datapackage.json"))
        )
    if not carpetas:
        print("No se ha encontrado ningún datapackage.json.")
        return 1
    informe = Informe()
    print("Validando conjuntos de datos:")
    for c in carpetas:
        try:
            validar_carpeta(c, informe)
        except (OSError, ValueError, KeyError) as exc:
            informe.error(c, f"no se pudo validar: {exc}")
    if informe.errores:
        print(f"\n{len(informe.errores)} error(es):")
        for e in informe.errores:
            print("  - " + e)
        return 1
    print("\nTodo correcto: CSV y JSON coinciden y no faltan campos obligatorios.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
