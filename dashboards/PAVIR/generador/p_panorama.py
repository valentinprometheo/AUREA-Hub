"""Panorama y Evolución: ¿cómo venimos?"""
from icons import ic
from comp import (fmt, pct, money, src, lvl, own, chip, delta, sec_head, eyebrow, ghdr, banner, kpi, bar, bars,
                  vcard, table, bsc_adv, minibar, mincard, ul)
from charts import area_hero, bars_month, spark
import data as D


def spark_hero():
    v = D.H_PED
    mx, mn = max(v), min(v)
    pts = [(4 + i * 292 / (len(v) - 1), 54 - (x - mn) / (mx - mn) * 46) for i, x in enumerate(v)]
    p = " ".join(f"{a:.0f},{b:.0f}" for a, b in pts)
    lx, ly = pts[-1]
    return (f'<polyline points="{p}" fill="none" stroke="rgba(255,255,255,.85)" stroke-width="2" vector-effect="non-scaling-stroke" stroke-linejoin="round"/>'
            f'<circle cx="{lx:.0f}" cy="{ly:.0f}" r="3.5" fill="#fff"/>')


def panorama():
    chart, ly = area_hero(D.H_DEUDA)
    top_pct = max(min(ly * 100 - 12, 70), 2)
    hero = f'''
<div class="hero-grid">
  <div class="hero">
    <div class="hero-sph sph-bg"></div>
    <div class="hero-top"><span class="hero-kick">Panorama · {D.PERIODO}</span><span class="hero-per">comparado con {D.PREV}</span></div>
    <div class="hero-h">Septiembre: más pedidos y menos deuda en calle.</div>
    <div class="hero-sub">{bsc_adv(
        f"Se tomaron <b>{D.PEDIDOS} pedidos</b> (+9% contra agosto) y se vendieron <b>{money(D.VENTAS_M)}</b>. La deuda que los distribuidores todavía no pagaron bajó 4% y queda en <b>{money(D.DEUDA_M)}</b>.",
        f"<b>{D.PEDIDOS} pedidos</b> (+9% m/m) por <b>{money(D.VENTAS_M)}</b>; ticket promedio $192.000. Cuentas por cobrar <b>{money(D.DEUDA_M)}</b> (−4% m/m), de las cuales {money(D.VENCIDO_M)} vencidas a +30 días.")}</div>
    <div class="chart-scale"><span>Deuda en calle · máx $61,4 M en marzo</span><span>menos es mejor ↓</span></div>
    <div class="hchart">{chart}<div class="endtag" style="top:calc({top_pct:.0f}% - 4px)">{money(D.DEUDA_M)}<span>septiembre</span></div></div>
    <div class="chart-x"><span>oct</span><span>dic</span><span>feb</span><span>abr</span><span>jun</span><span>sep</span></div>
    <div class="hero-stats">
      <div class="hs"><div class="l">Distribuidores activos</div><div class="v">{D.ACTIVOS}</div><div class="m">de {D.RED} · {D.PROV_ACT} provincias</div></div>
      <div class="hs"><div class="l">Consultas por día</div><div class="v">165</div><div class="m">{fmt(D.CONSULTAS)} en el mes</div></div>
      <div class="hs"><div class="l">Deuda en calle</div><div class="v">{money(D.DEUDA_M)}</div><div class="m">{D.CON_DEUDA} distribuidores</div></div>
    </div>
  </div>
  <div class="hero-pink">
    <div class="hp-top">
      <div class="hp-row"><div class="hp-ic">{ic("truck")}</div><span class="hp-chip">12 corredores en la calle</span></div>
      <svg class="hp-spk" viewBox="0 0 300 60" preserveAspectRatio="none">{spark_hero()}</svg>
      <div><div class="hp-l">Pedidos del mes</div><div class="hp-v">{D.PEDIDOS}</div>
      <div class="hp-d"><span class="pin">▲ +9%</span> 352 los tomó un corredor · 32 llegaron directo</div></div>
    </div>
    <div class="hp-foot">
      <div class="mini"><b>{D.COBRADOS}</b><span>Cobrados</span></div><div class="hp-sp"></div>
      <div class="mini"><b>{D.DESPACHADOS}</b><span>Despachados</span></div><div class="hp-sp"></div>
      <div class="mini"><b style="color:var(--crit)">{D.VENCIDOS}</b><span>Vencidos +30d</span></div>
    </div>
  </div>
</div>'''

    kp = '<div class="g4">' + "".join([
        kpi("Ventas del mes", money(D.VENTAS_M), delta("+8%"), bsc_adv("Lo facturado a la red en septiembre.", "Facturado a distribuidores · 384 pedidos · ticket $192.000."), "dollar", "grn", "erp",
            adv="<b>Ticket promedio</b>: ventas ÷ pedidos. Agosto: $194.000."),
        kpi("Consultas", fmt(D.CONSULTAS), delta("+6%"), bsc_adv("Personas que escribieron por WhatsApp, Instagram o mail.", "Conversaciones nuevas en Prometheo · 165/día · 81% respondió al agente."), "chat", "blu", "pro",
            adv="Una consulta = un contacto nuevo o que vuelve a escribir después de 30 días."),
        kpi("Consultas calificadas", fmt(D.CALIFICADA), delta("+6%"), bsc_adv("58 de cada 100 dijeron qué producto, dónde y cuánto.", "58% sobre el total · 78% sobre la base curada (sin posventa ni proveedores)."), "checkc", "", "pro",
            adv="<b>Calificada</b>: tipo de contacto + línea + zona + cantidad o momento de obra."),
        kpi("Deuda en calle", money(D.DEUDA_M), delta("−4%", "good", "down"), bsc_adv("Lo que la red todavía debe. Menos es mejor.", "Cuentas por cobrar · 84 distribuidores · $11,9 M vencido +30d."), "clock", "pnk", "erp",
            adv="<b>Cuentas por cobrar</b>: saldo de cuenta corriente al cierre del mes."),
    ]) + "</div>"

    # origen de la demanda: inbound / outbound
    grupos = {}
    for g, c, v, s in D.INBOUND:
        grupos.setdefault(g, []).append((c, v, s))
    cols = {"Pago": "var(--src-meta)", "Orgánico": "var(--vio)", "Directo": "var(--pnk)"}
    mk = ""
    for g, rows in grupos.items():
        mx = max(v for _, v, _ in rows) or 1
        rr = ""
        for c, v, s in rows:
            st = {"on": '<span class="stc sc-on">Activa</span>', "off": '<span class="stc sc-off">Pausada</span>', "miss": '<span class="stc sc-off">Faltante</span>', "": ""}[s]
            extra = "oportunidad" if v == 0 else f"{pct(v, D.CONSULTAS)}%"
            rr += bar(c + st, fmt(v), 100 * v / max(mx, 1), extra, cols[g], "miss" if s == "miss" else "")
        mk += f'<div><div class="subl"><span class="dot2" style="background:{cols[g]}"></span>{g}</div>{rr}</div>'
    inbound = f'''<div class="card pad">
  <div class="io-h"><div class="io-ic" style="background:var(--grad)">{ic("inb")}</div><div><b>Inbound · el cliente escribe primero</b><span>Consultas que llegaron solas, según de dónde vinieron</span></div>
  <div class="tot"><b>{fmt(D.CONSULTAS)}</b><span>consultas</span></div></div>
  <div class="mkgrid">{mk}</div>
  <div class="note">{bsc_adv("Marketing trae a la persona hasta el clic. Desde ahí, el agente de Prometheo conversa, califica y deriva al distribuidor de la zona.",
      "Atribución por ID de anuncio para Meta; el resto por canal de entrada declarado. <b>225 consultas (5%) no tienen origen</b>: es un faltante estructural (boca a boca, contacto guardado), no un error de carga.")}</div>
</div>'''
    outbound = f'''<div class="card pad">
  <div class="io-h"><div class="io-ic" style="background:var(--src-wpp)">{ic("outb")}</div><div><b>Outbound · PAVIR escribe primero</b><span>Campañas a la base propia y visitas</span></div>
  <div class="tot"><b>3</b><span>canales</span></div></div>
  <div class="mkgrid two">
    <div><div class="subl"><span class="dot2" style="background:var(--src-wpp)"></span>WhatsApp Marketing <span class="stc sc-on">Iniciado</span></div>
      {bar("Enviados", "150", 100, "", "var(--src-wpp)")}{bar("Respondieron", "47", 31, "33%", "var(--src-wpp)")}{bar("Pedidos", "9", 6, "", "var(--src-wpp)")}</div>
    <div><div class="subl"><span class="dot2" style="background:var(--src-mail)"></span>Email Marketing <span class="stc sc-on">Iniciado</span></div>
      {bar("Enviados", "200", 100, "", "var(--src-mail)")}{bar("Clic o respuesta", "34", 17, "18%", "var(--src-mail)")}{bar("Pedidos", "6", 3, "", "var(--src-mail)")}</div>
  </div>
  <div style="margin-top:14px"><div class="subl"><span class="dot2" style="background:var(--warn)"></span>Visita de corredor</div>
    {bar("Pedidos tomados en la visita", "352", 92, "92% de los pedidos", "var(--warn)")}</div>
  <div class="obase">{chip("Padrón de clientes · 700", "ledger")}{chip("Feria BATEV · 320", "badge")}{chip("Scraping de corralones · 220", "globe")}</div>
</div>'''

    rec = [
        ("01", "chat", fmt(D.CONSULTAS), "Consultas", "del mes", "sm", ""),
        ("02", "checkc", fmt(D.CALIFICADA), "Calificadas", "58% de las consultas", "", ""),
        ("03", "arrow", fmt(D.DERIVADA), "Derivadas", "al distribuidor o corredor", "sm", ""),
        ("04", "lock", "?", "Qué consulta compró", "hoy no se registra", "", "cut"),
        ("05", "doc", str(D.PEDIDOS), "Pedidos", "89% se cobró", "", ""),
        ("06", "repeat", f"{D.RECOMPRA}%", "Recompra 30 días", "le vuelve a comprar", "sm", ""),
    ]
    rr = "".join(f'<div class="rec {cut}"><div class="rs">{ic(i)}{n}</div><div class="n {"grad-txt" if n == "01" else ""}">{v}</div><div class="l">{l}</div><span class="c {c}">{s}</span></div>'
                 for n, i, v, l, s, c, cut in rec)
    recorrido = f'''<div class="card pad">{ghdr("Del contacto al pedido · el recorrido completo", "route", "Marketing ve hasta el clic · Prometheo, del clic a la derivación")}
<div class="recorrido">{rr}</div>
<div class="note">{bsc_adv("El paso 04 está vacío: hoy se sabe cuántas consultas entran y cuántos pedidos se cargan, pero no <b>qué consulta terminó en pedido</b>. Es lo primero que resuelve el CRM bien cargado (ver Venta · CRM).",
    "Pasos 01 a 03 salen de Prometheo; 05 y 06, del export de Producí. El vínculo consulta → pedido no existe: <b>0 consultas con tag de pedido</b> y 214 con evidencia de compra en la conversación. Ver Venta · CRM › Cómo mejorar el CRM.")}</div></div>'''

    decs = [
        ("var(--crit)", "dollar", "Cobrar", own("cob"),
         f"<b>{D.VENCIDOS} distribuidores</b> tienen deuda vencida hace más de 30 días: <b>{money(D.VENCIDO_M)}</b> de los {money(D.DEUDA_M)} en calle.",
         "Enviar el estado de cuenta y cobrar antes de despachar el próximo pedido. El corredor de la zona lo lleva en la visita."),
        ("var(--vio)", "refresh", "Seguir", own("ven"),
         f"<b>{fmt(D.FUGA)} consultas calificadas</b> se derivaron y nadie volvió a escribir: ya dijeron qué producto, dónde y cuánto.",
         f"Activar el seguimiento automático a las 48 h de la derivación y avisar al corredor. <b>{D.FUGA_EDAD[0][1]}</b> son de esta semana."),
        ("var(--blu)", "pin", "Visitar", own("ven"),
         f"<b>{D.TOCA_COMPRAR} distribuidores</b> entraron en su ventana de recompra (compran cada 7 a 10 días) y todavía no pidieron.",
         f"Ponerlos primero en la ruta del corredor y ofrecer ventanas a los <b>{D.SOLO_PUERTAS}</b> que hoy compran solo puertas."),
    ]
    dd = "".join(f'''<div class="dec-item" style="--dc:{c}"><div class="dec-h"><div class="dec-ic">{ic(i)}</div><b>{t}</b>{o}</div>
<div class="dec-p"><span class="pi">{ic("eye")}</span><div><span class="k">Qué pasa</span>{a}</div></div>
<div class="dec-p"><span class="pi">{ic("arrow")}</span><div><span class="k">Qué hacer</span>{b}</div></div></div>''' for c, i, t, o, a, b in decs)

    adv = f'''<div class="adv">{eyebrow("Métricas de gestión · modo avanzado")}
<div class="g4">
{kpi("Derivadas", fmt(D.DERIVADA), delta("+6%"), "53% de las consultas · 92% de las calificadas", "arrow", "blu", "pro")}
{kpi("Dormidos +45 días", str(D.DORMIDOS), delta("+5", "bad", "up"), "Activos sin pedido hace más de 45 días", "hourglass", "amb", "erp")}
{kpi("En ventana de recompra", str(D.TOCA_COMPRAR), delta("le toca", "flat", None), "Compran cada 7 a 10 días y no pidieron", "repeat", "", "erp")}
{kpi("Costo por consulta calificada", "$794", delta("−6%", "good", "down"), "Meta Ads · $520.000 ÷ 655 calificadas", "sigma", "pnk", "calc", adv="<b>Calif.</b> = consulta calificada en Prometheo. Menos es mejor.")}
</div></div>'''

    return f'''<section class="panel p-panorama">
<div class="iobar"><button class="iobtn primary">{ic("inb")}Exportar reporte del mes</button><span class="iohint">Consolidado de Prometheo, export de Producí y canales</span></div>
{hero}{kp}
{eyebrow("Origen de la demanda · inbound y outbound")}
<div class="inout">{inbound}{outbound}</div>
{adv}
{eyebrow("Recorrido · del contacto al pedido")}
{recorrido}
{eyebrow("Qué hago ahora · tres decisiones con dueño")}
<div class="dec">{dd}</div>
</section>'''


def evolucion():
    M = D.MESES
    last = len(M) - 1
    t_ventas = bars_month(M, [D.H_VENT], ["var(--vio)"], lambda v: f"${fmt(v)}M" if v else "0", line=D.H_OBJ)
    rows = []
    for i in range(len(M)):
        tick = D.H_VENT[i] * 1e6 / D.H_PED[i]
        rows.append([f"<b>{M[i]}</b>", f"${fmt(D.H_VENT[i], 1)} M", fmt(D.H_PED[i]), f"${fmt(tick / 1000)} mil", f"{D.H_REC[i]}%",
                     f"{pct(D.H_VENT[i], D.H_OBJ[i])}%{minibar(pct(D.H_VENT[i], D.H_OBJ[i]), 'var(--good)' if D.H_VENT[i] >= D.H_OBJ[i] else 'var(--warn)')}"])
    rows[-1] = (rows[-1], "tr:tot")
    ventas = f'''<div class="stab st-ventas">
<div class="g4">
{kpi("Ventas del mes", money(D.VENTAS_M), delta("+8%"), "contra $68,4 M de agosto", "dollar", "grn", "erp")}
{kpi("Pedidos", str(D.PEDIDOS), delta("+9%"), "352 por corredor · 32 directos", "doc", "", "erp")}
{kpi("Ticket promedio", "$192 mil", delta("−1%", "bad", "down"), "ventas ÷ pedidos", "sigma", "blu", "calc")}
{kpi("Recompra a 30 días", f"{D.RECOMPRA}%", delta("+1 p.p."), "de la red activa volvió a comprar", "repeat", "pnk", "erp", adv="<b>p.p.</b> = puntos porcentuales.")}
</div>
<div class="card pad mt">{ghdr("Ventas por mes · 12 meses", "trend", "barras: ventas · línea punteada: objetivo del mes", src("erp"))}{t_ventas}
<div class="chart-lg"><span><i style="background:var(--vio)"></i>Ventas del mes (millones)</span><span><i style="background:none;border-top:2px dashed var(--ink);height:0;width:16px;border-radius:0"></i>Objetivo comercial</span><span>Pico mar-may · piso dic-feb</span></div></div>
<div class="mt">{table(["Mes", "Ventas", "Pedidos", "Ticket promedio", "Recompra 30d", "% del objetivo"], rows, 640)}</div>
<div class="adv mt">{vcard("Ventas por línea · mes a mes (millones)", bars_month(M, list(D.H_LINEA.values()), ["var(--vio)", "var(--blu)", "var(--pnk)"], lambda v: f"${fmt(v)}M") +
    '<div class="chart-lg"><span><i style="background:var(--vio)"></i>Puertas de acero 61%</span><span><i style="background:var(--blu)"></i>Ventanas 24%</span><span><i style="background:var(--pnk)"></i>Pivotantes 15%</span></div>', "box", "septiembre", src("erp"))}</div>
</div>'''

    t_deuda = bars_month(M, [[D.H_DEUDA[i] - D.H_VENC[i] for i in range(len(M))], D.H_VENC], ["var(--blu)", "var(--crit)"], lambda v: f"${fmt(v)}M")
    drows = []
    for i in range(len(M)):
        dso = D.H_DEUDA[i] / (D.H_VENT[i] / 30)
        drows.append([f"<b>{M[i]}</b>", f"${fmt(D.H_DEUDA[i], 1)} M", f"${fmt(D.H_DEUDA[i] - D.H_VENC[i], 1)} M", f"${fmt(D.H_VENC[i], 1)} M",
                      str(D.H_CDEU[i]), str(D.H_NVENC[i]), f"{D.H_TERM[i]}%", f"{fmt(dso)} días"])
    drows[-1] = (drows[-1], "tr:tot")
    deuda = f'''<div class="stab st-deuda">
<div class="g4">
{kpi("Cuentas por cobrar", money(D.DEUDA_M), delta("−4%", "good", "down"), "saldo de cuenta corriente · menos es mejor", "clock", "pnk", "erp")}
{kpi("Vencido a más de 30 días", money(D.VENCIDO_M), delta("−6%", "good", "down"), f"{D.VENCIDOS} distribuidores · frena el despacho", "alert", "amb", "erp")}
{kpi("Cobranza en término", "88%", delta("+1 p.p."), "pagó dentro de los 30 días", "checkc", "grn", "erp")}
{kpi("Días promedio de cobro", "17", delta("−3 días", "good", "down"), "cuántos días de venta están en la calle", "cal", "blu", "calc", adv="Saldo ÷ (ventas del mes ÷ 30). En la jerga: <b>DSO</b> (days sales outstanding).")}
</div>
<div class="g3 mt">
  <div class="vcard">{ghdr("La distinción de PAVIR", "filter", "", src("erp"))}
    <div class="estlegend" style="margin-bottom:10px"><span class="est ok">{ic("check")}Sin deuda</span><span class="est warn">{ic("clock")}Con deuda al día</span><span class="est bad">{ic("alert")}Vencido +30d</span></div>
    {bar("Sin deuda · se despacha apenas pide", fmt(D.SIN_DEUDA), 100, "88%", "var(--st-ok)")}
    {bar("Con deuda dentro de los 30 días", str(D.DEUDA_AL_DIA), 8.6, "8%", "var(--st-warn)")}
    {bar("Vencido a más de 30 días · cobra antes", str(D.VENCIDOS), 5, "4%", "var(--st-bad)")}
    <div class="note">Regla comercial: <b>sin deuda</b> se consulta disponibilidad y se despacha; <b>con deuda vencida</b> se envía estado de cuenta y se cobra antes de despachar.</div></div>
  <div class="card pad span2">{ghdr("Cuentas por cobrar por mes", "trend", "menos es mejor", src("erp"))}{t_deuda}
  <div class="chart-lg"><span><i style="background:var(--blu)"></i>Dentro de los 30 días</span><span><i style="background:var(--crit)"></i>Vencido a más de 30 días</span></div></div>
</div>
<div class="mt">{table(["Mes", "Saldo total", "Al día", "Vencido +30d", "Dist. con deuda", "Dist. vencidos", "Cobranza en término", "Días de cobro"], drows, 760)}</div>
</div>'''

    trs = ""
    for nm, kind, desc, tags in D.EMBUDOS:
        k = {"auto": '<span class="stc sc-on">Automático</span>', "man": '<span class="stc sc-off">Manual</span>', "none": '<span class="stc sc-new">Sin embudo propio</span>'}[kind]
        trs += f'<tr><td class="cj l" colspan="7">{nm} {k}<span class="sub">{desc}</span></td></tr>'
        for t, v in tags:
            d = v[-1] - v[-2]
            dd = f'<span class="delta {"d-good" if d > 0 else ("d-bad" if d < 0 else "d-flat")}">{"+" if d > 0 else ""}{fmt(d)}</span>'
            trs += f'<tr><td class="l"><code>{t}</code></td>' + "".join(f"<td>{fmt(x)}</td>" for x in v) + f"<td>{dd}</td><td>{spark(v, {'auto': 'var(--vio)', 'man': 'var(--warn)', 'none': 'var(--ink4)'}[kind])}</td></tr>"
    tags = f'''<div class="stab st-tags">
{banner("info", "tag", "Los tags más usados mes a mes, separados por embudo. El embudo del agente se carga solo; los embudos del equipo dependen de que alguien los marque. Por eso <b>Seguimiento y venta</b> casi no se mueve aunque las ventas sí.")}
<div class="card mt" style="overflow:hidden"><div class="tblwrap"><table style="min-width:720px"><thead><tr><th>Tag</th><th>jun</th><th>jul</th><th>ago</th><th>sep</th><th>vs ago</th><th>Tendencia</th></tr></thead><tbody>{trs}</tbody></table></div></div>
</div>'''

    crows = [[f"<b>{M[i]}</b>", fmt(D.H_CONS[i]), fmt(D.H_CALIF[i]), f"{pct(D.H_CALIF[i], D.H_CONS[i])}%", fmt(D.H_DERIV[i]), fmt(D.H_PED[i])] for i in range(len(M))]
    crows[-1] = (crows[-1], "tr:tot")
    cons = f'''<div class="stab st-cons">
<div class="card pad">{ghdr("Consultas y calificadas por mes", "chat", "", src("pro"))}{bars_month(M, [D.H_CALIF, [D.H_CONS[i] - D.H_CALIF[i] for i in range(len(M))]], ["var(--vio)", "var(--blu-soft)"], lambda v: fmt(v))}
<div class="chart-lg"><span><i style="background:var(--vio)"></i>Calificadas</span><span><i style="background:var(--blu-soft);border:1px solid var(--line)"></i>Resto de las consultas</span></div></div>
<div class="mt">{table(["Mes", "Consultas", "Calificadas", "% calificada", "Derivadas", "Pedidos (Producí)"], crows, 600)}</div>
</div>'''

    adv = f'''<div class="adv">{eyebrow("Qué cambia con el CRM bien cargado · modo avanzado", " " + lvl("proy"))}
<div class="g4">
{kpi("Consulta → pedido", "0% → medible", "", "Hoy no se vincula; con el tag de pedido, sí", "lock", "", "calc")}
{kpi("Seguimiento a 48 h", "34% → 60%", "", "Objetivo con seguimiento automático", "refresh", "blu", "calc")}
{kpi("Recompra a 30 días", "62% → 75%", "", "Objetivo con alerta de ventana", "repeat", "pnk", "calc")}
{kpi("Vencido +30d", "$11,9 M → $8 M", "", "Objetivo con estado de cuenta automático", "dollar", "grn", "calc")}
</div></div>'''

    return f'''<section class="panel p-evolucion">
{sec_head("Evolución · mes a mes", "Ventas, cobranza y uso del CRM, <em>mes a mes.</em>", ("Primero lo que más importa: <b>cuánto se vendió</b> y <b>cuánto falta cobrar</b>. Después, cómo se movieron los tags de cada embudo y las consultas.", "Ventas y pedidos del export de Producí; <b>cuentas por cobrar</b> con la distinción al día / vencido +30 días y <b>días promedio de cobro</b> (DSO). Tags por embudo con variación mensual y separación automático / manual. 12 meses, cierre al 30 de septiembre."))}
<div class="subtabs evtabs"><label for="ev-ventas">{ic("dollar")}Ventas</label><label for="ev-deuda">{ic("clock")}Cuentas por cobrar</label><label for="ev-tags">{ic("tag")}Tags por embudo</label><label for="ev-cons">{ic("chat")}Consultas</label></div>
{ventas}{deuda}{tags}{cons}
{adv}
</section>'''
