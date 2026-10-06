"""Distribuidores y Corredores."""
from icons import ic
from comp import (fmt, pct, money, src, lvl, own, chip, delta, sec_head, eyebrow, ghdr, banner, kpi, bar, bars,
                  vcard, table, bsc_adv, minibar, mincard, ul, i3, kv, cmpbar, est)
import data as D


def distribuidores():
    kp = '<div class="g4">' + "".join([
        kpi("Distribuidores en el padrón", str(D.RED), delta("0%", "flat", None), "Código, razón social y contacto", "building", "", "erp"),
        kpi("Activos", str(D.ACTIVOS), delta("+4", "good"), "71% · compraron en los últimos 90 días", "checkc", "grn", "erp"),
        kpi("Provincias con red activa", str(D.PROV_ACT), delta("0", "flat", None), f"{D.PROV_PAS} provincias solo con pasivos", "pin", "blu", "erp"),
        kpi("Deuda en calle", money(D.DEUDA_M), delta("−4%", "good", "down"), f"{D.CON_DEUDA} distribuidores · menos es mejor", "clock", "pnk", "erp"),
    ]) + "</div>"
    legend = f'<div class="estlegend"><b style="color:var(--ink2)">Estado de cuenta:</b>{est("ok")}{est("warn")}{est("bad")}{est("off")}<span>· el color y el ícono cambian juntos</span></div>'
    grid = f'''<div class="g3 mt">
{vcard("Por estado", bar("Activos · compraron en 90 días", "500", 100, "71%", "var(--st-ok)") + bar("Pasivos · sin compra en 90 días", "200", 40, "29%", "var(--st-off)"), "users", "", src("erp"))}
{vcard("Estado de cuenta", bar(est("ok"), fmt(D.SIN_DEUDA), 100, "88%", "var(--st-ok)") + bar(est("warn", "Con deuda al día"), str(D.DEUDA_AL_DIA), 8.6, "8%", "var(--st-warn)") + bar(est("bad"), str(D.VENCIDOS), 5, "4%", "var(--st-bad)"), "dollar", "", src("erp"))}
{vcard("Tipo de distribuidor", bars([("Corralón", 230), ("Ferretería", 140), ("Vidriería o aberturas", 70), ("Constructora u obra", 60)], total=500), "store", "base: 500 activos", src("erp"))}
{vcard("Activos por provincia", bars([("Buenos Aires", 156), ("Santa Fe", 72), ("Córdoba", 64), ("Mendoza", 41), ("Otras 11 provincias", 167)], total=500), "pin", "", src("erp"))}
{vcard("Cada cuánto compran", bars([("Cada 7 a 10 días", 218), ("Una vez por mes", 164), ("Esporádico", 118)], total=500), "clock", "", src("erp"))}
{vcard("Señales de acción", bar("Le toca comprar", "126", 100, "", "var(--vio)") + bar("Sin comprar +45 días", "73", 58, "", "var(--st-warn)") + bar("Vencidos +30 días", "31", 25, "", "var(--st-bad)"), "bolt", "", src("calc"))}
</div>'''
    top = [
        ("Corralón del Oeste", "GBA Oeste", "Corralón", "Puertas de acero", 14, 8.9, "AMBA Oeste", "ok"),
        ("Aberturas Rosario", "Santa Fe", "Vidriería", "Ventanas PVC", 11, 6.4, "Litoral", "ok"),
        ("Ferretería Centro", "Córdoba", "Ferretería", "Puertas de acero", 9, 5.1, "Centro", "warn"),
        ("Casa Mendoza", "Mendoza", "Corralón", "Pivotantes", 8, 4.7, "Cuyo", "ok"),
        ("Aberturas del Litoral", "Entre Ríos", "Vidriería", "Ventanas de aluminio", 7, 3.9, "Litoral", "bad"),
        ("Corralón Norte", "Tucumán", "Corralón", "Puertas de acero", 6, 3.3, "NOA", "ok"),
        ("Materiales Sur", "Neuquén", "Ferretería", "Ventanas PVC", 5, 2.8, "Comahue", "warn"),
        ("Obras y Aberturas", "Chaco", "Constructora", "Puertas de acero", 3, 1.6, "NEA", "bad"),
    ]
    rows = [[f'<b>{n}</b><span class="sub">{z}</span>', t, l, str(p), f"<b>${fmt(v, 1)} M</b>", c, f'<td class="l">{est(s)}</td>'] for n, z, t, l, p, v, c, s in top]
    tabla = table(["Distribuidor · provincia", "Tipo", "Línea principal", "Pedidos 90 días", "Volumen 90 días", "Corredor", '<span style="display:block;text-align:left">Estado de cuenta</span>'], rows, 820)
    adv = f'''<div class="adv">{eyebrow("Cruces de red · modo avanzado")}
{mincard("7 provincias solo con pasivos", "zonas sin red activa, para captar", kv([("7", "provincias sin activos"), ("200", "pasivos reactivables"), ("1.240", "semilla para Lookalike B2B")]) + ul(["Reactivar pasivos con difusión y visita del corredor más cercano", "Captar distribuidores nuevos con Lookalike del padrón (ver Audiencias)"]), "pin", "200", "pasivos", True)}
{mincard("Concentración de cartera", "el 20% que hace la caja", kv([("100", "distribuidores que más compran"), ("68%", "de la facturación"), ("7 a 10 días", "cada cuánto compran")]) + ul(["Visita fija y cuidado del vencimiento para sostener la caja", "Resto de la red: campañas de reactivación de menor costo"]), "star", "68%", "facturación")}
</div>'''
    return f'''<section class="panel p-distrib">
{sec_head("Distribuidores · la red", "700 clientes en el padrón, <em>500 activos en 15 provincias.</em>",
          ("La red es el cliente real de PAVIR. Sin exclusividad de zona: el tablero muestra dónde hay cartera para activar, quién debe y dónde concentrar al corredor.", "Padrón y cuenta corriente del export de Producí. <b>Activo</b>: compró en los últimos 90 días. <b>Vencido</b>: saldo con más de 30 días. Los estados combinan color e ícono para que se distingan también en blanco y negro."))}
{kp}
<div class="mt">{legend}</div>
{grid}
{eyebrow("Los que más compran · volumen de 90 días", " " + src("erp"))}
{tabla}
{adv}
</section>'''


BENEF = {
    "Zona de obra": "la derivación va al distribuidor exacto",
    "Momento de obra": "se sabe quién compra este mes y quién en tres",
    "Cantidad de puertas": "se detecta quién llega a las 10 puertas del descuento",
    "Forma de pago": "la cobranza se anticipa antes del despacho",
    "Resultado de la visita": "el CRM mide su conversión real de visita a pedido",
    "Línea": "se arma el guion de venta cruzada",
}


def _vars(c):
    base, (weak, falta) = c[9], c[10]
    offs = [6, 10, -3, -7, -2, -5]
    vals = {}
    for v, o in zip(D.VARS_CORR, offs):
        vals[v] = max(min(base + o, 97), 100 - falta + 4)
    vals[weak] = 100 - falta
    return vals


def _heat(p):
    cls = "h4" if p >= 80 else ("h3" if p >= 60 else ("h2" if p >= 40 else "h1"))
    return f'<td class="heat {cls}">{p}%</td>'


def corredores():
    tv = sum(c[6] for c in D.CORR)
    to = sum(c[7] for c in D.CORR)
    tp = sum(c[5] for c in D.CORR)
    tc = sum(c[2] for c in D.CORR)
    tr = sum(c[8] for c in D.CORR)
    tconv = sum(c[3] for c in D.CORR)
    tvis = sum(c[4] for c in D.CORR)
    dprom = round(sum(c[9] for c in D.CORR) / len(D.CORR))
    kp = '<div class="g4">' + "".join([
        kpi("Ventas de los corredores", money(tv), delta("+7%"), f"{pct(tv, to)}% del objetivo de {money(to)}", "dollar", "grn", "erp"),
        kpi("Pedidos tomados", str(tp), delta("+8%"), f"de {D.PEDIDOS} pedidos del mes", "doc", "", "erp"),
        kpi("Recompra a 30 días", f"{pct(tr, tc)}%", delta("+1 p.p."), f"{tr} de {tc} distribuidores asignados", "repeat", "pnk", "erp"),
        kpi("Datos completos", f"{dprom}%", delta("+3 p.p."), "de las 6 variables clave, en sus conversaciones", "list", "blu", "pro",
            adv="Promedio de carga de zona, línea, cantidad, momento de obra, forma de pago y resultado de la visita."),
    ]) + "</div>"

    def estado(p):
        return est("ok", "En objetivo") if p >= 100 else (est("warn", "Cerca") if p >= 85 else est("bad", "Por debajo"))

    rows_b, rows_a = [], []
    for c in sorted(D.CORR, key=lambda c: -c[6] / c[7]):
        po = pct(c[6], c[7])
        rec = pct(c[8], c[2])
        colr = "var(--st-ok)" if po >= 100 else ("var(--st-warn)" if po >= 85 else "var(--st-bad)")
        rows_b.append([f'<b>{c[0]}</b><span class="sub">{c[1]}</span>', f"<b>${fmt(c[6], 1)} M</b>", f"{po}%{minibar(po, colr)}", str(c[5]), f"{c[8]} de {c[2]} · {rec}%", f'<td class="l">{estado(po)}</td>'])
        rows_a.append([f'<b>{c[0]}</b>', str(c[2]), str(c[3]), str(c[4]), str(c[5]), f"{pct(c[5], c[3])}", f"${fmt(c[6], 1)} M", f"{po}%", f"{rec}%",
                       _heat(c[9]), f"{c[11]} min", str(c[12])])
    rows_a.append(([f"<b>Total</b>", str(tc), fmt(tconv), str(tvis), str(tp), f"{pct(tp, tconv)}", money(tv), f"{pct(tv, to)}%", f"{pct(tr, tc)}%", _heat(dprom), "—", str(sum(c[12] for c in D.CORR))], "tr:tot"))
    t_b = table(["Corredor · zona", "Vendió", "% del objetivo", "Pedidos", "Recompraron a 30 días", '<span style="display:block;text-align:left">Estado</span>'], rows_b, 760)
    t_a = table(["Corredor", "Cartera", "Conversaciones", "Visitas marcadas", "Pedidos", "Pedidos c/100 conv.", "Ventas", "% objetivo", "Recompra 30d", "Datos completos", "Respuesta mediana", "Vencidos"], rows_a, 1100)
    gl = '<div class="glos"><div><b>Conversaciones</b>chats donde el corredor es moderador en Prometheo</div><div><b>Visitas marcadas</b>tag de visita cargado en el CRM</div><div><b>Pedidos c/100 conv.</b>pedidos ÷ conversaciones × 100</div><div><b>Respuesta mediana</b>minutos hasta la primera respuesta humana</div></div>'

    # scorecards
    cards = ""
    for c in D.CORR:
        po = pct(c[6], c[7])
        rec = pct(c[8], c[2])
        weak, falta = c[10]
        if po >= 100:
            fort = f"Superó el objetivo: <b>{po}%</b> ({money(c[6])} sobre {money(c[7])})."
        elif rec >= 65:
            fort = f"Recompra alta: <b>{c[8]} de {c[2]}</b> clientes volvieron a comprar en 30 días."
        elif c[9] >= 75:
            fort = f"Registra <b>{c[9]}%</b> de los datos clave en sus conversaciones."
        else:
            fort = f"Cartera de <b>{c[2]} distribuidores</b> con {c[5]} pedidos tomados en el mes."
        opp = f"Preguntar <b>«{weak.lower()}»</b> en la visita: hoy falta en el {falta}% de sus conversaciones. Con ese dato, {BENEF[weak]}."
        if c[4] / c[5] < 0.3:
            opp2 = f"Marcar la visita en el CRM: tomó <b>{c[5]} pedidos</b> y marcó <b>{c[4]} visitas</b>."
        else:
            opp2 = f"Sumar ventanas en la visita a los que compran solo puertas de su cartera."
        ws = c[0].replace("·", " ").split()
        ini = (ws[0][0] + ws[1][0]) if len(ws) > 1 else ws[0][:2]
        ini = ini.upper()
        colr = "var(--st-ok)" if po >= 100 else ("var(--st-warn)" if po >= 85 else "var(--st-bad)")
        rec_n, win = D.RECOMPRARON[c[0]]
        cards += f'''<div class="sc"><div class="sc-h"><div class="sc-av">{ini}</div><div><b>{c[0]}</b><span>{c[1]}</span></div>{estado(po)}</div>
<div class="sc-m"><div><div class="v">${fmt(c[6], 1)} M</div><div class="k">vendió</div></div><div><div class="v">{c[5]}</div><div class="k">pedidos</div></div><div><div class="v">{rec}%</div><div class="k">recompró a 30 días</div></div></div>
<div class="sc-obj" style="--tone:{colr}">{cmpbar(min(po * 0.8, 100), 80, "objetivo", f"{po}% del objetivo", f"objetivo {money(c[7])}")}</div>
<div class="sc-p"><span class="pi pi-good">{ic("check")}</span><div><span class="k">Fortaleza</span>{fort}</div></div>
<div class="sc-p"><span class="pi pi-up">{ic("upr")}</span><div><span class="k">Para crecer</span>{opp}</div></div>
<div class="adv"><div class="sc-p"><span class="pi pi-up">{ic("route")}</span><div><span class="k">También</span>{opp2}</div></div>
<div class="sc-p"><span class="pi pi-good">{ic("repeat")}</span><div><span class="k">Recompraron en 30 días</span>{", ".join(rec_n)}</div></div>
<div class="sc-p"><span class="pi" style="background:var(--warn-bg);color:var(--warn)">{ic("clock")}</span><div><span class="k">En ventana, sin pedido todavía</span>{", ".join(win)}</div></div>
<div class="sc-m" style="border-bottom:none"><div><div class="v">{c[3]}</div><div class="k">conversaciones</div></div><div><div class="v">{c[4]}</div><div class="k">visitas marcadas</div></div><div><div class="v">{c[11]} min</div><div class="k">respuesta mediana</div></div></div></div>
</div>'''

    # heatmap de variables
    hrows = []
    for c in D.CORR:
        v = _vars(c)
        hrows.append([f"<b>{c[0]}</b>"] + [_heat(v[k]) for k in D.VARS_CORR] + [f'{c[10][0]}'])
    heat = table(["Corredor"] + D.VARS_CORR + ["Para sumar primero"], hrows, 900)

    insights = f'''<div class="igrid">
{i3("replicar", "Mandar la lista de precios por WhatsApp antes de la visita: recompra 71% contra 55%",
    [("Segmento", "5 corredores que lo hacen · 207 clientes"), ("Fuente", "Conversaciones del moderador + pedidos"), ("Base", "451 distribuidores asignados")],
    ["AMBA Norte, AMBA Oeste, Centro, Norte y Comahue envían la lista el día anterior a la visita.",
     "Sus clientes llegan con el pedido pensado: <b>146 de 207</b> recompraron en 30 días.",
     "En el resto de la red, <b>134 de 244</b>. La diferencia no es la zona: es la preparación."],
    "71%", "de los clientes de quienes envían la lista recompró en 30 días. En el resto, 55 de cada 100.",
    cmpbar(71, 55, "resto 55%", "con lista previa", "corredores que no la envían"), own("ven"), lab3="Resultado contra el resto de la red")}
{i3("ruta", "Visitar cada 7 días a los 100 que más compran: recompra 78% contra 49%",
    [("Segmento", "Top 100 por volumen"), ("Fuente", "Pedidos de Producí + visitas marcadas"), ("Base", "100 distribuidores · 68% de la venta")],
    ["Los que reciben visita semanal reponen antes de quedarse sin stock.",
     "Con visita cada 15 días o más, la recompra a 30 días cae a <b>49%</b>.",
     "Son 7 de cada 10 pesos de venta: la ruta se arma empezando por ellos."],
    "78%", "de los top 100 con visita semanal recompró en 30 días. Con visita cada 15 días o más: 49%.",
    cmpbar(78, 49, "cada 15 días 49%", "visita semanal", "visita cada 15 días o más"), own("ven"), lab3="Resultado contra el resto de la red")}
{i3("subir", "Ofrecer ventanas en la misma visita sube el pedido 22%",
    [("Segmento", "Clientes que compran solo puertas"), ("Fuente", "Pedidos de Producí"), ("Base", f"{D.SOLO_PUERTAS} distribuidores")],
    ["4 de 12 corredores ofrecen ventanas cuando toman un pedido de puertas.",
     "Cuando el pedido suma ventanas, el ticket pasa de <b>$192.000 a $234.000</b>.",
     f"Hay <b>{D.SOLO_PUERTAS}</b> distribuidores que nunca compraron ventanas."],
    "+22%", "de ticket cuando el pedido suma ventanas.",
    cmpbar(100, 82, "pedido solo puertas", "con ventanas · $234.000", "solo puertas · $192.000"), own("ven"), lab3="Resultado contra el pedido habitual")}
{i3("asignar", f"{D.SIN_CORREDOR} distribuidores activos no tienen corredor asignado",
    [("Segmento", "Activos sin moderador en Prometheo"), ("Fuente", "Campo moderador + padrón"), ("Base", "500 activos")],
    ["Cuando escriben, nadie recibe la notificación: responde el agente y no hay seguimiento humano.",
     "Recompran a 30 días al <b>31%</b>, la mitad que el resto de la red.",
     "Asignarlos por zona reparte 4 clientes más por corredor."],
    "31%", "recompra a 30 días de los activos sin corredor. Con corredor: 62%.",
    cmpbar(31, 62, "con corredor 62%", "sin corredor", "con corredor asignado"), own("ven"), lab3="Resultado contra el resto de la red")}
{i3("replicar", "Los que registran 8 de cada 10 datos llegan al objetivo",
    [("Segmento", "5 corredores con datos completos ≥ 80%"), ("Fuente", "Variables de sus conversaciones"), ("Base", "12 corredores")],
    ["Con zona, cantidad y momento de obra cargados, el corredor sabe a quién visitar primero.",
     "Los que registran el 80% o más llegan al <b>109%</b> del objetivo en promedio.",
     "Los que registran menos del 60% llegan al <b>70%</b>: el dato faltante es tiempo de ruta perdido."],
    "109%", "del objetivo en promedio para quienes registran 8 de cada 10 datos. Los que registran menos de 6: 70%.",
    cmpbar(87, 56, "menos de 6 datos · 70%", "8 o más datos · 109%", "menos de 6 de cada 10 datos"), own("aurea"), lab3="Resultado contra el resto de la red")}
{i3("ruta", "Cuyo y NEA: visita mensual más WhatsApp de recompra cada 10 días",
    [("Corredor", "Cuyo y NEA"), ("Zona", "Mendoza, San Juan, Chaco, Corrientes, Misiones"), ("Cartera", "64 distribuidores")],
    ["Por distancia, visitan una vez por mes a clientes que compran cada 10 días.",
     "Entre visitas no hay contacto: la recompra cae a <b>42%</b>.",
     "Un WhatsApp de recompra desde el CRM cubre los días sin visita sin sumar viajes."],
    "42%", "recompra a 30 días en Cuyo y NEA. Promedio de la red: 62%.",
    cmpbar(42, 62, "red 62%", "Cuyo y NEA", "promedio de la red"), own("mkt"), lab3="Resultado contra el resto de la red")}
</div>'''

    return f'''<section class="panel p-corredores">
{sec_head("Corredores · 12 vendedores en la calle", "Cuánto vendió cada corredor, <em>y dónde puede crecer.</em>",
          "Cada corredor es un <b>moderador</b> en Prometheo: sus conversaciones, lo que registró y lo que quedó sin preguntar salen del CRM; pedidos y ventas, del export de Producí. La lectura es para mejorar la gestión, no para comparar personas.")}
{kp}
{eyebrow("Ranking del mes · ventas contra objetivo")}
<div class="bsc">{t_b}</div>
<div class="adv">{t_a}{gl}</div>
{eyebrow("Cada corredor · fortaleza y oportunidad", ' <span class="lvl l-est">' + ic("info") + 'en Avanzado: quiénes recompraron y quiénes están en ventana</span>')}
<div class="scgrid">{cards}</div>
{eyebrow("Recompra a 30 días · lo que hacen los que mejor venden")}
{insights}
<div class="adv">{eyebrow("Dónde cada corredor puede sumar información · % de conversaciones con el dato cargado", " " + src("pro"))}
{heat}
<div class="estlegend mt"><span class="chip"><i style="width:10px;height:10px;border-radius:3px;background:var(--good-bg);display:inline-block"></i>80% o más</span><span class="chip"><i style="width:10px;height:10px;border-radius:3px;background:var(--blu-soft);display:inline-block"></i>60 a 79%</span><span class="chip"><i style="width:10px;height:10px;border-radius:3px;background:var(--warn-bg);display:inline-block"></i>40 a 59%</span><span class="chip"><i style="width:10px;height:10px;border-radius:3px;background:var(--crit-bg);display:inline-block"></i>menos de 40%</span></div></div>
</section>'''
