"""Demanda de productos, Criterio comercial e Insights."""
from icons import ic
from comp import (fmt, pct, money, src, lvl, own, chip, delta, sec_head, eyebrow, ghdr, banner, kpi, bar, bars,
                  vcard, table, bsc_adv, minibar, mincard, ul, i3, kv, cmpbar)
import data as D


# =====================================================================
def demanda():
    kp = '<div class="g4">' + "".join([
        kpi("Categorías", "3", "", "Puertas de acero · pivotantes · ventanas", "box", "", "erp"),
        kpi("Modelos en catálogo", "18", "", "Líneas y modelos padre", "list", "blu", "erp"),
        kpi("Piden puertas de acero", "52%", delta("−2 p.p.", "flat", None), "de las consultas que dicen qué producto buscan", "door", "pnk", "pro"),
        kpi("Mínimo para descuento", "10 puertas", "", "La palanca de ticket del distribuidor", "dollar", "grn", "erp"),
    ]) + "</div>"
    lines = [("Puertas de acero", 62, 52, "var(--vio)"), ("Ventanas", 24, 30, "var(--blu)"), ("Pivotantes", 14, 18, "var(--pnk)")]
    cmp_rows = ""
    for l, comp_, ped, col in lines:
        gap = ped - comp_
        g = f'<span class="delta {"d-good" if gap > 0 else "d-flat"}">{"+" if gap > 0 else ""}{gap} p.p.</span>'
        cmp_rows += (f'<div style="padding:10px 0;border-top:1px solid var(--line2)"><div style="display:flex;align-items:center;gap:8px;margin-bottom:7px"><b style="font-size:13px">{l}</b>'
                     f'<span style="margin-left:auto;font-size:11px;color:var(--ink3)">pedido − comprado: {g}</span></div>'
                     f'{bar(src("erp", "Comprado"), f"{comp_}%", comp_ / 0.7, "de los pedidos", col)}'
                     f'{bar(src("pro", "Pedido"), f"{ped}%", ped / 0.7, "de las consultas", "var(--ink4)")}</div>')
    gapcard = f'''<div class="card pad">{ghdr("Lo que se compró contra lo que se pidió · por línea", "layers", "pedidos de la red vs consultas de personas")}
{cmp_rows}
<div class="note">{bsc_adv("Ventanas y pivotantes se piden más de lo que la red compra. La demanda existe: falta que el distribuidor los tenga en el salón.",
   "Comprado: participación en los 384 pedidos (Producí). Pedido: participación en las 3.270 consultas que dicen qué producto buscan (Prometheo). No se suman: son dos poblaciones distintas, la red y el consumidor.")}</div></div>'''

    prod = f'''<div class="g3 mt">
{vcard("Puertas de acero · por línea", bars([("Clásica", 44, "44%"), ("Luján", 33, "33%"), ("PAVIR premium", 23, "23%")]), "door", "", src("erp"))}
{vcard("Pivotantes · por modelo", bars([("Lisa", 28, "28%"), ("Wall Panel", 24, "24%"), ("Postigos laterales", 19, "19%"), ("Nueva Colección", 16, "16%"), ("Texturada", 13, "13%")]), "door", "", src("erp"))}
{vcard("Ventanas · PVC o aluminio", bars([("PVC", 54, "54%"), ("Aluminio alta prestación", 21, "21%"), ("Aluminio mediana", 15, "15%"), ("Aluminio económica", 10, "10%")]), "window", "", src("erp"))}
{vcard("Tamaño del pedido", bars([("Menos de 10 puertas", 205), ("De 10 a 30 puertas", 170), ("Más de 30 puertas", 125)], total=500), "box", "base: 500 activos", src("erp"))}
{vcard("Extras que suben el ticket", bar("Colores especiales de acero", "17%", 100, "de los pedidos", "var(--pnk)") + bar("Cerradura electrónica full", "9%", 53, "de los pedidos") + bar("Contramarco de pivotante", "incluido", 80, "", "var(--good)"), "plus", "", src("erp"))}
{vcard("Venta cruzada · la palanca", bar("Compran solo puertas", str(D.SOLO_PUERTAS), 42, "distribuidores", "var(--warn)") + bar("Compran puertas y ventanas", "352", 100, "distribuidores", "var(--good)") + bar("Mínimo para descuento", "10", 40, "puertas"), "repeat", "", src("erp"))}
</div>'''

    pide = f'''<div class="g3">
{vcard("Qué piden en la consulta", bars([("Pidió cotización", 76, "46%"), ("Pidió ficha técnica", 36, "22%"), ("Está comparando marcas", 23, "14%"), ("Pregunta por cerradura electrónica", 15, "9%")]), "chat", "tags de la conversación", src("pro"))}
{vcard("En qué momento de la obra está", bars([("Etapa de aberturas", 38, "38%"), ("Reforma o ampliación", 25, "25%"), ("Reposición o rotura", 21, "21%"), ("Obra nueva desde cero", 16, "16%")]), "building", "base declarada: 1.640", src("pro"))}
{vcard("Por dónde escriben", "".join(bar(l, fmt(v), 100 * v / 3020, f"{pct(v, D.CONSULTAS)}%") for l, v in D.PUERTA), "chat", f"{fmt(D.CONSULTAS)} consultas", src("pro"))}
</div>
<div class="adv mt"><div class="g2">
{vcard("Zona de quien consulta", bars([("AMBA", 35, "35%"), ("Centro", 24, "24%"), ("Litoral", 17, "17%"), ("Cuyo", 13, "13%"), ("NOA, NEA y Sur", 11, "11%")]), "pin", "base declarada: 3.270", src("pro"))}
{vcard("Línea por zona · dónde se pide qué", bars([("Pivotantes en AMBA", 46, "46% de los pivotantes"), ("Ventanas PVC en Centro y Litoral", 41, "41% de las ventanas"), ("Puertas de seguridad en Cuyo y NOA", 33, "33% de las puertas")]), "grid", "cruce línea × zona", src("calc"))}
</div></div>'''

    big = f'''<div class="bigcamp">
<div class="bc" style="--bcac:var(--vio)"><div class="bc-hd"><div class="bc-nm">Puertas de acero</div><span class="obj">Volumen</span></div><div class="bc-o">Clásica · Luján · PAVIR premium</div>
<div class="bc-big"><div class="n">62%</div><div class="u">de los pedidos</div></div><div class="bc-cap">52% de las consultas · nanofosfatizado y pintura a 220 °C, sistema antibarreta</div>
<div class="bc-verd">{ic("star")}<div><b>Producto ancla.</b> Sumar la cerradura electrónica full sube el ticket.</div></div></div>
<div class="bc" style="--bcac:var(--blu)"><div class="bc-hd"><div class="bc-nm">Ventanas</div><span class="obj" style="background:var(--blu-soft);color:var(--src-meta)">Venta cruzada</span></div><div class="bc-o">PVC · aluminio alta, mediana y económica</div>
<div class="bc-big"><div class="n">24%</div><div class="u">de los pedidos</div></div><div class="bc-cap">30% de las consultas · PVC lidera con 54%</div>
<div class="bc-verd">{ic("plus")}<div><b>Palanca de ticket.</b> {D.SOLO_PUERTAS} distribuidores compran solo puertas: sumar ventanas no cuesta captación.</div></div></div>
<div class="bc" style="--bcac:var(--pnk)"><div class="bc-hd"><div class="bc-nm">Pivotantes</div><span class="obj" style="background:var(--pnk-soft);color:#A8467F">Ticket alto</span></div><div class="bc-o">Lisa · Wall Panel · Postigos · Texturada</div>
<div class="bc-big"><div class="n">14%</div><div class="u">de los pedidos</div></div><div class="bc-cap">18% de las consultas · margen alto, contramarco incluido</div>
<div class="bc-verd">{ic("eye")}<div><b>Oportunidad.</b> El 44% de quien pregunta dice que nunca la vio exhibida.</div></div></div>
</div>'''

    cat = table(["Categoría", "Línea o gama", "Modelos", "Material", "Terminación", "Extra clave"], [
        ["<b>Puerta de entrada</b>", "Clásica", "Triple contacto", "Acero", "Poliéster 220 °C", "Antibarreta"],
        ["<b>Puerta de entrada</b>", "Luján", "Reforzada", "Acero", "Nanofosfatizado", "Cerradura reforzada"],
        ["<b>Puerta de entrada</b>", "PAVIR premium", "Blanco Antártida · Gris Grafito · Acero Símil", "Acero", "Hasta 120 micrones", "Cerradura electrónica full"],
        ["<b>Pivotante</b>", "Aluminio", "Lisa · Postigos · Wall Panel · Nueva Colección · Texturada", "Aluminio", "Anodizado o pintura", "Contramarco incluido"],
        ["<b>Ventana</b>", "PVC", "Corrediza · Rebatir · Oscilobatiente · Paño fijo", "PVC", "Blanco o símil madera", "Doble vidrio hermético"],
        ["<b>Ventana</b>", "Aluminio", "Alta prestación · Mediana · Económica", "Aluminio", "Anodizado o pintura", "Abrir, rebatir o corrediza"],
    ], 860)

    return f'''<section class="panel p-demanda">
{sec_head("Demanda de productos · qué se compró y qué se pidió", "Qué se compró <em>y qué se pidió.</em>",
          ("Lo que la red le compró a PAVIR al lado de lo que piden las personas que consultan. <b>La diferencia entre las dos es la oportunidad.</b>", "Comprado: participación en los pedidos del export de Producí. Pedido: participación en las consultas de Prometheo que declaran producto. Son dos poblaciones (red y consumidor): se comparan, no se suman."))}
{kp}
<div class="mt">{gapcard}</div>
{eyebrow("Qué se compró · por línea y modelo", " " + src("erp"))}
{prod}
{eyebrow("Qué se pidió · lo que dicen las consultas", " " + src("pro"))}
{pide}
{eyebrow("Líneas destacadas · las que mueven la caja")}
{big}
<div class="adv">{eyebrow("Catálogo por modelo · modo avanzado")}{cat}</div>
</section>'''


# =====================================================================
def criterio():
    kp = '<div class="g4">' + "".join([
        kpi("Dicen qué necesitan resolver", "78%", delta("+12 p.p."), f"<b>{fmt(D.CRIT_PROBLEMA)}</b> de {fmt(D.CRIT_BASE)} lo cuentan con sus palabras: «se me rompió la cerradura», «estoy en etapa de aberturas»", "quote", "", "pro",
            adv=f"Nivel {lvl('senal')} · lo registra el agente desde la conversación, sin preguntas extra."),
        kpi("Dicen qué les cuesta esperar", "41%", delta("+5 p.p."), f"<b>{fmt(D.CRIT_IMPACTO)}</b>: obra frenada, casa sin cerrar, mudanza con fecha", "hourglass", "pnk", "pro",
            adv=f"Nivel {lvl('senal')} · inferido por el agente: es el dato más frágil del grupo."),
        kpi("Cuentan qué pasó para escribir hoy", "55%", delta("+9 p.p."), f"<b>{fmt(D.CRIT_DISPARADOR)}</b>: un robo, la obra llegó a aberturas, una reforma", "bolt", "blu", "pro",
            adv=f"Nivel {lvl('senal')} · con antigüedad: menos de 30 días, 30 a 90, más de 90."),
        kpi("Derivaciones con fecha acordada", "34%", delta("−3 p.p.", "bad", "down"), f"<b>{fmt(D.SEGUIMIENTO)}</b> de {fmt(D.DERIVADA)} terminaron en visita, entrega o pedido con fecha", "cal", "grn", "pro",
            adv=f"Nivel {lvl('indicio')} · lo carga el equipo después de cada contacto."),
    ]) + "</div>"

    q = '<span class="adv" style="display:inline">' + lvl("senal") + "</span>"
    cards = f'''<div class="igrid">
{i3("motivo", 'Quien consulta por «obra parada» avanza casi el doble que quien consulta por «precio»',
    [("Qué mide", "El motivo de la consulta, en palabras del cliente"), ("Base", f"{fmt(D.CRIT_PROBLEMA)} consultas que dicen qué necesitan"), ("Dato", "Conversación con el agente")],
    ["<b>1.120 consultas</b> dicen que la obra está frenada esperando las aberturas.",
     "De esas, <b>58 de cada 100</b> llegan a una fecha acordada (visita, entrega o pedido). De las que preguntan solo «precio», 31 de cada 100.",
     "Quien tiene la obra parada no pide descuento: pregunta <b>disponibilidad y plazo de entrega</b>."],
    "58%", "de las consultas por «obra parada» llegan a una fecha acordada. Las que consultan por «precio»: 31%.",
    cmpbar(58, 31, "«precio» 31%", "«obra parada»", "consultas por «precio»"), own("ven"), q, lab2="Qué dice la conversación", lab3="Resultado contra el resto")}
{i3("urg", 'Tres situaciones explican 7 de cada 10 consultas urgentes: «etapa de aberturas», «robo» y «reforma»',
    [("Qué mide", "Qué pasó para que escriba hoy"), ("Base", f"{fmt(D.CRIT_DISPARADOR)} consultas que lo cuentan"), ("Dato", "Conversación con el agente")],
    ["<b>Obra en etapa de aberturas</b> 38% · <b>robo o inseguridad</b> 19% · <b>reforma</b> 14%.",
     "Quien escribe después de un robo pide <b>puerta de seguridad</b> y decide en días, no en meses.",
     "Ninguna de las tres se puede elegir como público en Meta, pero <b>sí se puede nombrar en el anuncio</b>."],
    "71%", "de las consultas con un motivo de urgencia se explican con estas tres situaciones.",
    cmpbar(71, None, "", "las tres situaciones"), own("mkt"), q, lab2="Qué dice la conversación", lab3="Resultado")}
{i3("avance", "2 de cada 3 derivaciones terminan sin una fecha acordada",
    [("Qué mide", "Qué pasó después de derivar"), ("Base", f"{fmt(D.DERIVADA)} derivaciones"), ("Dato", "Lo carga el corredor o el distribuidor")],
    [f"<b>{fmt(D.SEGUIMIENTO)}</b> tienen una acción con fecha: visita, entrega o pedido.",
     f"<b>{fmt(D.DERIVADA - D.SEGUIMIENTO)}</b> quedaron en «lo veo»: la charla sigue sin compromiso.",
     "No falta demanda: el tramo que se enfría es el que sigue a la derivación (ver Venta · CRM)."],
    "34%", "de las derivaciones terminó con una fecha acordada. El objetivo propuesto es 60%.",
    cmpbar(34, 60, "objetivo 60%", "hoy", "objetivo con seguimiento a 48 h"), own("ven"), '<span class="adv" style="display:inline">' + lvl("indicio") + "</span>", lab2="Qué dice la conversación", lab3="Resultado contra el objetivo")}
{i3("freno", 'De los que preguntan por pivotantes, 44% dice que «nunca la vio exhibida»',
    [("Qué mide", "Qué le impide avanzar"), ("Base", "490 consultas por pivotante que lo cuentan"), ("Dato", "Conversación con el agente")],
    ["No es un problema de precio ni de interés: es de <b>exhibición</b>.",
     "El distribuidor no la tiene en el salón y el consumidor no se anima a comprar lo que no vio.",
     "Coincide con la campaña de WhatsApp: el <b>exhibidor</b> es lo que destrabó los pedidos."],
    "44%", "de quienes preguntan por pivotantes nunca vio uno exhibido.",
    cmpbar(44, None, "", "nunca la vio exhibida"), own("ven"), '<span class="adv" style="display:inline">' + lvl("indicio") + "</span>", lab2="Qué dice la conversación", lab3="Resultado")}
{i3("filtro", '1 de cada 5 consultas no es compra: es «posventa» o «consulta técnica»',
    [("Qué mide", "Si la consulta es de compra o no"), ("Base", f"{fmt(D.CONSULTAS)} consultas"), ("Dato", "Conversación con el agente")],
    ["<b>1.089 consultas</b> son medidas, compatibilidad o garantía de algo ya comprado.",
     "Entran al mismo embudo que la demanda y bajan todas las tasas de conversión.",
     "Separadas, la calificación real pasa de <b>58% a 78%</b>."],
    "78%", "de calificación sobre la demanda real. Mezclada con posventa: 58%.",
    cmpbar(78, 58, "sin separar 58%", "demanda real", "todas las consultas juntas"), own("aurea"), q, lab2="Qué dice la conversación", lab3="Resultado contra la lectura sin separar")}
{i3("prior", 'Urgencia alta y «pasó hace menos de 30 días»: 612 consultas que avanzan 66%',
    [("Qué mide", "Cruce de urgencia y momento"), ("Base", "612 consultas con los dos datos"), ("Dato", "Conversación con el agente")],
    ["<b>612 consultas</b> dicen qué les cuesta esperar y que lo que las disparó pasó hace menos de 30 días.",
     "Llegan a fecha acordada en <b>66 de cada 100</b>: casi el doble que el promedio, sin pauta nueva.",
     "Hoy entran a la misma cola que quien está comparando precios: es la lista que el corredor tendría que ver primero cada mañana."],
    "66%", "de las consultas de esta cola llegan a fecha acordada. Promedio de todas las derivaciones: 34%.",
    cmpbar(66, 34, "promedio 34%", "cola prioritaria", "promedio de las derivaciones"), own("ven"), q, lab2="Qué dice la conversación", lab3="Resultado contra el promedio")}
</div>'''

    uso = f'''<div class="g3">
<div class="dec-item" style="--dc:var(--good)"><div class="dec-h"><div class="dec-ic">{ic("star")}</div><b>La cola del día</b>{own("ven")}</div>
<div class="dec-p"><span class="pi">{ic("eye")}</span><div><span class="k">Qué es</span><b>612 consultas</b> con urgencia alta y motivo reciente, ordenadas arriba de todo.</div></div>
<div class="dec-p"><span class="pi">{ic("arrow")}</span><div><span class="k">Para qué sirve</span>El corredor empieza el día por quien avanza 66%, no por quien escribió primero.</div></div></div>
<div class="dec-item" style="--dc:var(--pnk)"><div class="dec-h"><div class="dec-ic">{ic("mega")}</div><b>El texto del anuncio</b>{own("mkt")}</div>
<div class="dec-p"><span class="pi">{ic("eye")}</span><div><span class="k">Qué es</span>Las tres situaciones que hacen escribir: «etapa de aberturas», «robo» y «reforma».</div></div>
<div class="dec-p"><span class="pi">{ic("arrow")}</span><div><span class="k">Para qué sirve</span>Un anuncio que nombra la situación («¿llegaste a la etapa de aberturas?») se prueba contra el que nombra el producto.</div></div></div>
<div class="dec-item" style="--dc:var(--blu)"><div class="dec-h"><div class="dec-ic">{ic("store")}</div><b>La exhibición en el salón</b>{own("ven")}</div>
<div class="dec-p"><span class="pi">{ic("eye")}</span><div><span class="k">Qué es</span>44% de quien pregunta por pivotantes nunca vio uno exhibido.</div></div>
<div class="dec-p"><span class="pi">{ic("arrow")}</span><div><span class="k">Para qué sirve</span>Prioriza dónde colocar exhibidores: en los distribuidores de las zonas que más los piden.</div></div></div>
</div>'''

    voz = f'''<div class="adv">{eyebrow("La voz del cliente · frases reales, sin convertir en porcentaje · modo avanzado", " " + src("pro"))}
<div class="g3">
<div class="quote"><h5>{ic("quote")}Motivo · «obra parada»</h5><p>«Tengo la obra frenada, el albañil espera la puerta para cerrar»</p><p>«Necesito las ventanas antes del 15, se me vence el alquiler»</p><p>«¿Tienen stock de la Luján o hay que esperar?»</p></div>
<div class="quote"><h5>{ic("bolt")}Urgencia · «robo»</h5><p>«Nos entraron el fin de semana, necesito algo seguro ya»</p><p>«Quiero la que tiene cerradura de varios puntos»</p><p>«¿Cuánto tarda la instalación?»</p></div>
<div class="quote"><h5>{ic("hand")}Freno · «no la vi»</h5><p>«Me gusta la pivotante pero no la vi en ningún corralón»</p><p>«¿Dónde la puedo ver armada?»</p><p>«En la foto se ve bien, ¿pero en persona?»</p></div>
</div>
<div class="note">Cada frase es de una persona: explica un número que ya existe, no es un patrón por sí sola.</div>
{eyebrow("Qué tan completo está cada dato · modo avanzado")}
<div class="g2">
{vcard("Carga de cada dato en las conversaciones", bar("Qué necesita resolver", "78%", 78, "señal", "var(--blu)") + bar("Qué pasó para escribir hoy", "55%", 55, "señal", "var(--blu)") + bar("Qué le cuesta esperar", "41%", 41, "señal", "var(--blu)") + bar("Qué le impide avanzar", "29%", 29, "indicio", "var(--warn)") + bar("Qué pasó después del contacto", "34%", 34, "indicio · lo carga el equipo", "var(--warn)"), "list", "base: 4.950", src("pro"))}
{vcard("Cómo se lee cada nivel", '<div class="estlegend" style="flex-direction:column;align-items:flex-start;gap:9px">' +
       f'<span>{lvl("hecho")} 80% o más: puede encabezar una card.</span><span>{lvl("senal")} 40 a 79%: card con la base aclarada.</span><span>{lvl("indicio")} 10 a 39%: acompaña, no encabeza.</span><span>{lvl("est")} menos de 10%: se trabaja en Cómo mejorar el CRM.</span></div>', "info")}
</div></div>'''

    return f'''<section class="panel p-criterio">
{sec_head("Criterio comercial · lo que dice cada conversación", "Qué necesita quien consulta, <em>y por qué escribe hoy.</em>",
          ("Además de contar consultas, el agente registra <b>qué necesita resolver</b> cada persona, <b>qué le cuesta esperar</b> y <b>qué pasó para que escriba hoy</b>. Con eso se ordena a quién atender primero y qué decir en el anuncio.", "Cinco datos que el agente extrae de la misma conversación, sin preguntas extra. Cada uno muestra su <b>base</b> y su <b>nivel de confianza</b> (Hecho, Señal o Indicio): un dato con poca carga acompaña, no encabeza."))}
{kp}
{eyebrow("Lo que se ve en las conversaciones · tocá cada card para ver el análisis")}
<div class="estlegend"><b style="color:var(--ink2)">Las etiquetas dicen qué se aprende del cliente:</b><span class="chip">{ic("quote")}Motivo</span><span class="chip">{ic("bolt")}Urgencia</span><span class="chip">{ic("cal")}Avance</span><span class="chip">{ic("hand")}Freno</span><span class="chip">{ic("filter")}Filtro</span><span class="chip">{ic("star")}Prioridad</span></div>
{cards}
{eyebrow("Cómo se usa esto")}
{uso}
{voz}
</section>'''


# =====================================================================
AVG = D.META["pcal"]
CAVG = D.META["ccal"]


def _ad_card(a, seal, name, extra, owner="mkt", big=None, txt=None, cmp=None):
    ctx = [("Campaña", f'{a["camp"]} · objetivo Mensajes'), ("Conjunto", a["conj"]), ("Anuncio", f'{a["nm"]}<span class="anm">{a["code"]}</span>')]
    bl = [f'Objetivo de la campaña en Meta: <b>Mensajes</b>. Meta lo da por cumplido con <b>{a["conv_meta"]} conversaciones</b>; Prometheo registró <b>{a["cons"]} consultas</b>.',
          f'En el CRM: <b>{a["calif"]}</b> calificaron, <b>{a["deriv"]}</b> se derivaron y <b>{a["seg"]}</b> tienen seguimiento con fecha.',
          extra,
          f'Costo por consulta calificada: <b>${fmt(a["ccal"])}</b> (promedio de la cuenta: ${fmt(CAVG)}).']
    big = big or f'{a["pcal"]}%'
    txt = txt or f'de las consultas de este anuncio calificaron: <b>{a["calif"]} de {a["cons"]}</b> dijeron producto, zona y cantidad. El promedio de los 8 anuncios es {AVG}%.'
    cmp = cmp or cmpbar(a["pcal"], AVG, f"promedio {AVG}%", "este anuncio", "promedio de los 8 anuncios de la cuenta")
    adv = kv([(f'{fmt(a["ctr"], 1)}%', "<abbr>CTR</abbr> · clics sobre impresiones"), (fmt(a["frec"], 1), "<abbr>Frec.</abbr> · veces que cada persona lo vio"),
              (f'${fmt(a["cpc"])}', "<abbr>CPC</abbr> · costo por clic"), (f'{pct(a["resp"], a["cons"])}%', "respondió al agente"),
              (str(a["cotiz"]), "pidió cotización"), (str(a["b2b"]), "comercios (B2B)")])
    return i3(seal, name, ctx, bl, big, txt, cmp, own(owner), adv=adv, sources=src("meta") + " " + src("pro"), lab3="Resultado contra el objetivo de la campaña")


def _conj_card(cj, seal, name, bullets, owner="mkt", big=None, txt=None, cmp=None):
    ads = D.CONJS[cj]
    t = D.agg(ads)
    camp = ads[0]["camp"]
    nm = " · ".join(a["nm"] for a in ads)
    ctx = [("Campaña", f"{camp} · objetivo Mensajes"), ("Conjunto", cj), ("Anuncio", f'{len(ads)} anuncio{"s" if len(ads) > 1 else ""}: {nm}')]
    big = big or f'{t["pcal"]}%'
    txt = txt or f'de las consultas de este conjunto calificaron ({t["calif"]} de {t["cons"]}). El promedio de los 7 conjuntos es {AVG}%.'
    cmp = cmp or cmpbar(t["pcal"], AVG, f"promedio {AVG}%", "este conjunto", "promedio de los 7 conjuntos")
    adv = kv([(fmt(t["alc"]), "personas alcanzadas"), (fmt(t["frec"], 1), "<abbr>Frec.</abbr> · veces que cada persona lo vio"), (f'${fmt(t["gasto"])}', "inversión del mes"),
              (f'${fmt(t["ccal"])}', "costo por calificada"), (f'{pct(t["resp"], t["cons"])}%', "respondió al agente"), (str(t["b2b"]), "comercios (B2B)")])
    return i3(seal, name, ctx, bullets, big, txt, cmp, own(owner), adv=adv, sources=src("meta") + " " + src("pro"), lab3="Resultado contra el objetivo de la campaña")


def insights():
    A = {a["code"]: a for a in D.ADS}
    M = D.META
    grupal = f'''<div class="grupal">
<div class="gv"><div class="l">{ic("checkc")}Califican · promedio</div><div class="n">{M["pcal"]}%</div><div class="m">{M["calif"]} de {fmt(M["cons"])} consultas de Meta</div></div>
<div class="gv"><div class="l">{ic("sigma")}Costo por calificada</div><div class="n">${fmt(M["ccal"])}</div><div class="m">${fmt(M["gasto"])} ÷ {M["calif"]} calificadas</div></div>
<div class="gv"><div class="l">{ic("up")}Mejor conjunto</div><div class="n">Retargeting</div><div class="m"><b>59%</b> califica · $536 por calificada</div></div>
<div class="gv"><div class="l">{ic("down")}Conjunto a revisar</div><div class="n">Broad</div><div class="m"><b>19%</b> califica · $1.754 por calificada</div></div>
</div>'''
    hier = f'''<div class="hier">
<div class="hc"><span class="cx-ic k-camp">{ic("camp")}</span><div><b>Campaña</b><span>Define el objetivo (acá: <b>Mensajes</b>) y el producto. Ej.: Puertas de acero.</span></div>{ic("chevr", "i ar")}</div>
<div class="hc"><span class="cx-ic k-conj">{ic("conj")}</span><div><b>Conjunto de anuncios</b><span>Define <b>a quién</b> se le muestra y con qué presupuesto. Ej.: Retargeting.</span></div>{ic("chevr", "i ar")}</div>
<div class="hc"><span class="cx-ic k-anun">{ic("anun")}</span><div><b>Anuncio</b><span>Es <b>lo que se ve</b>: video, imagen o carrusel. Ej.: video de la puerta Luján.</span></div></div>
</div>'''

    anun = f'''<div class="stab st-anun"><div class="igrid">
{_ad_card(A["VID_PuertaLujanCerradura_RET"], "subir", "Video de puerta Luján a quien ya visitó la web: el anuncio con más consultas calificadas",
          "<b>52</b> pidieron cotización (27%, la tasa más alta de la cuenta) y <b>11</b> ya dijeron en la charla que compraron.")}
{_ad_card(A["VID_PuertaClasicaSeguridad_IG"], "mant", "Video de puerta Clásica de seguridad en intereses de construcción: el que más calificadas trae en volumen",
          "Es el anuncio con más consultas calificadas en número (<b>120</b>): sostiene el volumen de la campaña.")}
{_ad_card(A["VID_VentanaPVCAhorro_IG"], "subir", "Video de ventana PVC y ahorro de energía en obra nueva: la mitad de las consultas califica",
          "Duplica la calificación del otro anuncio de ventanas (52% contra 19%) con menos inversión.")}
{_ad_card(A["EST_PavirPremiumTerminacion_WPP"], "mant", "Imagen de terminación PAVIR premium: menos volumen, más pedidos de la línea de margen alto",
          "<b>36 de sus 88</b> calificadas piden la línea premium: es el anuncio que más ticket alto trae.")}
{_ad_card(A["CAR_PuertaAceroColores_BROAD"], "corr", "Carrusel de colores de puerta de acero en reformas: 1 de cada 3 pide un color especial",
          "<b>64 de 190</b> preguntan por colores especiales, que tardan 20 días más: el anuncio promete algo que no está en stock.")}
{_ad_card(A["CAR_VentanaPVCGenerico_BROAD"], "paus", "Carrusel de ventana PVC genérica al público amplio: solo 19 de cada 100 consultas califican",
          "Trae el mayor volumen de la cuenta (<b>300</b>), pero 1 de cada 3 no responde al agente y muchos están «mirando precios».", "mkt")}
{_ad_card(A["VID_PivotanteWallPanel_IG"], "mant", "Video de pivotante Wall Panel en arquitectura y diseño: trae estudios y obras",
          "<b>10</b> de sus consultas son estudios de arquitectura o constructoras: compran más de una unidad.")}
{_ad_card(A["EST_PivotanteExhibidor_LAA"], "prob", "Imagen del exhibidor de pivotantes al público parecido a los distribuidores: 46 comercios que quieren revender",
          "Solo <b>19</b> se derivaron: el resto de los comercios quedó en el embudo del consumidor (ver Venta · CRM › B2B).", "ven",
          big="38%", txt="de las consultas de este anuncio son comercios que quieren revender (46 de 120). En el resto de la cuenta, 3 de cada 100.",
          cmp=cmpbar(38, 3, "resto de la cuenta 3%", "este anuncio · comercios", "promedio del resto de los anuncios"))}
</div></div>'''

    conj = f'''<div class="stab st-conj"><div class="igrid">
{_conj_card("Retargeting · visitó la web", "subir", "Retargeting a quien ya visitó la web: llega decidido y califica 59%",
            ["Es gente que ya conoce PAVIR: <b>92%</b> responde al agente (promedio de la cuenta: 82%).", "<b>59%</b> califica y <b>27%</b> pide cotización.", "Audiencia chica (38.000 personas, frecuencia 2,7): subir presupuesto con techo para no saturar."])}
{_conj_card("Intereses · Construcción", "mant", "Intereses de construcción: el conjunto que más volumen calificado trae",
            ["<b>440 consultas</b> entre dos anuncios: el conjunto más grande de la cuenta.", "<b>47%</b> califica, por encima del promedio.", "El video de la Clásica trae volumen; la imagen premium, ticket alto: conviven bien."])}
{_conj_card("Broad · consumidor final", "paus", "Público amplio sin segmentar: mucho volumen, 19% califica",
            ["<b>300 consultas</b>, pero solo <b>57</b> calificaron.", "1 de cada 3 no respondió al agente: muchos sin obra en curso.", "Cuesta <b>$1.754</b> por calificada, más del doble del promedio."])}
{_conj_card("Lookalike · distribuidores", "prob", "Público parecido a los distribuidores: 38% son comercios que quieren revender",
            ["La audiencia se arma con el padrón de distribuidores (público similar en Meta).", "<b>46 de 120</b> consultas son comercios: es captación de red, no de consumidor.", "Medirlo por altas de distribuidores, no por calificadas de consumidor."], "ven",
            big="38%", txt="de las consultas de este conjunto son comercios. En el resto de los conjuntos, 3 de cada 100.", cmp=cmpbar(38, 3, "resto 3%", "este conjunto · comercios", "promedio del resto de los conjuntos"))}
{_conj_card("Intereses · Obra nueva", "subir", "Intereses de obra nueva: quien está construyendo califica 52%",
            ["Pide ventanas PVC en medidas estándar: el agente cotiza sin derivar dudas técnicas.", "<b>88 de 170</b> calificaron.", "Es el mejor conjunto de la campaña de ventanas."])}
{_conj_card("Intereses · Reformas", "corr", "Intereses de reformas: 40% califica y pregunta por colores fuera de stock",
            ["<b>64 de 190</b> preguntan por colores especiales.", "Quien reforma compara más: <b>13%</b> pide cotización, la tasa más baja.", "Cambiar el carrusel a los colores en stock antes de sumar presupuesto."])}
</div>
<div class="mt">{table(["Conjunto", "Campaña", "Anuncios", "Inversión", "Consultas", "% califica", "Costo por calificada", "Comercios (B2B)"],
    [[f"<b>{cj}</b>", ads[0]["camp"], str(len(ads)), f'${fmt(D.agg(ads)["gasto"])}', str(D.agg(ads)["cons"]), f'{D.agg(ads)["pcal"]}%{minibar(D.agg(ads)["pcal"], "var(--vio)")}', f'${fmt(D.agg(ads)["ccal"])}', str(D.agg(ads)["b2b"])]
     for cj, ads in sorted(D.CONJS.items(), key=lambda kv_: -D.agg(kv_[1])["pcal"])], 820)}</div></div>'''

    com = f'''<div class="stab st-com">
{banner("info", "info", "Insights sobre la red de distribuidores. No vienen de un anuncio: vienen del padrón y los pedidos (export de Producí) cruzados con el CRM. Por eso el contexto de cada card es <b>segmento · fuente · base</b> en vez de campaña · conjunto · anuncio.")}
<div class="igrid mt">
{i3("cruz", f"Ofrecer ventanas a los {D.SOLO_PUERTAS} distribuidores que hoy compran solo puertas",
    [("Segmento", "Activos que nunca pidieron ventanas"), ("Fuente", "Pedidos de 90 días (Producí)"), ("Base", f"{D.ACTIVOS} distribuidores activos")],
    [f"<b>{D.SOLO_PUERTAS} distribuidores</b> compran solo puertas; 352 ya compran las dos líneas.", "Con <b>10 puertas</b> ya acceden al descuento: sumar ventanas no cambia la condición.", "Es ticket extra <b>sin costo de captación</b>: el cliente ya existe."],
    "0%", f"de estos {D.SOLO_PUERTAS} compra ventanas hoy. En la red activa, 70 de cada 100 compran las dos líneas (352 de 500).",
    cmpbar(1, 70, "red activa 70% cruza", "estos distribuidores", "toda la red activa"), own("ven"), lab2="Qué muestra el cruce", lab3="Resultado contra el resto de la red")}
{i3("cuidar", "100 distribuidores hacen 68 de cada 100 pesos de venta",
    [("Segmento", "Top 100 por volumen"), ("Fuente", "Pedidos de 90 días (Producí)"), ("Base", f"{D.ACTIVOS} distribuidores activos")],
    ["El 20% de la red concentra el <b>68%</b> de la facturación.", "Compran cada 7 a 10 días: una visita perdida es un pedido perdido.", "Retenerlos rinde más que captar distribuidores nuevos."],
    "68%", "de la facturación sale del 20% de la red.",
    cmpbar(68, 20, "20% de la red", "facturación del top 100", "porción de la red que representan"), own("ven"), lab2="Qué muestra el cruce", lab3="Resultado")}
{i3("react", f"{D.TOCA_COMPRAR} distribuidores entraron en su ventana de recompra antes del valle de diciembre",
    [("Segmento", "Activos que compran cada 7 a 10 días"), ("Fuente", "Pedidos (Producí) + CRM"), ("Base", "218 distribuidores de compra frecuente")],
    ["Pico de pedidos en <b>marzo-mayo</b>, piso en <b>diciembre-febrero</b>.", "Un incentivo ahora adelanta el pedido y llena la planta antes del valle.", f"<b>{D.TOCA_COMPRAR}</b> ya están en ventana y no pidieron."],
    "62%", "de la red activa recompró a 30 días. El objetivo es 75%.",
    cmpbar(62, 75, "objetivo 75%", "recompra actual", "objetivo con alerta de ventana"), own("ven"), lab2="Qué muestra el cruce", lab3="Resultado contra el objetivo")}
{i3("cobrar", f"{D.VENCIDOS} distribuidores con deuda vencida a más de 30 días frenan el despacho",
    [("Segmento", "Cuenta corriente vencida +30 días"), ("Fuente", "Cuentas por cobrar (Producí)"), ("Base", f"{D.RED} distribuidores en el padrón")],
    [f"<b>{money(D.VENCIDO_M)}</b> vencido, de {money(D.DEUDA_M)} en calle.", "Regla comercial: con deuda vencida, se cobra antes de despachar.", "El estado de cuenta automático por WhatsApp acelera el cobro sin sumar trabajo."],
    "4%", f"de la red tiene deuda vencida ({D.VENCIDOS} de {D.RED}). 12% tiene algún saldo.",
    cmpbar(4, 12, "con algún saldo 12%", "vencido +30 días", "con algún saldo pendiente"), own("cob"), lab2="Qué muestra el cruce", lab3="Resultado")}
</div></div>'''

    regla = f'''<div class="adv">{eyebrow("Cómo se decide cada sello · modo avanzado")}
{mincard("Criterio · cuantitativo, sobre el objetivo real de la campaña", "Meta mide conversaciones; el sello se decide por lo que pasa en el CRM",
         kv([(f"{AVG}%", "califica · promedio de la cuenta"), (f"${fmt(CAVG)}", "costo por calificada · promedio"), ("1.560", "consultas de Meta en el mes")]) +
         ul(["<b>Subir</b>: califica más de 50% y cuesta menos que el promedio por calificada.", "<b>Mantener</b>: entre 40% y 50%, o volumen alto con costo en el promedio.",
             "<b>Corregir</b>: el anuncio promete algo que el CRM muestra como problema (stock, color, plazo).", "<b>Pausar</b>: califica menos de 25% o cuesta más del doble del promedio.",
             "<b>Probar</b>: trae otro tipo de cliente (comercios) y se mide con otra vara."]), "target", "", "", True)}
</div>'''

    return f'''<section class="panel p-insights">
{sec_head("Insights · resultado de cada anuncio medido en el CRM", "Qué anuncio trae compradores, <em>y cuál no.</em>",
          ("Cada card toma un <b>anuncio</b> o un <b>conjunto de anuncios</b> de Meta y mide qué pasó con esas consultas dentro de Prometheo: cuántas calificaron, cuántas se derivaron y cuántas llegaron a una fecha. El objetivo de todas las campañas es <b>Mensajes</b>: Meta lo da por cumplido con la conversación; el CRM muestra si esa conversación sirvió.", "Cruce por <b>ID de anuncio</b> entre el export de Meta y las variables de Prometheo. Métrica de decisión: <b>% que califica</b> y <b>costo por consulta calificada</b> contra el promedio de la cuenta. Abrí cada card: en este modo se suma la lectura técnica (CTR, frecuencia, CPC) con cada sigla explicada."))}
{grupal}
{eyebrow("Cómo leer cada card · campaña › conjunto › anuncio")}
{hier}
<div class="subtabs instabs"><label for="in-anun">{ic("anun")}Por anuncio</label><label for="in-conj">{ic("conj")}Por conjunto de anuncios</label><label for="in-com">{ic("building")}Comercial · red de distribuidores</label></div>
{anun}{conj}{com}
{regla}
</section>'''
