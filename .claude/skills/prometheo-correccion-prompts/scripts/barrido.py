#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
barrido.py - Ayuda mecánica para el BARRIDO DE COHERENCIA (Prometheo / AUREA).

Automatiza la parte verificable por máquina de cuatro de los siete chequeos:

  1 · PRESENCIA             cada regla corregida está literalmente en el texto final
  3 · PROPAGACIÓN           todas las apariciones de un mecanismo, con su sector
  4 · ESTRUCTURA HUÉRFANA   candidatos: sectores que todavía nombran la fuente vieja
                            y que nadie invoca
  5 · REFERENCIAS CRUZADAS  "ver Sección X" que apunta a algo inexistente, y
                            placeholders casi duplicados (tilde, mayúscula, separador)

Los chequeos 2 (contradicción), 6 (ámbito) y 7 (reconciliación entre rondas) son de
criterio: el script los deja marcados como pendientes de revisión humana.

Este script NO reemplaza el barrido. Es el piso mecánico del barrido.

Uso:

    python3 barrido.py PROMPT.md \\
        --reglas reglas.txt \\
        --mecanismo "apéndice" --mecanismo "integración nativa" \\
        --huerfano "Apéndice A" \\
        --json salida.json

  --reglas    archivo de texto, una cadena literal por línea (nombre de regla, número
              o frase clave del enunciado). Líneas vacías y con # se ignoran.
  --mecanismo palabra clave del mecanismo que cambió. Repetible.
  --huerfano  palabra clave de la fuente o el bloque VIEJO. Repetible. El script marca
              los sectores que la siguen nombrando y dice si alguien los invoca.

Salida: reporte legible por stdout. Exit code 1 si algún chequeo mecánico tiene hallazgos.
"""

import argparse
import json
import re
import sys
import unicodedata

# ---------------------------------------------------------------- utilidades

SECTION_RE = re.compile(
    r"^\s*(?:=+\s*|#+\s*)?(SECCI[ÓO]N|AP[ÉE]NDICE|ANEXO)\s*[:.]?\s*([0-9]+[A-Za-z]?)",
    re.IGNORECASE,
)

REF_RE = re.compile(
    r"(?:ver\s+)?\(?\s*(secci[óo]n|ap[ée]ndice|anexo)\s*([0-9]+[A-Za-z]?)\s*\)?",
    re.IGNORECASE,
)

RULE_REF_RE = re.compile(r"\bregla\s+([0-9]+)\b", re.IGNORECASE)
RULE_DEF_RE = re.compile(r"^\s*REGLA\s+([0-9]+)\b", re.IGNORECASE | re.MULTILINE)

# /Brochure-Torre-Sur  ·  [VIDEO_MOB_URBANO_2]
PLACEHOLDER_RE = re.compile(
    r"(/[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][\w\-ÁÉÍÓÚÜÑáéíóúüñ]*|\[[A-Z0-9_]{3,}\])"
)


def fold(s):
    """Normaliza para detectar casi duplicados: sin tildes, minúsculas, sin separadores."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-]+", "", s).lower()


def map_sections(lines):
    """Devuelve marcas [(linea, etiqueta, numero)] y spans {etiqueta: (inicio, fin)}."""
    marks = []
    for i, line in enumerate(lines, 1):
        m = SECTION_RE.match(line)
        if m:
            kind = m.group(1).upper()
            kind = "SECCIÓN" if kind.startswith("SECCI") else kind.replace("APENDICE", "APÉNDICE")
            marks.append((i, f"{kind} {m.group(2).upper()}", m.group(2).upper()))
    spans = {}
    for idx, (ln, label, _num) in enumerate(marks):
        end = marks[idx + 1][0] - 1 if idx + 1 < len(marks) else len(lines)
        spans[label] = (ln, end)
    return marks, spans


def section_of(line_no, marks):
    """Etiqueta del sector al que pertenece una línea."""
    current = "(antes del primer sector)"
    for ln, label, _ in marks:
        if ln <= line_no:
            current = label
        else:
            break
    return current


def referenced_sections(lines, marks):
    """Sectores invocados desde alguna parte del prompt que no sea su propio encabezado."""
    header_lines = {ln for ln, _, _ in marks}
    invoked = set()
    for i, line in enumerate(lines, 1):
        if i in header_lines:
            continue
        for m in REF_RE.finditer(line):
            kind = m.group(1).upper()
            kind = "SECCIÓN" if kind.startswith("SECCI") else kind.replace("APENDICE", "APÉNDICE")
            invoked.add(f"{kind} {m.group(2).upper()}")
    return invoked


# ---------------------------------------------------------------- chequeos


def chequeo_presencia(text, reglas):
    faltantes, presentes = [], []
    for r in reglas:
        (presentes if r in text else faltantes).append(r)
    return {"total": len(reglas), "presentes": presentes, "faltantes": faltantes}


def chequeo_propagacion(lines, marks, mecanismos):
    hits = {}
    for kw in mecanismos:
        kw_f = fold(kw)
        found = []
        for i, line in enumerate(lines, 1):
            if kw_f and kw_f in fold(line):
                found.append(
                    {"linea": i, "sector": section_of(i, marks), "texto": line.strip()[:160]}
                )
        hits[kw] = found
    return hits


def chequeo_huerfano(lines, marks, claves, invocados):
    out = {}
    for kw in claves:
        kw_f = fold(kw)
        sectores = {}
        for i, line in enumerate(lines, 1):
            if kw_f and kw_f in fold(line):
                sectores.setdefault(section_of(i, marks), []).append(i)
        out[kw] = [
            {
                "sector": sec,
                "lineas": lns,
                "invocado_por_alguien": sec in invocados,
            }
            for sec, lns in sorted(sectores.items())
        ]
    return out


def chequeo_referencias(text, lines, marks, spans, invocados):
    existentes = set(spans)
    existentes_num = {num for _, _, num in marks}
    header_lines = {ln for ln, _, _ in marks}

    rotas, ok = [], 0
    for i, line in enumerate(lines, 1):
        if i in header_lines:
            continue
        for m in REF_RE.finditer(line):
            kind = m.group(1).upper()
            kind = "SECCIÓN" if kind.startswith("SECCI") else kind.replace("APENDICE", "APÉNDICE")
            num = m.group(2).upper()
            label = f"{kind} {num}"
            if label in existentes or (kind == "SECCIÓN" and num in existentes_num):
                ok += 1
            else:
                rotas.append({"linea": i, "referencia": label, "texto": line.strip()[:160]})

    definidas = {m.group(1) for m in RULE_DEF_RE.finditer(text)}
    reglas_rotas = []
    if definidas:
        for i, line in enumerate(lines, 1):
            if RULE_DEF_RE.match(line):
                continue
            for m in RULE_REF_RE.finditer(line):
                if m.group(1) not in definidas:
                    reglas_rotas.append(
                        {"linea": i, "referencia": f"REGLA {m.group(1)}",
                         "texto": line.strip()[:160]}
                    )

    return {"ok": ok, "secciones_rotas": rotas, "reglas_rotas": reglas_rotas}


def chequeo_placeholders(lines):
    tokens = {}
    for i, line in enumerate(lines, 1):
        for m in PLACEHOLDER_RE.finditer(line):
            tokens.setdefault(m.group(1), []).append(i)
    grupos = {}
    for t in tokens:
        grupos.setdefault(fold(t), []).append(t)
    casi = [sorted(v) for v in grupos.values() if len(v) > 1]
    return {"distintos": len(tokens), "tokens": tokens, "casi_duplicados": casi}


# ---------------------------------------------------------------- reporte


def main():
    ap = argparse.ArgumentParser(description="Barrido de coherencia (chequeos 1, 3, 4 y 5).")
    ap.add_argument("prompt", help="archivo del prompt final a verificar")
    ap.add_argument("--reglas", help="archivo con una cadena literal por línea")
    ap.add_argument("--mecanismo", action="append", default=[],
                    help="palabra clave del mecanismo que cambió (repetible)")
    ap.add_argument("--huerfano", action="append", default=[],
                    help="palabra clave de la fuente o bloque VIEJO (repetible)")
    ap.add_argument("--json", help="volcar el resultado a un JSON")
    args = ap.parse_args()

    with open(args.prompt, encoding="utf-8") as f:
        text = f.read()
    lines = text.splitlines()
    marks, spans = map_sections(lines)
    invocados = referenced_sections(lines, marks)

    reglas = []
    if args.reglas:
        with open(args.reglas, encoding="utf-8") as f:
            reglas = [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]

    out = {"archivo": args.prompt, "sectores_detectados": [l for _, l, _ in marks]}
    fallas = 0

    print("=" * 74)
    print("BARRIDO DE COHERENCIA · parte mecánica")
    print("=" * 74)
    print(f"Archivo: {args.prompt}")
    print(f"Sectores detectados: {len(marks)}  ->  "
          f"{', '.join(l for _, l, _ in marks) if marks else 'ninguno'}")
    print()

    # ---- 1
    print("-" * 74)
    print("1 · PRESENCIA")
    if not reglas:
        print("   N/A  no se pasó --reglas. Chequeo pendiente de verificación manual.")
        out["presencia"] = "N/A"
    else:
        res = chequeo_presencia(text, reglas)
        out["presencia"] = res
        print(f"   {len(res['presentes'])}/{res['total']} reglas presentes.")
        for r in res["faltantes"]:
            print(f"   FALTA: {r}")
        if res["faltantes"]:
            fallas += 1
        else:
            print("   OK")

    # ---- 3
    print("-" * 74)
    print("3 · PROPAGACIÓN DE MECANISMO")
    if not args.mecanismo:
        print("   N/A  no se pasó --mecanismo. Si cambió un mecanismo, este chequeo")
        print("        NO puede quedar en N/A: volvé a correr con las palabras clave.")
        out["propagacion"] = "N/A"
    else:
        hits = chequeo_propagacion(lines, marks, args.mecanismo)
        out["propagacion"] = hits
        for kw, found in hits.items():
            sectores = sorted({h["sector"] for h in found})
            print(f'   "{kw}": {len(found)} apariciones en {len(sectores)} sector(es)')
            for h in found:
                print(f"      L{h['linea']:>5} [{h['sector']}] {h['texto']}")
            if len(sectores) > 1:
                print("      REVISAR: aparece en más de un sector. Verificá que TODOS")
                print("               digan lo mismo sobre el mecanismo.")
        print("   Revisión humana obligatoria sobre la lista de arriba.")

    # ---- 4
    print("-" * 74)
    print("4 · ESTRUCTURA HUÉRFANA")
    if not args.huerfano:
        print("   N/A  no se pasó --huerfano. Si cambió la fuente de un dato, este chequeo")
        print("        NO puede quedar en N/A: pasá la palabra clave de la fuente vieja.")
        out["huerfano"] = "N/A"
    else:
        h = chequeo_huerfano(lines, marks, args.huerfano, invocados)
        out["huerfano"] = h
        candidatos = 0
        for kw, sectores in h.items():
            print(f'   "{kw}": aparece en {len(sectores)} sector(es)')
            for s in sectores:
                flag = "invocado por otra sección" if s["invocado_por_alguien"] \
                    else "NADIE LO INVOCA  <-- candidato a huérfano"
                print(f"      [{s['sector']}] líneas {s['lineas'][:8]}"
                      f"{'…' if len(s['lineas']) > 8 else ''}  ·  {flag}")
                if not s["invocado_por_alguien"]:
                    candidatos += 1
        if candidatos:
            print(f"   {candidatos} candidato(s) a estructura huérfana.")
            print("   Si el bloque ya no sirve a ninguna regla vigente: se ELIMINA dentro")
            print("   del mismo sector entregado y se registra en la matriz.")
            print("   Antes de borrar placeholders, verificá contra el inventario real.")
            fallas += 1
        else:
            print("   Sin candidatos: todo lo que nombra la fuente vieja sigue invocado.")

    # ---- 5
    print("-" * 74)
    print("5 · REFERENCIAS CRUZADAS")
    ref = chequeo_referencias(text, lines, marks, spans, invocados)
    out["referencias"] = ref
    print(f"   Referencias a sector resueltas: {ref['ok']}")
    for r in ref["secciones_rotas"]:
        print(f"   ROTA: L{r['linea']} invoca {r['referencia']} (no existe) :: {r['texto']}")
    for r in ref["reglas_rotas"]:
        print(f"   ROTA: L{r['linea']} invoca {r['referencia']} (no definida) :: {r['texto']}")
    if ref["secciones_rotas"] or ref["reglas_rotas"]:
        fallas += 1
    else:
        print("   OK  ninguna referencia apunta a algo inexistente.")

    ph = chequeo_placeholders(lines)
    out["placeholders"] = {"distintos": ph["distintos"], "casi_duplicados": ph["casi_duplicados"]}
    print(f"   Placeholders / tokens de archivo distintos: {ph['distintos']}")
    for grupo in ph["casi_duplicados"]:
        print(f"   CASI DUPLICADO: {grupo}")
        print("      Difieren solo en tilde, mayúscula o separador. Uno de los dos rompe")
        print("      el adjunto en silencio. Verificá contra el inventario real.")
    if ph["casi_duplicados"]:
        fallas += 1

    # ---- pendientes de criterio
    print("-" * 74)
    print("2 · CONTRADICCIÓN ENTRE REGLAS   PENDIENTE (criterio humano)")
    print("6 · ÁMBITO DE CADA REGLA         PENDIENTE (criterio humano)")
    print("7 · RECONCILIACIÓN ENTRE RONDAS  PENDIENTE (criterio humano)")
    print("-" * 74)
    print()
    if fallas:
        print(f"RESULTADO MECÁNICO: {fallas} chequeo(s) con hallazgos. Corregí y volvé a")
        print("correr el barrido COMPLETO, no solo el chequeo que falló.")
    else:
        print("RESULTADO MECÁNICO: sin hallazgos. Faltan los chequeos 2, 6 y 7.")
    print("Con menos de 7/7 la versión NO se entrega. Aplica también a entregas parciales.")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print(f"\nJSON: {args.json}")

    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
