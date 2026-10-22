"""Genera tableros/MIA_Tablero_IC.html con la estética del tablero de referencia de EDFAN.

Uso: python3 tableros/build_mia.py <ruta al HTML de referencia de EDFAN>
Toma del HTML de referencia el CSS, los íconos SVG, el logo y los scripts; el contenido es de MIA.
Todos los números son modelados (no hay export de Prometheo).
"""
import re
import sys
from pathlib import Path

REF = Path(sys.argv[1])
OUT = Path(__file__).with_name("MIA_Tablero_IC.html")
ref = REF.read_text(encoding="utf-8")

head = ref[: ref.index('<input type="radio" name="nav"')]
head = head.replace("<title>EDFAN IC Demo</title>", "<title>MIA IC Demo</title>")
logo = re.search(r'<img class="tb-logo" src="([^"]+)"', ref).group(1)
scripts = ref[ref.rindex("</details></div></div><div class=\"yeq\">"):]
scripts = scripts[scripts.index("<script>"):].replace("edfan", "mia")


# ---------- helpers ----------
def ic(name, style=""):
    st = f' style="{style}"' if style else ""
    return f'<svg class="i"{st}><use href="#i-{name}"/></svg>'


def n(x, d=0):
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def ars(x):
    return "$" + n(round(x))


SRC = {
    "pro": ("qt", "chat", "Prometheo"),
    "meta": ("s-meta", "meta", "Meta Ads"),
    "tt": ("s-tt", "play", "TikTok Ads"),
    "mail": ("s-mail", "mail", "Email"),
    "wpp": ("s-wpp", "wa", "WhatsApp Mkt"),
    "calc": ("qbw", "sigma", "Cálculo"),
    "erp": ("s-erp", "ledger", "Registro de altas"),
}


def src(k):
    c, i, t = SRC[k]
    return f'<span class="qq {c}">{ic(i)}{t}</span>'


def kpi(icon, tone, s, label, value, delta="", up=True, bsc="", adv="", qcp="", flat=False):
    d = ""
    if delta:
        cls = "d-flat" if flat else "qbr" if up else "qbr dn"
        d = f'<span class="qbt {cls}">{ic("up" if delta.startswith("+") else "down")}{delta}</span>'
    z = f'<span class="bsc">{bsc}</span><span class="adv">{adv or bsc}</span>' if bsc else ""
    p = f'<div class="qcp">{qcp}</div>' if qcp else ""
    return (f'<div class="qbu"><div class="qba"><div class="qbk {tone}">{ic(icon)}</div>{src(s)}</div>'
            f'<div class="qbv">{label}</div><div class="qbb"><div class="qy">{value}</div>{d}</div>'
            f'<div class="qz">{z}</div>{p}</div>')


def head_sec(kick, title, em, bsc, adv):
    return (f'<div class="qo"><div class="qr"><span class="qv"></span>{kick}</div>'
            f'<h1 class="sec">{title} <em>{em}</em></h1>'
            f'<p class="qcq"><span class="bsc">{bsc}</span><span class="adv">{adv}</span></p></div>')


def sub(t):
    return f'<div class="qo"><div class="qr"><span class="qv"></span>{t}</div></div>'


def yeq(t):
    return f'<div class="yeq">{ic("arrow")}<div><b>Y entonces qué</b><span>{t}</span></div></div>'


def bars(title, s, rows, note="", right="", color="var(--vio)"):
    m = max(r[1] for r in rows)
    out = "".join(
        f'<div class="qi"><span class="qj">{r[0]}</span><span class="qk">{r[2] if len(r) > 2 else n(r[1])}'
        f'{"<span>" + r[3] + "</span>" if len(r) > 3 else ""}</span>'
        f'<div class="qf"><div class="qh" style="width:{100 * r[1] / m:.1f}%;background:{color}"></div></div></div>'
        for r in rows)
    nt = f'<p class="qcm">{note}</p>' if note else ""
    rr = f'<span class="r">{right}</span>' if right else ""
    return f'<div class="qx"><div class="qw">{ic("pie")}{title}{src(s)}{rr}</div>{out}{nt}</div>'


def table(head_cells, rows, tot=None, minw=640):
    th = "".join(f"<th>{h}</th>" for h in head_cells)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    if tot:
        tr += '<tr class="tot">' + "".join(f"<td><b>{c}</b></td>" for c in tot) + "</tr>"
    return (f'<div class="qcf" style="overflow:hidden"><div class="tblwrap"><table style="min-width:{minw}px">'
            f"<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div></div>")


def steps(items, note=""):
    out = []
    for i, (lab, val, txt, p) in enumerate(items):
        out.append(f'<div class="fs"><div class="t"><span>{i + 1:02d}</span><span class="p">{p}</span></div>'
                   f'<div class="l">{lab}</div><div class="v"><b>{val}</b> {txt}</div>'
                   f'<div class="qbf"><span>{"base" if not i else "pasa " + p}</span></div></div>')
    nt = f'<div class="qcm">{note}</div>' if note else ""
    return f'<div class="fsteps" style="--n:{len(items)}">{"".join(out)}</div>{nt}'


def band(score):
    return "alta" if score >= 80 else "media" if score >= 55 else "hipotesis" if score >= 30 else "criterio"


BAND_TXT = {"alta": "basada en datos", "media": "informada por datos", "hipotesis": "hipótesis", "criterio": "criterio"}


def sx(score, label=False):
    b = band(score)
    on = 4 if score >= 80 else 3 if score >= 55 else 2 if score >= 30 else 1
    segs = "".join(f'<i class="{"on" if k < on else ""}"></i>' for k in range(4))
    em = f"<em>{BAND_TXT[b]}</em>" if label else ""
    return (f'<span class="sx" data-b="{b}" title="Índice Data Driven {score}%: {BAND_TXT[b]}. Cuánto de esta acción '
            f'se apoya en datos verificables. Rúbrica v1, sin calibrar.">{ic("gauge")}<b>{score}<small>%</small></b>'
            f'<span class="qs">{segs}</span>{em}</span>')


DD_LEGEND = (f'<div class="sxl">{ic("gauge")}<b>Índice Data Driven</b><span>cuánto de cada acción se apoya en datos:</span>'
             '<span class="qbe" data-b="alta"><i></i>80+ basada en datos</span><span class="qbe" data-b="media"><i></i>55–79 informada</span>'
             '<span class="qbe" data-b="hipotesis"><i></i>30–54 hipótesis</span><span class="qbe" data-b="criterio"><i></i>menos de 30 criterio</span></div>')

VERB_IC = {"activar": "bolt", "proteger": "shield", "corregir": "wrench", "separar": "layers", "medir": "pulse", "decidir": "compass"}
OWNER = {"Ventas": "o-ven", "Marketing": "o-mkt", "AUREA": "o-aurea", "Dirección": "o-cob"}


RUB_NAMES = ["Base y denominador", "Fuente y trazabilidad", "Cobertura", "Profundidad", "Evidencia previa", "Cierre medible"]
RUB_MAX = [20, 15, 15, 20, 15, 15]
TECHO = 54  # dato modelado: techo de la regla R2 de aurea-ic-dashboard


def score_of(c):
    return min(sum(c["rub"]), TECHO)


def action(c, extra=False):
    total = sum(c["rub"])
    score = score_of(c)
    rub = "".join(f'<div class="qd"><span>{k}</span><span class="qe"><i style="width:{100 * a / b:.0f}%"></i></span><b>{a}/{b}</b></div>'
                  for k, a, b in zip(RUB_NAMES, c["rub"], RUB_MAX))
    techo = f"Suma de la rúbrica {total}; con dato modelado el techo es {TECHO}." if total > TECHO else f"Suma de la rúbrica {total}, por debajo del techo de {TECHO} por dato modelado."
    cls = "i3 av adv" if extra else "i3 av"
    return (f'<details class="{cls}" data-v="{c["v"]}"><summary><div class="qbg"><span class="qby"><span class="qcd">{ic(VERB_IC[c["v"]])}</span>{c["v"].capitalize()}</span>'
            f'<span class="qce {OWNER[c["owner"]]}">{c["owner"]}</span>{sx(score)}</div><div class="qbl">{c["title"]}</div>'
            f'<div class="qbh"><div class="cx"><span class="ql qbm">{ic("target")}</span><span class="qm">Qué mide</span><span class="qn">{c["mide"]}</span></div>'
            f'<div class="cx"><span class="ql qbi">{ic("filter")}</span><span class="qm">Base</span><span class="qn">{c["base"]}</span></div>'
            f'<div class="cx"><span class="ql qbn">{ic("chat")}</span><span class="qm">Dato</span><span class="qn">{c["dato"]}</span></div></div>'
            f'<div class="ad-do">{ic("arrow")}<div><b>Qué hacemos</b><span>{c["corto"]}</span></div></div>'
            f'<div class="ad-meta"><span>{ic("user")}<b>{c["owner"]}</b></span><span>{ic("clock")}<b>{c["cuando"]}</b></span><span>{ic("target")}<b>{c["meta"]}</b></span></div>'
            f'<div class="qbd"><span class="op">Ver el detalle: dónde, cómo se mide y por qué este índice</span><span class="cl">Plegar</span>{ic("chev")}</div></summary>'
            f'<div class="qa"><div class="qb"><span class="n">{ic("arrow")}</span>Qué hacer</div><p class="qp">{c["hacer"]}</p>'
            f'<div class="qu">{ic("pin")}<span><b>Dónde se cambia:</b> {c["donde"]}</span></div></div>'
            f'<div class="qa"><div class="qb"><span class="n">{ic("target")}</span>Efecto esperado</div><p class="qp">{c["efecto"]}</p></div>'
            f'<div class="qa"><div class="qb"><span class="n">{ic("pulse")}</span>Cómo lo medimos</div><p class="qp">{c["medimos"]}</p>'
            f'<div class="qbs">{ic("shield")}<span><b>Guardiana:</b> {c["guardiana"]}</span></div></div>'
            f'<div class="qa qbo"><div class="qb"><span class="n">{ic("gauge")}</span>Por qué este índice Data Driven {sx(score, True)}</div>'
            f'<div class="qbz">{rub}</div><p class="qbj">{c["porque"]} {techo} Rúbrica v1, sin calibrar: el resultado se registra al cierre del período.</p></div></details>')


def adx(a, color):
    ok = a["calif"] / a["anun"] if a["anun"] else 0
    s1 = "good" if ok >= .35 else "warn" if ok >= .2 else "crit"
    cpc = a["gasto"] / a["calif"] if a["calif"] else 0
    s2 = "good" if a["susc"] >= 4 else "warn" if a["susc"] >= 1 else "crit"
    mx = a["conv"]
    fun = "".join(f'<div class="qcb"><span>{k}</span><i style="width:{100 * v / mx:.0f}%"></i><b>{v}</b></div>'
                  for k, v in [("Anunciantes", a["anun"]), ("Calificados", a["calif"]), ("Hot leads", a["hot"]), ("Demos", a["demos"]), ("Altas", a["susc"])])
    vc = {"good": "var(--good);--vb:var(--good-bg)", "warn": "var(--warn);--vb:var(--warn-bg)", "crit": "var(--crit);--vb:var(--crit-bg)"}[s2]
    return (f'<div class="adx" style="--ax:{color};--axb:color-mix(in srgb,{color} 14%,transparent)"><div class="adx-h"><span class="adx-ic">{ic("anun")}</span>'
            f'<div style="min-width:0"><b>{a["id"]} · {a["nombre"]}</b><span>{ic("target")}{a["publico"]} · {a["canal"]}</span></div></div>'
            f'<div class="adx-tiles"><div class="qch"><span>{ic("chat")}Charlas</span><b>{a["conv"]}</b></div>'
            f'<div class="qch" data-s="{s1}"><span>{ic("checkc")}Califica</span><b>{100 * ok:.0f}%</b></div>'
            f'<div class="qch" data-s="{s2}"><span>{ic("lock")}Altas</span><b>{a["susc"]}</b></div></div>'
            f'<div class="adx-fun">{fun}</div><div class="adx-v" style="--vc:{vc}">{ic("bulb")}<span>{a["lectura"]} · Costo por calificado {ars(cpc) if cpc else "–"}.</span></div></div>')


# ---------- datos modelados ----------
PLAN = 45000
ADS = [
    dict(id="TT-01", canal="TikTok", nombre="Publicá gratis tu propiedad", publico="Dueños directos", gasto=380000, imp=410000, alc=236000, clics=5330, inter=9120, conv=142, anun=118, calif=41, hot=14, demos=15, susc=5, v3=38, v6=24, q=(61, 40, 27, 18), pixel=210, lectura="Sostener: volumen de dueños con buena calificación"),
    dict(id="TT-02", canal="TikTok", nombre="MIA Map: precios por barrio", publico="Buscadores", gasto=300000, imp=520000, alc=301000, clics=7800, inter=18400, conv=188, anun=12, calif=3, hot=1, demos=1, susc=0, v3=46, v6=31, q=(70, 52, 38, 29), pixel=340, lectura="Mover: el mejor gancho, pero trae buscadores"),
    dict(id="TT-03", canal="TikTok", nombre="Simulador de crédito UVA", publico="Inversores", gasto=220000, imp=290000, alc=182000, clics=3480, inter=6200, conv=74, anun=9, calif=4, hot=2, demos=2, susc=1, v3=35, v6=22, q=(58, 37, 24, 16), pixel=150, lectura="Medir: muestra chica de anunciantes"),
    dict(id="TT-04", canal="TikTok", nombre="Inmobiliarias: subí tu cartera", publico="Inmobiliarias", gasto=260000, imp=180000, alc=120000, clics=1980, inter=2650, conv=61, anun=54, calif=29, hot=11, demos=12, susc=4, v3=29, v6=17, q=(49, 30, 18, 11), pixel=66, lectura="Escalar: la que más vende por peso en TikTok"),
    dict(id="IG-01", canal="Instagram", nombre="Reel Amoblador con IA", publico="Buscadores", gasto=280000, imp=340000, alc=190000, clics=4080, inter=11300, conv=121, anun=22, calif=8, hot=3, demos=3, susc=1, lectura="Separar: pasa a objetivo descarga de app"),
    dict(id="IG-02", canal="Instagram", nombre="Carrusel Plan inmobiliarias", publico="Inmobiliarias", gasto=310000, imp=210000, alc=128000, clics=2310, inter=3100, conv=96, anun=81, calif=38, hot=12, demos=14, susc=5, lectura="Sostener: la que más califica de Meta"),
    dict(id="IG-03", canal="Instagram", nombre="Click to WhatsApp Demo gratis", publico="Inmobiliarias", gasto=350000, imp=230000, alc=141000, clics=2760, inter=2900, conv=168, anun=102, calif=34, hot=13, demos=12, susc=4, lectura="Sostener: más anunciantes por peso"),
    dict(id="FB-01", canal="Facebook", nombre="Vendé sin intermediarios", publico="Dueños directos", gasto=240000, imp=260000, alc=150000, clics=2860, inter=4100, conv=109, anun=88, calif=22, hot=6, demos=6, susc=2, lectura="Ajustar: dueños con una sola propiedad"),
    dict(id="FB-02", canal="Facebook", nombre="Bolsa de Pedidos", publico="Inmobiliarias", gasto=160000, imp=150000, alc=96000, clics=1350, inter=1700, conv=47, anun=31, calif=9, hot=2, demos=2, susc=1, lectura="Medir: muestra chica"),
]
COLOR = {"TikTok": "#EE1D52", "Instagram": "var(--pnk)", "Facebook": "var(--src-meta)"}


def wilson(k, m):
    if not m:
        return 0, 0
    z = 1.96
    p = k / m
    d = 1 + z * z / m
    c = p + z * z / (2 * m)
    r = z * ((p * (1 - p) / m + z * z / (4 * m * m)) ** .5)
    return (c - r) / d, (c + r) / d


def ads_table(rows, total_label):
    body = []
    t = dict(gasto=0, imp=0, clics=0, conv=0, anun=0, calif=0, demos=0, susc=0)
    for a in rows:
        for k in t:
            t[k] += a[k]
        lo, hi = wilson(a["calif"], a["anun"])
        small = ' <span class="lvl" style="background:var(--warn-bg);color:var(--warn-ink)">n&lt;30</span>' if a["anun"] < 30 else ""
        body.append([f'<b>{a["id"]}</b> <span class="sub" style="display:inline">{a["nombre"]}</span>', ars(a["gasto"]), n(a["imp"]), n(a["clics"]),
                     f'{100 * a["clics"] / a["imp"]:.2f}%'.replace(".", ","), a["conv"], a["anun"], f'{a["calif"]}{small}',
                     f'{100 * a["calif"] / a["anun"]:.0f}% <span class="sub" style="display:inline">({100 * lo:.0f}–{100 * hi:.0f})</span>',
                     a["hot"], a["demos"], f'<b>{a["susc"]}</b>', ars(a["gasto"] / a["calif"]) if a["calif"] else "–",
                     ars(a["gasto"] / a["susc"]) if a["susc"] else "–", n(a["susc"] * PLAN * 12 / a["gasto"], 1) + "x"])
    tot = [total_label, ars(t["gasto"]), n(t["imp"]), n(t["clics"]), f'{100 * t["clics"] / t["imp"]:.2f}%'.replace(".", ","), t["conv"], t["anun"], t["calif"],
           f'{100 * t["calif"] / t["anun"]:.0f}%', "", t["demos"], t["susc"], ars(t["gasto"] / t["calif"]), ars(t["gasto"] / t["susc"]) if t["susc"] else "–",
           n(t["susc"] * PLAN * 12 / t["gasto"], 1) + "x"]
    hd = ["Pauta", f'Gasto {src("meta" if rows[0]["canal"] != "TikTok" else "tt")}', "Impresiones", "Clics", "CTR",
          f'Charlas {src("pro")}', "Anunciantes", "Calificados", "% califica (IC 95%)", "Hot", "Demos", "Altas",
          f'Costo por calificado {src("calc")}', "Costo por alta (CAC)", "ROAS 12m"]
    return table(hd, body, tot, minw=1180)


# ---------- paneles ----------
P = {}

P["panorama"] = (
    '<div class="iobar"><span class="demo-tag">' + ic("info") + 'Dato ilustrativo</span><span class="iohint">Demo de Inteligencia Comercial para MIA · cifras modeladas con la estructura real de Prometheo</span></div>'
    '<div class="hero-grid"><div class="hero"><div class="hero-sph sph-bg"></div><div class="hero-top"><span class="hero-kick">Panorama · 1 al 15 de octubre 2026</span><span class="hero-per">comparado con la quincena anterior</span></div>'
    '<div class="hero-h">1.840 conversaciones en quince días, <em>dos de cada tres resueltas sin intervención humana.</em></div>'
    '<div class="hero-sub"><span class="bsc"><b>+8%</b> contra la quincena anterior, por los cinco canales. El agente cerró <b>1.214 charlas</b> sin derivarlas, entre <b>181 y 236 anunciantes</b> calificaron y <b>29</b> se dieron de alta.</span>'
    '<span class="adv">1.840 conversaciones (+7,9%) · 610 anunciantes · 181 a 236 calificados (30% a 39% de los anunciantes, criterio a validar) · 78 demos · 29 altas. Costo por calificado de la pauta paga: $13.351.</span></div>'
    '<div class="chart-scale"><span>Conversaciones por día · mín 98 · máx 142</span><span>más es mejor ↑</span></div>'
    '<div class="hchart"><svg viewBox="0 0 600 150" preserveAspectRatio="none" role="img"><defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'
    '<path d="M 6 88 L 90 80 L 174 72 L 258 66 L 342 70 L 426 52 L 510 44 L 594 30 L 594 150 L 6 150 Z" fill="url(#hg)"/><path d="M 6 88 L 90 80 L 174 72 L 258 66 L 342 70 L 426 52 L 510 44 L 594 30" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"/><circle cx="594" cy="30" r="4.5" fill="#fff"/></svg>'
    '<div class="endtag" style="top:calc(20% - 4px)">142<span>15 oct</span></div></div><div class="chart-x"><span>1 oct</span><span>5 oct</span><span>10 oct</span><span>15 oct</span></div>'
    '<div class="hero-stats"><div class="hs"><div class="l">Charlas por día</div><div class="v">123</div><div class="m">1.840 en la quincena</div></div>'
    '<div class="hs"><div class="l">Resueltas sin contacto humano</div><div class="v">66%</div><div class="m">1.214 de 1.840</div></div>'
    '<div class="hs"><div class="l">Pauta que más vende</div><div class="v">IG-02 · TT-01</div><div class="m">5 altas cada una</div></div></div></div>'
    f'<div class="hero-pink"><div class="hp-top"><div class="hp-row"><div class="hp-ic">{ic("lock")}</div><span class="hp-chip">Altas de suscripción</span></div>'
    '<svg class="hp-spk" viewBox="0 0 300 60" preserveAspectRatio="none" role="img"><polyline points="4,50 62,44 120,40 178,30 236,22 296,8" fill="none" stroke="rgba(255,255,255,.85)" stroke-width="2" vector-effect="non-scaling-stroke" stroke-linejoin="round"/></svg>'
    '<div><div class="hp-l">Altas por quincena · mín 14 · máx 29</div><div class="hp-v">29</div><div class="hp-d"><span class="pin">+4 vs quincena anterior</span> inmobiliarias, dueños y desarrolladoras con plan pago</div></div></div>'
    '<div class="hp-foot"><div class="mini"><b>78</b><span>Demos</span></div><div class="hp-sp"></div><div class="mini"><b>70</b><span>Hot leads</span></div><div class="hp-sp"></div><div class="mini"><b>37%</b><span>De demo a alta</span></div></div></div></div>'
    '<div class="g4">'
    + kpi("chat", "blu", "pro", "Conversaciones", "1.840", "+7,9%", bsc="Personas que escribieron por cualquiera de los 5 canales.", adv="1.840 contra 1.706 · 610 anunciantes, 1.020 buscadores, 210 soporte u otros.", qcp="<b>Conversación</b>: contacto nuevo o reactivado en Prometheo, por fecha de ingreso.")
    + kpi("checkc", "grn", "pro", "Resueltas sin contacto humano", "1.214", "+21%", bsc="66% de todas las charlas, sin que nadie del equipo escriba.", adv="1.214 de 1.840 · quincena anterior 1.003 de 1.706 (58,8%).", qcp="Tag <b>Resuelto sin humano</b> y variable resuelto_por = agente.")
    + kpi("target", "", "calc", "Anunciantes calificados · rango", "181–236", "+12%", bsc="30% a 39% de los anunciantes · criterio propuesto, a validar con MIA.", adv="Estricto 181 (3 de 4 sumas) · amplio 236 (2 de 4) sobre 610 anunciantes · quincena anterior 210 (amplio).", qcp="<b>Calificado (propuesta)</b>: anunciante en zona y operación que MIA cubre + 2 de 4: propiedades activas, paga otro portal, plan de interés, decisor.")
    + kpi("lock", "pnk", "erp", "Altas de suscripción", "29", "+4", bsc="37% de las demos terminó en alta.", adv="Cruce del tag Suscripto con el registro de altas de MIA.", qcp="<b>Alta</b>: plan pago activado.")
    + '</div><div class="adv mt"><div class="g4">'
    + kpi("dollar", "", "calc", "Costo por calificado · pauta paga", "$13.351", "+7,7%", up=False, bsc="TikTok + Meta ÷ sus calificados · menos es mejor", qcp="$2.500.000 ÷ 188 calificados atribuidos.")
    + kpi("flame", "amb", "pro", "Hot leads", "70", "+9%", bsc="9 sin seguimiento en 24 h.", qcp="<b>Hot lead</b>: pide demo, precio de un plan o tiene más de 10 propiedades para subir ya.")
    + kpi("users", "blu", "pro", "Derivadas a humano", "418", "+3%", bsc="23% de las charlas, casi todas de anunciantes.")
    + kpi("dollar", "grn", "calc", "ROAS 12 meses", "6,3x", "+0,9x", bsc="Altas × plan de $45.000 × 12 ÷ gasto pauta.", qcp="Modelado, sin bajas.")
    + "</div></div>"
    + sub("Origen de la demanda · por canal de entrada a Prometheo")
    + '<div class="g2">'
    + bars("Conversaciones por canal", "pro", [("WhatsApp", 820), ("Instagram DM", 430), ("TikTok DM", 260), ("Facebook Messenger", 210), ("Gmail", 120)], "Todos los canales entran por Prometheo: un solo CRM, un solo conteo.")
    + bars("Tipo de contacto", "pro", [("Buscador (compra, alquiler, inversión)", 1020), ("Inmobiliaria", 310), ("Dueño directo", 260), ("Soporte de la app", 150), ("Spam u otros", 60), ("Desarrolladora", 40)], "Solo el anunciante entra a calificación. El buscador se mide como demanda.", color="var(--blu)")
    + "</div>"
    + sub("Recorrido · de la charla al alta")
    + '<div class="qcf pad"><div class="qw">' + ic("route") + 'De la charla al alta · el recorrido del anunciante<span class="r">base: 1.840 conversaciones</span></div>'
    + steps([("Conversaciones", "1.840", "todos los canales", ""), ("Anunciantes", "610", "inmobiliarias, dueños, desarrolladoras", "33%"),
             ("Calificados", "236", "criterio propuesto", "39%"), ("Demo agendada", "78", "tag Demo agendada", "33%"), ("Alta", "29", "plan pago", "37%")],
            "El paso más flojo es de anunciante a calificado: 121 no califican porque falta el dato de cuántas propiedades manejan.")
    + "</div>"
    + yeq("El agente resuelve solo 2 de cada 3 charlas y la pauta dirigida a inmobiliarias es la que vende. La pauta a buscadores llena el CRM pero no da altas: ver Pauta → Venta en Canales Marketing.")
)

WEEKS = ["S1 sep", "S2 sep", "S3 sep", "S4 sep", "S1 oct", "S2 oct"]


def barchart(vals, color, fmt=lambda v: n(v), maxv=None):
    """Barras por tramo semanal con eje y grilla, como Evolución de EDFAN."""
    top = maxv or max(vals) * 1.15
    out = []
    for k in range(5):
        y = 206 - k * 46.5
        out.append(f'<line class="gl" x1="50" x2="992" y1="{y:.1f}" y2="{y:.1f}"/><text x="44" y="{y + 3:.1f}" text-anchor="end">{fmt(top * k / 4)}</text>')
    step = 942 / len(vals)
    for i, v in enumerate(vals):
        h = v / top * 186
        x = 50 + i * step + step * .2
        w = step * .6
        out.append(f'<rect x="{x:.1f}" y="{206 - h:.1f}" width="{w:.1f}" height="{h:.1f}" rx="3" fill="{color}" opacity="{1 if i >= len(vals) - 2 else .45}"/>'
                   f'<text x="{x + w / 2:.1f}" y="224" text-anchor="middle">{WEEKS[i]}</text>')
    out.append(f'<text class="lbl" x="{x + w / 2:.1f}" y="{206 - h - 4:.1f}" text-anchor="middle">{fmt(vals[-1])}</text>')
    return f'<svg class="chart" viewBox="0 0 1000 230" role="img" preserveAspectRatio="xMidYMid meet">{"".join(out)}</svg>'


def evo_card(icon, title, s, right, vals, color, legend, fmt=lambda v: n(v), maxv=None):
    return (f'<div class="qcf pad"><div class="qw">{ic(icon)}{title}{src(s)}<span class="r">{right}</span></div>'
            f'{barchart(vals, color, fmt, maxv)}<div class="chart-lg"><span><i style="background:{color}"></i>{legend}</span>'
            f'<span><i style="background:{color};opacity:.45"></i>quincenas anteriores</span></div></div>')


EV_CONV = [770, 810, 838, 868, 896, 944]
EV_CAL = [94, 102, 101, 109, 112, 124]
EV_ALTA = [10, 12, 12, 13, 13, 16]
EV_PCT = [34, 35, 36, 37, 38, 40]
EV_RES = [55, 57, 58, 60, 64, 68]
pct = lambda v: f"{v:.0f}%"
CANALES = [("TikTok Ads", 465, 193, 77, 30, 10), ("Meta Ads · Instagram", 385, 205, 80, 29, 10), ("Meta Ads · Facebook", 156, 119, 31, 8, 3),
           ("Email Marketing", 96, 28, 14, 4, 2), ("WhatsApp Marketing", 214, 38, 19, 5, 3), ("Orgánico y sin atribución", 524, 27, 15, 2, 1)]
P["evolucion"] = (
    head_sec("Evolución · semana a semana", "Conversaciones, calificados y altas", "por tramo semanal.",
             "Cómo vienen las conversaciones, cuántos anunciantes califican y cuántos terminan en alta.",
             "Cada quincena se divide en dos tramos semanales. 1 al 15 sep: 1.580 conversaciones, 196 calificados, 22 altas. 16 al 30 sep: 1.706, 210 y 25. 1 al 15 oct: 1.840, 236 y 29. En color pleno, la quincena actual.")
    + '<div class="g4">'
    + kpi("chat", "blu", "pro", "Conversaciones · quincena", "1.840", "+7,9%", bsc="1.706 · 1.580 las dos anteriores")
    + kpi("checkc", "", "calc", "Calificados · amplio", "236", "+12%", bsc="210 · 196 las dos anteriores")
    + kpi("lock", "pnk", "erp", "Altas", "29", "+16%", bsc="25 · 22 las dos anteriores")
    + kpi("pulse", "grn", "calc", "% de calificación", "39%", "+1,4 p.p.", bsc="sobre anunciantes · subió 6 semanas seguidas")
    + '</div><div class="g2">'
    + evo_card("chat", "Conversaciones por semana", "pro", f"mín {n(min(EV_CONV))} · máx {n(max(EV_CONV))}", EV_CONV, "var(--blu)", "Conversaciones · los 5 canales")
    + evo_card("checkc", "Calificados por semana", "calc", f"mín {min(EV_CAL)} · máx {max(EV_CAL)}", EV_CAL, "var(--good)", "Calificados · criterio propuesto a validar")
    + '</div><div class="g2">'
    + evo_card("lock", "Altas por semana", "erp", "total 1–15 sep 22 · 16–30 sep 25 · 1–15 oct 29", EV_ALTA, "var(--pnk)", "Altas de suscripción")
    + evo_card("pulse", "% de calificación por semana", "calc", f"de {EV_PCT[0]}% a {EV_PCT[-1]}%", EV_PCT, "var(--vio)", "Calificados ÷ anunciantes", pct, 50)
    + '</div><div class="adv"><div class="g2">'
    + evo_card("bot", "% resueltas sin contacto humano por semana", "pro", f"de {EV_RES[0]}% a {EV_RES[-1]}%", EV_RES, "var(--good)", "Resueltas sin contacto humano ÷ conversaciones", pct, 100)
    + '<div class="qcf" style="overflow:hidden"><div class="tblwrap"><table style="min-width:560px"><thead><tr><th>Canal · 1 al 15 oct</th><th>Charlas</th><th>Anunciantes</th><th>% califica</th><th>Demos</th><th>Altas</th></tr></thead><tbody>'
    + "".join(f"<tr><td><b>{c}</b></td><td>{n(ch)}</td><td>{an}</td><td>{100 * ca / an:.0f}%</td><td>{de}</td><td>{al}</td></tr>" for c, ch, an, ca, de, al in CANALES)
    + '</tbody></table></div><p class="qcm" style="padding:0 14px 12px">% califica sobre anunciantes de cada canal. Orgánico: 27 anunciantes, muestra chica.</p></div>'
    + "</div></div>"
    + yeq("Las conversaciones crecen todas las semanas y la calificación acompaña (de 34% a 40%). Las altas suben más despacio: dependen de que la demo se haga el mismo día, por eso la acción está en el seguimiento de hot leads.")
)

P["ventacrm"] = (
    head_sec("Venta · CRM · el estado de cada anunciante", "Quién califica, a quién atender primero", "y qué mejorar en el CRM.",
             "Qué tan bien califica el agente al anunciante y dónde se corta el embudo.", "El agente responde, explica planes y califica; el equipo hace la demo y da el alta. Base: 610 anunciantes de la quincena.")
    + f'<div class="cq"><div class="cq-top"><div><div class="cq-k">{ic("compass")}Criterio de calificación · propuesta a validar con MIA</div><div class="cq-t">Así calificaría MIA, <em>medido en sus conversaciones.</em></div>'
    '<div class="cq-s">Los dos obligatorios y al menos 2 de los 4 que suman. El hot lead se marca con una sola señal. Hasta que MIA lo valide, el número no titula: se muestra el rango.</div></div>'
    '<div class="cq-nums"><div><b>236</b><span>calificados</span><i>rango 181 a 236</i></div><div><b>70</b><span>hot leads</span><i>9 sin seguimiento</i></div><div><b>78</b><span>demo agendada</span><i>6 sin fecha</i></div></div></div>'
    '<div class="cq-rule"><div class="cq-col"><h6>Obligatorios · los dos</h6><span class="ch ob">Es anunciante <b>610</b></span><span class="ch ob">Zona y operación que MIA cubre <b>546</b></span></div><div class="cq-plus">+</div>'
    '<div class="cq-col"><h6>Suman · al menos 2 de 4</h6><span class="ch su">Propiedades activas para subir <b>354</b></span><span class="ch su">Paga otro portal <b>402</b></span><span class="ch su">Plan de interés <b>287</b></span><span class="ch su">Decisor en la charla <b>311</b></span></div>'
    '<div class="cq-plus">·</div><div class="cq-col"><h6>Hot lead · una señal alcanza</h6><span class="ch ho">Pide demo hoy</span><span class="ch ho">Pide precio de un plan</span><span class="ch ho">Más de 10 propiedades</span></div></div>'
    '<p class="cq-note">Estricto: 3 de 4 sumas = 181. Falta la definición de MIA (Doc 1, bloque B3) para que el número sea exacto.</p></div>'
    + '<div class="g4">'
    + kpi("users", "blu", "pro", "Anunciantes", "610", "+9%", bsc="33% de las charlas.")
    + kpi("checkc", "", "calc", "Calificados", "236", "+12%", bsc="39% de los anunciantes · estricto 181.")
    + kpi("flame", "amb", "pro", "Hot leads", "70", "+9%", bsc="9 sin seguimiento en 24 h.")
    + kpi("lock", "grn", "erp", "Demo → alta", "37%", "+2 p.p.", bsc="29 de 78 demos.")
    + "</div><div class=\"g2\">"
    + bars("Por qué no califican · 374", "calc", [("Sin cantidad de propiedades", 121), ("Menos de 2 sumas", 98), ("Zona sin cobertura de MIA", 64), ("No fit: solo quiere publicar gratis", 58), ("No fit: no decide (empleado)", 33)], "El primero es un faltante de captura, no de interés: se arregla en el prompt.", color="var(--warn)")
    + '<div class="adv">' + table(["Etapa (Smart Tag)", "Declarada", "Por evidencia", "Diferencia"], [["Calificado", 261, 236, "−25"], ["Demo agendada", 84, 78, "−6"], ["Alta", 29, 29, "0"]], minw=380)
    + '<p class="qcm">Etapa declarada por el tag vs etapa que cumple la definición. Se muestran las dos mientras no converjan.</p></div>'
    + "</div>"
    + yeq("236 calificados con la regla propuesta. El faltante más grande es la cantidad de propiedades: el agente no lo pregunta en Instagram ni en TikTok. Validar la definición con MIA antes de que el número titule.")
)

P["resueltas"] = (
    head_sec("Resueltas sin contacto humano", "1.214 conversaciones,", "cerradas por el agente sin que nadie del equipo escriba.",
             "Cuántas charlas resolvió el agente solo, en qué y por qué canal.", "Tag Resuelto sin humano + variable resuelto_por. Una charla resuelta es la que cierra con la respuesta dada y sin derivación ni intervención humana.")
    + '<div class="g4">'
    + kpi("checkc", "grn", "pro", "Resueltas sin contacto humano", "1.214", "+21%", bsc="66,0% de 1.840 conversaciones.")
    + kpi("pulse", "", "calc", "% resueltas", "66,0%", "+7,2 p.p.", bsc="quincena anterior 58,8% (1.003 de 1.706)")
    + kpi("users", "blu", "pro", "Derivadas a humano", "418", "+3%", flat=True, bsc="22,7% · casi todas de anunciantes")
    + kpi("clock", "pnk", "calc", "Horas de equipo ahorradas", "≈ 101 h", "+18 h", bsc="5 min por charla, supuesto a validar")
    + '</div><div class="adv mt"><div class="g4">'
    + kpi("bolt", "", "pro", "Primera respuesta del agente", "< 1 min", bsc="mediana de la quincena")
    + kpi("x", "amb", "pro", "Sin respuesta del contacto", "208", "−4%", bsc="11,3% · no escribieron después del primer mensaje")
    + kpi("repeat", "", "pro", "Reabiertas en 48 h", "41", bsc="3,4% de las resueltas · guardiana de la resolución")
    + kpi("chat", "blu", "pro", "Resueltas de buscadores", "870", bsc="85% de los 1.020 buscadores")
    + '</div></div>'
    + f'<div class="cq"><div class="cq-top"><div><div class="cq-k">{ic("bot")}Agente de MIA · Prometheo</div><div class="cq-t">Dos de cada tres charlas <em>no necesitaron a nadie.</em></div>'
    '<div class="cq-s">Equivale a unas 101 horas de atención del equipo en la quincena (5 minutos por charla, supuesto a validar).</div></div>'
    '<div class="cq-nums"><div><b>1.214</b><span>resueltas sin contacto humano</span><i>66,0% de 1.840 · antes 58,8%</i></div><div><b>418</b><span>derivadas a humano</span><i>22,7%</i></div><div><b>208</b><span>sin respuesta del contacto</span><i>11,3%</i></div></div></div>'
    '<div class="cq-grid"><div class="cq-box"><h6>' + ic("checkc") + 'Qué resolvió solo</h6><div class="cq-steps">'
    + "".join(f'<div class="cq-st"><i style="width:{w}%"></i><b>{v}</b><span>{t}</span></div>' for v, t, w in [(612, "Buscador · link a la app y filtros", 100), (258, "Buscador · MIA Tools (UVA, alquiler)", 42), (212, "Anunciante · planes y precios", 35), (132, "Soporte de la app", 22)])
    + '</div></div><div class="cq-box"><h6>' + ic("inb") + 'Por canal</h6><div class="cq-cmp">'
    + "".join(f'<div><span>{c}</span><b>{r}</b><i>de {t}</i><b>{100 * r / t:.0f}%</b><i></i></div>' for c, t, r in [("WhatsApp", 820, 520), ("Instagram DM", 430, 301), ("TikTok DM", 260, 196), ("Facebook", 210, 127), ("Gmail", 120, 70)])
    + '</div></div><div class="cq-box"><h6>' + ic("users") + 'Qué se derivó a humano · 418</h6><div class="cq-steps">'
    + "".join(f'<div class="cq-st"><i style="width:{w}%"></i><b>{v}</b><span>{t}</span></div>' for v, t, w in [(236, "Anunciante calificado → demo", 100), (98, "Anunciante con duda de contrato", 42), (52, "Reclamo o baja", 22), (32, "Desarrolladora (B2B)", 14)])
    + '</div><p>Que el anunciante llegue al humano está bien: es la venta.</p></div></div></div>'
    + yeq("El agente resuelve muy bien al buscador y responde planes y precios al anunciante. Lo que se deriva es casi todo venta. Guardiana: satisfacción en charlas resueltas, que hoy no se mide (ver Calidad de datos).")
)

P["demanda"] = (
    head_sec("Demanda · qué piden los buscadores", "Lo que busca la gente en MIA,", "para vendérselo a las inmobiliarias.",
             "Compradores, inquilinos e inversores: qué operación, dónde y con qué herramienta.", "Base: 1.020 buscadores. Sirve para el pitch a inmobiliarias: «esto te piden en tu zona».")
    + '<div class="g4">'
    + kpi("users", "blu", "pro", "Buscadores", "1.020", "+6%", bsc="55% de las conversaciones")
    + kpi("home", "", "pro", "Buscan alquilar", "54%", "+2 p.p.", bsc="551 de 1.020", adv="551 de 1.020 · compra 347 · inversión 122")
    + kpi("pin", "pnk", "pro", "Zona más pedida", "Córdoba Capital", bsc="214 consultas · 21% de los que declaran zona")
    + kpi("box", "amb", "pro", "Pedidos sin oferta", "167", "+11%", up=False, bsc="consultas sin avisos suficientes en MIA")
    + '</div>'
    + '<div class="g3">'
    + bars("Operación", "pro", [("Alquiler", 551, "54%"), ("Compra", 347, "34%"), ("Inversión", 122, "12%")])
    + bars("Zonas más pedidas", "pro", [("Córdoba Capital", 214), ("CABA", 198), ("GBA Norte", 143), ("Rosario", 97), ("La Plata", 66)], color="var(--blu)")
    + bars("MIA Tools consultadas", "pro", [("Simulador UVA", 188), ("MIA Map", 161), ("Calculadora de alquiler", 97), ("Amoblador IA", 74), ("Generador de contratos", 52)], color="var(--pnk)")
    + '</div><div class="adv mt">' + table(["Pedido sin oferta (Bolsa de Pedidos)", "Consultas", "Avisos activos en MIA", "Consultas por aviso"],
                                          [["Alquiler 2 amb. Córdoba Capital ≤ $450.000", 84, 21, "4,0"], ["Casa con patio GBA Norte, USD 90–130 mil", 61, 38, "1,6"], ["Campo 50–200 ha, inversión", 22, 4, "5,5"]], minw=560)
    + '<p class="qcm">Avisos activos: modelado. Con la base de MIA se cruza real.</p></div>'
    + yeq("El alquiler en Córdoba Capital tiene 4 consultas por aviso: es el argumento de venta para inmobiliarias cordobesas en la próxima pauta.")
)

P["criterio"] = (
    head_sec("Criterio comercial · sobre los 236 calificados", "Qué le duele al anunciante", "y qué lo hace escribir hoy.",
             "Los cinco campos del núcleo y a quién llamar primero.", "Perfil B2B de suscripción con recompra (inmobiliarias y desarrolladoras): capa variable Gap Selling + resultado de contacto. Impacto y causa raíz son señales blandas: sin refuerzo en el prompt nacen en Indicio.")
    + '<div class="g4">'
    + kpi("quote", "", "pro", "Problema declarado", "82%", bsc="193 de 236 calificados · Hecho")
    + kpi("flame", "amb", "pro", "Impacto alto", "48", bsc="27% de 175 con impacto cargado · Señal")
    + kpi("bolt", "blu", "pro", "Disparador hace menos de 30 días", "61%", bsc="91 de 149 con disparador · Señal")
    + kpi("cal", "grn", "pro", "Avance con fecha", "52", "+9", bsc="resultado de contacto cargado por el equipo")
    + '</div>'
    + table(["Campo", "Cobertura", "Nivel", "Valor más frecuente"],
            [["Problema", "82%", '<span class="lvl" style="background:var(--good-bg);color:var(--good-ink)">Hecho</span>', "Paga mucho en un portal y no le llegan consultas"],
             ["Impacto", "74%", '<span class="lvl" style="background:var(--warn-bg);color:var(--warn-ink)">Señal</span>', "3 a 10 propiedades sin rotar"],
             ["Causa raíz", "31%", '<span class="lvl" style="background:var(--crit-bg);color:var(--crit-ink)">Indicio</span>', "Avisos sin foto ni precio actualizado"],
             ["Evento disparador", "63%", '<span class="lvl" style="background:var(--warn-bg);color:var(--warn-ink)">Señal</span>', "Le subió el precio el portal actual"],
             ["Resultado de contacto", "88%", '<span class="lvl" style="background:var(--good-bg);color:var(--good-ink)">Hecho</span>', "Demo agendada con fecha"]], minw=620)
    + '<div class="adv mt">' + table(["Impacto × evento disparador", "Subió el portal", "Propiedad vacía +60 días", "Nueva captación", "Sin disparador"],
                                    [["Alto (más de 10 propiedades)", "<b>22</b>", 9, 6, 11], ["Medio (3 a 10)", 18, 14, 8, 19], ["Bajo (1 o 2)", 5, 21, 4, 38]], minw=620)
    + '<p class="qcm">Base: 175 con impacto cargado (74%). Celda prioritaria: 22 inmobiliarias grandes a las que el portal les subió el precio.</p></div>'
    + '<div class="adv mt"><div class="qg">'
    + "".join(f'<div class="qc" style="--q:var(--vio);--qb:var(--vio-soft)"><div class="qc-h"><span class="qc-ic">{ic("quote")}</span><span class="qc-th">{t}</span><span class="qc-n">{k}</span></div><blockquote>{ic("quote")}{q}</blockquote><div class="qc-m">{ic("user")}{w}</div></div>'
              for t, k, q, w in [("Problema declarado", "cita", "Pago el portal todos los meses y este mes me entraron dos consultas.", "Inmobiliaria · Córdoba · 14 propiedades"),
                                 ("Evento disparador", "cita", "Nos aumentaron 40% el plan y estamos viendo alternativas.", "Inmobiliaria · CABA · 22 propiedades"),
                                 ("Impacto", "cita", "Tengo tres departamentos vacíos desde agosto.", "Dueño directo · La Plata")])
    + '</div><p class="qcm">Citas de una persona cada una: explican un número, no son un patrón.</p></div>'
    + yeq("«Me subió el portal» es el disparador dominante: el mensaje de venta es precio. Impacto y causa raíz todavía no alcanzan para priorizar sin refuerzo del prompt.")
)

P["audiencias"] = (
    head_sec("Audiencias · listas para la pauta", "Cada lista con su tag de origen", "y su tamaño real.",
             "Quién entra como semilla, quién como exclusión.", "Similares en TikTok y Meta desde 1.000 coincidencias reales. La señal QualifiedLead (Conversions API y Events API de TikTok) vale solo si el tag de calificado está bien cargado.")
    + '<div class="g4">'
    + kpi("seed", "grn", "pro", "Semilla de similares", "236", bsc="de 1.000 coincidencias necesarias · 24%")
    + kpi("flame", "amb", "pro", "Hot leads para retargeting", "70", bsc="tag Hot lead")
    + kpi("x", "", "pro", "Excluidos de la pauta a anunciantes", "1.049", bsc="1.020 buscadores + 29 altas")
    + kpi("checkc", "blu", "calc", "Listas listas para usar", "3 de 5", bsc="2 esperan volumen o medición")
    + '</div>'
    + table(["Lista", "Tag de origen", "Tamaño", "Uso", "Estado"],
            [["Anunciantes calificados", "Calificado", 236, "Semilla de similares (TikTok y Meta)", '<span class="fx-st pend">Falta llegar a 1.000</span>'],
             ["Hot leads", "Hot lead", 70, "Retargeting Click to WhatsApp «demo hoy»", '<span class="fx-st ok">Lista</span>'],
             ["Altas actuales", "Suscripto", "29 + base", "Exclusión", '<span class="fx-st ok">Lista</span>'],
             ["Buscadores", "Buscador", "1.020", "Exclusión en pauta a anunciantes", '<span class="fx-st ok">Lista</span>'],
             ["Dueños directos", "perfil_anunciante = dueño", 260, "Similar para TT-01 y FB-01", '<span class="fx-st pend">Medir</span>']], minw=620)
    + yeq("Excluir a los 1.020 buscadores de la pauta a anunciantes es lo más barato que se puede hacer esta quincena.")
)

P["tokens"] = (
    head_sec("Consumo de Tokens · CRM", "Cada charla procesada cuesta ≈ USD 0,40.", "Más de la mitad la usan buscadores.",
             "Cuánto consume el agente, en qué se va y cuánto cobra Meta.", "Escenario [CÁLCULO]: sin panel de consumo todavía. Proyección USD 0,40 por conversación. Prometheo cobra la inteligencia; Meta cobra el canal: no se suman.")
    + '<div class="g4">'
    + kpi("dollar", "blu", "calc", "Consumo de IA · quincena", "USD 736", "+8%", bsc="1.840 charlas × USD 0,40 (proyección).")
    + kpi("checkc", "grn", "calc", "Costo de IA por resuelta", "USD 0,40", bsc="Sobre 1.214 resueltas sin humano.")
    + kpi("wa", "", "calc", "Meta · mensajes de marketing", "$161.208", bsc="1.800 plantillas × $89,56.")
    + kpi("bot", "pnk", "pro", "Suscripción Prometheo", "USD 149", bsc="Plan Enterprise por mes.")
    + '</div><div class="g2">'
    + bars("En qué se gasta la IA", "calc", [("Conversación con buscadores", 405, "USD 405", "55%"), ("Conversación con anunciantes", 184, "USD 184", "25%"), ("Extracción de variables", 88, "USD 88", "12%"), ("Smart Tags", 44, "USD 44", "6%"), ("Soporte", 15, "USD 15", "2%")],
           "El buscador no compra suscripción: va en una línea aparte, como la no-demanda en real estate.")
    + '<div class="qx"><div class="qw">' + ic("wa") + "Costo de Meta · quincena" + src("calc") + '</div><div class="kv"><div><div class="v">$0</div><div class="k">servicio · dentro de ventana y cupo</div></div><div><div class="v">$161.208</div><div class="k">marketing · 1.800 plantillas</div></div><div><div class="v">$0</div><div class="k">utilidad</div></div><div><div class="v">$161.208</div><div class="k">total</div></div></div><p class="qcm">Marketing ARS 89,56 por plantilla (rate card oficial, sin impuestos). El dato real sale de la factura de Meta.</p></div>'
    + "</div>"
    + '<div class="g2">'
    + '<div class="qx"><div class="qw">' + ic("alert") + "Cortes de saldo" + src("pro") + '</div><div class="empty-st" style="text-align:center;padding:18px 10px;color:var(--ink3);font-size:12.5px;border:1px dashed var(--line);border-radius:12px">' + ic("info", "width:20px;height:20px;color:var(--ink4)") + '<p style="margin:6px 0 0"><b style="color:var(--ink2)">Sin datos suficientes en este período.</b><br>Falta conectar el panel de consumo de Prometheo. Si el saldo llega a cero, el agente deja de responder: se declara en Integraciones.</p></div></div>'
    + bars("Puerta de entrada", "pro", [("Click to WhatsApp (IG-03)", 168, "168", "9%"), ("Mensaje directo en redes", 900, "900", "49%"), ("WhatsApp orgánico y difusión", 652, "652", "35%"), ("Gmail", 120, "120", "7%")],
           "Solo el 9% entra por Click to WhatsApp: la ventana gratis de 72 h cubre poco del servicio. El resto entra en el cupo de 1.000 mensajes por mes.", color="var(--blu)")
    + '</div>'
    + yeq("Más de la mitad del saldo de IA lo consumen buscadores que se resuelven con un link a la app. Un flujo corto para buscadores baja el costo sin tocar la venta.")
)

# --- canales ---
P["pauta"] = (
    head_sec("Pauta → Venta · cada pauta, por separado", "TikTok y Meta ven el clic.", "Prometheo ve qué pasó después.",
             "Cada pauta medida por lo que importa: cuántos anunciantes califican y cuántos se dan de alta.", "Cruce por ID de anuncio (Meta, Click to WhatsApp) y por código de pauta en el mensaje prellenado o UTM (TikTok, email, WhatsApp). El gasto es de cada plataforma; el conteo de charlas es de Prometheo. Nunca se suman.")
    + '<div class="bridge"><div class="eq"><b>TikTok y Meta ven hasta el clic</b> × <b>Prometheo ve del clic al alta</b></div><p>Cada peso de pauta se juzga por el anunciante calificado y el alta que trajo.</p></div>'
    + '<div class="srclegend"><div class="slg">' + src("tt") + src("meta") + '<span>Gasto, impresiones, clics, CTR, video y píxel.</span></div><div class="slg">' + src("pro") + '<span>Charlas reales, anunciantes, <b>calificación</b>, hot leads, demos y altas.</span></div><div class="slg">' + src("calc") + '<span>% que califica con su intervalo, costo por calificado, CAC y ROAS.</span></div></div>'
    + sub("Ficha por pauta · las nueve, de los tres canales pagos")
    + '<div class="adg">' + "".join(adx(a, COLOR[a["canal"]]) for a in ADS) + "</div>"
    + sub("Tabla completa · plataforma a la izquierda, Prometheo a la derecha")
    + ads_table(ADS, "Total pauta")
    + '<p class="qcm">IC 95% = intervalo de Wilson de la tasa de calificación: con pocos anunciantes, el rango se abre. <b>n&lt;30</b> = muestra chica, no comparar. ROAS 12m = altas × $45.000 × 12 ÷ gasto (modelado, sin bajas).</p>'
    + sub("Cómo sabe Prometheo de qué pauta vino cada charla")
    + '<div class="g2"><div class="qx"><div class="qw">' + ic("doc") + "Variables" + src("pro") + '</div><div class="pm-chips">'
    + "".join(f'<span class="qcs">{v}</span>' for v in ["canal_ingreso", "pauta_origen (ad_id o código)", "utm_source", "utm_campaign", "ctwa_clid (Meta)", "ttclid (TikTok, vía landing)", "tipo_contacto", "perfil_anunciante", "cant_propiedades", "portal_actual", "plan_interes", "zona", "operacion", "evento_disparador", "objecion_principal", "resultado_contacto", "resuelto_por", "fecha_alta"])
    + '</div></div><div class="qx"><div class="qw">' + ic("tag") + "Tags y Smart Tags" + src("pro") + '</div><div class="pm-chips">'
    + "".join(f'<span class="qcs">{t}</span>' for t in ["Origen · TikTok Ads", "Origen · Meta IG", "Origen · Meta FB", "Origen · Email", "Origen · WA Marketing", "Origen · Orgánico", "Anunciante", "Buscador", "Soporte app", "Calificado", "Hot lead", "Demo agendada", "Suscripto", "No fit", "Resuelto sin humano", "Derivado a humano"])
    + '</div><p class="qcm">TikTok no pasa el ID de anuncio a un mensaje directo: cada pauta lleva un código en el mensaje prellenado («Hola MIA, vengo de TT-04») o un link con UTM, y Prometheo lo guarda en pauta_origen.</p></div></div>'
    + yeq("TT-02 (MIA Map) es la pauta más barata por charla y la peor por alta: trae buscadores. IG-02, TT-01 y TT-04 venden. Mover presupuesto de TT-02 a TT-04 es la decisión de la quincena (Action Driven).")
)

TT = [a for a in ADS if a["canal"] == "TikTok"]
tg = sum(a["gasto"] for a in TT)


def ttrow(a, cells):
    return [f'<b>{a["id"]}</b> <span class="sub" style="display:inline">{a["nombre"]}</span>'] + cells


quart = "".join(
    f'<div class="qx"><div class="qw">{ic("eye")}{a["id"]} · cuartiles{src("tt")}</div>'
    + "".join(f'<div class="qi"><span class="qj">{lab}</span><span class="qk">{q}%</span><div class="qf"><div class="qh" style="width:{q}%;background:#EE1D52"></div></div></div>'
              for lab, q in zip(["25%", "50%", "75%", "100% (finalización)"], a["q"]))
    + "</div>" for a in TT)

P["tiktok"] = (
    '<div class="qo" style="margin-top:6px"><div class="hbrand" style="margin-bottom:8px"><span class="wm" style="font-size:30px">TikTok Ads</span><span class="ic" style="font-size:15px"><b>Canal</b>Marketing</span></div>'
    '<p class="qcq"><span class="bsc">Las métricas que entrega marketing, agrupadas como las lee TikTok, y al final qué pasó en Prometheo con cada pauta.</span>'
    '<span class="adv">TikTok manda en gasto, distribución, video y píxel. Prometheo manda en charlas, calificación y altas. El píxel cuenta registros en la web; Prometheo cuenta conversaciones: son dos preguntas distintas.</span></p></div>'
    + '<div class="g4">'
    + kpi("dollar", "grn", "tt", "Inversión de la quincena", ars(tg), "+12%", flat=True, bsc="4 pautas", qcp=f"CPM {ars(tg / sum(a['imp'] for a in TT) * 1000)}")
    + kpi("chat", "blu", "pro", "Charlas en Prometheo", str(sum(a["conv"] for a in TT)), "+18%", bsc="con código de pauta")
    + kpi("checkc", "", "pro", "Calificados", str(sum(a["calif"] for a in TT)), "+9%", bsc=f"{100 * sum(a['calif'] for a in TT) / sum(a['anun'] for a in TT):.0f}% de los anunciantes de TikTok")
    + kpi("lock", "pnk", "erp", "Altas", str(sum(a["susc"] for a in TT)), "+2", bsc="cruce del tag con el registro de altas")
    + "</div>"
    + sub("1 · Distribución y costo")
    + table(["Pauta", f'Impresiones {src("tt")}', "Alcance", "Frecuencia", "CPM", "CPC", "Gasto"],
            [ttrow(a, [n(a["imp"]), n(a["alc"]), n(a["imp"] / a["alc"], 2), ars(a["gasto"] / a["imp"] * 1000), ars(a["gasto"] / a["clics"]), ars(a["gasto"])]) for a in TT], minw=720)
    + sub("2 · Interacción")
    + table(["Pauta", f'Clics (destino) {src("tt")}', "CTR", "Interacciones de pago", "Tasa de interacción"],
            [ttrow(a, [n(a["clics"]), f'{100 * a["clics"] / a["imp"]:.2f}%'.replace(".", ","), n(a["inter"]), f'{100 * a["inter"] / a["imp"]:.2f}%'.replace(".", ",")]) for a in TT], minw=620)
    + sub("3 · Reproducción de video · el gancho y la retención")
    + table(["Pauta", f'Visualizaciones 3 s {src("tt")}', "Visualizaciones 6 s", "Tasa de finalización", "P25", "P50", "P75"],
            [ttrow(a, [f'{a["v3"]}% <span class="sub" style="display:inline">{n(a["imp"] * a["v3"] / 100)}</span>', f'{a["v6"]}%', f'<b>{a["q"][3]}%</b>', f'{a["q"][0]}%', f'{a["q"][1]}%', f'{a["q"][2]}%']) for a in TT], minw=720)
    + '<div class="adv mt"><div class="g4">' + quart + "</div></div>"
    + sub("4 · Conversión · píxel de TikTok al lado de Prometheo")
    + table(["Pauta", f'Conversiones píxel {src("tt")}', "CPA píxel", "CVR", f'Charlas {src("pro")}', "Calificados", "Altas", f'Costo por calificado {src("calc")}', "ROAS 12m"],
            [ttrow(a, [a["pixel"], ars(a["gasto"] / a["pixel"]), f'{100 * a["pixel"] / a["clics"]:.1f}%'.replace(".", ","), a["conv"], a["calif"], f'<b>{a["susc"]}</b>',
                       ars(a["gasto"] / a["calif"]), n(a["susc"] * PLAN * 12 / a["gasto"], 1) + "x"]) for a in TT], minw=900)
    + '<p class="qcm">El píxel dice que TT-02 es la mejor (CPA más bajo). Prometheo dice que no trajo ninguna alta. Las dos cosas son ciertas: convierte buscadores, no anunciantes.</p>'
    + yeq("TT-02 tiene el mejor gancho a 3 segundos y la peor venta: el video funciona, la audiencia no. TT-04 retiene menos pero vende: subir presupuesto y probar un gancho más fuerte en los primeros 3 segundos.")
)


def meta_panel(canal, title, lectura):
    rows = [a for a in ADS if a["canal"] == canal]
    g = sum(a["gasto"] for a in rows)
    return (
        f'<div class="qo" style="margin-top:6px"><div class="hbrand" style="margin-bottom:8px"><span class="wm" style="font-size:30px">{title}</span><span class="ic" style="font-size:15px"><b>Canal</b>Marketing</span></div>'
        '<p class="qcq"><span class="bsc">El cruce Meta × Prometheo de cada anuncio: qué pasó con cada clic dentro del CRM.</span>'
        '<span class="adv">Meta manda en inversión, alcance, impresiones y clics; Prometheo manda en cuántas charlas hubo y qué pasó con ellas. <b>CTR</b> = clics ÷ impresiones.</span></p></div>'
        + '<div class="g4">'
        + kpi("dollar", "grn", "meta", "Inversión de la quincena", ars(g), "+6%", flat=True, bsc=f"{len(rows)} anuncios")
        + kpi("chat", "blu", "pro", "Charlas", str(sum(a["conv"] for a in rows)), "+10%", bsc="Meta informa más conversaciones iniciadas: manda Prometheo.")
        + kpi("checkc", "", "pro", "Calificados", str(sum(a["calif"] for a in rows)), "+14%", bsc=f"{100 * sum(a['calif'] for a in rows) / sum(a['anun'] for a in rows):.0f}% de los anunciantes")
        + kpi("lock", "pnk", "erp", "Altas", str(sum(a["susc"] for a in rows)), "+1", bsc="cruce del tag con el registro de altas")
        + '</div><div class="adg">' + "".join(adx(a, COLOR[canal]) for a in rows) + "</div>"
        + '<div class="adv mt">' + ads_table(rows, "Total " + canal) + "</div>"
        + yeq(lectura))


P["instagram"] = meta_panel("Instagram", "Meta Ads · Instagram", "IG-03 (Click to WhatsApp) trae más anunciantes por peso e IG-02 es el que más califica. IG-01 (Amoblador IA) gusta pero trae buscadores: pasa a objetivo de descarga de app, fuera del embudo comercial.")
P["facebook"] = meta_panel("Facebook", "Meta Ads · Facebook", "FB-01 trae dueños directos con baja calificación (25%): muchos tienen una sola propiedad. Medir si el plan gratuito los convierte después antes de cortar. FB-02 tiene muestra chica.")

P["email"] = (
    '<div class="qo" style="margin-top:6px"><div class="hbrand" style="margin-bottom:8px"><span class="wm" style="font-size:30px">Email Marketing</span><span class="ic" style="font-size:15px"><b>Canal</b>Marketing</span></div>'
    '<p class="qcq"><span class="bsc">Titula el empalme: el clic que termina en una charla de Prometheo. La apertura no titula.</span><span class="adv">Envíos desde Gmail y la plataforma de envío masivo. El link lleva UTM y código de campaña para cruzarse con Prometheo.</span></p></div>'
    + '<div class="g4">'
    + kpi("route", "blu", "calc", "Tasa de empalme · reactivación", "21%", "+3 p.p.", bsc="61 charlas de 290 clics.")
    + kpi("checkc", "", "pro", "Calificados", "14", "+4", bsc="todos de la reactivación")
    + kpi("lock", "pnk", "erp", "Altas", "2", "+1", bsc="anunciantes vencidos que volvieron")
    + kpi("mail", "", "mail", "Bajas", "140", "+8%", up=False, bsc="0,9% de los entregados")
    + "</div>"
    + table(["Campaña", f'Enviados {src("mail")}', "Entregados", "Aperturas", "Clics", "Bajas", f'Empalme {src("pro")}', "Calificados", "Altas", f'CTOR {src("calc")}', "Tasa de empalme"],
            [["Reactivación anunciantes vencidos", "4.200", "4.080", "1.510 · 37%", "290 · 7,1%", 22, "<b>61</b>", 14, 2, "19%", "21%"],
             ["Newsletter buscadores · octubre", "12.000", "11.640", "3.260 · 28%", "640 · 5,5%", 118, "<b>35</b>", 0, 0, "20%", "5%"]], minw=980)
    + '<p class="qcm">Empalme: contacto que escribe a Prometheo dentro de las 72 h del clic (ventana propuesta, a validar). 18 empalmes llegaron sin código de campaña: faltante estructural, no se reparten. La apertura se infla por precarga de imágenes: no titula.</p>'
    + yeq("La reactivación de anunciantes vencidos empalma 21% de los clics y trajo 2 altas. El newsletter a buscadores no vende: es contenido y se mide con otra vara.")
)

P["wamkt"] = (
    '<div class="qo" style="margin-top:6px"><div class="hbrand" style="margin-bottom:8px"><span class="wm" style="font-size:30px">WhatsApp Marketing</span><span class="ic" style="font-size:15px"><b>Canal</b>Marketing</span></div>'
    '<p class="qcq"><span class="bsc">Titula la respuesta, no la lectura. El tier y la calidad del número también son métricas.</span><span class="adv">Difusiones desde Prometheo con API oficial. Doble lectura: sobre entregados y sobre leídos.</span></p></div>'
    + '<div class="g4">'
    + kpi("chat", "blu", "wpp", "Tasa de respuesta", "12,3%", "+2,4 p.p.", bsc="214 de 1.742 entregados.", adv="214 de 1.742 entregados · 16,6% sobre 1.290 leídos.")
    + kpi("checkc", "", "pro", "Calificados", "19", "+5", bsc="de las 214 respuestas")
    + kpi("layers", "grn", "wpp", "Tier de envío", "10.000", bsc="subió desde 1.000")
    + kpi("shield", "grn", "wpp", "Calidad del número", "Alta", bsc="bloqueos 0,6% (11)")
    + "</div>"
    + table(["Difusión", f'Enviados {src("wpp")}', "Entregados", "Leídos", "Respuestas", "Bloqueos", f'Calificados {src("pro")}', "Altas", f'Costo Meta {src("calc")}'],
            [["Plan Pro −30% inmobiliarias · plantilla marketing", "1.800", "1.742", "1.290 · 74%", "<b>214</b> · 12,3%", 11, 19, 3, "$161.208"]], minw=820)
    + yeq("12,3% de respuesta y 3 altas por $161 mil. Bloqueos en 0,6%: hay margen para una segunda difusión segmentada por zona.")
)

# --- Action Driven ---
# rub: puntos por componente (base, fuente, cobertura, profundidad, evidencia previa, cierre), niveles de score-data-driven.md
CARDS = [
    dict(v="decidir", owner="Marketing", rub=[14, 5, 7, 15, 5, 15], title="Presupuesto TikTok · TT-02 trae 188 charlas y 0 altas",
         mide="Gasto, charlas y altas por código de pauta", base="87 anunciantes de TikTok · 465 charlas", dato="TT-02: 3 calificados, 0 altas · TT-04: 29 y 4",
         corto="Pasar $150.000 de TT-02 a TT-04 durante una quincena.", cuando="Esta semana", meta="+2 a +4 altas",
         hacer="Pasar $150.000 de TT-02 a TT-04 durante una quincena. TT-02 sigue con objetivo de descarga de app, fuera del embudo comercial.", donde="TikTok Ads Manager · presupuesto por grupo de anuncios", efecto="+2 a +4 altas con el mismo gasto total de TikTok.",
         medimos="Altas de TT-04 ÷ gasto, al cierre de la quincena, con la misma base.", guardiana="% de calificados de TT-04 no baja de 40% al subir el presupuesto.", porque="Base 14: 87 anunciantes. Fuente 5: dato modelado. Cobertura 7: código de pauta al 71%. Profundidad 15: contrastado entre pautas. Evidencia 5: buena práctica. Cierre 15: misma métrica, fecha y guardiana."),
    dict(v="activar", owner="Ventas", rub=[14, 5, 11, 10, 5, 15], title="Hot leads · 9 de 70 sin seguimiento en 24 h",
         mide="Hot leads sin derivación ni seguimiento", base="70 hot leads de la quincena", dato="9 sin seguimiento (antes 12)",
         corto="Aviso inmediato al vendedor de turno y demo ofrecida el mismo día.", cuando="Esta semana", meta="0 hot sin seguimiento",
         hacer="Aviso al vendedor de turno cuando entra un hot lead; demo ofrecida el mismo día con dos horarios cerrados.", donde="Prometheo · acción del Smart Tag Hot lead (prompt listo abajo)", efecto="Cero hot sin seguimiento y +2 demos por quincena.",
         medimos="Hot leads sin seguimiento a las 24 h, cada semana.", guardiana="Tasa de demo a alta no cae (hoy 37%).", porque="Base 14: 70 hot leads. Fuente 5: modelado. Cobertura 11: tag al 88%. Profundidad 10: diagnóstico. Evidencia 5: estándar del rubro. Cierre 15."),
    dict(v="separar", owner="AUREA", rub=[20, 5, 15, 10, 5, 15], title="Flujo buscador · 55% del saldo de IA lo consume quien no compra",
         mide="Reparto del gasto de IA por tipo de contacto", base="1.840 charlas · USD 736 proyectados", dato="1.020 buscadores · USD 405",
         corto="Al buscador, link a la app y MIA Tools en dos mensajes, y cerrar.", cuando="Próxima quincena", meta="−25% a −35% costo IA buscador",
         hacer="Al detectar Buscador, responder con link a la app y MIA Tools en dos mensajes y cerrar con el tag Resuelto sin humano.", donde="Prometheo · prompt del agente, sector de ruteo", efecto="−25% a −35% del costo de IA por charla de buscador.",
         medimos="USD por charla de buscador procesada.", guardiana="% resueltas sin contacto humano no baja de 66%.", porque="Base 20: 1.840 charlas. Fuente 5: proyección. Cobertura 15: tipo de contacto al 96%. Profundidad 10. Evidencia 5. Cierre 15."),
    dict(v="corregir", owner="AUREA", rub=[20, 5, 7, 10, 5, 10], title="Cantidad de propiedades · 121 anunciantes no califican por falta del dato",
         mide="Motivo de no calificación", base="374 que no califican", dato="121 sin cant_propiedades",
         corto="Preguntar «¿cuántas propiedades manejás hoy?» en el primer bloque.", cuando="Próxima quincena", meta="Cobertura 80% o más",
         hacer="Sumar «¿cuántas propiedades manejás hoy?» en el primer bloque del agente para anunciantes, sin repreguntar si ya está.", donde="Prometheo · prompt + variable cant_propiedades (prompt listo abajo)", efecto="El rango de calificados se achica y el orden de llamada mejora.",
         medimos="Cobertura de cant_propiedades.", guardiana="Abandono en el primer bloque de preguntas.", porque="Base 20. Fuente 5. Cobertura 7: 58%. Profundidad 10. Evidencia 5. Cierre 10: sin fecha cerrada."),
    dict(v="medir", owner="Marketing", rub=[20, 5, 7, 5, 5, 10], title="Atribución TikTok · 71% de las charlas trae el código de pauta",
         mide="Cobertura de pauta_origen en TikTok", base="465 charlas de TikTok", dato="330 con código · 135 sin pauta",
         corto="Código en el mensaje prellenado y UTM en todas las pautas.", cuando="Próxima quincena", meta="Cobertura 90%",
         hacer="Mensaje prellenado con código en todas las pautas y link con UTM a una landing con píxel.", donde="TikTok Ads · URL y mensaje del anuncio", efecto="Cobertura de 90% o más: TikTok pasa de Señal a Hecho.",
         medimos="% de charlas de TikTok con pauta_origen.", guardiana="Charlas totales de TikTok no bajan por fricción del link.", porque="Base 20. Fuente 5. Cobertura 7. Profundidad 5: descriptivo. Evidencia 5. Cierre 10."),
    dict(v="decidir", owner="Dirección", rub=[20, 0, 0, 5, 5, 5], title="Definición de calificado · hoy es un rango de 181 a 236",
         mide="Criterio de calificación del anunciante", base="610 anunciantes", dato="181 estricto · 236 amplio",
         corto="Validar con MIA obligatorios y sumas en 30 minutos.", cuando="Antes del próximo corte", meta="Un solo número",
         hacer="Validar con MIA obligatorios, sumas y señales de hot lead en una reunión de 30 minutos.", donde="Doc 1 · bloque B3", efecto="El número de calificados deja de ser rango y puede titular.",
         medimos="Diferencia entre la definición propuesta y la validada.", guardiana="Que la cohorte no cambie entre pestañas.", porque="Es una decisión de definición, no un dato."),
]

PM = [
    ("pmA", "activar", "AUREA", "var(--warn)", "Alta", "Aviso al vendedor cuando entra un hot lead", "El tag Hot lead ya existe. Falta que el aviso llegue al vendedor de turno y que se ofrezca la demo el mismo día.", "70", "hot leads en la quincena", 54,
     "Necesito cambiar la acción del Smart Tag &quot;Hot lead&quot; del asistente de MIA.\n- Que envíe una notificación al vendedor de turno con nombre, canal de ingreso, cantidad de propiedades y plan de interés.\n- No cambies el prompt de asignación del tag.\nAntes de guardar, mostrame cómo queda la acción y a quién le llega. No apliques nada hasta que te confirme con &quot;Sí, confirmar&quot;."),
    ("pmB", "corregir", "AUREA", "var(--crit)", "Urgente", "Preguntar cuántas propiedades maneja el anunciante", "121 anunciantes no califican porque falta el dato. La pregunta va en el primer bloque, una sola vez.", "121", "sin cant_propiedades", 54,
     "Necesito sumar una pregunta al asistente de MIA cuando el contacto es Anunciante.\n- En el primer bloque: &quot;¿Cuántas propiedades manejás hoy?&quot;.\n- Guardar la respuesta en la variable &quot;cant_propiedades&quot; (número).\n- No preguntarlo si ya está cargado.\nAntes de guardar, mostrame el sector del prompt como queda. No apliques nada hasta que te confirme con &quot;Sí, confirmar&quot;."),
]


def pm(p):
    pid, v, owner, col, pri, title, why, cnt, cntl, score, prompt = p
    return (f'<details class="pm" id="{pid}" style="--pc:{col}"><summary><div class="pm-n">{pid[-1].replace("A", "1").replace("B", "2")}</div><div class="pm-main">'
            f'<div class="pm-k">Posible mejora · <span class="ac-v" data-v="{v}">{ic(VERB_IC[v])}{v.capitalize()}</span> · {owner}</div><div class="pm-t">{title}</div><div class="pm-why">{why}</div>'
            f'<div class="pm-chips"><span class="qcs" style="--c:{col}">{pri}</span><span class="qcs">Configuración · Prometheo</span>{sx(score)}</div></div>'
            f'<div class="pm-cnt"><b>{cnt}</b><span>{cntl}</span></div><div class="pm-more"><span class="op">Ver prompt para Mi Prometheo</span><span class="cl">Plegar</span>{ic("chev")}</div></summary>'
            f'<div class="pm-body"><div class="mp"><div class="mp-h"><span class="mp-av">{ic("bot")}</span><div><b>Mi Prometheo</b><span>Prompt listo para pegar · revisalo antes de enviar</span></div>'
            f'<button class="mp-copy" type="button" data-copy="pt-{pid}">{ic("doc")}<span>Copiar prompt</span></button></div><div class="mp-bubble" id="pt-{pid}">{prompt}</div></div></div></details>')


P["action"] = (
    head_sec("Action Driven · acciones con dueño", "Qué hacemos esta quincena,", "ordenado por impacto.",
             "Cada acción con un verbo, un dueño y su índice Data Driven: cuánto se apoya en datos.", "Rúbrica de score v1, sin calibrar. Con datos modelados ningún índice pasa de 54. En Básico se ven las tres de mayor impacto; en Avanzado, todas.")
    + '<div class="g4">'
    + kpi("bolt", "", "calc", "Acciones de la quincena", str(len(CARDS)), bsc="3 de alto impacto en Básico.")
    + kpi("user", "blu", "calc", "Dueños", "4", bsc="Marketing 2 · AUREA 2 · Ventas 1 · Dirección 1")
    + kpi("lock", "pnk", "calc", "Efecto esperado en altas", "+2 a +5", bsc="si se ejecutan las dos primeras")
    + kpi("gauge", "amb", "calc", "Índice Data Driven medio", f"{sum(score_of(c) for c in CARDS) / len(CARDS):.0f}%", bsc="techo 54 por dato modelado")
    + '</div>'
    + sub("Plan de la quincena · para el dueño de MIA")
    + '<div class="plan">' + table(["#", "Acción", "Dueño", "Para cuándo", "Meta", "Índice Data Driven"],
            [[f"<b>{i + 1}</b>", f'<span class="ac-v" data-v="{c["v"]}">{c["v"].capitalize()}</span> <b>{c["corto"]}</b>', c["owner"], c["cuando"], c["meta"], sx(score_of(c))] for i, c in enumerate(CARDS)], minw=820) + '</div>'
    + sub("Las acciones, una por una")
    + DD_LEGEND
    + '<div class="igrid avg ad-grid">' + "".join(action(c, i > 2) for i, c in enumerate(CARDS)) + "</div>"
    + '<p class="qcm bsc">Las tres de mayor impacto. En <b>Avanzado</b> se ven las 6.</p>'
    + f'<div class="subsec mejora mpx"><div class="ss-h"><div class="ss-ic mpx-ic">{ic("flame")}</div><div><div class="ss-k">Subsector · Posibles mejoras</div><h2>Del hallazgo al prompt, <em>listo para pedir.</em></h2>'
    f'<span class="mpx-pill">{ic("flame")}Potenciado por <b>Mi Prometheo</b></span></div></div><div class="pm-list">' + "".join(pm(p) for p in PM) + "</div></div>"
    + '<div class="adv mt">' + table(["Registro de calibración", "Índice al proponer", "Resultado al cierre", "Estado"],
                                    [[c["title"].split(" · ")[0], f"{score_of(c)}%", "se registra el 30/10", '<span class="fx-st pend">abierta</span>'] for c in CARDS], minw=620)
    + '<p class="qcm">Rúbrica de score versión 1, sin calibrar: se calibra con 20 cards cerradas.</p></div>'
    + yeq("Primero la plata: mover presupuesto de TT-02 a TT-04 y cortar el costo de IA de buscadores. Después, el seguimiento de hot leads, que es la venta más cercana.")
)

# --- fuentes ---
CAL = [("tipo_contacto", 96, "Panorama, Venta"), ("canal_ingreso", 100, "Panorama, Resueltas"), ("resuelto_por", 94, "Resueltas"), ("pauta_origen · Meta (ctwa_clid)", 92, "Pauta → Venta"),
       ("pauta_origen · TikTok (código)", 71, "TikTok"), ("utm_campaign · Gmail", 38, "Email"), ("cant_propiedades", 58, "Venta, Criterio"), ("portal_actual", 66, "Criterio"),
       ("plan_interes", 47, "Venta"), ("evento_disparador", 63, "Criterio"), ("causa_raiz", 31, "Criterio"), ("fecha_alta (cierre)", 0, "Venta · hoy fuera del CRM"), ("satisfacción post-resolución", 0, "Resueltas")]


def lvl(v):
    if v >= 80:
        return '<span class="lvl" style="background:var(--good-bg);color:var(--good-ink)">Hecho</span>'
    if v >= 40:
        return '<span class="lvl" style="background:var(--warn-bg);color:var(--warn-ink)">Señal</span>'
    if v >= 10:
        return '<span class="lvl" style="background:var(--crit-bg);color:var(--crit-ink)">Indicio</span>'
    return '<span class="lvl" style="background:var(--inset);color:var(--ink3)">No reportable</span>'


P["calidad"] = (
    head_sec("Calidad de datos · Data Driven", "Cada número con base, cobertura y origen.", "Lo que falta, se dibuja.",
             "Qué tan confiable es cada variable que usa el tablero.", "Escalera: Hecho 80% o más · Señal 40 a 79% · Indicio 10 a 39% · No reportable menos de 10%. Con cobertura menor a 80%, doble lectura.")
    + '<div class="g4">'
    + kpi("checkc", "grn", "calc", "Variables en Hecho", "4", bsc="80% o más de cobertura")
    + kpi("pulse", "blu", "calc", "Variables en Señal", "6", bsc="40 a 79%: se muestran con su base")
    + kpi("alert", "amb", "calc", "Variables en Indicio", "2", bsc="10 a 39%: no titulan")
    + kpi("x", "", "calc", "No reportables", "2", bsc="cierre y satisfacción: faltantes de proceso")
    + '</div>'
    + table(["Variable", "Cobertura", "", "Nivel", "Dónde se usa"],
            [[f"<b>{a}</b>", f"{v}%", f'<div class="qf" style="width:140px"><div class="qh" style="width:{v}%;background:var(--vio)"></div></div>', lvl(v), w] for a, v, w in CAL], minw=620)
    + yeq("La atribución de TikTok depende del código en el mensaje: 71% de cobertura. Hasta pasar 80%, las cifras por pauta de TikTok se leen como Señal.")
)


def cn(icon, color, name, on, chip, desc):
    st = '<span class="qco on"><i></i>Conectado</span>' if on else '<span class="qco off"><i></i>A conectar</span>'
    btn = f'<button class="qcc" type="button">{ic("sliders")}Configuración</button>' if on else f'<button class="qcc go" type="button">{ic("plug")}Conectar</button>'
    ch = f'<span class="qcl">{ic("cal")}{chip}</span>' if chip else ""
    return (f'<div class="cn"><div class="cn-h"><span class="qcn" style="--c:{color}">{ic(icon)}</span><div><b>{name}</b>{st}</div></div>'
            f'<div class="cn-d">{ch}<p>{desc}</p></div><div class="cn-f">{btn}</div></div>')


CH = "".join(f'<span class="qcl" style="margin:4px 4px 0 0">{ic(i)}{t}</span>' for i, t in [("wa", "WhatsApp · API"), ("mail", "Gmail"), ("ig", "Instagram DM"), ("fb", "Facebook Messenger"), ("play", "TikTok DM")])
P["integraciones"] = (
    head_sec("Integraciones · de dónde sale este tablero", "Todas las fuentes,", "en dos sectores.",
             "Qué alimenta el tablero, qué está conectado y cuándo se actualizó cada fuente.", "Cada fuente manda en lo suyo: Prometheo en charlas y calificación, cada canal en su gasto y alcance, el registro de altas en las suscripciones.")
    + '<div class="bridge"><div class="eq"><b>TikTok y Meta ven hasta el clic</b> × <b>Prometheo ve del clic al alta</b></div><p>El cruce por <b>ID de anuncio</b> (Meta) y por <b>código de pauta</b> (TikTok, email y WhatsApp) es el producto.</p></div>'
    + f'<div class="cn-sec"><div class="cn-sh"><span class="cn-si">{ic("crm")}</span><div><b>CRM</b><span>Un solo CRM: todos los canales de conversación entran por Prometheo</span></div></div>'
    + f'<div class="cn-g" style="grid-template-columns:1fr"><div class="cn"><div class="cn-h"><span class="qcn" style="--c:linear-gradient(135deg,#7C5CBF,#5B8FD9)">{ic("bot")}</span><div><b>Prometheo</b><span class="qco off"><i></i>Esperando export</span></div></div>'
    + f'<div class="cn-d"><p>Conversaciones, tags, variables, calificación, resolución sin humano y altas. Los cinco canales viven adentro de Prometheo, por eso no van como tarjetas aparte:</p><div style="margin-top:8px">{CH}</div></div>'
    + f'<div class="cn-f"><button class="qcc" type="button">{ic("sliders")}Configuración</button></div></div></div></div>'
    + f'<div class="cn-sec"><div class="cn-sh"><span class="cn-si">{ic("mega")}</span><div><b>Canales Marketing</b><span>Gasto, alcance y envíos de cada canal</span></div></div><div class="cn-g">'
    + cn("play", "#111", "TikTok Ads", False, "", "Gasto, distribución, video y píxel por anuncio y día.")
    + cn("meta", "#0866FF", "Meta Ads · Instagram y Facebook", False, "", "Inversión, impresiones, clics y conversaciones por anuncio.")
    + cn("mail", "#B4649B", "Email Marketing", False, "", "Envíos, entregas, aperturas, clics y bajas.")
    + cn("wa", "#1F9E7E", "WhatsApp Marketing", False, "", "Difusiones, plantillas, leídos, bloqueos, tier y calidad.")
    + "</div></div>"
    + f'<div class="cn-sec"><div class="cn-sh"><span class="cn-si">{ic("layers")}</span><div><b>Otras integraciones</b><span>Cierre y costos</span></div></div><div class="cn-g">'
    + cn("ledger", "#A0612A", "Registro de altas de MIA", False, "", "Planes pagos activados. Sin esto no hay ciclo cerrado.")
    + cn("pie", "#7C5CBF", "Panel de consumo de IA", False, "", "Consumo por mes, reparto y cortes de saldo.")
    + "</div></div>"
    + yeq("Faltantes declarados: export de Prometheo (todo el tablero es modelado), registro de altas, panel de consumo y precio real de los planes (se usó $45.000 por mes).")
)

# ---------- navegación ----------
NAV = [
    ("Resumen", None, [("panorama", "grid", "Panorama"), ("evolucion", "trend", "Evolución"), ("action", "bolt", "Action Driven")]),
    ("crm", "crm", [("ventacrm", "crm", "Venta · CRM"), ("resueltas", "checkc", "Resueltas sin contacto humano"), ("demanda", "box", "Demanda"), ("criterio", "compass", "Criterio comercial"),
                    ("audiencias", "users", "Audiencias"), ("tokens", "bolt", "Consumo de Tokens - CRM")]),
    ("marketing", "mega", [("pauta", "route", "Pauta → Venta"), ("tiktok", "play", "TikTok Ads", "#EE1D52"), ("instagram", "ig", "Meta Ads · Instagram", "var(--pnk)"),
                                   ("facebook", "fb", "Meta Ads · Facebook", "var(--src-meta)"), ("email", "mail", "Email Marketing", "var(--src-mail)"), ("wamkt", "wa", "WhatsApp Marketing", "var(--src-wpp)")]),
    ("De dónde sale esto", None, [("calidad", "shield", "Calidad de datos"), ("integraciones", "plug", "Integraciones")]),
]
ids = [t[0] for _, _, items in NAV for t in items]


def navlabel(t):
    dot = f'<span class="chch" style="background:{t[3]}"></span>' if len(t) > 3 else ""
    return f'<label class="nav" data-t="{t[0]}" for="dn-{t[0]}">{ic(t[1])}{t[2]}{dot}</label>'


side = [f'<aside class="side"><div class="brand"><div class="sph sph-bg"></div><div><b>MIA</b><span>Inteligencia Comercial</span></div></div>']
for name, icon, items in NAV:
    labels = "".join(navlabel(t) for t in items)
    if icon:
        side.append(f'<details class="ngrp" name="ngrp"{" open" if name == "crm" else ""}><summary><span class="ng-ic">{ic(icon)}</span><span class="ng-t">{name}</span>{ic("chev")}</summary><div class="ng-b">{labels}</div></details>')
    else:
        side.append(f'<div class="navlab">{name}</div>{labels}')
side.append(f'<div class="side-foot"><button class="themebtn" type="button" onclick="tgl()"><svg class="i sun"><use href="#i-sun"/></svg><svg class="i moon"><use href="#i-moon"/></svg><span>Tema claro / oscuro</span></button></div></aside>')

radios = "".join(f'<input type="radio" name="nav" id="dn-{i}" class="st"{" checked" if i == "panorama" else ""}>' for i in ids)
radios += '<input type="radio" name="mode" id="mode-simple" class="st" checked><input type="radio" name="mode" id="mode-adv" class="st">'

topbar = (f'<div class="topbar"><div class="tb-l"><img class="tb-logo" src="{logo}" alt="AUREA Hub"><div class="hbrand"><span class="wm">MIA</span><span class="ic"><b>Inteligencia</b>Comercial</span></div></div>'
          f'<div class="tb-r"><span class="period">{ic("cal")}1 al 15 oct 2026 <span>· vs 16 al 30 sep</span></span><span class="demo">{ic("info")}Demo · datos modelados</span>'
          f'<span class="dd-pill">{ic("gauge")}<b>Data Driven</b> · cada cifra con base, cobertura y origen</span>'
          f'<div class="mode"><label for="mode-simple">{ic("rows")}Básico</label><label for="mode-adv">{ic("sliders")}Avanzado</label></div></div></div>'
          f'<div class="updbar">{ic("refresh", "width:13px;height:13px")}Última actualización por fuente: '
          + "".join(f'<span class="u"><span class="dt" style="background:{c}"></span>{t} <b>{d}</b></span>' for c, t, d in [
              ("var(--src-pro)", "Prometheo", "modelado 15 oct"), ("#EE1D52", "TikTok Ads", "modelado 15 oct"), ("var(--src-meta)", "Meta Ads", "modelado 15 oct"),
              ("var(--src-mail)", "Email", "modelado 14 oct"), ("var(--src-wpp)", "WhatsApp", "modelado 13 oct"), ("var(--src-erp)", "Registro de altas", "sin conectar")])
          + "</div>"
          f'<div class="modehint bsc">{ic("rows")}<span><b>Modo básico:</b> lo esencial de cada pestaña, en palabras simples. Pasá a <b>Avanzado</b> para ver el detalle, los cruces y las definiciones.</span></div>'
          f'<div class="modehint adv">{ic("sliders")}<span><b>Modo avanzado:</b> todo lo del básico, más el detalle técnico: bases, coberturas, intervalos y cruces.</span></div>')

extra_css = "<style>" + "".join(
    f"#dn-{i}:checked~.shell .nav[data-t={i}]{{background:var(--grad);color:#fff;box-shadow:0 6px 16px -6px rgba(124,92,191,.6)}}"
    f"#dn-{i}:checked~.shell .nav[data-t={i}] svg.i{{color:#fff}}#dn-{i}:checked~.shell .p-{i}{{display:block}}" for i in ids) + """
:root{--src-tt:#EE1D52}.s-tt{background:var(--src-tt)}
.ngrp{margin-top:8px;border-top:1px solid var(--line2)}
.ngrp>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:8px;padding:12px 10px 6px}
.ngrp>summary::-webkit-details-marker{display:none}
.ng-ic{display:flex;align-items:center}.ng-ic svg.i{width:14px;height:14px;color:var(--vio)}
.ng-t{flex:1;font-size:12px;font-weight:700;letter-spacing:.04em;text-transform:lowercase;color:var(--ink2)}
.ngrp>summary>svg.i:last-child{width:14px;height:14px;color:var(--ink4);transition:transform .2s}.ngrp[open]>summary>svg.i:last-child{transform:rotate(180deg)}
.ng-b{padding:2px 6px 8px}
.dd-pill{display:inline-flex;align-items:center;gap:7px;font-size:11px;color:var(--ink2);padding:6px 12px 6px 9px;border-radius:999px;background:var(--surface);border:1px solid transparent;background-image:linear-gradient(var(--surface),var(--surface)),var(--grad);background-origin:border-box;background-clip:padding-box,border-box}
.dd-pill svg.i{width:14px;height:14px;color:var(--vio)}.dd-pill b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
tr.tot td{background:var(--surface2)}
.plan td:nth-child(2),.plan th:nth-child(2),.plan td:nth-child(3),.plan th:nth-child(3),.plan td:nth-child(4),.plan th:nth-child(4){text-align:left}.plan td:nth-child(2){white-space:normal}
.hero-h em{font-family:var(--serif);font-weight:400;font-style:italic}
.ad-grid{align-items:stretch}.ad-grid>.i3:not([open])>summary{height:100%;display:flex;flex-direction:column}
.ad-grid .qbl{min-height:2.7em}.ad-grid .qbh{flex:1}.ad-grid .qbd{margin-top:auto}
.ad-do{display:flex;gap:9px;align-items:flex-start;margin-top:12px;padding:11px 12px;border-radius:12px;background:var(--tb,var(--surface2));border:1px solid color-mix(in srgb,var(--tone,var(--vio)) 30%,transparent)}
.ad-do>svg.i{width:16px;height:16px;color:var(--tone,var(--vio));flex-shrink:0;margin-top:2px}.ad-do b{display:block;font-size:9.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--tone,var(--vio))}
.ad-do span{display:block;font-size:13.5px;font-weight:700;line-height:1.35;color:var(--ink);margin-top:2px;min-height:2.7em}
.ad-meta{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;margin:8px 0 10px}.ad-meta span{display:flex;align-items:center;gap:5px;font-size:11px;color:var(--ink3);background:var(--surface2);border:1px solid var(--line2);border-radius:9px;padding:6px 8px;min-width:0}
.ad-meta svg.i{width:12px;height:12px;flex-shrink:0;color:var(--ink3)}.ad-meta b{color:var(--ink);font-weight:700}
.i3.av[data-v=corregir]{--tb:var(--sv-corregir-bg)}.i3.av[data-v=proteger]{--tb:var(--sv-proteger-bg)}.i3.av[data-v=separar]{--tb:var(--sv-separar-bg)}.i3.av[data-v=medir]{--tb:var(--sv-medir-bg)}.i3.av[data-v=decidir]{--tb:var(--sv-decidir-bg)}.i3.av[data-v=activar]{--tb:var(--sv-activar-bg)}
@media (max-width:900px){.ad-meta{grid-template-columns:1fr}}.qbr.dn{color:var(--crit)}
</style>"""
# ícono TikTok (nota musical) que no trae el set de referencia
tt_icon = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><symbol id="i-play" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5M14 3c.5 2.6 2.4 4.5 5 5"/></symbol></defs></svg>'

panels = "".join(f'<section class="panel p-{i}">{P[i]}</section>' for i in ids)
html = head + extra_css + tt_icon + radios + '<div class="shell">' + "".join(side) + '<main class="main">' + topbar + panels + "</main></div>" + scripts
OUT.write_text(html, encoding="utf-8")
print(OUT, len(html.encode()))
