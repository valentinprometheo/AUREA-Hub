# Componentes del tablero IC (markup idéntico al tablero EDFAN de AUREA)
import html as _h

def esc(s): return _h.escape(str(s), quote=False)
def I(n): return f'<svg class="i"><use href="#i-{n}"/></svg>'

def num(n, d=0):
    """Formato es-AR: 1.234 · 0,48"""
    if isinstance(n, str): return n
    s = f'{n:,.{d}f}'
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')

def pct(a, b, d=0):
    return '—' if not b else num(100 * a / b, d) + '%'

SRC = {
    'pro': ('qt', 'chat', 'Prometheo'),
    'calc': ('qcj', 'sigma', 'Cálculo'),
    'panel': ('qt', 'pie', 'Panel de consumo'),
    'tokko': ('qt', 'building', 'Tokko vía Prometheo'),
    'meta': ('qcj', 'meta', 'Tarifa oficial Meta'),
    'aurea': ('qcj', 'spark', 'AUREA'),
}
def src(k):
    c, i, l = SRC[k]
    return f'<span class="qba {c}">{I(i)}{l}</span>'

LVL = {
    'hecho': ('l-hecho', 'checkc', 'Hecho'), 'senal': ('qcr', 'pulse', 'Señal'),
    'indicio': ('qbw', 'eye', 'Indicio'), 'noreport': ('l-proy', 'x', 'No reportable'),
    'noexiste': ('l-proy', 'x', 'No existe'), 'nomedible': ('l-proy', 'x', 'No medible'),
    'calculo': ('qbw', 'sigma', 'Cálculo'), 'propuesta': ('qbw', 'flask', 'Propuesta a validar'),
}
def lvl(k):
    c, i, l = LVL[k]
    return f'<span class="qbx {c}">{I(i)}{l}</span>'

def level_of(p):
    return 'hecho' if p >= 80 else 'senal' if p >= 40 else 'indicio' if p >= 10 else 'noreport'

def BA(b, a=None):
    """Texto básico / avanzado."""
    out = f'<span class="bsc">{b}</span>'
    if a: out += f'<span class="adv">{a}</span>'
    return out

def head(kicker, h1, em, b, a=None):
    return (f'<div class="qo"><div class="qr"><span class="qy"></span>{kicker}</div>'
            f'<h1 class="sec">{h1} <em>{em}</em></h1><p class="lead">{BA(b, a)}</p></div>')

def sec(t): return f'<div class="qo"><div class="qr"><span class="qy"></span>{t}</div></div>'

def kpi(icon, tone, s, name, val, delta=None, dcls='d-flat', darrow=None, b='', a=None, defin=None):
    tone_c = f' {tone}' if tone else ''
    d = ''
    if delta is not None:
        ar = I(darrow) if darrow else ''
        d = f'<span class="qcv {dcls}">{ar}{delta}</span>'
    out = (f'<div class="qbm"><div class="qw"><div class="qbb{tone_c}">{I(icon)}</div>{src(s)}</div>'
           f'<div class="qbn">{name}</div><div class="qx"><div class="qbo">{val}</div>{d}</div>'
           f'<div class="qbp">{BA(b, a) if a else b}</div>')
    if defin: out += f'<div class="qcc">{defin}</div>'
    return out + '</div>'

def bar(label, val, sub, w, color='var(--vio)', miss=False, tag=''):
    cls = 'qd miss' if miss else 'qd'
    st = f'width:{w:.1f}%' + ('' if miss else f';background:{color}')
    return (f'<div class="{cls}"><span class="qe">{label}{tag}</span><span class="qf">{val}<span>{sub}</span></span>'
            f'<div class="qa"><div class="qb" style="{st}"></div></div></div>')

def bars(items, total=None, color='var(--vio)', maxv=None, subfmt=None):
    """items: [(label, n)] ; % sobre total"""
    mx = maxv or max([n for _, n in items] + [1])
    out = ''
    for lab, n in items:
        sub = subfmt(n) if subfmt else (pct(n, total) if total else '')
        out += bar(esc(lab), num(n), sub, 100 * n / mx, color)
    return out

def card(icon, title, s=None, r='', body='', cls='qbe'):
    sc = src(s) if s else ''
    rr = f'<span class="r">{r}</span>' if r else ''
    return f'<div class="{cls}"><div class="qbj">{I(icon)}{title}{sc}{rr}</div>{body}</div>'

def qci(icon, title, s=None, r='', body=''):
    return card(icon, title, s, r, body, cls='qci pad')

def table(headers, rows, minw=620, txt=False):
    th = ''.join(f'<th>{h}</th>' for h in headers)
    tr = ''
    for r in rows:
        cells = ''.join(f'<td>{c}</td>' if i else f'<td><b>{c}</b></td>' for i, c in enumerate(r))
        tr += f'<tr class="">{cells}</tr>'
    cls = ' class="tt"' if txt else ''
    return (f'<div class="qci" style="overflow:hidden"><div class="qby"><table{cls} style="min-width:{minw}px">'
            f'<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div></div>')

def qbd(b, a=None, style=''):
    st = f' style="{style}"' if style else ''
    return f'<div class="qbd"{st}>{BA(b, a) if a else b}</div>'

def note(t): return f'<p class="qbd" style="margin-top:8px">{t}</p>'

def yeq(t):
    return f'<div class="yeq">{I("arrow")}<div><b>Y entonces qué</b><span>{t}</span></div></div>'

def empty(icon, title, text):
    return (f'<div class="empty">{I(icon)}<b style="color:var(--ink2);font-size:13px">{title}</b>'
            f'<span>{text}</span></div>')

def quote(title, lines, icon='quote'):
    ps = ''.join(f'<p>{l}</p>' for l in lines)
    return f'<div class="quote"><h5>{I(icon)}{title}</h5>{ps}</div>'

# ---------- Cards de acción ----------
VERB = {'activar': ('bolt', 'Activar'), 'corregir': ('wrench', 'Corregir'), 'separar': ('layers', 'Separar'),
        'medir': ('pulse', 'Medir'), 'decidir': ('compass', 'Decidir'), 'proteger': ('shield', 'Proteger'),
        'mantener': ('shield', 'Mantener'), 'subir': ('up', 'Subir'), 'reducir': ('down', 'Reducir')}
OWN = {'AUREA': 'qcq qcl', 'Ventas': 'qcq o-ven', 'Marketing': 'qcq o-mkt', 'Dirección': 'qcq o-cob'}
PARTS = [('Base', 20), ('Fuente', 15), ('Cobertura', 15), ('Profundidad', 20), ('Evidencia', 15), ('Cierre', 15)]

def band(s):
    if s >= 80: return 'alta', 'basada en datos', 4
    if s >= 55: return 'media', 'informada por datos', 3
    if s >= 30: return 'hipotesis', 'hipótesis con indicio', 2
    return 'criterio', 'criterio experto', 1

def gauge(score, em=False):
    b, lab, k = band(score)
    dots = ''.join(f'<i class="{"on" if i < k else ""}"></i>' for i in range(4))
    e = f'<em>{lab}</em>' if em else ''
    return (f'<span class="sx" data-b="{b}" title="Índice data-driven {score}%: {lab}. Cuánto de esta acción se apoya en '
            f'datos verificables. Rúbrica v1, sin calibrar.">{I("gauge")}<b>{score}<small>%</small></b>'
            f'<span class="qs">{dots}</span>{e}</span>')

def mc(kind):
    if not kind: return ''
    if kind == 'start':
        return '<span class="mc mc-s" title="Mejora Continua · Plan Start (estabilidad): estrategia y ajustes del agente y el CRM, dentro del plan contratado.">MC · Start</span>'
    return '<span class="mc mc-p" title="Mejora Continua · Plan Pro (escalabilidad): integración nativa entre plataformas; es desarrollo y se cotiza aparte.">MC · Pro</span>'

def act(verb, owner, parts, title, mide, base, dato, cite, hacer, donde, efecto, medimos, guard,
        why, techo, adv=False, mcard=None, ceiling_lbl=None):
    score = sum(parts)
    lim = {'Hecho': 100, 'Señal': 79, 'Indicio': 54, 'No reportable': 29, 'Modelado': 54}[techo]
    score = min(score, lim)
    ic, vl = VERB[verb]
    cls = 'i3 av adv' if adv else 'i3 av'
    qj = ''.join(f'<div class="qj"><span>{n}</span><span class="qk"><i style="width:{round(100*p/m)}%"></i></span><b>{p}/{m}</b></div>'
                 for (n, m), p in zip(PARTS, parts))
    capped = '' if sum(parts) <= lim else f' El cálculo da {sum(parts)}: se aplica el techo.'
    return (f'<details class="{cls}" data-v="{verb}"><summary><div class="qbg"><span class="qbz"><span class="qcp">{I(ic)}</span>{vl}</span>'
            f'<span class="{OWN[owner]}">{owner}</span>{gauge(score)}</div>'
            f'<div class="mcrow">{mc(mcard)}</div>'
            f'<div class="qbr">{title}</div><div class="qbh">'
            f'<div class="cx"><span class="ql qbq">{I("target")}</span><span class="qm">Qué mide</span><span class="qn">{mide}</span></div>'
            f'<div class="cx"><span class="ql qbt">{I("filter")}</span><span class="qm">Base</span><span class="qn">{base}</span></div>'
            f'<div class="cx"><span class="ql qce">{I("chat")}</span><span class="qm">Dato</span><span class="qn">{dato} <cite>{cite}</cite></span></div>'
            f'</div><div class="qbc"><span class="op">Qué hago ahora</span><span class="cl">Plegar</span>{I("chev")}</div></summary>'
            f'<div class="qbody"><div class="qh"><div class="qi"><span class="n">{I("arrow")}</span>Qué hacer</div><p class="qp">{hacer}</p>'
            f'<div class="qz">{I("pin")}<span><b>Dónde se cambia:</b> {donde}</span></div></div>'
            f'<div class="qh"><div class="qi"><span class="n">{I("target")}</span>Efecto esperado</div><p class="qp">{efecto}</p></div>'
            f'<div class="qh"><div class="qi"><span class="n">{I("pulse")}</span>Cómo lo medimos</div><p class="qp">{medimos}</p>'
            f'<div class="qca">{I("shield")}<span><b>Guardiana:</b> {guard}</span></div></div>'
            f'<div class="qh qbs"><div class="qi"><span class="n">{I("gauge")}</span>Por qué este índice {gauge(score, True)}</div>'
            f'<div class="qcb">{qj}</div><p class="qbi">{why}{capped} Techo por el dato central ({techo}): {lim}. '
            f'Rúbrica v1, sin calibrar: el resultado se registra al cierre del período.</p></div></div></details>')

def legend():
    return (f'<div class="sxl">{I("gauge")}<b>Índice data-driven</b><span>cuánto de cada acción se apoya en datos:</span>'
            '<span class="qcd" data-b="alta"><i></i>80+ basada en datos</span><span class="qcd" data-b="media"><i></i>55–79 informada</span>'
            '<span class="qcd" data-b="hipotesis"><i></i>30–54 hipótesis</span><span class="qcd" data-b="criterio"><i></i>menos de 30 criterio</span></div>')

def mclegend():
    return ('<div class="mcl"><b>Quién lo ejecuta</b>'
            f'{mc("start")}<span>Estabilidad: estrategia y ajustes del agente y del CRM, dentro de tu plan de Mejora Continua.</span>'
            f'{mc("pro")}<span>Escalabilidad: integración nativa entre plataformas. Es desarrollo y se cotiza aparte.</span></div>')

def acts(cards, n_total):
    return (f'<div class="igrid avg">{"".join(cards)}</div>'
            f'<p class="qbd bsc">Las tres de mayor impacto. En <b>Avanzado</b> se ven las {n_total}.</p>')

# ---------- Posible mejora (Mi Prometheo) ----------
def pm(pid, n, kicker, title, desc, chips, score, count_lbl, prompt, color='var(--vio)', mcard=None, done=False):
    ch = ''.join(f'<span class="qq" style="--c:{color}">{c}</span>' for c in chips)
    nbox = f'<div class="pm-n pm-done">{I("checkc")}</div>' if done else f'<div class="pm-n">{n}</div>'
    body = ''
    if prompt:
        body = (f'<div class="qcu"><div class="mp"><div class="mp-h"><span class="mp-av">{I("bot")}</span><div><b>Mi Prometheo</b>'
                f'<span>Prompt listo para pegar · revisalo antes de enviar</span></div><button class="mp-copy" type="button" data-copy="pt-{pid}">'
                f'{I("doc")}<span>Copiar prompt</span></button></div><div class="qch" id="pt-{pid}">{esc(prompt)}</div></div></div>')
    sc = gauge(score) if score is not None else ''
    tail = (f'<div class="qct"><span class="op">Ver prompt para Mi Prometheo</span><span class="cl">Plegar</span>{I("chev")}</div>'
            if prompt else '')
    cnt = f'<div class="qcy"><b>{count_lbl[0]}</b><span>{count_lbl[1]}</span></div>' if count_lbl else ''
    return (f'<details class="pm{" pm-ok" if done else ""}" id="{pid}" style="--pc:{color}"><summary>{nbox}<div class="qcs"><div class="pm-k">{kicker}</div>'
            f'<div class="pm-t">{title}</div><div class="qcx">{desc}</div><div class="qck">{ch}{mc(mcard)}{sc}</div></div>{cnt}{tail}</summary>{body}</details>')

def stage(color, icon, title, sub, qty, unit, rows, actxt):
    rl = ''.join(f'<div class="rowl"><span class="k">{I(i)}{k}</span><span class="v">{v}</span></div>' for i, k, v in rows)
    return (f'<div class="stage" style="--stc:{color}"><div class="sh"><div class="dec-ic">{I(icon)}</div><h4>{title}</h4></div>'
            f'<div class="ssub">{sub}</div><div class="qty">{qty} <small>{unit}</small></div>{rl}'
            f'<div class="act">{I("arrow")}<div>{actxt}</div></div></div>')

def fsteps(steps):
    out = f'<div class="fsteps" style="--n:{len(steps)}">'
    for i, (lab, v, unit, p, w, pas, leak) in enumerate(steps):
        out += (f'<div class="fs{" leak" if leak else ""}"><div class="t"><span>{i+1:02d}</span><span class="p">{p}</span></div>'
                f'<div class="l">{lab}</div><div class="v"><b>{v}</b> {unit}</div><div class="bar"><i style="width:{max(w,1.5):.1f}%"></i></div>'
                f'<div class="pass"><span>{pas}</span></div></div>')
    return out + '</div>'

def recorrido(steps):
    out = '<div class="recorrido">'
    for i, (ic, n, l, c, cut) in enumerate(steps):
        g = ' grad-txt' if i == 0 else ''
        out += (f'<div class="rec{" cut" if cut else ""}"><div class="rs">{I(ic)}{i+1:02d}</div><div class="n{g}">{n}</div>'
                f'<div class="l">{l}</div><span class="c sm">{c}</span></div>')
    return out + '</div>'

def cn(icon, color, name, on, pill_icon, pill, text, btn='Configuración', extra=''):
    st = '<span class="cn-st on"><i></i>Conectado</span>' if on is True else (
        '<span class="cn-st off"><i></i>No conectado</span>' if on is False else f'<span class="cn-st off"><i></i>{on}</span>')
    bi = 'sliders' if btn == 'Configuración' else 'plug'
    return (f'<div class="cn"><div class="cn-h"><span class="cn-ic" style="--c:{color}">{I(icon)}</span><div><b>{name}</b>{st}</div></div>'
            f'<div class="cn-d"><span class="cn-pill">{I(pill_icon)}{pill}</span><p>{text}</p>{extra}</div>'
            f'<div class="cn-f"><button class="qcz" type="button">{I(bi)}{btn}</button></div></div>')

def cnsec(icon, title, sub, cards):
    return (f'<div class="cn-sec"><div class="cn-sh"><span class="cn-si">{I(icon)}</span><div><b>{title}</b><span>{sub}</span></div></div>'
            f'<div class="cn-g">{"".join(cards)}</div></div>')

def barchart(labels, series, ymax, shade=None, colors=None, legend_items=None, highlight_last=True, stacked=False, lbl_last=True):
    """series: list of lists. stacked: second series on top."""
    W, H, x0, y0, top = 1000, 230, 50, 206, 20
    n = len(labels); slot = (992 - x0) / n; bw = slot * .58
    out = f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" preserveAspectRatio="xMidYMid meet">'
    for k in range(5):
        v = ymax * k / 4; y = y0 - (y0 - top) * k / 4
        out += f'<line class="gl" x1="{x0}" x2="992" y1="{y:.1f}" y2="{y:.1f}"/><text x="44" y="{y+3:.1f}" text-anchor="end">{num(round(v))}</text>'
    for i in (shade or []):
        x = x0 + slot * i + 2
        out += (f'<rect x="{x:.1f}" y="12" width="{slot-4:.1f}" height="194" rx="4" fill="var(--crit)" opacity=".10"/>'
                f'<text x="{x+(slot-4)/2:.1f}" y="19" text-anchor="middle" style="fill:var(--crit);font-weight:700">sin procesar</text>')
    colors = colors or ['var(--vio)', 'var(--crit)']
    for i, lab in enumerate(labels):
        cx = x0 + slot * i + slot / 2; base = y0
        for si, s in enumerate(series):
            v = s[i]; h = (y0 - top) * v / ymax
            yb = base if stacked else y0
            op = '1' if (highlight_last and i == n - 1 and si == 0) else '.55'
            if stacked and si > 0: op = '.85'
            off = 0 if stacked or len(series) == 1 else (si - (len(series) - 1) / 2) * bw / len(series)
            w = bw if stacked or len(series) == 1 else bw / len(series)
            out += f'<rect x="{cx - w/2 + off:.1f}" y="{yb - h:.1f}" width="{w:.1f}" height="{h:.1f}" rx="3" fill="{colors[si]}" opacity="{op}"/>'
            if stacked: base = yb - h
        out += f'<text x="{cx:.1f}" y="224" text-anchor="middle">{lab}</text>'
    if lbl_last:
        tot = sum(s[-1] for s in series) if stacked else series[0][-1]
        out += f'<text class="lbl" x="{x0 + slot*(n-1) + slot/2:.1f}" y="{y0 - (y0-top)*tot/ymax - 4:.1f}" text-anchor="middle">{num(tot)}</text>'
    out += '</svg>'
    if legend_items:
        out += '<div class="chart-lg">' + ''.join(
            f'<span><i style="background:{c}"></i>{t}</span>' if c else f'<span>{t}</span>' for c, t in legend_items) + '</div>'
    return out

def fx(color, bg, icon, kind, title, found, fix, where):
    return (f'<div class="fx" style="--fx:{color};--fxb:{bg}"><div class="qcm"><span class="qcf">{I(icon)}</span><div>'
            f'<span class="qcn">{kind}</span><b>{title}</b></div></div><div class="qu"><span class="qbf">{I("eye")}Qué encontramos</span>'
            f'<p>{found}</p></div><div class="qu qbu"><span class="qbf">{I("wrench")}Arreglo</span><p>{fix}</p></div>'
            f'<div class="qco"><span class="qbv">{I("arrow")}{where}</span></div></div>')

def vcd(color, icon, title, sub, rows, q):
    fun = ''.join(f'<div class="vm"><span>{k}</span><i style="width:{w:.0f}%"></i><b>{v}</b></div>' for k, w, v in rows)
    vq = ''.join(f'<div data-s="{s}"><b>{b}</b><span>{t}</span></div>' for s, b, t in q)
    return (f'<div class="vcd"><div class="vcd-h"><span class="vcd-av" style="background:{color}">{I(icon)}</span><div><b>{title}</b>'
            f'<span>{sub}</span></div></div><div class="vcd-b"><div class="vcd-fun">{fun}</div><div class="vq">{vq}</div></div></div>')


# ---------- Citas (a voz de quien consulta) ----------
def vq(theme, n, unit, quote_txt, meta, act_who, act_txt, m=None):
    who = mc(m) if m else f'<span class="vq-who">{act_who}</span>'
    return (f'<div class="vqc"><div class="vqh"><span class="vqk">{theme}</span><span class="vqn"><b>{n}</b>{unit}</span></div>'
            f'<blockquote class="vqq">«{quote_txt}»</blockquote><div class="vqm">{I("building")}<span>{meta}</span></div>'
            f'<div class="vqa"><div class="vqal">{I("arrow")}Qué cambiar {who}</div><p>{act_txt}</p></div></div>')

# ---------- Núcleo de criterio comercial ----------
def nucleo(rows):
    """rows: (campo, desc, variable|None, carga, carga_icon, cov|None, lvlkey, estado)"""
    h = ('<div class="nuc"><div class="nuc-r nuc-hd"><span>Campo del núcleo</span><span>Variable en Prometheo</span><span>Lo carga</span>'
         '<span>Cobertura</span><span>Nivel</span><span>Estado</span></div>')
    for campo, desc, var, carga, ic, cov, lk, est in rows:
        v = f'<code class="nuc-var">{var}</code>' if var else '<span class="nuc-none">sin variable</span>'
        c = (f'<span class="nuc-cov"><span class="mtrk"><i style="width:{max(cov,2):.0f}%"></i></span><b>{num(cov)}%</b></span>'
             if cov is not None else '<span class="nuc-none">—</span>')
        h += (f'<div class="nuc-r"><div class="nuc-c"><b>{campo}</b><span>{desc}</span></div><div>{v}</div>'
              f'<div><span class="nuc-who">{I(ic)}{carga}</span></div><div>{c}</div><div>{lvl(lk)}</div><div class="nuc-e">{est}</div></div>')
    return h + '</div>'

# ---------- Mini barra con pista visible ----------
def mbar(p, cls=''):
    return f'<span class="mtrk{(" " + cls) if cls else ""}"><i style="width:{max(min(p,100),1.5):.1f}%"></i></span>'
