#!/usr/bin/env python3
"""Auditoría de una nueva versión de la skill aurea-metodologia contra la anterior.

Uso:
  python3 auditar.py --anterior RUTA/aurea-metodologia --nueva RUTA/aurea-metodologia

Chequea, sin depender de la memoria de nadie:
  1. Encabezado del SKILL.md (name, description, largo de la descripción <= 1024).
  2. Archivos perdidos (estaban en la anterior y no están en la nueva).
  3. Recortes grandes (archivos que perdieron más del 30% de sus líneas).
  4. Términos derogados (lee la tabla de metodologia-correccion-agente.md).
  5. Superposición: dos archivos que se declaran "fuente-única-de" lo mismo.
  6. Archivos nuevos sin encabezado de auto-ruteo.
  7. Referencias rotas: archivos .md que el SKILL.md o el router nombran y no existen.
  8. CHANGELOG: la primera entrada tiene que ser una versión nueva.
  9. Largo del SKILL.md (ideal < 500 líneas).
Sale con código 1 si hay alguna FALLA. Las ALERTAS no frenan, pero hay que justificarlas.
"""
import argparse, os, re, sys, difflib

try:
    import yaml
except ImportError:
    yaml = None

MARCAS_OK = re.compile(r"derogad|histór|incorrect|modelo viejo|ya no|reemplaz|qué decía antes|"
                       r"no se crea|nunca se guarda|no hay variable|quedó|superad|registro|❌|antes:|redundant|se eliminan",
                       re.I)
EXCLUIR_ARCHIVOS = ("CHANGELOG.md", "HISTORIAL-")
# Un archivo marcado como histórico en sus primeras líneas se conserva como registro:
# no se audita por términos derogados (no es molde, es historia).
MARCA_HISTORICO = re.compile(r"CASO HISTÓRICO|Registro histórico", re.I)

resultados = []
def rep(nivel, chequeo, detalle):
    resultados.append((nivel, chequeo, detalle))

def md_files(raiz):
    out = {}
    for d, _, fs in os.walk(raiz):
        for f in fs:
            p = os.path.join(d, f)
            out[os.path.relpath(p, raiz)] = p
    return out

def leer(p):
    try:
        return open(p, encoding="utf-8").read()
    except Exception:
        return ""

def chequeo_frontmatter(nueva):
    t = leer(os.path.join(nueva, "SKILL.md"))
    if not t.startswith("---"):
        rep("FALLA", "1 encabezado", "SKILL.md no empieza con encabezado ---"); return
    fm = t.split("---")[1]
    if yaml:
        data = yaml.safe_load(fm) or {}
        name, desc = data.get("name"), data.get("description") or ""
    else:
        name = re.search(r"^name:\s*(.+)$", fm, re.M); name = name and name.group(1).strip()
        desc = fm
    if not name:
        rep("FALLA", "1 encabezado", "falta name")
    if not desc:
        rep("FALLA", "1 encabezado", "falta description")
    elif len(desc) > 1024:
        rep("FALLA", "1 encabezado", f"descripción de {len(desc)} caracteres (máximo 1024)")
    else:
        rep("OK", "1 encabezado", f"name={name} · descripción {len(desc)}/1024")
    n = t.count("\n")
    rep("OK" if n < 500 else "ALERTA", "9 largo SKILL.md", f"{n} líneas (ideal < 500)")

def chequeo_archivos(ant, nue):
    fa, fn = md_files(ant), md_files(nue)
    perdidos = sorted(set(fa) - set(fn))
    if perdidos:
        for p in perdidos:
            rep("ALERTA", "2 archivo perdido", f"{p} (justificar en el CHANGELOG o restaurar)")
    else:
        rep("OK", "2 archivos perdidos", f"ninguno · anterior {len(fa)} · nueva {len(fn)}")
    recortes = 0
    for rel in sorted(set(fa) & set(fn)):
        if not rel.endswith(".md"):
            continue
        a, b = leer(fa[rel]).splitlines(), leer(fn[rel]).splitlines()
        if len(a) < 20:
            continue
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        quitadas = sum(i2 - i1 for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ("delete", "replace"))
        if len(b) < len(a) and quitadas / len(a) > 0.30:
            recortes += 1
            rep("ALERTA", "3 recorte grande", f"{rel}: perdió {quitadas} de {len(a)} líneas ({len(a)}→{len(b)})")
    if not recortes:
        rep("OK", "3 recortes grandes", "ningún archivo perdió más del 30%")
    return fa, fn

def terminos_derogados(nue):
    cands = [p for p in md_files(nue).values() if p.endswith("metodologia-correccion-agente.md")]
    if not cands:
        rep("ALERTA", "4 términos derogados", "no encontré metodologia-correccion-agente.md"); return []
    t = leer(cands[0])
    m = re.search(r"\| Término derogado.*?\n\|[-| ]+\n(.*?)(?:\n\n|\Z)", t, re.S)
    if not m:
        rep("ALERTA", "4 términos derogados", "no encontré la tabla de términos derogados"); return []
    terminos = []
    for fila in m.group(1).splitlines():
        celda = fila.split("|")[1] if fila.startswith("|") else ""
        terminos += re.findall(r"`([^`]+)`", celda) + re.findall(r'"([^"]+)"', celda)
    return [x.strip() for x in terminos if len(x.strip()) > 3]

def chequeo_derogados(nue):
    terms = terminos_derogados(nue)
    if not terms:
        return
    hits = 0
    historicos = []
    for rel, p in md_files(nue).items():
        if not rel.endswith(".md") or any(x in rel for x in EXCLUIR_ARCHIVOS):
            continue
        if "metodologia-correccion-agente.md" in rel:
            continue
        lineas = leer(p).splitlines()
        if MARCA_HISTORICO.search("\n".join(lineas[:30])):
            historicos.append(rel)
            continue
        for i, l in enumerate(lineas):
            for term in terms:
                if term.lower() in l.lower():
                    ctx = " ".join(lineas[max(0, i - 2):i + 2])
                    if MARCAS_OK.search(ctx):
                        continue
                    hits += 1
                    rep("FALLA", "4 término derogado", f"{rel}:{i+1} usa «{term}»")
    if not hits:
        rep("OK", "4 términos derogados", f"{len(terms)} términos buscados, ninguno vigente")
    if historicos:
        rep("OK", "4 registros históricos", f"{len(historicos)} archivos marcados como históricos, no auditados: {', '.join(os.path.basename(h) for h in historicos)}")

def encabezado(texto):
    m = re.match(r"---\n(.*?)\n---", texto, re.S)
    return m.group(1) if m else ""

def chequeo_superposicion(fn):
    duenos = {}
    for rel, p in fn.items():
        if not rel.endswith(".md"):
            continue
        h = encabezado(leer(p))
        m = re.search(r"^fuente-única-de:\s*(.+)$", h, re.M)
        if m:
            clave = re.sub(r"\W+", " ", m.group(1).lower()).strip()
            duenos.setdefault(clave, []).append(rel)
    dup = {k: v for k, v in duenos.items() if len(v) > 1}
    if dup:
        for k, v in dup.items():
            rep("FALLA", "5 superposición", f"«{k}» lo declaran: {', '.join(v)}")
    else:
        rep("OK", "5 superposición", f"{len(duenos)} temas con un solo archivo dueño")

def chequeo_encabezados_nuevos(fa, fn):
    # Todo archivo .md nuevo dentro de references/ es doctrina, salvo los que no son molde:
    # casos de referencia, historiales, copias de otras skills, rubros de calificación y CHANGELOG.
    excluir = ("08-casos-referencia", "HISTORIAL-", "02-skills/", "calificacion/rubros/", "CHANGELOG.md")
    nuevos = [r for r in set(fn) - set(fa) if r.endswith(".md") and r.startswith("references/")
              and not any(x in r for x in excluir)]
    sin = [r for r in nuevos if "consultar-cuando:" not in encabezado(leer(fn[r]))]
    for r in sin:
        rep("ALERTA", "6 sin auto-ruteo", f"{r} no tiene encabezado consultar-cuando/fuente-única-de")
    if not sin:
        rep("OK", "6 auto-ruteo", f"{len(nuevos)} archivos nuevos de doctrina, todos con encabezado")

def chequeo_referencias(nue, fn):
    nombres = {os.path.basename(r) for r in fn}
    rutas = set(fn)
    rotas = []
    for base in ("SKILL.md",):
        t = leer(os.path.join(nue, base))
        for ref in set(re.findall(r"`([^`\s]+\.md)`", t)):
            ref_clean = ref.replace("<rubro>", "")
            if "<" in ref or ref_clean.endswith("/.md"):
                continue
            if ref in rutas or ref.replace("references/", "references/", 1) in rutas or os.path.basename(ref) in nombres:
                continue
            rotas.append(f"{base} → {ref}")
    for r in rotas:
        rep("FALLA", "7 referencia rota", r)
    if not rotas:
        rep("OK", "7 referencias", "todo archivo nombrado en el SKILL.md existe")

def chequeo_changelog(ant, nue):
    def primera(raiz):
        for rel, p in md_files(raiz).items():
            if rel.endswith("references/CHANGELOG.md"):
                m = re.search(r"^## (v[\d.]+)", leer(p), re.M)
                return m and m.group(1)
    a, n = primera(ant), primera(nue)
    if not n:
        rep("FALLA", "8 CHANGELOG", "no encontré references/CHANGELOG.md con entradas ## vX")
    elif a == n:
        rep("FALLA", "8 CHANGELOG", f"la primera entrada sigue siendo {n}: falta la entrada de la versión nueva")
    else:
        rep("OK", "8 CHANGELOG", f"{a} → {n}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--anterior", required=True)
    ap.add_argument("--nueva", required=True)
    a = ap.parse_args()
    chequeo_frontmatter(a.nueva)
    fa, fn = chequeo_archivos(a.anterior, a.nueva)
    chequeo_derogados(a.nueva)
    chequeo_superposicion(fn)
    chequeo_encabezados_nuevos(fa, fn)
    chequeo_referencias(a.nueva, fn)
    chequeo_changelog(a.anterior, a.nueva)
    orden = {"FALLA": 0, "ALERTA": 1, "OK": 2}
    for nivel, ch, det in sorted(resultados, key=lambda r: (orden[r[0]], r[1])):
        print(f"[{nivel:6}] {ch}: {det}")
    f = sum(1 for r in resultados if r[0] == "FALLA")
    al = sum(1 for r in resultados if r[0] == "ALERTA")
    print(f"\nResultado: {f} fallas · {al} alertas")
    sys.exit(1 if f else 0)

if __name__ == "__main__":
    main()
