"""Meta en Prometheo, Audiencias e Integraciones."""
from icons import ic
from comp import (fmt, pct, money, src, lvl, own, chip, delta, sec_head, eyebrow, ghdr, banner, kpi, bar, bars,
                  vcard, table, bsc_adv, minibar, mincard, ul, i3, kv, cmpbar, fsteps)
import data as D


def _act(icon, text, go):
    return f'<div class="act"><div class="a-ic">{ic(icon)}</div><div class="a-t">{text}<span class="go">{ic("eye")}Se ve en: {go}</span></div></div>'


def metaprom():
    M = D.META
    kp = '<div class="g4">' + "".join([
        kpi("Consultas de anuncios a WhatsApp", fmt(M["cons"]), "", "Las únicas que Meta puede optimizar con el CRM", "meta", "blu", "pro"),
        kpi("Califican hoy", f'{M["pcal"]}%', "", f'{M["calif"]} de {fmt(M["cons"])} · Meta no lo sabe', "checkc", "", "pro"),
        kpi("Señales que el tablero detectó", "9", "", "3 por integración · abajo, cada una", "bulb", "pnk", "calc"),
        kpi("Contactos para excluir de la pauta", "700", "", "Distribuidores que ya compran", "x", "amb", "erp"),
    ]) + "</div>"
    grid = f'''<div class="metagrid">
<div class="mt3"><div class="mt3-hd"><div class="mt3-ic">{ic("form")}</div>{own("mkt", "MKT")}</div><h3>Lead Forms</h3>
<p class="what">La consulta entra al CRM con el anuncio de origen y las respuestas del formulario ya cargadas como tags.</p>
<div class="seen">{ic("bulb")}Lo que vio el tablero de PAVIR</div>
<div class="acts">
{_act("alert", f'<b>{pct(M["cons"] - M["ident"], M["cons"])} de cada 100</b> consultas de pauta llegan sin línea ni zona y el agente pregunta de cero. Un form con 3 campos (<b>tipo de contacto, línea y zona</b>) las trae calificadas.', "Venta · CRM › embudo")}
{_act("store", f'<b>{M["b2b"]} comercios</b> entraron por anuncios pensados para el consumidor. La pregunta «¿Sos comercio o consumidor?» los manda al embudo B2B desde el primer mensaje.', "Venta · CRM › B2B")}
{_act("pin", '<b>230 calificadas</b> no se derivaron porque faltaba la zona. En el form, la zona es obligatoria.', "Cómo mejorar el CRM")}
</div>
<div class="mt3-f">Prioridad <span class="lvl l-senal">Media</span> · se mide en <b>% que llega con línea y zona</b></div></div>

<div class="mt3"><div class="mt3-hd"><div class="mt3-ic">{ic("pulse")}</div>{own("mkt", "MKT")}</div><h3>Ads · CAPI</h3>
<p class="what">Prometheo le avisa a Meta qué consulta calificó, servidor a servidor, para que la pauta aprenda del comprador y no del mensaje.</p>
<div class="seen">{ic("bulb")}Lo que vio el tablero de PAVIR</div>
<div class="acts">
{_act("target", f'Meta optimiza hacia la <b>conversación</b>: {fmt(M["cons"])} en el mes y solo {M["pcal"]} de cada 100 califican. Mapear el tag <code>calificada</code> al evento de Meta le enseña a buscar a los {M["calif"]}.', "Insights › por anuncio")}
{_act("conj", 'El conjunto <b>Broad</b> trae 300 consultas y califica 19%; <b>Retargeting</b>, 59%. Hoy Meta los ve iguales: con el evento, aprende cuál de los dos perfiles compra.', "Insights › por conjunto")}
{_act("doc", f'Hay <b>{M["ped"]} compras</b> dichas en la conversación y 0 marcadas. Con el tag de pedido, el evento <b>Compra</b> cierra el círculo hasta la venta.', "Cómo mejorar el CRM")}
</div>
<div class="mt3-f">Prioridad <span class="lvl l-hecho">Alta</span> · se mide en <b>costo por consulta calificada</b> (hoy ${fmt(M["ccal"])})</div></div>

<div class="mt3"><div class="mt3-hd"><div class="mt3-ic">{ic("users")}</div>{own("mkt", "MKT")}</div><h3>Audiencias</h3>
<p class="what">Públicos personalizados y públicos similares (Lookalike) armados con los tags del CRM.</p>
<div class="seen">{ic("bulb")}Lo que vio el tablero de PAVIR</div>
<div class="acts">
{_act("seed", '<b>1.240 contactos B2B</b> (padrón + feria BATEV + scraping) superan las 1.000 coincidencias: alcanza para un <b>Lookalike de distribuidores</b> en las 7 provincias sin red.', "Distribuidores · Audiencias")}
{_act("refresh", '<b>640 consultaron una línea y no se derivaron</b>. Público personalizado para volver a mostrarles esa misma línea.', "Audiencias")}
{_act("x", '<b>700 distribuidores ya compran</b>. Excluir el tag <code>ya_distribuidor</code> de toda campaña de captación evita pagar dos veces.', "Distribuidores")}
</div>
<div class="mt3-f">Prioridad <span class="lvl l-hecho">Alta</span> · se mide en <b>altas de distribuidores nuevos</b></div></div>
</div>'''
    flow = fsteps([dict(num="01", pt="100%", label="Clic a WhatsApp", val=f'<b>{fmt(M["cons"])}</b> consultas', w=100, **{"pass": "base"}),
                   dict(num="02", pt=f'{pct(M["resp"], M["cons"])}%', label="Respondieron", val=f'<b>{fmt(M["resp"])}</b>', w=pct(M["resp"], M["cons"]), **{"pass": f'pasa {pct(M["resp"], M["cons"])}%'}),
                   dict(num="03", pt=f'{M["pcal"]}%', label="Calificadas", val=f'<b>{M["calif"]}</b> · evento sugerido', w=M["pcal"], **{"pass": f'pasa {pct(M["calif"], M["resp"])}%'}),
                   dict(num="04", pt=f'{pct(M["deriv"], M["cons"])}%', label="Derivadas", val=f'<b>{M["deriv"]}</b>', w=pct(M["deriv"], M["cons"]), **{"pass": f'pasa {pct(M["deriv"], M["calif"])}%'}),
                   dict(num="05", pt=f'{pct(M["ped"], M["cons"])}%', label="Compra", val=f'<b>{M["ped"]}</b> por evidencia · 0 con tag', w=3, cls="dim", **{"pass": "hoy sin tag"})])
    mapa = table([f'Smart Tag {src("pro")}', "Consultas del mes", f'Evento de Meta {src("meta")}', "Para qué le sirve a la pauta"], [
        ["<code>consulta_nueva</code>", fmt(M["cons"]), "Conversación iniciada", "Lo que Meta ya optimiza hoy: volumen"],
        ["<code>calificada</code>", str(M["calif"]), "<b>Lead calificado ★</b>", "Aprender quién dice producto, zona y cantidad"],
        ["<code>derivado_distribuidor</code>", str(M["deriv"]), "Cliente potencial", "Aprender quién llega a un distribuidor"],
        ["<code>comercio</code>", str(M["b2b"]), "Evento personalizado B2B", "Separar la captación de red del consumidor"],
        ["<code>pedido_reportado</code>", "0 · hoy sin uso", "Compra", "Cerrar el círculo hasta la venta"]], 720)
    return f'''<section class="panel p-metaprom">
{sec_head("Meta en Prometheo · WhatsApp API", "El puente <em>con Meta.</em>",
          ("Tres integraciones de Meta que ya existen en Prometheo. Debajo de cada una, <b>lo que el tablero de PAVIR muestra hoy</b> y que indica que conviene usarla. Solo cuentan las consultas que entraron por <b>anuncios de clic a WhatsApp</b>.", "Lead Forms, <b>CAPI</b> (Conversions API: eventos del CRM enviados a Meta servidor a servidor) y Audiencias. Cada señal enlaza con la pestaña donde se detectó; ninguna se activa sola: el tablero muestra, no ejecuta."))}
{kp}
<div class="mt">{grid}</div>
{eyebrow("Del clic al distribuidor · lo que Meta podría aprender")}
<div class="card pad">{flow}
<div class="note">{bsc_adv("Hoy Meta aprende del paso 01. Con CAPI aprende del 03 y busca más gente parecida a la que califica.",
    "Evento recomendado para optimizar: <b>calificada</b> (655 al mes, volumen suficiente para el aprendizaje). <b>Compra</b> queda para cuando el tag de pedido tenga uso.")}</div></div>
<div class="adv">{eyebrow("Mapeo de Smart Tags a eventos de Meta · modo avanzado")}{mapa}
<div class="mt">{banner("info", "info", "La integración prepara el evento y la audiencia; <b>la optimización la hace Meta</b>. Lo que cambia es de qué aprende: del mensaje (consumidor final mirando precios) o de la consulta calificada.")}</div></div>
</section>'''


def _au(icon, bg, name, badge, badge_style, owners, sub, n, unit, items, open_=False):
    o = " open" if open_ else ""
    return (f'<details class="aucard"{o}><summary class="au-s"><div class="au-ic" style="background:{bg}">{ic(icon)}</div><div class="au-t"><div class="au-n">{name} '
            f'<span class="au-badge" style="{badge_style}">{badge}</span> {owners}</div><div class="au-ss">{sub}</div></div><div class="au-c">{n}<span>{unit}</span></div>'
            f'<span class="chev">{ic("chev")}</span></summary><div class="au-d"><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div></details>')


def audiencias():
    cust = "background:var(--vio-soft);color:var(--vio)"
    lal = "background:var(--good-bg);color:var(--good-ink)"
    excl = "background:var(--crit-bg);color:var(--crit-ink)"
    meter = lambda n: f'<div class="meter"><i style="width:{min(n / 1500 * 100, 100):.0f}%;background:{"var(--good)" if n >= 1000 else "var(--warn)"}"></i><span class="th" style="left:66.6%"></span></div>'
    return f'''<section class="panel p-audiencias">
{sec_head("Audiencias · listas para la pauta", "Audiencias, <em>listas para exportar.</em>",
          ("Las listas salen de los tags del CRM y se sincronizan con Meta. Un <b>público personalizado</b> funciona con cualquier tamaño. Un <b>público similar</b> necesita al menos <b>1.000 coincidencias</b>. La más valiosa para PAVIR: el público similar a sus <b>distribuidores</b>.", "<b>Custom Audience</b> (público personalizado): remarketing, exclusión y segmentación, sin mínimo. <b>Lookalike</b> (público similar): Meta lo habilita desde 1.000 coincidencias reales (match rate), no contactos cargados. Cada lista declara su tag de origen."))}
<div class="g4">{kpi("Públicos personalizados", "4", "", "3 para mostrar · 1 para excluir", "users", "", "pro")}{kpi("Habilitan público similar", "3", "", "superan las 1.000 coincidencias", "seed", "grn", "calc")}
{kpi("Semilla B2B", "1.240", "", "padrón 700 + feria 320 + scraping 220", "store", "blu", "calc")}{kpi("A excluir de la captación", "700", "", "ya son distribuidores", "x", "amb", "erp")}</div>
{eyebrow("Públicos personalizados · cualquier tamaño")}
{_au("refresh", "var(--grad)", "Consultó y no se derivó", "Personalizado", cust, own("mkt", "MKT") + " " + own("ven", "VENTAS"), "Volver a mostrar la línea que preguntó", "640", "consultas · 90 días",
     ["Tags: <code>consulta_nueva</code> + línea, sin <code>derivado_distribuidor</code>", "Marketing: anuncio con el producto que preguntó · Ventas: nuevo contacto del agente", "Sirve aunque sea menor a 1.000"], True)}
{_au("bolt", "var(--grad)", "Interés en pivotantes", "Personalizado", cust, own("mkt", "MKT"), "Por línea de producto · ticket alto", "290", "consultas",
     ["Tags: <code>calificada</code> + <code>pivotante</code>", "Anuncio con el exhibidor y la terminación"])}
{_au("doc", "var(--grad)", "Pidió cotización y no compró", "Personalizado", cust, own("mkt", "MKT") + " " + own("ven", "VENTAS"), "Objeción de precio o de terminación", "410", "consultas",
     ["Tags: <code>pidio_cotizacion</code> sin <code>pedido_reportado</code>", "Marketing: anuncio de durabilidad y terminación · Ventas: seguir con el distribuidor de la zona"])}
{_au("x", "var(--ink3)", "Ya es distribuidor", "Exclusión", excl, own("mkt", "MKT"), "No pagar por alcanzar a quien ya compra", "700", "clientes",
     ["Tag: <code>ya_distribuidor</code>", "Acción: <b>excluir</b> de toda campaña de captación B2B", "Sin exclusión, el público similar se parece a la cartera propia y la vuelve a traer"])}
{eyebrow("Semillas de público similar (Lookalike) · requieren 1.000 coincidencias")}
{_au("seed", "var(--good)", "Distribuidores · semilla B2B", "Habilita similar", lal, own("mkt", "MKT") + " " + own("ven", "VENTAS"), "Buscar puntos de venta parecidos a los mejores", "1.240", "contactos",
     ["Fuentes: padrón de Producí (700) + feria BATEV (320) + scraping de corralones (220)", "Similar 1% para captar distribuidores en las <b>7 provincias sin red activa</b>", "El padrón trae teléfono: coincidencia alta en Meta"] , True)}
{_au("checkc", "var(--good)", "Consumidor final calificado", "Habilita similar", lal, own("mkt", "MKT"), "Semilla de quien dice producto, zona y cantidad", "2.870", "consultas",
     ["Tag: <code>calificada</code> (todas las líneas, 90 días)", "La mejor semilla para bajar el costo por consulta útil"])}
{_au("star", "var(--good)", "Interesados en la línea premium", "Habilita similar", lal, own("mkt", "MKT"), "Pivotantes, PAVIR premium y cerradura full", "1.060", "consultas",
     ["Tags: <code>pivotante</code> · <code>pavir_premium</code> · <code>cerradura_full</code> (6 meses)", "Sola, <code>pivotante</code> daba 290: agrupar la línea premium es lo que la habilita"])}
<div class="adv">{eyebrow("Requisitos y coincidencia · modo avanzado")}
<div class="g3">
{vcard("Cuánto falta para habilitar similar", "".join(f'<div style="margin-bottom:10px"><div style="display:flex;justify-content:space-between;font-size:12px"><span>{n}</span><b>{fmt(v)}</b></div>{meter(v)}</div>' for n, v in [("Distribuidores B2B", 1240), ("Línea premium", 1060), ("Pivotantes solo", 290), ("Pidió cotización", 410)]) + '<div class="note">La línea negra marca las 1.000 coincidencias.</div>', "seed")}
{vcard("Cómo sube la coincidencia", kv([("~90%", "con teléfono"), ("~70%", "con email"), ("refuerzo", "nombre y apellido")]) + '<div class="note">Lookalike se habilita con 1.000 coincidencias <b>reales</b> (personas que Meta reconoce), no con contactos cargados.</div>', "phone")}
{vcard("Origen de cada lista", bar("Padrón de Producí", "700", 100, "", "var(--src-erp)") + bar("Feria BATEV", "320", 46, "", "var(--pnk)") + bar("Scraping", "220", 31, "", "var(--ink4)") + bar("Conversaciones (Prometheo)", "2.870", 100, "", "var(--src-pro)"), "list")}
</div></div>
</section>'''


def _intg(icon, color, name, desc, status, scls, extra="", live=True):
    return (f'<div class="intg {"live" if live else "avail"}"><span class="stt {scls}">{status}</span><div class="ci">{ic(icon, style=f"color:{color}")}</div>'
            f'<h4>{name}</h4><p>{desc}</p>{extra}</div>')


def integraciones():
    bases = f'<div class="bases"><span class="chip">{ic("ledger")}Padrón</span><span class="chip">{ic("badge")}Ferias</span><span class="chip">{ic("globe")}Scraping</span></div>'
    bases_wpp = f'<div class="bases"><span class="chip">{ic("ledger")}Padrón</span><span class="chip">{ic("badge")}Ferias</span></div>'
    srcs = [
        ("chat", "var(--src-pro)", "Prometheo · export", "Consultas, tags, variables, moderador y conversación. Define cuántas consultas hubo.", D.ACT, "Mensual"),
        ("ledger", "var(--src-erp)", "Producí · export de gestión", "Padrón, cuenta corriente, pedidos y ventas. Se carga como archivo: no es una integración.", D.ACT, "Mensual"),
        ("meta", "var(--src-meta)", "Meta Ads · export", "Inversión, alcance, impresiones y clics por anuncio y día.", D.ACT, "Manual"),
        ("mail", "var(--src-mail)", "Plataforma de email", "Envíos, entregas, aperturas, clics, rebotes y bajas.", "28 sep 2026", "Por campaña"),
        ("wa", "var(--src-wpp)", "WhatsApp Marketing (Prometheo)", "Enviados, entregados, leídos, rechazos, tier y calidad del número.", "29 sep 2026", "Por campaña"),
        ("google", "var(--src-goog)", "Google Ads", "Cuenta integrada, sin inversión. Los números de su pestaña son proyección.", "—", "Pausado"),
    ]
    rows = "".join(f'<div class="srcrow"><div class="nm">{ic(i, style=f"color:{c}")}{n}</div><div class="ds">{d}</div><div class="dt"><b>{u}</b>{f}</div></div>' for i, c, n, d, u, f in srcs)
    return f'''<section class="panel p-integraciones">
{sec_head("Integraciones · de dónde sale este tablero", "Un tablero, <em>toda la operación comercial.</em>", ("Qué canales ya alimentan el tablero, cuáles faltan y cuándo se actualizó cada fuente.", "Canales integrados vía Prometheo, fuentes por archivo (export) y faltantes de integración declarados. Debajo, la llave con la que se cruza cada fuente."))}
<div class="bridge"><div class="eq"><b>Marketing genera la consulta</b> × <b>Prometheo la califica y la deriva</b></div>
<p>Marketing ve hasta el clic. Prometheo ve del clic a la derivación y al seguimiento. El cruce por <b>ID de anuncio</b> es lo que une las dos mitades: cada peso de pauta se juzga por la consulta que trajo, no por el clic.</p></div>
<div class="g4">{kpi("Canales integrados", "6", "", "Prometheo, Instagram, Meta, Google, Email y WhatsApp", "plug", "grn", "calc")}{kpi("Pendientes", "3", "", "Facebook, LinkedIn y estrategia personalizada", "plus", "", "calc")}
{kpi("Fuentes por archivo", "1", "", "Producí: export mensual de gestión", "ledger", "amb", "erp")}{kpi("Sin medir todavía", "1", "", "Qué consulta terminó en pedido", "lock", "pnk", "calc")}</div>
{eyebrow("Canales integrados · ya alimentan el tablero")}
<div class="intg-grid intg-on">
{_intg("chat", "var(--src-pro)", "Prometheo · WhatsApp API", f"El agente califica, taggea la línea y deriva con la zona. Es la base del tablero: {fmt(D.CONSULTAS)} consultas al mes.", "Activa", "on")}
{_intg("ig", "var(--pnk)", "Instagram Direct", "Segunda puerta de entrada: 18% de las consultas. Mismo agente y mismo embudo que WhatsApp.", "Activa", "on")}
{_intg("meta", "var(--src-meta)", "Meta Ads", "Pauta atribuida por anuncio. Falta el evento de conversión (CAPI) para que optimice hacia la consulta calificada.", "Activa", "on")}
{_intg("google", "var(--src-goog)", "Google Ads", "Integrado y con pestaña propia, hoy sin inversión. La oportunidad está en la búsqueda de marca.", "Pauta pausada", "pause")}
{_intg("mail", "var(--src-mail)", "Email Marketing", "Campañas a base propia: el agente responde el mail y sigue en Prometheo. Bases: padrón, ferias y scraping.", "Iniciada", "on", bases)}
{_intg("wa", "var(--src-wpp)", "WhatsApp Marketing", "Difusiones con plantilla aprobada desde el CRM. Bases: padrón y ferias (con consentimiento); el scraping no entra al masivo.", "Iniciada", "on", bases_wpp)}
</div>
{eyebrow("Pendientes · lo que suma la próxima etapa")}
<div class="intg-grid">
{_intg("fb", "#1877F2", "Facebook Marketing", "Publicaciones y respuesta a comentarios desde Prometheo. El comentario con intención («¿precio?») entra como consulta.", "Pendiente", "off", live=False)}
{_intg("in", "#0A66C2", "LinkedIn Marketing", "Captación B2B de constructoras, estudios y corralones con varias sucursales: el público que hoy llega por scraping.", "Pendiente", "off", live=False)}
{_intg("spark", "var(--vio)", "Estrategia personalizada de marketing", "Plan por temporada (pico mar-may, valle dic-feb) que combina pauta, ferias, email y WhatsApp sobre los tags del CRM.", "A diseñar", "off", live=False)}
</div>
{eyebrow("¿De dónde sale esto? · fuentes y última actualización")}
<div class="card pad">{rows}</div>
<div class="adv">{eyebrow("Cómo se cruza cada fuente · la llave de unión · modo avanzado")}
{table(["Fuente", "Llave de unión", "Con qué dato de Prometheo", "Cobertura"], [
    ["<b>Meta Ads</b>", "ID de anuncio (<code>ad_id</code>)", "Variable de anuncio de origen", "84% de las consultas de pauta"],
    ["<b>Producí</b>", "Código de cliente y teléfono", "Contacto del distribuidor", "93% del padrón"],
    ["<b>Email</b>", "Identificador de envío en el link", "Conversación iniciada dentro de 72 h", "85% de empalme"],
    ["<b>WhatsApp Marketing</b>", "Misma plataforma", "Respuesta a la plantilla", "100%"],
    ["<b>Pedido ↔ consulta</b>", "Sin llave hoy", "Tag de pedido confirmado (a crear)", "0% · faltante de proceso"]], 760)}</div>
{eyebrow("Orden recomendado · el camino de la próxima etapa")}
<div class="steps">
<div class="stp"><div class="stp-h"><div class="stp-n">1</div><b>Evento de conversión en Meta</b></div><div class="stp-d">Mapear <code>calificada</code> al evento de Meta. La pauta deja de aprender del mensaje y aprende de la consulta que sirve.</div><div class="stp-f">{ic("upr")}<div>Desbloquea: <b>costo por consulta calificada más bajo</b></div></div></div>
<div class="stp"><div class="stp-h"><div class="stp-n">2</div><b>Ferias y scraping al CRM</b></div><div class="stp-d">Cargar BATEV y el scraping con su tag, no en Excel: alimentan las secuencias de email y WhatsApp y la semilla B2B.</div><div class="stp-f">{ic("upr")}<div>Desbloquea: <b>outbound medible y semilla de 1.240</b></div></div></div>
<div class="stp"><div class="stp-h"><div class="stp-n">3</div><b>LinkedIn y Facebook Marketing</b></div><div class="stp-d">Sumar los dos canales pendientes con la misma lógica: la respuesta entra como consulta y se mide en el CRM.</div><div class="stp-f">{ic("upr")}<div>Desbloquea: <b>captación de red en las 7 provincias sin distribuidor</b></div></div></div>
</div>
<div class="mt">{banner("info", "info", "El valor no está en un dato suelto sino en el <b>cruce</b>. Ninguna cifra de este tablero suma dos fuentes: Prometheo define cuántas consultas hubo y el resto explica de dónde vinieron.")}</div>
</section>'''
