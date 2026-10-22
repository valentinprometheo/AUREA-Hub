"""Genera tableros/MIA_Tablero_IC.html con la estética del tablero de referencia de EDFAN.

Uso: python3 tableros/build_mia.py <ruta al HTML de referencia de EDFAN>
Toma del HTML de referencia el CSS, los íconos SVG, el logo y los scripts; el contenido es de MIA.
El modelo de datos sigue el diseño de CRM de MIA (variables tipo_usuario, canal, intencion_principal,
estado_embudo y sistema_operativo; Smart Tags de soporte por área, comerciales y de experiencia).
Todos los números son modelados (no hay export de Prometheo).
"""
import re
import sys
from pathlib import Path

REF = Path(sys.argv[1])
OUT = Path(__file__).with_name("MIA_Tablero_IC.html")
ref = REF.read_text(encoding="utf-8")

head = ref[: ref.index('<input type="radio" name="nav"')]
head = head.replace("<title>EDFAN IC Demo</title>", "<title>MIA App · Inteligencia Comercial</title>")
head = head.replace("family=Arimo:", "family=Manrope:wght@500;600;700;800&family=Arimo:")
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


def pc(a, b, d=0):
    return n(100 * a / b, d) + "%" if b else "–"


SRC = {
    "pro": ("qt", "chat", "Prometheo"),
    "meta": ("s-meta", "meta", "Meta Ads"),
    "tt": ("s-tt", "play", "TikTok Ads"),
    "mail": ("s-mail", "mail", "Email"),
    "wpp": ("s-wpp", "wa", "WhatsApp"),
    "calc": ("qbw", "sigma", "Cálculo"),
    "erp": ("s-erp", "ledger", "Registro de altas"),
    "app": ("s-app", "phone", "Datos de la app"),
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


def g4(*cards):
    return '<div class="g4">' + "".join(cards) + "</div>"


def head_sec(kick, title, em, bsc, adv):
    return (f'<div class="qo"><div class="qr"><span class="qv"></span>{kick}</div>'
            f'<h1 class="sec">{title} <em>{em}</em></h1>'
            f'<p class="qcq"><span class="bsc">{bsc}</span><span class="adv">{adv}</span></p></div>')


def chan_head(icon, name, kind, bsc, adv):
    return (f'<div class="qo" style="margin-top:6px"><div class="chh"><span class="chh-ic">{ic(icon)}</span><div><span class="chh-k">{kind}</span>'
            f'<span class="chh-t">{name}</span></div></div><p class="qcq"><span class="bsc">{bsc}</span><span class="adv">{adv}</span></p></div>')


def sub(t, note=""):
    nt = f'<span class="qr-n">{note}</span>' if note else ""
    return f'<div class="qo"><div class="qr"><span class="qv"></span>{t}{nt}</div></div>'


def yeq(t):
    return f'<div class="yeq">{ic("arrow")}<div><b>Y entonces qué</b><span>{t}</span></div></div>'


def srclegend(*items):
    return '<div class="srclegend">' + "".join(f'<div class="slg">{"".join(src(k) for k in ks)}<span>{t}</span></div>' for ks, t in items) + "</div>"


GRAD_BAR = {"var(--vio)": "var(--grad)", "var(--blu)": "linear-gradient(90deg,#5B8FD9,#7C5CBF)", "var(--pnk)": "linear-gradient(90deg,#C77AA8,#7C5CBF)",
            "var(--good)": "linear-gradient(90deg,#7C5CBF,#5B8FD9)", "var(--warn)": "linear-gradient(90deg,#C77AA8,#B5751F)"}


def bars(title, s, rows, note="", right="", color="var(--vio)", icon="pie", cls="qx"):
    color = GRAD_BAR.get(color, color)
    m = max(r[1] for r in rows)
    out = "".join(
        f'<div class="qi"><span class="qj">{r[0]}</span><span class="qk">{r[2] if len(r) > 2 and r[2] else n(r[1])}'
        f'{"<span>" + r[3] + "</span>" if len(r) > 3 else ""}</span>'
        f'<div class="qf"><div class="qh" style="width:{100 * r[1] / m:.1f}%;background:{color}"></div></div></div>'
        for r in rows)
    nt = f'<p class="qcm">{note}</p>' if note else ""
    rr = f'<span class="r">{right}</span>' if right else ""
    return f'<div class="{cls}"><div class="qw">{ic(icon)}{title}{src(s)}{rr}</div>{out}{nt}</div>'


def stat(icon, title, s, value, unit, text, kv=None, adv_kv=None, tone="var(--vio)"):
    """Card de subsector: título, cifra protagonista y casilleros."""
    k = ""
    if kv:
        k = f'<div class="kv" style="--kc:{len(kv)}">' + "".join(f'<div><div class="v">{v}</div><div class="k">{t}</div></div>' for v, t in kv) + "</div>"
    if adv_kv:
        k += f'<div class="adv"><div class="kv" style="--kc:{len(adv_kv)}">' + "".join(f'<div><div class="v">{v}</div><div class="k">{t}</div></div>' for v, t in adv_kv) + "</div></div>"
    u = f' <small class="u">{unit}</small>' if unit else ""
    return (f'<div class="qx qcg" style="--ct:{tone}"><div class="qw">{ic(icon)}{title}{src(s)}</div>'
            f'<div class="qy" style="font-size:26px">{value}{u}</div><div class="qz">{text}</div>{k}</div>')


def table(head_cells, rows, tot=None, minw=640):
    th = "".join(f"<th>{h}</th>" for h in head_cells)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    if tot:
        tr += '<tr class="tot">' + "".join(f"<td><b>{c}</b></td>" for c in tot) + "</tr>"
    return (f'<div class="qcf" style="overflow:hidden"><div class="tblwrap"><table style="min-width:{minw}px">'
            f"<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div></div>")


def steps(title, right, items, note="", icon="filter"):
    out = []
    base = items[0][1]
    for i, it in enumerate(items):
        lab, val, txt = it[0], it[1], it[2]
        cls = it[3] if len(it) > 3 else ""
        p = "" if not i else pc(val, items[i - 1][1], 1 if val / items[i - 1][1] < .1 else 0)
        w = max(2, 100 * val / base)
        out.append(f'<div class="fs {cls}"><div class="t"><span>{i + 1:02d}</span><span class="p">{p}</span></div><div class="l">{lab}</div>'
                   f'<div class="v"><b>{n(val)}</b> {txt}</div><div class="qbq"><i style="width:{w:.0f}%"></i></div>'
                   f'<div class="qbf"><span>{"base" if not i else "pasa " + p}</span></div></div>')
    nt = f'<div class="qcm">{note}</div>' if note else ""
    return (f'<div class="qcf pad"><div class="qw">{ic(icon)}{title}<span class="r">{right}</span></div>'
            f'<div class="fsteps" style="--n:{len(items)}">{"".join(out)}</div>{nt}</div>')


def band(score):
    return "alta" if score >= 80 else "media" if score >= 55 else "hipotesis" if score >= 30 else "criterio"


BAND_TXT = {"alta": "basada en datos", "media": "informada por datos", "hipotesis": "hipótesis", "criterio": "criterio"}


def sx(score, label=False):
    b = band(score)
    on = 4 if score >= 80 else 3 if score >= 55 else 2 if score >= 30 else 1
    segs = "".join(f'<i class="{"on" if k < on else ""}"></i>' for k in range(4))
    em = f"<em>{BAND_TXT[b]}</em>" if label else ""
    return (f'<span class="sx" data-b="{b}" title="Índice Data Driven {score}%: {BAND_TXT[b]}. Rúbrica v1, sin calibrar.">{ic("gauge")}'
            f'<b>{score}<small>%</small></b><span class="qs">{segs}</span>{em}</span>')


DD_LEGEND = (f'<div class="sxl">{ic("gauge")}<b>Índice Data Driven</b><span>cuánto de cada acción se apoya en datos:</span>'
             '<span class="qbe" data-b="alta"><i></i>80+ basada en datos</span><span class="qbe" data-b="media"><i></i>55–79 informada</span>'
             '<span class="qbe" data-b="hipotesis"><i></i>30–54 hipótesis</span><span class="qbe" data-b="criterio"><i></i>menos de 30 criterio</span></div>')

VERB_IC = {"activar": "bolt", "proteger": "shield", "corregir": "wrench", "separar": "layers", "medir": "pulse", "decidir": "compass"}
OWNER = {"Ventas": "o-ven", "Marketing": "o-mkt", "AUREA": "o-aurea", "Dirección": "o-cob"}
LEVEL = {"Hecho": ("var(--good-bg)", "var(--good-ink)"), "Señal": ("var(--warn-bg)", "var(--warn-ink)"),
         "Indicio": ("var(--crit-bg)", "var(--crit-ink)"), "No reportable": ("var(--inset)", "var(--ink3)")}


def lvl_of(v):
    return "Hecho" if v >= 80 else "Señal" if v >= 40 else "Indicio" if v >= 10 else "No reportable"


def lvl(v):
    t = lvl_of(v) if not isinstance(v, str) else v
    bg, fg = LEVEL[t]
    return f'<span class="lvl" style="background:{bg};color:{fg}">{t}</span>'


# ---------- datos modelados (quincena 1 al 15 oct 2026 vs 16 al 30 sep) ----------
CONV, CONV_ANT = 1840, 1706
RES, RES_ANT = 1214, 1003
CANAL = [("WhatsApp", "wa", 820), ("Instagram", "ig", 430), ("TikTok", "play", 260), ("Facebook", "fb", 210), ("Gmail", "mail", 120)]
TIPO = [("Particular", "user", 1214), ("Inmobiliaria", "building", 318), ("Inversor", "dollar", 122), ("Desarrolladora", "layers", 46), ("Sin identificar", "info", 140)]
INTENCION = [("Buscar", 612), ("Alquilar", 344), ("Publicar", 286), ("Vender", 168), ("Informarse", 160), ("Invertir", 122), ("Sin identificar", 90), ("Emprendimiento", 58)]
EMBUDO = [("No descargó la app", 520), ("Descargó, sin registro", 298), ("Registrado", 412), ("Publicó un aviso", 236), ("Usuario activo", 254)]
AREAS = [("Acceso y cuenta", "lock", 248, 186, ["#LOGIN_REGISTRO 132", "#VERIFICACION 74", "#RESET_PASSWORD 42"]),
         ("Publicaciones", "home", 196, 201, ["#UPLOAD_FOTOS 88", "#PUBLICACIONES 64", "#EDICION_PUBLICACION 44"]),
         ("Búsqueda", "eye", 104, 110, ["#FILTROS 58", "#BUSQUEDA 31", "#IMAGENES_NO_CARGAN 15"]),
         ("Rendimiento", "bolt", 88, 70, ["#CRASH 41", "#PERFORMANCE 29", "#PANTALLA_BLANCA 18"]),
         ("Permisos y dispositivo", "phone", 52, 55, ["#PERMISOS_UBICACION 38", "#PERMISOS 14"]),
         ("Administrativos", "doc", 38, 35, ["#FACTURA 24", "#DATOS_FISCALES 14"]),
         ("Otros técnicos", "alert", 36, 40, ["#ESCALAMIENTO_TECNICO 22", "#ERROR_DESCONOCIDO 14"])]
SOPORTE = sum(a[2] for a in AREAS)
COMERCIAL = [("Quiere un asesor", "#QUIERE_ASESOR", 96), ("Solicita demo", "#SOLICITA_DEMO", 78), ("Modelo de negocio", "#CONSULTA_MODELO_NEGOCIO", 52),
             ("Carga masiva de avisos", "#CARGA_MASIVA", 34), ("Publicidad en la app", "#CONSULTA_PUBLICIDAD", 28), ("Alianza", "#PARTNERSHIP", 9)]
EXPERIENCIA = [("Feedback positivo", "#FEEDBACK_POSITIVO", 92), ("Sugerencia", "#SUGERENCIA", 64), ("Queja", "#QUEJA", 46), ("Reclamo público", "#RECLAMO_PUBLICO", 12)]
B2B = 364
CAL_AMP, CAL_EST, CAL_ANT = 176, 134, 158
HOT, HOT_SIN = 58, 9
DEMO_AG, DEMO_RE, ALTAS, ALTAS_ANT = 67, 52, 27, 22

ADS = [
    dict(id="TT-01", camp="Descargas · Personas", conj="Propietarios 30 a 60", canal="TikTok", fmt="Video", nombre="Publicá gratis tu propiedad", publico="Particulares que venden", gasto=380000, imp=410000, alc=236000, clics=5330, inter=9120, conv=142, b2b=18, calif=7, hot=2, demos=3, altas=1, reg=64, v3=38, v6=24, q=(61, 40, 27, 18), pixel=210, lectura="Sostener: trae registros de particulares"),
    dict(id="TT-02", camp="Descargas · Personas", conj="Broad 18 a 45 · AMBA y Córdoba", canal="TikTok", fmt="Video", nombre="Mapa de precios por barrio", publico="Personas que buscan", gasto=300000, imp=520000, alc=301000, clics=7800, inter=18400, conv=188, b2b=6, calif=2, hot=0, demos=0, altas=0, reg=92, v3=46, v6=31, q=(70, 52, 38, 29), pixel=340, lectura="Mover: el mejor gancho, pero no trae inmobiliarias"),
    dict(id="TT-03", camp="Descargas · Personas", conj="Broad 18 a 45 · AMBA y Córdoba", canal="TikTok", fmt="Video", nombre="Simulador de crédito UVA", publico="Inversores y compradores", gasto=220000, imp=290000, alc=182000, clics=3480, inter=6200, conv=74, b2b=4, calif=1, hot=0, demos=1, altas=0, reg=31, v3=35, v6=22, q=(58, 37, 24, 16), pixel=150, lectura="Medir: muestra chica"),
    dict(id="TT-04", camp="Inmobiliarias · Planes", conj="Intereses · real estate", canal="TikTok", fmt="Video", nombre="Inmobiliarias: subí tu cartera", publico="Inmobiliarias", gasto=260000, imp=180000, alc=120000, clics=1980, inter=2650, conv=61, b2b=46, calif=28, hot=11, demos=13, altas=5, reg=4, v3=29, v6=17, q=(49, 30, 18, 11), pixel=66, lectura="Escalar: la que más vende en TikTok"),
    dict(id="IG-01", camp="Descargas · App", conj="Intereses · decoración y hogar", canal="Instagram", fmt="Reel", nombre="Amoblá tu propiedad con IA", publico="Personas que buscan", gasto=280000, imp=340000, alc=190000, clics=4080, inter=11300, conv=121, b2b=14, calif=6, hot=2, demos=2, altas=1, reg=48, ubic="Reels", lectura="Separar: objetivo descarga de app"),
    dict(id="IG-02", camp="Inmobiliarias · Demo", conj="Lookalike · altas actuales", canal="Instagram", fmt="Carrusel", nombre="Plan para inmobiliarias", publico="Inmobiliarias", gasto=310000, imp=210000, alc=128000, clics=2310, inter=3100, conv=96, b2b=64, calif=37, hot=14, demos=14, altas=6, reg=3, ubic="Feed", lectura="Sostener: la que más califica de Meta"),
    dict(id="IG-03", camp="Inmobiliarias · Demo", conj="Retargeting · visitó el perfil", canal="Instagram", fmt="Historia · Click to WhatsApp", nombre="Pedí tu demo por WhatsApp", publico="Inmobiliarias y desarrolladoras", gasto=350000, imp=230000, alc=141000, clics=2760, inter=2900, conv=168, b2b=70, calif=32, hot=13, demos=12, altas=4, reg=12, ubic="Historias", lectura="Sostener: más cuentas comerciales por peso"),
    dict(id="FB-01", camp="Particulares · Vender", conj="Propietarios 35 a 65", canal="Facebook", fmt="Imagen", nombre="Vendé sin intermediarios", publico="Particulares que venden", gasto=240000, imp=260000, alc=150000, clics=2860, inter=4100, conv=109, b2b=12, calif=4, hot=1, demos=1, altas=0, reg=41, ubic="Feed", lectura="Ajustar: trae particulares, no altas"),
    dict(id="FB-02", camp="Inmobiliarias · Bolsa de pedidos", conj="Administradores de páginas inmobiliarias", canal="Facebook", fmt="Carrusel", nombre="Bolsa de pedidos para inmobiliarias", publico="Inmobiliarias", gasto=160000, imp=150000, alc=96000, clics=1350, inter=1700, conv=47, b2b=29, calif=13, hot=4, demos=5, altas=2, reg=2, ubic="Feed", lectura="Sostener y medir: muestra chica"),
    dict(id="FB-03", camp="Campos", conj="Productores rurales", canal="Facebook", fmt="Video", nombre="Campos: comprá y vendé", publico="Productores e inversores", gasto=150000, imp=170000, alc=104000, clics=1190, inter=1500, conv=38, b2b=9, calif=4, hot=2, demos=2, altas=0, reg=11, ubic="Marketplace", lectura="Medir: nicho chico, buena calidad"),
]
GADS = [
    dict(id="GG-01", canal="Google", fmt="Búsqueda · exacta", camp="Marca MIA", conj="Marca · exacta", kw="«mia app inmobiliaria», «mercado inmobiliario argentino»", nombre="Marca MIA", publico="Quien ya conoce MIA", gasto=60000, imp=3100, alc=3100, clics=540, inter=0, conv=72, b2b=6, calif=4, hot=1, demos=2, altas=1, reg=38, lectura="Proteger: la búsqueda de marca es la más barata"),
    dict(id="GG-02", canal="Google", fmt="Búsqueda · frase", camp="Inmobiliarias · Publicar", conj="Publicar propiedades · frase", kw="«portal para inmobiliarias», «publicar propiedades inmobiliaria»", nombre="Publicá tu cartera en MIA", publico="Inmobiliarias", gasto=140000, imp=6800, clics=420, alc=6800, inter=0, conv=64, b2b=14, calif=9, hot=4, demos=3, altas=2, reg=6, lectura="Subir: intención alta de inmobiliarias"),
    dict(id="GG-03", canal="Google", fmt="Búsqueda · frase", camp="Inmobiliarias · Publicar", conj="Competencia · frase", kw="«alternativa a zonaprop», «zonaprop precio planes»", nombre="La alternativa a los portales caros", publico="Inmobiliarias", gasto=110000, imp=5200, clics=380, alc=5200, inter=0, conv=51, b2b=10, calif=7, hot=3, demos=2, altas=1, reg=4, lectura="Sostener: el precio del portal es el disparador"),
    dict(id="GG-04", canal="Google", fmt="Búsqueda · amplia", camp="Descargas · Alquiler", conj="Alquilar · amplia", kw="«alquiler departamento córdoba», «alquilar 2 ambientes»", nombre="Encontrá tu alquiler en MIA", publico="Personas que buscan", gasto=90000, imp=12400, clics=860, alc=12400, inter=0, conv=96, b2b=1, calif=0, hot=0, demos=0, altas=0, reg=61, lectura="Separar: trae descargas, no inmobiliarias"),
]
CH = {"Google": ("google", "var(--vio)", "var(--blu-soft)"), "TikTok": ("play", "var(--vio)", "var(--vio-soft)"), "Instagram": ("ig", "var(--pnk)", "var(--pnk-soft)"), "Facebook": ("fb", "var(--blu)", "var(--blu-soft)")}


def tot(rows, k):
    return sum(a[k] for a in rows)


def wilson(k, m):
    if not m:
        return 0, 0
    z = 1.96
    p = k / m
    d = 1 + z * z / m
    c = p + z * z / (2 * m)
    r = z * ((p * (1 - p) / m + z * z / (4 * m * m)) ** .5)
    return (c - r) / d, (c + r) / d


def adcard(a):
    icon, col, soft = CH[a["canal"]]
    ok = a["calif"] / a["b2b"] if a["b2b"] else 0
    s1 = "good" if ok >= .4 else "warn" if ok >= .25 else "crit"
    s2 = "good" if a["altas"] >= 4 else "warn" if a["altas"] >= 1 else "crit"
    mx = a["conv"]
    fun = "".join(f'<div class="qcb"><span>{k}</span><i style="width:{max(2, 100 * v / mx):.0f}%"></i><b>{v}</b></div>'
                  for k, v in [("Cuentas comerciales", a["b2b"]), ("Calificadas", a["calif"]), ("Demos", a["demos"]), ("Altas", a["altas"])])
    vc = {"good": "var(--good);--vb:var(--good-bg)", "warn": "var(--warn);--vb:var(--warn-bg)", "crit": "var(--crit);--vb:var(--crit-bg)"}[s2]
    cpc = ars(a["gasto"] / a["calif"]) if a["calif"] else "–"
    return (f'<div class="adx" style="--ax:{col};--axb:{soft}"><div class="adx-h"><span class="adx-ic">{ic(icon)}</span>'
            f'<div style="min-width:0"><span class="ad-k">{a["canal"]} · {a["fmt"]} <code>{a["id"]}</code></span><b>{a["nombre"]}</b><span>{ic("target")}{a["publico"]}</span></div></div>'
            f'<div class="adx-tiles"><div class="qch t1"><span>{ic("chat")}Charlas</span><b>{a["conv"]}</b></div>'
            f'<div class="qch t2"><span>{ic("checkc")}Califica<i class="st-dot" data-s="{s1}"></i></span><b>{pc(a["calif"], a["b2b"])}</b></div>'
            f'<div class="qch t3"><span>{ic("lock")}Altas<i class="st-dot" data-s="{s2}"></i></span><b>{a["altas"]}</b></div></div>'
            f'<div class="adx-fun">{fun}</div>'
            f'<div class="ad-meta2"><span>Gasto<b>{ars(a["gasto"])}</b></span><span>Por calificada<b>{cpc}</b></span><span>Registros en la app<b>{a["reg"]}</b></span></div>'
            f'<div class="adx-v ad-v" data-s="{s2}">{ic("bulb")}<span><b>{a["lectura"].split(":")[0]}</b>{":" + a["lectura"].split(":", 1)[1] if ":" in a["lectura"] else ""}.</span></div></div>')


def ads_table(rows):
    body = []
    for a in rows:
        lo, hi = wilson(a["calif"], a["b2b"])
        small = ' <span class="lvl" style="background:var(--warn-bg);color:var(--warn-ink)">n&lt;30</span>' if a["b2b"] < 30 else ""
        body.append([f'<b>{a["nombre"]}</b><span class="sub">{a["canal"]} · {a["fmt"]} · {a["id"]}</span>', ars(a["gasto"]), n(a["imp"]), n(a["clics"]),
                     pc(a["clics"], a["imp"], 2), a["conv"], f'{a["b2b"]}{small}', a["calif"],
                     f'{pc(a["calif"], a["b2b"])} <span class="sub" style="display:inline">({100 * lo:.0f}–{100 * hi:.0f})</span>',
                     a["demos"], f'<b>{a["altas"]}</b>', a["reg"], ars(a["gasto"] / a["calif"]) if a["calif"] else "–",
                     ars(a["gasto"] / a["altas"]) if a["altas"] else "–"])
    t = {k: tot(rows, k) for k in ["gasto", "imp", "clics", "conv", "b2b", "calif", "demos", "altas", "reg"]}
    totr = ["Total", ars(t["gasto"]), n(t["imp"]), n(t["clics"]), pc(t["clics"], t["imp"], 2), t["conv"], t["b2b"], t["calif"], pc(t["calif"], t["b2b"]),
            t["demos"], t["altas"], t["reg"], ars(t["gasto"] / t["calif"]), ars(t["gasto"] / t["altas"]) if t["altas"] else "–"]
    hd = ["Anuncio", "Gasto", "Impresiones", "Clics", "CTR", f'Charlas {src("pro")}', "Cuentas comerciales", "Calificadas",
          "% califica (IC 95%)", "Demos", "Altas", f'Registros {src("app")}', f'Costo por calificada {src("calc")}', "Costo por alta"]
    return table(hd, body, totr, minw=1240)


# ---------- paneles ----------
P = {}
TT = [a for a in ADS if a["canal"] == "TikTok"]
IG = [a for a in ADS if a["canal"] == "Instagram"]
FB = [a for a in ADS if a["canal"] == "Facebook"]
GASTO = tot(ADS, "gasto")
CAL_PAGA = tot(ADS, "calif")

# --- Panorama
P["panorama"] = (
    '<div class="iobar"><span class="demo-tag">' + ic("info") + 'Dato ilustrativo</span><span class="iohint">Demo de Inteligencia Comercial para MIA App · cifras modeladas con el diseño de CRM de MIA en Prometheo</span></div>'
    '<div class="hero-grid"><div class="hero"><div class="hero-sph sph-bg"></div><div class="hero-top"><span class="hero-kick">Panorama · 1 al 15 de octubre 2026</span><span class="hero-per">comparado con la quincena anterior</span></div>'
    '<div class="hero-h">1.840 conversaciones en quince días, <em>dos de cada tres resueltas sin intervención humana.</em></div>'
    f'<div class="hero-sub"><span class="bsc"><b>+8%</b> contra la quincena anterior, por los cinco canales. El agente resolvió <b>1.214 charlas</b> solo, detectó <b>{CAL_EST} a {CAL_AMP} oportunidades</b> con inmobiliarias y desarrolladoras y salieron <b>{ALTAS} altas</b> de suscripción.</span>'
    f'<span class="adv">1.840 conversaciones (+7,9%) · {B2B} cuentas comerciales · {CAL_EST}–{CAL_AMP} calificadas (criterio a validar) · {DEMO_AG} demos pedidas · {ALTAS} altas · 41% de las charlas trae un problema técnico.</span></div>'
    '<div class="chart-scale"><span>Conversaciones por día · mín 98 · máx 142</span><span>más es mejor ↑</span></div>'
    '<div class="hchart"><svg viewBox="0 0 600 150" preserveAspectRatio="none" role="img"><defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'
    '<path d="M 6 88 L 90 80 L 174 72 L 258 66 L 342 70 L 426 52 L 510 44 L 594 30 L 594 150 L 6 150 Z" fill="url(#hg)"/><path d="M 6 88 L 90 80 L 174 72 L 258 66 L 342 70 L 426 52 L 510 44 L 594 30" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"/><circle cx="594" cy="30" r="4.5" fill="#fff"/></svg>'
    '<div class="endtag" style="top:calc(20% - 4px)">142<span>15 oct</span></div></div><div class="chart-x"><span>1 oct</span><span>5 oct</span><span>10 oct</span><span>15 oct</span></div>'
    '<div class="hero-stats"><div class="hs"><div class="l">Charlas por día</div><div class="v">123</div><div class="m">1.840 en la quincena</div></div>'
    '<div class="hs"><div class="l">Resueltas sin contacto humano</div><div class="v">66%</div><div class="m">1.214 de 1.840</div></div>'
    '<div class="hs"><div class="l">Problema técnico más frecuente</div><div class="v">Acceso</div><div class="m">248 charlas · +33%</div></div></div></div>'
    f'<div class="hero-pink"><div class="hp-top"><div class="hp-row"><div class="hp-ic">{ic("lock")}</div><span class="hp-chip">Altas de suscripción</span></div>'
    '<svg class="hp-spk" viewBox="0 0 300 60" preserveAspectRatio="none" role="img"><polyline points="4,50 62,44 120,40 178,30 236,22 296,8" fill="none" stroke="rgba(255,255,255,.85)" stroke-width="2" vector-effect="non-scaling-stroke" stroke-linejoin="round"/></svg>'
    f'<div><div class="hp-l">Altas por quincena · mín 12 · máx {ALTAS}</div><div class="hp-v">{ALTAS}</div><div class="hp-d"><span class="pin">+{ALTAS - ALTAS_ANT} vs quincena anterior</span> inmobiliarias y desarrolladoras con plan pago</div></div></div>'
    f'<div class="hp-foot"><div class="mini"><b>{DEMO_AG}</b><span>Demos pedidas</span></div><div class="hp-sp"></div><div class="mini"><b>{HOT}</b><span>Hot leads</span></div><div class="hp-sp"></div><div class="mini"><b>{pc(ALTAS, DEMO_RE)}</b><span>De demo a alta</span></div></div></div></div>'
    + g4(kpi("chat", "blu", "pro", "Conversaciones", n(CONV), "+7,9%", bsc="Personas que escribieron por cualquiera de los 5 canales.", qcp="<b>Conversación</b>: contacto nuevo o reactivado en Prometheo, por fecha de ingreso."),
         kpi("checkc", "grn", "pro", "Resueltas sin contacto humano", n(RES), "+21%", bsc="66% de las charlas, sin que nadie del equipo escriba.", qcp="Smart Tag <b>Resuelto sin humano</b>."),
         kpi("target", "", "calc", "Oportunidades calificadas", f"{CAL_EST}–{CAL_AMP}", "+11%", bsc=f"de {B2B} inmobiliarias y desarrolladoras · criterio a validar con MIA", qcp="Rango: lectura estricta (3 de 4 sumas) y amplia (2 de 4)."),
         kpi("lock", "pnk", "erp", "Altas de suscripción", str(ALTAS), f"+{ALTAS - ALTAS_ANT}", bsc=f"{pc(ALTAS, DEMO_RE)} de las demos realizadas.", qcp="<b>Alta</b>: plan pago activado."))
    + '<div class="adv mt">' + g4(kpi("wrench", "amb", "pro", "Charlas con problema técnico", n(SOPORTE), "+10%", up=False, bsc="41% de las conversaciones · Smart Tags de soporte"),
                                  kpi("phone", "blu", "app", "Registros después de la charla", "412", "+14%", bsc="cruce con los datos de la app"),
                                  kpi("flame", "amb", "pro", "Hot leads", str(HOT), "+9%", bsc=f"{HOT_SIN} sin seguimiento en 24 h"),
                                  kpi("dollar", "", "calc", "Costo por calificada · pauta", ars(GASTO / CAL_PAGA), "−6%", bsc=f"{ars(GASTO)} ÷ {CAL_PAGA} calificadas atribuidas · menos es mejor")) + "</div>"
    + sub("Quién escribe y para qué", "variables canal, tipo_usuario e intencion_principal")
    + '<div class="g3">'
    + bars("Por canal de entrada", "pro", [(c, v) for c, _, v in CANAL], "Los cinco canales entran por Prometheo: un solo conteo.", icon="inb")
    + bars("Tipo de usuario", "pro", [(c, v) for c, _, v in TIPO], "Solo inmobiliarias y desarrolladoras pueden pagar un plan.", color="var(--blu)", icon="users")
    + bars("Qué quiere hacer", "pro", INTENCION[:6], "Buscar y alquilar son 52% de las charlas.", color="var(--pnk)", icon="target")
    + "</div>"
    + sub("Recorrido comercial · de la charla al alta")
    + steps("De la charla al alta", f"base: {n(CONV)} conversaciones",
            [("Conversaciones", CONV, "todos los canales"), ("Cuentas comerciales", B2B, "inmobiliarias y desarrolladoras"),
             ("Calificadas", CAL_AMP, "lectura amplia"), ("Pidieron demo", DEMO_AG, "#SOLICITA_DEMO"), ("Demo realizada", DEMO_RE, "marcada por Ventas", "leak"), ("Alta", ALTAS, "plan pago")],
            "El paso más flojo es de demo pedida a demo realizada: 15 inmobiliarias pidieron demo y no la tuvieron.", icon="route")
    + yeq("El agente resuelve solo 2 de cada 3 charlas y la pauta dirigida a inmobiliarias es la que vende. La alerta de la quincena está en el producto: los problemas de acceso a la cuenta subieron 33%.")
)

# --- Evolución
WEEKS = ["S1 sep", "S2 sep", "S3 sep", "S4 sep", "S1 oct", "S2 oct"]


def barchart(vals, color, fmt=lambda v: n(v), maxv=None):
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


pct = lambda v: f"{v:.0f}%"
EV_CONV = [770, 810, 838, 868, 896, 944]
EV_CAL = [68, 74, 76, 82, 84, 92]
EV_ALTA = [5, 7, 10, 12, 12, 15]
EV_PCT = [42, 43, 44, 45, 47, 49]
EV_RES = [55, 57, 58, 60, 64, 68]
EV_TEC = [38, 37, 39, 40, 40, 42]
P["evolucion"] = (
    head_sec("Evolución · semana a semana", "Conversaciones, oportunidades y altas", "por tramo semanal.",
             "Cómo vienen las conversaciones, cuántas cuentas comerciales califican y cuántas terminan en alta.",
             "Cada quincena se divide en dos tramos semanales. 1 al 15 sep: 1.580 conversaciones, 142 calificadas, 12 altas. 16 al 30 sep: 1.706, 158 y 22. 1 al 15 oct: 1.840, 176 y 27. En color pleno, la quincena actual.")
    + g4(kpi("chat", "blu", "pro", "Conversaciones · quincena", "1.840", "+7,9%", bsc="1.706 · 1.580 las dos anteriores"),
         kpi("checkc", "", "calc", "Calificadas · lectura amplia", str(CAL_AMP), "+11%", bsc="158 · 142 las dos anteriores"),
         kpi("lock", "pnk", "erp", "Altas", str(ALTAS), "+23%", bsc="22 · 12 las dos anteriores"),
         kpi("wrench", "amb", "pro", "Charlas con problema técnico", "41%", "+2 p.p.", up=False, bsc="subió tres semanas seguidas · menos es mejor"))
    + '<div class="g2">'
    + evo_card("chat", "Conversaciones por semana", "pro", f"mín {n(min(EV_CONV))} · máx {n(max(EV_CONV))}", EV_CONV, "var(--blu)", "Conversaciones · los 5 canales")
    + evo_card("checkc", "Calificadas por semana", "calc", f"mín {min(EV_CAL)} · máx {max(EV_CAL)}", EV_CAL, "var(--good)", "Oportunidades calificadas · lectura amplia")
    + '</div><div class="g2">'
    + evo_card("lock", "Altas por semana", "erp", "total por quincena 12 · 22 · 27", EV_ALTA, "var(--pnk)", "Altas de suscripción")
    + evo_card("pulse", "% de calificación por semana", "calc", f"de {EV_PCT[0]}% a {EV_PCT[-1]}%", EV_PCT, "var(--vio)", "Calificadas ÷ cuentas comerciales", pct, 60)
    + '</div><div class="adv"><div class="g2">'
    + evo_card("bot", "% resueltas sin contacto humano", "pro", f"de {EV_RES[0]}% a {EV_RES[-1]}%", EV_RES, "var(--good)", "Resueltas ÷ conversaciones", pct, 100)
    + evo_card("wrench", "% de charlas con problema técnico", "pro", f"de {EV_TEC[0]}% a {EV_TEC[-1]}% · menos es mejor", EV_TEC, "var(--warn)", "Charlas con Smart Tag de soporte ÷ conversaciones", pct, 60)
    + "</div></div>"
    + yeq("Las conversaciones y las oportunidades crecen todas las semanas. La serie a vigilar es la técnica: subió 4 puntos en tres semanas, empujada por el acceso a la cuenta.")
)

# --- Venta · CRM (subsectores en cards separadas)
P["ventacrm"] = (
    head_sec("Venta · CRM · inmobiliarias y desarrolladoras", "Quién puede pagar un plan,", "a quién llamar primero y qué mejorar.",
             "El agente detecta las cuentas comerciales, las califica y deriva la demo a Ventas.",
             f"Base: {B2B} cuentas comerciales (tipo_usuario = inmobiliaria o desarrolladora). Los particulares usan MIA gratis y se miden en Usuarios y embudo.")
    + g4(kpi("building", "blu", "pro", "Cuentas comerciales", str(B2B), "+9%", bsc="318 inmobiliarias · 46 desarrolladoras"),
         kpi("checkc", "", "calc", "Calificadas", f"{CAL_EST}–{CAL_AMP}", "+11%", bsc=f"{pc(CAL_EST, B2B)} a {pc(CAL_AMP, B2B)} de las cuentas · a validar"),
         kpi("flame", "amb", "pro", "Hot leads", str(HOT), "+9%", bsc=f"{HOT_SIN} sin seguimiento en 24 h"),
         kpi("lock", "pnk", "erp", "Altas", str(ALTAS), f"+{ALTAS - ALTAS_ANT}", bsc=f"{pc(ALTAS, DEMO_RE)} de las {DEMO_RE} demos realizadas"))
    + sub("Criterio de calificación", "propuesta a validar con MIA · Doc 1, bloque B3")
    + '<div class="g3">'
    + '<div class="qx crit-c"><div class="cc-h"><span class="cc-n">1</span><div><span class="cc-k">Obligatorios</span><b>Los dos</b></div></div>'
    + "".join(f'<div class="cc-r"><span>{t}</span><b>{v}</b></div>' for t, v in [("Es inmobiliaria o desarrolladora", B2B), ("Opera en una zona que MIA cubre", 331)])
    + '<p class="qcm">Si falta uno, no califica.</p></div>'
    + '<div class="qx crit-c"><div class="cc-h"><span class="cc-n">2</span><div><span class="cc-k">Suman</span><b>Al menos 2 de 4</b></div></div>'
    + "".join(f'<div class="cc-r"><span>{t}</span><b>{v}</b></div>' for t, v in [("Tiene propiedades para publicar", 214), ("Hoy paga otro portal", 241), ("Pregunta por un plan", 172), ("Habla quien decide", 186)])
    + f'<p class="qcm">Estricto, 3 de 4: {CAL_EST}. Amplio, 2 de 4: {CAL_AMP}.</p></div>'
    + '<div class="qx crit-c"><div class="cc-h"><span class="cc-n">3</span><div><span class="cc-k">Hot lead</span><b>Una señal alcanza</b></div></div>'
    + "".join(f'<div class="cc-r"><span>{t}</span><b>{v}</b></div>' for t, v in [("Pide una demo", 78), ("Carga masiva de avisos", 34), ("Más de 10 propiedades", 41)])
    + '<p class="qcm">Es prioridad, no etapa: aviso al vendedor en el momento.</p></div>'
    + "</div>"
    + sub("Recorrido de la cuenta comercial")
    + steps("De la cuenta comercial al alta", f"base: {B2B} cuentas",
            [("Cuentas comerciales", B2B, "detectadas por el agente"), ("Calificadas", CAL_AMP, "lectura amplia"), ("Pidieron demo", DEMO_AG, "#SOLICITA_DEMO"),
             ("Demo realizada", DEMO_RE, "marcada por Ventas", "leak"), ("Alta", ALTAS, "plan pago")], icon="route")
    + sub("Qué piden y por qué no califican")
    + '<div class="g2">'
    + bars("Oportunidades comerciales", "pro", [(t, v, "", tag) for t, tag, v in COMERCIAL], "Smart Tags del grupo Comercial / Oportunidades.", color="var(--good)", icon="bulb")
    + bars(f"Por qué no califican · {B2B - CAL_AMP}", "calc", [("No dijo cuántas propiedades maneja", 64), ("Menos de 2 condiciones que suman", 51), ("Zona sin cobertura de MIA", 33), ("Solo quiere publicar gratis", 28), ("No es quien decide", 12)],
           "El primero es un dato que falta, no falta de interés: se arregla en el prompt.", color="var(--warn)", icon="filter")
    + "</div>"
    + '<div class="adv mt">' + table(["Etapa (Smart Tag)", "Declarada por el tag", "Cumple la definición", "Diferencia"],
                                    [["Calificada", 194, CAL_AMP, "−18"], ["Demo agendada", 71, DEMO_AG, "−4"], ["Alta", ALTAS, ALTAS, "0"]], minw=520)
    + '<p class="qcm">Se muestran las dos columnas mientras no converjan.</p></div>'
    + yeq(f"Entre {CAL_EST} y {CAL_AMP} cuentas califican. Lo que más frena es un dato que el agente no pregunta: cuántas propiedades maneja la inmobiliaria. La venta se pierde después de pedir la demo: 15 no la tuvieron.")
)

# --- Usuarios y embudo
P["usuarios"] = (
    head_sec("Usuarios y embudo · estado_embudo", "En qué etapa está cada persona", "cuando le escribe a MIA.",
             "Muestra si el problema es de marketing (no descargan) o de producto (descargan y no se registran).",
             "Variable estado_embudo, cargada por el agente en cada conversación. La conversión posterior (si se registró o publicó después de la charla) sale de los datos de la app.")
    + g4(kpi("phone", "", "pro", "No descargaron la app", "520", "+12%", flat=True, bsc="28% de las charlas · problema de llegada"),
         kpi("x", "amb", "pro", "Descargaron y no se registraron", "298", "+19%", up=False, bsc="16% · fricción en el registro"),
         kpi("home", "blu", "pro", "Publicaron un aviso", "236", "+6%", bsc="13% · ya son oferta en MIA"),
         kpi("users", "grn", "pro", "Usuarios activos", "254", "+4%", bsc="14% · escriben por soporte o mejoras"))
    + sub("La etapa al escribir")
    + '<div class="g2">'
    + bars("Estado en el embudo", "pro", EMBUDO, "Base: 1.720 con etapa identificada (93%) · Hecho.", color="var(--vio)", icon="route")
    + bars("Qué quiere hacer, según la etapa", "pro", [("No descargó · quiere buscar o alquilar", 388), ("Descargó · quiere publicar", 164), ("Registrado · quiere vender", 112), ("Publicó · consulta por planes", 96), ("Activo · soporte técnico", 171)],
           "Cruce de estado_embudo con intencion_principal.", color="var(--blu)", icon="target")
    + "</div>"
    + sub("Qué pasó después de la charla", "cruce con los datos de la app")
    + '<div class="g3">'
    + stat("phone", "Descargaron la app", "app", "212", "de 520", "Personas que no tenían la app y la descargaron en los 7 días siguientes a la charla.", [("41%", "conversión"), ("WhatsApp", "canal que más convierte")])
    + stat("user", "Se registraron", "app", "412", "", "Registros nuevos después de una charla: descargas nuevas más los que ya tenían la app.", [("138", "de los 298 trabados"), ("46%", "destrabados")], tone="var(--blu)")
    + stat("home", "Publicaron su primer aviso", "app", "94", "", "Particulares e inmobiliarias que publicaron dentro de los 7 días.", [("61", "particulares"), ("33", "inmobiliarias")], tone="var(--pnk)")
    + "</div>"
    + '<div class="adv mt">' + table(["Tipo de usuario", "Conversaciones", "No descargó", "Sin registro", "Registrado", "Publicó", "Activo"],
                                    [["Particular", "1.214", 402, 236, 288, 128, 160], ["Inmobiliaria", 318, 52, 31, 72, 88, 75], ["Inversor", 122, 48, 20, 34, 6, 14], ["Desarrolladora", 46, 6, 4, 10, 14, 5]], minw=720)
    + '<p class="qcm">Sin identificar: 140 (8%). Las filas no suman 1.840 por esa diferencia.</p></div>'
    + yeq("298 personas descargaron la app y se trabaron antes de registrarse: es el mismo problema que muestra Soporte técnico en Acceso y cuenta. Arreglar el registro suma usuarios sin gastar más en pauta.")
)

# --- Soporte técnico
area_cards = "".join(
    f'<div class="qx area"><div class="ar-h"><span class="ar-ic">{ic(icn)}</span><b>{t}</b><span class="ar-d {"bad" if (v - a) / a > .1 else "ok" if v <= a else "neu"}">{"+" if v >= a else "−"}{abs(round(100 * (v - a) / a))}%</span></div>'
    f'<div class="ar-v">{v}<small> charlas</small></div><div class="ar-b"><i style="width:{100 * v / AREAS[0][2]:.0f}%"></i></div>'
    f'<div class="ar-t">{"".join(f"<span>{x}</span>" for x in tags)}</div></div>'
    for t, icn, v, a, tags in AREAS[:6])
P["soporte"] = (
    head_sec("Soporte técnico · fricción por área de la app", "Dónde se traba la gente", "dentro de MIA.",
             "Cada problema técnico se clasifica por área: acceso, publicaciones, búsqueda, rendimiento, permisos y administrativos.",
             "Smart Tags técnicos agrupados en 7 áreas. Son acumulativos: una charla puede tener login y verificación a la vez; acá se cuenta el área principal.")
    + g4(kpi("wrench", "amb", "pro", "Charlas con problema técnico", n(SOPORTE), "+10%", up=False, bsc=f"{pc(SOPORTE, CONV)} de las conversaciones"),
         kpi("lock", "pnk", "pro", "Área que más creció", "Acceso", "+33%", up=False, bsc="248 charlas · 186 la quincena anterior"),
         kpi("checkc", "grn", "pro", "Resueltas por el agente", "594", "+18%", bsc="78% de los problemas técnicos"),
         kpi("doc", "blu", "pro", "Escalados con los 4 datos", "61%", "+9 p.p.", bsc="102 de 168 · listos para el técnico"))
    + sub("Fricción por área", "comparado con la quincena anterior")
    + f'<div class="areas">{area_cards}</div>'
    + sub("Diagnóstico")
    + '<div class="g3">'
    + bars("Top 5 problemas", "pro", [("#LOGIN_REGISTRO", 132), ("#UPLOAD_FOTOS", 88), ("#VERIFICACION", 74), ("#PUBLICACIONES", 64), ("#FILTROS", 58)], "El login explica la suba de Acceso.", color="var(--warn)", icon="alert")
    + bars("Sistema operativo", "pro", [("Android", 402, "", "53%"), ("iPhone", 268, "", "35%"), ("Sin dato", 92, "", "12%")], "#CRASH: 31 de 41 en Android.", color="var(--blu)", icon="phone")
    + f'<div class="qx"><div class="qw">{ic("doc")}Escalamiento al técnico{src("pro")}</div>'
    + "".join(f'<div class="cc-r"><span>{t}</span><b>{v}</b></div>' for t, v in [("¿Android o iPhone?", "152 de 168"), ("Texto del error o pantalla", "131 de 168"), ("En qué paso se traba", "124 de 168"), ("Captura de pantalla", "109 de 168")])
    + '<p class="qcm">Los 4 datos completos: 102 (61%). Nunca se piden contraseñas ni códigos.</p></div>'
    + "</div>"
    + sub("Experiencia y marca", "Smart Tag #EXPERIENCIA y variable sentimiento")
    + '<div class="g3">'
    + stat("checkc", "Sentimiento positivo", "pro", "43%", "", "92 de 214 charlas con opinión sobre la app.", [("70", "neutras"), ("52", "negativas")], tone="var(--good)")
    + bars("Qué dicen", "pro", [(t, v, "", tag) for t, tag, v in EXPERIENCIA], color="var(--pnk)", icon="quote")
    + f'<div class="qx"><div class="qw">{ic("quote")}En sus palabras{src("pro")}</div><blockquote class="qte">Me encantó la calculadora de alquiler, la uso todos los meses.</blockquote><blockquote class="qte">No me llega el código para verificar la cuenta.</blockquote><p class="qcm">Citas de una persona cada una: explican un número, no son un patrón.</p></div>'
    + "</div>"
    + yeq("Acceso y cuenta subió 33% y casi todo es login y verificación. Es un problema de producto, no de atención: el agente lo resuelve, pero la gente no debería llegar a escribir.")
)

# --- Resueltas (subsectores separados)
P["resueltas"] = (
    head_sec("Resueltas sin contacto humano", "1.214 conversaciones,", "cerradas por el agente sin que nadie del equipo escriba.",
             "Cuántas charlas resolvió el agente solo, en qué y por qué canal.",
             "Smart Tag Resuelto sin humano. Una charla resuelta cierra con la respuesta dada, sin derivación ni intervención del equipo.")
    + g4(kpi("checkc", "grn", "pro", "Resueltas sin contacto humano", n(RES), "+21%", bsc="66% de las conversaciones"),
         kpi("pulse", "", "calc", "% resueltas", "66%", "+7 p.p.", bsc="quincena anterior 59%"),
         kpi("users", "blu", "pro", "Derivadas al equipo", "418", "+3%", flat=True, bsc="23% · soporte avanzado y ventas"),
         kpi("clock", "pnk", "calc", "Horas de equipo ahorradas", "≈ 101 h", "+18 h", bsc="5 min por charla, supuesto a validar"))
    + sub("Qué resolvió el agente solo")
    + '<div class="g4">'
    + stat("eye", "Búsqueda y uso de la app", "pro", "322", "charlas", "Cómo buscar, filtrar, guardar favoritos y usar el mapa.", [("27%", "de las resueltas")])
    + stat("wrench", "Problemas técnicos", "pro", "594", "charlas", "Login, fotos, verificación y permisos resueltos con pasos.", [("49%", "de las resueltas")], tone="var(--warn)")
    + stat("sliders", "MIA Tools", "pro", "212", "charlas", "Calculadoras, comparador UVA, contratos y amoblado con IA.", [("17%", "de las resueltas")], tone="var(--pnk)")
    + stat("dollar", "Planes y precios", "pro", "86", "charlas", "Inmobiliarias que preguntaron por planes y no pidieron demo.", [("7%", "de las resueltas")], tone="var(--blu)")
    + "</div>"
    + sub("Por canal y qué pasó al equipo")
    + '<div class="g2">'
    + bars("Resueltas por canal", "pro", [("WhatsApp", 520, "520", "63% de 820"), ("Instagram", 301, "301", "70% de 430"), ("TikTok", 196, "196", "75% de 260"), ("Facebook", 127, "127", "60% de 210"), ("Gmail", 70, "70", "58% de 120")], color="var(--good)", icon="inb")
    + bars("Derivadas al equipo · 418", "pro", [("Demo o asesor (Ventas)", 196), ("Soporte técnico avanzado", 168), ("Reclamo o baja", 54)], "Que una inmobiliaria llegue a Ventas está bien: es la venta.", color="var(--blu)", icon="users")
    + "</div>"
    + '<div class="adv mt">' + g4(kpi("bolt", "", "pro", "Primera respuesta del agente", "< 1 min", bsc="mediana de la quincena"),
                                  kpi("x", "amb", "pro", "Sin respuesta del contacto", "208", "−4%", bsc="11% · no volvieron a escribir"),
                                  kpi("repeat", "", "pro", "Reabiertas en 48 h", "41", bsc="3% de las resueltas · guardiana"),
                                  kpi("quote", "blu", "pro", "Resueltas con queja", "9", bsc="#QUEJA dentro de una resuelta")) + "</div>"
    + yeq("El agente resuelve muy bien el uso de la app y los problemas técnicos simples. Lo que pasa al equipo es casi todo venta o soporte avanzado: está bien que llegue a una persona.")
)

# --- Demanda
ZONAS = [("CABA", 248, ["Palermo 64", "Belgrano 41", "Caballito 38"]), ("Córdoba Capital", 214, ["Nueva Córdoba 72", "Güemes 39", "Cerro de las Rosas 28"]),
         ("GBA Norte", 143, ["Vicente López 44", "Tigre 37", "San Isidro 31"]), ("Rosario", 97, ["Centro 41", "Fisherton 19"]),
         ("La Plata", 66, ["Casco urbano 48"]), ("GBA Oeste", 58, ["Morón 22", "Ituzaingó 14"]), ("Mendoza", 41, ["Ciudad 26"]), ("Costa Atlántica", 37, ["Mar del Plata 24 · temporario"])]
ZT = sum(z[1] for z in ZONAS)
zone_rows = "".join(
    f'<div class="zr"><span class="zn">{i + 1}</span><div class="zm"><div class="zt"><b>{z}</b><span>{v} · {pc(v, ZT)}</span></div>'
    f'<div class="zb"><i style="width:{100 * v / ZONAS[0][1]:.0f}%"></i></div><div class="zs">{" · ".join(s)}</div></div></div>'
    for i, (z, v, s) in enumerate(ZONAS))
P["demanda"] = (
    head_sec("Demanda · qué buscan las personas", "Dónde y qué buscan,", "para mostrárselo a las inmobiliarias.",
             "Compradores, inquilinos e inversores: zona, operación, tipo de propiedad, ambientes y presupuesto.",
             f"Base: 1.078 personas que buscan (intencion_principal = buscar, alquilar o invertir). Zona declarada: {ZT} (84%) · Hecho. Zona, tipo de propiedad, ambientes y presupuesto son variables propuestas para sumar al CRM.")
    + g4(kpi("users", "blu", "pro", "Personas que buscan", "1.078", "+6%", bsc="59% de las conversaciones"),
         kpi("pin", "pnk", "pro", "Zona más pedida", "CABA", bsc="248 consultas · Palermo a la cabeza"),
         kpi("home", "", "pro", "Lo más buscado", "Depto 2 amb.", bsc="286 consultas · 42% de los que dicen ambientes"),
         kpi("box", "amb", "pro", "Pedidos sin oferta", "167", "+11%", up=False, bsc="consultas sin avisos suficientes en MIA"))
    + sub("Zonas más pedidas", f"base: {ZT} con zona declarada")
    + f'<div class="zg"><div class="qcf pad zcard"><div class="qw">{ic("pin")}Ranking de zonas{src("pro")}<span class="r">barrios más pedidos debajo de cada zona</span></div>{zone_rows}</div>'
    + '<div class="zside">'
    + stat("trend", "Zona que más crece", "pro", "Córdoba Capital", "", "214 consultas, +28% contra la quincena anterior. Nueva Córdoba explica un tercio.", [("+28%", "vs quincena anterior"), ("4,0", "consultas por aviso")], tone="var(--pnk)")
    + stat("alert", "Más consultas por aviso", "pro", "Nueva Córdoba", "", "Alquiler de 1 y 2 ambientes: 72 consultas para 18 avisos activos.", [("72", "consultas"), ("18", "avisos en MIA")], tone="var(--warn)")
    + "</div></div>"
    + sub("Qué buscan")
    + '<div class="g4">'
    + bars("Operación", "pro", [("Comprar", 612, "", "57%"), ("Alquilar", 344, "", "32%"), ("Invertir", 122, "", "11%")], icon="route")
    + bars("Tipo de propiedad", "pro", [("Departamento", 452), ("Casa", 196), ("PH", 88), ("Campo", 54), ("Terreno", 42), ("Local u oficina", 38), ("Temporario", 34)], color="var(--blu)", icon="home")
    + bars("Ambientes", "pro", [("Monoambiente", 82), ("2 ambientes", 286), ("3 ambientes", 214), ("4 o más", 98)], "Base 680 (63%) · Señal.", color="var(--pnk)", icon="layers")
    + bars("MIA Tools", "pro", [("Comparador UVA", 188), ("¿Cuánto vale mi propiedad?", 124), ("Calculadora de alquiler", 97), ("Hablar con experto", 83), ("Amoblar con IA", 74)], color="var(--good)", icon="sliders")
    + "</div>"
    + sub("Presupuesto declarado")
    + '<div class="g2">'
    + bars("Alquiler · pesos por mes", "pro", [("Hasta $400.000", 92), ("$400.000 a $700.000", 148), ("$700.000 a $1.000.000", 64), ("Más de $1.000.000", 22)], "Base 326 de 344 que alquilan (95%) · Hecho.", color="var(--vio)", icon="dollar")
    + bars("Compra · dólares", "pro", [("Hasta USD 80.000", 58), ("USD 80.000 a 150.000", 112), ("USD 150.000 a 250.000", 74), ("Más de USD 250.000", 36)], "Base 280 de 612 que compran (46%) · Señal: doble lectura.", color="var(--blu)", icon="dollar")
    + "</div>"
    + '<div class="adv mt">' + table(["Pedido sin oferta (Bolsa de Pedidos)", "Consultas", "Avisos activos en MIA", "Consultas por aviso"],
                                    [["Alquiler 1 y 2 amb. · Nueva Córdoba · hasta $450.000", 72, 18, "4,0"], ["Casa con patio · GBA Norte · USD 90 a 130 mil", 61, 38, "1,6"], ["Campo de 50 a 200 ha · inversión", 22, 4, "5,5"],
                                     ["Temporario · Mar del Plata · enero", 24, 9, "2,7"]], minw=620) + "</div>"
    + yeq("Córdoba Capital crece 28% y Nueva Córdoba tiene 4 consultas por aviso: es el argumento para salir a buscar inmobiliarias cordobesas, con el dato en la mano.")
)

# --- Criterio comercial (valor más frecuente grande)
CRIT = [
    ("Problema declarado", "quote", 82, "Paga un portal y le llegan pocas consultas", 41, [("Paga un portal y le llegan pocas consultas", 41), ("No tiene web propia", 24), ("Le cuesta gestionar los avisos", 19)], "Declarado por el lead", "Gap Selling"),
    ("Impacto", "flame", 74, "3 a 10 propiedades sin rotar", 45, [("3 a 10 propiedades sin rotar", 45), ("Más de 10 propiedades", 34), ("1 o 2 propiedades", 21)], "Inferido por el agente", "Gap Selling"),
    ("Causa raíz", "compass", 31, "Avisos sin fotos ni precio al día", 38, [("Avisos sin fotos ni precio al día", 38), ("Publica en un solo canal", 33), ("No responde rápido", 29)], "Inferido por el agente", "Gap Selling"),
    ("Evento disparador", "bolt", 63, "El portal actual subió el precio", 46, [("El portal actual subió el precio", 46), ("Captó propiedades nuevas", 28), ("Abrió una sucursal", 14)], "Declarado por el lead", "Jobs to be Done"),
    ("Resultado de contacto", "cal", 88, "Demo con fecha acordada", 52, [("Demo con fecha (avance)", 52), ("Sigue la charla sin fecha", 31), ("No venta, con motivo", 17)], "Cargado por Ventas", "SPIN"),
]


def crit_card(t, icn, cov, top, share, rows, origin, metod):
    rr = "".join(f'<div class="cr-r"><span>{a}</span><b>{b}%</b><div class="qf"><div class="qh" style="width:{b}%;background:var(--vio)"></div></div></div>' for a, b in rows)
    return (f'<div class="qx crit2"><div class="c2-h"><span class="c2-ic">{ic(icn)}</span><b>{t}</b>{lvl(cov)}</div>'
            f'<div class="c2-q"><span class="c2-k">Valor más frecuente</span><div class="c2-v">{top}</div><div class="c2-s"><b>{share}%</b> de los que lo declaran</div></div>'
            f'<div class="c2-rows">{rr}</div><div class="c2-f"><span>{ic("filter")}Cobertura {cov}%</span><span>{ic("info")}{origin}</span><span>{ic("compass")}{metod}</span></div></div>')


P["criterio"] = (
    head_sec(f"Criterio comercial · sobre las {CAL_AMP} calificadas", "Qué le duele a la inmobiliaria", "y qué la hace escribir hoy.",
             "El valor más frecuente de cada campo, con su cobertura y de dónde sale.",
             "Perfil B2B de suscripción con recompra: núcleo de cinco campos + capa Gap Selling y resultado de contacto. Impacto y causa raíz son señales blandas: sin refuerzo en el prompt nacen en Indicio.")
    + g4(kpi("quote", "", "pro", "Problema declarado", "82%", bsc="144 de 176 · Hecho"),
         kpi("flame", "amb", "pro", "Impacto alto", "44", bsc="34% de 130 con impacto · Señal"),
         kpi("bolt", "blu", "pro", "Disparador hace menos de 30 días", "61%", bsc="68 de 111 con disparador · Señal"),
         kpi("cal", "grn", "pro", "Avance con fecha", "52%", "+9 p.p.", bsc="resultado de contacto, cargado por Ventas"))
    + sub("Los cinco campos · valor más frecuente")
    + '<div class="crit-g">' + "".join(crit_card(*c) for c in CRIT) + "</div>"
    + sub("A quién llamar primero", "impacto × evento disparador")
    + table(["Impacto \\ disparador", "Subió el portal", "Captó propiedades", "Abrió sucursal", "Sin disparador"],
            [["<b>Alto</b> · más de 10 propiedades", "<b class='hot'>19</b>", 9, 6, 10], ["<b>Medio</b> · 3 a 10", 21, 11, 4, 22], ["<b>Bajo</b> · 1 o 2", 6, 8, 2, 12]], minw=620)
    + '<p class="qcm">Base: 130 con impacto cargado (74%). Celda prioritaria: 19 inmobiliarias grandes a las que el portal les subió el precio.</p>'
    + yeq("«El portal me subió el precio» es el disparador dominante: el mensaje de venta es precio y llegada. Primero se llama a las 19 inmobiliarias grandes de esa celda.")
)

# --- Audiencias
P["audiencias"] = (
    head_sec("Audiencias · listas para la pauta", "Cada lista con su tag de origen", "y su tamaño real.",
             "Quién entra como semilla y quién se excluye.",
             "Similares en TikTok y Meta desde 1.000 coincidencias reales. La señal de calificada (Conversions API y Events API de TikTok) vale solo si el tag está bien cargado.")
    + g4(kpi("seed", "grn", "pro", "Semilla de similares", str(CAL_AMP), bsc="de 1.000 coincidencias necesarias · 18%"),
         kpi("flame", "amb", "pro", "Hot leads para retargeting", str(HOT), bsc="Smart Tag Hot lead"),
         kpi("x", "", "pro", "Excluidos de la pauta comercial", "1.241", bsc="1.214 particulares + 27 altas"),
         kpi("checkc", "blu", "calc", "Listas listas para usar", "4 de 6", bsc="2 esperan volumen"))
    + '<div class="g3 mt">'
    + "".join(stat(i, t, "pro", v, "", d, [(tag, "tag de origen"), (uso, "uso")], tone=c) for i, t, v, d, tag, uso, c in [
        ("building", "Inmobiliarias calificadas", str(CAL_AMP), "Semilla de público similar para TikTok y Meta.", "Calificada", "semilla", "var(--good)"),
        ("flame", "Hot leads", str(HOT), "Retargeting con Click to WhatsApp: «pedí tu demo hoy».", "Hot lead", "retargeting", "var(--warn)"),
        ("lock", "Altas actuales", "27 + base", "Se excluyen de toda la pauta de venta.", "Suscripto", "exclusión", "var(--vio)"),
        ("user", "Particulares que buscan", "1.078", "Se excluyen de la pauta a inmobiliarias; semilla para la pauta de descarga.", "Particular", "exclusión", "var(--blu)"),
        ("phone", "Descargaron y no se registraron", "298", "Recordatorio de registro por WhatsApp, con plantilla de utilidad.", "descargo_no_registro", "reactivación", "var(--pnk)"),
        ("dollar", "Inversores", "122", "Pauta de emprendimientos de desarrolladoras.", "Inversor", "semilla", "var(--good)")])
    + "</div>"
    + yeq("Excluir a los particulares de la pauta a inmobiliarias es lo más barato que se puede hacer esta quincena. Las 298 personas trabadas en el registro son una lista lista para reactivar.")
)

# --- Consumo de tokens con tres vistas: todo, Meta y tokens de IA
IA_USD = 736
META_MKT = 1800 * 89.56
cons_todo = (
    g4(kpi("bot", "", "pro", "Suscripción Prometheo", "USD 149", bsc="plan Enterprise · fijo por mes"),
       kpi("bolt", "blu", "calc", "Tokens de IA · quincena", f"USD {IA_USD}", "+8%", flat=True, bsc="1.840 charlas × USD 0,40 (proyección)"),
       kpi("meta", "pnk", "calc", "Meta · mensajes de WhatsApp", ars(META_MKT), bsc="1.800 plantillas de marketing"),
       kpi("checkc", "grn", "calc", "Costo de IA por resuelta", "USD 0,61", bsc="USD 736 ÷ 1.214 resueltas"))
    + '<div class="g3 mt">'
    + stat("bot", "Prometheo cobra la inteligencia", "calc", "USD 885", "por quincena", "Suscripción del mes + tokens de IA de la quincena. Se paga en dólares.", [("USD 149", "suscripción"), ("USD 736", "tokens")])
    + stat("meta", "Meta cobra el canal", "calc", ars(META_MKT), "por quincena", "Mensajes de WhatsApp que salen por API. Se paga en pesos.", [("$0", "servicio"), (ars(META_MKT), "marketing")], tone="var(--pnk)")
    + stat("info", "Por qué no se suman", "calc", "2 facturas", "", "Distinta moneda y distinto proveedor. El tablero los muestra al lado, nunca en un total.", [("USD", "Prometheo"), ("ARS", "Meta")], tone="var(--blu)")
    + "</div>"
)
cons_meta = (
    g4(kpi("chat", "grn", "calc", "Servicio · respuestas", "$0", bsc="dentro de ventana y del cupo de 1.000"),
       kpi("mega", "pnk", "calc", "Marketing · plantillas", ars(META_MKT), bsc="1.800 × ARS 89,56"),
       kpi("clock", "", "calc", "Utilidad · recordatorios", "$0", bsc="sin envíos en la quincena"),
       kpi("meta", "blu", "pro", "Entran por Click to WhatsApp", "9%", bsc="168 de 1.840 · ventana gratis de 72 h"))
    + '<div class="g2 mt">'
    + bars("Mensajes por categoría", "calc", [("Servicio · respuesta del agente", 4120, "4.120", "$0"), ("Marketing · difusión", 1800, "1.800", ars(META_MKT)), ("Utilidad", 0.01, "0", "$0")],
           "Tarifas de lista, Argentina, sin impuestos: servicio y utilidad ARS 37,68 · marketing ARS 89,56. 1.000 mensajes de servicio gratis por mes por número.", color="var(--pnk)", icon="wa")
    + bars("Puerta de entrada", "pro", [("Mensaje directo en redes", 900, "900", "49%"), ("WhatsApp orgánico y difusión", 652, "652", "35%"), ("Click to WhatsApp", 168, "168", "9%"), ("Gmail", 120, "120", "7%")],
           "Con poco Click to WhatsApp, la ventana gratis cubre poco: el servicio entra en el cupo de 1.000 por ahora.", color="var(--blu)", icon="inb")
    + "</div>"
)
cons_ia = (
    g4(kpi("bolt", "blu", "calc", "Tokens de IA · quincena", f"USD {IA_USD}", "+8%", flat=True, bsc="proyección USD 0,40 por charla"),
       kpi("chat", "", "calc", "Costo por charla procesada", "USD 0,40", bsc="sin panel de consumo todavía"),
       kpi("user", "amb", "calc", "Consumo de particulares", "66%", bsc="USD 486 · no pueden pagar un plan"),
       kpi("alert", "", "pro", "Cortes por saldo", "Sin dato", bsc="falta conectar el panel de consumo"))
    + '<div class="g2 mt">'
    + bars("En qué se gasta la IA", "calc", [("Conversación con particulares", 405, "USD 405", "55%"), ("Conversación con cuentas comerciales", 184, "USD 184", "25%"), ("Extracción de variables", 88, "USD 88", "12%"), ("Smart Tags", 44, "USD 44", "6%"), ("Soporte y Mi Prometheo", 15, "USD 15", "2%")],
           "Extracción y Smart Tags se cobran en cada charla, aunque no completen nada.", color="var(--vio)", icon="pie")
    + f'<div class="qx"><div class="qw">{ic("alert")}Cortes de saldo{src("pro")}</div><div class="empty-st">{ic("info", "width:22px;height:22px;color:var(--ink4)")}<p><b>Sin datos suficientes en este período.</b><br>Falta conectar el panel «Entendé tu consumo» de Prometheo. Si el saldo llega a cero, el agente deja de responder: se declara en Integraciones.</p></div></div>'
    + "</div>"
)
P["tokens"] = (
    head_sec("Consumo de Tokens · CRM", "Prometheo cobra la inteligencia,", "Meta cobra el canal.",
             "Tres costos que no se mezclan: la suscripción, los tokens de IA y los mensajes de Meta.",
             "Escenario [CÁLCULO]: sin panel de consumo todavía. Tarifas de Meta: rate card oficial en pesos, Argentina, desde el 1/10/2026, sin impuestos.")
    + '<div class="segt"><label for="cs-todo">' + ic("grid") + 'Todo</label><label for="cs-meta">' + ic("meta") + 'Meta</label><label for="cs-ia">' + ic("bolt") + 'Tokens de IA</label></div>'
    + f'<div class="cstab cs-todo">{cons_todo}</div><div class="cstab cs-meta">{cons_meta}</div><div class="cstab cs-ia">{cons_ia}</div>'
    + yeq("Dos de cada tres dólares de IA los consumen particulares que se resuelven con un link a la app. Un flujo corto para ellos baja el costo sin tocar la venta.")
)


# --- Pauta y venta
def ch_summary(name, rows):
    icon, col, soft = CH[name]
    g = tot(rows, "gasto")
    return (f'<div class="chs" style="--cc:{col};--cs:{soft}"><div class="chs-h"><span class="chs-ic">{ic(icon)}</span><div><b>{name}</b><span>{len(rows)} anuncios · {ars(g)}</span></div></div>'
            f'<div class="kv"><div><div class="v">{tot(rows, "conv")}</div><div class="k">charlas</div></div><div><div class="v">{tot(rows, "calif")}</div><div class="k">calificadas</div></div>'
            f'<div><div class="v">{tot(rows, "altas")}</div><div class="k">altas</div></div><div><div class="v">{ars(g / tot(rows, "calif"))}</div><div class="k">por calificada</div></div></div></div>')


P["pauta"] = (
    head_sec("Pauta y venta · cada anuncio, por separado", "TikTok y Meta ven el clic.", "Prometheo ve qué pasó después.",
             "Cada anuncio medido por lo que importa: cuántas inmobiliarias califican y cuántas se dan de alta.",
             "Cruce por ID de anuncio (Meta, Click to WhatsApp) y por código en el mensaje prellenado o UTM (TikTok). El gasto es de cada plataforma; el conteo de charlas es de Prometheo. Nunca se suman.")
    + '<div class="bridge"><div class="eq"><b>TikTok y Meta ven hasta el clic</b> × <b>Prometheo ve del clic al alta</b></div><p>Cada peso de pauta se juzga por la inmobiliaria calificada y el alta que trajo.</p></div>'
    + g4(kpi("dollar", "grn", "calc", "Inversión de la quincena", ars(GASTO), "+9%", flat=True, bsc="TikTok + Instagram + Facebook"),
         kpi("chat", "blu", "pro", "Charlas desde anuncios", n(tot(ADS, "conv")), "+14%", bsc=f"{pc(tot(ADS, 'conv'), CONV)} de las conversaciones"),
         kpi("checkc", "", "pro", "Calificadas desde anuncios", str(CAL_PAGA), "+12%", bsc=f"{ars(GASTO / CAL_PAGA)} por calificada"),
         kpi("lock", "pnk", "erp", "Altas desde anuncios", str(tot(ADS, "altas")), "+5", bsc=f"{ars(GASTO / tot(ADS, 'altas'))} por alta"))
    + sub("Por red")
    + '<div class="g3">' + ch_summary("TikTok", TT) + ch_summary("Instagram", IG) + ch_summary("Facebook", FB) + "</div>"
    + "".join(sub(f"{name} · {len(rows)} anuncios") + '<div class="adg">' + "".join(adcard(a) for a in rows) + "</div>" for name, rows in [("TikTok", TT), ("Instagram", IG), ("Facebook", FB)])
    + '<div class="adv">' + sub("Tabla completa") + ads_table(ADS)
    + '<p class="qcm">IC 95% = intervalo de Wilson de la tasa de calificación. <b>n&lt;30</b> = muestra chica, no comparar. Registros: cruce con los datos de la app.</p></div>'
    + sub("Cómo sabe Prometheo de qué anuncio vino cada charla")
    + '<div class="g2"><div class="qx"><div class="qw">' + ic("doc") + "Variables" + src("pro") + '</div><div class="pm-chips">'
    + "".join(f'<span class="qcs">{v}</span>' for v in ["canal", "tipo_usuario", "intencion_principal", "estado_embudo", "sistema_operativo", "pauta_origen · propuesta", "utm_campaign · propuesta", "ctwa_clid (Meta)"])
    + '</div></div><div class="qx"><div class="qw">' + ic("tag") + "Smart Tags" + src("pro") + '</div><div class="pm-chips">'
    + "".join(f'<span class="qcs">{t}</span>' for t in ["#SOLICITA_DEMO", "#QUIERE_ASESOR", "#CARGA_MASIVA", "#CONSULTA_PUBLICIDAD", "#CONSULTA_MODELO_NEGOCIO", "#PARTNERSHIP", "Calificada", "Hot lead", "Suscripto"])
    + '</div><p class="qcm">TikTok no pasa el ID del anuncio a un mensaje directo: cada anuncio lleva un código en el mensaje prellenado y Prometheo lo guarda en pauta_origen.</p></div></div>'
    + yeq("«Mapa de precios por barrio» es el video más barato por charla y no trajo ninguna alta: atrae a personas que buscan. «Inmobiliarias: subí tu cartera» y «Plan para inmobiliarias» son los que venden.")
)

# --- TikTok
tt_cards = "".join(
    f'<div class="qx vid"><div class="vid-h"><span class="vid-ic">{ic("play")}</span><div><span class="ad-k">Video <code>{a["id"]}</code></span><b>{a["nombre"]}</b></div></div>'
    f'<div class="vid-hook"><span>Gancho · vio 3 segundos</span><b>{a["v3"]}%</b></div>'
    + "".join(f'<div class="cr-r"><span>{l}</span><b>{q}%</b><div class="qf"><div class="qh" style="width:{q}%;background:var(--vio)"></div></div></div>' for l, q in zip(["25% del video", "50%", "75%", "Lo vio completo"], a["q"]))
    + f'<div class="kv" style="--kc:2"><div><div class="v">{a["v6"]}%</div><div class="k">6 s o interactuó</div></div><div><div class="v">{n(a["inter"])}</div><div class="k">interacciones pagas</div></div></div></div>'
    for a in TT)
tt_g = tot(TT, "gasto")
P["tiktok"] = (
    chan_head("play", "TikTok Ads", "Canales Marketing",
              "Las métricas que entrega marketing, en el orden en que las lee TikTok, y al final qué pasó en Prometheo con cada video.",
              "TikTok manda en gasto, distribución, video y píxel. Prometheo manda en charlas, calificación y altas. El píxel cuenta registros; Prometheo cuenta conversaciones: son dos preguntas distintas.")
    + srclegend((["tt"], "Gasto, impresiones, alcance, clics, video y píxel."), (["pro"], "Charlas, cuentas comerciales, calificación y altas."), (["calc"], "CPM, CPC, CPA y costo por calificada."))
    + g4(kpi("dollar", "grn", "tt", "Inversión", ars(tt_g), "+12%", flat=True, bsc=f"4 videos · CPM {ars(tt_g / tot(TT, 'imp') * 1000)}"),
         kpi("eye", "blu", "tt", "Alcance", n(tot(TT, "alc")), "+15%", bsc=f"{n(tot(TT, 'imp'))} impresiones · frecuencia {n(tot(TT, 'imp') / tot(TT, 'alc'), 2)}"),
         kpi("chat", "", "pro", "Charlas en Prometheo", str(tot(TT, "conv")), "+18%", bsc=f"{tot(TT, 'calif')} calificadas"),
         kpi("lock", "pnk", "erp", "Altas", str(tot(TT, "altas")), "+2", bsc=f"{ars(tt_g / tot(TT, 'altas'))} por alta"))
    + sub("1 · Distribución y costo")
    + table(["Video", "Impresiones", "Alcance", "Frecuencia", f'CPM {src("calc")}', "CPC", "Gasto"],
            [[f'<b>{a["nombre"]}</b><span class="sub">{a["id"]}</span>', n(a["imp"]), n(a["alc"]), n(a["imp"] / a["alc"], 2), ars(a["gasto"] / a["imp"] * 1000), ars(a["gasto"] / a["clics"]), ars(a["gasto"])] for a in TT], minw=760)
    + sub("2 · Interacción")
    + table(["Video", "Clics al destino", "CTR", "Interacciones de pago", "Tasa de interacción"],
            [[f'<b>{a["nombre"]}</b><span class="sub">{a["id"]}</span>', n(a["clics"]), pc(a["clics"], a["imp"], 2), n(a["inter"]), pc(a["inter"], a["imp"], 2)] for a in TT], minw=640)
    + sub("3 · Reproducción · el gancho y la retención")
    + f'<div class="g4">{tt_cards}</div>'
    + sub("4 · Conversión · píxel de TikTok al lado de Prometheo")
    + table(["Video", f'Conversiones píxel {src("tt")}', "CPA píxel", "CVR", f'Charlas {src("pro")}', "Calificadas", "Altas", f'Costo por calificada {src("calc")}'],
            [[f'<b>{a["nombre"]}</b><span class="sub">{a["id"]}</span>', a["pixel"], ars(a["gasto"] / a["pixel"]), pc(a["pixel"], a["clics"], 1), a["conv"], a["calif"], f'<b>{a["altas"]}</b>', ars(a["gasto"] / a["calif"])] for a in TT], minw=900)
    + '<p class="qcm">El píxel dice que «Mapa de precios» es el mejor (CPA más bajo). Prometheo dice que no trajo ninguna alta. Las dos cosas son ciertas: convierte personas que buscan, no inmobiliarias.</p>'
    + yeq("«Mapa de precios» tiene el mejor gancho y no vende: el video funciona, la audiencia no. «Inmobiliarias: subí tu cartera» retiene menos pero vende: subir presupuesto y probar un gancho más fuerte en los primeros 3 segundos.")
)


def meta_tab(name, rows, edad, lectura):
    icon, col, soft = CH[name]
    g = tot(rows, "gasto")
    plc = {}
    for a in rows:
        plc[a["ubic"]] = plc.get(a["ubic"], 0) + a["imp"]
    return (
        chan_head(icon, name, "Meta Ads · Canales Marketing",
                  f"El cruce de cada anuncio de {name} con Prometheo: qué pasó con cada clic dentro del CRM.",
                  "Meta manda en inversión, alcance, impresiones y clics; Prometheo manda en cuántas charlas hubo y qué pasó con ellas. CTR = clics ÷ impresiones · CPC = costo por clic · CPM = costo cada mil impresiones.")
        + srclegend((["meta"], "Inversión, alcance, impresiones, clics y ubicaciones."), (["pro"], "Charlas, calificación, demos y altas."), (["calc"], "Costo por calificada y por alta."))
        + g4(kpi("dollar", "grn", "meta", "Inversión", ars(g), "+6%", flat=True, bsc=f"{len(rows)} anuncios · CPM {ars(g / tot(rows, 'imp') * 1000)}"),
             kpi("eye", "blu", "meta", "Alcance", n(tot(rows, "alc")), "+8%", bsc=f"CTR {pc(tot(rows, 'clics'), tot(rows, 'imp'), 2)} · CPC {ars(g / tot(rows, 'clics'))}"),
             kpi("checkc", "", "pro", "Calificadas", str(tot(rows, "calif")), "+12%", bsc=f"{pc(tot(rows, 'calif'), tot(rows, 'b2b'))} de las cuentas comerciales"),
             kpi("lock", "pnk", "erp", "Altas", str(tot(rows, "altas")), "+2", bsc=f"{ars(g / tot(rows, 'altas'))} por alta"))
        + steps("Del anuncio al alta", "Meta ve hasta el clic, Prometheo todo lo que sigue",
                [("Impresiones", tot(rows, "imp"), "veces que se vio"), ("Clics", tot(rows, "clics"), "al destino"), ("Charlas", tot(rows, "conv"), "en Prometheo"),
                 ("Cuentas comerciales", tot(rows, "b2b"), "inmobiliarias y desarrolladoras"), ("Calificadas", tot(rows, "calif"), "lectura amplia"), ("Demos", tot(rows, "demos"), "pedidas", "leak"), ("Altas", tot(rows, "altas"), "plan pago")])
        + sub("Anuncio por anuncio")
        + '<div class="adg">' + "".join(adcard(a) for a in rows) + "</div>"
        + sub("Dónde se vio y a quién llegó")
        + '<div class="g2">'
        + bars("Ubicación", "meta", [(k, v, n(v), pc(v, tot(rows, "imp"))) for k, v in sorted(plc.items(), key=lambda x: -x[1])], "Impresiones por ubicación principal de cada anuncio.", color=col, icon="layers")
        + bars("Edad del público alcanzado", "meta", edad, "Distribución de alcance que informa Meta.", color=col, icon="users")
        + "</div>"
        + '<div class="adv mt">' + ads_table(rows) + "</div>"
        + yeq(lectura))


P["instagram"] = meta_tab("Instagram", IG, [("18 a 24", 8, "", "8%"), ("25 a 34", 38, "", "38%"), ("35 a 44", 31, "", "31%"), ("45 a 54", 18, "", "18%"), ("55 o más", 5, "", "5%")],
                          "«Pedí tu demo por WhatsApp» trae más inmobiliarias por peso y «Plan para inmobiliarias» es el que más califica. «Amoblá tu propiedad con IA» gusta pero atrae a quien busca: pasa a la pauta de descarga de la app.")
P["facebook"] = meta_tab("Facebook", FB, [("18 a 24", 4, "", "4%"), ("25 a 34", 18, "", "18%"), ("35 a 44", 34, "", "34%"), ("45 a 54", 29, "", "29%"), ("55 o más", 15, "", "15%")],
                         "Facebook llega a un público mayor, más propietario y más de campo. «Bolsa de pedidos» y «Campos» califican bien con poco gasto; «Vendé sin intermediarios» trae particulares y ninguna alta.")

# --- Email (estructura EDFAN)
EM_SEG = [("Inmobiliarias con plan vencido", "Volvé a publicar con 30% off", 1400, 1360, 520, 128, 31, 9, 2), ("Registrados que nunca publicaron", "Publicá tu primer aviso gratis", 2800, 2700, 760, 154, 22, 2, 0),
          ("Desarrolladoras sin emprendimiento cargado", "Mostrá tu proyecto a inversores", 320, 312, 140, 36, 8, 4, 0)]
emt = [sum(s[i] for s in EM_SEG) for i in range(2, 9)]
P["email"] = (
    chan_head("mail", "Email Marketing", "Canales Marketing",
              "El email <b>genera la conversación</b>: sale desde el correo de MIA y el agente de Prometheo responde, califica y ofrece la demo. Lo que importa no es cuántos lo abrieron sino <b>cuántos terminaron conversando</b>.",
              "La plataforma de email manda en envíos, entregas, aperturas, clics, rebotes y bajas; Prometheo, en las conversaciones y la calificación. <b>Empalme</b>: escribieron a Prometheo dentro de las 72 h del clic ÷ clics únicos (ventana propuesta). La apertura se infla por la precarga de imágenes: no titula.")
    + srclegend((["mail"], "Enviados, entregados, aperturas, clics, rebotes y bajas."), (["pro"], "Quién conversó con el agente, calificación y demo."), (["calc"], "Empalme, CTOR y calificación por segmento."))
    + sub("De dónde sale la base · tres segmentos")
    + '<div class="g3">'
    + stat("building", "Inmobiliarias con plan vencido", "erp", "1.400", "", "Pagaron un plan y no renovaron. El mail ofrece volver con descuento.", [("Suscripto vencido", "tag de origen"), ("cliente", "consentimiento")])
    + stat("user", "Registrados que nunca publicaron", "app", "2.800", "", "Se registraron y no cargaron un aviso. El mail los lleva a publicar gratis.", [("registrado", "estado_embudo"), ("registro", "consentimiento")], tone="var(--blu)")
    + stat("layers", "Desarrolladoras sin emprendimiento", "pro", "320", "", "Escribieron alguna vez y no cargaron su proyecto en Emprendimientos.", [("Desarrolladora", "tipo_usuario"), ("consultó", "consentimiento")], tone="var(--pnk)")
    + "</div>"
    + steps("La campaña · tres envíos, uno por segmento", f"base: {n(emt[0])} · titula el empalme, no la apertura",
            [("Enviados", emt[0], "contactos"), ("Entregados", emt[1], ""), ("Abrieron", emt[2], "no titula", "dim"), ("Clic", emt[3], "únicos"),
             ("Conversaron en Prometheo", emt[4], "en 72 h", "leak"), ("Calificaron", emt[5], "cuentas comerciales"), ("Alta", emt[6], "plan pago")], icon="mail")
    + sub("Por segmento · el mismo embudo para los tres")
    + table(["Segmento", "Concepto del envío", "Base", "Entreg.", "Clic", "Empalme", "Calificó", "Alta"],
            [[f"<b>{s[0]}</b>", s[1], n(s[2]), n(s[3]), s[5], f'{s[6]} <small>{pc(s[6], s[5])}</small>', s[7], f"<b>{s[8]}</b>"] for s in EM_SEG],
            ["Total", "—", n(emt[0]), n(emt[1]), emt[3], f'{emt[4]} ({pc(emt[4], emt[3])})', emt[5], emt[6]], minw=860)
    + g4(kpi("mail", "", "mail", "Tasa de entrega", pc(emt[1], emt[0]), bsc=f"{n(emt[1])} de {n(emt[0])}"),
         kpi("alert", "amb", "mail", "Rebotes", str(emt[0] - emt[1]), bsc="62 duros · 86 blandos"),
         kpi("minus", "pnk", "mail", "Bajas", "41", bsc="1,0% de los entregados"),
         kpi("sigma", "blu", "calc", "CTOR", pc(emt[3], emt[2], 1), bsc="clics ÷ aperturas: calidad del contenido"))
    + yeq("Las inmobiliarias con plan vencido empalman 24% de los clics y trajeron las 2 altas. Los registrados sin publicar hacen clic pero conversan poco: el mail tiene que llevarlos directo a publicar en la app, no al chat.")
)

# --- WhatsApp Marketing (estructura EDFAN)
WA_SEG = [("Inmobiliarias calificadas sin demo", "Agendá tu demo de 15 minutos", 620, 604, 451, 58, 14, "calificaron", "var(--good)"),
          ("Descargaron y no se registraron", "Terminá tu registro en 1 minuto", 820, 796, 590, 49, 31, "se registraron", "var(--blu)"),
          ("Inversores", "Nuevos emprendimientos en preventa", 360, 342, 249, 21, 3, "calificaron", "var(--pnk)")]
wt = [sum(s[i] for s in WA_SEG) for i in range(2, 6)]
P["wamkt"] = (
    chan_head("wa", "WhatsApp Marketing", "Canales Marketing",
              "En WhatsApp no hay clic: <b>titula la respuesta</b>. La lectura está subestimada (quien apagó la confirmación de lectura no cuenta) y no titula.",
              "La plataforma de envío manda en enviados, entregados, leídos, tier y calidad del número; Prometheo, en respuestas, calificación y demos. Respuesta con doble lectura: sobre entregados y sobre leídos. Costo de Meta: plantilla de marketing ARS 89,56 por envío (rate card oficial, Argentina, sin impuestos).")
    + srclegend((["wpp"], "Enviados, entregados, leídos, tier y calidad del número."), (["pro"], "Respuestas, calificación, demos y registros."), (["calc"], "Respuesta por segmento y costo por respuesta."))
    + g4(kpi("wa", "grn", "wpp", "Respuesta", pc(wt[3], wt[1], 1), bsc=f"{wt[3]} de {n(wt[1])} entregados · {pc(wt[3], wt[2], 1)} de los leídos", qcp="Doble lectura: sobre entregados y sobre leídos."),
         kpi("checkc", "", "pro", "Respuestas calificadas", "17", bsc="inmobiliarias e inversores · 2 altas"),
         kpi("shield", "grn", "wpp", "Calidad del número", "Alta", bsc="tier 10.000 contactos por día · actualizado 13/10", qcp="Si la calidad baja, el hallazgo es ese, no la respuesta."),
         kpi("dollar", "amb", "calc", "Costo de Meta de la difusión", ars(wt[0] * 89.56), bsc=f"{n(wt[0])} plantillas de marketing × ARS 89,56"))
    + steps("La difusión · tres segmentos, una plantilla por segmento", f"base: {n(wt[0])} enviados · titula la respuesta",
            [("Enviados", wt[0], "plantilla marketing"), ("Entregados", wt[1], ""), ("Leídos", wt[2], "subestimado", "dim"), ("Respondieron", wt[3], "en Prometheo", "leak"),
             ("Calificaron", 17, "cuentas comerciales"), ("Alta", 2, "plan pago")], icon="wa")
    + sub("Por segmento")
    + '<div class="g3">'
    + "".join(f'<div class="qx qcg" style="--ct:{c}"><div class="qw">{ic("wa")}{t}{src("wpp")}</div><div class="qy" style="font-size:26px">{pc(r, e, 1)} <small class="u">respondió</small></div>'
              f'<div class="qz">«{msg}»</div><div class="kv"><div><div class="v">{e}</div><div class="k">entregados</div></div><div><div class="v">{r}</div><div class="k">respuestas</div></div><div><div class="v">{q}</div><div class="k">{ql}</div></div></div>'
              f'<div class="adv"><div class="kv"><div><div class="v">{pc(l, e)}</div><div class="k">leyó</div></div><div><div class="v">{pc(r, l, 1)}</div><div class="k">respondió de los que leyeron</div></div><div><div class="v">{ars(env * 89.56)}</div><div class="k">costo de Meta</div></div></div></div></div>'
              for t, msg, env, e, l, r, q, ql, c in WA_SEG)
    + "</div>"
    + '<p class="qcm">«Descargaron y no se registraron» es un mensaje de utilidad: aprobado como plantilla de utilidad cuesta ARS 37,68 en vez de 89,56.</p>'
    + yeq("Las inmobiliarias calificadas sin demo responden 9,6% y trajeron las 2 altas. El recordatorio de registro destrabó 31 registros y conviene pasarlo a plantilla de utilidad: cuesta menos de la mitad.")
)

# --- Action Driven
RUB_NAMES = ["Base y denominador", "Fuente y trazabilidad", "Cobertura", "Profundidad", "Evidencia previa", "Cierre medible"]
RUB_MAX = [20, 15, 15, 20, 15, 15]
CARDS = [
    dict(grp="Esta semana", v="activar", owner="Ventas", rub=[14, 10, 11, 15, 10, 15], tema="Demos sin hacer",
         title="15 inmobiliarias pidieron una demo y no la tuvieron", corto="Llamarlas hoy y ofrecer dos horarios cerrados.", cuando="Hoy", meta="12 de 15 demos hechas",
         mide="Pedidos de demo sin demo realizada", base=f"{DEMO_AG} pedidos de demo en la quincena", dato="15 sin demo · 9 son hot leads",
         hacer="Que el vendedor de turno llame hoy a las 15 inmobiliarias y ofrezca dos horarios cerrados; registrar la demo con el tag Demo realizada.", donde="Bandeja de Ventas en Prometheo · filtro #SOLICITA_DEMO sin Demo realizada",
         efecto="+3 a +5 altas en la próxima quincena, con la tasa actual de demo a alta (52%).", medimos="Demos pedidas sin realizar, cada lunes.", guardiana="Que la tasa de demo a alta no caiga por apurar demos."),
    dict(grp="Esta semana", v="decidir", owner="Marketing", rub=[20, 15, 7, 15, 5, 15], tema="Presupuesto de TikTok",
         title="El video «Mapa de precios» trajo 188 charlas y ninguna alta", corto="Mover la mitad de su presupuesto al video para inmobiliarias.", cuando="Esta semana", meta="+2 a +4 altas",
         mide="Gasto, charlas y altas por video", base="4 videos de TikTok · 465 charlas", dato="«Mapa de precios»: 0 altas · «Inmobiliarias: subí tu cartera»: 5 altas",
         hacer="Pasar $150.000 de «Mapa de precios» a «Inmobiliarias: subí tu cartera» durante una quincena. «Mapa de precios» sigue, con objetivo de descarga de la app.", donde="TikTok Ads Manager · presupuesto por grupo de anuncios",
         efecto="+2 a +4 altas con el mismo gasto total de TikTok.", medimos="Altas del video para inmobiliarias ÷ gasto, al cierre de la quincena.", guardiana="Que el % de calificación de ese video no baje de 50%."),
    dict(grp="Esta semana", v="corregir", owner="Dirección", rub=[20, 10, 15, 15, 5, 15], tema="Registro y verificación",
         title="Los problemas de acceso a la cuenta subieron 33%", corto="Revisar el login y el envío del código de verificación.", cuando="Esta semana", meta="Menos de 190 charlas",
         mide="Charlas con Smart Tags de Acceso y cuenta", base=f"{n(SOPORTE)} charlas con problema técnico", dato="248 de Acceso (antes 186) · #LOGIN_REGISTRO 132",
         hacer="Que el equipo de producto revise el registro y el envío del código de verificación; el agente ya junta sistema operativo, error, paso y captura.", donde="App de MIA · flujo de registro y verificación",
         efecto="Volver a 186 charlas de acceso o menos, y +100 registros por quincena.", medimos="Charlas con Smart Tags de Acceso, cada semana.", guardiana="Que no suban las charlas de Publicaciones por el cambio."),
    dict(grp="Próxima quincena", v="separar", owner="AUREA", rub=[20, 10, 15, 10, 10, 15], tema="Costo de IA",
         title="Dos de cada tres dólares de IA van a particulares", corto="Responderles en dos mensajes y mandarlos a la app.", cuando="Próxima quincena", meta="−25% a −35% de costo",
         mide="Reparto del gasto de IA por tipo de usuario", base="1.840 charlas · USD 736 proyectados", dato="Particulares: USD 486",
         hacer="Cuando el agente detecta un particular que busca, responde con el link a la app y la MIA Tool que corresponde en dos mensajes, y cierra.", donde="Prometheo · prompt del agente, sector de ruteo",
         efecto="−25% a −35% del costo de IA por charla de particular.", medimos="USD por charla de particular procesada.", guardiana="Que el % de resueltas sin contacto humano no baje de 66%."),
    dict(grp="Próxima quincena", v="proteger", owner="AUREA", rub=[20, 10, 11, 10, 5, 15], tema="Escalamientos técnicos",
         title="4 de cada 10 escalamientos llegan al técnico sin los datos", corto="Pedir siempre los 4 datos antes de derivar.", cuando="Próxima quincena", meta="85% completos",
         mide="Escalamientos con sistema operativo, error, paso y captura", base="168 escalamientos", dato="102 completos (61%)",
         hacer="Reforzar en el prompt los 4 datos mínimos antes de derivar, sin pedir nunca contraseñas ni códigos.", donde="Prometheo · prompt del agente, sector de soporte",
         efecto="85% de escalamientos completos y menos idas y vueltas con el técnico.", medimos="% de escalamientos completos.", guardiana="Que no suba el abandono de la charla por pedir datos."),
    dict(grp="Próxima quincena", v="medir", owner="Marketing", rub=[20, 10, 7, 5, 5, 10], tema="Atribución de TikTok",
         title="3 de cada 10 charlas de TikTok no dicen de qué video vinieron", corto="Poner un código en el mensaje de cada video.", cuando="Próxima quincena", meta="90% atribuidas",
         mide="Charlas de TikTok con el código del video", base="465 charlas de TikTok", dato="330 con código (71%)",
         hacer="Mensaje prellenado con código en todos los videos y link con UTM a una landing con píxel.", donde="TikTok Ads · mensaje y URL de cada anuncio",
         efecto="90% de las charlas de TikTok atribuidas a un video.", medimos="% de charlas de TikTok con código.", guardiana="Que no bajen las charlas de TikTok por el paso extra."),
    dict(grp="Para decidir", v="decidir", owner="Dirección", rub=[20, 5, 0, 5, 5, 5], tema="Definición de calificada",
         title=f"Hoy las oportunidades calificadas son un rango: {CAL_EST} a {CAL_AMP}", corto="Validar con MIA qué es una inmobiliaria calificada.", cuando="Antes del próximo corte", meta="Un solo número",
         mide="Criterio de calificación de la cuenta comercial", base=f"{B2B} cuentas comerciales", dato=f"{CAL_EST} estricto · {CAL_AMP} amplio",
         hacer="Reunión de 30 minutos con MIA para validar obligatorios, condiciones que suman y señales de hot lead.", donde="Doc 1 · bloque B3",
         efecto="El número de calificadas deja de ser rango y puede titular.", medimos="Diferencia entre la definición propuesta y la validada.", guardiana="Que la cohorte no cambie entre pestañas."),
]


def score_of(c):
    return sum(c["rub"])


def action(c):
    score = score_of(c)
    rub = "".join(f'<div class="qd"><span>{k}</span><span class="qe"><i style="width:{100 * a / b:.0f}%"></i></span><b>{a}/{b}</b></div>' for k, a, b in zip(RUB_NAMES, c["rub"], RUB_MAX))
    return (f'<details class="i3 av" data-v="{c["v"]}"><summary>'
            f'<div class="ad-top"><span class="qby"><span class="qcd">{ic(VERB_IC[c["v"]])}</span>{c["v"].capitalize()}</span><span class="qce {OWNER[c["owner"]]}">{c["owner"]}</span>{sx(score)}</div>'
            f'<div class="ad-tema">{c["tema"]}</div><div class="ad-title">{c["title"]}</div>'
            f'<div class="ad-do">{ic("arrow")}<div><b>Qué hacemos</b><span>{c["corto"]}</span></div></div>'
            f'<div class="ad-meta"><span>{ic("clock")}<em>Cuándo</em><b>{c["cuando"]}</b></span><span>{ic("target")}<em>Meta</em><b>{c["meta"]}</b></span></div>'
            f'<div class="qbh"><div class="cx"><span class="ql qbm">{ic("target")}</span><span class="qm">Qué mide</span><span class="qn">{c["mide"]}</span></div>'
            f'<div class="cx"><span class="ql qbi">{ic("filter")}</span><span class="qm">Base</span><span class="qn">{c["base"]}</span></div>'
            f'<div class="cx"><span class="ql qbn">{ic("chat")}</span><span class="qm">Dato</span><span class="qn">{c["dato"]}</span></div></div>'
            f'<div class="qbd"><span class="op">Ver el detalle</span><span class="cl">Plegar</span>{ic("chev")}</div></summary>'
            f'<div class="qa"><div class="qb"><span class="n">{ic("arrow")}</span>Qué hacer</div><p class="qp">{c["hacer"]}</p>'
            f'<div class="qu">{ic("pin")}<span><b>Dónde se cambia:</b> {c["donde"]}</span></div></div>'
            f'<div class="qa"><div class="qb"><span class="n">{ic("target")}</span>Efecto esperado</div><p class="qp">{c["efecto"]}</p></div>'
            f'<div class="qa"><div class="qb"><span class="n">{ic("pulse")}</span>Cómo lo medimos</div><p class="qp">{c["medimos"]}</p>'
            f'<div class="qbs">{ic("shield")}<span><b>Guardiana:</b> {c["guardiana"]}</span></div></div>'
            f'<div class="qa qbo"><div class="qb"><span class="n">{ic("gauge")}</span>Por qué este índice {sx(score, True)}</div>'
            f'<div class="qbz">{rub}</div><p class="qbj">Índice ilustrativo de la demo: calculado como si las cifras vinieran del export real. Con el export de Prometheo se recalcula; mientras el dato sea modelado, el techo es 54. Rúbrica v1, sin calibrar.</p></div></details>')


PM = [
    ("pmA", "activar", "Ventas", "var(--crit)", "Urgente", "Aviso al vendedor cuando una inmobiliaria pide demo", "El Smart Tag #SOLICITA_DEMO ya existe. Falta que avise al vendedor de turno en el momento.", "15", "demos sin hacer",
     "Necesito cambiar la acción del Smart Tag &quot;#SOLICITA_DEMO&quot; del asistente de MIA.\n- Que envíe una notificación al vendedor de turno con nombre, tipo_usuario, canal y cantidad de propiedades.\n- No cambies el prompt de asignación del tag.\nAntes de guardar, mostrame cómo queda la acción y a quién le llega. No apliques nada hasta que te confirme con &quot;Sí, confirmar&quot;."),
    ("pmB", "proteger", "AUREA", "var(--warn)", "Alta", "Pedir los 4 datos antes de derivar al técnico", "El agente ya los pide a veces. Falta que sea obligatorio antes de usar #ESCALAMIENTO_TECNICO.", "66", "escalamientos incompletos",
     "Necesito ajustar el sector de soporte del asistente de MIA.\n- Antes de derivar con #ESCALAMIENTO_TECNICO, pedir una por vez: sistema operativo, texto del error o pantalla, en qué paso se traba y una captura.\n- Nunca pedir contraseñas ni códigos.\n- No repreguntar lo que el usuario ya dijo.\nAntes de guardar, mostrame el sector como queda. No apliques nada hasta que te confirme con &quot;Sí, confirmar&quot;."),
]


def pm(p, i):
    pid, v, owner, col, pri, title, why, cnt, cntl, prompt = p
    return (f'<details class="pm" id="{pid}" style="--pc:{col}"><summary><div class="pm-n">{i}</div><div class="pm-main">'
            f'<div class="pm-k">Posible mejora · <span class="ac-v" data-v="{v}">{ic(VERB_IC[v])}{v.capitalize()}</span> · {owner}</div><div class="pm-t">{title}</div><div class="pm-why">{why}</div>'
            f'<div class="pm-chips"><span class="qcs" style="--c:{col}">{pri}</span><span class="qcs">Configuración · Prometheo</span></div></div>'
            f'<div class="pm-cnt"><b>{cnt}</b><span>{cntl}</span></div><div class="pm-more"><span class="op">Ver prompt para Mi Prometheo</span><span class="cl">Plegar</span>{ic("chev")}</div></summary>'
            f'<div class="pm-body"><div class="mp"><div class="mp-h"><span class="mp-av">{ic("bot")}</span><div><b>Mi Prometheo</b><span>Prompt listo para pegar · revisalo antes de enviar</span></div>'
            f'<button class="mp-copy" type="button" data-copy="pt-{pid}">{ic("doc")}<span>Copiar prompt</span></button></div><div class="mp-bubble" id="pt-{pid}">{prompt}</div></div></div></details>')


groups = []
for g in ["Esta semana", "Próxima quincena", "Para decidir"]:
    cs = [c for c in CARDS if c["grp"] == g]
    wrap = "" if g == "Esta semana" else ' class="adv"'
    groups.append(f'<div{wrap}>' + sub(g, f"{len(cs)} {'acción' if len(cs) == 1 else 'acciones'}")
                  + '<div class="igrid avg ad-grid">' + "".join(action(c) for c in cs) + "</div></div>")
P["action"] = (
    head_sec("Action Driven · acciones con dueño", "Qué hacemos esta quincena,", "ordenado por impacto.",
             "Cada acción en su card: qué hacemos, quién, cuándo y con qué meta. El índice Data Driven dice cuánto se apoya en datos.",
             "Rúbrica de score v1, sin calibrar. Índices ilustrativos de la demo. En Básico se ven las tres de esta semana; en Avanzado, todas.")
    + g4(kpi("bolt", "", "calc", "Acciones de la quincena", str(len(CARDS)), bsc="3 para esta semana"),
         kpi("user", "blu", "calc", "Dueños", "4", bsc="Ventas · Marketing · Dirección · AUREA"),
         kpi("lock", "pnk", "calc", "Efecto esperado en altas", "+5 a +9", bsc="si se hacen las dos primeras"),
         kpi("gauge", "grn", "calc", "Índice Data Driven medio", f"{sum(score_of(c) for c in CARDS) / len(CARDS):.0f}%", bsc="ilustrativo · se recalcula con el export"))
    + DD_LEGEND + "".join(groups)
    + '<p class="qcm bsc">Las tres de esta semana. En <b>Avanzado</b> se ven las 7.</p>'
    + f'<div class="subsec mejora mpx"><div class="ss-h"><div class="ss-ic mpx-ic">{ic("flame")}</div><div><div class="ss-k">Subsector · Posibles mejoras</div><h2>Del hallazgo al prompt, <em>listo para pedir.</em></h2>'
    f'<span class="mpx-pill">{ic("flame")}Potenciado por <b>Mi Prometheo</b></span></div></div><div class="pm-list">' + "".join(pm(p, i + 1) for i, p in enumerate(PM)) + "</div></div>"
    + '<div class="adv mt">' + table(["Registro de calibración", "Índice al proponer", "Resultado al cierre", "Estado"],
                                    [[c["tema"], f"{score_of(c)}%", "se registra el 30/10", '<span class="fx-st pend">abierta</span>'] for c in CARDS], minw=620) + "</div>"
    + yeq("Primero la venta que ya está pedida: las 15 demos. Después, plata de pauta mejor puesta y el registro de la app, que es el freno de producto más grande de la quincena.")
)

# --- Calidad de datos
CAL = [("tipo_usuario", 92, "Panorama, Venta, Usuarios"), ("canal", 100, "Panorama, Resueltas"), ("intencion_principal", 95, "Panorama, Demanda"), ("estado_embudo", 93, "Usuarios y embudo"),
       ("sistema_operativo", 88, "Soporte técnico"), ("Smart Tags de soporte", 96, "Soporte técnico"), ("pauta_origen · Meta", 92, "Pauta y venta"), ("pauta_origen · TikTok", 71, "TikTok"),
       ("zona · propuesta", 84, "Demanda"), ("ambientes · propuesta", 63, "Demanda"), ("presupuesto de compra · propuesta", 46, "Demanda"), ("cantidad de propiedades", 58, "Venta, Criterio"),
       ("causa raíz", 31, "Criterio"), ("sentimiento", 12, "Soporte · experiencia"), ("fecha de alta (cierre)", 0, "Venta · hoy fuera del CRM")]
P["calidad"] = (
    head_sec("Calidad de datos · Data Driven", "Cada número con base, cobertura y origen.", "Lo que falta, se dibuja.",
             "Qué tan confiable es cada variable que usa el tablero.", "Escalera: Hecho 80% o más · Señal 40 a 79% · Indicio 10 a 39% · No reportable menos de 10%. Con cobertura menor a 80%, doble lectura.")
    + g4(*[kpi(i, t, "calc", l, str(sum(1 for _, v, _ in CAL if lvl_of(v) == lv)), bsc=d) for i, t, l, lv, d in [
        ("checkc", "grn", "Variables en Hecho", "Hecho", "80% o más de cobertura"), ("pulse", "blu", "Variables en Señal", "Señal", "40 a 79%: se muestran con su base"),
        ("alert", "amb", "Variables en Indicio", "Indicio", "10 a 39%: no titulan"), ("x", "", "No reportables", "No reportable", "faltantes de proceso")]])
    + table(["Variable", "Cobertura", "", "Nivel", "Dónde se usa"],
            [[f"<b>{a}</b>", f"{v}%", f'<div class="qf" style="width:140px"><div class="qh" style="width:{v}%;background:var(--vio)"></div></div>', lvl(v), w] for a, v, w in CAL], minw=620)
    + yeq("Las variables del diseño de MIA (tipo de usuario, canal, intención, etapa y sistema operativo) llegan a Hecho. Lo que falta son las propuestas nuevas de Demanda y el registro de altas dentro del CRM.")
)


def cn(icon, color, name, on, desc):
    st = '<span class="qco on"><i></i>Conectado</span>' if on else '<span class="qco off"><i></i>A conectar</span>'
    btn = f'<button class="qcc" type="button">{ic("sliders")}Configuración</button>' if on else f'<button class="qcc go" type="button">{ic("plug")}Conectar</button>'
    return (f'<div class="cn"><div class="cn-h"><span class="qcn" style="--c:{color}">{ic(icon)}</span><div><b>{name}</b>{st}</div></div>'
            f'<div class="cn-d"><p>{desc}</p></div><div class="cn-f">{btn}</div></div>')


CHN = "".join(f'<span class="qcl" style="margin:4px 4px 0 0">{ic(i)}{t}</span>' for i, t in [("wa", "WhatsApp · API"), ("mail", "Gmail"), ("ig", "Instagram"), ("fb", "Facebook"), ("play", "TikTok")])
P["integraciones"] = (
    head_sec("Integraciones · de dónde sale este tablero", "Todas las fuentes,", "en tres sectores.",
             "Qué alimenta el tablero, qué está conectado y cuándo se actualizó cada fuente.", "Cada fuente manda en lo suyo: Prometheo en charlas y calificación, cada canal en su gasto y alcance, la app en registros y publicaciones.")
    + '<div class="bridge"><div class="eq"><b>TikTok y Meta ven hasta el clic</b> × <b>Prometheo ve del clic al alta</b></div><p>El cruce por <b>ID de anuncio</b> (Meta) y por <b>código de anuncio</b> (TikTok, email y WhatsApp) es el producto.</p></div>'
    + f'<div class="cn-sec"><div class="cn-sh"><span class="cn-si">{ic("crm")}</span><div><b>CRM</b><span>Un solo CRM: todos los canales de conversación entran por Prometheo</span></div></div>'
    + f'<div class="cn-g" style="grid-template-columns:1fr"><div class="cn"><div class="cn-h"><span class="qcn" style="--c:linear-gradient(135deg,#7C5CBF,#5B8FD9)">{ic("bot")}</span><div><b>Prometheo</b><span class="qco off"><i></i>Esperando export</span></div></div>'
    + f'<div class="cn-d"><p>Conversaciones, Smart Tags, variables, calificación, resolución sin humano y escalamientos. Los cinco canales viven adentro de Prometheo:</p><div style="margin-top:8px">{CHN}</div></div>'
    + f'<div class="cn-f"><button class="qcc" type="button">{ic("sliders")}Configuración</button></div></div></div></div>'
    + f'<div class="cn-sec"><div class="cn-sh"><span class="cn-si">{ic("mega")}</span><div><b>Canales Marketing</b><span>Gasto, alcance y envíos de cada canal</span></div></div><div class="cn-g">'
    + cn("play", "var(--ink)", "TikTok Ads", False, "Gasto, distribución, video y píxel por anuncio y día.")
    + cn("ig", "linear-gradient(45deg,#C77AA8,#7C5CBF)", "Meta Ads · Instagram", False, "Inversión, alcance, clics y ubicaciones por anuncio.")
    + cn("fb", "var(--blu)", "Meta Ads · Facebook", False, "Inversión, alcance, clics y edad del público por anuncio.")
    + cn("mail", "var(--src-mail)", "Email Marketing", False, "Envíos, entregas, aperturas, clics y bajas.")
    + cn("wa", "var(--src-wpp)", "WhatsApp Marketing", False, "Difusiones, plantillas, leídos, tier y calidad.")
    + "</div></div>"
    + f'<div class="cn-sec"><div class="cn-sh"><span class="cn-si">{ic("layers")}</span><div><b>Otras integraciones</b><span>Producto, cierre y costos</span></div></div><div class="cn-g">'
    + cn("phone", "var(--vio)", "Datos de la app de MIA", False, "Descargas, registros, avisos publicados y usuarios activos.")
    + cn("ledger", "var(--src-erp)", "Registro de altas", False, "Planes pagos activados. Sin esto no hay ciclo cerrado.")
    + cn("pie", "var(--pnk)", "Panel de consumo de IA", False, "Consumo por mes, reparto y cortes de saldo.")
    + "</div></div>"
    + yeq("Faltantes declarados: export de Prometheo (todo el tablero es modelado), datos de la app, registro de altas, panel de consumo y precio real de los planes.")
)

# ================= v5: reestructura (360, canales con campaña › conjunto › anuncio, Google, evolución, histórico) =================
ALL = ADS + GADS
GG = GADS
GASTO_ALL = tot(ALL, "gasto")
CAL_ALL = tot(ALL, "calif")
ALT_ALL = tot(ALL, "altas")


def kvx(items, kc=None):
    kc = kc or len(items)
    return f'<div class="kv" style="--kc:{kc}">' + "".join(f'<div><div class="v">{v}</div><div class="k">{t}</div></div>' for v, t in items) + "</div>"


def bigsub(icon, kick, title, em, text):
    return (f'<div class="bigsub"><span class="bs-ic">{ic(icon)}</span><div><span class="bs-k">{kick}</span>'
            f'<div class="bs-t">{title} <em>{em}</em></div><p>{text}</p></div></div>')


# --- Venta · CRM con Resueltas adentro
_res = P["resueltas"]
_res = _res[_res.index('<div class="g4">'):]
P["ventacrm"] = (P["ventacrm"] + bigsub("checkc", "Subsector · dentro de Venta · CRM", "Resueltas sin contacto humano:", "1.214 charlas cerradas por el agente.",
                                       "Cuántas charlas resolvió el agente solo, en qué y por qué canal, y qué pasó al equipo.") + _res)

# --- Posibles mejoras como pestaña de CRM
PM += [
    ("pmC", "corregir", "AUREA", "var(--warn)", "Alta", "Preguntar cuántas propiedades maneja la inmobiliaria", "64 cuentas no califican porque falta el dato. La pregunta va una sola vez, en el primer bloque.", "64", "sin el dato",
     "Necesito sumar una pregunta al asistente de MIA cuando tipo_usuario es inmobiliaria o desarrolladora.\n- En el primer bloque: &quot;¿Cuántas propiedades manejás hoy?&quot;.\n- Guardar la respuesta en una variable nueva &quot;cant_propiedades&quot; (número).\n- No preguntarlo si ya está cargado.\nAntes de guardar, mostrame el sector del prompt como queda. No apliques nada hasta que te confirme con &quot;Sí, confirmar&quot;."),
    ("pmD", "separar", "AUREA", "var(--blu)", "Media", "Respuesta corta para particulares que buscan", "Los particulares consumen dos de cada tres dólares de IA y se resuelven con un link a la app.", "USD 486", "de IA en particulares",
     "Necesito ajustar el sector de ruteo del asistente de MIA.\n- Si tipo_usuario es particular e intencion_principal es buscar o alquilar, responder en hasta dos mensajes: link a la app y la MIA Tool que corresponda.\n- Cerrar con el Smart Tag &quot;Resuelto sin humano&quot;.\n- No cambiar el flujo de inmobiliarias.\nAntes de guardar, mostrame el sector como queda. No apliques nada hasta que te confirme con &quot;Sí, confirmar&quot;."),
]
P["mejoras"] = (
    head_sec("Posibles mejoras · CRM", "Del hallazgo al prompt,", "listo para pedir.",
             "Cada mejora del CRM con su prompt para Mi Prometheo: se copia, se revisa y se pega.",
             "Cada prompt pide ver el cambio antes de aplicarlo y espera la confirmación «Sí, confirmar». Nada se aplica solo.")
    + g4(kpi("bolt", "", "calc", "Mejoras propuestas", str(len(PM)), bsc="todas con prompt listo"),
         kpi("flame", "pnk", "calc", "Urgentes", "1", bsc="aviso de demo a Ventas"),
         kpi("bot", "blu", "pro", "Se aplican en", "Mi Prometheo", bsc="con confirmación antes de guardar"),
         kpi("shield", "grn", "calc", "Con guardiana", f"{len(PM)} de {len(PM)}", bsc="cada cambio se mide después"))
    + f'<div class="subsec mejora mpx"><div class="ss-h"><div class="ss-ic mpx-ic">{ic("flame")}</div><div><div class="ss-k">Posibles mejoras</div><h2>Lo que conviene cambiar <em>en el CRM esta quincena.</em></h2>'
    f'<span class="mpx-pill">{ic("flame")}Potenciado por <b>Mi Prometheo</b></span></div></div><div class="pm-list">' + "".join(pm(p, i + 1) for i, p in enumerate(PM)) + "</div></div>"
    + yeq("Primero el aviso de demo a Ventas: es plata que ya está pedida. Después los dos ajustes del agente, que cuidan la calificación y el costo.")
)
_a = P["action"]
_i = _a.index('<div class="subsec mejora mpx">')
_j = _a.index('<div class="adv mt">', _i)
P["action"] = _a[:_i] + f'<div class="go-mej">{ic("flame")}<span>Los prompts listos para aplicar estas acciones están en <b>CRM · Posibles mejoras</b>.</span></div>' + _a[_j:]

# --- Usuarios: el cuadro de la derecha, explicado
ETAPA_INT = [("1", "No descargó la app", 520, "Buscar o alquilar", 388, "Llegan desde redes buscando una propiedad. El agente los manda a descargar la app."),
             ("2", "Descargó, sin registro", 298, "Publicar", 164, "Quieren publicar y se trabaron en el registro. Es el freno de producto de Soporte técnico."),
             ("3", "Registrado", 412, "Vender", 112, "Ya tienen cuenta y quieren vender: el agente los guía a cargar su primer aviso."),
             ("4", "Publicó un aviso", 236, "Planes", 96, "Inmobiliarias con avisos que preguntan por un plan pago: oportunidad comercial."),
             ("5", "Usuario activo", 254, "Soporte técnico", 171, "Usan MIA todos los días y escriben por un problema: cuidarlos es retención.")]
etapa_rows = "".join(
    f'<div class="et-r"><span class="et-n">{n_}</span><div class="et-m"><div class="et-t"><span>{et}</span><b>{v} charlas</b></div>'
    f'<div class="et-i"><em>Lo que más quiere</em><b>{it}</b><span>{iv} de {v} · {pc(iv, v)}</span></div>'
    f'<div class="zb"><i style="width:{100 * iv / v:.0f}%"></i></div><p>{tx}</p></div></div>' for n_, et, v, it, iv, tx in ETAPA_INT)
P["usuarios"] = (
    head_sec("Usuarios y embudo · estado_embudo", "En qué etapa está cada persona", "cuando le escribe a MIA.",
             "Muestra si el problema es de marketing (no descargan) o de producto (descargan y no se registran).",
             "Variable estado_embudo, cargada por el agente en cada conversación. Lo que pasó después de la charla sale de los datos de la app.")
    + g4(kpi("phone", "", "pro", "No descargaron la app", "520", "+12%", flat=True, bsc="28% de las charlas · problema de llegada"),
         kpi("x", "amb", "pro", "Descargaron y no se registraron", "298", "+19%", up=False, bsc="16% · fricción en el registro"),
         kpi("home", "blu", "pro", "Publicaron un aviso", "236", "+6%", bsc="13% · ya son oferta en MIA"),
         kpi("users", "grn", "pro", "Usuarios activos", "254", "+4%", bsc="14% · escriben por soporte o mejoras"))
    + sub("La etapa al escribir y qué quiere cada una")
    + '<div class="g2">'
    + bars("Estado en el embudo", "pro", EMBUDO, "Base: 1.720 con etapa identificada (93%) · Hecho.", icon="route")
    + f'<div class="qx"><div class="qw">{ic("target")}Qué quiere cada etapa{src("pro")}<span class="r">estado_embudo × intencion_principal</span></div>{etapa_rows}</div>'
    + "</div>"
    + sub("Qué pasó después de la charla", "cruce con los datos de la app")
    + '<div class="g3">'
    + stat("phone", "Descargaron la app", "app", "212", "de 520", "Personas que no tenían la app y la descargaron en los 7 días siguientes a la charla.", [("41%", "conversión"), ("WhatsApp", "canal que más convierte")])
    + stat("user", "Se registraron", "app", "412", "", "Registros nuevos después de una charla: descargas nuevas más los que ya tenían la app.", [("138", "de los 298 trabados"), ("46%", "destrabados")], tone="var(--blu)")
    + stat("home", "Publicaron su primer aviso", "app", "94", "", "Particulares e inmobiliarias que publicaron dentro de los 7 días.", [("61", "particulares"), ("33", "inmobiliarias")], tone="var(--pnk)")
    + "</div>"
    + '<div class="adv mt">' + table(["Tipo de usuario", "Conversaciones", "No descargó", "Sin registro", "Registrado", "Publicó", "Activo"],
                                    [["Particular", "1.214", 402, 236, 288, 128, 160], ["Inmobiliaria", 318, 52, 31, 72, 88, 75], ["Inversor", 122, 48, 20, 34, 6, 14], ["Desarrolladora", 46, 6, 4, 10, 14, 5]], minw=720) + "</div>"
    + yeq("298 personas descargaron la app y se trabaron antes de registrarse: es el mismo problema que muestra Soporte técnico en Acceso y cuenta. Arreglar el registro suma usuarios sin gastar más en pauta.")
)


# --- tarjeta de anuncio sin repetir el canal
def adcard2(a):
    return adcard(a).replace(f'{a["canal"]} · {a["fmt"]} <code>', f'{a["fmt"]} <code>')


def chsec(name, rows):
    icon, col, soft = CH[name]
    g = tot(rows, "gasto")
    return (f'<div class="chsec" style="--cc:{col};--cs:{soft}"><div class="chsec-h"><span class="chsec-ic">{ic(icon)}</span><div class="chsec-t"><b>{name}{" Ads" if name == "Google" else ""}</b>'
            f'<span>{len(rows)} anuncios · inversión {ars(g)}</span></div>'
            + kvx([(tot(rows, "conv"), "charlas"), (tot(rows, "calif"), "calificadas"), (tot(rows, "altas"), "altas"), (ars(g / max(1, tot(rows, "calif"))), "por calificada")])
            + f'</div><div class="chsec-sub"><span>{ic("anun")}Anuncios del canal</span></div><div class="adg">{"".join(adcard2(a) for a in rows)}</div></div>')


def ch_mini(name, rows):
    icon, col, soft = CH[name]
    g = tot(rows, "gasto")
    return (f'<div class="chs" style="--cc:{col};--cs:{soft}"><div class="chs-h"><span class="chs-ic">{ic(icon)}</span><div><b>{name}{" Ads" if name == "Google" else ""}</b><span>{len(rows)} anuncios · {ars(g)}</span></div></div>'
            + kvx([(tot(rows, "conv"), "charlas"), (tot(rows, "calif"), "calificadas"), (tot(rows, "altas"), "altas"), (ars(g / max(1, tot(rows, "calif"))), "por calificada")], 2) + "</div>")


P["pauta"] = (
    head_sec("Visión 360 · todos los canales, una sola venta", "TikTok, Meta y Google ven el clic.", "Prometheo ve qué pasó después.",
             "Cada anuncio de cada red, medido por lo que importa: cuántas inmobiliarias califican y cuántas se dan de alta.",
             "Cruce por ID de anuncio (Meta, Click to WhatsApp), por GCLID o UTM (Google) y por código en el mensaje prellenado (TikTok). El gasto es de cada plataforma; el conteo de charlas es de Prometheo. Nunca se suman.")
    + '<div class="bridge"><div class="eq"><b>Las redes ven hasta el clic</b> × <b>Prometheo ve del clic al alta</b></div><p>Cada peso de pauta se juzga por la inmobiliaria calificada y el alta que trajo.</p></div>'
    + g4(kpi("dollar", "grn", "calc", "Inversión de la quincena", ars(GASTO_ALL), "+11%", flat=True, bsc="TikTok + Instagram + Facebook + Google"),
         kpi("chat", "blu", "pro", "Charlas desde anuncios", n(tot(ALL, "conv")), "+14%", bsc=f"{pc(tot(ALL, 'conv'), CONV)} de las conversaciones"),
         kpi("checkc", "", "pro", "Calificadas desde anuncios", str(CAL_ALL), "+12%", bsc=f"{ars(GASTO_ALL / CAL_ALL)} por calificada"),
         kpi("lock", "pnk", "erp", "Altas desde anuncios", str(ALT_ALL), "+5", bsc=f"{ars(GASTO_ALL / ALT_ALL)} por alta"))
    + sub("Las cuatro redes de un vistazo")
    + '<div class="g4">' + "".join(ch_mini(nm, rw) for nm, rw in [("TikTok", TT), ("Instagram", IG), ("Facebook", FB), ("Google", GG)]) + "</div>"
    + sub("Red por red")
    + "".join(chsec(nm, rw) for nm, rw in [("TikTok", TT), ("Instagram", IG), ("Facebook", FB), ("Google", GG)])
    + '<div class="adv">' + sub("Tabla completa") + ads_table(ALL)
    + '<p class="qcm">IC 95% = intervalo de Wilson de la tasa de calificación. <b>n&lt;30</b> = muestra chica, no comparar. Registros: cruce con los datos de la app.</p></div>'
    + yeq("Los anuncios que hablan con inmobiliarias son los que venden, en las cuatro redes. Los que hablan con personas que buscan traen descargas y registros, no altas: se miden con otra vara.")
)


# --- cuadro principal por canal: campaña › conjunto › anuncio
def camp_tree(rows, lvl2="Conjunto de anuncios", lvl3="Anuncio"):
    camps = []
    for a in rows:
        if a["camp"] not in camps:
            camps.append(a["camp"])
    total_alt = max(1, tot(rows, "altas"))
    out = []
    for c in camps:
        cr = [a for a in rows if a["camp"] == c]
        conjs = []
        for a in cr:
            if a["conj"] not in conjs:
                conjs.append(a["conj"])
        inner = ""
        for j in conjs:
            jr = [a for a in cr if a["conj"] == j]
            ads_html = "".join(
                f'<div class="tr-ad"><span class="tr-ic">{ic("search" if a["canal"] == "Google" else "anun")}</span><div class="tr-n"><b>{a["nombre"]}</b><span>{a.get("kw", a["fmt"])} · <code>{a["id"]}</code></span></div>'
                f'<div class="tr-m"><span><b>{a["conv"]}</b>charlas</span><span><b>{a["calif"]}</b>calificadas</span><span><b>{ars(a["gasto"] / a["calif"]) if a["calif"] else "–"}</b>por calificada</span>'
                f'<span class="tr-alt"><b>{a["altas"]}</b>altas · {pc(a["altas"], total_alt)}</span></div></div>' for a in jr)
            inner += (f'<div class="tr-conj"><div class="tr-ch"><span class="tr-lv">{ic("users")}{lvl2}</span><b>{j}</b><span class="tr-s">{tot(jr, "calif")} calificadas · {tot(jr, "altas")} altas</span></div>{ads_html}</div>')
        out.append(f'<div class="tr-camp"><div class="tr-chd"><span class="tr-cic">{ic("camp")}</span><div><span class="tr-lv">Campaña</span><b>{c}</b></div>'
                   + kvx([(ars(tot(cr, "gasto")), "inversión"), (tot(cr, "conv"), "charlas"), (tot(cr, "calif"), "calificadas"), (tot(cr, "altas"), "altas")])
                   + f'</div>{inner}</div>')
    hier = (f'<div class="hier2"><div><span class="tr-cic">{ic("camp")}</span><b>Campaña</b><span>Define el objetivo: descargas o inmobiliarias.</span></div>'
            f'<div><span class="tr-cic">{ic("users")}</span><b>{lvl2}</b><span>Define a quién se le muestra y con qué presupuesto.</span></div>'
            f'<div><span class="tr-cic">{ic("search" if lvl3 == "Palabra clave" else "anun")}</span><b>{lvl3}</b><span>{"Lo que la persona buscó en Google." if lvl3 == "Palabra clave" else "Lo que se ve: video, imagen o carrusel."}</span></div></div>')
    return hier + '<div class="tree">' + "".join(out) + "</div>"


def camp_cards(rows):
    camps = []
    for a in rows:
        if a["camp"] not in camps:
            camps.append(a["camp"])
    cards = []
    for c in camps:
        cr = [a for a in rows if a["camp"] == c]
        cards.append(f'<div class="qx qcg" style="--ct:var(--vio)"><div class="qw">{ic("camp")}{c}<span class="r">{len(set(a["conj"] for a in cr))} conjuntos · {len(cr)} anuncios</span></div>'
                     f'<div class="qy" style="font-size:26px">{tot(cr, "altas")} <small class="u">altas</small></div><div class="qz">{tot(cr, "conv")} charlas · {ars(tot(cr, "gasto"))} invertidos</div>'
                     + kvx([(pc(tot(cr, "calif"), max(1, tot(cr, "b2b"))), "califica"), (ars(tot(cr, "gasto") / max(1, tot(cr, "calif"))), "por calificada"), (tot(cr, "reg"), "registros")]) + "</div>")
    k = len(cards)
    return f'<div class="g{3 if k >= 3 else 2}">' + "".join(cards) + "</div>"


def channel_core(name, rows, src_k, lvl2="Conjunto de anuncios", lvl3="Anuncio"):
    return (sub("1 · Del anuncio al alta", "la red ve hasta el clic, Prometheo todo lo que sigue")
            + steps("Del anuncio al alta", f"base: {n(tot(rows, 'imp'))} impresiones",
                    [("Impresiones", tot(rows, "imp"), "veces que se vio"), ("Clics", tot(rows, "clics"), "al destino"), ("Charlas", tot(rows, "conv"), "en Prometheo"),
                     ("Cuentas comerciales", tot(rows, "b2b"), "inmobiliarias y desarrolladoras"), ("Calificadas", tot(rows, "calif"), "lectura amplia"),
                     ("Demos", tot(rows, "demos"), "pedidas", "leak"), ("Altas", tot(rows, "altas"), "plan pago")])
            + sub("2 · Por campaña · lo que pasó después del clic")
            + camp_cards(rows)
            + sub(f"3 · Campaña › {lvl2.lower()} › {lvl3.lower()} · cómo impacta en las altas", "% de altas = participación en las altas del canal")
            + camp_tree(rows, lvl2, lvl3))


_tt = P["tiktok"]
_k = _tt.index('<div class="qo"><div class="qr"><span class="qv"></span>1 · Distribución y costo')
P["tiktok"] = _tt[:_k] + channel_core("TikTok", TT, "tt") + sub("4 · Las métricas de TikTok, en su orden") + _tt[_k:].replace("1 · Distribución y costo", "4.1 · Distribución y costo").replace("2 · Interacción", "4.2 · Interacción").replace("3 · Reproducción", "4.3 · Reproducción").replace("4 · Conversión · píxel", "4.4 · Conversión · píxel")


def meta_tab2(name, rows, edad, lectura):
    icon, col, soft = CH[name]
    g = tot(rows, "gasto")
    plc = {}
    for a in rows:
        plc[a["ubic"]] = plc.get(a["ubic"], 0) + a["imp"]
    return (
        chan_head(icon, name, "Meta Ads · Canales Marketing",
                  f"El cruce de cada campaña, conjunto y anuncio de {name} con Prometheo: qué pasó con cada clic hasta el alta.",
                  "Meta manda en inversión, alcance, impresiones y clics; Prometheo manda en cuántas charlas hubo y qué pasó con ellas. CTR = clics ÷ impresiones · CPC = costo por clic · CPM = costo cada mil impresiones.")
        + srclegend((["meta"], "Inversión, alcance, impresiones, clics y ubicaciones."), (["pro"], "Charlas, calificación, demos y altas."), (["calc"], "Costo por calificada y por alta."))
        + g4(kpi("dollar", "grn", "meta", "Inversión", ars(g), "+6%", flat=True, bsc=f"{len(rows)} anuncios · CPM {ars(g / tot(rows, 'imp') * 1000)}"),
             kpi("eye", "blu", "meta", "Alcance", n(tot(rows, "alc")), "+8%", bsc=f"CTR {pc(tot(rows, 'clics'), tot(rows, 'imp'), 2)} · CPC {ars(g / tot(rows, 'clics'))}"),
             kpi("checkc", "", "pro", "Calificadas", str(tot(rows, "calif")), "+12%", bsc=f"{pc(tot(rows, 'calif'), tot(rows, 'b2b'))} de las cuentas comerciales"),
             kpi("lock", "pnk", "erp", "Altas", str(tot(rows, "altas")), "+2", bsc=f"{ars(g / max(1, tot(rows, 'altas')))} por alta"))
        + channel_core(name, rows, "meta")
        + sub("4 · Anuncio por anuncio")
        + '<div class="adg">' + "".join(adcard2(a) for a in rows) + "</div>"
        + sub("5 · Dónde se vio y a quién llegó")
        + '<div class="g2">'
        + bars("Ubicación", "meta", [(k, v, n(v), pc(v, tot(rows, "imp"))) for k, v in sorted(plc.items(), key=lambda x: -x[1])], "Impresiones por ubicación principal de cada anuncio.", color=col, icon="layers")
        + bars("Edad del público alcanzado", "meta", edad, "Distribución de alcance que informa Meta.", color=col, icon="users")
        + "</div>"
        + '<div class="adv mt">' + ads_table(rows) + "</div>"
        + yeq(lectura))


P["instagram"] = meta_tab2("Instagram", IG, [("18 a 24", 8, "", "8%"), ("25 a 34", 38, "", "38%"), ("35 a 44", 31, "", "31%"), ("45 a 54", 18, "", "18%"), ("55 o más", 5, "", "5%")],
                           "La campaña «Inmobiliarias · Demo» trae 10 de las 11 altas de Instagram: el retargeting y el lookalike de altas califican mejor que cualquier público frío. «Amoblá tu propiedad con IA» atrae a quien busca: pasa a la pauta de descarga.")
P["facebook"] = meta_tab2("Facebook", FB, [("18 a 24", 4, "", "4%"), ("25 a 34", 18, "", "18%"), ("35 a 44", 34, "", "34%"), ("45 a 54", 29, "", "29%"), ("55 o más", 15, "", "15%")],
                          "Facebook llega a un público mayor, más propietario y más de campo. «Bolsa de pedidos» trae las 2 altas con poco gasto; «Vendé sin intermediarios» trae particulares y ninguna alta.")

# --- Google Ads
gg_g = tot(GG, "gasto")
P["google"] = (
    chan_head("google", "Google Ads", "Canales Marketing",
              "Quien busca en Google ya tiene la intención. Arriba, el cruce Google × Prometheo; abajo, el export. TikTok y Meta generan el interés; Google lo capta cuando alguien escribe «portal para inmobiliarias».",
              "Jerarquía de Google: campaña › grupo de anuncios › palabra clave. Cruce por GCLID y UTM en el link a WhatsApp o al formulario. CTR = clics ÷ impresiones · CPC = costo por clic.")
    + srclegend((["calc"], "Google: costo, impresiones, clics, CTR, CPC y conversiones."), (["pro"], "De la conversión a la cuenta calificada, la demo y el alta."), (["erp"], "Altas por cruce con el registro."))
    + g4(kpi("dollar", "grn", "calc", "Inversión", ars(gg_g), "nueva", flat=True, bsc="4 grupos de búsqueda · primera quincena completa"),
         kpi("search", "blu", "calc", "Clics", n(tot(GG, "clics")), bsc=f"CTR {pc(tot(GG, 'clics'), tot(GG, 'imp'), 1)} · CPC {ars(gg_g / tot(GG, 'clics'))}"),
         kpi("checkc", "", "pro", "Calificadas", str(tot(GG, "calif")), bsc=f"{pc(tot(GG, 'calif'), tot(GG, 'b2b'))} de las cuentas comerciales"),
         kpi("lock", "pnk", "erp", "Altas", str(tot(GG, "altas")), bsc=f"{ars(gg_g / tot(GG, 'altas'))} por alta"))
    + channel_core("Google", GG, "calc", "Grupo de anuncios", "Palabra clave")
    + sub("4 · Palabras clave · lo que la gente escribió")
    + '<div class="g2">'
    + bars("Búsquedas con más charlas", "calc", [(a["kw"].split(",")[0].strip("«» "), a["conv"], str(a["conv"]), a["fmt"].split("· ")[1]) for a in sorted(GG, key=lambda x: -x["conv"])], "Concordancia: exacta, frase o amplia.", icon="search")
    + bars("Palabras negativas sugeridas", "calc", [("gratis", 41), ("dueño directo sin comisión", 28), ("temporario", 19), ("tasación", 12)], "Charlas que trajo la concordancia amplia y no eran demanda: se excluyen.", color="var(--warn)", icon="filter")
    + "</div>"
    + '<div class="adv mt">' + sub("Acciones de conversión · cómo entra cada consulta")
    + table(["Acción de conversión", "Tipo", "Charlas", "Cómo entra a Prometheo"],
            [["Clic para chatear por WhatsApp", "Mensaje", 168, "Directo: charla con el agente"], ["Formulario «Quiero publicar»", "Formulario", 79, "Directo: con tipo_usuario ya cargado"], ["Descarga de la app", "App", 36, "No entra: se cruza con los datos de la app"]], minw=640)
    + '<p class="qcm">Las descargas desde Google no generan charla: se miden en la app, no en Prometheo.</p>' + ads_table(GG) + "</div>"
    + yeq("Las búsquedas de inmobiliarias («portal para inmobiliarias», «alternativa a Zonaprop») traen 3 de las 4 altas de Google. La búsqueda de alquiler trae descargas, no ventas: necesita palabras negativas antes de subir presupuesto.")
)

# --- Evolución: conversaciones, calificadas y % en un mismo gráfico; por canal; todo; histórico
WEEKS6 = WEEKS


def combo(bars_series, line=None, labels=WEEKS6, right_fmt=pct, right_max=None):
    top = max(max(s[1]) for s in bars_series) * 1.15
    nb = len(bars_series)
    out = []
    for k in range(5):
        y = 206 - k * 46.5
        out.append(f'<line class="gl" x1="50" x2="950" y1="{y:.1f}" y2="{y:.1f}"/><text x="44" y="{y + 3:.1f}" text-anchor="end">{n(top * k / 4)}</text>')
        if line:
            out.append(f'<text x="958" y="{y + 3:.1f}" text-anchor="start">{right_fmt((right_max or max(line[1]) * 1.15) * k / 4)}</text>')
    step = 900 / len(labels)
    for i, lab in enumerate(labels):
        gw = step * .7
        bw = gw / nb
        for j, (nm, vals, col) in enumerate(bars_series):
            h = vals[i] / top * 186
            x = 50 + i * step + step * .15 + j * bw
            out.append(f'<rect x="{x:.1f}" y="{206 - h:.1f}" width="{bw - 3:.1f}" height="{h:.1f}" rx="3" fill="{col}"/>')
        out.append(f'<text x="{50 + i * step + step / 2:.1f}" y="224" text-anchor="middle">{lab}</text>')
    if line:
        nm, vals, col = line
        rm = right_max or max(vals) * 1.15
        pts = [(50 + i * step + step / 2, 206 - v / rm * 186) for i, v in enumerate(vals)]
        out.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round"/>')
        out += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="#fff" stroke="{col}" stroke-width="2.5"/>' for x, y in pts]
        out.append(f'<text class="lbl" x="{pts[-1][0]:.1f}" y="{pts[-1][1] - 10:.1f}" text-anchor="middle">{right_fmt(vals[-1])}</text>')
    leg = "".join(f'<span><i style="background:{c}"></i>{nm}</span>' for nm, _, c in bars_series) + (f'<span><i style="background:{line[2]};height:3px;border-radius:2px"></i>{line[0]} · eje derecho</span>' if line else "")
    return f'<svg class="chart" viewBox="0 0 1000 230" role="img" preserveAspectRatio="xMidYMid meet">{"".join(out)}</svg><div class="chart-lg">{leg}</div>'


def stacked(series, labels=WEEKS6):
    totals = [sum(s[1][i] for s in series) for i in range(len(labels))]
    top = max(totals) * 1.15
    out = []
    for k in range(5):
        y = 206 - k * 46.5
        out.append(f'<line class="gl" x1="50" x2="992" y1="{y:.1f}" y2="{y:.1f}"/><text x="44" y="{y + 3:.1f}" text-anchor="end">{top * k / 4:.0f}</text>')
    step = 942 / len(labels)
    for i, lab in enumerate(labels):
        y0 = 206
        x = 50 + i * step + step * .2
        w = step * .6
        for nm, vals, col in series:
            h = vals[i] / top * 186
            out.append(f'<rect x="{x:.1f}" y="{y0 - h:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{col}"/>')
            y0 -= h
        out.append(f'<text x="{x + w / 2:.1f}" y="224" text-anchor="middle">{lab}</text><text class="lbl" x="{x + w / 2:.1f}" y="{y0 - 5:.1f}" text-anchor="middle">{totals[i]}</text>')
    leg = "".join(f'<span><i style="background:{c}"></i>{nm}</span>' for nm, _, c in series)
    return f'<svg class="chart" viewBox="0 0 1000 230" role="img" preserveAspectRatio="xMidYMid meet">{"".join(out)}</svg><div class="chart-lg">{leg}</div>'


CHC = [("TikTok", [1, 1, 2, 2, 2, 4], "#7C5CBF"), ("Instagram", [2, 2, 3, 4, 5, 6], "#C77AA8"), ("Facebook", [0, 1, 1, 1, 1, 1], "#5B8FD9"),
       ("Google Ads", [0, 0, 1, 2, 2, 2], "#9C7FD6"), ("Email", [1, 1, 1, 1, 1, 1], "#B4649B"), ("WhatsApp", [1, 2, 2, 2, 1, 1], "#1F9E7E")]
EV_CONV2, EV_CAL2, EV_PCT2, EV_ALT2 = EV_CONV, EV_CAL, EV_PCT, [sum(c[1][i] for c in CHC) for i in range(6)]
MESES26 = [("Enero", 2410, 214, 18, 51, 980), ("Febrero", 2380, 221, 19, 52, 1040), ("Marzo", 2690, 248, 24, 55, 1120), ("Abril", 2820, 262, 26, 56, 1180),
           ("Mayo", 2950, 271, 27, 58, 1230), ("Junio", 3010, 279, 29, 58, 1260), ("Julio", 3120, 286, 31, 59, 1310), ("Agosto", 3180, 291, 33, 60, 1380),
           ("Septiembre", 3286, 300, 34, 61, 1420), ("Octubre · 1 al 15", 1840, 176, 27, 66, 736)]
TRIM26 = [("Primer trimestre", MESES26[0:3]), ("Segundo trimestre", MESES26[3:6]), ("Tercer trimestre", MESES26[6:9]), ("Cuarto trimestre · en curso", MESES26[9:])]
Q25 = [("Primer trimestre 2025", 4120, 296, 14, 41, 1650), ("Segundo trimestre 2025", 5030, 389, 22, 44, 2040), ("Tercer trimestre 2025", 5980, 471, 31, 47, 2430), ("Cuarto trimestre 2025", 6620, 548, 39, 49, 2760)]


def mrow(r):
    return [f"<b>{r[0]}</b>", n(r[1]), r[2], r[3], f"{r[4]}%", f"USD {n(r[5])}"]


HCOLS = ["Período", "Conversaciones", "Calificadas", "Altas", "% resueltas sin humano", "Tokens de IA"]
hist26 = "".join(
    f'<details class="hq"{" open" if "cuarto" in t.lower() else ""}><summary><b>{t}</b><span>{n(sum(m[1] for m in ms))} conversaciones · {sum(m[2] for m in ms)} calificadas · {sum(m[3] for m in ms)} altas</span>{ic("chev")}</summary>'
    + table(HCOLS, [mrow(m) for m in ms], minw=720) + "</details>" for t, ms in TRIM26)
hist25 = table(HCOLS, [mrow(q) for q in Q25], ["Total 2025", n(sum(q[1] for q in Q25)), sum(q[2] for q in Q25), sum(q[3] for q in Q25), "45%", f"USD {n(sum(q[5] for q in Q25))}"], minw=720)
P["evolucion"] = (
    head_sec("Evolución · semana a semana y mes a mes", "Cómo viene MIA,", "en un solo lugar.",
             "Conversaciones, calificadas y su porcentaje en un mismo gráfico; las altas por canal; y el histórico de 2025 y 2026.",
             "Seis tramos semanales: dos quincenas anteriores y la actual (en color pleno). El histórico abre por trimestre y mes; 2025 va resumido por trimestre.")
    + g4(kpi("chat", "blu", "pro", "Conversaciones · quincena", "1.840", "+7,9%", bsc="1.706 · 1.580 las dos anteriores"),
         kpi("checkc", "", "calc", "Calificadas · lectura amplia", str(CAL_AMP), "+11%", bsc="158 · 142 las dos anteriores"),
         kpi("lock", "pnk", "erp", "Altas", str(ALTAS), "+23%", bsc="22 · 12 las dos anteriores"),
         kpi("pulse", "grn", "calc", "% de calificación", f"{EV_PCT[-1]}%", "+2 p.p.", bsc="calificadas ÷ cuentas comerciales"))
    + '<div class="segt"><label for="ev2-a">' + ic("chat") + 'Conversaciones y calificación</label><label for="ev2-b">' + ic("mega") + 'Altas por canal</label><label for="ev2-c">' + ic("grid") + 'Todo</label></div>'
    + '<div class="evtab ev-a"><div class="qcf pad"><div class="qw">' + ic("chat") + 'Conversaciones, calificadas y % de calificación' + src("pro") + '<span class="r">por semana</span></div>'
    + combo([("Conversaciones", EV_CONV2, "#5B8FD9"), ("Calificadas", [v * 6 for v in EV_CAL2], "#7C5CBF")], ("% de calificación", EV_PCT2, "#C77AA8"), right_max=60)
    + '<p class="qcm">Las calificadas se dibujan ×6 para que se vean al lado de las conversaciones; el valor real está en la tabla del histórico.</p></div></div>'
    + '<div class="evtab ev-b"><div class="qcf pad"><div class="qw">' + ic("lock") + 'Altas por canal de marketing' + src("erp") + '<span class="r">por semana · total arriba de cada barra</span></div>'
    + stacked(CHC) + '<p class="qcm">Instagram explica la mitad de la suba: la campaña «Inmobiliarias · Demo» empezó en S3 sep. Google suma desde su primera semana.</p></div></div>'
    + '<div class="evtab ev-c"><div class="qcf pad"><div class="qw">' + ic("grid") + 'Todo el embudo · conversaciones, calificadas y altas' + src("calc") + '<span class="r">por semana</span></div>'
    + combo([("Conversaciones", EV_CONV2, "#5B8FD9"), ("Calificadas ×6", [v * 6 for v in EV_CAL2], "#7C5CBF")], ("Altas", EV_ALT2, "#C77AA8"), right_fmt=lambda v: f"{v:.0f}", right_max=20)
    + "</div></div>"
    + sub("Histórico", "2026 por trimestre y mes · 2025 resumido")
    + '<div class="segt"><label for="h-26">' + ic("cal") + '2026</label><label for="h-25">' + ic("ledger") + '2025 · resumido</label></div>'
    + f'<div class="htab h26">{hist26}</div><div class="htab h25">{hist25}<p class="qcm">2025 se muestra por trimestre. El detalle mensual está en el export de Prometheo.</p></div>'
    + yeq("Las conversaciones y las calificadas crecen todas las semanas y la calificación pasó de 42% a 49%. Las altas siguen a Instagram y a Google: son los canales que hablan con inmobiliarias.")
)

# --- Consumo de tokens: histórico en cada vista
LAB_H = ["T1 25", "T2 25", "T3 25", "T4 25", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct*"]


def hbar(vals, color, fmt, nq=4):
    top = max(vals) * 1.15
    out = []
    for k in range(5):
        y = 206 - k * 46.5
        out.append(f'<line class="gl" x1="60" x2="992" y1="{y:.1f}" y2="{y:.1f}"/><text x="54" y="{y + 3:.1f}" text-anchor="end">{fmt(top * k / 4)}</text>')
    step = 932 / len(vals)
    for i, v in enumerate(vals):
        h = v / top * 186
        x = 60 + i * step + step * .18
        w = step * .64
        out.append(f'<rect x="{x:.1f}" y="{206 - h:.1f}" width="{w:.1f}" height="{h:.1f}" rx="3" fill="{color}" opacity="{.4 if i < nq else 1}"/><text x="{x + w / 2:.1f}" y="224" text-anchor="middle">{LAB_H[i]}</text>')
    out.append(f'<line x1="{60 + nq * step:.1f}" x2="{60 + nq * step:.1f}" y1="14" y2="210" stroke="var(--line)" stroke-dasharray="4 4"/>')
    return f'<svg class="chart" viewBox="0 0 1000 230" role="img" preserveAspectRatio="xMidYMid meet">{"".join(out)}</svg>'


IA_H = [550, 680, 810, 920, 980, 1040, 1120, 1180, 1230, 1260, 1310, 1380, 1420, 1490]
META_H = [60000, 75000, 90000, 110000, 120000, 98000, 160000, 140000, 175000, 150000, 190000, 210000, 230000, 320000]
TOT_H = [v + 149 for v in IA_H]


def hist_card(title, s, vals, color, fmt, note):
    return (f'<div class="qcf pad mt"><div class="qw">{ic("cal")}{title}{src(s)}<span class="r">2025 · promedio mensual por trimestre | 2026 · por mes</span></div>'
            f'{hbar(vals, color, fmt)}<div class="chart-lg"><span><i style="background:{color};opacity:.4"></i>2025 resumido</span><span><i style="background:{color}"></i>2026</span><span>* octubre proyectado con la primera quincena</span></div><p class="qcm">{note}</p></div>')


usd = lambda v: f"USD {n(v)}"
_tk = P["tokens"]
_tk = _tk.replace('</div><div class="cstab cs-meta">', hist_card("Histórico · Prometheo (suscripción + tokens de IA)", "calc", TOT_H, "#7C5CBF", usd, "En dólares. Meta va aparte, en pesos: nunca se suman.") + '</div><div class="cstab cs-meta">', 1)
_tk = _tk.replace('</div><div class="cstab cs-ia">', hist_card("Histórico · mensajes de Meta", "calc", META_H, "#C77AA8", lambda v: "$" + n(v / 1000) + " mil", "En pesos. Desde el 1/10/2026 Meta cobra también el servicio, con 1.000 mensajes gratis por mes.") + '</div><div class="cstab cs-ia">', 1)
_ix = _tk.rindex('</div><div class="yeq">')
_tk = _tk[:_ix] + hist_card("Histórico · tokens de IA", "calc", IA_H, "#5B8FD9", usd, "El costo por charla bajó de USD 0,44 a USD 0,40 en el año: más charlas resueltas en menos mensajes.") + _tk[_ix:]
P["tokens"] = _tk

# --- integraciones: Google
P["integraciones"] = P["integraciones"].replace(cn("fb", "var(--blu)", "Meta Ads · Facebook", False, "Inversión, alcance, clics y edad del público por anuncio."),
                                                cn("fb", "var(--blu)", "Meta Ads · Facebook", False, "Inversión, alcance, clics y edad del público por anuncio.")
                                                + cn("google", "linear-gradient(135deg,#5B8FD9,#7C5CBF)", "Google Ads", False, "Costo, clics, palabras clave y conversiones por campaña."))


# ---------- navegación ----------
NAV = [
    ("Resumen", None, [("panorama", "grid", "Panorama"), ("evolucion", "trend", "Evolución"), ("action", "bolt", "Action Driven")]),
    ("CRM", "crm", [("ventacrm", "building", "Venta · CRM"), ("usuarios", "route", "Usuarios y embudo"), ("soporte", "wrench", "Soporte técnico"),
                    ("demanda", "pin", "Demanda"), ("criterio", "compass", "Criterio comercial"), ("mejoras", "flame", "Posibles mejoras"),
                    ("audiencias", "users", "Audiencias"), ("tokens", "bolt", "Consumo de Tokens - CRM")]),
    ("Marketing", "mega", [("pauta", "globe", "Visión 360"), ("tiktok", "play", "TikTok Ads", "var(--vio)"), ("instagram", "ig", "Instagram", "var(--pnk)"),
                           ("facebook", "fb", "Facebook", "var(--blu)"), ("google", "google", "Google Ads", "#9C7FD6"), ("email", "mail", "Email Marketing", "var(--src-mail)"), ("wamkt", "wa", "WhatsApp Marketing", "var(--src-wpp)")]),
    ("De dónde sale esto", None, [("calidad", "shield", "Calidad de datos"), ("integraciones", "plug", "Integraciones")]),
]
ids = [t[0] for _, _, items in NAV for t in items]


def navlabel(t):
    dot = f'<span class="chch" style="background:{t[3]}"></span>' if len(t) > 3 else ""
    return f'<label class="nav" data-t="{t[0]}" for="dn-{t[0]}">{ic(t[1])}{t[2]}{dot}</label>'


side = [f'<aside class="side"><div class="brand2"><img src="{logo}" alt="AUREA Hub"><span>Inteligencia<br>Comercial</span></div>']
for name, icon, items in NAV:
    labels = "".join(navlabel(t) for t in items)
    if icon:
        side.append(f'<details class="ngrp" open><summary><span class="ng-ic">{ic(icon)}</span><span class="ng-t">{name}</span>{ic("chev")}</summary><div class="ng-b">{labels}</div></details>')
    else:
        side.append(f'<div class="navlab">{name}</div>{labels}')
side.append('<div class="side-foot"><button class="themebtn" type="button" onclick="tgl()"><svg class="i sun"><use href="#i-sun"/></svg><svg class="i moon"><use href="#i-moon"/></svg><span>Tema claro / oscuro</span></button></div></aside>')

radios = "".join(f'<input type="radio" name="nav" id="dn-{i}" class="st"{" checked" if i == "panorama" else ""}>' for i in ids)
radios += '<input type="radio" name="mode" id="mode-simple" class="st" checked><input type="radio" name="mode" id="mode-adv" class="st">'
radios += '<input type="radio" name="evo2" id="ev2-a" class="st" checked><input type="radio" name="evo2" id="ev2-b" class="st"><input type="radio" name="evo2" id="ev2-c" class="st"><input type="radio" name="hist" id="h-26" class="st" checked><input type="radio" name="hist" id="h-25" class="st">'
radios += '<input type="radio" name="cons" id="cs-todo" class="st" checked><input type="radio" name="cons" id="cs-meta" class="st"><input type="radio" name="cons" id="cs-ia" class="st">'

topbar = (f'<div class="topbar"><div class="tb-l"><div class="client"><span>Cliente</span><b>MIA App</b></div></div>'
          f'<div class="tb-r"><span class="period">{ic("cal")}1 al 15 oct 2026 <span>· vs 16 al 30 sep</span></span><span class="demo">{ic("info")}Demo · datos modelados</span>'
          f'<span class="dd-pill">{ic("gauge")}<b>Data Driven</b> · cada cifra con base, cobertura y origen</span>'
          f'<div class="mode"><label for="mode-simple">{ic("rows")}Básico</label><label for="mode-adv">{ic("sliders")}Avanzado</label></div></div></div>'
          f'<div class="updbar">{ic("refresh", "width:13px;height:13px")}Última actualización por fuente: '
          + "".join(f'<span class="u"><span class="dt" style="background:{c}"></span>{t} <b>{d}</b></span>' for c, t, d in [
              ("var(--src-pro)", "Prometheo", "modelado 15 oct"), ("var(--vio)", "TikTok Ads", "modelado 15 oct"), ("var(--src-meta)", "Meta Ads", "modelado 15 oct"), ("#9C7FD6", "Google Ads", "modelado 15 oct"),
              ("var(--src-mail)", "Email", "modelado 14 oct"), ("var(--src-wpp)", "WhatsApp", "modelado 13 oct"), ("var(--ink3)", "App de MIA", "sin conectar"), ("var(--src-erp)", "Registro de altas", "sin conectar")])
          + "</div>"
          f'<div class="modehint bsc">{ic("rows")}<span><b>Modo básico:</b> lo esencial de cada pestaña, en palabras simples. Pasá a <b>Avanzado</b> para ver el detalle, los cruces y las definiciones.</span></div>'
          f'<div class="modehint adv">{ic("sliders")}<span><b>Modo avanzado:</b> todo lo del básico, más el detalle técnico: bases, coberturas, intervalos y cruces.</span></div>')

extra_css = "<style>" + "".join(
    f"#dn-{i}:checked~.shell .nav[data-t={i}]{{background:var(--grad);color:#fff;box-shadow:0 6px 16px -6px rgba(124,92,191,.6)}}"
    f"#dn-{i}:checked~.shell .nav[data-t={i}] svg.i{{color:#fff}}#dn-{i}:checked~.shell .p-{i}{{display:block}}" for i in ids) + """
:root{--src-tt:var(--ink);--src-app:#6F6888;--brand-font:'Manrope',var(--hel)}.s-tt{background:var(--src-tt)}.s-app{background:var(--src-app)}
.brand2{display:flex;flex-direction:column;align-items:center;text-align:center;gap:10px;padding:14px 10px 20px;border-bottom:1px solid var(--line2);margin-bottom:6px}
.brand2 img{height:72px;width:auto;filter:drop-shadow(0 8px 18px rgba(124,92,191,.25))}.brand2 span{font-family:var(--brand-font);font-weight:700;font-size:16px;line-height:1.15;letter-spacing:-.01em;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.client{display:flex;flex-direction:column;line-height:1}.client span{font-size:10px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--ink3)}
.client b{font-family:var(--brand-font);font-size:30px;font-weight:800;letter-spacing:-.02em;color:var(--ink);margin-top:5px}
.ngrp{margin:6px 0 2px}
.ngrp>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;padding:8px 11px;border-radius:var(--r-s);font-size:12.8px;font-weight:700;color:var(--ink);background:var(--grad-soft);box-shadow:inset 0 -2px 0 0 color-mix(in srgb,var(--vio) 35%,transparent)}
.ngrp>summary::-webkit-details-marker{display:none}
.ng-ic{width:22px;height:22px;border-radius:7px;background:var(--grad);display:flex;align-items:center;justify-content:center;flex-shrink:0}.ng-ic svg.i{width:13px;height:13px;color:#fff}
.ng-t{flex:1}
.ngrp>summary>svg.i:last-child{width:15px;height:15px;color:var(--ink3);transition:transform .2s}.ngrp[open]>summary>svg.i:last-child{transform:rotate(180deg)}
.ng-b{padding:4px 0 4px 6px}
.dd-pill{display:inline-flex;align-items:center;gap:7px;font-size:11px;color:var(--ink2);padding:6px 12px 6px 9px;border-radius:999px;background:var(--surface);border:1px solid transparent;background-image:linear-gradient(var(--surface),var(--surface)),var(--grad);background-origin:border-box;background-clip:padding-box,border-box}
.dd-pill svg.i{width:14px;height:14px;color:var(--vio)}.dd-pill b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
tr.tot td{background:var(--surface2)}.qbr.dn{color:var(--crit)}.hero-h em{font-family:var(--serif);font-weight:400;font-style:italic}
.qr-n{margin-left:auto;font-weight:600;letter-spacing:.02em;text-transform:none;color:var(--ink4)}
.qy small.u{font-size:12px;color:var(--ink3);font-weight:600}
.chh{display:flex;align-items:center;gap:14px;margin-bottom:8px}.chh-ic{width:46px;height:46px;border-radius:14px;background:var(--grad);display:flex;align-items:center;justify-content:center;box-shadow:0 8px 20px -10px rgba(124,92,191,.8)}
.chh-ic svg.i{width:22px;height:22px;color:#fff}.chh-k{display:block;font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--ink3)}.chh-t{display:block;font-size:28px;font-weight:700;letter-spacing:-.02em;color:var(--ink)}
.crit-c .cc-h,.c2-h{display:flex;align-items:center;gap:10px;margin-bottom:12px}.cc-n{width:30px;height:30px;border-radius:10px;background:var(--grad);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center}
.cc-k{display:block;font-size:9.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3)}.crit-c .cc-h b{font-size:15px;color:var(--ink)}
.cc-r{display:flex;justify-content:space-between;gap:10px;align-items:center;padding:8px 10px;border-radius:10px;background:var(--surface2);border:1px solid var(--line2);font-size:12.3px;color:var(--ink2);margin-top:6px}.cc-r b{color:var(--ink);font-variant-numeric:tabular-nums;white-space:nowrap}
.areas{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}.area .ar-h{display:flex;align-items:center;gap:9px}.ar-ic{width:30px;height:30px;border-radius:10px;background:var(--vio-soft);display:flex;align-items:center;justify-content:center}.ar-ic svg.i{width:15px;height:15px;color:var(--vio)}
.area .ar-h b{font-size:13.5px;color:var(--ink);flex:1}.ar-d{font-size:11px;font-weight:800;border-radius:20px;padding:2px 8px}.ar-d.bad{background:var(--crit-bg);color:var(--crit-ink)}.ar-d.ok{background:var(--good-bg);color:var(--good-ink)}.ar-d.neu{background:var(--inset);color:var(--ink3)}
.ar-v{font-size:28px;font-weight:700;color:var(--ink);margin:10px 0 6px;font-variant-numeric:tabular-nums}.ar-v small{font-size:12px;color:var(--ink3);font-weight:600}
.ar-b{height:6px;border-radius:4px;background:var(--inset);overflow:hidden}.ar-b i{display:block;height:100%;background:var(--grad)}
.ar-t{display:flex;flex-wrap:wrap;gap:5px;margin-top:10px}.ar-t span{font-size:10.5px;color:var(--ink2);background:var(--surface2);border:1px solid var(--line2);border-radius:20px;padding:2px 8px}
.qte{margin:8px 0 0;padding:10px 12px;border-radius:12px;background:var(--surface2);font-family:var(--serif);font-style:italic;font-size:14.5px;line-height:1.4;color:var(--ink)}
.empty-st{text-align:center;padding:20px 12px;color:var(--ink3);font-size:12.5px;border:1px dashed var(--line);border-radius:12px}.empty-st p{margin:8px 0 0}.empty-st b{color:var(--ink2)}
.zg{display:grid;grid-template-columns:1.6fr 1fr;gap:14px}.zside{display:flex;flex-direction:column;gap:14px}
.zr{display:flex;gap:12px;align-items:flex-start;padding:9px 0;border-top:1px solid var(--line2)}.zcard .qw+.zr{border-top:0}
.zn{width:26px;height:26px;border-radius:8px;background:var(--vio-soft);color:var(--vio);font-weight:800;font-size:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.zcard .zr:nth-child(-n+4) .zn{background:var(--grad);color:#fff}
.zm{flex:1;min-width:0}.zt{display:flex;justify-content:space-between;gap:10px}.zt b{font-size:14px;color:var(--ink)}.zt span{font-size:12px;color:var(--ink2);font-variant-numeric:tabular-nums}
.zb{height:7px;border-radius:5px;background:var(--inset);margin:6px 0 5px;overflow:hidden}.zb i{display:block;height:100%;background:var(--grad);border-radius:5px}.zs{font-size:11px;color:var(--ink3)}
.crit-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.c2-ic{width:30px;height:30px;border-radius:10px;background:var(--grad);display:flex;align-items:center;justify-content:center}.c2-ic svg.i{width:15px;height:15px;color:#fff}.c2-h b{flex:1;font-size:14px;color:var(--ink)}
.c2-k{display:block;font-size:9.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3)}
.c2-v{font-family:var(--serif);font-style:italic;font-size:23px;line-height:1.2;color:var(--ink);margin:4px 0 4px}.c2-s{font-size:12px;color:var(--ink3)}.c2-s b{color:var(--vio);font-size:14px}
.c2-rows{margin-top:12px;display:flex;flex-direction:column;gap:7px}.cr-r{display:grid;grid-template-columns:1fr auto;gap:4px 10px;font-size:11.8px;color:var(--ink2)}.cr-r b{color:var(--ink);font-variant-numeric:tabular-nums}.cr-r .qf{grid-column:1/-1}
.c2-f{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px;padding-top:10px;border-top:1px solid var(--line2)}.c2-f span{display:inline-flex;align-items:center;gap:4px;font-size:10.5px;color:var(--ink3)}.c2-f svg.i{width:11px;height:11px}
b.hot{color:var(--crit-ink);background:var(--crit-bg);padding:2px 8px;border-radius:6px}
.chs{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m);box-shadow:var(--shadow);padding:14px 16px;border-top:3px solid var(--cc)}
.chs-h{display:flex;align-items:center;gap:10px}.chs-ic{width:34px;height:34px;border-radius:11px;background:var(--cs);display:flex;align-items:center;justify-content:center}.chs-ic svg.i{width:17px;height:17px;color:var(--cc)}
.chs-h b{display:block;font-size:15px;color:var(--ink)}.chs-h span{font-size:11px;color:var(--ink3)}
.adx-ic{background:var(--axb)!important}.adx-ic svg.i{color:var(--ax)!important}
.adx-h .ad-k{display:flex;align-items:center;gap:6px;font-size:9.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);margin:0 0 3px}
.ad-k code{font-family:ui-monospace,Menlo,monospace;font-size:9.5px;letter-spacing:0;color:var(--ink4);background:var(--inset);border-radius:5px;padding:1px 5px;text-transform:none}
.ad-meta2{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;padding:0 15px 12px}.ad-meta2 span{display:flex;flex-direction:column;gap:2px;font-size:10px;color:var(--ink3);background:var(--surface2);border:1px solid var(--line2);border-radius:9px;padding:6px 8px}
.ad-meta2 b{font-size:12.5px;color:var(--ink);font-variant-numeric:tabular-nums}
.vid-h{display:flex;gap:10px;align-items:center;margin-bottom:10px}.vid-ic{width:32px;height:32px;border-radius:10px;background:var(--vio-soft);display:flex;align-items:center;justify-content:center;flex-shrink:0}.vid-ic svg.i{width:16px;height:16px;color:var(--vio)}
.vid-h .ad-k{display:flex;align-items:center;gap:6px;font-size:9.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3)}
.vid-h b{display:block;font-size:13.5px;color:var(--ink);line-height:1.25}.vid-hook{display:flex;justify-content:space-between;align-items:baseline;background:var(--grad-soft);border-radius:10px;padding:8px 10px;margin-bottom:10px}
.vid-hook span{font-size:11px;color:var(--ink2)}.vid-hook b{font-size:22px;color:var(--ink)}.vid .cr-r{margin-top:6px}
.segt{display:inline-flex;gap:4px;padding:4px;border-radius:999px;background:var(--surface);border:1px solid var(--line);box-shadow:var(--shadow);margin-bottom:16px}
.segt label{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:700;color:var(--ink2);padding:7px 14px;border-radius:999px;cursor:pointer}.segt label svg.i{width:14px;height:14px}
#cs-todo:checked~.shell label[for=cs-todo],#cs-meta:checked~.shell label[for=cs-meta],#cs-ia:checked~.shell label[for=cs-ia]{background:var(--grad);color:#fff}
.cstab{display:none}#cs-todo:checked~.shell .cs-todo,#cs-meta:checked~.shell .cs-meta,#cs-ia:checked~.shell .cs-ia{display:block}
.ad-grid{align-items:stretch}.ad-grid>.i3:not([open])>summary{height:100%;display:flex;flex-direction:column}.ad-grid .qbh{margin-top:12px}.ad-grid .qbd{margin-top:auto}
.ad-top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;padding-bottom:12px;border-bottom:1px solid var(--line2)}.ad-top .sx{margin-left:auto;transform:scale(1.12);transform-origin:right center}
.ad-tema{margin-top:14px;font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--tone,var(--vio))}
.ad-title{font-size:17px;font-weight:700;line-height:1.3;letter-spacing:-.01em;color:var(--ink);margin-top:4px;min-height:2.6em}
.ad-do{display:flex;gap:9px;align-items:flex-start;margin-top:12px;padding:12px;border-radius:12px;background:var(--tb,var(--surface2));border:1px solid color-mix(in srgb,var(--tone,var(--vio)) 28%,transparent)}
.ad-do>svg.i{width:16px;height:16px;color:var(--tone,var(--vio));flex-shrink:0;margin-top:2px}.ad-do b{display:block;font-size:9.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--tone,var(--vio))}
.ad-do span{display:block;font-size:14px;font-weight:700;line-height:1.35;color:var(--ink);margin-top:3px;min-height:2.7em}
.ad-meta{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}.ad-meta span{display:grid;grid-template-columns:auto 1fr;align-items:center;column-gap:6px;font-size:11px;color:var(--ink3);background:var(--surface2);border:1px solid var(--line2);border-radius:10px;padding:7px 9px}
.ad-meta svg.i{width:13px;height:13px;color:var(--ink3);grid-row:span 2}.ad-meta em{font-style:normal;font-size:9px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}.ad-meta b{color:var(--ink);font-size:12.5px;font-weight:700}
.i3.av[data-v=corregir]{--tb:var(--sv-corregir-bg)}.i3.av[data-v=proteger]{--tb:var(--sv-proteger-bg)}.i3.av[data-v=separar]{--tb:var(--sv-separar-bg)}.i3.av[data-v=medir]{--tb:var(--sv-medir-bg)}.i3.av[data-v=decidir]{--tb:var(--sv-decidir-bg)}.i3.av[data-v=activar]{--tb:var(--sv-activar-bg)}
/* paleta y degradés del Panorama, sutiles, en todas las cards */
.qx,.qcf.pad,.chs,.area,.crit2{position:relative;overflow:hidden}
.qx::before,.qcf.pad::before{content:"";position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad);opacity:.55}
.qx::after,.qcf.pad::after{content:"";position:absolute;right:-60px;top:-60px;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,color-mix(in srgb,var(--pnk) 14%,transparent),transparent 70%);pointer-events:none}
.qcg::before{background:var(--ct);opacity:.9}
.g4>.qbu:first-child{background:var(--grad-soft);border-color:color-mix(in srgb,var(--vio) 22%,var(--line))}
.g4>.qbu:first-child .qy{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.qbk{background:var(--grad-soft)!important}.qbk svg.i{color:var(--vio)!important}
.chs{background:linear-gradient(180deg,var(--cs),var(--surface) 55%)}.chs .kv>div:first-child{background:var(--surface)!important}
.area{background:linear-gradient(160deg,var(--grad-soft) 0,var(--surface) 45%)}.ar-ic{background:var(--grad)}.ar-ic svg.i{color:#fff}
.crit2{background:linear-gradient(170deg,var(--grad-soft) 0,var(--surface) 40%)}
/* card de anuncio */
.adx-h{background:var(--grad-soft)!important;border-left:0!important;position:relative}
.adx-h::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:2px;background:var(--grad);opacity:.5}
.adx-ic{background:var(--grad)!important;box-shadow:0 6px 14px -8px rgba(124,92,191,.8)}.adx-ic svg.i{color:#fff!important}
.adx-h b{font-size:15px!important}
.adx-tiles .qch{background:var(--surface2)!important;border-color:var(--line2)!important}
.adx-tiles .qch span,.adx-tiles .qch b{color:var(--ink)!important}.adx-tiles .qch span{color:var(--ink3)!important}
.adx-tiles .qch.t2{background:var(--grad-soft)!important;border-color:color-mix(in srgb,var(--vio) 25%,transparent)!important}
.adx-tiles .qch.t3{background:var(--grad)!important;border-color:transparent!important;box-shadow:0 8px 18px -12px rgba(124,92,191,.9)}
.adx-tiles .qch.t3 span,.adx-tiles .qch.t3 b{color:#fff!important}.adx-tiles .qch.t3 b{font-size:20px}
.st-dot{width:7px;height:7px;border-radius:50%;margin-left:auto;display:inline-block}.st-dot[data-s=good]{background:var(--good)}.st-dot[data-s=warn]{background:var(--warn)}.st-dot[data-s=crit]{background:var(--crit)}
.qch.t3 .st-dot{box-shadow:0 0 0 2px rgba(255,255,255,.85)}
.qcb i{background:var(--grad)!important;opacity:.85}
.ad-v{background:var(--grad-soft)!important;border-top:1px solid color-mix(in srgb,var(--vio) 18%,transparent)!important;color:var(--ink)!important}
.ad-v svg.i{color:var(--vio)!important}.ad-v b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.ad-v[data-s=crit]{box-shadow:inset 3px 0 0 var(--crit)}.ad-v[data-s=warn]{box-shadow:inset 3px 0 0 var(--warn)}.ad-v[data-s=good]{box-shadow:inset 3px 0 0 var(--good)}
.zn{background:var(--grad-soft)}
/* v5 · simetría: casilleros en columnas iguales */
.kv{grid-template-columns:repeat(var(--kc,3),minmax(0,1fr))!important}
.g2>*,.g3>*,.g4>*{min-width:0}
/* cards blancas sobre el fondo, con jerarquía */
.qx,.qcf,.qbu,.chs,.area,.crit2,.adx,.chsec{background:var(--surface)!important;box-shadow:0 1px 0 rgba(255,255,255,.6) inset,0 14px 34px -22px rgba(60,40,120,.45)!important;border:1px solid color-mix(in srgb,var(--vio) 14%,var(--line))!important}
.g4>.qbu:first-child{background:linear-gradient(160deg,var(--grad-soft),var(--surface) 70%)!important}
.qbk{background:var(--grad)!important}.qbk svg.i{color:#fff!important}
/* criterio comercial: la frase con más jerarquía */
.c2-q{margin:2px -16px 12px;padding:14px 16px 14px 18px;background:var(--grad-soft);border-left:4px solid transparent;border-image:var(--grad) 1;position:relative}
.c2-v{font-size:27px!important;line-height:1.15!important;margin:4px 0 6px!important}
.c2-s b{font-size:18px!important}
/* subsector grande dentro de una pestaña */
.bigsub{display:flex;gap:16px;align-items:flex-start;margin:34px 0 14px;padding:20px 22px;border-radius:var(--r-xl);background:var(--grad-soft);border:1px solid color-mix(in srgb,var(--vio) 20%,var(--line));position:relative;overflow:hidden}
.bigsub::before{content:"";position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.bs-ic{width:46px;height:46px;border-radius:14px;background:var(--grad);display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 8px 20px -10px rgba(124,92,191,.8)}.bs-ic svg.i{width:22px;height:22px;color:#fff}
.bs-k{font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--vio)}.bs-t{font-size:22px;font-weight:700;letter-spacing:-.015em;color:var(--ink);margin-top:4px}.bs-t em{font-family:var(--serif);font-weight:400}
.bigsub p{margin:6px 0 0;font-size:13px;color:var(--ink2)}
.go-mej{display:flex;gap:10px;align-items:center;margin-top:18px;padding:12px 16px;border-radius:var(--r-m);background:var(--grad-soft);font-size:13px;color:var(--ink2)}.go-mej svg.i{width:16px;height:16px;color:var(--vio)}
/* usuarios: qué quiere cada etapa */
.et-r{display:flex;gap:12px;padding:10px 0;border-top:1px solid var(--line2)}.qx .qw+.et-r{border-top:0}
.et-n{width:26px;height:26px;border-radius:8px;background:var(--grad);color:#fff;font-weight:800;font-size:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.et-m{flex:1;min-width:0}.et-t{display:flex;justify-content:space-between;font-size:11px;color:var(--ink3);text-transform:uppercase;letter-spacing:.06em;font-weight:700}.et-t b{color:var(--ink2)}
.et-i{display:flex;align-items:baseline;gap:8px;margin-top:3px}.et-i em{font-style:normal;font-size:11px;color:var(--ink3)}.et-i b{font-size:16px;color:var(--ink)}.et-i span{margin-left:auto;font-size:12px;color:var(--vio);font-weight:700}
.et-m p{margin:0;font-size:12px;color:var(--ink2);line-height:1.45}
/* visión 360: sección por red */
.chsec{border-radius:var(--r-xl);padding:0;margin-bottom:20px;overflow:hidden;border-top:4px solid var(--cc)!important}
.chsec-h{display:grid;grid-template-columns:auto 1fr minmax(0,1.4fr);gap:16px;align-items:center;padding:18px 20px;background:linear-gradient(120deg,var(--cs),var(--surface) 70%)}
.chsec-ic{width:56px;height:56px;border-radius:16px;background:var(--grad);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 22px -12px rgba(124,92,191,.9)}.chsec-ic svg.i{width:28px;height:28px;color:#fff}
.chsec-t b{display:block;font-size:26px;font-weight:800;letter-spacing:-.02em;color:var(--ink);font-family:var(--brand-font)}.chsec-t span{font-size:12px;color:var(--ink3)}
.chsec-h .kv{margin:0}.chsec-h .kv>div{background:var(--surface)!important}
.chsec-sub{display:flex;align-items:center;gap:10px;padding:12px 20px;border-top:1px solid var(--line2);border-bottom:1px solid var(--line2);background:var(--surface2)}
.chsec-sub span{display:inline-flex;align-items:center;gap:7px;font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--ink3)}.chsec-sub svg.i{width:13px;height:13px;color:var(--vio)}
.chsec .adg{padding:16px 20px 20px}
/* campaña › conjunto › anuncio */
.hier2{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-bottom:14px}.hier2>div{display:grid;grid-template-columns:auto 1fr;column-gap:10px;align-items:center;padding:12px 14px;border-radius:var(--r-m);background:var(--surface);border:1px solid var(--line)}
.hier2 b{font-size:13px;color:var(--ink)}.hier2 span:last-child{grid-column:2;font-size:11.5px;color:var(--ink3)}
.tr-cic{width:30px;height:30px;border-radius:10px;background:var(--grad);display:flex;align-items:center;justify-content:center;grid-row:span 2}.tr-cic svg.i{width:15px;height:15px;color:#fff}
.tree{display:flex;flex-direction:column;gap:14px}
.tr-camp{background:var(--surface);border:1px solid color-mix(in srgb,var(--vio) 16%,var(--line));border-radius:var(--r-l);box-shadow:0 14px 34px -24px rgba(60,40,120,.5);overflow:hidden}
.tr-chd{display:grid;grid-template-columns:auto minmax(0,1fr) minmax(0,1.6fr);gap:14px;align-items:center;padding:14px 16px;background:var(--grad-soft)}
.tr-chd>div>b{display:block;font-size:17px;color:var(--ink)}.tr-lv{display:inline-flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3)}.tr-lv svg.i{width:11px;height:11px}
.tr-chd .kv{margin:0}.tr-chd .kv>div{background:var(--surface)!important}
.tr-conj{margin:12px 16px;border:1px solid var(--line2);border-radius:var(--r-m);background:var(--surface2);overflow:hidden}
.tr-ch{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;padding:10px 14px;border-bottom:1px solid var(--line2)}.tr-ch b{font-size:14px;color:var(--ink)}.tr-s{margin-left:auto;font-size:11.5px;color:var(--ink3)}
.tr-ad{display:grid;grid-template-columns:auto minmax(0,1fr) minmax(0,1.5fr);gap:12px;align-items:center;padding:10px 14px;background:var(--surface);border-top:1px solid var(--line2)}.tr-ch+.tr-ad{border-top:0}
.tr-ic{width:28px;height:28px;border-radius:9px;background:var(--vio-soft);display:flex;align-items:center;justify-content:center}.tr-ic svg.i{width:14px;height:14px;color:var(--vio)}
.tr-n b{display:block;font-size:13.5px;color:var(--ink)}.tr-n span{font-size:11px;color:var(--ink3)}.tr-n code{font-family:ui-monospace,Menlo,monospace;font-size:10px;color:var(--ink4)}
.tr-m{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px}.tr-m span{display:flex;flex-direction:column;font-size:10px;color:var(--ink3);background:var(--surface2);border-radius:8px;padding:5px 8px}.tr-m b{font-size:13.5px;color:var(--ink);font-variant-numeric:tabular-nums}
.tr-m .tr-alt{background:var(--grad);color:rgba(255,255,255,.85)}.tr-m .tr-alt b{color:#fff}
/* evolución e histórico */
#ev2-a:checked~.shell label[for=ev2-a],#ev2-b:checked~.shell label[for=ev2-b],#ev2-c:checked~.shell label[for=ev2-c],#h-26:checked~.shell label[for=h-26],#h-25:checked~.shell label[for=h-25]{background:var(--grad);color:#fff}
.evtab,.htab{display:none}#ev2-a:checked~.shell .ev-a,#ev2-b:checked~.shell .ev-b,#ev2-c:checked~.shell .ev-c,#h-26:checked~.shell .h26,#h-25:checked~.shell .h25{display:block}
.hq{background:var(--surface);border:1px solid color-mix(in srgb,var(--vio) 14%,var(--line));border-radius:var(--r-m);margin-bottom:10px;overflow:hidden;box-shadow:0 10px 26px -22px rgba(60,40,120,.5)}
.hq>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:12px;padding:12px 16px;background:var(--grad-soft)}.hq>summary::-webkit-details-marker{display:none}
.hq>summary b{font-size:14px;color:var(--ink)}.hq>summary span{margin-left:auto;font-size:12px;color:var(--ink2)}.hq>summary svg.i{width:15px;height:15px;color:var(--ink3);transition:transform .2s}.hq[open]>summary svg.i{transform:rotate(180deg)}
.hq .qcf{border:0!important;box-shadow:none!important;border-radius:0}
@media (max-width:900px){.chsec-h,.tr-chd,.tr-ad{grid-template-columns:1fr}.hier2{grid-template-columns:1fr}.tr-m{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:900px){.areas,.zg{grid-template-columns:1fr}.ad-meta,.ad-meta2{grid-template-columns:1fr}.client b{font-size:24px}}
</style>"""
tt_icon = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
           '<symbol id="i-play" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5M14 3c.5 2.6 2.4 4.5 5 5"/></symbol><symbol id="i-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 18a7 7 0 1 0 0-14 7 7 0 0 0 0 14ZM20 20l-4-4"/></symbol></defs></svg>')

panels = "".join(f'<section class="panel p-{i}">{P[i]}</section>' for i in ids)
html = head + extra_css + tt_icon + radios + '<div class="shell">' + "".join(side) + '<main class="main">' + topbar + panels + "</main></div>" + scripts
OUT.write_text(html, encoding="utf-8")
print(OUT, len(html.encode()))
