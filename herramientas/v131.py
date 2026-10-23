"""aurea-metodologia v1.30 -> v1.31. Cambios aditivos, cada uno con su línea "Actualización v1.31"."""
import os, re, sys
os.chdir(sys.argv[1])  # carpeta nueva/
M = 'aurea-metodologia'
R = f'{M}/references'
D = f'{R}/01-metodologia/02-ETAPA2-Diseno'


def rd(p): return open(p, encoding='utf-8').read()
def wr(p, s): open(p, 'w', encoding='utf-8').write(s)


def sub(p, old, new):
    s = rd(p)
    assert s.count(old) == 1, f'{p}: {s.count(old)} x {old[:70]!r}'
    wr(p, s.replace(old, new))


# 1. Router: la auditoría web es el Paso 1.1 de la Etapa 1 (como dice su propia skill)
for p, old, new in [
    (f'{M}/SKILL.md',
     '| Etapa 0 — auditoría web |',
     '| Etapa 1 · Paso 1.1 — auditoría web (pre-discovery; antes se llamaba "Etapa 0") |'),
    (f'{R}/01-metodologia/00-CONSULTA.md',
     '| **Etapa 0 — auditoría web** |',
     '| **Etapa 1 · Paso 1.1 — auditoría web** (antes "Etapa 0") |'),
]:
    sub(p, old, new)
for p, old in [(f'{M}/SKILL.md', '1. ¿En qué ESTADÍO estoy?      -> Etapa 0 / 1 / 2 (diseño) / 2 (iteración) / 3 / 4'),
               (f'{R}/01-metodologia/00-CONSULTA.md', '1. ¿En qué ESTADÍO estoy?      → Etapa 0 / 1 / 2 (diseño) / 2 (iteración) / 3 / 4')]:
    arrow = '->' if '->' in old else '→'
    sub(p, old, f'1. ¿En qué ESTADÍO estoy?      {arrow} Etapa 1 (Paso 1.1 auditoría web, discovery) / 2 (diseño) / 2 (iteración) / 3 / 4')
sub(f'{M}/SKILL.md', '## Tabla de despacho por ESTADÍO (eje PROCESO)\n',
    '## Tabla de despacho por ESTADÍO (eje PROCESO)\n\n'
    '> Actualización v1.31: la auditoría web pasó a ser el Paso 1.1 de la Etapa 1 (así la nombra su\n'
    '> skill desde v1.2x); el router todavía decía "Etapa 0". Qué decía antes: "Etapa 0 — auditoría web".\n')
sub(f'{R}/01-metodologia/00-CONSULTA.md', '| **Etapa 1 · Paso 1.1 — auditoría web** (antes "Etapa 0") |',
    '| **Etapa 1 · Paso 1.1 — auditoría web** (antes "Etapa 0"; Actualización v1.31) |')

# 2. Calificación: integra la v1.1 de la skill suelta (13/10), que nunca entró al módulo
C = f'{R}/calificacion/00-criterio-calificacion.md'
sub(C, 'proponer una línea de\nWhatsApp aparte para inmobiliarias y proveedores y medirlo en el tablero.',
    'proponer una línea de\nWhatsApp aparte para inmobiliarias y proveedores y medirlo en el tablero. Tarifas, costo por\n'
    'conversación y rentabilidad: fuente única en la skill `ic-costos-y-rentabilidad-de-prometheo`.\n\n'
    '### 2.11 Score y guardiana en cada cambio\n'
    'Un cambio de criterio, una recalificación con Mi Prometheo o un cambio para ahorrar tokens se\n'
    'propone como card de `aurea-data-action-driven`: verbo, dueño, efecto esperado y score con su\n'
    '"por qué". Guardianas obligatorias: si el cambio sube el % de calificados, que la definición del\n'
    'cliente no se afloje; si ahorra tokens o mensajes, que no baje el % de calificación ni crezcan\n'
    'los hot leads sin seguimiento.\n\n'
    '> Complemento v1.31: la sección 2.11 y el puntero a costos venían de la v1.1 de la skill suelta\n'
    '> `aurea-hub-criterio-calificacion-leads` (13/10/2026), que se actualizó después de la unión de la\n'
    '> v1.22 y nunca entró a este módulo.')
s = rd(C)
m = re.search(r'\n(- \[ \] [^\n]*)\n(?=\n## Mejora continua de este módulo)', s)
assert m, 'no encontré el checklist'
wr(C, s[:m.end(1)] + '\n- [ ] Cada cambio propuesto es una card con score y guardiana (2.11).' + s[m.end(1):])

# 3. Tarifas y recarga: el detalle de calificación trae lo derogado el 13/10
src = rd('aurea-hub-criterio-calificacion-leads/references/ahorro-de-tokens.md')
src = src.replace('`references/', '`references/calificacion/')
head, _, body = src.partition('\n')
wr(f'{R}/calificacion/ahorro-de-tokens-detalle.md',
   head + '\n\n> Actualización v1.31: este archivo se reemplazó por la v1.1 de la skill suelta de calificación\n'
   '> (13/10/2026). Qué decía antes: tarifas de Meta en USD (Marketing 0,0618, Utilidad 0,026),\n'
   '> "Recarga automática con piso" como palanca 1 y "USD 0,35 por conversación" en septiembre; los\n'
   '> tres quedaron derogados por `ic-costos-y-rentabilidad-de-prometheo`.\n' + body)
sub(f'{D}/restricciones-plataforma-prometheo.md',
    '**Recarga automática con piso: obligatoria en el go-live** (Perfil › Pagos › Saldo de tu cuenta).',
    '**Cero cortes de saldo en el go-live:** carga semanal con un monto medido (EDFAN: USD 75 por\n'
    'semana); la recarga automática (Perfil › Pagos › Saldo de tu cuenta) viene activada de fábrica,\n'
    'se avisa en el onboarding y se recomienda recién cuando el cliente ya sabe cuánto gasta por mes.\n'
    '> Actualización v1.31: antes decía "Recarga automática con piso: obligatoria en el go-live";\n'
    '> quedó derogado por el criterio de costos del 13/10/2026.\n')
sub(f'{D}/ahorro-de-tokens.md', '7. **Recarga automática con piso** en el go-live (restricción 8).',
    '7. **Cero cortes de saldo** en el go-live: carga semanal medida (restricción 8).\n'
    '   > Actualización v1.31: antes decía "Recarga automática con piso"; quedó derogado el 13/10/2026.')

# 4. Dos filas nuevas en la tabla de términos derogados (para que el auditor los busque siempre)
T = f'{D}/metodologia-correccion-agente.md'
sub(T, '| FAQ, Excepciones u Outlet como embudo | v1.12 / v1.18 | FAQ se responde dentro del embudo; excepción = tag; Outlet = condición del catálogo + variable de interés |',
    '| FAQ, Excepciones u Outlet como embudo | v1.12 / v1.18 | FAQ se responde dentro del embudo; excepción = tag; Outlet = condición del catálogo + variable de interés |\n'
    '| "Recarga automática con piso" como obligatoria o primer paso | v1.31 | Cero cortes con carga semanal medida; recarga automática cuando el cliente ya sabe cuánto gasta |\n'
    '| Tarifas de Meta en USD: "0,0618", "USD 0,026" | v1.31 | Rate card oficial en pesos, en `ic-costos-y-rentabilidad-de-prometheo` |')

# 5. CHANGELOG
CH = f'{R}/CHANGELOG.md'
sub(CH, '\n---\n\n## v1.30 - 23 octubre 2026',
    '\n---\n\n## v1.31 - 23 octubre 2026\n\n'
    '**Auditoría del ecosistema de skills.** Se compararon las skills sueltas instaladas contra sus\n'
    'copias en `02-skills/` y contra las skills de costos y calificación. La metodología estaba sana\n'
    'por dentro, pero tenía tres desajustes con el resto del ecosistema.\n\n'
    '**Corregido**\n'
    '- `SKILL.md` y `00-CONSULTA.md`: la auditoría web es el Paso 1.1 de la Etapa 1, no "Etapa 0"\n'
    '  (su propia skill ya lo decía).\n'
    '- `calificacion/ahorro-de-tokens-detalle.md`: reemplazado por la v1.1 de la skill suelta de\n'
    '  calificación (13/10). Tenía tarifas de Meta en USD, la recarga automática como palanca 1 y\n'
    '  USD 0,35 por conversación, los tres derogados.\n'
    '- `restricciones-plataforma-prometheo.md` (restricción 8) y `ahorro-de-tokens.md` (punto 7):\n'
    '  "recarga automática con piso obligatoria" pasa a "cero cortes con carga semanal medida".\n\n'
    '**Complementado**\n'
    '- `calificacion/00-criterio-calificacion.md`: sección 2.11 (score y guardiana en cada cambio) y su\n'
    '  ítem de checklist, más el puntero a la skill de costos. Venían de la v1.1 de la skill suelta.\n'
    '- `metodologia-correccion-agente.md`: dos filas nuevas en la tabla de términos derogados (recarga\n'
    '  automática con piso, tarifas de Meta en USD), para que `auditar.py` los busque en cada versión.\n\n'
    '**Fuera de esta skill (mismo día):** las skills sueltas `prometheo-*` se reinstalan desde\n'
    '`02-skills/`; `aurea-hub-criterio-calificacion-leads` queda como redirección a este módulo.\n\n'
    '**Auditado con scripts/auditar.py** (v1.30 → v1.31).\n\n'
    '**Sigue pendiente (decisión de Valen):** nombres de variables en formato natural vs snake_case.\n'
    '\n---\n\n## v1.30 - 23 octubre 2026')
print('v1.31 aplicada')
