# Pestañas 7 a 14 · TKVA (incluye Reporte comercial en el formato de Vanesa)
R = json.load(open('R.json'))
ARS_S, ARS_M = 37.6798, 89.5620

# ================= REPORTE COMERCIAL (formato del reporte semanal y mensual de Vanesa) =================
RW = R['weeks']
wk_ids = ['w1', 'w2', 'w3', 'w4']
rw_tabs = '<div class="subtabs rwtabs">' + ''.join(f'<label for="rw-{i}">{I("cal")}{w["lab"]}</label>' for i, w in zip(wk_ids, RW)) + '</div>'
def wk_block(i, w, prev):
    d = f'{num(100 * (w["n"] - prev["n"]) / prev["n"])}%' if prev else None
    tot = w['fun'][0][1] or w['n']
    fun_html = ''.join(bar(t, num(v), pct(v, w['n']), 100 * v / max(1, max(x for _, x in w['fun'])), c)
                       for (t, v), c in zip(w['fun'], ['var(--blu)', 'var(--vio)', 'var(--crit)', 'var(--warn)', 'var(--ink4)', 'var(--good)']))
    est_html = bars(w['est'], w['n'], 'var(--vio)')
    ori = sorted(w['ori'].items(), key=lambda x: -x[1])
    ori_html = ''.join(bar(k, num(v), pct(v, w['n']), 100 * v / max(x for _, x in ori), 'var(--blu)', miss=(k == 'Sin dato')) for k, v in ori)
    def lst(rows, title, icon, empty_txt):
        if not rows:
            return card(icon, title, 'pro', '0 en el CRM', empty(icon, 'Sin registro en Prometheo esta semana', empty_txt))
        return (f'<div class="qbe"><div class="qbj">{I(icon)}{title}{src("pro")}<span class="r">{len(rows)} en el CRM</span></div>'
                + table(['Emprendimiento', 'Nombre', 'Origen', 'Búsqueda', 'Último punto del resumen de la IA'], rows, 760, txt=True) + '</div>')
    return (f'<div class="stab st-{i}"><div class="g4">'
            + kpi('chat', 'blu', 'pro', 'Total contactos', str(w['n']), (('+' if w['n'] >= prev['n'] else '') + d) if prev else None, 'd-flat', None, f'contactos nuevos del {w["lab"]}', f'{w["compra"]} son consultas de compra (sin inmobiliarias, proveedores ni No Fit).')
            + kpi('checkc', 'grn', 'calc', 'Calificados · criterio EDFAN', str(w['calif']), None, '', None, 'lectura amplia, sobre lo que procesó la IA')
            + kpi('bolt', 'pnk', 'calc', 'Hot leads', str(w['hot']), None, '', None, 'una señal de compra alcanza')
            + kpi('cal', 'amb', 'pro', 'Visitas en el CRM', str(len(w['vis'])), None, '', None, 'contactos con tag de visita actualizados en la semana')
            + '</div><div class="g2">'
            + card('filter', 'Embudo de conversión', 'pro', f'{w["n"]} leads · tags del embudo de Recepción', fun_html + note('Mismo embudo que muestra el panel de Prometheo: etapas del agente, por contacto que entró en la semana.'))
            + card('layers', 'Estado de los contactos', 'pro', 'los cuatro estados del reporte semanal', est_html
                   + note('Esperando respuesta = En Seguimiento o Fantasma · Cerrado = No Fit o No Concretado · Recontactar = tag "Re-contactar más adelante" · Visitas = Visita Agendada o Realizada. Por contacto que entró en la semana; la tarjeta "Visitas en el CRM" cuenta los contactos con visita actualizados en la semana.'))
            + '</div>' + card('pin', 'Origen de los contactos', 'pro', f'Canal Origen · {w["n"]} contactos', ori_html
                              + note('Facebook no se distingue: el CRM no guarda la plataforma del anuncio. Ver "Lo que hay que sumar al CRM".'))
            + '<div class="mt">' + lst(w['vis'], 'Seguimiento · visitas', 'cal', 'Las visitas que coordina Vanesa no llegan al tag. Se arregla con la Posible mejora 1.') + '</div>'
            + '<div class="mt">' + lst(w['rec'], 'Seguimiento · recontactar', 'repeat', 'Nadie quedó con el tag "Re-contactar más adelante" esta semana.') + '</div></div>')
weeks_html = ''.join(wk_block(i, w, RW[k - 1] if k else None) for k, (i, w) in enumerate(zip(wk_ids, RW)))

RM = R['months']
mlab2 = {'2026-07': 'Julio (22–31)', '2026-08': 'Agosto', '2026-09': 'Septiembre', '2026-10': 'Octubre (al 14)'}
PEND = '<span class="qcw">falta inversión</span>'
def ratio(a, b): return f'{num(a / b, 1)} : 1' if (a and b) else '<span class="qcw">sin dato</span>'
mon_rows = [
    ['Contactos · Instagram (declarado)'] + [num(m['ori'].get('Instagram', 0)) for m in RM],
    ['Contactos · Instagram (mensaje directo)'] + [num(m['ig_dm']) if m['ig_dm'] else '<span class="qcw">0 · canal sin datos</span>' for m in RM],
    ['Contactos · Facebook'] + ['<span class="qcw">no se distingue</span>' for m in RM],
    ['Contactos · WhatsApp directo'] + [num(m['ori'].get('WhatsApp', 0)) for m in RM],
    ['Contactos · LT (formulario)'] + [num(m['ori'].get('LT (formulario)', 0)) for m in RM],
    ['Contactos · con anuncio de Meta'] + [num(m['ad']) for m in RM],
    ['Total contactos'] + [f'<b>{num(m["n"])}</b>' for m in RM],
    ['Entrevistas (visita realizada)'] + [num(m['entrev']) for m in RM],
    ['Ventas (tag "Convertido", compradores)'] + [num(m['ventas']) for m in RM],
    ['Inversión total · CM'] + ['<span class="qcw">sin fuente</span>' for m in RM],
    ['CPC · CPE · CPV'] + [PEND for m in RM],
    ['Ratio contactos / entrevista'] + [ratio(m['n'], m['entrev']) for m in RM],
    ['Ratio entrevista / venta'] + [ratio(m['entrev'], m['ventas']) for m in RM],
    ['Ratio contactos / venta'] + [ratio(m['n'], m['ventas']) for m in RM]]
monthly = table(['Indicador del reporte mensual'] + [mlab2[m['m']] for m in RM], mon_rows, 760)

CRMRD = table(['Lo que mide Vanesa', 'Qué falta hoy en el CRM', 'Cambio en Prometheo', 'Quién'], [
    ['Contactos por origen (Facebook / Instagram)', 'El ID de anuncio no dice la plataforma; Canal Origen no tiene "Facebook"; el canal de Instagram no registra conversaciones desde el 30/07.', 'Sumar "Facebook" a Canal Origen y leer la plataforma del export de Meta por ID de anuncio. Reconectar Instagram.', mc('start')],
    ['Contactos de LT', 'Los formularios no entran solos: el reporte del 01/10 al 07/10 cuenta 54 de LT y Prometheo registra 25.', 'Integración Go High Level → Prometheo o Meta Forms (vía A).', mc('pro')],
    ['Entrevistas totales · CPE', f'La visita se coordina pero no se marca: {D["visita"]} pedidos, {D["visita_tag"]} con tag, fecha de visita en 1 contacto.', 'Etapa "Entrevista realizada" (hoy Visita Realizada) con fecha obligatoria al marcarla.', mc('start')],
    ['Ventas totales · CPV', f'"Convertido" mezcla ventas con inmobiliarias y postventa (11 tags, 2 ventas nuevas). La reserva del 9G de Maker Núñez no figura como venta.', 'Tag "Reservado / Vendido" solo para ventas nuevas, con variable "Unidad" (ej. 9G) y monto. Postventa con su propio tag.', mc('start')],
    ['Estados de la semana', '"Cerrado" no distingue venta de descarte; "Esperando respuesta" no es una etapa.', 'Usar los tags que ya existen: En Seguimiento / Fantasma, No Fit / No Concretado con motivo, Re-contactar más adelante, Visita.', mc('start')],
    ['Comentarios por contacto', 'El campo Comentarios está en 1 contacto.', 'Variable corta "Próximo paso" que carga Vanesa (o el agente) al cerrar cada contacto.', mc('start')],
    ['Inversión, CPC, CPE, CPV', 'Sin gasto de Meta conectado.', 'Export de Meta por ID de anuncio y mes, o carga mensual de la inversión por origen. Conexión nativa con Meta Ads: desarrollo.', mc('pro')]], 720, txt=True)

rep = ('<section class="panel p-reporte">' + head('Reporte comercial · semanal y mensual', 'El reporte que Vanesa arma a mano,', 'armado desde el CRM.',
                                                 'Mismas preguntas que su reporte de los lunes: cuántos contactos entraron, en qué estado están, de dónde vienen y a quién hay que seguir. Lo que el CRM todavía no registra se marca en ámbar.',
                                                 'Semanas de jueves a miércoles, como el reporte original. Contactos por fecha de ingreso; visitas y recontactar por la última actualización del contacto en la semana. Nombres de pila, como en el reporte.')
       + f'<div class="cutx" style="border-left-color:var(--warn)"><div class="cutx-h"><span class="cutx-ic">{I("eye")}</span><div><span class="cutx-k">Cotejo con el reporte manual</span>'
       '<b>Tres diferencias que el CRM resuelve. <em>Y tres que el CRM todavía no ve.</em></b>'
       f'<p>Del 01/10 al 07/10 el reporte dice 80 contactos; Prometheo registra {RW[2]["n"]}. El reporte cuenta 54 contactos de LT; Prometheo, {RW[2]["ori"].get("LT (formulario)", 0)}: '
       f'la diferencia son formularios que no entraron al CRM. Y el bloque de estados (54 · 15 · 8 · 4) es igual en las dos semanas: es lo que pasa cuando se arma a mano.</p></div></div>'
       f'<div class="cutx-g"><div><span>{I("anun")}Formularios fuera del CRM</span><b>≈ 29</b><p>contactos de LT esa semana que están en el reporte y no en Prometheo.</p></div>'
       f'<div><span>{I("cal")}Visitas sin tag</span><b>5 → {len(RW[1]["vis"])}</b><p>visitas del 24/09 al 30/09 en el reporte contra las que tienen tag en el CRM.</p></div>'
       f'<div><span>{I("lock")}Reserva sin registrar</span><b>9G</b><p>la reserva de Maker Núñez del reporte no tiene el tag de venta en Prometheo.</p></div></div>'
       f'<div class="cutx-f">{I("arrow")}<span>Lo que falta para que este reporte salga solo está abajo, en "Lo que hay que sumar al CRM".</span></div></div>'
       + sec('Reporte semanal · elegí la semana') + rw_tabs + weeks_html
       + sec('Reporte mensual · indicadores de Vanesa') + monthly
       + qbd('Contactos, entrevistas y ventas salen del CRM; inversión, CPC, CPE y CPV necesitan el gasto. Los ratios con pocas entrevistas o ventas se leen como orden, no como tasa.',
             'CPC = inversión ÷ contactos · CPE = inversión ÷ entrevistas · CPV = inversión ÷ ventas. "CM" del reporte original queda a confirmar con Vanesa. Entrevista = Visita Realizada en compradores; venta = "Convertido" en compradores. Instagram (mensaje directo) es el canal de Prometheo: tuvo 163 conversaciones del 22 al 30/07 y ninguna después.')
       + sec('Lo que hay que sumar al CRM para que el reporte salga solo') + mclegend() + CRMRD
       + yeq('El reporte de Vanesa ya se puede armar desde el CRM en contactos, estados y origen. Para entrevistas, ventas y costos faltan tres cosas: marcar la visita con fecha, un tag de venta limpio y la inversión por origen. Con eso, CPC, CPE y CPV salen solos cada mes.')
       + '</section>')
PANELS.insert(1, rep)

# ================= 7 · DEMANDA =================
P_ = D['P']; Z = D['zona2']; ZN = D['zona_n']
zon = sorted([(k, v) for k, v in Z.items() if k != 'Otros barrios'], key=lambda x: -x[1])
tip = sorted(D['d_tip'].items(), key=lambda x: -x[1])
fin = sorted(D['d_fin'].items(), key=lambda x: -x[1])
pay = D['d_pago']; payl = [('Financiado', pay.get('financiado', 0)), ('Apto crédito', pay.get('apto_credito', 0)), ('Contado', pay.get('contado', 0)), ('Otro', pay.get('otro', 0))]
payn = sum(v for _, v in payl)
NFM = D['nofit_m']; nf_items = [(k, v) for k, v in NFM.items() if k not in ('Sin motivo claro',)]
nfn = sum(v for _, v in nf_items)
def blk(icon, title, n, base, level, items, color, extra='', missing=None):
    r = f'base declarada: {n} de {base} · {pct(n, base)} {lvl(level)}'
    body = bars(items, n, color)
    if missing is not None: body += bar('Sin dato', num(missing), f'{pct(missing, base)} del total', 100 * missing / max(v for _, v in items), miss=True)
    return card(icon, title, 'pro', r, body + extra)
dem = ('<section class="panel p-demanda">' + head('Demanda · qué pide el mercado', 'Núñez manda:', '4 de cada 10 que dicen barrio.',
                                                'Qué barrio, qué tipología, para qué y cómo quieren pagar quienes consultan.',
                                                f'Base: consultas de compra procesadas por la IA ({P_} conversaciones). Doble lectura cuando la cobertura es menor al 80%: sobre el total y sobre quienes declaran el dato. Las variables multi-select no suman 100%.')
       + '<div class="g2">'
       + blk('pin', 'Barrio de interés (Tokko)', ZN, P_, level_of(100 * ZN / P_), zon, 'var(--vio)', note('Calles normalizadas a su barrio (Manzanares y Cabildo → Núñez; Regimiento de los Patricios → Barracas; Drago y Lavalleja → Villa Crespo). Un lead puede declarar más de uno.'))
       + blk('home', 'Tipología', sum(1 for _ in range(1)) and D['cov']['Tipología'][0], P_, level_of(D['cov']['Tipología'][1]), tip, 'var(--blu)', note(f'{D["d_tip_multi"]} registros listan varias tipologías: puede ser lo que ofreció el agente.'), missing=P_ - D['cov']['Tipología'][0])
       + blk('user', 'Para qué compran', D['s_fin'] if False else sum(v for _, v in fin), P_, 'indicio', fin, 'var(--pnk)', note('Indicio: se lee el orden, no el porcentaje. Inversión pesa más en Green Line.'), missing=P_ - sum(v for _, v in fin))
       + blk('dollar', 'Forma de pago', payn, P_, 'indicio', payl, 'var(--good)', note('Más de la mitad de los que declaran forma de pago quiere financiar o necesita apto crédito.'), missing=P_ - payn)
       + card('cal', 'Cuándo compran', None, lvl('noexiste'), empty('clock', 'No hay variable de plazo', 'TKVA no tiene "Horizonte de compra". Sin ella, "compra ya" no se puede medir y el hot lead pierde su señal más fuerte. Posible mejora 6.'))
       + card('alert', 'Estado de obra que buscan', None, lvl('noexiste'), empty('building', 'No hay variable de estado de obra ni de objeción', 'Las frases sobre entrega aparecen en el resumen (ver Criterio comercial), pero no se cuentan.'))
       + '</div>' + sec('Por qué no compran · motivo del No Fit') + '<div class="g2">'
       + card('x', 'Motivo del No Fit', 'calc', f'base: {nfn} de {D["nodem_det"]["No Fit"]} No Fit con motivo identificable · {lvl("indicio")}', bars(sorted(nf_items, key=lambda x: -x[1]), nfn, 'var(--ink4)')
              + note(f'Leído del resumen de la IA: {NFM["Sin motivo claro"]} No Fit no dicen por qué. {NFM.get("Sigue evaluando (mal cerrado)", 0)} siguen evaluando: se cerraron antes de tiempo.'))
       + quote('Precio · cómo lo dicen (resumido por la IA)', ['«Rechazó la propuesta por precio: "muy caro para mí".» · Liberti · 2 ambientes',
                                                            '«Indicó que el precio supera su presupuesto y planea sacar una hipoteca.» · Liberti · 2 ambientes',
                                                            '«El 2 ambientes excede su presupuesto; declaró USD 80.000.» · Green Line · inversión',
                                                            '«Necesita disponibilidad para fines de septiembre, pero Maker Núñez se entrega en diciembre.» · Maker Núñez · vivienda'])
       + '</div>' + card('dollar', 'Presupuesto', None, lvl('noreport'),
                         empty('lock', 'No reportable como distribución', f'{D["pres"][0]} contactos con un monto real y {D["pres_cero"]} guardados como 0. Entre los que dieron monto, la mitad está por debajo de USD {num(D["pres"][1])} (rango central: USD {num(D["pres"][2])} a {num(D["pres"][3])}), con n chico. Se corrige con la Posible mejora 5.'))
       + yeq('Núñez y Maker Núñez son lo que más se pide, en 2 ambientes y con financiación. El precio es el primer motivo de No Fit: la primera respuesta tiene que ofrecer la unidad más chica o el plan de pagos antes de cerrar la charla.')
       + '</section>')
PANELS.append(dem)

# ================= 8 · CRITERIO COMERCIAL =================
crt = ('<section class="panel p-criterio">' + head('Criterio comercial · por qué consultan hoy', 'El agente sabe qué buscan.', 'Todavía no registra por qué ahora.',
                                                  'Qué problema trae cada lead y qué lo hizo consultar hoy: es el dato que ordena a quién llamar primero. Capa elegida para TKVA: Jobs to be Done (B2C de ticket alto y ciclo largo).',
                                                  'Núcleo fijo de cinco campos: problema, impacto, causa raíz, evento disparador y resultado de contacto. Base: conversaciones de compra procesadas.')
       + table(['Campo del núcleo', 'Variable en Prometheo', 'Lo carga', 'Cobertura', 'Nivel', 'Estado'], [
           ['Problema declarado', '—', 'Agente · cita', '—', lvl('noexiste'), 'Solo aparece parafraseado en el Resumen por IA'],
           ['Impacto', '—', 'Agente', '—', lvl('noexiste'), 'No existe la variable'],
           ['Causa raíz', '—', 'Agente', '—', lvl('noexiste'), 'No existe la variable'],
           ['Evento disparador', '—', 'Agente', '—', lvl('noexiste'), 'Se propone "Evento Disparador" (Opciones), Posible mejora 6'],
           ['Resultado de contacto', '<code>tags del embudo Venta y Cierre</code>', 'Vanesa', f'{pct(D["humana"], D["compra"])}', lvl('noreport'), f'{D["humana"]} compradores con visita, negociación o cierre']], 760, txt=True)
       + qbd('Ningún campo del núcleo existe como variable: el hallazgo es la ausencia, no la distribución. Por eso esta pestaña no titula porcentajes y muestra lo que dice el resumen de la IA.',
             'El cruce impacto alto × disparador de menos de 30 días (a quién llamar primero) queda bloqueado hasta que existan las variables. Mientras tanto, la cola se ordena por hot lead.')
       + sec('A voz de quien consulta · lo que resume la IA, sin convertir en porcentaje')
       + qbd('Cada frase es de una persona: no es un patrón. El contador dice en cuántas conversaciones procesadas aparece el tema en el resumen; la acción dice qué cambiar.')
       + '<div class="g3">'
       + quote('Financiación y cuotas · 228 resúmenes lo mencionan', ['«Consultó si podía pagar el 50% y financiar el saldo con crédito hipotecario.» · Maker Núñez · vivienda', f'{mc("start")} Primera respuesta con anticipo y cuotas del proyecto.'])
       + quote('Apto crédito · 45 resúmenes', ['«Se le indicó que Maker Núñez no es apto crédito y ofrece financiación propia.» · Maker Núñez', 'Ventas · ofrecer Liberti (apto crédito) cuando el lead lo necesita.'])
       + quote('Cochera · 42 resúmenes', ['«Las opciones de Maker Belgrano no le interesaron porque no tenían cochera.» · Maker Belgrano', 'Marketing · decir en el anuncio qué proyectos tienen cochera.'])
       + quote('Entrega · 24 resúmenes', ['«Consultó por entrega inmediata; Maker Núñez tiene entrega estimada en diciembre de 2026.» · Maker Núñez · vivienda', f'{mc("start")} Fecha de entrega en la primera respuesta.'])
       + quote('Inversión y renta · 135 resúmenes', ['«Busca una propiedad para alquilar por Airbnb, similar a sus unidades en Saavedra.» · Maker Núñez · inversión', 'Ventas · llamar con rentabilidad estimada y plan de pagos.'])
       + quote('Familia · 28 resúmenes', ['«Busca monoambientes para futura vivienda de uno de sus hijos.» · Maker Núñez y Green Line · vivienda', 'Es un evento disparador: hoy no se registra.'])
       + '</div>' + sec('Qué cambiar para que el criterio se pueda medir') + '<div class="fxg c3">'
       + fx('var(--vio)', 'var(--vio-soft)', 'compass', 'Variable nueva', 'Crear "Evento Disparador"', 'Hoy no existe: el cruce impacto × disparador está bloqueado.', 'Opciones del rubro: vende otra propiedad, necesita mudarse, vivienda para un familiar, inversión o renta, termina un alquiler.', 'Venta · CRM › Posible mejora 6')
       + fx('var(--vio)', 'var(--vio-soft)', 'x', 'Variable nueva', 'Crear "Objeción Principal"', 'El precio aparece como primer motivo de No Fit, pero solo se puede leer en el texto.', 'Opciones: precio, entrega, financiación o crédito, ubicación, tamaño, cochera, otro.', 'Venta · CRM › Posible mejora 6')
       + fx('var(--warn)', 'var(--warn-bg)', 'hand', 'Del equipo', 'Resultado de contacto', f'{D["humana"]} compradores con etapa del equipo en tres meses.', 'Visita realizada, reserva o "No Concretado" con motivo, marcados por Vanesa.', 'Vanesa y el agente')
       + '</div>' + legend()
       + acts([act('medir', 'AUREA', [20, 10, 0, 10, 5, 10], 'Criterio comercial · ninguno de los cinco campos existe como variable', 'Cobertura del núcleo de criterio comercial', f'{B} conversaciones de compra procesadas', '0 de 5 campos con variable · el motivo solo está en el resumen de la IA', CIT,
                   'Crear "Objeción Principal" y "Evento Disparador" como variables de Opciones y reforzar en el prompt que se carguen solo cuando el lead lo dice.',
                   'Prometheo › Variables · prompt del agente (Posible mejora 6)', 'Las dos variables por encima del 40% de las conversaciones procesadas en 30 días.', 'Cobertura de las dos variables, al 30/11.', 'gasto de extracción por charla (cada variable nueva consume).',
                   'Dato central No reportable (no hay variable): la card existe como Medir con techo 29.', 'No reportable', mcard='start')], 1)
       + yeq('El agente sabe qué buscan y cuánto pueden pagar, pero no qué los frena ni qué los hizo consultar hoy. Con dos variables nuevas, esta pestaña ordena a quién llamar primero y le da a la pauta el "por qué ahora".')
       + '</section>')
PANELS.append(crt)

# ================= 9 · INSIGHTS Y ACCIONABLES =================
ADS = {a['id']: a for a in D['ads']}
def adcard(verb, owner, parts, how_v, how_t, title, a, bul, hacer, donde, big, txt, cmpw, cmpk, cmplab, medimos, guard, why, techo):
    score = min(sum(parts), {'Hecho': 100, 'Señal': 79, 'Indicio': 54}[techo]); ic, vl = VERB[verb]
    qj = ''.join(f'<div class="qj"><span>{n}</span><span class="qk"><i style="width:{round(100*p/m)}%"></i></span><b>{p}/{m}</b></div>' for (n, m), p in zip(PARTS, parts))
    lis = ''.join(f'<li>{b}</li>' for b in bul)
    return (f'<details class="i3 av pz" data-v="{verb}"><summary><div class="qbg"><span class="qbz"><span class="qcp">{I(ic)}</span>{vl}</span><span class="{OWN[owner]}">{owner}</span>{gauge(score)}</div>'
            f'<div class="subrow">{I("arrow")}<span>Cómo</span><span class="subv">{I("flask")}{how_v}</span><span>{how_t}</span></div><div class="qbr">{title}</div><div class="qbh">'
            f'<div class="cx"><span class="ql k-anun">{I("anun")}</span><span class="qm">Anuncio</span><span class="qn">{esc(a["name"][:60])}<span class="anm">ID {a["id"]}</span></span></div>'
            f'<div class="cx"><span class="ql k-camp">{I("building")}</span><span class="qm">Proyecto</span><span class="qn">{a["pj"]} · {a["pj_n"]} de {a["pj_tot"]} lo piden</span></div>'
            f'<div class="cx"><span class="ql qbq">{I("users")}</span><span class="qm">Público</span><span class="qn">{a["viv"]} vivienda · {a["inv"]} inversión</span></div></div>'
            f'<div class="qbc"><span class="op">Ver análisis y qué hacer</span><span class="cl">Plegar</span>{I("chev")}</div></summary>'
            f'<div class="qh"><div class="qi"><span class="n">{I("eye")}</span>Qué muestra el CRM</div><ul class="i3-b">{lis}</ul></div>'
            f'<div class="qh"><div class="qi"><span class="n">{I("arrow")}</span>Qué hacer</div><p class="qp">{hacer}</p><div class="qz">{I("pin")}<span><b>Dónde se cambia:</b> {donde}</span></div></div>'
            f'<div class="qh"><div class="qi"><span class="n">{I("target")}</span>Efecto esperado</div><div class="res"><div class="big">{big}</div><div class="rt"><div class="txt">{txt}</div>'
            f'<div class="cmp"><span class="fill" style="width:{cmpw:.1f}%"></span><span class="mk c" style="left:calc({cmpk:.1f}% - 1px)"><b>{cmplab}</b></span></div>'
            f'<div class="cmp-lg"><span><i class="sw"></i>este anuncio</span><span><i class="sm"></i>{cmplab}</span></div></div></div></div>'
            f'<div class="qh"><div class="qi"><span class="n">{I("pulse")}</span>Cómo lo medimos</div><p class="qp">{medimos}</p><div class="qca">{I("shield")}<span><b>Guardiana:</b> {guard}</span></div></div>'
            f'<div class="qh qbs"><div class="qi"><span class="n">{I("gauge")}</span>Por qué este índice {gauge(score, True)}</div><div class="qcb">{qj}</div>'
            f'<p class="qbi">{why} Techo por el dato central ({techo}): {score if False else {"Hecho":100,"Señal":79,"Indicio":54}[techo]}. Rúbrica v1, sin calibrar: el resultado se registra al cierre del período.</p></div></details>')
avg = 100 * CAL_A / B
aL = ADS['120247657051160615']; aG = ADS['120250550832800615']; aN = ADS['120250791067620615']; aE = ADS['120250284174290615']; aT = ADS['120250768745120562']
ins_cards = [
    adcard('corregir', 'Marketing', [14, 10, 11, 15, 5, 12], 'Probar', 'un copy con precio desde y plan de pagos',
           f'«EN VENTA · Liberti»: el que más contactos trae, y la mitad termina en No Fit', aL,
           [f'<b>{aL["n"]} contactos</b>, el anuncio con más volumen; {aL["cal"]} calificados de {aL["b"]} procesados ({pct(aL["cal"], aL["b"])}).',
            f'<b>{aL["nofit"]} No Fit</b> ({pct(aL["nofit"], aL["n"])}): el motivo más repetido es el precio de 2 ambientes desde USD 140.000.',
            f'{aL["unavez"]} escribieron una sola vez: llegan por "apto crédito" y se van con el precio.'],
           'Decir el precio desde y el plan de pagos en el anuncio, y que la primera respuesta ofrezca la unidad más chica o el esquema de cuotas antes de cerrar la charla.',
           'Administrador de anuncios › copy del anuncio · prompt del agente, primera respuesta sobre Liberti',
           pct(aL['nofit'], aL['n']), 'de los contactos del anuncio terminan en No Fit. Promedio de compradores: 14%.', 100 * aL['nofit'] / aL['n'], 14, 'promedio 14%',
           'No Fit y calificados del anuncio, misma base, al 30/11.', 'volumen de consultas del anuncio.',
           'Cruce por ID de anuncio con el criterio EDFAN y el tag No Fit (Hecho); el motivo de precio se lee del resumen (Indicio). Sin gasto no se sabe cuánto cuesta cada calificado.', 'Señal'),
    adcard('mantener', 'Marketing', [8, 10, 11, 15, 5, 12], 'Probar', 'el mismo creativo en Maker Belgrano',
           '«La obra avanza…» (Maker Núñez): pocos contactos, la mayor proporción de hot leads', aN,
           [f'{aN["n"]} contactos desde el 02/10; {aN["hot"]} hot leads ({pct(aN["hot"], aN["n"])}) y {aN["cal"]} calificados.',
            f'Pide Maker Núñez: {aN["pj_n"]} de {aN["pj_tot"]} lo nombran. Ningún contacto de no-demanda.',
            'Habla de entrega cercana: es lo que pregunta quien compra pronto.'],
           'Mantener el anuncio y el creativo. Probar el mismo enfoque ("la obra avanza, falta poco para la entrega") en otro proyecto con entrega cercana.',
           'Administrador de anuncios › duplicar el conjunto con otro proyecto',
           pct(aN['hot'], aN['n']), 'de los contactos del anuncio son hot leads. Promedio de compradores: 13%.', 100 * aN['hot'] / aN['n'], 13, 'promedio 13%',
           'Hot leads y calificados del anuncio, al 30/11.', 'que el volumen no caiga por debajo de 10 contactos por semana.',
           'n chico (15 contactos): es una prueba, no una tendencia.', 'Señal'),
    adcard('proteger', 'Marketing', [8, 10, 11, 15, 5, 12], 'Sostener', 'el anuncio de Green Line y revisar la no-demanda',
           '«Green Line sigue avanzando»: el único activo desde agosto, con hot leads constantes', aG,
           [f'{aG["n"]} contactos del {aG["desde"]} al {aG["hasta"]}; {aG["hot"]} hot leads y {aG["cal"]} calificados.',
            f'{aG["nodem"]} de no-demanda ({pct(aG["nodem"], aG["n"])}): inmobiliarias que preguntan por el proyecto.',
            'Green Line es el proyecto que mejor califica (33%).'],
           'Mantenerlo activo y excluir de la audiencia a inmobiliarias (lista de exclusión de Audiencias).',
           'Administrador de anuncios › públicos de exclusión',
           pct(aG['hot'], aG['n']), 'de los contactos del anuncio son hot leads. Promedio de compradores: 13%.', 100 * aG['hot'] / aG['n'], 13, 'promedio 13%',
           'Hot leads y no-demanda del anuncio, al 30/11.', 'calificación del anuncio.', 'Cruce por ID de anuncio; n chico.', 'Señal'),
    adcard('corregir', 'Marketing', [14, 10, 15, 15, 5, 12], 'Revisar', 'qué anuncios corrían del 29/08 al 15/09',
           '«Los espacios cobran vida…»: 69 de sus 74 contactos llegaron sin que el agente registrara nada', aE,
           [f'{aE["n"]} contactos del {aE["desde"]} al {aE["hasta"]}: casi todo el anuncio cayó en el hueco del agente.',
            f'{aE["sinproc"]} sin resumen, tags ni variables: no se sabe qué proyecto pidieron ni si calificaban.',
            'La pauta siguió activa mientras el agente no cargaba datos.'],
           'Revisar a mano esos contactos (filtro por ID de anuncio en Prometheo) y, la próxima vez, pausar la pauta si el agente se pausa.',
           'Prometheo › Contactos › filtro por ID de anuncio · Administrador de anuncios',
           pct(aE['sinproc'], aE['n']), 'de los contactos del anuncio quedaron sin procesar. Resto del período: 9%.', 100 * aE['sinproc'] / aE['n'], 9, 'resto 9%',
           'Contactos del anuncio con resumen, al 30/11.', 'que no se dupliquen mensajes a quien ya respondió.', 'El hueco se ve en un campo del sistema (Hecho).', 'Hecho')]
okI = (f'<div class="okband"><div class="okic">{I("checkc")}</div><div><span class="okk">Mejora continua · hecha</span>'
       '<b class="okt">Línea B2B aparte: el agente ya no gasta saldo en inmobiliarias y proveedores.</b>'
       f'<p>Insight del período anterior: muchas inmobiliarias y proveedores escribían a la línea de ventas y el agente los atendía como compradores ({num(b2b_msgs)} mensajes, {pct(b2b_msgs, EV["total"])} de lo que envió TKVA). '
       'A pedido de TKVA se abrieron dos líneas: B2C con agente y B2B sin agente. El efecto se mide el próximo período con la no-demanda en la línea de ventas.</p>'
       f'<div class="okf">{mc("start")}<span class="qq" style="--c:var(--good)">Ver Inmobiliarias y proveedores</span></div></div></div>')
INS = [('anun', 'crit', 'Agente sin procesar 18 días', f'{G["sinproc"]} conversaciones sin datos y {G["ad"]} contactos de pauta en el hueco.', 'Carga semanal medida y aviso antes de pausar.', 'Consumo variable CRM', 'start'),
       ('inb', 'warn', 'Formularios de LT por fuera', f'LT califica {pct(LT["cal"], LT["b"])} contra {pct(WA["cal"], WA["b"])} de WhatsApp, y una parte ni siquiera entra a Prometheo.', 'Integración Go High Level o Meta Forms (Pro); primer mensaje o carga (Start).', 'Integraciones', 'pro'),
       ('ig', 'warn', 'Instagram sin datos desde el 30/07', '163 conversaciones por mensaje directo del 22 al 30/07; ninguna después.', 'Confirmar si se desconectó o se apagó a propósito y reconectar.', 'Integraciones', 'start'),
       ('dollar', 'vio', 'El precio frena Liberti', f'{D["proj"][1]["nofit"]} No Fit en Liberti; el motivo más repetido es 2 ambientes desde USD 140.000.', 'Unidad más chica o plan de pagos antes de cerrar la charla.', 'Demanda', 'start'),
       ('repeat', 'good', 'El seguimiento funciona', f'{CALSEG} de {CAL_A} calificados tienen próximo paso.', 'Sostenerlo y sumar los hot leads a la cola.', 'Venta · CRM', None),
       ('building', 'blu', 'Tokko empezó a cargar unidades', 'Propiedades interesadas pasó de 1% en julio a 58% en octubre: ahora se ve qué unidad pregunta cada lead.', 'Usarlo para el aviso de hot lead.', 'Proyectos', None)]
def insfx(icon, tone, title, found, fix, where, m):
    col = {'crit': ('var(--crit)', 'var(--crit-bg)'), 'warn': ('var(--warn)', 'var(--warn-bg)'), 'vio': ('var(--vio)', 'var(--vio-soft)'), 'good': ('var(--good)', 'var(--good-bg)'), 'blu': ('var(--blu)', 'var(--blu-soft)')}[tone]
    return fx(col[0], col[1], icon, f'Insight {mc(m)}' if m else 'Insight', title, found, fix, where)
insp = ('<section class="panel p-insights">' + head('Insights y accionables · del período y anuncio por anuncio', 'Primero lo que ya se hizo.', 'Después, lo que sigue.',
                                                    'Cada insight dice qué encontramos y qué cambiar. Cada anuncio, medido por calidad: cuántos conversan, cuántos califican y cuántos no son demanda.',
                                                    'Cohorte: contactos del 22/07 al 14/10, por el primer anuncio registrado. Calificación sobre la demanda de compra procesada. La misma definición en todo el tablero.')
        + sec('Mejora continua · ya aplicada') + okI
        + sec('Insights del período') + mclegend() + '<div class="fxg c3">' + ''.join(insfx(*x) for x in INS) + '</div>'
        + '<div class="g4">'
        + kpi('checkc', 'grn', 'calc', 'Califican · promedio', pct(CAL_A, B), None, '', None, f'{CAL_A} de {B} conversaciones de compra procesadas')
        + kpi('flame', 'pnk', 'calc', 'Más hot leads', 'La obra avanza', None, '', None, f'Maker Núñez · {aN["hot"]} de {aN["n"]}')
        + kpi('alert', 'amb', 'calc', 'Anuncio a revisar', 'Liberti', None, '', None, f'{aL["nofit"]} No Fit de {aL["n"]}')
        + kpi('chat', 'blu', 'pro', 'Con anuncio identificado', pct(D['con_ad'], D['total']), None, '', None, f'{D["con_ad"]} de {num(D["total"])} contactos')
        + '</div>' + sec('Cómo leer cada card · anuncio › proyecto › público')
        + f'<div class="howr"><div><span class="ql k-anun">{I("anun")}</span><div><b>Anuncio</b><span>Lo que se ve en Meta. Llega a Prometheo con su ID en cada consulta.</span></div></div>'
          f'<div><span class="ql k-camp">{I("building")}</span><div><b>Proyecto</b><span>Qué proyecto pide quien escribe desde ese anuncio.</span></div></div>'
          f'<div><span class="ql qbq">{I("users")}</span><div><b>Público</b><span>Para qué compra: inversión o vivienda. Campaña, conjunto y costo llegan con el export de Meta.</span></div></div></div>'
        + sec('Insights y accionables · una card por anuncio') + legend() + f'<div class="igrid avg">{"".join(ins_cards)}</div>'
        + yeq('La separación B2B ya está hecha. Lo que sigue: que el agente no vuelva a quedar sin procesar, que los formularios de LT entren solos y que Liberti responda al precio antes de que la charla termine en No Fit.')
        + '</section>')
PANELS.append(insp)

# ================= 10 · META · ANUNCIOS EN PROMETHEO =================
def adx(a, color, soft, verdict, vc):
    b = max(a['b'], 1)
    tiles = (f'<div class="ad-t" data-s=""><span>{I("chat")}Contactos</span><b>{a["n"]}</b></div>'
             + (f'<div class="ad-t" data-s="{"good" if a["cal"]/b >= .2 else "warn"}"><span>{I("checkc")}Calificó</span><b>{pct(a["cal"], b)}<small>{a["cal"]} de {a["b"]}</small></b></div>' if a['b'] >= 10 else
              f'<div class="ad-t" data-s="warn"><span>{I("checkc")}Calificó</span><b>s/d<small>{a["b"]} procesadas</small></b></div>')
             + f'<div class="ad-t" data-s=""><span>{I("users")}Inv. / viv.</span><b>{a["inv"]} / {a["viv"]}</b></div>')
    rows = [('Conversó', a['convo'], a['compra']), ('Procesado por la IA', a['b'], a['compra']), ('Hot lead', a['hot'], a['compra']), ('Pide financiación', a['fin'], a['compra']), ('Una sola vez', a['unavez'], a['compra']), ('No Fit', a['nofit'], a['n'])]
    fun = ''.join(f'<div class="qcg pc"><span>{k}</span><i style="width:{100*v/max(t,1):.0f}%"></i><b>{v}<small>{pct(v, t)}</small></b></div>' for k, v, t in rows)
    return (f'<div class="adx" style="--ax:{color};--axb:{soft}"><div class="adx-h"><span class="adx-ic">{I("anun")}</span><div style="min-width:0"><b>{esc(a["name"][:58])}</b>'
            f'<span>{I("building")}pide {a["pj"]} ({a["pj_n"]} de {a["pj_tot"]}) · {a["desde"]} al {a["hasta"]} · ID {a["id"]}</span></div></div>'
            f'<div class="adx-tiles">{tiles}</div><div class="adx-fun">{fun}</div><div class="adx-v" style="--vc:{vc[0]};--vb:{vc[1]}">{I("bulb")}<span>{verdict}</span></div></div>')
GOOD = ('var(--good)', 'var(--good-bg)'); WARN = ('var(--warn)', 'var(--warn-bg)'); CRIT = ('var(--crit)', 'var(--crit-bg)')
coh_ads = [a for a in D['ads'] if a['pj_tot'] >= 3 and any(p.lower() in a['name'].lower() for p in ['liberti', 'green line', 'maker', 'drago', 'obra avanza'])]
fichas = (adx(aL, 'var(--vio)', 'var(--vio-soft)', 'Trae volumen, pero la mitad termina en No Fit por precio. Corregir el copy y la primera respuesta.', CRIT)
          + adx(aT, 'var(--blu)', 'var(--blu-soft)', 'Corrió en el arranque (22 al 29/07). Nombre genérico ("TKVA 2"): casi nadie dijo proyecto. No volver a uno genérico.', WARN)
          + adx(aG, 'var(--pnk)', 'var(--pnk-soft)', 'El único activo desde agosto, con hot leads constantes. Sostenerlo y excluir inmobiliarias.', GOOD)
          + adx(aN, 'var(--good)', 'var(--good-bg)', 'Nuevo (desde el 02/10): la mayor proporción de hot leads. n chico: es una prueba.', GOOD)
          + adx(aE, 'var(--warn)', 'var(--warn-bg)', 'Cayó entero en el hueco del agente: sin datos de quién escribió. Revisar a mano.', CRIT))
meta = ('<section class="panel p-metaprom">' + head('Meta · lo que Prometheo ya sabe de cada anuncio', 'Sin el export de Meta,', 'igual sabemos qué trae cada anuncio.',
                                                    'Cada consulta que llega desde un anuncio trae su ID de anuncio. Con eso, Prometheo dice qué proyecto pide, quién es y si califica. Lo que falta es el gasto.',
                                                    'Datos de Prometheo: ID Anuncio y nombre del anuncio por contacto. Vigencia = primera y última consulta registrada con ese ID, no las fechas de la campaña en Meta.')
        + '<div class="g4">'
        + kpi('anun', 'blu', 'pro', 'Anuncios con contactos', str(len(D['ads'])), None, '', None, f'{sum(1 for a in D["ads"] if a["n"] >= 10)} con 10 o más contactos', None, 'Un ID = un anuncio de Meta.')
        + kpi('target', 'pnk', 'pro', 'Contactos con anuncio', pct(D['con_ad'], D['total']), None, '', None, f'{D["con_ad"]} de {num(D["total"])}', None, 'Indicio: la mayor parte de la pauta va a la landing y a los formularios de LT, que no pasan el ID.')
        + kpi('checkc', 'grn', 'calc', 'Coherencia anuncio → proyecto', pct(sum(a['pj_n'] for a in coh_ads), sum(a['pj_tot'] for a in coh_ads)), None, '', None, f'{sum(a["pj_n"] for a in coh_ads)} de {sum(a["pj_tot"] for a in coh_ads)} piden el proyecto del anuncio', None, 'Sobre los anuncios que nombran un proyecto.')
        + kpi('layers', 'amb', 'pro', 'Multi-toque', str(D['multi_ad']), None, '', None, 'contactos con más de un ID de anuncio')
        + '</div>' + sec('Ficha por anuncio · los de más contactos y los que hay que mirar') + f'<div class="adg">{fichas}</div>'
        + qbd('Porcentajes sobre la demanda de compra del anuncio (sin inmobiliarias, proveedores ni No Fit); No Fit sobre todos los contactos del anuncio.',
              'Primer anuncio registrado en el contacto. Calificación sobre conversaciones procesadas por la IA. Inversión / vivienda es Indicio: se lee como orden.')
        + sec('Qué le dice esto a la pauta') + '<div class="fxg c3">'
        + fx('var(--good)', 'var(--good-bg)', 'checkc', 'Mantener', 'Un anuncio por proyecto', 'Los anuncios que nombran un proyecto traen gente que pide ese proyecto; el genérico «TKVA 2» casi no deja proyecto.', 'Seguir con un anuncio por proyecto.', 'Coherencia anuncio → proyecto')
        + fx('var(--crit)', 'var(--crit-bg)', 'dollar', 'Corregir', 'Liberti y el precio', 'El anuncio dice "apto crédito" y trae a quien necesita crédito con presupuesto menor al precio.', 'Precio desde y cuotas en el copy.', 'Insights › Liberti')
        + fx('var(--vio)', 'var(--vio-soft)', 'layers', 'Medir', 'Formularios sin ID', 'La pauta que va a la landing de LT no deja ID de anuncio en Prometheo.', 'Remarketing a Click to WhatsApp directo, con mensaje propio por proyecto.', 'Integraciones › Formularios LT')
        + '</div><div class="qbe mt"><div class="qbj">' + I('lock') + 'Lo que se suma cuando llegue el export de Meta<span class="r">faltante de integración</span></div>'
        '<ul class="i3-b" style="--tone:var(--ink4)"><li>Gasto, impresiones y clics por ID de anuncio y por día, del 22/07 al 14/10, y la plataforma (Facebook o Instagram).</li>'
        '<li>Con el mismo ID: costo por contacto (CPC), por entrevista (CPE) y por venta (CPV), los tres costos del reporte de Vanesa.</li>'
        '<li>El conteo de contactos lo sigue poniendo Prometheo: Meta explica de dónde vinieron, no cuántos fueron.</li></ul></div>'
        + yeq(f'El {pct(D["total"] - D["con_ad"], D["total"])} de los contactos llega sin ID de anuncio: es la parte ciega. Pasar el remarketing a Click to WhatsApp y que los formularios entren con su origen es lo que achica ese hueco.')
        + '</section>')
PANELS.append(meta)

# ================= 11 · CONSUMO VARIABLE CRM (Tokens IA | META) =================
PANEL = {'ago': (138.00, 269), 'sep': (62.48, 563), 'oct': (74.20, 325)}
REP = {'Agosto': [('Extracción de datos', 35), ('Generación de texto', 27), ('Asignación de Smart Tags', 16), ('Mi Prometheo', 14), ('Respuesta del asistente', 6), ('Otros gastos', 3)],
       'Septiembre': [('Respuesta del asistente', 42), ('Extracción de datos', 22), ('Asignación de Smart Tags', 11), ('Respuesta del asistente (testing)', 11), ('Sugerencia de respuesta', 8), ('Otros gastos', 7)],
       'Octubre al 14': [('Respuesta del asistente', 52), ('Extracción de datos', 27), ('Asignación de Smart Tags', 15), ('Detección de bots', 2), ('Respuesta del asistente (testing)', 1), ('Otros gastos', 2)]}
TOT = {'Agosto': 138.00, 'Septiembre': 62.48, 'Octubre al 14': 74.20}
def rep_card(mes, tone):
    rows = REP[mes]; t = TOT[mes]
    return card('pie', f'En qué se gasta · {mes.lower()}', 'panel', f'total del panel USD {num(t, 2)}',
                ''.join(bar(k, f'USD {num(t * p / 100, 2)}', f'{p}%', p * 100 / max(x for _, x in rows), tone) for k, p in rows))
cv_tabs = f'<div class="subtabs cvtabs"><label for="cv-ia">{I("bot")}Tokens IA · Prometheo</label><label for="cv-meta">{I("wa")}META · WhatsApp</label></div>'
vsplit = ('<div class="vsplit"><div class="vs" style="--vsc:var(--vio)"><span class="k">Variable 1 · Tokens IA</span><b class="t">Prometheo cobra la inteligencia</b>'
          '<p>Saldo de IA que consume el agente en cada conversación: responder, extraer variables, asignar tags. Se carga aparte del abono de Prometheo.</p></div>'
          '<div class="vs" style="--vsc:var(--good)"><span class="k">Variable 2 · META</span><b class="t">Meta cobra el canal</b>'
          '<p>Desde el 1/10/2026, cada respuesta por la API oficial de WhatsApp tiene costo, con 1.000 gratis por mes por número. Lo factura Meta, en pesos, directo a TKVA.</p></div></div>')
ppd = 74.20 / 14
ia = ('<div class="stab st-ia"><div class="g4">'
      + kpi('pie', 'blu', 'panel', 'Consumo de IA · octubre al 14', 'USD 74,20', '+19%', 'd-flat', 'up', 'contra USD 62,48 de septiembre completo',
            f'Ritmo de octubre ≈ USD {num(ppd, 2)} por día: el mes cerraría entre USD 145 y 165 [cálculo]. Agosto: USD 138,00.', 'Panel "Entendé tu consumo". Cargar saldo no es consumir.')
      + kpi('sigma', '', 'calc', 'Costo por conversación', 'USD 0,23 a 0,51', None, '', None, 'octubre USD 0,23 · agosto USD 0,51 · septiembre no reportable',
            'Consumo del panel ÷ conversaciones del panel (oct 325, ago 269). Septiembre (USD 62,48 ÷ 563 = USD 0,11) no se usa: el agente no procesó 18 días y el resultado no es real. Para proyectar se usa USD 0,40 por conversación.', 'La referencia inicial de la propuesta (USD 20 cada 2.000 chats) quedó superada por lo medido.')
      + kpi('alert', 'amb', 'pro', 'Días sin procesar', '18', f'{G["sinproc"]} conversaciones', 'd-bad', None, 'del 29/08 al 15/09', 'Si el saldo llega a cero, el agente deja de responder y de cargar datos. Es también un faltante de datos: está declarado en Integraciones.')
      + kpi('layers', 'pnk', 'panel', 'Extracción + Smart Tags', '42%', 'del gasto de octubre', 'd-flat', None, 'USD 31,16 de USD 74,20', 'Se cobra en cada conversación, aunque no asigne nada y aunque el lead no compre.')
      + '</div>' + qci('trend', 'Consumo por mes', 'panel', 'USD del panel · conversaciones del panel',
                       (bar('Agosto · 269 conversaciones', 'USD 138,00', '≈ USD 0,51 por conversación', 100) + bar('Septiembre · 563 conversaciones (18 días sin procesar)', 'USD 62,48', 'no reportable por conversación', 100*62.48/138, 'var(--vio)') + bar('Octubre al 14 · 325 conversaciones', 'USD 74,20', '≈ USD 0,23 por conversación', 100*74.20/138, 'var(--vio)'))
                       + note('Septiembre parece más barato porque el agente casi no procesó: no es ahorro. Desde septiembre Prometheo detalla más las categorías: agosto no es comparable categoría por categoría.'))
      + '<div class="g3 mt">' + rep_card('Agosto', 'var(--ink4)') + rep_card('Septiembre', 'var(--blu)') + rep_card('Octubre al 14', 'var(--vio)') + '</div>'
      + qbd('En octubre, la respuesta del asistente es el 52% del gasto: es lo esperable. Extracción y Smart Tags juntos son el 42%, el doble de la referencia de otra cuenta del rubro (22%).',
            'Mi Prometheo fue el 14% de agosto (recalificaciones y acciones masivas). Testing (11% en septiembre) es el costo de probar el agente: baja cuando el prompt se estabiliza.')
      + '<div class="g2 mt">' + card('chat', 'A quién le habla el agente', 'pro', f'{num(EV["total"])} mensajes enviados por TKVA · 22/07 al 14/10',
                                     bars([('Compradores que conversan', EV['conv']), ('Inmobiliarias', EV['inmo']), ('Equipo interno', EV['eq']), ('No Fit', EV['nofit']), ('Proveedores', EV['prov']), ('Postventa', EV['post']), ('Compradores de un solo mensaje', EV['unavez'])], EV['total'], 'var(--vio)'))
      + card('user', 'Variables que se evalúan y casi no se usan', 'pro', f'cobertura sobre {P_} conversaciones procesadas',
             bars([('Asesor asignado', 0), ('Historial', 0), ('Fecha de visita', 1), ('Email', D['cov']['Email'][0]), ('Presupuesto con monto', D['cov']['Presupuesto (sin ceros)'][0])], P_, 'var(--warn)', maxv=P_)
             + note('Cada variable con carga automática se evalúa en cada conversación. Las que no se usan pasan a manual; la fecha de visita no: se completa al marcar la visita.'))
      + '</div>' + sec('Ahorro de tokens · acciones con score') + legend() + mclegend()
      + acts([A_CORTE,
              act('corregir', 'AUREA', [8, 5, 15, 10, 10, 15], 'Extracción y Smart Tags · 42% del gasto de IA de octubre', 'Gasto de IA en extracción de datos y Smart Tags', 'USD 74,20 de octubre al 14', 'USD 20,03 extracción + USD 11,13 Smart Tags', 'Panel "Entendé tu consumo" (captura)',
                  'Pedir a Mi Prometheo el diagnóstico de tags y variables con prompt (Posible mejora T) y pasar a manual lo que casi nunca se completa: asesor asignado, historial, email. Las etapas humanas no se apagan: se miden.',
                  'Mi Prometheo (diagnóstico de consumo) · Contactos › Variables', 'Extracción + Smart Tags por debajo del 30% del gasto en noviembre.', 'Porcentaje del panel y USD por conversación, noviembre contra octubre.', 'cobertura de las variables que califican.',
                  'El reparto sale de una captura del panel; todavía no se sabe qué tag o variable consume más (falta el diagnóstico).', 'Hecho', mcard='start'),
              act('proteger', 'Dirección', [14, 10, 15, 10, 10, 15], f'Línea B2B · {num(b2b_msgs)} mensajes a inmobiliarias y proveedores en el período', 'Mensajes del agente a no-demanda', f'{num(EV["total"])} mensajes enviados', f'{pct(b2b_msgs, EV["total"])} a inmobiliarias y proveedores · la línea aparte ya está activa', CIT,
                  'Sostener la línea B2B sin agente y que la respuesta del agente en la línea de ventas derive a la B2B cuando detecta una inmobiliaria o un proveedor.',
                  'Respuesta del agente · web y firma con el número B2B', 'Menos de 5% de los mensajes del agente a no-demanda en noviembre.', 'Mensajes a no-demanda en la línea de ventas, noviembre.', 'ningún comprador derivado por error a la línea B2B.',
                  'Mejora continua ya aplicada (Evidencia 10): falta medir su efecto con un período completo.', 'Hecho')], 3)
      + '<div class="ss-lab"><span class="n">T</span>Mi Prometheo también consume</div>'
      + qbd('Las acciones de Mi Prometheo entran en el gasto (14% de agosto). Por eso cada prompt de las Posibles mejoras está auditado, pide el conteo antes de aplicar y va en una conversación por pedido.')
      + pm('pmt', 'T', 'Posible Mejora · Corregir · AUREA', 'Diagnóstico de consumo con Mi Prometheo', 'Un pedido de solo lectura que muestra qué tags, variables y ajustes están consumiendo, antes de tocar nada.',
           ['Consulta · sin cambios', 'Tokens: Bajo'], 63, ('4', 'preguntas'),
           'Necesito un diagnóstico de consumo del asistente de TKVA. Es solo de lectura: no cambies nada.\n1) Listame todos los Smart Tags que tienen prompt de asignación por IA, con cuántos contactos tiene cada uno.\n2) Listame todas las variables que tienen prompt (carga automática) y cuáles son de carga manual.\n3) Decime si está activada la extracción de datos offline y si están activados los mensajes humanizados.\n4) Decime cuánto saldo hay hoy y qué recargas se hicieron en septiembre y octubre, con fecha y monto.\nDevolvelo como cuatro listas cortas.', 'var(--good)', 'start')
      + '</div>')
# META
oct_env = D['oct_env']; ad_sh = D['oct_ad'] / D['oct_n']
low, mid, high = 2000, 2700, 3500
def cobr(t, free_share): return max(0, round(t * (1 - free_share)) - 1000)
sc = [('Ritmo bajo, 32% de las charlas desde anuncios', low, cobr(low, ad_sh)), ('Ritmo medio, 32% desde anuncios', mid, cobr(mid, ad_sh)), ('Ritmo alto, sin ventana de 72 h', high, cobr(high, 0))]
sc_rows = [[a, num(t), num(c), f'ARS {num(c * ARS_S)}'] for a, t, c in sc]
api_qr = ('<div class="vsplit"><div class="vs" style="--vsc:var(--vio)"><span class="k">API oficial · lo que tiene TKVA hoy</span><b class="t">Para operar a escala</b>'
          '<p>Se conecta mediante Meta y requiere portfolio comercial y medio de pago. Es más estable. Permite plantillas aprobadas para escribir después de 24 h, campañas masivas (en Enterprise) y Meta Forms. '
          'Los seguimientos fuera de la ventana de 24 h necesitan plantilla. Con coexistencia se puede seguir usando WhatsApp Business en el celular; con API pura, el número queda solo en la API.</p>'
          f'<div class="okf" style="margin-top:9px"><span class="qq" style="--c:var(--vio)">Meta cobra por mensaje desde el 1/10</span><span class="qq" style="--c:var(--vio)">1.000 respuestas gratis por número</span></div></div>'
          '<div class="vs" style="--vsc:var(--ink3)"><span class="k">QR · alternativa</span><b class="t">Para atención uno a uno</b>'
          '<p>Se conecta escaneando un código y depende de una sesión vinculada, que puede desconectarse. Permite asistente, Smart Tags, variables y seguimientos, y responder después de 24 h sin plantilla. '
          'No permite campañas masivas, plantillas oficiales ni Meta Forms. No tiene cargo de Meta por mensaje.</p>'
          f'<div class="okf" style="margin-top:9px"><span class="qq" style="--c:var(--ink3)">Sin costo de Meta</span><span class="qq" style="--c:var(--ink3)">Sin primer mensaje a formularios</span></div></div></div>')
mt = ('<div class="stab st-meta">' + api_qr + '<div class="g4">'
      + kpi('wa', 'grn', 'pro', 'Conexión de la línea de ventas', 'API oficial', None, '', None, 'confirmado por AUREA', None, 'Ninguna de las dos modalidades responde en grupos; las dos mantienen la atención uno a uno.')
      + kpi('chat', 'blu', 'pro', 'Mensajes enviados · octubre al 14', num(oct_env), None, '', None, f'a los {D["oct_n"]} contactos que entraron en octubre', 'Más los mensajes a contactos de meses anteriores, que el export no separa por fecha.')
      + kpi('target', 'pnk', 'pro', 'Puerta de entrada · Click to WhatsApp', pct(D['oct_ad'], D['oct_n']), None, '', None, 'de los contactos de octubre llega con ID de anuncio', None, 'La ventana de 72 h de un anuncio no se cobra si se responde dentro de las 24 h y el contacto escribe desde el celular.')
      + kpi('sigma', 'amb', 'calc', 'Costo de Meta estimado', 'ARS 14 mil a 94 mil', 'por mes', 'd-flat', None, 'escenario, no factura', None, 'El dato real sale de la factura de Meta de octubre.')
      + '</div>' + table(['Tipo de mensaje', 'Costo en Argentina', 'Cuándo aplica'], [
          ['Servicio (respuestas del agente o de Vanesa por API)', 'ARS 37,68', 'Desde el 1/10/2026 se cobra, con 1.000 mensajes gratis por mes por número'],
          ['Utilidad', 'ARS 37,68', 'Recordatorios, confirmaciones y el primer mensaje a un lead de formulario, con plantilla'],
          ['Marketing', 'ARS 89,56', 'Reactivaciones y ofertas con plantilla'],
          ['Click to WhatsApp', 'Gratis 72 h', 'Corre desde la respuesta; hay que responder en 24 h y el contacto tiene que escribir desde el celular']], 700, txt=True)
      + '<div class="mt">' + table(['Escenario · [CÁLCULO]', 'Mensajes enviados por mes', 'Mensajes cobrables', 'Costo de Meta aprox.'], sc_rows, 700) + '</div>'
      + qbd(f'Sobre {num(low)} a {num(high)} mensajes enviados por mes, menos los 1.000 gratis y la parte que entra por anuncio. Tarifas oficiales de Meta en pesos, sin impuestos. Es un escenario: el export no trae los mensajes por fecha ni por categoría.',
            f'Si los ≈ 220 leads de formulario por mes reciben un primer mensaje con plantilla: ARS {num(220 * ARS_S)} por mes en utilidad o ARS {num(220 * ARS_M)} en marketing. Si la línea B2B también va por API, suma su propio cupo de 1.000 gratis.')
      + sec('Qué hago ahora · META') + legend()
      + acts([A_APIQR.replace('class="i3 av adv"', 'class="i3 av"', 1),
              act('proteger', 'Marketing', [14, 10, 7, 15, 10, 15], f'Click to WhatsApp · {pct(D["oct_ad"], D["oct_n"])} de los contactos de octubre llega desde un anuncio', 'Contactos con ID de anuncio de Meta', f'{D["oct_n"]} contactos de octubre', f'{D["oct_ad"]} con anuncio · la ventana de 72 h baja el costo de Meta', f'{CIT} · cálculo AUREA',
                  'Pasar la pauta de formulario y remarketing a Click to WhatsApp y responder dentro de las 24 h para usar la ventana de 72 h sin costo.',
                  'Administrador de anuncios · objetivo de mensajes', 'Más charlas dentro de la ventana gratuita y menos plantillas pagas.', '% de contactos con anuncio y factura de Meta de noviembre.', 'calificación por anuncio.',
                  'El ID de anuncio está en el 30% de las conversaciones procesadas; el ahorro en Meta es cálculo, no factura.', 'Señal'),
              act('medir', 'AUREA', [8, 0, 0, 10, 10, 15], 'Factura de Meta de octubre · el costo real del canal todavía no se ve', 'Mensajes facturados por categoría', 'línea de ventas por API', 'sin dato real: escenario de ARS 14 mil a 94 mil', 'Cálculo AUREA',
                  'Bajar la factura de Meta de octubre (o el panel de WhatsApp Manager) con los mensajes por categoría y cargarla en el próximo tablero.',
                  'Meta Business Suite › Facturación · WhatsApp Manager › Estadísticas', 'Reemplazar el escenario por el costo real.', 'Factura de octubre contra el escenario.', 'que el costo se lea por línea (ventas y B2B).',
                  'Dato modelado: Fuente 0 y techo 54.', 'Modelado')], 3)
      + '</div>')
tok = ('<section class="panel p-tokens">' + head('Consumo variable CRM', 'Dos costos variables:', 'Tokens IA por un lado, META por el otro.',
                                                'Cuánto consume el agente, en qué se va cada dólar, qué costó quedarse sin procesar y cuánto empieza a cobrar Meta desde el 1/10. Prometheo cobra la inteligencia; Meta cobra el canal: los dos costos no se suman.',
                                                'Consumo y reparto: panel "Entendé tu consumo" de Prometheo (agosto a octubre al 14). Mensajes: export de contactos al 14/10. Tarifas de Meta: rate card oficial en pesos, Argentina, sin impuestos. El abono de Prometheo es fijo y no está en esta pestaña.')
       + vsplit + cv_tabs + ia + mt
       + yeq('El costo no está en la conversación: está en quedarse sin procesar. Primero, que el agente no vuelva a cortarse; después, que no se gaste en lo que no se usa. En Meta, mientras la mayoría de las charlas llegue desde un anuncio y dentro de las 72 h, el cupo de 1.000 cubre buena parte.')
       + '</section>')
PANELS.append(tok)

# ================= 12 · AUDIENCIAS =================
AU = D['aud']
aud = ('<section class="panel p-audiencias">' + head('Audiencias · listas que salen del CRM', 'Cada tag bien cargado', 'es una audiencia.',
                                                    'Listas que se pueden armar hoy desde Prometheo, para pauta (públicos personalizados) o para el seguimiento de Vanesa.',
                                                    f'Conteos al 14/10. Coincidencia con Meta por teléfono: {num(AU["tel"])} contactos tienen teléfono ({pct(AU["tel"], D["total"])}) y solo {AU["mail"]} tienen email.')
       + table(['Audiencia', 'Contactos', 'Cómo se arma en Prometheo', 'Dueño'], [
           ['Hot leads <span class="qcw">la señal que conviene que aprenda Meta</span>', HOT, 'Tag "Hot Lead" (no existe hoy: Posible mejora 2)', 'MKT'],
           ['Calificados · criterio EDFAN <span class="qcw">semilla de públicos similares</span>', RNG, f'Tag "Calificado" (hoy {D["tagcal"]}: Posible mejora 3)', 'MKT'],
           ['Inversores <span class="qcw">Green Line y Maker Núñez</span>', AU['inv'], 'Destino u objetivo = inversión · tag "Inversor"', 'MKT'],
           ['Vivienda <span class="qcw">Maker Crespo y Maker Núñez</span>', AU['viv'], 'Destino = vivienda · tag "Consumidor final"', 'MKT'],
           ['Hot leads sin próximo paso <span class="qcw">seguimiento de Vanesa</span>', HOT_SIN, 'Hot lead sin tags de seguimiento', 'VENTAS'],
           ['Leads de formulario LT <span class="qcw">remarketing por Click to WhatsApp</span>', LT['n'], 'Canal Origen = LT', 'MKT'],
           ['Exclusión: no-demanda <span class="qcw">sacar de la pauta</span>', D['nodem'], 'Inmobiliaria, Proveedor, No Fit, Cliente ya compró, Equipo', 'MKT']], 760, txt=True)
       + qbd(f'La exclusión importa: {pct(D["nodem"], D["total"])} de los contactos no son demanda. No conviene usarlos como base de públicos similares.',
             'La señal a Meta (Conversions API, evento de lead calificado) solo vale si el tag está bien cargado: hoy el tag "Calificado" y el criterio coinciden en 18 contactos.')
       + yeq(f'Con {CAL_A} calificados no se llega a las 1.000 coincidencias de un público similar propio. Hoy sirven como público personalizado; la no-demanda va siempre como exclusión.')
       + '</section>')
PANELS.append(aud)

# ================= 13 · INTEGRACIONES =================
CAL_ROWS = [['Agente sin procesar · cero cortes', 'Corregir · AUREA', 80, 'Basada en datos', 'Hecho · 100', 'pendiente (30/11)'],
            ['Hot leads sin próximo paso', 'Activar · Ventas', 66, 'Informada', 'Señal · 79', 'pendiente (31/10)'],
            ['Formularios de LT', 'Decidir · Dirección', 69, 'Informada', 'Hecho · 100', 'pendiente (30/11)'],
            ['Calificado por regla', 'Corregir · AUREA', 77, 'Informada', 'Señal · 79', 'pendiente (30/11)'],
            ['Capacidad de pago', 'Corregir · AUREA', 80, 'Basada en datos', 'Hecho · 100', 'pendiente (30/11)'],
            ['API o QR', 'Decidir · Dirección', 38, 'Hipótesis', 'Modelado · 54', 'pendiente (factura oct)']]
integ = ('<section class="panel p-integraciones">' + head('Integraciones · de dónde sale este tablero', 'Todas las fuentes,', 'en tres sectores.',
                                                         'Qué alimenta el tablero, qué falta conectar y cuándo se actualizó cada fuente.',
                                                         'Fuentes por sector (CRM, marketing y otras), estado y última actualización. Los faltantes por tipo están en Venta · CRM › Calidad del dato.')
         + mclegend()
         + cnsec('crm', 'CRM', 'Donde vive la consulta, la calificación y el embudo', [
             cn('bot', 'linear-gradient(135deg,#7C5CBF,#5B8FD9)', 'Prometheo', True, 'chat', 'export 14/10 · 1.470 contactos', f'Consultas, tags y variables. Del 29/08 al 15/09 el agente no procesó: {G["sinproc"]} conversaciones sin datos.'),
             cn('wa', '#25D366', 'WhatsApp · línea de ventas', True, 'phone', 'API oficial · con agente', 'Por donde entra casi todo. Desde el 1/10 Meta cobra cada respuesta por API, con 1.000 gratis por mes.'),
             cn('wa', '#1E6B3A', 'WhatsApp · línea B2B', True, 'checkc', 'mejora continua aplicada · sin agente', 'Línea aparte para inmobiliarias y proveedores. No consume saldo de IA.', extra=f'<div style="margin-top:6px">{mc("start")}</div>'),
             cn('ig', 'linear-gradient(45deg,#F58529,#DD2A7B,#8134AF)', 'Instagram · mensajes directos', 'Sin datos desde el 30/07', 'ig', '163 conversaciones del 22 al 30/07', 'Desde el 30/07 no entra ninguna conversación por Instagram. Confirmar si se desconectó o se apagó a propósito.', 'Conectar')])
         + cnsec('mega', 'Marketing y canales de marketing', 'Meta, formularios y landing', [
             cn('meta', '#1877F2', 'Meta · anuncios en Prometheo', True, 'anun', 'ID de anuncio por contacto', f'Qué anuncio trajo cada contacto: {D["con_ad"]} de {num(D["total"])}. Es la mitad del cruce.'),
             cn('meta', '#1877F2', 'Meta Ads · gasto', False, 'dollar', 'falta el export', 'Sin gasto no hay CPC, CPE ni CPV (los costos del reporte de Vanesa). Conexión nativa: desarrollo.', 'Conectar', extra=f'<div style="margin-top:6px">{mc("pro")}</div>'),
             cn('inb', '#E8590C', 'Formularios LT · Go High Level', False, 'doc', '≈ 220 leads por mes', 'El lead de formulario no manda un mensaje y espera a que Vanesa lo tome a mano. Vía A: integración GHL → Prometheo (Pro). Vías B y C: primer mensaje desde GHL o carga del contacto con origen (Start).', 'Conectar', extra=f'<div style="margin-top:6px">{mc("pro")} {mc("start")}</div>'),
             cn('fb', '#1877F2', 'Meta Forms · formularios instantáneos', 'Disponible · sin configurar', 'checkc', 'Enterprise + API oficial: TKVA cumple', 'Prometheo crea el contacto y manda una plantilla aprobada por WhatsApp. Cubre los formularios de Facebook e Instagram, no los de la landing. La plantilla la cobra Meta.', 'Conectar', extra=f'<div style="margin-top:6px">{mc("pro")}</div>')])
         + cnsec('plug', 'Otras integraciones', 'Catálogo, cierre y costos', [
             cn('building', '#0F6E6E', 'Tokko', True, 'building', 'vía Prometheo', 'Barrios, propiedades y fichas llegan como campos del contacto. El catálogo (stock, precios) no viene en el export.'),
             cn('pie', '#7C5CBF', 'Panel de consumo de IA', True, 'pie', 'agosto a octubre al 14 (capturas)', 'Consumo por mes y reparto del gasto de IA.'),
             cn('ledger', '#667085', 'Reporte semanal y mensual de Vanesa', 'Manual', 'doc', 'reporte del 24/09 al 07/10', 'Contactos, estados, origen, visitas, ventas e inversión. Desde este tablero se arma solo en lo que el CRM registra.'),
             cn('lock', '#667085', 'Registro de ventas', False, 'lock', '2 ventas nuevas con tag', '"Convertido" mezcla ventas con postventa e inmobiliarias. Sin un tag de venta limpio no hay CPV.', 'Conectar'),
             cn('doc', '#667085', 'Factura de Meta · WhatsApp', False, 'doc', 'desde el 1/10', 'Mensajes reales por categoría. Sin ella, el costo de Meta es un escenario.', 'Conectar'),
             cn('mega', '#667085', 'Email y WhatsApp masivo', 'Sin campañas en el período', 'mega', 'estado vacío', 'No hubo campañas de email ni difusiones de WhatsApp: esas métricas aparecen cuando las haya.')])
         + '<div class="qbe mt"><div class="qbj">' + I('alert') + 'Faltantes declarados</div><ul class="i3-b">'
         f'<li><b>Agente sin procesar del 29/08 al 15/09.</b> {G["sinproc"]} conversaciones sin resumen, tags ni variables. Todo número que depende de la IA corre sobre las {B} conversaciones de compra procesadas.</li>'
         '<li><b>Instagram sin datos desde el 30/07.</b> Los que llegan por Instagram y escriben por WhatsApp quedan como "Instagram" declarado, sin el mensaje directo.</li>'
         '<li><b>Formularios de LT fuera del CRM.</b> El reporte manual del 01/10 al 07/10 cuenta 54 contactos de LT; Prometheo registra 25.</li>'
         '<li><b>Gasto de Meta y registro de ventas.</b> Sin ellos no hay CPC, CPE ni CPV.</li>'
         '<li><b>Línea base.</b> TKVA no tiene medición de antes del agente (discovery B10): "¿Cómo venimos?" compara contra el mes anterior.</li></ul></div>'
         + sec('Registro de calibración · rúbrica de score versión 1, sin calibrar')
         + table(['Card', 'Verbo · dueño', 'Score', 'Banda', 'Techo aplicado', 'Resultado al cierre'], CAL_ROWS, 760)
         + qbd('Al cerrar cada período se registra si el efecto se cumplió. Con 20 cards cerradas se revisan los pesos de la rúbrica.')
         + sec('Glosario') + table(['Término', 'Qué significa en este tablero'], [
             ['Consulta', 'Contacto nuevo en Prometheo por fecha de ingreso. Es el conteo maestro.'],
             ['Consulta de compra', 'Consulta sin tags de inmobiliaria, proveedor, postventa, equipo ni No Fit.'],
             ['Conversó', 'El lead mandó 2 o más mensajes.'],
             ['Procesada por la IA', 'Tiene Resumen por IA. Sin resumen, el agente no cargó tags ni variables.'],
             ['Calificado (criterio EDFAN)', 'Proyecto o zona que TKVA comercializa, una tipología que existe y al menos 2 de: intención de compra, finalidad, presupuesto o forma de pago, estado de obra compatible. Rango estricto a amplio. Propuesta a validar con TKVA.'],
             ['Hot lead (criterio EDFAN)', 'Una señal alcanza: unidad concreta, compra ya o pronto (90 días), contado o anticipo. El pedido de visita es una etapa aparte.'],
             ['Entrevista', 'Visita realizada (tag "Visita Realizada"), como en el reporte de Vanesa.'],
             ['MC · Start / MC · Pro', 'Start: estabilidad, estrategia y ajustes dentro del plan de Mejora Continua. Pro: escalabilidad, integración nativa entre plataformas, es desarrollo.'],
             ['Índice data-driven', 'Cuánto de cada acción se apoya en datos verificables (0 a 100%). Rúbrica v1, sin calibrar.'],
             ['p.p.', 'Puntos porcentuales: diferencia entre dos porcentajes.']], 700, txt=True)
         + yeq('Faltan cuatro cosas para el tablero completo: el gasto de Meta, un tag de venta limpio, los formularios de LT dentro del CRM e Instagram reconectado. Las dos primeras habilitan los costos del reporte de Vanesa.')
         + '</section>')
PANELS.append(integ)
