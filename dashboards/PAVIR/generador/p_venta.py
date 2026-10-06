"""Venta · CRM (con el subsector "Cómo mejorar el CRM")."""
from icons import ic
from comp import (fmt, pct, money, src, lvl, own, chip, delta, sec_head, eyebrow, ghdr, banner, kpi, bar, bars,
                  vcard, table, bsc_adv, minibar, mincard, ul, i3, kv, cmpbar, fsteps)
from charts import donut
import data as D


def _stage(color, icon, title, sub, qty, unit, rows, act):
    rr = "".join(f'<div class="rowl"><span class="k">{ic(i)}{k}</span><span class="v">{v}</span></div>' for i, k, v in rows)
    return (f'<div class="stage" style="--stc:{color}"><div class="sh"><div class="dec-ic">{ic(icon)}</div><h4>{title}</h4></div>'
            f'<div class="ssub">{sub}</div><div class="qty">{qty} <small>{unit}</small></div>{rr}'
            f'<div class="act">{ic("arrow")}<div>{act}</div></div></div>')


def _key(color, icon, kicker, title, text, stats, adv_html="", adv_title=""):
    st = "".join(f'<div><div class="v">{v}</div><div class="k">{k}</div></div>' for v, k in stats)
    adv = f'<div class="key-adv adv"><h5>{ic("sliders")}{adv_title}</h5>{adv_html}</div>' if adv_html else ""
    return (f'<div class="key" style="--kc:{color}"><div class="key-h"><div class="key-ic">{ic(icon)}</div><div style="min-width:0">'
            f'<div class="key-k">{kicker}</div><div class="key-t">{title}</div><div class="key-s">{text}</div></div></div>'
            f'<div class="key-stats" style="--n:{len(stats)}">{st}</div>{adv}</div>')


def _bars_simple(rows, color="var(--vio)"):
    tot = sum(v for _, v in rows)
    mx = max(v for _, v in rows)
    return "".join(bar(l, fmt(v), 100 * v / mx, f"{pct(v, tot)}%", color) for l, v in rows)


def ventacrm():
    colas = f'''<div class="g3">
{_stage("var(--crit)", "dollar", "A cobrar", "Deuda vencida que frena el próximo despacho", D.VENCIDOS, "distribuidores",
        [("dollar", "Vencido +30 días", money(D.VENCIDO_M)), ("alert", "Con deuda total", f"{D.CON_DEUDA} dist.")],
        "Enviar <b>estado de cuenta</b> y cobrar (transferencia, e-cheq o efectivo) antes de despachar.")}
{_stage("var(--vio)", "repeat", "Le toca comprar", "Entraron en su ventana de recompra", D.TOCA_COMPRAR, "distribuidores",
        [("clock", "Compran cada", "7 a 10 días"), ("box", "Compran solo puertas", f"{D.SOLO_PUERTAS} dist.")],
        "Priorizar la <b>visita del corredor</b> y ofrecer ventanas en el mismo pedido.")}
{_stage("var(--warn)", "hourglass", "Sin comprar +45 días", "Activos que dejaron de pedir", D.DORMIDOS, "distribuidores",
        [("pin", "En el Interior", "41 dist."), ("users", "Pasivos reactivables", f"{D.PASIVOS} dist.")],
        "Difusión por WhatsApp con <b>novedad de temporada</b> y coeficiente vigente.")}
</div>'''

    F = [("Entró", D.CONSULTAS), ("Respondió al agente", D.RESPONDIO), ("Dijo línea y zona", D.IDENTIFICO),
         ("Calificada", D.CALIFICADA), ("Derivada", D.DERIVADA), ("Con seguimiento", D.SEGUIMIENTO), ("Pedido confirmado", D.PEDIDO_TAG)]
    steps = []
    for i, (l, v) in enumerate(F):
        p = pct(v, D.CONSULTAS)
        if i == 0:
            ps, cls = "base", ""
        elif l == "Pedido confirmado":
            ps, cls = f"0 con tag · {D.PEDIDO_EVID} por evidencia", "dim"
        else:
            pp = pct(v, F[i - 1][1])
            ps, cls = f"pasa {pp}%", ("leak" if pp < 50 else "")
        val = f"<b>{fmt(v)}</b> contactos" if l != "Pedido confirmado" else f"<b>{D.PEDIDO_EVID}</b> por evidencia"
        steps.append(dict(num=f"0{i + 1}", pt=f"{p}%", label=l, val=val, w=max(p, 2), **{"pass": ps}, cls=cls))
    embudo = f'''<div class="card pad">{ghdr("El embudo de consultas, paso a paso", "filter", f"% sobre las {fmt(D.CONSULTAS)} consultas · y cuánto pasa de un paso al siguiente", src("pro"))}
{fsteps(steps)}
<div class="note">{bsc_adv("El paso marcado en rojo es donde más se pierde: después de derivar, casi nadie vuelve a escribir.",
   "<b>Calificada</b>: tipo de contacto + línea + zona + cantidad o momento de obra. <b>Con seguimiento</b>: hay una acción acordada con fecha (visita, entrega o pedido). <b>Pedido confirmado</b> se muestra con dos lecturas: tag cargado y evidencia en la conversación.")}</div></div>'''

    # ---------- cuello de botella (card aislada) ----------
    dg = "".join([
        vcard("Qué pidieron", _bars_simple(D.FUGA_LINEA), "box", "base: 1.980"),
        vcard("Quiénes son", _bars_simple(D.FUGA_TIPO, "var(--blu)"), "users", "tipo de contacto"),
        vcard("Dónde están", _bars_simple(D.FUGA_ZONA, "var(--pnk)"), "pin", "zona declarada"),
        vcard("Hace cuánto calificaron", _bars_simple(D.FUGA_EDAD, "var(--good)"), "clock", "días desde la calificación"),
        vcard("Dónde se cortó", _bars_simple(D.FUGA_CORTE, "var(--warn)"), "alert", "último paso registrado"),
        vcard("De dónde vinieron", _bars_simple(D.FUGA_ORIGEN, "var(--src-meta)"), "inb", "origen de la consulta"),
    ])
    cuello_adv = f'''<div class="dgrid">{dg}</div>
<div class="g3 mt">
{banner("good", "clock", f"<b>{D.FUGA_EDAD[0][1]} calificaron hace menos de 7 días.</b> Todavía están en ventana: un mensaje hoy los recupera sin pauta nueva.")}
{banner("warn", "bolt", f"<b>{D.FUGA_URGENTE} declararon urgencia</b> (obra en etapa de aberturas o robo). Son los primeros de la cola: deciden en días.")}
{banner("info", "store", f"<b>250 son comercios que quieren revender.</b> Se derivaron a un distribuidor que les compite: van al embudo B2B, no a la cola del consumidor.")}
</div>
<div class="note"><b>Próximo paso:</b> seguimiento automático por Smart Tag a las 48 h de <code>derivado_distribuidor</code> sin <code>visita_agendada</code>, con aviso al corredor de la zona. Las 230 sin zona vuelven al agente para pedirla antes de derivar.</div>'''
    cuello = _key("var(--warn)", "alert", f'Fuga principal {lvl("senal")}',
                  "El cuello de botella <em>no está en la demanda.</em>",
                  f"De cada 100 que entran, 81 responden y 58 quedan calificadas. Pero de esas <b>{fmt(D.CALIFICADA)} calificadas solo {fmt(D.SEGUIMIENTO)} tienen seguimiento</b>: "
                  f"se enfrían <b>{fmt(D.FUGA)} consultas que ya dijeron qué querían</b> (producto, zona y cantidad). Es la fuga más cara del embudo.",
                  [(fmt(D.CALIFICADA), "calificadas en el mes"), (fmt(D.SEGUIMIENTO), "con seguimiento y fecha"), (fmt(D.FUGA), "sin tocar después de derivar")],
                  cuello_adv, f"Quiénes son las {fmt(D.FUGA)} consultas que ya dijeron qué querían")

    # ---------- subregistro (etapa declarada vs evidencia) ----------
    ev_rows = [
        ["<b>Tag <code>visita_agendada</code> cargado</b><span class='sub'>lo marca el corredor o el equipo</span>", "126", "2,5%"],
        ["<b>Evidencia de seguimiento</b><span class='sub'>la conversación tiene fecha de visita, entrega o pedido</span>", "<b>890</b>", "18%"],
        ["<b>Tag <code>pedido_reportado</code> cargado</b><span class='sub'>lo marca el equipo</span>", "0", "0%"],
        ["<b>Evidencia de compra</b><span class='sub'>“ya la compré”, foto de factura o el distribuidor lo confirma</span>", f"<b>{D.PEDIDO_EVID}</b>", "4%"],
    ]
    corr_rows = [[f"<b>{c[0]}</b>", str(c[4]), str(c[5]), f"{pct(c[4], c[5])}%{minibar(pct(c[4], c[5]), 'var(--warn)')}"] for c in sorted(D.CORR, key=lambda c: c[4] / c[5])[:6]]
    sub_adv = f'''<div class="g2">
<div>{table(["Lectura", "Contactos", "Sobre 4.950"], ev_rows, 460)}</div>
<div>{table(["Corredor", "Visitas marcadas", "Pedidos tomados", "Marcado"], corr_rows, 420)}</div></div>
<div class="note">El corredor <b>sí trabaja</b>: tomó 352 pedidos. Lo que no hace es marcarlo en el CRM, porque el pedido vive en otro sistema. La regla que lo arregla: no se puede cerrar la visita sin dejar el resultado.</div>'''
    subreg = _key("var(--good)", "eye", f'Etapa declarada vs etapa por evidencia {lvl("senal")}',
                  "El embudo no está vacío: <em>está subregistrado.</em>",
                  f"Hay <b>764 contactos con evidencia de seguimiento</b> (fecha acordada en la conversación) y <b>214 con evidencia de compra</b> que nadie marcó. "
                  f"La cola real de seguimiento es <b>7 veces más grande</b> que la que muestra el tag.",
                  [("126", "con el tag de visita"), ("890", "con fecha acordada en la charla"), ("0 → 214", "pedidos: con tag → por evidencia")],
                  sub_adv, "Dónde está el subregistro")

    # ---------- hallazgo vistoso: uso de embudos ----------
    emb = ""
    for nm, who, deb, tiene, kind in D.USO_EMB:
        p = pct(tiene, deb)
        cls = {"auto": "c-auto", "man": "c-man", "none": "c-none"}[kind]
        wi = {"auto": "bot", "man": "hand", "none": "x"}[kind]
        emb += (f'<div class="emb-r"><div class="emb-n">{nm}<span>{ic(wi)}{who} · {fmt(tiene)} de {fmt(deb)}</span></div>'
                f'<div class="emb-t"><i class="{cls}" style="width:{max(p, 0.8)}%"></i></div><div class="emb-v">{p}%</div></div>')
    tot_tags = D.TAGS_AUTO + D.TAGS_MAN
    hallazgo = f'''<div class="hallazgo">
<div class="hz-top"><div style="min-width:0"><span class="hz-badge">{ic("spark")}El hallazgo del mes</span>
<div class="hz-t">El dato se corta <em>justo donde empieza la plata.</em></div>
<div class="hz-s">{bsc_adv("El agente ya carga solo <b>86 de cada 100 datos</b> del CRM. Los 14 restantes los tiene que marcar el equipo, y son justo los de la venta, la cobranza y el cierre. El próximo salto no es más tecnología: es usar lo que ya está armado.",
    f"Sobre {fmt(tot_tags)} tags aplicados en septiembre, <b>{fmt(D.TAGS_AUTO)} los puso el agente</b> y {fmt(D.TAGS_MAN)} el equipo. El embudo del agente cubre el 92% de lo esperado; los embudos manuales, entre 0% y 67%. La medición se corta en el traspaso del agente al equipo.")}</div></div></div>
<div class="hz-body">
  <div>{donut([(D.TAGS_AUTO, "var(--vio)"), (D.TAGS_MAN, "var(--warn)")], "86%", "de los datos los carga el agente solo")}
  <div class="dlg"><div><i style="background:var(--vio)"></i>Automático · el agente<b>{fmt(D.TAGS_AUTO)}</b></div><div><i style="background:var(--warn)"></i>Manual · el equipo<b>{fmt(D.TAGS_MAN)}</b></div></div></div>
  <div>{ghdr("Uso de cada embudo · contactos con tag sobre los que deberían tenerlo", "layers")}
  <div class="emb">{emb}</div>
  <div class="emb-lg"><span><i class="c-auto"></i>Automático (lo carga el agente)</span><span><i class="c-man"></i>Manual (lo marca el equipo)</span><span><i class="c-none"></i>Sin embudo creado</span></div></div>
</div>
<div class="hz-foot">
  <div>{ic("checkc", style="color:var(--good)")}<div><b>Lo que ya funciona.</b> El agente recibe, califica y deriva el 92% de las consultas sin que nadie toque nada.</div></div>
  <div>{ic("hand", style="color:var(--warn)")}<div><b>Lo que falta marcar.</b> Seguimiento, cobranza y pedido: 3 de cada 4 quedan sin registrar.</div></div>
  <div>{ic("upr", style="color:var(--vio)")}<div><b>Lo que se gana.</b> Con esos tres tags, el tablero mide por primera vez qué consulta terminó en pedido.</div></div>
</div></div>'''

    # ---------- fugas ----------
    fugas = f'''<div class="igrid">
{i3("corr", "Fuga 1 · De calificada a seguimiento: pasa solo el 31%",
    [("Qué mide", "Calificadas que llegan a una fecha acordada"), ("Base", f"{fmt(D.CALIFICADA)} calificadas"), ("Dato", "Tags del embudo + conversación")],
    [f"<b>{fmt(D.CALIFICADA)}</b> llegaron a calificada; <b>{fmt(D.SEGUIMIENTO)}</b> tienen seguimiento con fecha.",
     f"<b>{fmt(D.FUGA)}</b> se enfriaron: es la fuga más cara porque ya dijeron qué querían.",
     "No hace falta más pauta para recuperarlas: el dato ya está en el CRM."],
    "31%", "de las calificadas llega a una fecha acordada. El paso anterior (identificada → calificada) pasa el 88%.",
    cmpbar(31, 88, "paso anterior 88%", "calificada → seguimiento", "identificada → calificada"), own("ven"),
    lab2="Qué muestra el CRM", lab3="Cuánto pasa de un paso al siguiente")}
{i3("corr", "Fuga 2 · De responder a decir qué busca: pasa el 82%",
    [("Qué mide", "Conversaciones que dejan línea y zona"), ("Base", f"{fmt(D.RESPONDIO)} que respondieron"), ("Dato", "Variables del agente")],
    [f"<b>{fmt(D.RESPONDIO)}</b> respondieron al agente; <b>{fmt(D.IDENTIFICO)}</b> dijeron qué producto y dónde.",
     f"<b>{fmt(D.RESPONDIO - D.IDENTIFICO)}</b> conversaron sin dejar zona ni línea: el agente manda material antes de preguntar.",
     "Próximo paso: pedir zona y línea dentro de los 2 primeros mensajes."],
    "82%", "de los que responden dicen qué buscan y dónde. Objetivo: 90%.",
    cmpbar(82, 90, "objetivo 90%", "hoy", "objetivo propuesto"), own("aurea"),
    lab2="Qué muestra el CRM", lab3="Cuánto pasa de un paso al siguiente")}
{i3("corr", "Fuga 3 · De entrar a responder: las consultas sin anuncio responden menos",
    [("Qué mide", "Consultas que responden al primer mensaje"), ("Base", f"{fmt(D.CONSULTAS)} consultas"), ("Dato", "Origen + conversación")],
    [f"<b>{fmt(D.CONSULTAS - D.RESPONDIO)}</b> nunca respondieron al agente (19%).",
     "Con anuncio identificado responde el <b>82%</b>; sin origen identificado, el <b>61%</b>.",
     "Próximo paso: segundo toque automático a las 24 h y cerrar el origen de las 225 sin atribuir."],
    "61%", "responde cuando no se sabe de dónde vino. Con anuncio identificado: 82%.",
    cmpbar(61, 82, "con anuncio 82%", "sin origen identificado", "con anuncio identificado"), own("mkt"),
    lab2="Qué muestra el CRM", lab3="Cuánto pasa de un paso al siguiente")}
</div>'''

    # ---------- B2B vs B2C ----------
    vs = f'''<div class="vs">
<div class="vs-c"><div class="vs-h"><div class="io-ic" style="background:var(--blu)">{ic("home")}</div><div><b>B2C · consumidor final</b><span>Compra una vez, decide en días</span></div></div>
<div class="vs-row">Consultas del mes<b>3.960 · 80%</b></div><div class="vs-row">Se califican<b>61%</b></div>
<div class="vs-row">Qué se hace hoy<b>Se deriva al distribuidor de la zona</b></div><div class="vs-row">Embudo<b>Recepción y calificación</b></div>
<div class="vs-row">Tag de tipo de contacto<b>{ic("check", style="color:var(--good)")} consumidor_final</b></div></div>
<div class="vs-c"><div class="vs-h"><div class="io-ic" style="background:var(--vio)">{ic("store")}</div><div><b>B2B · comercios y obras</b><span>Compran de forma recurrente, deciden en semanas</span></div></div>
<div class="vs-row">Consultas del mes<b>472 · 10%</b></div><div class="vs-row">Se califican<b>71%</b></div>
<div class="vs-row">Qué se hace hoy<b style="color:var(--crit-ink)">47% se deriva a un distribuidor que les compite</b></div><div class="vs-row">Embudo<b style="color:var(--crit-ink)">El mismo que el consumidor</b></div>
<div class="vs-row">Tag de tipo de contacto<b>{ic("check", style="color:var(--good)")} comercio · arquitecto_obra</b></div></div>
</div>'''
    b2b_adv = f'''<div class="g2">{vcard("Tipo de contacto · las 4.950 consultas", _bars_simple(D.TIPO), "users", "tag excluyente", src("pro"))}
{vcard("Qué pasó con los 472 B2B", bars([("Derivados a un distribuidor", 220, "47%"), ("Derivados al corredor", 96, "20%"), ("Con seguimiento y fecha", 41, "9%"), ("Alta como distribuidor nuevo", 2, "0,4%")], "var(--vio)"), "store", "base: 472", src("pro"))}</div>
<div class="note"><b>Embudo propuesto · Red B2B:</b> comercio identificado → lista de precios enviada → visita del corredor → primer pedido → alta en la red. Cada etapa es una Smart Tag; la de visita notifica al corredor de la zona.</div>'''
    b2b = _key("var(--vio)", "store", f'B2B y B2C {lvl("senal")}',
               "Separados por tag, <em>mezclados en el embudo.</em>",
               "El agente ya distingue al consumidor del comercio (el tag de tipo de contacto está cargado en el 95% de las consultas). Pero los dos siguen el mismo embudo, "
               "así que <b>un corralón que quiere revender termina derivado a un distribuidor que le compite</b>. Separarlos en un embudo propio cuida la red y mide cada ciclo por separado.",
               [("472", "consultas B2B en el mes"), ("95%", "tienen el tag de tipo de contacto"), ("0", "embudos B2B creados")],
               vs + '<div class="mt"></div>' + b2b_adv, "Cómo se reparte y qué pasa con cada uno")

    # ---------- base curada ----------
    curada = f'''<div class="g2">
{vcard("Quién no es demanda de compra", "".join(bar(l, fmt(v), 100 * v / 1089, f"{pct(v, D.NO_DEM_TOT)}%", "var(--ink4)") for l, v in D.NO_DEMANDA) +
       '<div class="note">Hay solapamiento mínimo entre categorías. Posventa no es un error: el cliente no tiene otro lugar donde preguntar.</div>', "filter", f"{fmt(D.NO_DEM_TOT)} contactos · 26%", src("pro"))}
{vcard("Por qué importa separarlos · efecto sobre los ratios",
       bar("Consultas del mes", fmt(D.CONSULTAS), 100, "100%") + bar("Demanda de compra real", fmt(D.BASE_CURADA), 74, "74%") + bar("Calificadas", fmt(D.CALIFICADA), 58, "58% · 78% de la demanda real") +
       '<div class="note">Sobre la base curada, la calificación sube de <b>58% a 78%</b>. Mezcladas, las 1.280 consultas que no son compra bajan todas las tasas del embudo y encarecen el costo por consulta útil.</div>', "sigma", "base curada", src("calc"))}
</div>'''

    # ---------- inventario de tags ----------
    def tagcol(color, title, chipc, desc, rows):
        rr = "".join(bar(f"<code>{t}</code>", fmt(v), 100 * v / D.CONSULTAS, f"{fmt(100 * v / D.CONSULTAS, 1)}%" if v else "", color) for t, v in rows)
        return f'<div class="bc" style="--bcac:{color}"><div class="bc-hd"><div class="bc-nm">{title}</div><span class="obj" style="background:{color};color:#fff">{chipc}</span></div><div class="bc-cap">{desc}</div>{rr}</div>'
    tags = f'''<div class="bigcamp">
{tagcol("var(--good)", "Vivos", "Se usan", "Estructuran el tramo del agente.", [("consulta_nueva", 4950), ("calificada", 2870), ("derivado_distribuidor", 2640), ("puerta · ventana · pivotante", 3060)])}
{tagcol("var(--warn)", "A medias", "Se usan poco", "Sirven, pero no siempre se cargan.", [("pidio_cotizacion", 410), ("visita_agendada", 126), ("objecion_precio", 61), ("estado_cuenta_enviado", 44)])}
{tagcol("var(--crit)", "Sin uso", "Por activar", "Todos del tramo de cierre: el recorrido está diseñado y falta marcarlo.", [("pedido_reportado", 0), ("alta_distribuidor", 2), ("no_concreto", 4), ("motivo_perdida", 2)])}
</div>
<div class="note">Las barras usan la misma escala en las tres columnas: % sobre las 4.950 consultas del mes. El export solo muestra tags que se usaron al menos una vez. Un tag configurado y nunca aplicado no aparece: para el inventario completo hace falta el catálogo de tags de la cuenta.</div>'''

    # ---------- variables ----------
    def vcol(title, chipc, rows, color):
        rr = "".join(bar(l, f"{v}%", v, "", color) for l, v in rows)
        return f'<div class="vcard">{ghdr(title, None, "", chipc)}{rr}</div>'
    variables = f'''<div class="g3">
{vcol("Útiles hoy", lvl("hecho"), [("Canal y fecha", 100), ("Tipo de contacto", 95), ("Línea de producto", 88), ("Anuncio de origen (pauta)", 84)], "var(--good)")}
{vcol("Mejorables", lvl("senal"), [("Zona", 66), ("Cantidad de puertas", 58), ("Momento de obra", 47), ("Forma de pago", 41)], "var(--blu)")}
{vcol("Por reforzar", lvl("indicio"), [("Causa del problema", 29), ("Resultado de la visita", 31), ("Motivo de no compra", 9), ("Pedido vinculado", 0)], "var(--warn)")}
</div>'''

    pasos = [
        ("1", "Campos requeridos por etapa", "Que no se pueda marcar <b>visita realizada</b> sin dejar el resultado del contacto. Hoy hay 2.640 derivaciones y 126 visitas marcadas: la brecha es de carga, no de trabajo.",
         [own("aurea", "Config. de Prometheo"), chip("Esfuerzo bajo", "clock"), chip("Impacto alto", "upr")], "Desbloquea: <b>conversión real de visita a pedido</b>"),
        ("2", "Seguimiento automático a las 48 h", f"Un Smart Tag dispara el mensaje a toda consulta derivada sin fecha a las 48 h y avisa al corredor. Recupera parte de las <b>{fmt(D.FUGA)}</b> que se enfrían.",
         [own("aurea", "Seguimientos"), chip("Esfuerzo bajo", "clock"), chip("Impacto alto", "upr")], "Desbloquea: <b>la cola de seguimiento sin trabajo manual</b>"),
        ("3", "Embudo propio para el B2B", "Comercio identificado → lista enviada → visita → primer pedido → alta. Separa los 472 comercios del consumidor y deja de derivarlos a la competencia.",
         [own("aurea", "Diseño de CRM"), chip("Esfuerzo medio", "clock"), chip("Impacto alto", "upr")], "Desbloquea: <b>altas de distribuidores medibles</b>"),
        ("4", "Pedir la zona antes de derivar", "Sin zona no hay forma de elegir distribuidor: 230 calificadas quedaron sin derivar. Una línea en el prompt del agente lo resuelve.",
         [own("aurea", "Prompt del agente"), chip("Esfuerzo bajo", "clock"), chip("Impacto medio", "upr")], "Desbloquea: <b>derivación al distribuidor exacto</b>"),
        ("5", "Reforzar urgencia y causa", "Son las dos señales que ordenan la cola (41% y 29% de carga). El prompt tiene que priorizarlas: si el refuerzo nombra todo, no prioriza nada.",
         [own("aurea", "Prompt del agente"), chip("Esfuerzo bajo", "clock"), chip("Impacto medio", "upr")], "Desbloquea: <b>cola ordenada por urgencia</b>"),
        ("6", "Marcar el pedido en la conversación", "Un tag de pedido confirmado (manual o desde la respuesta del distribuidor) une la consulta con la venta. Hoy hay 214 compras dichas en el chat y 0 marcadas.",
         [own("ven", "Proceso del equipo"), chip("Esfuerzo medio", "clock"), chip("Impacto alto", "upr")], "Desbloquea: <b>qué consulta y qué anuncio terminó en pedido</b>"),
    ]
    steps = '<div class="steps">' + "".join(
        f'<div class="stp"><div class="stp-h"><div class="stp-n">{n}</div><b>{t}</b></div><div class="stp-d">{d}</div>'
        f'<div class="stp-tags">{"".join(tg)}</div><div class="stp-f">{ic("upr")}<div>{f}</div></div></div>' for n, t, d, tg, f in pasos) + "</div>"

    defectos = f'''<div class="adv">
<div class="ss-lab"><span class="n">{ic("wrench")}</span>Defectos de modelo detectados · modo avanzado</div>
<div class="g3">
{_key("var(--crit)", "tag", "Tags que compiten", "Dos líneas en la misma consulta", "<b>186 consultas</b> tienen dos tags de línea y 41 están como calificada y no fit a la vez. La línea es una dimensión: los valores deberían ser excluyentes.", [("186", "con dos líneas"), ("41", "calificada + no fit")])}
{_key("var(--warn)", "pin", "La zona se carga tarde", "Derivar sin zona", "Solo el <b>66%</b> tiene zona al momento de derivar. Sin zona, la derivación la decide el agente por aproximación.", [("66%", "con zona al derivar"), ("230", "calificadas sin derivar")])}
{_key("var(--vio)", "user", "Moderador sin asignar", "49 activos sin corredor", "Los distribuidores sin moderador asignado no reciben notificación cuando escriben. Recompran al <b>31%</b>, contra 62% del resto.", [("49", "activos sin corredor"), ("31%", "recompra 30 días")])}
</div></div>'''

    concl = f'''<div class="concl">
<div class="concl-l"><div class="bn-ic">{ic("checkc")}</div><div><b class="t">La buena noticia: no hay que rediseñar nada.</b>
<p>Los tags existen, el agente funciona y el recorrido está pensado hasta el pedido. Lo que falta es carga en el último tramo, y se resuelve en este orden. Ninguno de los pasos depende de más pauta.</p></div></div>
<div class="concl-r">
<div><span class="n">1</span><b>Configuración</b> · campos requeridos y seguimiento a 48 h<span class="c">2 semanas</span></div>
<div><span class="n">2</span><b>Prompt</b> · zona antes de derivar, urgencia y causa<span class="c">1 semana</span></div>
<div><span class="n">3</span><b>Proceso</b> · embudo B2B y pedido marcado<span class="c">1 mes</span></div>
</div></div>'''

    mejora = f'''<div class="subsec mejora">
<div class="ss-h"><div class="ss-ic">{ic("wrench")}</div><div><div class="ss-k">Subsector · Cómo mejorar el CRM</div>
<h2>Lo que el CRM ya tiene, <em>y lo que le falta registrar.</em></h2>
<p>Lectura constructiva del uso del CRM: qué funciona, dónde se corta el dato y qué cambio lo arregla. <b>Datos ilustrativos</b> sobre la estructura real de Prometheo.</p></div></div>
{hallazgo}
<div class="ss-lab" style="margin-top:24px"><span class="n">1</span>Cards clave</div>
<div style="display:flex;flex-direction:column;gap:14px">{cuello}{subreg}{b2b}</div>
<div class="ss-lab"><span class="n">2</span>Dónde se pierde el embudo · tocá cada card para ver el análisis</div>
{fugas}
<div class="ss-lab"><span class="n">3</span>Sobre qué base se mide</div>
{curada}
<div class="ss-lab"><span class="n">4</span>Inventario de tags · cuáles se usan y cuáles no</div>
{tags}
<div class="ss-lab"><span class="n">5</span>Variables · qué tan completo está cada dato</div>
{variables}
<div class="ss-lab"><span class="n">6</span>Qué cambiar · por dónde se arregla cada cosa</div>
{steps}
{defectos}
{concl}
</div>'''

    cruces = f'''<div class="adv">{eyebrow("Cruces accionables · modo avanzado")}
{mincard("Corralón × AMBA × compra solo puertas", "el cruce con más espacio para sumar ventanas", kv([("64", "distribuidores"), ("0", "compran ventanas"), ("10 puertas", "ya habilitan descuento")]) + ul(["Guion de cruce: sumar <b>ventanas PVC</b> al pedido de puertas", "El corredor de AMBA los visita esta semana"]), "grid", "64", "dist.", True)}
{mincard("Sin comprar +45 días × Interior × sin deuda", "reactivación sin bloqueo de cuenta", kv([("41", "distribuidores"), ("$0", "deuda que frene"), ("63 días", "promedio sin comprar")]) + ul(["Difusión con <b>novedad de temporada</b> y coeficiente vigente", "Sin deuda: se despacha apenas piden"]), "clock", "41", "dist.")}
{mincard("Venta cruzada · la palanca del ticket", "10 puertas mínimo habilitan descuento", '<p class="note" style="margin:0">Se incentiva sumar <b>ventanas y puertas</b> en el mismo pedido. Con la línea taggeada en cada consulta, el agente detecta al distribuidor que compra una sola categoría y arma el guion de cruce. Exhibidores bonificados para el salón; no se trabaja en consignación.</p>', "plus", "10", "puertas mín.")}
</div>'''

    return f'''<section class="panel p-ventacrm">
{sec_head("Venta · CRM · el estado de cada contacto", "Tres colas de trabajo, <em>ordenadas por prioridad.</em>",
          "PAVIR no vende directo: el agente califica la consulta y la deriva al distribuidor de la zona; el corredor atiende a la red. Acá se ve <b>a quién atender primero</b>, dónde se pierde el embudo y <b>cómo mejorar el uso del CRM</b>.")}
{colas}
{eyebrow("El embudo de consultas")}
{embudo}
{cruces}
{mejora}
</section>'''
