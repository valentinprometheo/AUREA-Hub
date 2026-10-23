#!/usr/bin/env python3
"""Auditoría del ecosistema de skills de AUREA: lo que el auditor de la metodología no ve.

Uso:
  python3 auditar_ecosistema.py RUTA/CARPETA_DE_SKILLS

Chequea, entre todas las skills propias (aurea-*, prometheo-*, ic-*, documentos-client-facing):
  1. Copias divergentes: cada skill suelta prometheo-* contra su copia en
     aurea-metodologia/references/02-skills/. Tienen que ser idénticas.
  2. Referencias a skills inexistentes: nombres con forma de skill que no están instalados
     (excepto las que viven solo dentro de la metodología o están marcadas como pendientes).
  3. Cifras derogadas: los términos de la tabla de derogados de la skill de costos y de la
     metodología, fuera de un contexto que diga derogado o histórico.
  4. Superposición de decks: toda skill con kit de deck sin el sistema DRAKON tiene que derivar
     a aurea-estetica-documentacion.
  5. Barrido de coherencia: la skill de corrección de prompts tiene los mismos chequeos que la
     metodología.
Sale con código 1 si hay alguna FALLA.
"""
import os, re, sys

RAIZ = sys.argv[1] if len(sys.argv) > 1 else '.'
PROPIAS = ('aurea', 'prometheo', 'ic-', 'documentos-client-facing')
HISTORIA = ('CHANGELOG', 'HISTORIAL', 'hallazgos', 'aprendizajes')
CONTEXTO_OK = re.compile(r'derogad|histór|antes decía|qué decía antes|no se escribe|instancia|ejemplo de oro|caso real|ya no|'
                         r', no "|\\bni "|nunca|prohib|cerrada', re.I)
# Cifras derogadas por la skill de costos (13/10/2026) y la metodología v1.31
DEROGADAS = ['Licencia USD 150', 'desde USD 149', 'desde ~USD 149', 'pendiente de unificar 149 vs 150',
             '0,30 a 0,45', 'USD 20 cada 2.000', '0,0618', 'Recarga automática con piso', 'USD 0,35 por conversación',
             # precios de AUREA derogados por los paquetes (23/10/2026)
             'USD 850 por mes durante la implementación', 'USD 200 por mes con un canal incluido', 'Start · Estabilidad:** USD 200']
CSS_TOKENS = re.compile(r'^aurea-(blue|purple|green|orange|teal|coral)')
res = []


def rep(nivel, chequeo, detalle):
    res.append((nivel, chequeo, detalle))


def leer(p):
    return open(p, encoding='utf-8', errors='ignore').read()


skills = sorted(d for d in os.listdir(RAIZ) if os.path.isfile(os.path.join(RAIZ, d, 'SKILL.md')))
propias = [d for d in skills if d.startswith(PROPIAS)]
MET = os.path.join(RAIZ, 'aurea-metodologia', 'references', '02-skills')
internas = {d for r, ds, _ in os.walk(MET) for d in ds} if os.path.isdir(MET) else set()


def md(d):
    for r, _, fs in os.walk(os.path.join(RAIZ, d)):
        for f in fs:
            if f.endswith('.md') and not any(h in f for h in HISTORIA):
                yield os.path.join(r, f)


# 1. Copias divergentes
for d in [x for x in propias if x.startswith('prometheo-')]:
    copia = [os.path.join(r, d, 'SKILL.reference.md') for r, ds, _ in os.walk(MET) if d in ds]
    if not copia:
        rep('ALERTA', '1 copias', f'{d}: no tiene copia en la metodología')
    elif leer(os.path.join(RAIZ, d, 'SKILL.md')).strip() != leer(copia[0]).strip():
        rep('FALLA', '1 copias', f'{d}: distinta de su copia en la metodología')
if not [r for r in res if r[1] == '1 copias']:
    rep('OK', '1 copias', 'las skills prometheo-* coinciden con sus copias de la metodología')

# 2. Referencias a skills inexistentes
pendientes = ''
readme = os.path.join(RAIZ, 'aurea-metodologia', 'references', 'README.md')
if os.path.isfile(readme):
    pendientes = ' '.join(l for l in leer(readme).splitlines() if 'PENDIENTE' in l)
rotas = {}
for d in propias:
    for p in md(d):
        for m in re.findall(r'(?<![\w/-])((?:aurea|prometheo|ic)-[a-zñóé0-9-]{4,})(?![\w-]|\.\w)', leer(p)):
            if m in skills or m in internas or CSS_TOKENS.match(m) or m in pendientes or m.endswith('-'):
                continue
            rotas.setdefault(m, set()).add(d)
for k, v in sorted(rotas.items()):
    rep('ALERTA', '2 referencias', f'`{k}` no es una skill instalada · lo citan: {", ".join(sorted(v))}')
if not rotas:
    rep('OK', '2 referencias', 'todos los nombres de skill citados existen')

# 3. Cifras derogadas
hits = 0
for d in propias:
    for p in md(d):
        if d == 'ic-costos-y-rentabilidad-de-prometheo' or p.endswith('metodologia-correccion-agente.md'):
            continue  # son las fuentes que declaran los derogados
        ls = leer(p).splitlines()
        for i, l in enumerate(ls):
            for t in DEROGADAS:
                if t.lower() in l.lower() and not CONTEXTO_OK.search(' '.join(ls[max(0, i - 3):i + 2])):
                    hits += 1
                    rep('FALLA', '3 derogadas', f'{os.path.relpath(p, RAIZ)}:{i + 1} · "{t}"')
if not hits:
    rep('OK', '3 derogadas', f'{len(DEROGADAS)} cifras buscadas, ninguna vigente')

# 4. Decks
for d in propias:
    base = os.path.join(RAIZ, d)
    tiene_kit = any('aurea_kit.py' in fs for _, _, fs in os.walk(base))
    tiene_drakon = any('aurea-drakon.css' in fs for _, _, fs in os.walk(base))
    if tiene_kit and not tiene_drakon and 'aurea-estetica-documentacion' not in leer(os.path.join(base, 'SKILL.md')):
        rep('FALLA', '4 decks', f'{d}: tiene el kit reducido y no deriva a aurea-estetica-documentacion')
if not [r for r in res if r[1] == '4 decks']:
    rep('OK', '4 decks', 'toda skill con kit reducido deriva a aurea-estetica-documentacion')

# 5. Barrido de coherencia
mca = os.path.join(RAIZ, 'aurea-metodologia', 'references', '01-metodologia', '02-ETAPA2-Diseno', 'metodologia-correccion-agente.md')
cp = [d for d in skills if d.startswith('aurea-prometheo-corr')]
if os.path.isfile(mca) and cp:
    n_met = len(re.findall(r'^\d\. \*\*', leer(mca).split('## El barrido de coherencia')[1].split('Chequeo 9')[0], re.M))
    n_cp = len(re.findall(r'^### \d · ', leer(os.path.join(RAIZ, cp[0], 'references', '02-barrido-de-coherencia.md')), re.M))
    rep('OK' if n_cp >= n_met else 'FALLA', '5 barrido', f'metodología {n_met} chequeos (+9) · corrección de prompts {n_cp}')

for nivel, ch, det in sorted(res, key=lambda r: (r[0] != 'FALLA', r[0] != 'ALERTA', r[1])):
    print(f'[{nivel:6s}] {ch}: {det}')
fallas = sum(1 for r in res if r[0] == 'FALLA')
print(f'\nResultado: {fallas} fallas · {sum(1 for r in res if r[0] == "ALERTA")} alertas · {len(propias)} skills propias')
sys.exit(1 if fallas else 0)
