import json, re, sys
sys.path.insert(0, '.')
from lib import *
D = json.load(open('D.json'))
EDFAN = '/root/.claude/uploads/5cace1cd-6515-5715-a2db-3fed9a0ee26e/661eb56d-Aurea_Hub_-_IC_Dashboard_-_EDFAN_Real_Estate_Real.html'
src_html = open(EDFAN, encoding='utf-8').read()

# ---------- cabeza: CSS + iconos del tablero EDFAN, sin cambios de diseño ----------
head_end = src_html.find('<input type="radio" name="nav"')
HEAD = src_html[:head_end]
HEAD = HEAD.replace('<title>Aurea Hub - IC - Tablero</title>', '<title>TKVA · Inteligencia Comercial</title>')
LOGO = re.search(r'<img class="tb-logo" src="(data:[^"]+)"', src_html).group(1)
EXTRA_CSS = '''<style>
.d-good{color:var(--good)}
.mc{display:inline-flex;align-items:center;font-size:9px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:3px 8px;border-radius:20px;white-space:nowrap;border:1px solid transparent}
.mc-s{background:#E3F4E8;color:#1E6B3A;border-color:#BFE3CB}
.mc-p{background:#E9E7FB;color:#3F3A9E;border-color:#CFCAF5}
[data-theme=dark] .mc-s{background:#13301D;color:#8FD3A4;border-color:#22502F}
[data-theme=dark] .mc-p{background:#26234A;color:#B9B4F2;border-color:#3A3570}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .mc-s{background:#13301D;color:#8FD3A4;border-color:#22502F}:root:not([data-theme=light]) .mc-p{background:#26234A;color:#B9B4F2;border-color:#3A3570}}
.mcl{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;font-size:11.5px;color:var(--ink3);margin:-4px 0 14px}
.mcl b{color:var(--ink2);font-size:11px;letter-spacing:.06em;text-transform:uppercase;margin-right:2px}
.mcl span:not(.mc){margin-right:10px}
.qbg .mc{margin-left:2px}
table.tt th,table.tt td{text-align:left!important;white-space:normal;vertical-align:top}
table.tt td{line-height:1.45}
.tt td .mc{white-space:nowrap}
.pm-done{background:var(--good)!important}
.pm-done svg.i{width:20px;height:20px;color:#fff}
.pm.pm-ok{border-left:4px solid var(--good)}
.okband{display:flex;gap:14px;align-items:flex-start;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--good);border-radius:var(--r-l);box-shadow:var(--shadow);padding:16px 18px;margin-bottom:16px}
.okband .okic{flex:0 0 auto;width:40px;height:40px;border-radius:12px;background:var(--good);display:flex;align-items:center;justify-content:center}
.okband .okic svg.i{width:22px;height:22px;color:#fff}
.okband .okk{font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--good)}
.okband b.okt{display:block;font-size:16px;margin:3px 0 4px;color:var(--ink)}
.okband p{font-size:12.5px;color:var(--ink2);line-height:1.5}
.okband .okf{display:flex;flex-wrap:wrap;gap:6px;margin-top:9px}
.cvtabs{margin-top:4px}
.vsplit{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-bottom:16px}
.vsplit .vs{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-l);box-shadow:var(--shadow);padding:16px 18px;border-top:3px solid var(--vsc)}
.vsplit .vs .k{font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--vsc)}
.vsplit .vs b.t{display:block;font-size:22px;margin:4px 0 2px;color:var(--ink)}
.vsplit .vs p{font-size:12px;color:var(--ink3);line-height:1.5}
@media (max-width:760px){.vsplit{grid-template-columns:1fr}}
#cv-ia:checked~.shell label[for=cv-ia],#cv-meta:checked~.shell label[for=cv-meta]{background:var(--grad);color:#fff}
#dn-reporte:checked~.shell .nav[data-t=reporte]{background:var(--grad);color:#fff;box-shadow:0 6px 16px -6px rgba(124,92,191,.6)}
#dn-reporte:checked~.shell .nav[data-t=reporte] svg.i{color:#fff}
#dn-reporte:checked~.shell .p-reporte{display:block}
#rw-w1:checked~.shell label[for=rw-w1]{background:var(--grad);color:#fff}
#rw-w1:checked~.shell .st-w1{display:block}
#rw-w2:checked~.shell label[for=rw-w2]{background:var(--grad);color:#fff}
#rw-w2:checked~.shell .st-w2{display:block}
#rw-w3:checked~.shell label[for=rw-w3]{background:var(--grad);color:#fff}
#rw-w3:checked~.shell .st-w3{display:block}
#rw-w4:checked~.shell label[for=rw-w4]{background:var(--grad);color:#fff}
#rw-w4:checked~.shell .st-w4{display:block}
#cv-ia:checked~.shell .st-ia{display:block}
#cv-meta:checked~.shell .st-meta{display:block}
</style>'''
HEAD = HEAD + EXTRA_CSS

TABS = ['panorama', 'reporte', 'evolucion', 'ventacrm', 'vendedores', 'distrib', 'corredores', 'demanda', 'criterio',
        'insights', 'metaprom', 'tokens', 'audiencias', 'integraciones']
radios = ''.join(f'<input type="radio" name="nav" id="dn-{t}" class="st"{" checked" if t=="panorama" else ""}>' for t in TABS)
radios += ('<input type="radio" name="mode" id="mode-simple" class="st" checked><input type="radio" name="mode" id="mode-adv" class="st">'
           '<input type="radio" name="evo" id="ev-ventas" class="st" checked><input type="radio" name="evo" id="ev-deuda" class="st">'
           '<input type="radio" name="evo" id="ev-tags" class="st"><input type="radio" name="evo" id="ev-cons" class="st">'
           '<input type="radio" name="ins" id="in-anun" class="st" checked><input type="radio" name="ins" id="in-conj" class="st"><input type="radio" name="ins" id="in-com" class="st">'
           '<input type="radio" name="cv" id="cv-ia" class="st" checked><input type="radio" name="cv" id="cv-meta" class="st">'
           '<input type="radio" name="rw" id="rw-w1" class="st"><input type="radio" name="rw" id="rw-w2" class="st"><input type="radio" name="rw" id="rw-w3" class="st"><input type="radio" name="rw" id="rw-w4" class="st" checked>')

def nav(t, icon, label): return f'<label class="nav" data-t="{t}" for="dn-{t}">{I(icon)}{label}</label>'
def navlab(n, t): return f'<div class="navlab"><span class="q">{n}</span>{t}</div>'

SIDE = ('<div class="shell"><aside class="side"><div class="brand"><div class="sph sph-bg"></div><div><b>TKVA</b><span>Inteligencia Comercial</span></div></div>'
        + navlab(1, 'Cómo venimos') + nav('panorama', 'grid', 'Panorama') + nav('reporte', 'ledger', 'Reporte comercial') + nav('evolucion', 'trend', 'Evolución')
        + navlab(2, 'A quién le vendemos') + nav('ventacrm', 'crm', 'Venta · CRM') + nav('vendedores', 'user', 'Vanesa y el agente')
        + nav('distrib', 'building', 'Proyectos') + nav('corredores', 'users', 'Inmobiliarias y proveedores')
        + navlab(3, 'Qué pide el mercado') + nav('demanda', 'box', 'Demanda') + nav('criterio', 'compass', 'Criterio comercial')
        + navlab(4, 'Qué trajo resultado') + nav('insights', 'bulb', 'Insights y accionables') + nav('metaprom', 'meta', 'Meta · anuncios en Prometheo')
        + navlab(5, 'Qué hago ahora') + nav('tokens', 'bolt', 'Consumo variable CRM') + nav('audiencias', 'users', 'Audiencias')
        + navlab(6, 'De dónde sale esto') + nav('integraciones', 'plug', 'Integraciones')
        + f'<div class="side-foot"><button class="themebtn" type="button" onclick="tgl()"><svg class="i sun"><use href="#i-sun"/></svg>'
          f'<svg class="i moon"><use href="#i-moon"/></svg><span>Tema claro / oscuro</span></button></div></aside>')

TOP = (f'<main class="main"><div class="topbar"><div class="tb-l"><img class="tb-logo" src="{LOGO}" alt="AUREA Hub">'
       '<div class="hbrand"><span class="wm">TKVA</span><span class="ic"><b>Inteligencia</b>Comercial</span></div></div>'
       f'<div class="tb-r"><span class="period">{I("cal")}22 jul – 14 oct 2026 <span>· octubre comparado con septiembre</span></span>'
       f'<span class="real">{I("checkc")}Datos reales · Prometheo</span>'
       f'<div class="mode"><label for="mode-simple">{I("rows")}Básico</label><label for="mode-adv">{I("sliders")}Avanzado</label></div></div></div>'
       f'<div class="updbar"><svg class="i" style="width:13px;height:13px"><use href="#i-refresh"/></svg>Última actualización por fuente: '
       '<span class="u"><span class="dt" style="background:var(--src-pro)"></span>Prometheo <b>export 14 oct 2026</b></span>'
       '<span class="u"><span class="dt" style="background:var(--good)"></span>Panel de consumo <b>ago · sep · oct al 14</b></span>'
       '<span class="u"><span class="dt" style="background:var(--warn)"></span>IA del agente <b>sin procesar 29/08 – 15/09</b></span>'
       '<span class="u"><span class="dt" style="background:var(--good)"></span>Tokko <b>campos en el export de Prometheo</b></span>'
       '<span class="u"><span class="dt" style="background:var(--ink4)"></span>Meta Ads <b>sin export</b></span>'
       '<span class="u"><span class="dt" style="background:var(--ink4)"></span>Formularios LT · Go High Level <b>no entran solos</b></span>'
       '<span class="u"><span class="dt" style="background:var(--ink4)"></span>Factura de Meta <b>sin fuente</b></span></div>'
       f'<div class="modehint bsc">{I("rows")}<span><b>Modo básico:</b> lo esencial de cada pestaña, en palabras simples. Pasá a <b>Avanzado</b> para ver el detalle, los cruces y las definiciones.</span></div>'
       f'<div class="modehint adv">{I("sliders")}<span><b>Modo avanzado:</b> todo lo del básico, más el detalle técnico: bases, coberturas y cruces.</span></div>')

# ---------- números base ----------
M = {m['m']: m for m in D['months']}
jul, ago, sep, oct_ = M['2026-07'], M['2026-08'], M['2026-09'], M['2026-10']
CAL_S, CAL_A = D['calif']
B = D['B']
G = D['gap']
CALDEF = ('<b>Calificado (criterio EDFAN, aplicado a TKVA)</b>: conversó y cumple los dos obligatorios (proyecto o zona que TKVA '
          'comercializa, y una tipología que existe) más al menos 2 de los 4 que suman (intención de compra, finalidad, presupuesto o forma '
          'de pago, estado de obra compatible). Rango: lectura estricta (tipología única declarada, capacidad de pago declarada) y amplia.')
WEEKS = D['weeks']
wl = [w['wk'] for w in WEEKS]
SHADE = [i for i, w in enumerate(WEEKS) if w['wk'] in ('24/08', '31/08', '07/09', '14/09')]

def cal_rate(m): return pct(m['cal'], m['b'])

exec(open('tabs1.py', encoding='utf-8').read())
exec(open('tabs2.py', encoding='utf-8').read())

FOOT = ('<div class="qbd" style="text-align:center;margin:28px 0 8px">AUREA Hub · Inteligencia Comercial para TKVA · Export de Prometheo al 14/10/2026 · '
        'Panel de consumo de Prometheo (ago–oct) · Ningún número suma fuentes distintas.</div></main></div>')
tail_start = src_html.rfind('<script>', 0, src_html.rfind('<script>'))
SCRIPT = src_html[tail_start:]
SCRIPT = SCRIPT.replace("edfan-theme", "tkva-theme").replace("edfan-tab", "tkva-tab").replace("edfan-trk-", "tkva-trk-")
SCRIPT = SCRIPT.replace("['nav','evo','ins'].forEach(bind);", "['nav','evo','ins','cv','rw'].forEach(bind);")
SCRIPT = SCRIPT.replace("sync('ins','in-','.p-insights .stab','st-');}", "sync('ins','in-','.p-insights .stab','st-');sync('cv','cv-','.p-tokens .stab','st-');sync('rw','rw-','.p-reporte .stab','st-');}")
assert "'cv'" in SCRIPT and "sync('cv'" in SCRIPT

out = HEAD + radios + SIDE + TOP + ''.join(PANELS) + FOOT + SCRIPT
open('/home/user/AUREA-Hub/tableros-ic/tkva/IC_Dashboard_TKVA.html', 'w', encoding='utf-8').write(out)
print('ok', len(out.encode()))
