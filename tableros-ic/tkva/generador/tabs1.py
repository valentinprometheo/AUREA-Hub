# Pestañas 1 a 6 · TKVA
PANELS = []
HOT, HOT_SIN = D['hot'], D['hot_sin']
CALSIN = D['calif_sin']; CALSEG = D['calif_seg']
LT, WA, IG = D['LT'], D['WA'], D['IG']
PER_DAY_OCT = oct_['n'] / 14; PER_DAY_SEP = sep['n'] / 30
RNG = f'{CAL_S} a {CAL_A}'
CIT = 'Prometheo · export 14/10'

# ================= cards de acción compartidas =================
A_CORTE = act('corregir', 'AUREA', [20, 10, 15, 10, 10, 15],
    f'Agente sin procesar · {num(G["sinproc"])} conversaciones sin registrar entre el 29/08 y el 15/09',
    'Conversaciones de compra sin resumen, tags ni variables de la IA',
    f'{num(G["n"])} contactos que entraron del 29/08 al 15/09',
    f'{G["sinproc"]} sin procesar · {G["ad"]} llegaron por un anuncio · {G["noresp"]} sin ninguna respuesta', f'{CIT} y panel de consumo',
    'Cargar un monto semanal medido (≈ USD 50 por semana: el ritmo de octubre de USD 5,30 por día con 30% de colchón) y avisar a AUREA antes de pausar el agente por cualquier motivo. La Posible mejora 0 confirma qué pasó en esos 18 días.',
    'Prometheo › Perfil › Pagos › Saldo de tu cuenta · Posible mejora 0',
    'Cero días sin procesar en noviembre: ninguna conversación sin resumen por falta de saldo o por pausa.',
    'Conversaciones sin procesar y días sin procesar, al 30/11.', 'costo por charla procesada (no tiene que subir).',
    f'El hueco se ve en un campo del sistema (Resumen por IA) en {G["sinproc"]} de {G["convo"]} conversaciones y coincide con la caída del consumo de septiembre (−55%). Falta confirmar si fue saldo o una pausa: por eso Profundidad 10. La carga medida se usa con métrica en EDFAN.',
    'Hecho', mcard='start')
A_HOT = act('activar', 'Ventas', [14, 10, 7, 10, 10, 15],
    f'Hot leads · {HOT_SIN} con una señal de compra y sin próximo paso',
    'Hot leads (criterio EDFAN, una señal alcanza) sin seguimiento, derivación ni etapa del equipo',
    f'{HOT} hot leads del 22/07 al 14/10', f'{HOT_SIN} sin próximo paso · {D["hot_sig"]["unidad"]} preguntaron por una unidad concreta', CIT,
    'Que Vanesa los retome antes que al resto, empezando por los de octubre, con la unidad que preguntaron a mano. En paralelo, crear el tag Hot Lead con aviso inmediato (Posible mejora 2).',
    'Tag "Hot Lead" con notificación a Vanesa (Posible mejora 2) · bandeja de chats',
    f'{HOT_SIN} hot leads con un próximo paso registrado en la quincena.',
    'Hot leads sin próximo paso, misma base, al 31/10.', 'tiempo de respuesta de Vanesa al aviso (hoy no se ve en el export).',
    'Las señales se leen en el resumen de la IA y en Propiedades de Tokko (17%): se cuenta lo que se ve. "Compra ya" casi no aparece porque TKVA no tiene una variable de plazo. En EDFAN se usa con métrica.',
    'Señal')
A_FORM = act('decidir', 'Dirección', [14, 10, 15, 15, 5, 10],
    'Formularios de LT · 220 leads por mes esperan que alguien los tome a mano',
    'Leads de formulario (LT · Go High Level) y cómo califican frente a WhatsApp',
    f'{LT["b"]} conversaciones de LT procesadas · {WA["b"]} de WhatsApp',
    f'LT califica {LT["cal"]} de {LT["b"]} ({pct(LT["cal"], LT["b"])}) · WhatsApp {WA["cal"]} de {WA["b"]} ({pct(WA["cal"], WA["b"])}) · {LT["nofit"]} No Fit desde LT',
    f'{CIT} · resumen técnico TKVA × LT',
    'Elegir el camino. <b>A</b>: integración Go High Level → Prometheo, o Meta Forms nativo para los formularios instantáneos de Facebook e Instagram (requiere API oficial y Enterprise, que TKVA ya tiene): el lead se crea solo y el agente escribe primero con una plantilla. Es integración entre plataformas: <b>MC · Pro</b>. <b>B o C</b>, mientras tanto: primer mensaje desde Go High Level, o carga automática del contacto con su origen. Es estrategia y configuración: <b>MC · Start</b>. Y pasar el remarketing a Click to WhatsApp directo.',
    'Go High Level (LT) · Prometheo › Integraciones › Meta Forms · Administrador de anuncios',
    'Que los ≈ 220 leads de formulario por mes entren a Prometheo con su origen y reciban el primer mensaje sin esperar a Vanesa, también el fin de semana.',
    'Leads con canal LT en Prometheo y % que conversa, al 30/11.',
    '% de calificación de LT con el criterio EDFAN (que no baje al entrar más volumen) y costo de plantillas de Meta.',
    'Canal Origen está cargado en el 96% de las conversaciones procesadas. Los 220 por mes salen del resumen técnico con LT (agosto). Ninguna de las vías se probó todavía en la cuenta: Evidencia 5.',
    'Hecho', mcard='pro')
A_CALTAG = act('corregir', 'AUREA', [20, 10, 7, 15, 10, 15],
    f'Calificado · {D["tagcal"]} con el tag y {RNG} con el criterio EDFAN',
    'Leads que cumplen la regla frente a los que tienen el tag', f'{B} conversaciones de compra procesadas',
    f'solo {D["tagcal_ok"]} coinciden · {CAL_A - D["tagcal_ok"]} cumplen sin el tag · {D["tagcal"] - D["tagcal_ok"]} con el tag sin cumplir', CIT,
    'Llevar el criterio al tag "Calificado" por lotes con Mi Prometheo (Posible mejora 3) y que el prompt del tag use la regla (dos obligatorios y al menos dos sumas), no la impresión del agente.',
    'Mi Prometheo · prompt del Smart Tag "Calificado" (Posible mejora 3)',
    'Tag y criterio coinciden en al menos 8 de cada 10 calificados.', 'Tag "Calificado" contra criterio, misma base, al 30/11.',
    'que la definición no cambie ni se afloje.',
    'Los obligatorios están en Señal (proyecto 74%, tipología 72%). Sin el catálogo de Tokko el criterio es un rango. En EDFAN se corrigió igual.',
    'Señal', mcard='start')
A_CAP = act('corregir', 'AUREA', [20, 10, 15, 15, 5, 15],
    f'Capacidad de pago · {D["drop"][2]} cumplen los obligatorios y no llegan a dos sumas',
    'Conversaciones que no califican solo por falta de sumas', f'{B} conversaciones de compra procesadas',
    f'Forma de pago {num(D["cov"]["Forma de pago"][1],0)}% · presupuesto real {num(D["cov"]["Presupuesto (sin ceros)"][1],0)}% · {D["pres_cero"]} presupuestos guardados en 0', CIT,
    'Al final de la charla, después de proyecto y tipología, una sola pregunta de capacidad: "¿Pensás financiar o pagar de contado?" o "¿Con cuánto anticipo contás?". Y que el presupuesto quede vacío si el lead no lo dice, nunca en 0.',
    'Prompt del agente, sección de calificación · prompt de la variable de presupuesto (Posible mejora 5)',
    'Forma de pago por encima del 40% de las conversaciones procesadas.',
    'Cobertura de forma de pago y calificados (criterio EDFAN), misma base, al 30/11.',
    '% de conversaciones que se cortan después de la pregunta (no tiene que subir).',
    'Conteo del sistema sobre toda la base procesada. Preguntar el anticipo es buena práctica del rubro (pozo con anticipo de 30% a 40%), sin prueba previa en la cuenta.',
    'Hecho', mcard='start')
A_APIQR = act('decidir', 'Dirección', [8, 0, 0, 15, 5, 10],
    'WhatsApp por API o por QR · desde el 1/10 Meta cobra cada respuesta por API',
    'Costo de Meta de la línea de ventas frente a lo que habilita la API',
    'mensajes enviados en octubre (estimado a partir del export)',
    '≈ ARS 14.000 a 94.000 por mes según escenario · 1.000 respuestas gratis por número', 'Cálculo AUREA sobre tarifa oficial de Meta',
    'Decidir si TKVA necesita lo que solo da la API: plantillas para escribir después de 24 h, campañas masivas (Enterprise), Meta Forms y el primer mensaje a los leads de formulario. Si los necesita, quedarse en API y cuidar el cupo. Si alcanza con atención uno a uno y seguimiento, el QR no paga por mensaje, pero depende de una sesión vinculada que puede desconectarse.',
    'Prometheo › Canales · WhatsApp (API oficial o QR)',
    'Una decisión escrita con el costo de cada camino antes de la factura de Meta de octubre.',
    'Factura de Meta de octubre contra el escenario de esta pestaña.', 'que no se pierdan los leads de formulario (los resuelve la API).',
    'El costo de Meta es un escenario: el export no trae mensajes por fecha ni por categoría y todavía no hay factura. Por eso Fuente 0 y techo de dato modelado.',
    'Modelado', adv=True)

# ================= 1 · PANORAMA =================
wk_n = [w['n'] for w in WEEKS]
def path(vals, w=600, h=150, pad=6, top=14, bot=135):
    mx = max(vals); n = len(vals)
    pts = [(pad + (w - 2 * pad) * i / (n - 1), bot - (bot - top) * v / mx) for i, v in enumerate(vals)]
    return ' '.join(f'{"M" if i == 0 else "L"} {x:.0f} {y:.0f}' for i, (x, y) in enumerate(pts)), pts
pth, pts = path(wk_n)
wk_sp = [w['sinproc'] for w in WEEKS]
spk = ' '.join(f'{4 + 292 * i / (len(wk_sp) - 1):.0f},{56 - 50 * v / max(wk_sp):.0f}' for i, v in enumerate(wk_sp))
proy_top = max(D['d_proy'], key=D['d_proy'].get)

hero = (f'<div class="hero-grid"><div class="hero"><div class="hero-sph sph-bg"></div><div class="hero-top"><span class="hero-kick">Panorama · octubre 2026 al 14</span>'
        f'<span class="hero-per">comparado con septiembre</span></div>'
        f'<div class="hero-h">El agente volvió a procesar. Octubre califica como agosto.</div><div class="hero-sub">'
        + BA(f'Entraron <b>{oct_["n"]} consultas</b> en 14 días ({num(PER_DAY_OCT)} por día, {num(PER_DAY_SEP)} en septiembre). Cuando el agente procesa la conversación, califica <b>{num(100*oct_["cal"]/oct_["b"])} de cada 100</b>, igual que en agosto. Entre el 29/08 y el 15/09 no cargó datos: <b>{G["sinproc"]} conversaciones</b> quedaron sin resumen, tags ni variables.',
             f'<b>{oct_["n"]} consultas</b> del 1 al 14/10 ({num(PER_DAY_OCT,1)} por día; septiembre {num(PER_DAY_SEP,1)}). Calificación sobre conversaciones procesadas, criterio EDFAN en lectura amplia: <b>{cal_rate(oct_)}</b> en octubre, {cal_rate(sep)} en septiembre (sobre solo {sep["b"]} procesadas) y {cal_rate(ago)} en agosto. Lectura estricta: {pct(oct_["cal_s"], oct_["b"])} en octubre.')
        + f'</div><div class="chart-scale"><span>Consultas por semana · máx {max(wk_n)} · la primera es el arranque (22/07) y la última va hasta el 14/10</span><span>más es mejor ↑</span></div>'
        f'<div class="hchart"><svg viewBox="0 0 600 150" preserveAspectRatio="none" role="img"><defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'
        f'<path d="{pth} L 594 150 L 6 150 Z" fill="url(#hg)"/><path d="{pth}" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>'
        f'<circle cx="594" cy="{pts[-1][1]:.0f}" r="4.5" fill="#fff"/></svg><div class="endtag" style="top:calc({pts[-1][1]/150*100:.0f}% - 4px)">{wk_n[-1]}<span>sem. 12/10 (parcial)</span></div></div>'
        '<div class="chart-x"><span>20 jul</span><span>10 ago</span><span>31 ago</span><span>21 sep</span><span>12 oct</span></div>'
        f'<div class="hero-stats"><div class="hs"><div class="l">Consultas por día · oct</div><div class="v">{num(PER_DAY_OCT)}</div><div class="m">{oct_["n"]} del 1 al 14</div></div>'
        f'<div class="hs"><div class="l">Calificados · criterio EDFAN</div><div class="v">{RNG}</div><div class="m">del 22/07 al 14/10 · {D["tagcal"]} con el tag</div></div>'
        f'<div class="hs"><div class="l">Proyecto más pedido</div><div class="v">{proy_top}</div><div class="m">{D["d_proy"][proy_top]} consultas · {pct(D["d_proy"][proy_top], D["proy_n"])} de las que dicen proyecto</div></div></div></div>'
        f'<div class="hero-pink"><div class="hp-top"><div class="hp-row"><div class="hp-ic">{I("alert")}</div><span class="hp-chip">Agente sin procesar 29/08 – 15/09</span></div>'
        f'<svg class="hp-spk" viewBox="0 0 300 60" preserveAspectRatio="none" role="img"><polyline points="{spk}" fill="none" stroke="rgba(255,255,255,.85)" stroke-width="2" vector-effect="non-scaling-stroke" stroke-linejoin="round"/></svg>'
        f'<div><div class="hp-l">Conversaciones sin registrar · por semana, máx {max(wk_sp)}</div><div class="hp-v">{G["sinproc"]}</div>'
        f'<div class="hp-d"><span class="pin">18 días</span> del 29/08 al 15/09 · el agente no cargó datos</div></div></div>'
        f'<div class="hp-foot"><div class="mini"><b>{G["n"]}</b><span>Contactos en esos días</span></div><div class="hp-sp"></div>'
        f'<div class="mini"><b style="color:var(--warn)">{G["ad"]}</b><span>Llegaron por un anuncio</span></div><div class="hp-sp"></div>'
        f'<div class="mini"><b>{G["noresp"]}</b><span>Sin ninguna respuesta</span></div></div></div></div>')

d_ppd = 100 * (PER_DAY_OCT - PER_DAY_SEP) / PER_DAY_SEP
kp = ('<div class="g4">'
      + kpi('chat', 'blu', 'pro', 'Consultas · octubre al 14', str(oct_['n']), f'{num(d_ppd)}% por día', 'd-bad', 'down',
            'Personas que escribieron por WhatsApp o Instagram del 1 al 14/10.',
            f'{num(PER_DAY_OCT,1)} por día contra {num(PER_DAY_SEP,1)} en septiembre ({sep["n"]} en el mes).',
            '<b>Consulta</b>: contacto nuevo en Prometheo, por fecha de ingreso. Es el conteo maestro.')
      + kpi('checkc', '', 'calc', 'Tasa de calificación', cal_rate(oct_), f'+{num(100*oct_["cal"]/oct_["b"] - 100*sep["cal"]/sep["b"])} p.p.', 'd-good', 'up',
            f'De cada 100 conversaciones que la IA procesó en octubre, {num(100*oct_["cal"]/oct_["b"])} califican.',
            f'{oct_["cal"]} de {oct_["b"]} procesadas (estricta {oct_["cal_s"]}) · septiembre {sep["cal"]} de {sep["b"]} · agosto {ago["cal"]} de {ago["b"]}.', CALDEF)
      + kpi('alert', 'amb', 'calc', 'Conversaciones sin procesar', str(oct_['sinproc']), f'−{sep["sinproc"] - oct_["sinproc"]}', 'd-good', 'down',
            'Escribieron 2 o más mensajes y la IA no dejó resumen ni variables.',
            f'{oct_["sinproc"]} en octubre · {sep["sinproc"]} en septiembre · {ago["sinproc"]} en agosto (desde el 29/08).',
            'Menos es mejor. Se mide por la ausencia del <b>Resumen por IA</b>.')
      + kpi('target', 'pnk', 'pro', 'Con anuncio identificado', pct(oct_['ad'], oct_['n']), f'+{num(100*oct_["ad"]/oct_["n"] - 100*sep["ad"]/sep["n"])} p.p.', 'd-good', 'up',
            'Consultas que se pueden atribuir a un anuncio de Meta.',
            f'{oct_["ad"]} de {oct_["n"]} en octubre · septiembre {sep["ad"]} de {sep["n"]}. El resto entra por formulario, por WhatsApp directo o sin ID.',
            'Atribución por <b>ID de anuncio</b> que Meta pasa a Prometheo.')
      + '</div>')

ads = D['ads']; noad = D['noad']; TOT = D['total']
top_ads = [(a['name'][:46] + ('…' if len(a['name']) > 46 else ''), a['n']) for a in ads[:5]]
otros = sum(a['n'] for a in ads[5:])
mx = max(n for _, n in top_ads)
inb = ''.join(bar(esc(l), num(n), pct(n, TOT), 100 * n / mx, 'var(--src-meta)') for l, n in top_ads)
inb += bar(f'Otros {len(ads) - 5} anuncios', num(otros), pct(otros, TOT), 100 * otros / mx, 'var(--src-meta)')
canal = D['d_canal']
noad_rows = bar('Sin anuncio identificado<span class="stc sc-off">Faltante</span>', num(noad['n']), pct(noad['n'], TOT), 100, miss=True)
origin = (f'<div class="qbd" style="margin-top:10px">De las {num(noad["n"])} sin anuncio, el agente registró el canal de origen declarado: '
          f'WhatsApp directo {canal["WhatsApp"]}, Instagram {canal["Instagram"]}, formulario de LT {canal["LT"]}, cartel {canal["cartel"]}, web {canal["web"]} (sobre las conversaciones procesadas). '
          f'{pct(noad["nodem"], noad["n"])} de las que entran sin anuncio no son demanda.</div>')
inout = (sec('Origen de la demanda · inbound') + '<div class="inout"><div class="qci pad"><div class="io-h"><div class="io-ic" style="background:var(--grad)">'
         + I('inb') + f'</div><div><b>Inbound · el lead escribe primero</b><span>Contactos del 22/07 al 14/10, por anuncio de entrada</span></div>'
         f'<div class="tot"><b>{num(TOT)}</b><span>contactos</span></div></div><div class="mkgrid two"><div><div class="subl"><span class="dot2" style="background:var(--src-meta)"></span>Meta Ads · anuncio identificado</div>'
         + inb + '</div><div><div class="subl"><span class="dot2" style="background:var(--pnk)"></span>Sin atribución</div>' + noad_rows + origin + '</div></div>'
         + qbd('Meta trae a la persona hasta el clic. Desde ahí, el agente de Prometheo responde, informa el proyecto y la entrega, y califica.',
               f'Atribución por ID de anuncio (primer anuncio registrado en el contacto). {pct(noad["n"], TOT)} de los contactos no tiene anuncio: en TKVA es más alto que en otras cuentas porque una parte de la pauta va a la landing y a los formularios de LT, que no pasan el ID. Canal Origen lo completa la IA en el 96% de las conversaciones procesadas (dato autodeclarado).')
         + '</div>')
cq = D['canal_q']
qrows = [('WhatsApp directo', cq['WhatsApp']), ('Instagram', cq['Instagram']), ('Formulario LT', cq['LT'])]
qmx = max(100 * v[1] / v[0] for _, v in qrows)
qual = ''.join(bar(l, pct(v[1], v[0]), f'{v[1]} de {v[0]}', 100 * (100 * v[1] / v[0]) / 40, 'var(--good)') for l, v in qrows)
inout += (f'<div class="qci pad"><div class="io-h"><div class="io-ic" style="background:var(--grad)">{I("checkc")}</div><div><b>Calidad por canal de origen</b>'
          f'<span>De cada 100 conversaciones de compra procesadas, cuántas califican</span></div><div class="tot"><b>{pct(CAL_A, B)}</b><span>promedio</span></div></div>'
          + qual + qbd('WhatsApp directo califica el doble que el formulario de LT. Por anuncio, el detalle está en la pestaña Meta.',
                       'Criterio EDFAN, lectura amplia. Barras escaladas a 40% para que se lean las diferencias. Instagram trae más consultas de una sola pregunta (precio, ubicación).')
          + '</div></div>')

rec = (sec('Recorrido · de la consulta al cierre') + '<div class="qci pad"><div class="qbj">' + I('route') + 'De la consulta al cierre · el recorrido completo'
       f'<span class="r">Meta ve hasta el clic · Prometheo, del clic al cierre · base: consultas de compra del 22/07 al 14/10</span></div>'
       + recorrido([('chat', num(D['compra']), 'Consultas de compra', 'sin inmobiliarias, proveedores ni No Fit', False),
                    ('pulse', num(D['convo']), 'Conversaron', f'{pct(D["convo"], D["compra"])} respondió al agente', False),
                    ('bot', num(B), 'Procesadas por la IA', f'{pct(B, D["convo"])} de las que conversaron', True),
                    ('checkc', RNG, 'Calificadas', f'{pct(CAL_A, B)} de las procesadas', False),
                    ('repeat', str(CALSEG), 'Con seguimiento o derivación', f'{pct(CALSEG, CAL_A)} de las calificadas', False),
                    ('cal', str(D['humana']), 'Visita, negociación o cierre', f'tag del equipo · {D["tags"]["Convertido"][1]} "Convertido"', True)])
       + qbd(f'El agente califica y Vanesa sigue: <b>{CALSEG} de {CAL_A}</b> calificados tienen próximo paso. El corte está antes: <b>{D["sinproc"]}</b> conversaciones que la IA no procesó, casi todas entre el 29/08 y el 15/09.',
             f'Pasos 01 a 05 por lo que dejó la conversación, con el criterio de calificación de EDFAN. 06 depende de que se marque el tag: de los {D["tags"]["Convertido"][0]} "Convertido", {D["tags"]["Convertido"][0] - D["tags"]["Convertido"][1]} son inmobiliarias o clientes que ya habían comprado, así que no hay tasa de cierre posible. Es un faltante de proceso, no de demanda.')
       + '</div>')

pano = ('<section class="panel p-panorama"><div class="iobar"><span class="iohint">Export de Prometheo al 14/10/2026 · 1.470 contactos · datos reales</span></div>'
        + hero + kp + inout + rec + sec('Qué hago ahora · acciones con dueño y score') + legend() + mclegend()
        + acts([A_CORTE, A_HOT, A_FORM, A_CALTAG.replace('class="i3 av"', 'class="i3 av adv"', 1), A_CAP.replace('class="i3 av"', 'class="i3 av adv"', 1), A_APIQR], 6)
        + yeq(f'La demanda está y el agente volvió a procesar: octubre califica como agosto. Primero, que no vuelva a quedarse sin procesar; después, los {HOT_SIN} hot leads sin próximo paso, y decidir la vía de los formularios de LT, que hoy entran por fuera.')
        + '</section>')
PANELS.append(pano)

# ================= 2 · EVOLUCIÓN =================
cutx = (f'<div class="cutx"><div class="cutx-h"><span class="cutx-ic">{I("bolt")}</span><div><span class="cutx-k">El insight del período</span>'
        f'<b>18 días sin procesar parecen ahorro. <em>En realidad es pauta que nadie registró.</em></b>'
        f'<p>Del 29/08 al 15/09 el agente no cargó resumen, tags ni variables. El consumo de septiembre bajó 55% (USD 62,48) porque el agente casi no procesó, no porque cada charla costara menos.</p></div></div>'
        f'<div class="cutx-g"><div><span>{I("layers")}Deja de extraer datos</span><b>{G["sinproc"]}</b><p>conversaciones sin resumen, tags ni variables. Sin extracción no hay calificación ni aviso de hot lead: septiembre parece calificar poco solo por eso.</p></div>'
        f'<div><span>{I("anun")}Pauta sin registrar</span><b>{G["ad"]}</b><p>contactos de esos días llegaron por un anuncio. 69 de los 74 de «Los espacios cobran vida…» cayeron en el hueco.</p></div>'
        f'<div><span>{I("pulse")}Qué no cambia</span><b>{cal_rate(oct_)}</b><p>de calificación cuando el agente procesa, en agosto y en octubre. La demanda no se cortó: se cortó el registro.</p></div></div>'
        f'<div class="cutx-f">{I("arrow")}<span>Acción: carga semanal medida y aviso antes de pausar el agente. Detalle en Consumo variable CRM.</span></div></div>')
subt = (f'<div class="subtabs evtabs"><label for="ev-ventas">{I("chat")}Consultas</label><label for="ev-deuda">{I("checkc")}Calificación</label>'
        f'<label for="ev-tags">{I("bot")}Carga de la IA</label><label for="ev-cons">{I("tag")}Tags por mes</label></div>')
days = {'2026-07': 10, '2026-08': 31, '2026-09': 30, '2026-10': 14}
mlab = {'2026-07': 'julio (desde el 22)', '2026-08': 'agosto', '2026-09': 'septiembre', '2026-10': 'octubre (al 14)'}
ev1 = ('<div class="stab st-ventas"><div class="g4">'
       + kpi('chat', 'blu', 'pro', 'Consultas · septiembre', str(sep['n']), f'+{pct(sep["n"] - ago["n"], ago["n"])}', 'd-flat', 'up', f'contra {ago["n"]} de agosto')
       + kpi('cal', '', 'pro', 'Consultas · octubre al 14', str(oct_['n']), '14 días', 'd-flat', None, f'{num(PER_DAY_OCT)} por día · septiembre: {num(PER_DAY_SEP)} por día')
       + kpi('target', 'pnk', 'pro', 'Con anuncio · octubre', str(oct_['ad']), f'{pct(oct_["ad"], oct_["n"])}', 'd-flat', None, f'septiembre {sep["ad"]} ({pct(sep["ad"], sep["n"])})')
       + kpi('x', 'amb', 'calc', 'No-demanda · octubre', str(oct_['nodem']), f'{pct(oct_["nodem"], oct_["n"])}', 'd-flat', None,
             'inmobiliarias, proveedores, postventa, equipo y No Fit', f'{oct_["nodem_b2b"]} son inmobiliarias o proveedores.')
       + '</div>' + qci('trend', 'Consultas por semana', 'pro', 'barras: contactos nuevos · resaltada: semana actual (parcial)',
                         barchart(wl, [wk_n], 300, SHADE, legend_items=[('var(--vio)', 'Contactos de la semana'), ('var(--crit)', 'Semana con el agente sin procesar'),
                                                                     (None, 'La semana del 20/07 incluye el arranque: 118 contactos el 22/07, 41 de ellos inmobiliarias que ya conocían a Vanesa')]))
       + '<div class="mt">' + table(['Mes', 'Consultas', 'Por día', 'Con anuncio', 'No-demanda', 'Sin respuesta del agente'],
                                   [[mlab[m['m']], num(m['n']), num(m['n'] / days[m['m']], 1), f'{m["ad"]} · {pct(m["ad"], m["n"])}', num(m['nodem']), num(m['noresp'])] for m in D['months']], 640)
       + qbd('"Sin respuesta del agente": contactos a los que TKVA no les mandó ningún mensaje.', 'En julio es alto por el arranque: contactos de Vanesa que escribieron el primer día y que ella atendió por fuera. El conteo sale de "Msgs enviados" = 0.')
       + '</div></div>')
ev2 = ('<div class="stab st-deuda"><div class="g4">'
       + ''.join(kpi('checkc', 'grn' if m['cal'] / max(m['b'], 1) >= .2 else '', 'calc', f'Calificación · {mlab[m["m"]].split(" ")[0]}', cal_rate(m), None, '', None,
                     f'{m["cal"]} de {m["b"]} conversaciones procesadas · estricta {m["cal_s"]}') for m in D['months'])
       + '</div>' + qci('checkc', 'Calificados por semana', 'calc', 'barras: calificados con el criterio EDFAN (amplia) · base: conversaciones de compra',
                         barchart(wl, [[w['cal'] for w in WEEKS]], 20, SHADE, legend_items=[('var(--vio)', 'Calificados · criterio EDFAN'), ('var(--crit)', 'Semana con el agente sin procesar'), (None, 'Las caídas coinciden con el hueco del agente, no con menos demanda')]))
       + qbd('Los calificados caen en las semanas del 31/08, 07/09 y 14/09. En esas mismas semanas la IA no procesó las conversaciones. Sobre lo procesado, la tasa se mantiene entre 15% y 22% por mes.',
             CALDEF + ' Se calcula sobre las variables cargadas: no depende de que alguien marque el tag. Julio es más bajo porque incluye el arranque.')
       + '</div>')
ev3 = ('<div class="stab st-tags">' + qci('bot', 'Conversaciones por semana · procesadas y sin procesar', 'pro', 'base: consultas de compra que escribieron 2 o más mensajes',
                                          barchart(wl, [[w['proc'] for w in WEEKS], [w['sinproc'] for w in WEEKS]], 140, SHADE, colors=['var(--vio)', 'var(--crit)'], stacked=True, highlight_last=False,
                                                   legend_items=[('var(--vio)', 'Procesadas por la IA'), ('var(--crit)', 'Sin resumen ni variables de la IA')]))
       + '<div class="mt">' + table(['Período', 'Contactos que entraron', 'Conversaron', 'Sin procesar por la IA', 'Sin ninguna respuesta', 'Con anuncio'],
                                   [['29/08 – 15/09', G['n'], G['convo'], G['sinproc'], G['noresp'], G['ad']],
                                    ['resto del período', num(D['total'] - G['n']), num(D['convo'] - G['convo']), D['sinproc'] - G['sinproc'], D['noresp'] - G['noresp'], D['con_ad'] - G['ad']]], 640)
       + qbd('Un solo hueco, de 18 días: el agente deja de resumir y de cargar variables. La mayoría de los contactos igual recibió respuesta, por eso el problema no se vio en el chat sino en el CRM.',
             'Hipótesis: saldo de IA agotado o agente pausado. El panel de consumo de septiembre baja 55% (USD 62,48) y la semana del 22 al 28/09 ya muestra el agente reactivado. Se confirma con la Posible mejora 0. Mientras tanto, ningún filtro por variable de Mi Prometheo alcanza a estos contactos.')
       + '</div></div>')
TM = D['tagsm']
ev4 = ('<div class="stab st-cons">' + table(['Tag · por mes de ingreso del contacto', 'Julio', 'Agosto', 'Septiembre', 'Octubre al 14'],
                                           [[t] + [TM[t][m] for m in ['2026-07', '2026-08', '2026-09', '2026-10']] for t in TM], 620)
       + qbd(f'"Sin tags" sube a {TM["Sin tags"]["2026-09"]} en septiembre: son los contactos del hueco. "Calificado" se usó en julio ({TM["Calificado"]["2026-07"]}) y casi no se usa desde agosto, aunque la IA califica todos los meses.',
             'Conteo de contactos con el tag, según el mes en que ingresó el contacto (no el mes en que se puso el tag: el export no trae esa fecha).')
       + '</div>')
evo = ('<section class="panel p-evolucion">' + head('Evolución · semana a semana', 'Consultas, calificación y carga de la IA,', 'semana a semana.',
                                                  'Primero, <b>cuántas consultas entraron</b>. Después, cuántas <b>procesó la IA</b> y cuántas calificaron.',
                                                  'Semanas de lunes a domingo, por fecha de ingreso. La primera arranca el 20/07 (el agente se activó el 22/07) y la última llega hasta el 14/10 (parcial).')
       + cutx + subt + ev1 + ev2 + ev3 + ev4
       + yeq(f'Septiembre parece calificar peor ({sep["cal"]} contra {ago["cal"]} de agosto), pero la IA procesó {sep["b"]} de sus {sep["convo"]} conversaciones: es efecto del hueco, no de la demanda. Octubre, con el agente procesando, vuelve al {cal_rate(oct_)}.')
       + '</section>')
PANELS.append(evo)

# ================= 3 · VENTA · CRM =================
dp = D['drop']
cqb = (f'<div class="cq"><div class="cq-top"><div><div class="cq-k">{I("compass")}Criterio de calificación · referencia EDFAN</div>'
       f'<div class="cq-t">Así califica TKVA con la regla de EDFAN, <em>medido en sus conversaciones.</em></div>'
       '<div class="cq-s">TKVA todavía no tiene una definición propia: por indicación de AUREA se usa la de EDFAN Real Estate (mismo rubro) como <b>propuesta a validar con Vanesa</b>. Dos obligatorios y al menos 2 de los 4 que suman. El hot lead se marca con una sola señal; el pedido de visita es una etapa, no una señal.</div></div>'
       f'<div class="cq-nums"><div><b>{RNG}</b><span>calificados</span><i>estricta a amplia</i></div><div><b>{HOT}</b><span>hot leads</span><i>{HOT_SIN} sin próximo paso</i></div>'
       f'<div><b>{D["visita"]}</b><span>pidieron visita o reunión</span><i>{D["visita_tag"]} con tag de visita</i></div></div></div>'
       f'<div class="cq-rule"><div class="cq-col"><h6>Obligatorios · los dos</h6><span class="ch ob">Proyecto o zona que TKVA comercializa <b>{D["obl1"]}</b></span><span class="ch ob">Tipología que existe <b>{D["tip_any"]}</b></span></div>'
       f'<div class="cq-plus">+</div><div class="cq-col"><h6>Suman · al menos 2 de 4</h6><span class="ch su">Intención de compra <b>{D["s_int"]}</b></span><span class="ch su">Finalidad <b>{D["s_fin"]}</b></span>'
       f'<span class="ch su">Presupuesto o forma de pago <b>{D["s_cap"]}</b></span><span class="ch su">Estado de obra compatible <b>s/d</b></span></div>'
       f'<div class="cq-plus">|</div><div class="cq-col"><h6>Hot lead · con 1 señal</h6><span class="ch ho">Unidad concreta <b>{D["hot_sig"]["unidad"]}</b></span><span class="ch ho">Compra ya o pronto <b>{D["hot_sig"]["ya"]}</b></span>'
       f'<span class="ch ho">Contado o anticipo <b>{D["hot_sig"]["contado"]}</b></span><span class="ch ho">Vuelve sobre la misma unidad <b>s/d</b></span></div></div>'
       f'<p class="cq-note">Cantidades sobre las {B} conversaciones de compra procesadas del 22/07 al 14/10.</p>'
       f'<div class="cq-grid"><div class="cq-box"><h6>{I("filter")}Dónde se cae la calificación</h6><div class="cq-steps">'
       + ''.join(f'<div class="cq-st"><b>{v}</b><span>{t}</span><i style="width:{100*v/B:.1f}%"></i></div>' for v, t in [(B, 'conversaron y se procesaron'), (D['obl1'], 'con proyecto o zona'), (D['obl2'], 'con tipología que existe'), (CAL_A, 'con 2 sumas o más')])
       + f'</div><p>{dp[0]} sin proyecto ni zona con proyecto · {dp[1]} sin tipología · {dp[2]} con menos de 2 sumas.</p></div>'
       f'<div class="cq-box"><h6>{I("layers")}Lo que marca el CRM y lo que dice la conversación</h6><div class="cq-cmp">'
       f'<div><span>Calificado</span><b>{D["tagcal"]}</b><i>con tag</i><b>{RNG}</b><i>por criterio</i></div>'
       f'<div><span>Hot lead</span><b>0</b><i>con tag</i><b>{HOT}</b><i>por criterio</i></div>'
       f'<div><span>Pedido visita/reunión</span><b>{D["visita_tag"]}</b><i>con tag</i><b>{D["visita"]}</b><i>por criterio</i></div></div>'
       f'<p>El tag "Calificado" y el criterio casi no coinciden: solo {D["tagcal_ok"]} contactos tienen las dos cosas. No existe un tag de hot lead. Las mejoras 1 a 3 llevan el criterio a los tags.</p></div>'
       f'<div class="cq-box"><h6>{I("target")}Dentro de los calificados · criterio comercial</h6>'
       + bar(f'Objeción, dolor, evento disparador {lvl("noexiste")}', '—', 'sin variable', 1)
       + f'<p>TKVA no tiene variables de criterio comercial: el resumen de la IA es lo único que dice por qué consultan. Ver Criterio comercial y Posible mejora 6.</p></div></div>'
       '<div class="qbe mt adv"><div class="qbj">' + I('eye') + 'Qué es aproximado</div><ul class="i3-b">'
       '<li>"Zona que TKVA comercializa" se deriva del barrio de Tokko (Núñez, Belgrano, Villa Crespo, Almagro, Barracas) y "tipología que existe" de lo que el lead pidió: para que sea exacto hace falta el catálogo de Tokko.</li>'
       '<li>Intención de compra se aproxima con derivación a visita o negociación: TKVA no tiene variable de plazo. Estado de obra compatible no se puede medir (no hay variable de objeción).</li>'
       f'<li>Lectura estricta: una sola tipología pedida y capacidad declarada (presupuesto real o forma de pago financiado, apto crédito o contado). Amplia: suma también "otro" en forma de pago y la intención aproximada.</li>'
       '<li>"Vuelve sobre la misma unidad" y el tiempo de derivación en minutos no se pueden medir con este export.</li></ul></div></div>')
cond = table(['Condición', 'Tipo', 'Cómo se mide en el export', f'Cumplen (de {B})', 'Nivel'], [
    ['Proyecto o zona que TKVA comercializa', 'Obligatorio', 'Proyecto de interés, o barrio de Tokko donde hay proyecto', f'{D["obl1"]} · {pct(D["obl1"], B)}', lvl(level_of(100 * D['obl1'] / B))],
    ['Tipología que existe', 'Obligatorio', 'Tipología buscada (1 a 4 ambientes)', f'{D["tip_any"]} · {pct(D["tip_any"], B)}', lvl(level_of(100 * D['tip_any'] / B))],
    ['Intención de compra', 'Suma', 'Derivación a visita o negociación (sin variable de plazo)', f'{D["s_int"]} · {pct(D["s_int"], B)}', lvl(level_of(100 * D['s_int'] / B))],
    ['Finalidad', 'Suma', 'Destino u objetivo (vivienda, inversión) o tag Inversor / Consumidor final', f'{D["s_fin"]} · {pct(D["s_fin"], B)}', lvl(level_of(100 * D['s_fin'] / B))],
    ['Presupuesto o forma de pago', 'Suma', 'Presupuesto (sin los 0) o forma de pago cargada', f'{D["s_cap"]} · {pct(D["s_cap"], B)}', lvl(level_of(100 * D['s_cap'] / B))],
    ['Estado de obra compatible', 'Suma', 'No hay variable de estado ni de objeción', '—', lvl('nomedible')]], 700, txt=True)
hotr = table(['Señal', 'Cómo se mide', 'Contactos', 'Nivel'], [
    ['Pide precio, disponibilidad o pago de una unidad concreta', 'Propiedades de Tokko o el resumen nombra una unidad', D['hot_sig']['unidad'], lvl('indicio')],
    ['Compra ya o en el corto plazo', 'Lo dice el resumen (no hay variable de plazo)', D['hot_sig']['ya'], lvl('noreport')],
    ['Tiene el dinero o el anticipo, o pregunta por contado', 'Forma de pago = contado o lo dice el texto', D['hot_sig']['contado'], lvl('indicio')],
    ['Vuelve sobre la misma unidad', 'El export no trae los mensajes', '—', lvl('nomedible')],
    ['Pedido de visita o reunión · no es señal de hot lead', 'Derivación a visita, tag de visita o lo dice el resumen', D['visita'], lvl('senal')]], 640, txt=True)
stages = ('<div class="g3">'
          + stage('var(--crit)', 'bolt', 'Hot leads sin próximo paso', 'Al menos una señal y sin seguimiento ni derivación', HOT_SIN, 'leads',
                  [('target', 'Preguntaron por una unidad concreta (todos)', D['hot_sig']['unidad']), ('cal', 'Hot leads de octubre', oct_['hot'])],
                  'Crear el tag <b>Hot Lead</b> con aviso a Vanesa (mejora 2). El pedido de visita va en su propio tag (mejora 1).')
          + stage('var(--warn)', 'alert', 'Sin procesar por la IA', 'Conversaron y no tienen resumen ni variables', D['sinproc'], 'conversaciones',
                  [('cal', 'Del 29/08 al 15/09', G['sinproc']), ('x', 'Sin ninguna respuesta en esos días', G['noresp'])],
                  'Confirmar qué pasó (<b>mejora 0</b>) y cargar saldo con un monto semanal medido.')
          + stage('var(--good)', 'checkc', 'El seguimiento funciona', 'Calificados con seguimiento, derivación o etapa del equipo', f'{CALSEG} de {CAL_A}', 'calificados',
                  [('repeat', 'Calificados sin próximo paso', CALSIN), ('users', 'Calificados en "No Concretado"', 9)],
                  'Sostenerlo. Los que faltan van con los hot leads; los "No Concretado" llevan motivo (mejora 4).')
          + '</div>')
fun = qci('filter', 'El embudo de consultas, paso a paso', 'pro', f'% sobre las {num(D["compra"])} consultas de compra del 22/07 al 14/10 · y cuánto pasa de un paso al siguiente',
          fsteps([('Entró · consulta de compra', num(D['compra']), 'contactos', '100%', 100, 'base', False),
                  ('Conversó con el agente', num(D['convo']), 'contactos', pct(D['convo'], D['compra']), 100 * D['convo'] / D['compra'], f'pasa {pct(D["convo"], D["compra"])}', False),
                  ('Procesada por la IA', num(B), 'contactos', pct(B, D['compra']), 100 * B / D['compra'], f'pasa {pct(B, D["convo"])}', True),
                  ('Dijo proyecto o zona', num(D['obl1']), 'contactos', pct(D['obl1'], D['compra']), 100 * D['obl1'] / D['compra'], f'pasa {pct(D["obl1"], B)}', False),
                  ('Calificada', str(CAL_A), f'contactos · {CAL_S} estricta', pct(CAL_A, D['compra']), 100 * CAL_A / D['compra'], f'pasa {pct(CAL_A, D["obl1"])}', True),
                  ('Con seguimiento o derivación', str(CALSEG), 'calificados', pct(CALSEG, D['compra']), 100 * CALSEG / D['compra'], f'pasa {pct(CALSEG, CAL_A)}', False),
                  ('Visita, negociación o cierre', str(D['humana']), 'con tag', pct(D['humana'], D['compra'], 1), 100 * D['humana'] / D['compra'], f'{D["tags"]["Convertido"][1]} "Convertido" de compradores', False)])
          + qbd('Los pasos en rojo son donde más se pierde: 1 de cada 3 conversaciones no se procesó, y de las que dicen proyecto solo 1 de cada 4 completa las sumas.',
                '<b>Conversó</b>: el lead mandó 2 o más mensajes. <b>Con seguimiento o derivación</b>: tags En Seguimiento, Derivado, Re-contactar, etapas del equipo o Tipo de derivación cargado. El paso 07 depende de que se marque el tag: se muestra, pero no se calcula una tasa.'))

# subsector mejora del CRM
coinc = D['tagcal_ok']; solo_crit = CAL_A - coinc; solo_tag = D['tagcal'] - coinc
circ = 2 * 3.14159 * 87
def seg(v, tot, off): l = circ * v / tot; return f'stroke-dasharray="{l:.1f} {circ - l:.1f}" stroke-dashoffset="{-off:.1f}"', off + l
tot3 = coinc + solo_crit + solo_tag
s1, o = seg(coinc, tot3, 0); s2, o = seg(solo_crit, tot3, o); s3, o = seg(solo_tag, tot3, o)
donut = (f'<div class="donut"><svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="87" fill="none" stroke="var(--inset)" stroke-width="26"/>'
         f'<circle cx="100" cy="100" r="87" fill="none" stroke="var(--vio)" stroke-width="26" {s1} transform="rotate(-90 100 100)"/>'
         f'<circle cx="100" cy="100" r="87" fill="none" stroke="var(--warn)" stroke-width="26" {s2} transform="rotate(-90 100 100)"/>'
         f'<circle cx="100" cy="100" r="87" fill="none" stroke="var(--ink4)" stroke-width="26" {s3} transform="rotate(-90 100 100)"/></svg>'
         f'<div class="ctr"><b>{pct(coinc, CAL_A)}</b><span>de los calificados tiene el tag</span></div></div>'
         f'<div class="dlg"><div><i style="background:var(--vio)"></i>Tag y criterio<b>{coinc}</b></div><div><i style="background:var(--warn)"></i>Califican sin el tag<b>{solo_crit}</b></div>'
         f'<div><i style="background:var(--ink4)"></i>Tag sin cumplir el criterio<b>{solo_tag}</b></div></div>')
def emb(name, sub, icon, w, cls):
    return (f'<div class="emb-r"><div class="emb-n">{name}<span>{I(icon)}{sub}</span></div><div class="emb-t"><i class="{cls}" style="width:{w:.1f}%"></i></div><div class="emb-v">{num(w)}%</div></div>')
proc_tag = 100 * 0.99
mej = (f'<div class="subsec mejora"><div class="ss-h"><div class="ss-ic">{I("wrench")}</div><div><div class="ss-k">Subsector · Cómo mejorar el CRM</div>'
       '<h2>El agente califica, <em>el tag cuenta otra cosa.</em></h2><p>Lectura constructiva del uso del CRM: qué funciona, dónde se corta el dato y qué cambio lo arregla. <b>Datos reales</b> del export de Prometheo al 14/10/2026.</p></div></div>'
       f'<div class="hallazgo"><div class="hz-top"><div style="min-width:0"><span class="hz-badge">{I("spark")}El hallazgo del período</span>'
       '<div class="hz-t">El seguimiento funciona: <em>lo que falla es la etiqueta.</em></div><div class="hz-s">'
       + BA(f'Vanesa y el agente siguen a <b>{CALSEG} de {CAL_A}</b> calificados. Pero el tag "Calificado" no sigue la regla: solo <b>{coinc}</b> contactos tienen el tag y cumplen el criterio. Sin el tag correcto, el seguimiento automático y la señal a la pauta aprenden de otra cosa.',
             f'Calificados con el criterio EDFAN: {RNG} (base: {B} conversaciones de compra procesadas). Con el tag "Calificado": {D["tagcal"]} compradores, de los que {solo_tag} no cumplen el criterio. El tag se usó sobre todo en julio ({TM["Calificado"]["2026-07"]} contactos de ese mes).')
       + '</div></div></div><div class="hz-body"><div>' + donut + '</div><div><div class="qbj">' + I('layers') + 'Uso de cada tramo · contactos con el tag sobre los que deberían tenerlo</div><div class="emb">'
       + emb('Recepción y conversación', f'Agente · automático · {D["recep_tag"][0]} de {D["recep_tag"][1]} procesadas con una etapa', 'bot', 100 * D['recep_tag'][0] / D['recep_tag'][1], 'c-auto')
       + emb('Calificación', f'Agente · automático · {coinc} de {CAL_A} calificados', 'bot', 100 * coinc / CAL_A, 'c-auto')
       + emb('Seguimiento y derivación', f'Agente y Vanesa · {CALSEG} de {CAL_A} calificados', 'hand', 100 * CALSEG / CAL_A, 'c-man')
       + emb('Visita agendada', f'Vanesa · manual · {D["visita_tag"]} de {D["visita"]} que la pidieron', 'hand', 100 * D['visita_tag'] / D['visita'], 'c-man')
       + '</div></div></div></div>')
calidad = (sec('Calidad del dato · malas prácticas encontradas y cómo se arreglan') + '<div class="fxg">'
           + fx('var(--warn)', 'var(--warn-bg)', 'tag', 'Etapa que no sigue la regla', 'Calificado sin criterio', f'{D["tagcal"]} con el tag; {CAL_A} cumplen el criterio (amplia); solo {coinc} coinciden.', 'Llevar el criterio al tag por lotes.', 'Venta · CRM › Posible mejora 3')
           + fx('var(--crit)', 'var(--crit-bg)', 'flame', 'Prioridad sin tag', 'Hot lead sin tag', f'{HOT} hot leads por criterio y ningún tag de hot lead; a quién se avisó no queda en el export.', 'Tag Hot Lead con aviso a Vanesa.', 'Venta · CRM › Posible mejora 2')
           + fx('var(--crit)', 'var(--crit-bg)', 'cal', 'Etapa sin registrar', 'Visitas sin fecha', f'{D["visita"]} pidieron visita o reunión; {D["visita_tag"]} tienen tag de visita y la fecha de visita está cargada en 1 contacto.', 'Tag "Pedido visita/reunión" y fecha al agendar.', 'Venta · CRM › Posible mejora 1')
           + fx('var(--crit)', 'var(--crit-bg)', 'lock', 'Cierre contaminado', '"Convertido" que no son ventas', f'{D["tags"]["Convertido"][0]} contactos con "Convertido": {D["conv_tipo"].get("Inmobiliaria",0)} inmobiliarias y {D["conv_tipo"].get("Ya cliente (postventa)",0)} clientes que ya habían comprado. Compradores nuevos: {D["conv_tipo"].get("Comprador",0)}.', 'Que "Convertido" sea solo venta nueva; postventa con su tag.', 'Venta · CRM › Posible mejora 4')
           + fx('var(--blu)', 'var(--blu-soft)', 'layers', 'Valor ambiguo', 'Derivación "inmobiliaria" en compradores', f'{D["deriv_inmo_comp"]} compradores tienen Tipo de derivación = inmobiliaria: se usa para "lo atiende Vanesa como inmobiliaria", no para "es una inmobiliaria".', 'Definir el valor antes de filtrar por él.', 'Venta · CRM › Posible mejora 4')
           + fx('var(--warn)', 'var(--warn-bg)', 'dollar', 'Relleno con 0', 'Presupuesto en 0', f'{D["pres_cero"]} presupuestos guardados en 0 y solo {D["cov"]["Presupuesto (sin ceros)"][0]} con monto real.', '"Si no lo dice, dejala vacía" en el prompt de la variable.', 'Venta · CRM › Posible mejora 5')
           + fx('var(--blu)', 'var(--blu-soft)', 'users', 'Tags que compiten', 'Inversor y Consumidor final a la vez', '12 contactos con los dos tags · 11 con dos etapas del mismo embudo.', 'Corregir a mano según finalidad.', 'Prometheo › contactos, a mano')
           + fx('var(--vio)', 'var(--vio-soft)', 'user', 'Variable sin uso', 'Asesor asignado vacío', 'Asesor asignado 0% e Historial 0%: en TKVA, Vanesa atiende todos los leads. Igual se evalúan en cada conversación.', 'Pasarlas a carga manual: baja el gasto de extracción.', 'Consumo variable CRM › Tokens IA')
           + '</div>')
PM_LIST = [
    pm('pm0', '0', 'Posible Mejora · Medir · AUREA', 'Qué pasó entre el 29/08 y el 15/09', 'Pedido de solo lectura para confirmar si el agente estuvo sin saldo o pausado, y cuántos contactos quedaron sin procesar.',
       ['Consulta · sin cambios', 'Tokens: Bajo'], 75, ('3', 'preguntas'),
       'Necesito un diagnóstico de solo lectura de la cuenta de TKVA. No cambies nada.\n1) Decime si entre el 29/08/2026 y el 15/09/2026 el asistente estuvo desactivado o la cuenta se quedó sin saldo, con las fechas exactas.\n2) Listame las recargas de saldo de agosto, septiembre y octubre, con fecha y monto.\n3) Decime cuántos contactos que entraron en esas fechas no tienen Resumen por IA.\nDevolvelo como tres listas cortas.', 'var(--good)', 'start'),
    pm('pm1', '1', 'Posible Mejora · Corregir · AUREA', 'Tag "Pedido visita/reunión"', f'{D["visita"]} pidieron visita o reunión y solo {D["visita_tag"]} tienen un tag de visita. Un tag propio, que avise a Vanesa.',
       ['Tag nuevo', 'Tokens: Medio'], 72, (str(D['visita']), 'contactos'),
       'Quiero crear un Smart Tag nuevo en el asistente de TKVA llamado "Pedido visita/reunión".\nPrompt de asignación: asignalo solo cuando el lead pide explícitamente visitar la obra, ver una unidad o tener una reunión con Vanesa. No lo asignes si el asistente ofreció la visita y el lead no la aceptó.\nAcción: notificar a Vanesa.\nAntes de crear nada, mostrame el texto final del tag y decime cuántos contactos de los últimos 30 días lo tendrían (espero entre 30 y 60). No apliques el cambio hasta que yo te confirme con "Sí, confirmar".', 'var(--vio)', 'start'),
    pm('pm2', '2', 'Posible Mejora · Activar · AUREA', 'Tag "Hot Lead" con aviso a Vanesa', 'Prioridad, no etapa: convive con la etapa del embudo y avisa en el momento.',
       ['Tag nuevo', 'Tokens: Medio'], 66, (str(HOT), 'hot leads'),
       'Quiero crear un Smart Tag nuevo en el asistente de TKVA llamado "Hot Lead". Es un tag de prioridad: no reemplaza la etapa del embudo.\nPrompt de asignación: asignalo cuando el lead muestra al menos una de estas señales: pide precio, disponibilidad o forma de pago de una unidad concreta; dice que compra ya o en los próximos 90 días; dice que tiene el dinero o el anticipo, o pregunta por pago de contado.\nAcción: notificar a Vanesa en el momento.\nAntes de crearlo, mostrame el texto final y decime cuántos contactos de los últimos 30 días lo tendrían. No apliques el cambio hasta que yo te confirme con "Sí, confirmar".', 'var(--vio)', 'start'),
    pm('pm3', '3', 'Posible Mejora · Corregir · AUREA', 'Calificado por regla, por lotes', 'Que el tag "Calificado" siga la regla: dos obligatorios y al menos dos sumas. Primero un lote chico auditado.',
       ['Recalificar base', 'Tokens: Medio'], 77, (str(CAL_A), 'por criterio'),
       'Quiero recalificar contactos de TKVA con el tag "Calificado". Regla: tiene proyecto de interés (o barrio con proyecto de TKVA) y tipología buscada, y además al menos dos de estas: finalidad (vivienda o inversión), forma de pago o presupuesto mayor a 0, derivación a visita o negociación.\nPaso 1: filtrá los contactos que cumplen la regla y no tienen el tag "Calificado". Decime cuántos son (espero alrededor de 100; si da menos de 70 o más de 130, frená) y mostrame 5 ejemplos.\nPaso 2: listame los que tienen el tag y no cumplen la regla, sin cambiar nada.\nNo apliques ningún cambio hasta que yo te confirme cada lote.', 'var(--vio)', 'start'),
    pm('pm4', '4', 'Posible Mejora · Corregir · AUREA', '"Convertido" solo para ventas nuevas', 'Inmobiliarias y postventa fuera del cierre, y "No Concretado" con motivo.',
       ['Limpieza de tags', 'Tokens: Bajo'], 70, (str(D['tags']['Convertido'][0]), 'con el tag'),
       'En la cuenta de TKVA, listame los contactos con el tag "Convertido" que además tienen el tag "Inmobiliaria", "Inmobiliaria Activa" o "Cliente ya compró". Espero alrededor de 9. Mostrámelos con nombre y tags.\nDespués, listame los contactos con "No Concretado" que no tienen motivo en el resumen.\nNo cambies nada: solo listá. Yo te confirmo qué corregir.', 'var(--vio)', 'start'),
    pm('pm5', '5', 'Posible Mejora · Corregir · AUREA', 'Presupuesto vacío, nunca en 0', f'{D["pres_cero"]} presupuestos en 0 parecen dato y rompen promedios.',
       ['Prompt de variable', 'Tokens: Bajo'], 80, (str(D['pres_cero']), 'en 0'),
       'Quiero ajustar el prompt de la variable "var_presupuesto" del asistente de TKVA. Agregá al final: "Si el lead no dice un monto, dejala vacía. Nunca guardes 0."\nMostrame el prompt completo antes y después del cambio. No apliques nada hasta que yo te confirme con "Sí, confirmar".', 'var(--vio)', 'start'),
    pm('pm6', '6', 'Posible Mejora · Medir · AUREA', 'Variables de criterio comercial', 'Objeción principal y evento disparador: hoy no existen y el tablero no sabe qué frena ni por qué consultan ahora.',
       ['Variables nuevas', 'Tokens: Medio'], 28, ('2', 'variables'),
       'Quiero crear dos variables nuevas en el asistente de TKVA, de tipo Opciones.\n1) "Objeción Principal": precio, entrega o plazo, financiación o crédito, ubicación, tamaño, cochera, otro. Prompt: "Cargala solo si el lead dice qué le frena; si no lo dice, dejala vacía."\n2) "Evento Disparador": vende otra propiedad, necesita mudarse, vivienda para un familiar, inversión o renta, termina un alquiler, otro. Prompt: "Cargala solo si el lead cuenta qué pasó para que consulte hoy; si no, vacía."\nMostrame la configuración completa antes de crearlas. No apliques nada hasta que yo confirme.', 'var(--vio)', 'start'),
]
mejoras = ('<div id="mejoras"></div>' + sec('Posibles mejoras · listas para Mi Prometheo') + mclegend()
           + qbd('Cada prompt está auditado contra el export: pide el conteo antes de aplicar y va en una conversación por pedido. Mi Prometheo también consume saldo.') + ''.join(PM_LIST))
A_VIS = act('corregir', 'Ventas', [20, 10, 15, 10, 5, 12], f'Visitas · {D["visita"]} pidieron visita y {D["visita_tag"]} tienen el tag',
            'Pedidos de visita o reunión que llegan a un tag', f'{num(D["compra"])} consultas de compra', f'{D["visita"]} pedidos · {D["visita_tag"]} con tag · fecha de visita en 1 contacto', CIT,
            'Que cada visita agendada lleve el tag y la fecha el mismo día, y que la visita realizada se marque cuando pasa.',
            'Bandeja de Vanesa · tags del embudo Venta y Cierre · variable de fecha de visita', 'Tasa de visita por proyecto y por anuncio desde noviembre.',
            'Visitas con tag sobre pedidos de visita, al 30/11.', 'que el tag se marque cuando pasa, no a fin de mes.',
            'El conteo de tags es completo; el pedido de visita sale del resumen y de la derivación. No se probó antes en la cuenta.', 'Hecho', adv=True)
venta = ('<section class="panel p-ventacrm">' + head('Venta · CRM · el estado de cada consulta', 'Quién califica, a quién atender primero', 'y qué mejorar en el CRM.',
                                                   'TKVA vende proyectos en pozo, en obra y terminados. El agente responde, informa proyecto, entrega y financiación, y califica; Vanesa coordina la visita, negocia y cierra.',
                                                   'Acá se ve quién califica con el criterio de referencia, a quién atender primero y qué pedirle a Mi Prometheo para ordenar el CRM.')
         + cqb + '<div class="adv">' + sec('Cómo se mide cada condición en el export') + cond + '<div class="mt">' + hotr + '</div></div>'
         + f'<div class="iobar"><a class="iobtn primary" href="#mejoras" onclick="document.getElementById(\'mejoras\').scrollIntoView({{behavior:\'smooth\'}});return false;">{I("flame")}Ver las 7 posibles mejoras</a><span class="iohint">Potenciado por Mi Prometheo</span></div>'
         + stages + sec('El embudo de consultas') + fun + mej + calidad + mejoras
         + sec('Qué hago ahora · acciones con dueño y score') + legend() + mclegend()
         + acts([A_HOT, A_CALTAG, A_CAP, A_VIS], 4)
         + yeq(f'El seguimiento ya funciona ({CALSEG} de {CAL_A} calificados con próximo paso). Lo que falta es que los tags digan lo mismo que la conversación: Hot Lead, Calificado por regla y visitas con fecha. Las mejoras 0 a 3 primero.')
         + '</section>')
PANELS.append(venta)

# ================= 4 · VANESA Y EL AGENTE =================
VC = [('agente', 875, 2310, 686, 19, 363, 82, 14, 68), ('equipo', 278, 2831, 265, 99, 265, 65, 134, 278)]
a_, e_ = VC
vend = ('<section class="panel p-vendedores">' + head('Vanesa y el agente · quién atiende qué', 'En TKVA atiende Vanesa.', 'El agente califica y le pasa la conversación.',
                                                    'Cuántas conversaciones toma Vanesa, qué pasa con ellas y qué falta registrar. No hay asesores por finalidad: el campo de asesor queda vacío a propósito.',
                                                    'Fuente: tags del embudo humano (Derivado, visitas, negociación, cierre) y Tipo de derivación. Base: las consultas de compra del 22/07 al 14/10.')
        + '<div class="g4">'
        + kpi('chat', 'blu', 'pro', 'Consultas de compra', num(D['compra']), None, '', None, 'del 22/07 al 14/10')
        + kpi('users', 'pnk', 'pro', 'Tomadas por Vanesa', str(e_[1]), pct(e_[1], D['compra']), 'd-flat', None, 'Derivado, etapa del equipo o tipo de derivación cargado')
        + kpi('user', '', 'pro', 'Asesor asignado', '0%', 'a propósito', 'd-flat', None, 'Vanesa atiende personalmente todos los leads.', 'La variable se evalúa igual en cada conversación: conviene pasarla a manual (ahorra extracción).')
        + kpi('repeat', 'amb', 'pro', 'Derivados', str(D['tags']['Derivado'][0]), f'{D["tags"]["Derivado"][0] - D["tags"]["Derivado"][1]} no compradores', 'd-flat', None, f'{D["tags"]["Derivado"][1]} compradores · el resto inmobiliarias, postventa y proveedores')
        + '</div>' + sec('Agente y Vanesa · qué pasa con cada conversación') + '<div class="g2">'
        + vcd('var(--blu)', 'bot', 'Solo el agente', f'{a_[1]} consultas · {num(a_[2])} mensajes de TKVA',
              [('Conversaron', 100 * a_[3] / a_[1], a_[3]), ('Calificados', 100 * a_[4] / a_[5], a_[4]), ('Hot leads', 100 * a_[6] / a_[1], a_[6]), ('Pidieron visita', 100 * a_[7] / a_[1], a_[7]), ('Con próximo paso', 100 * a_[8] / a_[1], a_[8])],
              [('warn', pct(a_[4], a_[5]), 'califica'), ('warn', pct(a_[8], a_[1]), 'con próximo paso'), ('', num(a_[2] / a_[1], 1), 'mensajes por consulta')])
        + vcd('var(--vio)', 'users', 'Vanesa tomó la conversación', f'{e_[1]} consultas · {num(e_[2])} mensajes de TKVA',
              [('Conversaron', 100 * e_[3] / e_[1], e_[3]), ('Calificados', 100 * e_[4] / e_[5], e_[4]), ('Hot leads', 100 * e_[6] / e_[1], e_[6]), ('Pidieron visita', 100 * e_[7] / e_[1], e_[7])],
              [('good', pct(e_[4], e_[5]), 'califica'), ('good', pct(e_[7], e_[1]), 'pidieron visita'), ('', num(e_[2] / e_[1], 1), 'mensajes por consulta')])
        + '</div>' + qbd('Vanesa toma las conversaciones más avanzadas: de ahí sale casi todo lo calificado y todas las visitas.',
                         'Calificación sobre conversaciones procesadas (criterio EDFAN, amplia). La lectura amplia cuenta la derivación a visita o negociación como intención de compra, así que favorece a las conversaciones que tomó Vanesa: la diferencia no prueba que el agente califique peor, muestra quién cierra.')
        + sec('Embudo humano · lo que marca Vanesa') + '<div class="g2">'
        + card('hand', 'Etapas del equipo', 'pro', 'compradores con el tag',
               bars([(t, D['tags'][t][1]) for t in ['Derivado', 'En Seguimiento', 'Visita Agendada', 'Visita Realizada', 'En Negociación', 'Convertido', 'No Concretado']], None, 'var(--vio)', subfmt=lambda n: ''))
        + card('route', 'Por qué se derivó', 'pro', f'Tipo de derivación · base declarada: {sum(D["deriv"].values())}',
               bars([('Visita', D['deriv'].get('visita', 0)), ('Inmobiliaria (valor ambiguo)', D['deriv'].get('inmobiliaria', 0)), ('Negociación', D['deriv'].get('negociacion', 0)),
                     ('Jurídico o fiscal', D['deriv'].get('juridico_fiscal', 0)), ('Postventa', D['deriv'].get('postventa', 0))], sum(D['deriv'].values()), 'var(--blu)')
               + note(f'"Inmobiliaria" aparece en {D["deriv_inmo_comp"]} compradores: el valor se usa para algo distinto de "es una inmobiliaria". Ver Posible mejora 4.'))
        + '</div>' + sec('Qué hago ahora · acciones con dueño y score') + legend()
        + acts([A_VIS.replace('class="i3 av adv"', 'class="i3 av"', 1),
                act('corregir', 'AUREA', [14, 15, 15, 10, 5, 12], f'Tipo de derivación · "inmobiliaria" en {D["deriv_inmo_comp"]} compradores', 'Derivaciones con un valor que significa dos cosas', f'{sum(D["deriv"].values())} derivaciones de compradores', f'{D["deriv_inmo_comp"]} compradores con valor "inmobiliaria"', CIT,
                    'Definir qué significa "inmobiliaria" en Tipo de derivación (¿lo atiende Vanesa como canal B2B?) y separar ese caso de "es una inmobiliaria", que va por la línea B2B.',
                    'Prometheo › Variables › Tipo de derivación', 'Que el filtro por derivación no mezcle compradores con inmobiliarias.', 'Compradores con derivación "inmobiliaria", al 30/11.', 'ningún comprador fuera del embudo por error.',
                    'El campo está en el 38% de las conversaciones procesadas y el cruce con el tipo de contacto es completo.', 'Hecho', mcard='start'),
                act('medir', 'Ventas', [8, 10, 15, 5, 5, 8], f'Cierre · {D["tags"]["Convertido"][1]} ventas de compradores con tag en tres meses', 'Ventas nuevas registradas', 'compradores con etapa del equipo', f'{D["tags"]["Convertido"][1]} "Convertido" de compradores · {D["tags"]["No Concretado"][1]} "No Concretado"', CIT,
                    'Que Vanesa marque "Convertido" solo con venta nueva y "No Concretado" con motivo, el mismo día.', 'Bandeja de Vanesa · tags Venta y Cierre', 'Tasa de cierre por proyecto y por anuncio.', 'Ventas nuevas con tag, al 30/11.', 'que el tag se marque cuando pasa.',
                    'El conteo es completo, pero con tan pocas marcas no hay profundidad para leer el cierre.', 'Hecho')], 3)
        + yeq('El agente califica y Vanesa cierra: eso funciona. Lo que no se ve es el final: visitas sin fecha y "Convertido" mezclado con postventa e inmobiliarias. Con esos dos tags bien marcados, este tablero mide visitas y ventas por proyecto.')
        + '</section>')
PANELS.append(vend)

# ================= 5 · PROYECTOS =================
def pjt(PJ, PN):
    mxn = max(p['n'] for p in PJ)
    head_ = ('<div class="pjt"><div class="pjt-r pjt-hd"><span>Proyecto</span><span>Consultas</span><span>Califican</span>'
             '<span>Inversión · vivienda</span><span>Piden financiación</span><span>Tipología más pedida</span><span>No Fit</span><span>Hot leads</span></div>')
    rows = ''
    for i, p in enumerate(PJ):
        cr = 100 * p['cal'] / max(p['conv'], 1); iv = p['inv'] + p['viv']
        split = (f'<span class="pjt-split"><i style="width:{100*p["inv"]/iv:.0f}%"></i></span>' if iv else '<span class="pjt-split"></span>')
        tips = ''.join(f'<span class="pjt-tip">{x.strip()}</span>' for x in p['tip'].split(',') if x.strip())
        rows += (f'<div class="pjt-r"><div class="pjt-p"><span class="pjt-n">{i+1:02d}</span><b>{p["p"]}</b></div>'
                 f'<div class="pjt-m"><b>{p["n"]}</b><span>{pct(p["n"], PN)} del total</span>{mbar(100 * p["n"] / mxn)}</div>'
                 f'<div class="pjt-m"><b>{pct(p["cal"], p["conv"])}</b><span>{p["cal"]} de {p["conv"]}</span>{mbar(cr * 100 / 40, "ok")}</div>'
                 f'<div class="pjt-m"><b>{p["inv"]} · {p["viv"]}</b><span>inversión · vivienda</span>{split}</div>'
                 f'<div class="pjt-m"><b>{p["fin_req"]}</b><span>{pct(p["fin_req"], p["n"])} de sus consultas</span></div>'
                 f'<div class="pjt-tips">{tips}</div><div class="pjt-m mut"><b>{p["nofit"]}</b></div><div class="pjt-m hot"><b>{p["hot"]}</b></div></div>')
    return head_ + rows + '</div>'

PJ = D['proj']; PN = D['proy_n']
top3 = PJ[:3]
dist_ = ('<section class="panel p-distrib">' + head('Proyectos · qué se pide de cada uno', 'Maker Núñez, Liberti y Maker Crespo', 'concentran la demanda.',
                                                   'Cuántas consultas trae cada proyecto, cuántas califican y qué frena a cada uno.',
                                                   f'Proyecto de interés lo carga el agente ({num(D["cov"]["Proyecto"][1],0)}% de las conversaciones procesadas, Señal). Un lead puede consultar por más de un proyecto: los totales no suman 100%. Base: consultas de compra procesadas del 22/07 al 14/10.')
         + '<div class="g4">' + ''.join(kpi('building', t, 'pro', p['p'], str(p['n']), pct(p['n'], PN), 'd-flat', None, f'consultas · {p["cal"]} calificadas', None, f'% sobre las {PN} consultas que dicen proyecto.') for p, t in zip(top3, ['blu', 'pnk', '']))
         + kpi('layers', 'amb', 'pro', 'Resto de proyectos', str(sum(p['n'] for p in PJ[3:])), '3 proyectos', 'd-flat', None, 'Green Line, Maker Belgrano y Drago Select') + '</div>'
         + pjt(PJ, PN)
         + qbd('Green Line es el que mejor califica y el único donde inversión supera a vivienda. Liberti trae volumen, pero 1 de cada 3 termina en No Fit: el precio de 2 ambientes desde USD 140.000 frena a quien busca apto crédito.',
               'Inversión / Vivienda: destino, objetivo o tag (Indicio, 35% de las conversaciones procesadas). Tipología más pedida: solo leads que pidieron una sola tipología, para no contar lo que ofreció el agente. No Fit por proyecto: tag No Fit con ese proyecto cargado.')
         + sec('Tokko · lo que llega del catálogo al CRM') + '<div class="g4">'
         + kpi('pin', 'grn', 'tokko', 'Barrios interesados (Tokko)', f'{num(D["cov"]["Barrios (Tokko)"][1],0)}%', None, '', None, 'de las conversaciones procesadas', None, 'Campo que completa la integración con Tokko.')
         + kpi('building', '', 'tokko', 'Propiedades interesadas (Tokko)', f'{num(D["cov"]["Propiedades (Tokko)"][1],0)}%', None, '', None, 'tienen una propiedad de Tokko asociada', None, 'Subió de 5 contactos en julio a 64 en octubre.')
         + kpi('doc', '', 'tokko', 'Links de propiedades', f'{num(D["cov"]["Links (Tokko)"][1],0)}%', None, '', None, 'recibieron una ficha de Tokko')
         + kpi('lock', 'amb', 'calc', 'Stock, precio y disponibilidad', 'Sin dato', None, '', None, 'El export de contactos no trae el catálogo de Tokko: no se puede cruzar demanda contra unidades disponibles.', None, 'Faltante de integración: pedir el export del catálogo o la vista de unidades de Tokko.')
         + '</div>' + qbd('Con el catálogo de Tokko se podría ver, por proyecto, qué tipología se pide más de lo que queda en stock. Hoy el tablero ve la demanda, no la oferta.')
         + yeq('Maker Núñez trae la mayor demanda y los hot leads; Green Line es el que mejor califica. Liberti necesita otra respuesta al precio: ofrecer la unidad más chica o el plan de pagos antes de que la conversación termine en No Fit.')
         + '</section>')
PANELS.append(dist_)

# ================= 6 · INMOBILIARIAS Y PROVEEDORES =================
INM, PRV, EV = D['inmo'], D['prov'], D['env']
b2b_msgs = EV['inmo'] + EV['prov']
okband = (f'<div class="okband"><div class="okic">{I("checkc")}</div><div><span class="okk">Mejora continua · hecha</span>'
          '<b class="okt">Dos líneas de WhatsApp: B2C con agente, B2B sin agente.</b>'
          f'<p>El insight: el agente gastaba saldo conversando con inmobiliarias y proveedores. A pedido de TKVA se abrió una línea aparte para empresas B2B, '
          f'atendida sin agente, y la línea de ventas quedó para compradores. En el período, el agente les mandó <b>{num(b2b_msgs)} mensajes</b> a inmobiliarias y proveedores '
          f'({pct(b2b_msgs, EV["total"])} de todo lo que envió TKVA).</p><div class="okf">{mc("start")}<span class="qq" style="--c:var(--good)">Regla del rubro real estate</span>'
          '<span class="qq" style="--c:var(--good)">El efecto se mide el próximo período</span></div></div></div>')
corr = ('<section class="panel p-corredores">' + head('Inmobiliarias y proveedores · lo que no es comprador final', 'Las inmobiliarias ya tienen', 'su propia línea.',
                                                    'Inmobiliarias y proveedores escribían por la misma línea que los compradores. Eso ya se separó: acá se ve cuánto pesaban y qué medir ahora.',
                                                    'Inmobiliaria = tags Inmobiliaria, Inmobiliaria Activa o Inmobiliaria a Contactar. Proveedor = tag Proveedor. Se separan de la base de compra en todo el tablero.')
        + okband + '<div class="g4">'
        + kpi('users', 'blu', 'pro', 'Inmobiliarias que escribieron', str(INM['n']), None, '', None, f'{INM["jul22"]} el día del arranque (22/07)', None, 'Contactos que ya trabajaban con Vanesa.')
        + kpi('checkc', 'grn', 'pro', 'Inmobiliaria Activa', str(INM['activa']), None, '', None, 'relación activa, derivan clientes')
        + kpi('phone', '', 'pro', 'Inmobiliaria a Contactar', str(INM['contactar']), None, '', None, 'esperan el primer contacto de Vanesa')
        + kpi('truck', 'amb', 'pro', 'Proveedores', str(PRV['n']), f'{PRV["conv"]} conversaron', 'd-flat', None, 'tag Proveedor')
        + '</div><div class="g2">'
        + card('chat', 'A quién le escribió el agente', 'pro', f'{num(EV["total"])} mensajes enviados por TKVA · 22/07 al 14/10',
               bars([('Compradores que conversan', EV['conv']), ('Inmobiliarias', EV['inmo']), ('Equipo interno', EV['eq']), ('No Fit', EV['nofit']), ('Proveedores', EV['prov']), ('Postventa', EV['post']), ('Compradores de un solo mensaje', EV['unavez'])], EV['total'], 'var(--vio)')
               + note(f'Inmobiliarias y proveedores recibieron {num(b2b_msgs)} mensajes ({pct(b2b_msgs, EV["total"])}). Es el dato que justificó la línea aparte.'))
        + card('building', 'Por qué proyecto preguntan las inmobiliarias', 'pro', 'Indicio · n chico',
               bars(sorted(INM['proy'].items(), key=lambda x: -x[1]), INM['n'], 'var(--blu)')
               + note('Maker Núñez y Green Line son los que más mueve el canal B2B.'))
        + '</div>' + qci('trend', 'Inmobiliarias y proveedores por mes', 'pro', 'contactos nuevos con tag B2B · % sobre los contactos del mes',
                         bars([(mlab[m], v[0]) for m, v in D['nodem_m'].items()], None, 'var(--blu)', subfmt=None) + note(' · '.join(f'{mlab[m].split(" ")[0]}: {pct(v[0], v[1])} de los contactos' for m, v in D['nodem_m'].items())))
        + table(['Pieza del modelo', 'Valores o comportamiento', 'Estado en TKVA'], [
            ['Línea de WhatsApp B2B', 'Número aparte para inmobiliarias y proveedores, atendido sin agente', f'<span class="qbx l-hecho">{I("checkc")}Hecho</span> mejora continua aplicada'],
            ['Embudo Inmobiliaria', 'Inmobiliaria a Contactar → Inmobiliaria Activa', f'En uso: {INM["contactar"]} y {INM["activa"]} contactos'],
            ['Proveedor (tag, sin embudo)', 'Al asignarse: apagar el asistente', f'{PRV["conv"]} de {PRV["n"]} proveedores conversaron con el agente'],
            ['Tipo de contacto excluyente', 'Comprador · Inmobiliaria · Proveedor', 'Hoy lo dicen los tags; Tipo de derivación mezcla "inmobiliaria" con compradores']], 700, txt=True)
        + yeq(f'La separación ya está hecha. Lo que queda es medirla: que la no-demanda baje en la línea de ventas el próximo período y que ningún comprador termine en la línea B2B por error.')
        + '</section>')
PANELS.append(corr)
