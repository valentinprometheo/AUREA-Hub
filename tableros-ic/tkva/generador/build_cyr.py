# Costos y Rentabilidad · TKVA · mismo diseño que el documento de EDFAN, datos reales de TKVA
import re, json, sys
sys.path.insert(0, '../work')
from lib import num, pct
SRC = '/root/.claude/uploads/5cace1cd-6515-5715-a2db-3fed9a0ee26e/a7e6a924-Aurea_Hub_-_Costos_y_Rentabilidad_-_Template_EDFAN.html'
s = open(SRC, encoding='utf-8').read()
D = json.load(open('../work/D.json'))

HEAD = s[:s.find('<main class="container">')]
HEAD = HEAD.replace('EDFAN', 'TKVA')
def after(tag, start=0):
    i = s.find(tag, start); j = s.find('</svg>', i) + 6
    return s[s.find('<svg', i):j], j
# íconos de la plantilla
BAND, pos = [], 0
for _ in range(4):
    svg, pos = after('<div class="band-ic">', pos); BAND.append(svg)
CIC, pos = [], 0
for _ in range(3):
    svg, pos = after('<div class="c-ic">', pos); CIC.append(svg)
FEAT, pos = [], 0
for _ in range(2):
    svg, pos = after('<div class="feat-ic">', pos); FEAT.append(svg)
ICB, pos = [], 0
for _ in range(3):
    svg, pos = after('<div class="icb-ic">', pos); ICB.append(svg)
BADGE, _ = after('<span class="ic-badge">')
SEAL = {}
for m in re.finditer(r'<span class="ac-sic">', s):
    svg, j = after('<span class="ac-sic">', m.start())
    name = re.match(r'</span>(\w+)', s[j:]).group(1)
    SEAL.setdefault(name, svg)
KX = {}
for k in ('k1', 'k2', 'k3'):
    KX[k], _ = after(f'<span class="ac-cxi {k}">')
CHEV, _ = after('<span class="cl">Ocultar</span>')
LI, _ = after('<li><svg')
LI = s[s.find('<li><svg') + 4: s.find('</svg>', s.find('<li><svg')) + 6]
LOGO = re.search(r'<img class="hero-logo" src="[^"]+" alt="AUREA">', s).group(0)
ICIMG = re.search(r'<img class="iccard-img" src="[^"]+" alt="[^"]*">', s).group(0)
SPH = re.search(r'<div class="closer-sphere"><img src="[^"]+" alt=""></div>', s).group(0)
STROKE = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round">'
SEAL['Decidir'] = STROKE + '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/></svg>'
SEAL.setdefault('Separar', SEAL.get('Corregir'))
CHECK = STROKE + '<path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

def band(n, cls, eye, title, sub):
    return (f'<section class="sec band {cls}"><div class="band-in"><div class="band-num">{n}</div><div class="band-ic">{BAND[int(n)-1]}</div>'
            f'<div><div class="band-eye">{eye}</div><div class="band-title">{title}</div><div class="band-sub">{sub}</div></div></div></section>')
def callout(ic, eye, title, desc):
    return f'<div class="callout"><div class="c-ic">{ic}</div><div><div class="c-eye">{eye}</div><div class="c-title">{title}</div><div class="c-desc">{desc}</div></div></div>'
def feat(ic, label, title, desc):
    return f'<div class="feat"><div class="feat-ic">{ic}</div><div class="feat-label">{label}</div><div class="feat-title">{title}</div><div class="feat-desc">{desc}</div></div>'
def mcard(lbl, v, d, hi=False):
    return f'<div class="mcard{" hi" if hi else ""}"><div class="mc-lbl">{lbl}</div><div class="mc-v">{v}</div><div class="mc-d">{d}</div></div>'
def icb(ic, t, b, d):
    return f'<div class="icb"><div class="icb-ic">{ic}</div><div><div class="icb-t">{t} <b>{b}</b></div><div class="icb-d">{d}</div></div></div>'
def row(name, sub, val):
    return (f'<div style="display:flex;justify-content:space-between;gap:12px;align-items:baseline;border-bottom:1px solid rgba(31,27,46,.07);padding-bottom:8px">'
            f'<div><div style="font-size:13.5px;font-weight:700;color:#1F1B2E">{name}</div><div style="font-size:12px;color:#8783A0">{sub}</div></div>'
            f'<div style="font-size:15px;font-weight:700;color:#1F1B2E;white-space:nowrap">{val}</div></div>')
TCLS = {'Activar': ('t-act', 'o-ventas'), 'Corregir': ('t-corr', 'o-aurea'), 'Separar': ('t-sep', 'o-dir'), 'Decidir': ('t-dec', 'o-dir')}
OWNC = {'Ventas': 'o-ventas', 'AUREA': 'o-aurea', 'Dirección': 'o-dir', 'Marketing': 'o-mkt'}
def band_of(sc):
    return ('b-alta', 'Basada en datos') if sc >= 80 else ('b-media', 'Informada por datos') if sc >= 55 else ('b-hipo', 'Hipótesis con indicio') if sc >= 30 else ('b-crit', 'Criterio experto')
def ac(seal, owner, title, parts, mide, base, dato, ev_h, ev_rows, ev_n, prop, donde, efecto, medimos, why_extra=''):
    sc = sum(parts); bcls, blab = band_of(sc)
    if 'Modelado' in why_extra: sc = min(sc, 54); bcls, blab = band_of(sc)
    rows = ''.join(f'<div class="ac-ev-r"><span>{a} <i>{b}</i></span><b>{c}</b></div>' for a, b, c in ev_rows)
    why = ' · '.join(f'{n} {p}' for n, p in zip(['Base', 'Fuente', 'Cobertura', 'Profundidad', 'Evidencia', 'Cierre'], parts))
    return (f'<details class="ac {TCLS[seal][0]}"><summary><div class="ac-top"><span class="ac-seal"><span class="ac-sic">{SEAL[seal]}</span>{seal}</span>'
            f'<span class="ac-own {OWNC[owner]}">{owner}</span></div><div class="ac-nm">{title}</div>'
            f'<div class="ac-score {bcls}" style="--sc:{sc}"><strong>{sc}%</strong><span>basada en datos</span><em>{blab}</em><i></i></div>'
            f'<div class="ac-ctx"><div class="ac-cx"><span class="ac-cxi k1">{KX["k1"]}</span><span class="ac-k">Qué mide</span><span class="ac-v">{mide}</span></div>'
            f'<div class="ac-cx"><span class="ac-cxi k2">{KX["k2"]}</span><span class="ac-k">Base</span><span class="ac-v">{base}</span></div>'
            f'<div class="ac-cx"><span class="ac-cxi k3">{KX["k3"]}</span><span class="ac-k">Dato</span><span class="ac-v">{dato}</span></div></div>'
            f'<div class="ac-more"><span class="op">Ver evidencia y qué hacer</span><span class="cl">Ocultar</span>{CHEV}</div></summary>'
            f'<div class="ac-body"><div class="ac-row"><span class="ac-rk">La evidencia</span><div><div class="ac-ev"><div class="ac-ev-h">{ev_h}</div>{rows}<div class="ac-ev-n">{ev_n}</div></div></div></div>'
            f'<div class="ac-row"><span class="ac-rk">Nuestra propuesta</span><span>{prop}</span></div>'
            f'<div class="ac-row"><span class="ac-rk">Dónde</span><span>{donde}</span></div>'
            f'<div class="ac-row"><span class="ac-rk">Efecto</span><span>{efecto}</span></div>'
            f'<div class="ac-row"><span class="ac-rk">Cómo lo medimos</span><span>{medimos}</span></div>'
            f'<div class="ac-row"><span class="ac-rk">Por qué este score</span><span class="ac-why">{why} = <b>{sc}%</b>{why_extra}</span></div></div></details>')

# ---------- datos (todos del tablero de IC de TKVA, export 14/10/2026) ----------
G = D['gap']; B = D['B']; CAL_S, CAL_A = D['calif']; HOT, HOTSIN = D['hot'], D['hot_sin']
EV = D['env']; B2B = EV['inmo'] + EV['prov']
LT, WA = D['LT'], D['WA']
M = {m['m']: m for m in D['months']}
ago, sep, octo = M['2026-08'], M['2026-09'], M['2026-10']
ARS_S, ARS_M = 37.6798, 89.5620
PPD = 74.20 / 14
WEEKLY = round(PPD * 7 * 1.3 / 5) * 5          # ritmo de octubre × 7 días × 30% de colchón
ADSH = D['oct_ad'] / D['oct_n']
SC = [(2000, ADSH), (2700, ADSH), (3500, 0.0)]
SCV = [max(0, round(t * (1 - f)) - 1000) * ARS_S for t, f in SC]

# barras de consumo
vals = [('Agosto', 138.00, '269 conversaciones'), ('Septiembre', 62.48, '18 días sin procesar'), ('Octubre', 74.20, 'al 14')]
mx = 138.00
bars = ''
for i, (lab, v, sub) in enumerate(vals):
    h = 160 * v / mx; x = 50.33 + i * 186.67; cx = x + 43
    bars += (f'<rect x="{x:.1f}" y="{190-h:.1f}" width="86" height="{h:.1f}" rx="10" fill="url(#bar)"/>'
             f'<text x="{cx:.1f}" y="{181-h:.1f}" text-anchor="middle" font-family="Arimo,Helvetica,Arial" font-size="13" font-weight="700" fill="#1F1B2E">USD {num(v,2)}</text>'
             f'<text x="{cx:.1f}" y="209" text-anchor="middle" font-family="Arimo,Helvetica,Arial" font-size="12.5" fill="#4B4660">{lab}</text>'
             f'<text x="{cx:.1f}" y="225" text-anchor="middle" font-family="Arimo,Helvetica,Arial" font-size="10.5" fill="#8783A0">{sub}</text>')
CHART = ('<svg viewBox="0 0 560 230" width="100%" role="img" aria-label="Consumo de IA por mes"><defs><linearGradient id="bar" x1="0" y1="1" x2="0" y2="0">'
         '<stop offset="0" stop-color="#5B8FD9"/><stop offset=".6" stop-color="#7C5CBF"/><stop offset="1" stop-color="#F37D6E"/></linearGradient></defs>'
         '<line x1="0" y1="190" x2="560" y2="190" stroke="rgba(31,27,46,.14)"/>' + bars + '</svg>')
OCT = [('Respuesta del asistente', 'lo que contesta el agente', 52), ('Extracción de datos', 'completar variables', 27), ('Smart Tags', 'asignar etiquetas', 15),
       ('Detección de bots, testing y otros', 'soporte de la plataforma', 5)]

H = []
H.append(f'''<main class="container"><section class="hero"><div class="brand-lockup">{LOGO}</div>
<div class="hero-eyebrows"><span class="eyebrow"><span class="ob"></span>Master Partner Oficial de Prometheo</span><span class="eyebrow"><span class="ob"></span>TKVA · Octubre 2026</span></div>
<h1>Costos y rentabilidad <em>de Prometheo</em>.</h1>
<div class="minidx"><span class="minidx-i"><span class="minidx-n">01</span>Costo variable · WhatsApp</span><span class="minidx-i"><span class="minidx-n">02</span>Tokens de IA</span><span class="minidx-i"><span class="minidx-n">03</span>Calificación</span><span class="minidx-i"><span class="minidx-n">04</span>Posibles mejoras</span></div>
<p class="lead">Cuatro puntos para ponernos al día: el cambio de precios de WhatsApp (que por su conexión por API sí los alcanza), cómo consume el agente el saldo de IA, lo que aprendimos de sus leads y las posibles mejoras que salen de esos datos.</p></section>''')

# 01 · WhatsApp
H.append(band('01', 'bv', 'Costo variable · WhatsApp', 'Meta cobra por mensaje, solo por API', 'Es un cambio de Meta para todas las cuentas conectadas por API. TKVA está conectada por API: este cambio sí entra en su factura.'))
H.append(f'''<section class="sec tv"><div class="sec-head"><span class="eyebrow"><span class="ob"></span>Qué cambió el 1° de octubre</span>
<h2>Su cuenta va por API: <em>desde octubre, Meta cobra las respuestas</em>.</h2>
<p>Desde el 1° de octubre, Meta cobra cada respuesta que sale por la API oficial, la del agente y la de Vanesa, con 1.000 respuestas gratis por mes por número. TKVA está conectada por API, así que desde este mes hay un costo de WhatsApp que antes no existía. Lo factura Meta directo a TKVA, en pesos, aparte de Prometheo.</p></div>
<div style="margin-bottom:16px">{callout(CIC[0], 'Su conexión · API oficial', 'Hay costo por mensaje, con 1.000 respuestas gratis por mes.', 'Lo que envían el agente y Vanesa por la API paga a Meta pasadas las primeras 1.000 del mes. Las charlas que llegan desde un anuncio Click to WhatsApp tienen 72 h gratis si se responden dentro de las 24 h y el contacto escribe desde el celular.')}</div>
<div class="grid-2">{feat(FEAT[0], 'Tarifas', 'Cuánto cuesta cada mensaje', 'ARS 37,68 por cada respuesta del agente o del equipo (servicio) y por cada plantilla de utilidad, después de las primeras 1.000 del mes. ARS 89,56 por cada mensaje de una campaña de marketing. Precios de lista, más impuestos.')}
{feat(FEAT[1], 'Escenario · cálculo', 'Cuánto les puede costar por mes', f'Entre <b>ARS {num(SCV[0])}</b> y <b>ARS {num(SCV[2])}</b>, según cuántas respuestas salgan por mes (entre 2.000 y 3.500) y cuántas charlas lleguen desde un anuncio (32% en octubre). El número real sale de la factura de Meta de octubre.')}</div>
<div class="grid-2" style="margin-top:16px">{feat(CIC[1], 'Lo que da la API', 'Para operar a escala', 'Es más estable. Permite plantillas aprobadas para escribir después de 24 h, campañas masivas (en Enterprise) y Meta Forms, y el primer mensaje a los leads de formulario. Los seguimientos fuera de la ventana de 24 h necesitan plantilla.')}
{feat(CIC[2], 'Lo que daría el QR', 'Para atención uno a uno', 'No paga por mensaje y permite asistente, Smart Tags, variables y seguimientos, pero depende de una sesión vinculada que puede desconectarse. No permite campañas masivas, plantillas oficiales ni Meta Forms. La decisión es de ustedes: la vemos juntos con estos números.')}</div>
<p style="font-size:12px;color:var(--ink-3);margin-top:14px">Fuente: tarifas oficiales de Meta en pesos para Argentina, vigentes desde el 1/10/2026, más impuestos. Escenario calculado por AUREA sobre el export de Prometheo al 14/10/2026: no es factura.</p></section>''')

# 02 · Tokens
H.append(band('02', 'bm', 'Tokens de IA', 'Su consumo de IA', 'El otro costo variable es el saldo de IA en Prometheo. Qué consume el agente, en qué se va cada dólar y qué pasó entre el 29/08 y el 15/09.'))
H.append(f'''<section class="sec tv"><div class="sec-head"><span class="eyebrow"><span class="ob"></span>Panel "Entendé tu consumo" · agosto a octubre</span>
<h2>Septiembre gastó menos <em>porque el agente casi no procesó durante 18 días</em>.</h2>
<p>El consumo bajó de USD 138,00 en agosto a USD 62,48 en septiembre porque entre el 29/08 y el 15/09 el agente no cargó resumen, tags ni variables, no porque la IA se volviera más barata. En octubre, con el agente procesando, van USD 74,20 al día 14.</p></div>
<div class="grid-2" style="align-items:stretch"><div class="feat" style="padding:22px 24px 16px"><div class="feat-label">Consumo de IA por mes</div>{CHART}</div>
<div class="feat" style="padding:22px 24px 16px"><div class="feat-label">En qué se va cada dólar · octubre al 14</div><div style="display:grid;gap:10px;margin-top:6px">
{''.join(row(n, sub, f'USD {num(74.20 * p / 100, 2)} · {p}%') for n, sub, p in OCT)}</div>
<p style="font-size:11.5px;color:#8783A0;margin-top:8px">Porcentajes del panel de Prometheo (suman 99% por redondeo).</p></div></div>
<div class="grid-3" style="margin-top:16px">
{mcard('Por conversación', 'USD 0,23 a 0,51', 'Octubre USD 0,23 (USD 74,20 en 325 conversaciones) y agosto USD 0,51 (USD 138,00 en 269). Septiembre no se calcula: el agente no procesó 18 días. Para proyectar usamos USD 0,40.')}
{mcard('Por día · octubre', f'≈ USD {num(PPD, 2)}', 'USD 74,20 en 14 días. A este ritmo, octubre cerraría entre USD 145 y USD 165.')}
{mcard('Lo que no se registró', f'{G["sinproc"]} charlas', f'Sin resumen, tags ni variables entre el 29/08 y el 15/09. {G["noresp"]} contactos sin ninguna respuesta y {G["ad"]} que llegaron por un anuncio.', True)}</div>
<div style="margin-top:16px">{callout(CIC[1], 'Insight', 'Quedarse sin procesar, simbólicamente, sale caro.', f'Entendemos que el saldo es un costo a administrar mes a mes, y por eso queremos mostrarles en qué impacta un corte. <strong>En la atención:</strong> {G["noresp"]} personas no recibieron respuesta en esos días y {G["ad"]} habían llegado por un anuncio, es decir, ya habían costado pauta. <strong>En la lectura:</strong> {G["sinproc"]} conversaciones quedaron sin datos; por eso septiembre parece calificar {sep["cal"]} contra {ago["cal"]} de agosto, cuando sobre lo procesado califica parecido ({pct(sep["cal"], sep["b"])} contra {pct(ago["cal"], ago["b"])}), y octubre vuelve al {pct(octo["cal"], octo["b"])}.')}</div>
<div style="margin-top:12px">{callout(CIC[2], 'Cómo se arma el gasto', 'Crear tags y variables no consume. Lo que consume es que la IA los evalúe.', 'En octubre, extracción de datos y Smart Tags son el 42% del gasto. La extracción analiza cada charla para decidir si asigna un tag o guarda una variable, y consume aunque al final no asigne nada: por ejemplo, "asesor asignado" se evalúa en cada conversación y está vacío a propósito, porque Vanesa atiende todos los leads. Lo que se gestiona a mano no consume. El detalle está en Mi Perfil › Saldo disponible › Entendé tu consumo.')}</div></section>''')

# 03 · Calificación
H.append(band('03', 'bv', 'Calificación', 'Ahora sabemos cómo califican sus leads', 'Casi tres meses de conversaciones reales (22/07 al 14/10) nos mostraron cómo se comportan sus consultas. Con eso, la calificación ya se puede llevar al CRM.'))
nf = D['nofit_m']; nfn = sum(v for k, v in nf.items() if k != 'Sin motivo claro')
Z = D['zona2']
H.append(f'''<section class="sec tm"><div class="sec-head"><span class="eyebrow"><span class="ob"></span>Crecemos con ustedes</span>
<h2>Esto no se veía el primer día. <em>Hacía falta que sus leads hablaran.</em></h2></div>
<div class="iccard">{ICIMG}<div class="iccard-body"><div class="iccard-k"><span class="ic-badge">{BADGE}</span>Nuevo producto de AUREA</div>
<div class="iccard-t">Leído con Inteligencia Comercial</div><div class="iccard-d">Cruza su CRM con sus anuncios y lee cada conversación con un criterio de calificación de desarrollista (el mismo que usa EDFAN Real Estate, a validar con ustedes). El detalle completo está en su tablero de Inteligencia Comercial.</div></div></div>
<div style="margin-top:30px"><span class="eyebrow"><span class="ob"></span>Insights de ustedes</span></div>
<div class="icbul" style="margin-top:14px">
{icb(ICB[0], 'WhatsApp directo califica el doble que el formulario', f'{pct(WA["cal"], WA["b"])} contra {pct(LT["cal"], LT["b"])}', f'{WA["cal"]} de {WA["b"]} conversaciones de WhatsApp califican, contra {LT["cal"]} de {LT["b"]} que llegan por el formulario de LT.')}
{icb(ICB[1], 'Piden Núñez', pct(Z["Núñez"], D["zona_n"]), f'{Z["Núñez"]} de las {D["zona_n"]} que dicen barrio. Maker Núñez es el proyecto más pedido: {D["d_proy"]["Maker Núñez"]} consultas.')}
{icb(ICB[2], 'El precio frena', '1.er motivo de No Fit', f'{nf["Precio fuera de presupuesto"]} de los {nfn} No Fit con un motivo claro hablan de precio. En Liberti, 37 consultas terminaron en No Fit.')}</div>
<div class="grid-3" style="margin-top:16px">
{mcard('Califican · criterio EDFAN', f'{CAL_S} a {CAL_A} · {pct(CAL_S, B)} a {pct(CAL_A, B)}', f'De {B} conversaciones de compra procesadas. Dijeron proyecto o barrio, una tipología que existe y dos datos más. Es un rango porque falta el catálogo de Tokko.')}
{mcard('Son hot leads', f'{HOT} · {pct(HOT, B)}', f'De {B}: dieron al menos una señal de compra. {HOTSIN} ({pct(HOTSIN, B)}) todavía sin próximo paso.')}
{mcard('El tag "Calificado" coincide', f'{D["tagcal_ok"]} de {CAL_A}', f'{D["tagcal"]} contactos tienen el tag y solo {D["tagcal_ok"]} cumplen la regla. El seguimiento sí funciona: {D["calif_seg"]} de {CAL_A} calificados tienen próximo paso.', True)}</div></section>''')

# 04 · Posibles mejoras
H.append(band('04', 'bv', 'Posibles mejoras', 'Dónde mejorar sin perder ventas', 'Cada mejora sale de un dato, con su dueño y su score. Tocá cada card para ver qué hacer, dónde y qué efecto esperamos.'))
cards_a = (ac('Activar', 'Ventas', f'Hot leads · {HOTSIN} ya dieron una señal de compra y nadie los retomó', [14, 10, 7, 10, 10, 15],
              'Hot leads sin seguimiento, derivación ni etapa del equipo', f'{HOT} hot leads, 22/07 al 14/10', 'Variables y resumen que cargó la IA',
              'Qué señal dejó cada uno (la IA ya la guardó)',
              [('Preguntó por una unidad concreta', 'Tokko o el resumen nombra la unidad', D['hot_sig']['unidad']), ('Compra ya o en el corto plazo', 'lo dice el resumen', D['hot_sig']['ya']),
               ('Tiene el dinero o pregunta por contado', 'forma de pago = contado', D['hot_sig']['contado']), ('Vuelve sobre la misma unidad', 'no medible hoy', 'sin dato')],
              'La IA detectó la señal y la dejó en el CRM. Lo que falta no es el dato: es un tag "Hot Lead" que lo marque y le avise a Vanesa. Hoy ese tag no existe.',
              'Creamos el tag Hot Lead con aviso inmediato a Vanesa y se los dejamos en la bandeja, empezando por los de octubre, listos para retomar.',
              'Tag "Hot Lead" con notificación · bandeja de chats', f'{HOTSIN} hot leads con un próximo paso registrado en la quincena.',
              'Hot leads sin próximo paso, misma base, al 31/10. Guardiana: tiempo de respuesta de Vanesa.')
           + ac('Corregir', 'AUREA', f'Calificado · el tag y la regla coinciden en {D["tagcal_ok"]} de {CAL_A} calificados', [20, 10, 7, 15, 10, 15],
                'Leads que cumplen la regla frente a los que tienen el tag', f'{B} conversaciones de compra procesadas', 'Variables que cargó la IA',
                'Por qué califican (criterio de referencia)',
                [('Dijeron proyecto o barrio que TKVA vende', 'obligatorio', D['obl1']), ('Pidieron una tipología que existe', 'obligatorio', D['obl2']),
                 ('Dieron al menos 2 de 4 datos que suman', 'finalidad, forma de pago, etc.', CAL_A), ('Tienen el tag "Calificado" y cumplen la regla', 'hoy', D['tagcal_ok'])],
                f'{CAL_A - D["tagcal_ok"]} cumplen la regla sin el tag y {D["tagcal"] - D["tagcal_ok"]} tienen el tag sin cumplirla. El seguimiento funciona igual porque lo hace Vanesa, pero la pauta y los avisos aprenden de una etiqueta que dice otra cosa.',
                'Llevamos la regla al tag "Calificado" por lotes con Mi Prometheo, con un lote chico auditado primero, y ajustamos el prompt del tag para que use la regla.',
                'Mi Prometheo · prompt del Smart Tag "Calificado"', 'Tag y criterio coinciden en al menos 8 de cada 10 calificados.',
                'Tag "Calificado" contra criterio, misma base, al 30/11. Guardiana: que la definición no se afloje.'))
H.append(f'''<section class="sec tv"><div class="subtag"><span class="subtag-n">A</span><span class="eyebrow" style="margin:0"><span class="ic-badge">{BADGE}</span>Inteligencia Comercial dice</span></div>
<div class="sec-head"><h2>Retomar los hot leads <em>y que el CRM diga lo mismo que la conversación</em>.</h2>
<p>Es lo más importante de este informe. El seguimiento ya funciona: {D["calif_seg"]} de {CAL_A} calificados tienen próximo paso. Con Inteligencia Comercial encontramos lo que falta: {HOTSIN} hot leads que dieron una señal de compra y nadie retomó, y una etiqueta de calificado que no sigue la regla. El trabajo de ordenarlo es nuestro.</p></div>
<div class="cycle"><div class="cyc"><span class="cyc-n">01</span><div class="cyc-t">Analizamos</div><div class="cyc-d">Leemos cada charla con el criterio de calificación.</div></div>
<div class="cyc"><span class="cyc-n">02</span><div class="cyc-t">Recalificamos</div><div class="cyc-d">Llevamos ese criterio a los tags, por lotes, con Mi Prometheo.</div></div>
<div class="cyc"><span class="cyc-n">03</span><div class="cyc-t">Recuperamos</div><div class="cyc-d">Activamos el aviso sobre los hot leads sin próximo paso.</div></div>
<div class="cyc"><span class="cyc-n">04</span><div class="cyc-t">Comunicamos</div><div class="cyc-d">Vanesa recibe el lead con su señal y su próximo paso.</div></div></div>
<div class="acg" style="margin-top:22px">{cards_a}</div></section>''')
H.append(f'''<section class="askband"><div class="askin"><div class="subtag"><span class="subtag-n subtag-w">B</span><span class="ask-eye">Lo que necesitamos de ustedes</span></div>
<h2 class="ask-h">Su OK y su saldo, <em>para recalificar con Mi Prometheo</em>.</h2>
<p class="ask-p">La recalificación masiva se hace con Mi Prometheo, la herramienta de la plataforma que aplica cambios por lotes, y consume saldo de su cuenta. Con su aprobación, ejecutamos:</p>
<div class="ask-grid"><div class="ask-it"><span class="ask-n">1</span><div>Llevar la regla al tag <b>Calificado</b>: hoy coinciden {D["tagcal_ok"]} de {CAL_A}.</div></div>
<div class="ask-it"><span class="ask-n">2</span><div>Crear el tag <b>Hot Lead</b> con aviso inmediato a Vanesa.</div></div>
<div class="ask-it"><span class="ask-n">3</span><div>Volver a leer las <b>{G["sinproc"]} conversaciones</b> que quedaron sin procesar entre el 29/08 y el 15/09.</div></div></div>
<div class="ask-row"><span class="ask-cta">Carga semanal sugerida: <b>USD {WEEKLY}</b></span><span class="ask-note">Es el ritmo de consumo de octubre (USD {num(PPD, 2)} por día) con un 30% de colchón, para que el agente no vuelva a quedarse sin procesar. El costo de cada lote de Mi Prometheo lo informamos antes de correrlo.</span></div></div></section>''')
cards_c = (
    ac('Corregir', 'AUREA', f'Agente · {G["sinproc"]} conversaciones sin registrar entre el 29/08 y el 15/09', [20, 10, 15, 10, 10, 15],
       'Conversaciones de compra sin resumen ni variables', f'{G["n"]} contactos que entraron del 29/08 al 15/09', 'Export de Prometheo + panel de consumo',
       'Lo que pasó en esos 18 días',
       [('Contactos que entraron', 'del 29/08 al 15/09', G['n']), ('Conversaron', '2 o más mensajes', G['convo']), ('Sin resumen, tags ni variables', 'sin procesar por la IA', G['sinproc']),
        ('Sin ninguna respuesta', 'ningún mensaje de TKVA', G['noresp']), ('Llegaron por un anuncio', 'ya costaron pauta', G['ad'])],
       'Coincide con la caída del consumo de septiembre (−55%). Las variables las carga la IA sola: por eso estas conversaciones quedaron sin ningún dato y ningún filtro las alcanza.',
       f'Cargar un monto semanal medido, unos USD {WEEKLY} por semana, y avisarnos antes de pausar el agente por cualquier motivo, así pausamos también la pauta.',
       'Perfil › Pagos › Saldo de tu cuenta', 'Cero días sin procesar en noviembre.', 'Conversaciones sin procesar por semana, al 30/11. Guardiana: costo por conversación.')
    + ac('Decidir', 'Dirección', 'Formularios · unos 220 leads por mes esperan que alguien los tome a mano', [14, 10, 15, 15, 5, 10],
         'Leads de formulario (LT · Go High Level) y cómo califican frente a WhatsApp', f'{LT["b"]} conversaciones de LT procesadas · {WA["b"]} de WhatsApp', 'Export de Prometheo + resumen técnico con LT',
         'Lo que muestran los datos',
         [('Califican desde el formulario de LT', f'{LT["cal"]} de {LT["b"]}', pct(LT['cal'], LT['b'])), ('Califican desde WhatsApp directo', f'{WA["cal"]} de {WA["b"]}', pct(WA['cal'], WA['b'])),
          ('Contactos de LT del 01 al 07/10', 'reporte semanal de Vanesa', '54'), ('Los mismos días, en Prometheo', 'canal de origen LT', '25')],
         'El lead de formulario no manda un mensaje, así que el agente no lo atiende hasta que Vanesa lo toma. Una parte ni siquiera entra a Prometheo.',
         'Elegir el camino: integración de Go High Level a Prometheo o Meta Forms (para los formularios de Facebook e Instagram), que crean el lead y le escriben primero con una plantilla; o, mientras tanto, primer mensaje desde Go High Level o carga del contacto con su origen. Y pasar el remarketing a Click to WhatsApp.',
         'Go High Level (LT) · Prometheo › Integraciones › Meta Forms · Administrador de anuncios',
         'Que los leads de formulario entren solos, con su origen, y reciban el primer mensaje también el fin de semana.',
         f'Leads de LT en Prometheo y % que conversa, al 30/11. Guardiana: costo de plantillas de Meta (unos ARS {num(220 * ARS_S)} por mes en utilidad).')
    + ac('Corregir', 'AUREA', 'Tags y variables · algunas se evalúan en cada charla y casi no se usan', [8, 5, 15, 10, 10, 15],
         'Gasto de IA en extracción y Smart Tags', 'USD 74,20 de octubre al 14', 'USD 20,03 extracción + USD 11,13 Smart Tags',
         'Variables que se evalúan y casi no se completan',
         [('Asesor asignado', 'vacío a propósito', '0%'), ('Historial', 'en las conversaciones de compra', '0%'), ('Fecha de visita', '1 contacto', '0,1%'), ('Email', '12 contactos', '2%')],
         'Crear una variable no consume; consume que la IA la evalúe en cada charla. Lo que no se usa puede pasar a carga manual. La fecha de visita no: se completa al marcar la visita.',
         'Pedir a Mi Prometheo qué tags y variables tienen prompt de IA, y pasar a manual lo que casi nunca se completa. Las variables que califican se dejan automáticas.',
         'Mi Prometheo · Contactos › Variables', 'Extracción y Smart Tags por debajo del 30% del gasto en noviembre.',
         'Porcentaje del panel y USD por conversación, noviembre contra octubre. Guardiana: cobertura de las variables que califican.')
    + ac('Decidir', 'Dirección', 'WhatsApp · API o QR, con el costo de Meta a la vista', [8, 0, 0, 15, 5, 10],
         'Costo de Meta de la línea de ventas frente a lo que habilita la API', 'Mensajes enviados en octubre, estimados desde el export', f'ARS {num(SCV[0])} a {num(SCV[2])} por mes [cálculo]',
         'Qué da cada camino',
         [('API: plantillas, campañas y Meta Forms', 'costo por mensaje', 'Sí'), ('API: primer mensaje a leads de formulario', 'resuelve LT', 'Sí'),
          ('QR: sin costo de Meta', 'sesión vinculada que puede desconectarse', 'Sí'), ('QR: campañas y plantillas oficiales', 'no disponibles', 'No')],
         'El costo de Meta es un escenario: el export no trae los mensajes por fecha ni por categoría y todavía no hay factura. Por eso el score es bajo y la decisión es de ustedes.',
         'Decidir con la factura de octubre en la mano: si necesitan plantillas, campañas o los formularios, quedarse en API y cuidar el cupo; si alcanza con atención uno a uno, evaluar el QR.',
         'Prometheo › Canales · WhatsApp', 'Una decisión escrita con el costo de cada camino.', 'Factura de Meta de octubre contra el escenario.', ' · dato modelado: techo 54'))
H.append(f'''<section class="sec tv"><div class="subtag"><span class="subtag-n">C</span><span class="eyebrow" style="margin:0"><span class="ob"></span>Más puntos de mejora</span></div>
<div class="sec-head"><h2>Mejoras diseñadas <em>con el mismo nivel de exactitud</em>.</h2>
<p>Además de los leads, el análisis marcó ajustes de configuración y consumo. Cada uno sale de un dato de su cuenta y baja el gasto o limpia la medición, sin tocar la calidad de la atención.</p></div>
<div style="margin-bottom:16px">{callout(CHECK, 'Mejora continua · ya hecha', 'Línea B2B aparte: el agente ya no gasta saldo en inmobiliarias y proveedores.', f'En el período, el agente les mandó {num(B2B)} mensajes a inmobiliarias y proveedores ({pct(B2B, EV["total"])} de todo lo que envió TKVA). A pedido de ustedes se abrieron dos líneas: ventas con agente y B2B sin agente. El efecto lo medimos el próximo período.')}</div>
<div class="acg">{cards_c}</div></section>''')
H.append(f'''<section class="sec tm"><div class="sec-head"><span class="eyebrow"><span class="ob"></span>Cómo seguir</span>
<h2>Medir con datos y <em>mejorar continuamente</em>.</h2><p>Dos formas de llevar estas mejoras a la práctica, según lo que necesiten.</p></div>
<div class="grid-2"><div class="price grad"><div class="price-lbl">Nuevo producto de AUREA</div><div class="price-title">Inteligencia Comercial</div><div class="price-val">Desde USD 200 / mes</div>
<ul><li>{LI}<span>Hoy el tablero lee su CRM. Para cerrar el círculo del Ecosistema Comercial con IA, sumamos su canal de Meta</span></li>
<li>{LI}<span>Con la inversión de sus anuncios, el reporte que hoy arma Vanesa a mano sale solo, con costo por contacto, por entrevista y por venta</span></li>
<li>{LI}<span>Así las decisiones se basan en datos y cada insight se puede ejecutar</span></li><li>{LI}<span>Un canal incluido; USD 50 por cada canal extra</span></li></ul></div>
<div class="price"><div class="price-lbl">Siempre hay algo para mejorar, continuamente</div><div class="price-title">Mejora Continua</div><div class="price-val">Start USD 150 · Pro USD 250 / mes</div>
<ul><li>{LI}<span>Este tipo de trabajo es parte de Mejora Continua: afinamos al agente, medimos y ejecutamos las mejoras. Hoy tienen el plan Start</span></li>
<li>{LI}<span><strong>Start:</strong> estabilidad: estrategia y ajustes del agente y del CRM, con el consumo controlado. <strong>Pro:</strong> escalabilidad: cartera completa, funciones nuevas e integraciones entre plataformas</span></li>
<li>{LI}<span>Las integraciones nativas (como Go High Level a Prometheo) son desarrollo y se cotizan aparte</span></li><li>{LI}<span>Cada función nueva llega con su costo estimado antes de activarla</span></li></ul></div></div></section>''')
H.append(f'''<section class="closer"><div class="closer-text" style="text-align:left"><span class="eyebrow"><span class="ob"></span>En una línea</span>
<h2>Generamos, convertimos y medimos. <em>Cada vez más valor</em>.</h2>
<ul class="closer-list"><li>Marketing trae la demanda, Ventas la convierte e Inteligencia Comercial lee qué funcionó, para que el próximo círculo rinda más que el anterior.</li>
<li>El detalle completo, pestaña por pestaña, está en su tablero de Inteligencia Comercial.</li></ul></div>{SPH}</section>
<footer><div class="fm"><span class="mini-orb"></span>AUREA Hub · Master Partner Oficial de Prometheo CRM</div><div>TKVA · Valores de referencia, no promesas · Tablero de IC, export del 14/10/2026 · Panel de consumo al 14/10 · Tarifas: Meta, ARS 1/10/2026</div></footer></main></body></html>''')
out = HEAD + ''.join(H)
open('/home/user/AUREA-Hub/tableros-ic/tkva/AUREA_Hub_-_Costos_y_Rentabilidad_-_TKVA.html', 'w', encoding='utf-8').write(out)
print('ok', len(out.encode()), 'weekly', WEEKLY, 'scv', [round(x) for x in SCV], 'seals', list(SEAL))
