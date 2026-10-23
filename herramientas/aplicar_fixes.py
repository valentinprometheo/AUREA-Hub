"""Aplica las correcciones de la auditoría del 23/10/2026 sobre una copia de trabajo de las skills.
Cada reemplazo se verifica: si el texto esperado no está, el script frena."""
import os, re, shutil, sys

N = sys.argv[1]  # carpeta "nueva"
os.chdir(N)
log = []


def rd(p):
    return open(p, encoding='utf-8').read()


def wr(p, s):
    open(p, 'w', encoding='utf-8').write(s)


def sub_once(p, old, new):
    s = rd(p)
    assert s.count(old) == 1, f'{p}: esperaba 1 vez, hay {s.count(old)} de {old[:60]!r}'
    wr(p, s.replace(old, new))
    log.append(f'{p}: reemplazo puntual')


def append_after(p, anchor, extra):
    s = rd(p)
    assert s.count(anchor) == 1, f'{p}: ancla {anchor[:50]!r} aparece {s.count(anchor)} veces'
    wr(p, s.replace(anchor, anchor + extra))
    log.append(f'{p}: agregado')


# ---------- 1. Skills prometheo-* sueltas = copia vigente de la metodología ----------
MET = 'aurea-metodologia/references/02-skills'
for d in sorted(x for x in os.listdir('.') if x.startswith('prometheo-')):
    src = [os.path.join(r, d) for r, ds, _ in os.walk(MET) if d in ds][0]
    body = rd(os.path.join(src, 'SKILL.reference.md'))
    shutil.rmtree(d)
    os.makedirs(d)
    wr(os.path.join(d, 'SKILL.md'), body)
    log.append(f'{d}: sincronizada con {src}')

# ---------- 2. Nombres de skills que ya no existen ----------
RENOMBRES = {
    'aurea-hub-costos-rentabilidad': 'ic-costos-y-rentabilidad-de-prometheo',
    'aurea-dashboard-design': 'aurea-ic-dashboard-design',
    'aurea-curaduria-dato': 'aurea-ic-curaduria-del-dato',
    'prometheo-correccion-prompts': 'aurea-prometheo-corrección-prompts',
    'aurea-email-prometheo': 'aurea-ic-email-marketing',
    'aurea-whatsapp-prometheo': 'aurea-ic-whatsapp-marketing',
}
HISTORIA = ('CHANGELOG', 'HISTORIAL', 'hallazgos', 'aprendizajes')
for r, _, fs in os.walk('.'):
    for f in fs:
        if not f.endswith('.md') or any(h in f for h in HISTORIA):
            continue
        p = os.path.join(r, f)
        s = rd(p)
        n = s
        for a, b in RENOMBRES.items():
            n = re.sub(r'(?<![\w-])' + re.escape(a) + r'(?![\w-])', b, n)
        if n != s:
            wr(p, n)
            log.append(f'{p}: nombres de skills actualizados')

# ---------- 3. Costos: "pendiente 149 vs 150" -> fuente única ----------
COSTO_OLD = 'Plan pendiente de unificar: USD 149 vs 150.'
COSTO_NEW = ('Costos de plataforma: fuente única en `ic-costos-y-rentabilidad-de-prometheo` '
             '(Enterprise USD 149 recomendado, no es piso; IA se proyecta con USD 0,40).')
for p in ['aurea-estetica-documentacion/references/estetica-deck.md',
          'aurea-estetica-documentacion/references/estetica-deck-system.md',
          'documentos-client-facing/references/04-presentacion-estetica.md',
          'documentos-client-facing/references/04-presentacion-estetica-system.md',
          'aurea-deck-design/references/design-system.md',
          'aurea-deck-design/SKILL.md']:
    sub_once(p, COSTO_OLD, COSTO_NEW)
sub_once('aurea-estetica-documentacion/references/nuevos-servicios.md',
         '- Plan de plataforma: desde ~USD 149/150 por canal + tokens (pendiente de unificar 149 vs 150 en copy; confirmá el número vigente antes de escribirlo).',
         '- Plan de plataforma: **plan recomendado Enterprise (USD 149/mes)**, más saldo de IA y mensajes de Meta aparte. '
         'No se escribe "desde USD 149" ni "Licencia USD 150" (derogados el 13/10/2026). Fuente única: '
         '`ic-costos-y-rentabilidad-de-prometheo`; ante cualquier cifra, se lee de ahí.')
append_after('aurea-estetica-documentacion/references/sistema-drakon.md',
             '## La regla fundamental (misma doctrina que el NDA): CLONAR, no reconstruir\n',
             '\n> **Cifras del ejemplo (actualización 23/10/2026).** El ejemplo de oro es la propuesta real que se le\n'
             '> mandó a DRAKON: sus precios son de ese cliente y de esa fecha (Licencia USD 150, tokens USD 0,30 a\n'
             '> 0,45), hoy derogados. Al clonar, **se clona la estructura, nunca las cifras**: todo precio se\n'
             '> reemplaza por el vigente de `ic-costos-y-rentabilidad-de-prometheo` y el modelo de paquetes vigente.\n')

# ---------- 4. Una familia, una estética: decks a aurea-estetica-documentacion ----------
RUTEO = ('\n> **Ruteo (actualización 23/10/2026).** Todo deck, propuesta, presupuesto, guía o one-pager con la\n'
         '> estética AUREA se arma con `aurea-estetica-documentacion`, que tiene el sistema DRAKON completo\n'
         '> (`aurea-drakon.css`, bandas, price cards, íconos). Esta skill trae solo el kit reducido: si el\n'
         '> pedido es un deck, derivá allá. Lo que se queda acá: {resto}.\n')
for p, resto in [('documentos-client-facing/SKILL.md',
                  'el ruteo por familia y las familias 1, 2, 3 (Diseño de CRM, Carga de Contactos, Guión de Testing)'),
                 ('aurea-deck-design/SKILL.md', 'nada nuevo; se conserva como referencia histórica del one-pager PDF')]:
    s = rd(p)
    i = s.find('\n---', 4) + 4  # fin del frontmatter
    j = s.find('\n#', i)
    j = s.find('\n', j + 1) + 1  # después del primer título
    wr(p, s[:j] + RUTEO.format(resto=resto) + s[j:])
    log.append(f'{p}: ruteo a aurea-estetica-documentacion')

# ---------- 5. Corrección de prompts: chequeo 8 (+9) como en la metodología ----------
CP = 'aurea-prometheo-corrección-prompts'
sub_once(f'{CP}/SKILL.md', 'completa. Siete chequeos. Detalle',
         'completa. Ocho chequeos, más el 9 cuando hay rondas anteriores de feedback (igual que '
         '`metodologia-correccion-agente.md` de `aurea-metodologia`). Detalle')
sub_once(f'{CP}/SKILL.md', 'Obligatorio, siete chequeos, antes de entregar.',
         'Obligatorio, ocho chequeos (más el 9 cuando aplica), antes de entregar.')
sub_once(f'{CP}/SKILL.md', '| Barrido de coherencia (los 7 chequeos, con la evidencia que los originó) |',
         '| Barrido de coherencia (los 8 chequeos más el 9, con la evidencia que los originó) |')
B = f'{CP}/references/02-barrido-de-coherencia.md'
sub_once(B, '## Los siete chequeos', '## Los ocho chequeos (más el 9 cuando aplica)')
sub_once(B, '\n---\n\n## Cuándo se corre y qué pasa si falla',
         '\n---\n\n### 8 · Chequeo de compatibilidad con la versión del proveedor\n\n'
         'Si Prometheo (ITESA) entregó una reescritura del prompt, antes de activarla se verifica qué reglas\n'
         'nuestras conservó, cuáles perdió y qué contradicciones metió. Se compara regla por regla contra la\n'
         'última versión de AUREA y contra la hoja "No regresión (lo sagrado)" de la matriz. Lo perdido se\n'
         'repone por sector completo; lo contradictorio se resuelve con el chequeo 2. Gestión del proveedor en\n'
         '`gestion-proveedor-itesa.md` de `aurea-metodologia`.\n\n'
         '### 9 · Verificación acumulada de feedback (cuando aplica)\n\n'
         'Cuando hay rondas anteriores, cada corrección reportada por el cliente sigue verificada contra el\n'
         'texto vigente, con resultado X/X por bloque. Incluye lo que debe estar AUSENTE y sigue ausente (un\n'
         'dato retirado, un proyecto dado de baja).\n\n'
         '> Actualización 23/10/2026: esta skill tenía siete chequeos; se alinea con los 8 (+9) de la\n'
         '> metodología. Los chequeos 1 a 7 no cambian.\n'
         '\n---\n\n## Cuándo se corre y qué pasa si falla')
sub_once(B, 'Recién con 7 de 7 en OK se arma la entrega y se completa el campo `Barrido de coherencia:\n  OK (7/7)`',
         'Recién con 8 de 8 en OK (9 de 9 cuando aplica) se arma la entrega y se completa el campo `Barrido de coherencia:\n  OK (8/8)`')
M = f'{CP}/references/03-matriz-auditoria.md'
s = rd(M)
if 'Los siete chequeos' in s:
    wr(M, s.replace('Los siete chequeos', 'Los ocho chequeos (más el 9 cuando aplica)'))
    log.append(f'{M}: ocho chequeos')

print('\n'.join(log))
print(f'\n{len(log)} cambios')
