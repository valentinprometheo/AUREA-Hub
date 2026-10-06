"""Componentes HTML reutilizados por todas las pestañas."""
from icons import ic


def fmt(n, dec=0):
    """Número con separador de miles a la argentina."""
    if isinstance(n, str):
        return n
    if dec:
        s = f"{n:,.{dec}f}"
    else:
        s = f"{round(n):,}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def pct(a, b, dec=0):
    if not b:
        return 0
    v = round(100 * a / b, dec)
    return int(v) if dec == 0 else v


def money(m):
    """Millones con coma decimal: 42.8 -> $42,8 M"""
    return "$" + fmt(m, 1) + " M"


# ---------- chips ----------
SRC = {
    "pro": ("s-pro", "chat", "Prometheo"),
    "erp": ("s-erp", "ledger", "Producí"),
    "meta": ("s-meta", "meta", "Meta"),
    "calc": ("s-calc", "sigma", "Cálculo"),
    "wpp": ("s-wpp", "wa", "WhatsApp"),
    "mail": ("s-mail", "mail", "Email"),
    "goog": ("s-goog", "google", "Google"),
}


def src(k, label=None):
    c, i, t = SRC[k]
    return f'<span class="src {c}">{ic(i)}{label or t}</span>'


LVL = {
    "hecho": ("l-hecho", "checkc", "Hecho"),
    "senal": ("l-senal", "pulse", "Señal"),
    "indicio": ("l-indicio", "eye", "Indicio"),
    "proy": ("l-proy", "trend", "Proyección"),
    "est": ("l-est", "sigma", "Estimado"),
}


def lvl(k):
    c, i, t = LVL[k]
    return f'<span class="lvl {c}">{ic(i)}{t}</span>'


OWN = {"mkt": ("o-mkt", "Marketing"), "ven": ("o-ven", "Ventas"), "cob": ("o-cob", "Cobranza"), "aurea": ("o-aurea", "AUREA")}


def own(k, label=None):
    c, t = OWN[k]
    return f'<span class="own {c}">{label or t}</span>'


def chip(text, icon=None):
    return f'<span class="chip">{ic(icon) if icon else ""}{text}</span>'


def base(text):
    return f'<span class="base">{ic("filter")}{text}</span>'


def delta(txt, kind="good", arrow="up"):
    a = ic(arrow) if arrow else ""
    return f'<span class="delta d-{kind}">{a}{txt}</span>'


EST = {"ok": ("check", "Al día"), "warn": ("clock", "Con deuda"), "bad": ("alert", "Vencido +30d"), "off": ("minus", "Pasivo")}


def est(k, label=None):
    i, t = EST[k]
    return f'<span class="est {k}">{ic(i)}{label or t}</span>'


def bsc_adv(b, a):
    """Mismo dato, dos profundidades de texto."""
    return f'<span class="bsc">{b}</span><span class="adv">{a}</span>'


# ---------- headers ----------
def sec_head(eyebrow, title=None, lead=None, extra=""):
    h = f'<div class="sec-head"><div class="eyebrow"><span class="eb-orb"></span>{eyebrow}{extra}</div>'
    if title:
        h += f'<h1 class="sec">{title}</h1>'
    if lead:
        if isinstance(lead, tuple):
            lead = bsc_adv(*lead)
        h += f'<p class="lead">{lead}</p>'
    return h + "</div>"


def eyebrow(text, extra=""):
    return f'<div class="sec-head"><div class="eyebrow"><span class="eb-orb"></span>{text}{extra}</div></div>'


def ghdr(text, icon=None, right="", chips=""):
    r = f'<span class="r">{right}</span>' if right else ""
    return f'<div class="ghdr">{ic(icon) if icon else ""}{text}{chips}{r}</div>'


def banner(kind, icon, html):
    return f'<div class="banner {kind}"><div class="bn-ic">{ic(icon)}</div><div>{html}</div></div>'


# ---------- KPI ----------
def kpi(label, value, d="", sub="", icon="chat", tone="", source=None, adv=""):
    s = src(source) if source else ""
    sub_h = f'<div class="k-s">{sub}</div>' if sub else ""
    adv_h = f'<div class="k-ab adv">{adv}</div>' if adv else ""
    return (f'<div class="kpi"><div class="k-top"><div class="k-ic {tone}">{ic(icon)}</div>{s}</div>'
            f'<div class="k-l">{label}</div><div class="k-row"><div class="k-n">{value}</div>{d}</div>{sub_h}{adv_h}</div>')


# ---------- barras ----------
def bar(label, val, width, extra="", color=None, cls="", icon=None):
    st = f"width:{max(width, 1.5):.1f}%" + (f";background:{color}" if color else "")
    ex = f"<span>{extra}</span>" if extra != "" else ""
    lab = (ic(icon) if icon else "") + label
    return (f'<div class="bar-row {cls}"><span class="bar-lab">{lab}</span><span class="bar-val">{val}{ex}</span>'
            f'<div class="bar-track"><div class="bar-fill" style="{st}"></div></div></div>')


def bars(rows, color=None, total=None, mx=None):
    """rows: (label, value, extra). Ancho relativo al máximo."""
    mx = mx or max(r[1] for r in rows)
    out = []
    for r in rows:
        lab, v = r[0], r[1]
        extra = r[2] if len(r) > 2 else (f"{pct(v, total)}%" if total else "")
        col = r[3] if len(r) > 3 else color
        out.append(bar(lab, fmt(v), 100 * v / mx, extra, col))
    return "".join(out)


def vcard(title, body, icon=None, right="", chips="", cls=""):
    return f'<div class="vcard {cls}">{ghdr(title, icon, right, chips)}{body}</div>'


# ---------- tabla ----------
def table(head, rows, minw=640, cls=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    trs = []
    for r in rows:
        if isinstance(r, tuple) and len(r) == 2 and isinstance(r[1], str):
            cells, trc = r[0], r[1].replace("tr:", "")
        else:
            cells, trc = r, ""
        tds = "".join(c if c.startswith("<td") else f"<td>{c}</td>" for c in cells)
        trs.append(f'<tr class="{trc}">{tds}</tr>')
    return (f'<div class="card {cls}" style="overflow:hidden"><div class="tblwrap"><table style="min-width:{minw}px">'
            f'<thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div></div>')


def minibar(p, color="var(--vio)"):
    return f'<span class="minibar"><i style="width:{min(p, 100):.0f}%;background:{color}"></i></span>'


# ---------- comparación literal (subsector 3) ----------
def cmpbar(value_pct, marker_pct=None, marker_label="", fill_label="este anuncio", marker_legend=""):
    fill = f'<span class="fill" style="width:{min(value_pct, 100):.1f}%"></span>'
    mk = ""
    lg = f'<span><i class="sw"></i>{fill_label}</span>'
    if marker_pct is not None:
        pos = "c" if 22 <= marker_pct <= 78 else ("lft" if marker_pct < 22 else "rgt")
        mk = f'<span class="mk {pos}" style="left:calc({marker_pct:.1f}% - 1px)"><b>{marker_label}</b></span>'
        lg += f'<span><i class="sm"></i>{marker_legend or marker_label}</span>'
    return f'<div class="cmp">{fill}{mk}</div><div class="cmp-lg">{lg}</div>'


# ---------- card de insight: 3 subsectores ----------
SEAL = {
    "subir": ("t-subir", "up", "Subir"),
    "mant": ("t-mant", "shield", "Mantener"),
    "corr": ("t-corr", "wrench", "Corregir"),
    "paus": ("t-paus", "pause", "Pausar"),
    "red": ("t-corr", "down", "Reducir"),
    "prob": ("t-prob", "flask", "Probar"),
    # criterio comercial: sustantivos, no acciones
    "motivo": ("t-motivo", "quote", "Motivo"),
    "urg": ("t-urg", "bolt", "Urgencia"),
    "avance": ("t-avance", "cal", "Avance"),
    "freno": ("t-freno", "hand", "Freno"),
    "filtro": ("t-filtro", "filter", "Filtro"),
    "prior": ("t-prior", "star", "Prioridad"),
    # comercial (red)
    "cruz": ("t-subir", "plus", "Ampliar"),
    "cuidar": ("t-mant", "shield", "Cuidar"),
    "cobrar": ("t-paus", "dollar", "Cobrar antes"),
    "react": ("t-prob", "refresh", "Reactivar"),
    "replicar": ("t-mant", "repeat", "Replicar"),
    "ruta": ("t-prob", "route", "Ordenar ruta"),
    "asignar": ("t-corr", "user", "Asignar"),
}

CTX_IC = {
    "Campaña": ("k-camp", "camp"), "Conjunto": ("k-conj", "conj"), "Anuncio": ("k-anun", "anun"),
    "Grupo": ("k-conj", "conj"), "Palabra": ("k-anun", "search"),
    "Segmento": ("k-seg", "users"), "Fuente": ("k-src", "chat"), "Base": ("k-base", "filter"),
    "Envío": ("k-anun", "mail"), "Plantilla": ("k-anun", "wa"), "Corredor": ("k-seg", "user"),
    "Zona": ("k-conj", "pin"), "Cartera": ("k-base", "building"), "Qué mide": ("k-seg", "target"),
    "Dato": ("k-src", "chat"), "Origen": ("k-src", "list"),
}


def ctx_rows(rows):
    out = []
    for k, v in rows:
        cls, i = CTX_IC.get(k, ("k-base", "info"))
        out.append(f'<div class="cx"><span class="cx-ic {cls}">{ic(i)}</span><span class="cx-k">{k}</span><span class="cx-v">{v}</span></div>')
    return f'<div class="i3-ctx">{"".join(out)}</div>'


def i3(seal, name, ctx, bullets, big, txt, cmp="", owner="", level="", adv="", sources="", lab2="Qué muestra el CRM", lab3="Resultado contra el objetivo"):
    """Card de insight.
    1 (visible): sello + nombre literal + contexto (campaña / conjunto / anuncio u otro).
    2 y 3 (plegados): bullets de análisis y resultado con comparación literal.
    """
    tcls, ticon, tlabel = SEAL[seal]
    top = f'<div class="i3-top"><span class="seal"><span class="sic">{ic(ticon)}</span>{tlabel}</span>{owner}{level}</div>'
    s1 = (f'<summary>{top}<div class="i3-nm">{name}</div>{ctx_rows(ctx)}'
          f'<div class="i3-more"><span class="op">Ver análisis y resultado</span><span class="cl">Ocultar análisis</span>{ic("chev")}</div></summary>')
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    s2 = f'<div class="i3-sec"><div class="i3-lab"><span class="n">2</span>{lab2}{sources}</div><ul class="i3-b">{lis}</ul></div>'
    s3 = (f'<div class="i3-sec"><div class="i3-lab"><span class="n">3</span>{lab3}</div>'
          f'<div class="res"><div class="big">{big}</div><div class="rt"><div class="txt">{txt}</div>{cmp}</div></div></div>')
    a = f'<div class="i3-sec i3-adv adv"><div class="i3-lab"><span class="n">{ic("sliders")}</span>Lectura avanzada</div>{adv}</div>' if adv else ""
    return f'<details class="i3 {tcls}">{s1}{s2}{s3}{a}</details>'


def kv(items):
    """items: (valor, etiqueta)"""
    return '<div class="kv">' + "".join(f'<div><div class="v">{v}</div><div class="k">{k}</div></div>' for v, k in items) + "</div>"


def mincard(title, sub, body, icon="grid", val="", val_lab="", open_=False):
    v = f'<div class="mc-v">{val}<small>{val_lab}</small></div>' if val != "" else ""
    o = " open" if open_ else ""
    return (f'<details class="mincard"{o}><summary><div class="mc-ic">{ic(icon)}</div><div class="mc-t"><b>{title}</b><span>{sub}</span></div>{v}'
            f'<span class="chev">{ic("chev")}</span></summary><div class="mc-body">{body}</div></details>')


def ul(items, cls="i3-b"):
    return f'<ul class="{cls}" style="--tone:var(--vio)">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def fsteps(steps, n=None):
    """steps: dict(num, label, val, pct_total, pass_txt, cls)"""
    out = []
    for s in steps:
        out.append(
            f'<div class="fs {s.get("cls", "")}"><div class="t"><span>{s["num"]}</span><span class="p">{s["pt"]}</span></div>'
            f'<div class="l">{s["label"]}</div><div class="v">{s["val"]}</div>'
            f'<div class="bar"><i style="width:{s["w"]}%"></i></div>'
            f'<div class="pass"><span>{s["pass"]}</span></div></div>')
    return f'<div class="fsteps" style="--n:{n or len(steps)}">{"".join(out)}</div>'
