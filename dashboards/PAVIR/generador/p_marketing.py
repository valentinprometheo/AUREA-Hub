"""Canales: Meta Ads, Google Ads, Email Marketing y WhatsApp Marketing."""
from icons import ic
from comp import (fmt, pct, money, src, lvl, own, chip, delta, sec_head, eyebrow, ghdr, banner, kpi, bar, bars,
                  vcard, table, bsc_adv, minibar, mincard, ul, i3, kv, cmpbar, fsteps)
import data as D


def _chan_head(name, lead):
    if isinstance(lead, tuple):
        lead = bsc_adv(*lead)
    return (f'<div class="sec-head" style="margin-top:6px"><div class="hbrand" style="margin-bottom:8px"><span class="wm" style="font-size:30px">{name}</span>'
            f'<span class="ic" style="font-size:15px"><b>Canal</b>Marketing</span></div><p class="lead">{lead}</p></div>')


def _iobar(imp_label, locked_imp=False, hint=""):
    lk = '<span class="lk">Pausado</span>' if locked_imp else ""
    return (f'<div class="iobar"><button class="iobtn {"locked" if locked_imp else "primary"}">{ic("outb")}{imp_label}{lk}</button>'
            f'<button class="iobtn">{ic("inb")}Exportar este canal</button><button class="iobtn locked">{ic("lock")}Actualización automática <span class="lk">Próximamente</span></button>'
            f'<span class="iohint">{hint}</span></div>')


def _legend(items):
    return '<div class="srclegend">' + "".join(f'<div class="slg">{src(k)}<span>{t}</span></div>' for k, t in items) + "</div>"


def _steps(rows):
    """Embudo de canal: los dos primeros pasos son de la plataforma; desde el tercero, % sobre consultas."""
    ref = rows[2][1]
    out = []
    for i, (l, v, note) in enumerate(rows):
        if i == 0:
            ps, pt = "base", ""
        else:
            r = v / rows[i - 1][1]
            ps = f"pasa {fmt(100 * r, 1) if r < 0.1 else round(100 * r)}%"
            pt = f"{pct(v, ref)}%" if i >= 2 else ""
        w = 100 if i < 3 else max(100 * v / ref, 2)
        out.append(dict(num=f"0{i + 1}", pt=pt, label=l, val=f"<b>{fmt(v)}</b> {note}", w=w, **{"pass": ps}))
    return fsteps(out)


# =====================================================================
def metaads():
    M = D.META
    funnel = _steps([("Impresiones", M["imp"], "veces que se vio"), ("Clics en el enlace", M["clics"], "a WhatsApp"), ("Consultas", M["cons"], "en Prometheo"),
                     ("Respondieron", M["resp"], "al agente"), ("Calificadas", M["calif"], "producto, zona y cantidad"), ("Derivadas", M["deriv"], "a distribuidor o corredor"),
                     ("Con seguimiento", M["seg"], "fecha acordada"), ("Compra en la charla", M["ped"], "por evidencia")])
    kp = '<div class="g4">' + "".join([
        kpi("Inversión del mes", f'${fmt(M["gasto"])}', delta("+4%", "flat"), "3 campañas · 7 conjuntos · 8 anuncios", "dollar", "", "meta",
            adv=f'<b>CPM</b> (costo cada mil impresiones): ${fmt(M["gasto"] / M["imp"] * 1000)}'),
        kpi("Consultas", fmt(M["cons"]), delta("+9%"), f'{pct(M["cons"], D.CONSULTAS)}% de todas las consultas del mes', "chat", "blu", "pro",
            adv=f'Meta informa {fmt(M["conv_meta"])} conversaciones iniciadas: manda el conteo de Prometheo, no se suman.'),
        kpi("Calificadas", f'{M["calif"]}', delta("+11%"), f'{M["pcal"]}% de las consultas de Meta', "checkc", "grn", "pro",
            adv="<b>Calificada</b>: tipo de contacto + línea + zona + cantidad."),
        kpi("Costo por consulta calificada", f'${fmt(M["ccal"])}', delta("−6%", "good", "down"), "inversión ÷ calificadas · menos es mejor", "sigma", "pnk", "calc",
            adv=f'Costo por consulta (sin calificar): ${fmt(M["gasto"] / M["cons"])}.'),
    ]) + "</div>"
    kp_adv = '<div class="g4 mt adv">' + "".join([
        kpi("CTR", f'{fmt(M["ctr"], 2)}%', "", "clics en el enlace ÷ impresiones", "anun", "", "meta", adv="<b>CTR</b>: click-through rate, tasa de clics."),
        kpi("CPC", f'${fmt(M["cpc"])}', "", "inversión ÷ clics", "dollar", "", "meta", adv="<b>CPC</b>: costo por clic."),
        kpi("Comercios (B2B)", str(M["b2b"]), "", f'{pct(M["b2b"], M["cons"])}% de las consultas · 46 del Lookalike', "store", "blu", "pro"),
        kpi("Pidieron cotización", str(M["cotiz"]), "", f'{pct(M["cotiz"], M["cons"])}% de las consultas', "doc", "pnk", "pro"),
    ]) + "</div>"

    cards = ""
    colors = {"Puertas de acero": "var(--vio)", "Ventanas PVC": "var(--blu)", "Pivotantes": "var(--pnk)"}
    for c, ads in D.CAMPS.items():
        t = D.agg(ads)
        nconj = len({a["conj"] for a in ads})
        cards += f'''<div class="bc" style="--bcac:{colors[c]}"><div class="bc-hd"><span class="cx-ic k-camp">{ic("camp")}</span><div class="bc-nm">{c}</div><span class="obj">Mensajes</span></div>
<div class="bc-o">{ic("conj", style="width:13px;height:13px")}{nconj} conjuntos · {ic("anun", style="width:13px;height:13px")}{len(ads)} anuncios · <b>${fmt(t["gasto"])}</b></div>
<div class="bc-big"><div class="n">{fmt(t["cons"])}</div><div class="u">consultas {src("pro")}</div></div>
<div class="bc-cap"><b>{t["calif"]}</b> calificadas · <b>{t["deriv"]}</b> derivadas</div>
<div class="bc-row"><div><div class="v">{t["pcal"]}%</div><div class="k">califica</div></div><div><div class="v">${fmt(t["ccal"])}</div><div class="k">por calificada</div></div><div><div class="v">{t["seg"]}</div><div class="k">con fecha</div></div></div>
<div class="bc-row adv"><div><div class="v">{pct(t["resp"], t["cons"])}%</div><div class="k">respondió</div></div><div><div class="v">{t["cotiz"]}</div><div class="k">cotización</div></div><div><div class="v">{t["b2b"]}</div><div class="k">comercios</div></div></div>
<div class="bc-row adv"><div><div class="v">{fmt(t["ctr"], 2)}%</div><div class="k">CTR</div></div><div><div class="v">${fmt(t["cpc"])}</div><div class="k">CPC</div></div><div><div class="v">{t["ped"]}</div><div class="k">compra en la charla</div></div></div></div>'''

    rows_b, rows_a = [], []
    for c, ads in D.CAMPS.items():
        rows_b.append(([f'<td class="cj l" colspan="8">{ic("camp", style="width:13px;height:13px;color:#B4610F")} {c} · objetivo Mensajes</td>'], ""))
        rows_a.append(([f'<td class="cj l" colspan="18">{ic("camp", style="width:13px;height:13px;color:#B4610F")} {c} · objetivo Mensajes</td>'], ""))
        for a in ads:
            nm = f'<td class="l"><b>{a["nm"]}</b><span class="anm">{a["code"]}</span></td>'
            cj = f'<td class="l">{a["conj"]}</td>'
            rows_b.append([cj, nm, f'${fmt(a["gasto"])}', str(a["cons"]), str(a["calif"]), f'{a["pcal"]}%{minibar(a["pcal"])}', f'<b>${fmt(a["ccal"])}</b>', str(a["deriv"])])
            rows_a.append([cj, nm, fmt(a["alc"]), fmt(a["imp"]), fmt(a["frec"], 2), f'{fmt(a["ctr"], 1)}%', fmt(a["clics"]), f'${fmt(a["cpc"])}', f'${fmt(a["gasto"])}', str(a["conv_meta"]),
                           str(a["cons"]), str(a["resp"]), str(a["calif"]), f'{a["pcal"]}%', str(a["deriv"]), str(a["b2b"]), str(a["cotiz"]), str(a["seg"])])
    M_ = D.META
    rows_b.append((["<b>Total</b>", "", f'${fmt(M_["gasto"])}', fmt(M_["cons"]), str(M_["calif"]), f'{M_["pcal"]}%', f'${fmt(M_["ccal"])}', str(M_["deriv"])], "tr:tot"))
    rows_a.append((["<b>Total</b>", "", fmt(M_["alc"]), fmt(M_["imp"]), fmt(M_["frec"], 2), f'{fmt(M_["ctr"], 1)}%', fmt(M_["clics"]), f'${fmt(M_["cpc"])}', f'${fmt(M_["gasto"])}', fmt(M_["conv_meta"]),
                    fmt(M_["cons"]), fmt(M_["resp"]), str(M_["calif"]), f'{M_["pcal"]}%', str(M_["deriv"]), str(M_["b2b"]), str(M_["cotiz"]), str(M_["seg"])], "tr:tot"))
    th_b = [f'{ic("conj", style="width:12px;height:12px")} Conjunto', f'{ic("anun", style="width:12px;height:12px")} Anuncio', f'Inversión {src("meta")}', f'Consultas {src("pro")}', f'Calificadas {src("pro")}', f'% califica {src("calc")}', f'Costo por calificada {src("calc")}', f'Derivadas {src("pro")}']
    th_a = ["Conjunto", "Anuncio", f'Alcance {src("meta")}', f'Impres. {src("meta")}', f'Frec. {src("meta")}', f'CTR {src("meta")}', f'Clics {src("meta")}', f'CPC {src("meta")}', f'Inversión {src("meta")}', f'Conv. Meta {src("meta")}',
            f'Consultas {src("pro")}', f'Resp. {src("pro")}', f'Calif. {src("pro")}', f'% Calif. {src("calc")}', f'Deriv. {src("pro")}', f'B2B {src("pro")}', f'Cotiz. {src("pro")}', f'Seguim. {src("pro")}']
    glos = ('<div class="glos"><div><b>Frec.</b>frecuencia: veces que cada persona vio el anuncio</div><div><b>CTR</b>clics ÷ impresiones</div><div><b>CPC</b>costo por clic</div>'
            '<div><b>Conv. Meta</b>conversaciones que informa Meta</div><div><b>Resp.</b>respondió al agente</div><div><b>Calif.</b>calificada: producto, zona y cantidad</div>'
            '<div><b>B2B</b>comercio que quiere revender</div><div><b>Seguim.</b>seguimiento con fecha acordada</div></div>')

    return f'''<section class="panel p-metaads">
{_chan_head("Meta Ads", "Arriba, el <b>cruce Meta × Prometheo</b>: qué pasa con cada clic dentro del CRM (respuesta, calificación, derivación, seguimiento). Abajo, la <b>data del export de Meta</b> con las columnas de Prometheo al lado.")}
{_iobar("Importar export de Meta", hint="Hoy la carga es manual · la automática llega pronto")}
{_legend([("meta", "Inversión, alcance, impresiones, frecuencia, CTR, clics, CPC y conversaciones informadas."), ("pro", "Consultas reales, respuesta, <b>calificación</b>, derivación, comercios, cotización y seguimiento."), ("calc", "% que califica y costo por consulta calificada.")])}
{kp}{kp_adv}
{eyebrow("1 · Del anuncio al seguimiento · Meta ve hasta el clic, Prometheo todo lo que sigue")}
<div class="card pad">{funnel}
<div class="note">{bsc_adv("De cada 100 consultas que trae Meta, 42 califican y 12 llegan a una fecha acordada.",
   f"Meta informa {fmt(M['conv_meta'])} conversaciones; Prometheo registra {fmt(M['cons'])} consultas (la diferencia son chats duplicados o sin mensaje). <b>Manda Prometheo y no se suman.</b>")}</div></div>
{eyebrow("2 · Por campaña · lo que pasó después del clic")}
<div class="bigcamp">{cards}</div>
{eyebrow("3 · Por conjunto y anuncio · export de Meta con Prometheo al lado")}
<div class="bsc">{table(th_b, rows_b, 980)}</div>
<div class="adv">{table(th_a, rows_a, 1700)}</div>
{glos}
<div class="mt">{banner("info", "bulb", "El conjunto <b>Broad</b> trae volumen barato de consumidor final, pero solo 19% califica. <b>Retargeting</b> e <b>Intereses · Construcción</b> traen al que compra: ahí conviene poner la inversión y sumar el evento de conversión (ver Meta en Prometheo). El detalle anuncio por anuncio está en <b>Insights</b>.")}</div>
</section>'''


# =====================================================================
G = [
    dict(c="Búsqueda · Marca PAVIR", t="Búsqueda", kw="«puertas pavir» · exacta y amplia", imp=2100, clics=250, cpc=144, costo=36000, cons=24, resp=22, calif=15, deriv=14, b2b=3),
    dict(c="Búsqueda · Puerta de seguridad", t="Búsqueda", kw="«puerta de seguridad» · amplia", imp=11800, clics=520, cpc=185, costo=96000, cons=30, resp=25, calif=8, deriv=7, b2b=1),
    dict(c="Performance Max · Catálogo", t="PMax", kw="catálogo completo · formulario", imp=14500, clics=240, cpc=200, costo=48000, cons=14, resp=12, calif=5, deriv=4, b2b=1),
    dict(c="Display · Remarketing", t="Display", kw="visitantes de la web", imp=34000, clics=150, cpc=120, costo=18000, cons=4, resp=4, calif=2, deriv=2, b2b=1),
]


def googleads():
    T = {k: sum(g[k] for g in G) for k in ["imp", "clics", "costo", "cons", "resp", "calif", "deriv", "b2b"]}
    funnel = _steps([("Impresiones", T["imp"], "en búsqueda y display"), ("Clics", T["clics"], "a la web o WhatsApp"), ("Consultas", T["cons"], "en Prometheo"),
                     ("Respondieron", T["resp"], "al agente"), ("Calificadas", T["calif"], "producto, zona y cantidad"), ("Derivadas", T["deriv"], "a distribuidor")])
    kp = '<div class="g4">' + "".join([
        kpi("Inversión sugerida", f'${fmt(T["costo"])}', lvl("proy"), "4 campañas", "dollar", "", "goog"),
        kpi("Consultas", str(T["cons"]), lvl("proy"), f'tasa de conversión {fmt(100 * T["cons"] / T["clics"], 1)}%', "chat", "blu", "goog"),
        kpi("Calificadas", str(T["calif"]), lvl("proy"), f'{pct(T["calif"], T["cons"])}% de las consultas', "checkc", "grn", "pro"),
        kpi("Costo por calificada", f'${fmt(T["costo"] / T["calif"])}', lvl("proy"), "Marca: $2.400 · Meta hoy: $794", "sigma", "pnk", "calc"),
    ]) + "</div>"
    cards = f'''<div class="igrid">
{i3("subir", "Búsqueda de la marca PAVIR: quien la busca ya decidió, califica 63%",
    [("Campaña", "Búsqueda · Marca PAVIR"), ("Grupo", "Marca · exacta y amplia"), ("Palabra", "«puertas pavir», «pavir aberturas»")],
    ["Hoy esa búsqueda no tiene anuncio: el primer resultado puede ser un competidor.", "Proyección: <b>24 consultas</b> al mes, <b>15</b> calificadas.", "Es la campaña más barata por calificada de Google: <b>$2.400</b>."],
    "63%", "de las consultas por búsqueda de marca calificarían. Promedio proyectado de Google: 42%.",
    cmpbar(63, 42, "promedio 42%", "búsqueda de marca", "promedio proyectado de las 4 campañas"), own("mkt"), lvl("proy"), lab3="Resultado proyectado contra el objetivo")}
{i3("corr", "Búsqueda «puerta de seguridad»: mucho volumen, 27% califica",
    [("Campaña", "Búsqueda · Puerta de seguridad"), ("Grupo", "Genérico · amplia"), ("Palabra", "«puerta de seguridad», «puerta blindada»")],
    ["Trae volumen, pero mezcla consumidores de todo el país y curiosos.", "Proyección: <b>30 consultas</b>, <b>8</b> calificadas.", "Sumar la zona en el anuncio y palabras negativas («precio», «usada») antes de invertir."],
    "27%", "de las consultas calificarían. Promedio proyectado: 42%.",
    cmpbar(27, 42, "promedio 42%", "búsqueda genérica", "promedio proyectado"), own("mkt"), lvl("proy"), lab3="Resultado proyectado contra el objetivo")}
{i3("prob", "Performance Max con el catálogo: probar con formulario conectado al CRM",
    [("Campaña", "Performance Max · Catálogo"), ("Grupo", "Recursos del catálogo"), ("Palabra", "sin palabras clave: decide Google")],
    ["El formulario entra a Prometheo como consulta, con la línea ya cargada.", "Proyección: <b>14 consultas</b>, <b>5</b> calificadas.", "Sirve para medir si Google trae comercios (B2B) que Meta no alcanza."],
    "36%", "de las consultas calificarían. Promedio proyectado: 42%.",
    cmpbar(36, 42, "promedio 42%", "Performance Max", "promedio proyectado"), own("mkt"), lvl("proy"), lab3="Resultado proyectado contra el objetivo")}
</div>'''
    rows = [[f'<b>{g["c"]}</b><span class="sub">{g["kw"]}</span>', g["t"], fmt(g["imp"]), fmt(g["clics"]), f'{fmt(100 * g["clics"] / g["imp"], 1)}%', f'${g["cpc"]}', f'${fmt(g["costo"])}',
             str(g["cons"]), str(g["resp"]), str(g["calif"]), f'{pct(g["calif"], g["cons"])}%', str(g["deriv"]), str(g["b2b"]), f'<b>${fmt(g["costo"] / g["calif"])}</b>'] for g in G]
    rows.append((["<b>Total</b>", "", fmt(T["imp"]), fmt(T["clics"]), f'{fmt(100 * T["clics"] / T["imp"], 1)}%', "", f'${fmt(T["costo"])}', str(T["cons"]), str(T["resp"]), str(T["calif"]),
                  f'{pct(T["calif"], T["cons"])}%', str(T["deriv"]), str(T["b2b"]), f'${fmt(T["costo"] / T["calif"])}'], "tr:tot"))
    th = [f'{ic("camp", style="width:12px;height:12px")} Campaña', f'Tipo {src("goog")}', f'Impres. {src("goog")}', f'Clics {src("goog")}', f'CTR {src("goog")}', f'CPC {src("goog")}', f'Costo {src("goog")}',
          f'Consultas {src("pro")}', f'Resp. {src("pro")}', f'Calif. {src("pro")}', f'% Calif. {src("calc")}', f'Deriv. {src("pro")}', f'B2B {src("pro")}', f'Costo/calif. {src("calc")}']
    conv = table([f'Acción de conversión {src("goog")}', "Tipo", "Consultas", f'Cómo entra a Prometheo {src("pro")}'], [
        ["Clic para chatear por WhatsApp", "Mensaje", "40", "Directo: conversación con el agente"], ["Formulario de cotización", "Formulario", "24", "Directo: consulta con la línea cargada"], ["Llamada telefónica", "Llamada", "8", "Manual: hay que cargarla a mano"]], 620)
    return f'''<section class="panel p-googleads">
{_chan_head("Google Ads", "Hoy <b>pausado</b>. Así se vería al reactivarlo, con el mismo formato que Meta: arriba, el <b>cruce Google × Prometheo</b>; abajo, el export. Todos los números son <b>proyección</b> sobre la intención de búsqueda que hoy no se trabaja.<span class='adv'> Jerarquía de Google: campaña › grupo de anuncios › palabra clave. <b>CTR</b> = clics ÷ impresiones · <b>CPC</b> = costo por clic.</span>")}
{_iobar("Importar export de Google", True, "Reactivar la cuenta para empezar a medir en real")}
{_legend([("goog", "Costo, impresiones, clics, CTR, CPC, conversiones."), ("pro", "De la conversión a la <b>consulta calificada</b> y la derivación."), ("calc", "% que califica y costo por calificada.")])}
{kp}
{eyebrow("1 · De la búsqueda a la derivación", " " + lvl("proy"))}
<div class="card pad">{funnel}</div>
{eyebrow("2 · Campañas sugeridas · campaña › grupo de anuncios › palabra clave")}
{cards}
{eyebrow("3 · Export de Google con Prometheo al lado", " " + lvl("proy"))}
{table(th, rows, 1300)}
<div class="adv mt">{eyebrow("Acciones de conversión · cómo entra cada consulta · modo avanzado")}{conv}</div>
</section>'''


# =====================================================================
def _bases(canal):
    wpp = canal == "wpp"
    return f'''<div class="g3">
<div class="vcard">{ghdr("Padrón de clientes", "ledger", "", src("erp"))}<div class="k-n" style="font-size:26px">700</div><div class="k-s">Distribuidores activos y pasivos. <b>{"150 activos" if wpp else "200 pasivos"}</b> en esta campaña.</div>
<div class="obase"><span class="chip">{ic("tag")}distribuidor_{"activo" if wpp else "pasivo"}</span><span class="chip">{ic("check")}Consentimiento: es cliente</span></div></div>
<div class="vcard">{ghdr("Feria BATEV", "badge", "", src("pro"))}<div class="k-n" style="font-size:26px">320</div><div class="k-s">Tarjetas del stand cargadas al CRM con su tag, no a un Excel. <b>{"Pueden recibir WhatsApp: dejaron el número en el stand." if wpp else "Secuencia de 3 mails lista para el próximo envío."}</b></div>
<div class="obase"><span class="chip">{ic("tag")}feria_batev_2026</span><span class="chip">{ic("check")}Consentimiento en el stand</span></div></div>
<div class="vcard">{ghdr("Scraping de corralones", "globe", "", src("calc"))}<div class="k-n" style="font-size:26px">220</div><div class="k-s">Corralones y ferreterías relevados en las 7 provincias sin red activa. <b>{"No van por WhatsApp masivo: sin consentimiento sube el reporte y baja la calidad del número." if wpp else "Primer contacto por mail con opción de baja; si responden, siguen por WhatsApp."}</b></div>
<div class="obase"><span class="chip">{ic("tag")}prospecto_scraping</span><span class="chip">{ic("alert")}{"Excluido del masivo" if wpp else "Solo email con baja"}</span></div></div>
</div>'''


def email():
    funnel = fsteps([dict(num="01", pt="", label="Enviados", val="<b>200</b> pasivos", w=100, **{"pass": "base"}),
                     dict(num="02", pt="93%", label="Entregados", val="<b>186</b>", w=93, **{"pass": "pasa 93%"}),
                     dict(num="03", pt="", label="Abrieron", val="<b>97</b> · no titula", w=49, cls="dim", **{"pass": "52% · señal inflada"}),
                     dict(num="04", pt="17%", label="Clic o respuesta", val="<b>34</b>", w=17, **{"pass": "35% CTOR"}),
                     dict(num="05", pt="15%", label="Conversaron en Prometheo", val="<b>29</b>", w=15, **{"pass": "85% empalme"}),
                     dict(num="06", pt="9%", label="Calificados", val="<b>17</b>", w=9, **{"pass": "pasa 59%"}),
                     dict(num="07", pt="3%", label="Volvieron a pedir", val="<b>6</b>", w=3, **{"pass": "pasa 35%"})])
    C = "Reactivación de pasivos · bisagra interior"
    cards = f'''<div class="igrid">
{i3("paus", "El segmento con deuda abre 35% contra 57%: la cuenta trabada frena más que el precio",
    [("Campaña", C), ("Segmento", "Con deuda · 45 contactos"), ("Envío", "Los 3 envíos, mismo texto")],
    ["Recibieron el mismo mail que los otros dos segmentos: no es el mensaje, es la cuenta.", "De 40 entregados, <b>1 solo calificó</b>.", "Próximo paso: sacarlos del email y pasarlos a un contacto de cobranza."],
    "35%", "de apertura en el segmento con deuda. Los otros dos segmentos: 57%.",
    cmpbar(35, 57, "otros segmentos 57%", "con deuda", "segmentos sin deuda"), own("cob"), adv="<p>De los 45, <b>5 rebotaron</b> (11% contra 7% de la base): la cuenta trabada viene con ficha desactualizada.</p>",
    lab3="Resultado contra el resto de la campaña")}
{i3("corr", "9 de 29 preguntaron exactamente lo mismo: si la bisagra entra en el marco existente",
    [("Campaña", C), ("Segmento", "Los 29 que conversaron"), ("Envío", "Envío 1 · Novedad")],
    ["El mail no lo contesta: el agente responde uno por uno.", "Próximo paso: <b>una línea en el mail</b> y la ficha técnica en el catálogo.", "Si se contesta en el cuerpo, debería subir el CTOR sin tocar el asunto."],
    "31%", "de los que conversaron hizo la misma pregunta técnica.", cmpbar(31, None, "", "misma pregunta"), own("mkt"), lab2="Qué muestra la conversación", lab3="Resultado")}
{i3("mant", "El traspaso del mail al agente casi no pierde gente: 85% de empalme",
    [("Campaña", C), ("Segmento", "34 que hicieron clic o respondieron"), ("Envío", "Los 3 envíos")],
    ["<b>29 de 34</b> terminaron conversando con el agente.", "Se pierden <b>5</b>: clic sin escribir. Todos del envío 1.", "Es la métrica que la plataforma de email no ve, porque termina en el clic."],
    "85%", "de quienes reaccionaron al mail terminaron conversando en Prometheo.", cmpbar(85, None, "", "empalme email → Prometheo"), own("mkt"),
    adv="<p><b>Empalme</b>: contactos que escriben a Prometheo dentro de las 72 h del clic ÷ clics únicos.</p>", lab3="Resultado")}
{i3("red", "El primer envío hizo el 62% del trabajo: la secuencia puede ser de dos",
    [("Campaña", C), ("Segmento", "Los 3 segmentos"), ("Envío", "1 · Novedad → 2 · Prueba → 3 · Cierre")],
    ["Envío 1: <b>21</b> reacciones · Envío 2: <b>9</b> · Envío 3: <b>4</b>.", "El tercero ya raspa la base: 4 reacciones contra 1 baja.", "Próxima ronda: dos envíos y el esfuerzo a segmentar mejor."],
    "62%", "de las reacciones vinieron del primer envío.", cmpbar(62, None, "", "envío 1"), own("mkt"), lab3="Resultado")}
{i3("corr", "El reactivado pide lista de precios, no cotización",
    [("Campaña", C), ("Segmento", "Los 29 que conversaron"), ("Envío", "Los 3 envíos")],
    ["<b>21 de 29</b> pidieron la lista de precios antes que nada.", "<b>7</b> pidieron muestra o exhibidor para el salón.", "Solo <b>6</b> objetaron precio: la barrera es la información."],
    "72%", "pidió la lista de precios: adjuntarla ahorra un ida y vuelta.", cmpbar(72, None, "", "pidió lista"), own("mkt"), lab2="Qué muestra la conversación", lab3="Resultado")}
{i3("subir", "Las tarjetas de la feria BATEV no pueden terminar en un Excel",
    [("Campaña", "Feria BATEV 2026 · seguimiento"), ("Segmento", "320 contactos del stand"), ("Envío", "Secuencia de 3 mails, lista")],
    ["Hoy las tarjetas se vuelcan a una planilla y se enfrían en dos semanas.", "Cargadas al CRM con su tag, disparan el <b>seguimiento uno a uno</b> y la reunión con el corredor.", "Son la base del próximo envío y de la semilla de público parecido en Meta."],
    "320", "contactos de feria listos para la secuencia. Hoy, 0 seguidos desde el CRM.", cmpbar(100, None, "", "cargados al CRM con tag"), own("mkt"), lab2="Qué muestra el CRM", lab3="Resultado")}
</div>'''
    seg_tab = table(["Segmento", "Concepto del envío", "Base", "Entreg.", "Abrió", "Clic o resp.", "En Prometheo", "Calificó"], [
        ['<b>Solo puertas</b><span class="sub">no compran ventanas</span>', "Bisagra interior + cruce a ventana PVC", "84", "79", "45 <small>57%</small>", "17", "15", "<b>10</b>"],
        ['<b>Dormido sin deuda</b><span class="sub">+45 días sin pedido</span>', "Novedad de catálogo", "71", "67", "38 <small>57%</small>", "13", "11", "<b>6</b>"],
        (['<b>Con deuda</b><span class="sub">cuenta trabada</span>', "Novedad + regularización", "45", "40", "14 <small>35%</small>", "4", "3", "<b>1</b>"], "tr:hi"),
        (["<b>Total</b>", "—", "200", "186", "97 <small>52%</small>", "34", "29", "<b>17</b>"], "tr:tot")], 760)
    env_tab = table(["Envío", "Asunto", "Día", "Destinatarios", "Aperturas", "Clic o resp.", "CTOR"], [
        ["<b>1 · Novedad</b>", "Nueva línea: la bisagra va por dentro", "0", "186", "78 <small>42%</small>", "<b>21</b>", "27%"],
        ["<b>2 · Prueba</b>", "Los que ya la venden repiten pedido", "4", "165", "41 <small>25%</small>", "<b>9</b>", "22%"],
        ["<b>3 · Cierre</b>", "¿Te mando el catálogo y la lista?", "9", "156", "24 <small>15%</small>", "<b>4</b>", "17%"]], 760)
    return f'''<section class="panel p-email">
{_chan_head("Email Marketing", ("El email <b>genera la conversación</b>; el agente de Prometheo responde el mail, califica y deriva. Lo que importa no es cuántos lo abrieron sino <b>cuántos terminaron conversando</b>.", "El clic no es el final del embudo: es <b>el empalme</b> (conversación en Prometheo dentro de las 72 h del clic ÷ clics únicos). La apertura se muestra pero no titula: es una señal inflada por la precarga de imágenes. <b>CTOR</b> = clics ÷ aperturas."))}
{_legend([("mail", "Enviados, entregados, aperturas, clics, rebotes y bajas."), ("pro", "Quién conversó con el agente, qué pidió, <b>calificación</b> y derivación."), ("calc", "Empalme, CTOR y lectura por segmento.")])}
{eyebrow("De dónde sale la base · padrón, ferias y scraping")}
{_bases("mail")}
{eyebrow("La campaña · reactivar a los 200 pasivos con la línea de bisagra interior")}
<div class="card pad">{ghdr("Embudo de la campaña", "filter", "base: 200 pasivos · titula el empalme, no la apertura", src("calc"))}{funnel}
<div class="glos"><div><b>CTOR</b>clics ÷ aperturas: calidad del contenido</div><div><b>CTR</b>clics ÷ entregados: 18%</div><div><b>Empalme</b>conversaron en Prometheo ÷ clics</div><div><b>Rebote duro</b>dirección que ya no existe</div></div></div>
{eyebrow("Insights del cruce · campaña › segmento › envío")}
{cards}
{eyebrow("Métricas cruzadas · desplegá el detalle")}
{mincard("Embudo por segmento", "un concepto por segmento, el mismo embudo para los tres", seg_tab + '<div class="note"><b>Próximo paso:</b> sacar a los 45 con deuda del circuito de email y pasarlos a cobranza; el mail no resuelve una cuenta trabada.</div>', "grid", "3", "segmentos", True)}
{mincard("Envío por envío", "rendimiento decreciente y hasta dónde conviene insistir", env_tab + ul(["Cada envío sale solo a quien <b>no reaccionó</b> al anterior: las 34 reacciones son personas distintas.", "Las aperturas <b>sí se pisan</b>: 78 + 41 + 24 son eventos; personas que abrieron al menos uno, 97."]), "mail", "34", "reacciones")}
{mincard("Qué preguntaron los que volvieron", "lo que solo se ve en la conversación", bars([("Lista de precios actualizada", 21, "72%"), ("Plazo de entrega", 14, "48%"), ("¿Entra en marco existente?", 9, "31%"), ("Muestra o exhibidor para el salón", 7, "24%"), ("Objeción de precio", 6, "21%")]) + '<div class="note">Base 29; uno puede preguntar más de una cosa: los porcentajes no suman 100.</div>', "chat", "29", "conversaciones")}
<div class="adv">{eyebrow("Lectura de especialista · entregabilidad y velocidad · modo avanzado")}
<div class="g2">
<div class="bc" style="--bcac:var(--crit)"><div class="bc-hd"><div class="bc-nm">Entregabilidad</div>{src("mail")}</div><div class="bc-row"><div><div class="v">4,5%</div><div class="k">rebote duro</div></div><div><div class="v">0</div><div class="k">quejas de spam</div></div><div><div class="v">1,6%</div><div class="k">tasa de baja</div></div></div>
<div class="bc-verd">{ic("alert")}<div>El rebote duro está <b>por encima del 2%</b> que conviene sostener. Depurar los 9 antes del próximo envío.</div></div></div>
<div class="bc" style="--bcac:var(--good)"><div class="bc-hd"><div class="bc-nm">Velocidad de respuesta</div>{src("pro")}</div><div class="bc-row"><div><div class="v">40 s</div><div class="k">mediana del agente</div></div><div><div class="v">100%</div><div class="k">bajo 5 minutos</div></div><div><div class="v">26</div><div class="k">charlas de 2+ mensajes</div></div></div>
<div class="bc-verd">{ic("bolt")}<div>El que responde <b>encuentra a alguien del otro lado</b>, no un autoresponder.</div></div></div>
</div></div>
{eyebrow("Solo email · data de la plataforma de envío", " " + src("mail"))}
<div class="g4">{kpi("Tasa de entrega", "93%", "", "186 de 200", "check", "grn", "mail")}{kpi("Rebotes", "14", "", "9 duros · 5 blandos", "x", "amb", "mail")}{kpi("Bajas", "3", "", "1,6% de los entregados", "minus", "", "mail")}{kpi("CTR", "18%", "", "clic o respuesta sobre entregados", "anun", "blu", "mail")}</div>
<div class="mt">{banner("warn", "alert", "<b>Falta para cerrar el análisis:</b> el costo de la plataforma de envío. Sin ese número no hay costo por distribuidor reactivado ni comparación con Meta en la misma unidad. Es un faltante de integración: se resuelve conectando la cuenta.")}</div>
</section>'''


def whatsapp():
    seg = fsteps([dict(num="01", pt="", label="Padrón completo", val="<b>700</b>", w=100, **{"pass": "base"}),
                  dict(num="02", pt="71%", label="Activos", val="<b>500</b>", w=71, **{"pass": "pasa 71%"}),
                  dict(num="03", pt="45%", label="Corralón o vidriería", val="<b>312</b>", w=45, **{"pass": "pasa 62%"}),
                  dict(num="04", pt="24%", label="Nunca pidió pivotante", val="<b>171</b>", w=24, **{"pass": "pasa 55%"}),
                  dict(num="05", pt="21%", label="Cuenta al día", val="<b>150</b>", w=21, **{"pass": "pasa 88%"})])
    res = fsteps([dict(num="01", pt="", label="Enviados", val="<b>150</b>", w=100, **{"pass": "base"}),
                  dict(num="02", pt="95%", label="Entregados", val="<b>143</b>", w=95, **{"pass": "pasa 95%"}),
                  dict(num="03", pt="", label="Leídos", val="<b>118</b> · no titula", w=79, cls="dim", **{"pass": "83% · subestimado"}),
                  dict(num="04", pt="31%", label="Respondieron", val="<b>47</b>", w=31, **{"pass": "33% de entregados · 40% de leídos"}),
                  dict(num="05", pt="21%", label="Calificados por el agente", val="<b>31</b>", w=21, **{"pass": "pasa 66%"}),
                  dict(num="06", pt="6%", label="Pedido con pivotantes", val="<b>9</b>", w=6, **{"pass": "pasa 29%"})])
    C = "Pivotantes para la red que compra puertas"
    cards = f'''<div class="igrid">
{i3("mant", "El exhibidor es lo que cerró los pedidos, no el contramarco bonificado",
    [("Campaña", C), ("Segmento", "Los 9 que hicieron pedido"), ("Plantilla", "A · Beneficio ganado")],
    ["<b>8 de 9</b> pedidos pidieron el exhibidor en la conversación.", "Solo <b>3</b> mencionaron el contramarco bonificado.", "El freno era la exhibición, no el precio."],
    "89%", "de los pedidos pasó por el exhibidor.", cmpbar(89, None, "", "pidió exhibidor"), own("ven"),
    adv="<p>El exhibidor es costo de marketing, no de margen: mover el beneficio al exhibidor <b>abarata la promo</b>. Próxima prueba: exhibidor solo, sin bonificación.</p>",
    lab2="Qué muestra la conversación", lab3="Resultado")}
{i3("prob", "El corralón cierra 33%, la vidriería 20%: necesitan mensajes distintos",
    [("Campaña", C), ("Segmento", "96 corralones · 54 vidrierías"), ("Plantilla", "A y B")],
    ["Corralón: <b>7 pedidos</b> sobre 21 calificados · Vidriería: <b>2</b> sobre 10.", "Responden casi igual; la diferencia aparece en el cierre.", "La vidriería pregunta por medidas a medida; el corralón, por stock y plazo."],
    "33%", "cierre del corralón. Vidriería: 20%.", cmpbar(33, 20, "vidriería 20%", "corralón", "vidriería"), own("mkt"), lab3="Resultado contra el otro segmento")}
{i3("mant", "Responder abre 24 horas de conversación libre: 44 de 47 se resolvieron adentro",
    [("Campaña", C), ("Segmento", "Los 47 que respondieron"), ("Plantilla", "A y B")],
    ["Cuando el distribuidor contesta, el agente conversa <b>sin plantilla por 24 horas</b>.", "<b>44 de 47</b> quedaron resueltas dentro de esa ventana.", "Las 3 que se pasaron necesitaron otra plantilla para retomar."],
    "94%", "se resolvió dentro de la ventana de 24 horas.", cmpbar(94, None, "", "dentro de 24 h"), own("mkt"), lab3="Resultado")}
{i3("corr", "Siete rechazos que son tarea del CRM, no de la campaña",
    [("Campaña", C), ("Segmento", "150 enviados"), ("Plantilla", "A y B")],
    ["<b>4</b> números sin WhatsApp · <b>2</b> con prefijo mal cargado · <b>1</b> baja previa.", "Los 2 de prefijo se recuperan corrigiendo la ficha.", "La baja previa se marca como excluida permanente: reenviarle afecta la calidad del número."],
    "4,7%", "de la audiencia rebotó por calidad de ficha.", cmpbar(4.7, None, "", "rechazados"), own("ven"), lab3="Resultado")}
{i3("subir", "La plantilla que nombra al comercio rinde 15 puntos más",
    [("Campaña", C), ("Segmento", "75 contactos por variante"), ("Plantilla", "A · Beneficio ganado vs B · Novedad")],
    ["A: «{{comercio}}, por lo que compraste estos 90 días te toca…» · B: «Sumamos pivotantes…».", "La diferencia aparece <b>en la respuesta, no en la lectura</b>.", "La A queda como plantilla base de la cuenta."],
    "47%", "respuesta sobre leído de la variante A. Variante B: 32%.", cmpbar(47, 32, "variante B 32%", "variante A", "variante B"), own("mkt"), lab3="Resultado contra la otra variante")}
{i3("subir", "Los 320 contactos de la feria pueden recibir WhatsApp: dejaron el número en el stand",
    [("Campaña", "Feria BATEV 2026 · seguimiento"), ("Segmento", "320 contactos con consentimiento"), ("Plantilla", "Bienvenida de feria, a aprobar")],
    ["Son comercios y obras que se acercaron al stand: intención alta y reciente.", "Entran al embudo B2B con su tag y el corredor de la zona recibe el aviso.", "Los 220 del scraping <b>no</b> van por acá: sin consentimiento, primero mail."],
    "320", "contactos de feria para la próxima difusión. Uso del cupo diario: 32%.", cmpbar(32, None, "", "cupo diario que usarían"), own("mkt"), lab2="Qué muestra el CRM", lab3="Resultado")}
</div>'''
    var_tab = table(["Variante aprobada", "Apertura del mensaje", "Enviados", "Leídos", "Respondieron", "Resp. sobre leído"], [
        ['<b>A · Beneficio ganado</b><span class="sub">nombra el comercio y el volumen</span>', "«{{comercio}}, por lo que compraste estos 90 días te toca…»", "75", "62", "<b>29</b>", "47%"],
        ['<b>B · Novedad de línea</b><span class="sub">arranca por el producto</span>', "«Sumamos pivotantes de aluminio a la línea…»", "75", "56", "<b>18</b>", "32%"]], 700)
    tipo_tab = table(["Tipo de comercio", "Audiencia", "Entregados", "Leídos", "Respondieron", "Calificados", "Pedidos", "Cierre"], [
        ['<b>Corralón</b><span class="sub">mostrador, stock propio</span>', "96", "92", "78 <small>85%</small>", "32", "21", "<b>7</b>", "33%"],
        ['<b>Vidriería</b><span class="sub">venta a obra, a medida</span>', "54", "51", "40 <small>78%</small>", "15", "10", "<b>2</b>", "20%"],
        (["<b>Total</b>", "150", "143", "118 <small>83%</small>", "47", "31", "<b>9</b>", "29%"], "tr:tot")], 720)
    return f'''<section class="panel p-whatsapp">
{_chan_head("WhatsApp Marketing", ("Campañas masivas desde <b>Prometheo</b> con plantilla aprobada. La audiencia sale del CRM y la respuesta cae en la conversación del agente. Lo que importa es <b>cuántos respondieron</b>, no cuántos lo leyeron.", "La respuesta se lee sobre entregados y sobre leídos (doble lectura); la lectura no titula porque quien desactivó la confirmación no cuenta. <b>Tier</b> y <b>calidad del número</b> son métricas de tablero: definen el tamaño de la próxima difusión."))}
{_legend([("wpp", "Enviados, entregados, leídos, rechazados con motivo, tier y calidad del número."), ("pro", "Audiencia por Smart Tag, respuesta, <b>calificación</b> y pedido."), ("calc", "Tasas entre pasos y lectura por tipo de comercio.")])}
<div class="g4">{kpi("Respondieron", "33%", "", "47 de 143 entregados · 40% de los leídos", "chat", "grn", "pro", adv="Doble lectura: sobre entregados y sobre leídos. La lectura sola no titula: quien desactivó la confirmación no cuenta.")}
{kpi("Pedidos", "9", "", "distribuidores que incorporaron pivotantes", "doc", "", "pro")}
{kpi("Tier del número", "Tier 1", "", "1.000 contactos únicos por día · uso 15%", "sliders", "blu", "wpp", adv="<b>Tier</b>: tope de contactos únicos en 24 h. Define el tamaño máximo de la próxima difusión. Actualizado 29 sep.")}
{kpi("Calidad del número", "Alta", "", "0 reportes · 0 bloqueos · actualizado 29 sep", "shield", "grn", "wpp")}</div>
{eyebrow("De dónde sale la base · padrón, ferias y scraping")}
{_bases("wpp")}
{eyebrow("La campaña · pivotantes para la red que ya compra puertas")}
<div class="card pad">{ghdr("Los ejes de la segmentación", "filter", "de 700 en el padrón a 150 en la audiencia · cada filtro es una decisión", src("pro"))}{seg}
<div class="note">Ejes: <b>estado</b> (activo), <b>tipo de comprador</b> (corralón y vidriería, con salón), <b>producto</b> (nunca pidió pivotante) y <b>higiene</b> (cuenta al día). La oferta: contramarco bonificado y <b>exhibidor sin cargo</b> en el primer pedido de 3 pivotantes.</div></div>
<div class="card pad mt">{ghdr("Resultado de la campaña", "chat", "base: 150 enviados", src("calc"))}{res}</div>
{eyebrow("Insights · campaña › segmento › plantilla")}
{cards}
{eyebrow("Métricas cruzadas · desplegá el detalle")}
{mincard("Embudo por tipo de comercio", "mismo mensaje, dos ciclos de compra", tipo_tab, "grid", "2", "tipos", True)}
{mincard("Variantes de plantilla", "qué versión del mensaje rindió mejor", var_tab + ul(["La que <b>nombra al comercio y lo que ya compró</b> rinde 15 puntos más en respuesta sobre leído.", "Las dos se leen parecido porque el mensaje se ve en la notificación: por eso la lectura no decide."]), "wa", "2", "variantes")}
{mincard("Qué preguntaron los que respondieron", "lo que el agente resolvió sin pasar por una persona", bars([("Cómo es el exhibidor y qué ocupa", 28, "60%"), ("Plazo de entrega", 24, "51%"), ("Precio por unidad y condición de pago", 19, "40%"), ("Medidas a medida", 13, "28%"), ("Si se suma al beneficio de puertas", 9, "19%")]) + '<div class="note">Base 47; uno puede preguntar más de una cosa. El masivo va solo con texto: describir el exhibidor en la plantilla y que el agente mande la foto en la conversación.</div>', "chat", "47", "conversaciones")}
<div class="adv">{eyebrow("Salud del canal · modo avanzado")}
<div class="g2">
<div class="bc" style="--bcac:var(--good)"><div class="bc-hd"><div class="bc-nm">Salud del número</div>{src("wpp")}</div><div class="bc-row"><div><div class="v">Tier 1</div><div class="k">1.000 contactos/día</div></div><div><div class="v">15%</div><div class="k">uso del cupo</div></div><div><div class="v">0</div><div class="k">reportes</div></div></div>
<div class="bc-verd">{ic("shield")}<div>Calidad <b>alta</b>. El tier sube solo con calidad y actividad constante: hay margen para escalar a toda la red activa.</div></div></div>
<div class="bc" style="--bcac:var(--vio)"><div class="bc-hd"><div class="bc-nm">Cuándo contestan</div>{src("calc")}</div><div class="bc-row"><div><div class="v">8 min</div><div class="k">mediana hasta leer</div></div><div><div class="v">68%</div><div class="k">responde de 9 a 12 h</div></div><div><div class="v">4%</div><div class="k">después de las 18 h</div></div></div>
<div class="bc-verd">{ic("clock")}<div>El corralón atiende a la mañana: un envío a las 18 h se lee igual pero <b>no se contesta</b>.</div></div></div>
</div></div>
<div class="mt">{banner("good", "shield", "La campaña salió con <b>plantilla aprobada</b> y sobre contactos con consentimiento: es lo que mantiene alta la calidad del número. Escribirle a quien no dio permiso no cuesta una campaña, cuesta <b>el techo de todas las siguientes</b>.")}</div>
</section>'''
