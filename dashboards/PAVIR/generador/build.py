"""Genera el tablero de Inteligencia Comercial de PAVIR (HTML autocontenido).

Uso:  python3 build.py   ->  ../Dashboard_Inteligencia_Comercial_-_Aurea_Hub_PAVIR.html
"""
import os
from css import CSS
from icons import sprite, ic
import data as D
from p_panorama import panorama, evolucion
from p_venta import ventacrm
from p_red import distribuidores, corredores
from p_mercado import demanda, criterio, insights
from p_marketing import metaads, googleads, email, whatsapp
from p_meta import metaprom, audiencias, integraciones

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "Dashboard_Inteligencia_Comercial_-_Aurea_Hub_PAVIR.html")

NAV = [
    ("Cómo venimos", "1", [("panorama", "grid", "Panorama", None), ("evolucion", "trend", "Evolución", None)]),
    ("A quién le vendemos", "2", [("ventacrm", "crm", "Venta · CRM", None), ("distrib", "building", "Distribuidores", None), ("corredores", "route", "Corredores", None)]),
    ("Qué pide el mercado", "3", [("demanda", "box", "Demanda de productos", None), ("criterio", "compass", "Criterio comercial", None)]),
    ("Qué trajo resultado", "4", [("insights", "bulb", "Insights", None), ("metaads", "mega", "Meta Ads", "var(--good)"), ("googleads", "google", "Google Ads", "var(--warn)"),
                                  ("email", "mail", "Email Marketing", "var(--src-mail)"), ("whatsapp", "wa", "WhatsApp Marketing", "var(--src-wpp)")]),
    ("Qué hacer con Meta", "5", [("metaprom", "meta", "Meta en Prometheo", None), ("audiencias", "users", "Audiencias", None)]),
    ("De dónde sale esto", "6", [("integraciones", "plug", "Integraciones", None)]),
]
TABS = [t for _, _, items in NAV for t, *_ in items]
SUBTABS = {"evo": ["ventas", "deuda", "tags", "cons"], "ins": ["anun", "conj", "com"]}


def minify(c):
    import re
    c = re.sub(r"/\*.*?\*/", "", c, flags=re.S)
    c = re.sub(r"\s*\n\s*", "", c)
    c = re.sub(r"\s*([{};,>])\s*", r"\1", c)
    return c


def dyn_css():
    out = []
    for t in TABS:
        out.append(f"#dn-{t}:checked~.shell .nav[data-t={t}]{{background:var(--grad);color:#fff;box-shadow:0 6px 16px -6px rgba(124,92,191,.6)}}")
        out.append(f"#dn-{t}:checked~.shell .nav[data-t={t}] svg.i{{color:#fff}}")
        out.append(f"#dn-{t}:checked~.shell .p-{t}{{display:block}}")
    out.append("#mode-simple:checked~.shell .mode label[for=mode-simple],#mode-adv:checked~.shell .mode label[for=mode-adv]{background:var(--grad);color:#fff}")
    pref = {"evo": "ev", "ins": "in"}
    for g, items in SUBTABS.items():
        p = pref[g]
        for s in items:
            out.append(f"#{p}-{s}:checked~.shell label[for={p}-{s}]{{background:var(--grad);color:#fff}}")
            out.append(f"#{p}-{s}:checked~.shell .st-{s}{{display:block}}")
    return "\n".join(out)


def radios():
    r = [f'<input type="radio" name="nav" id="dn-{t}" class="st"{" checked" if i == 0 else ""}>' for i, t in enumerate(TABS)]
    r += ['<input type="radio" name="mode" id="mode-simple" class="st" checked>', '<input type="radio" name="mode" id="mode-adv" class="st">']
    pref = {"evo": "ev", "ins": "in"}
    for g, items in SUBTABS.items():
        r += [f'<input type="radio" name="{g}" id="{pref[g]}-{s}" class="st"{" checked" if i == 0 else ""}>' for i, s in enumerate(items)]
    return "\n".join(r)


def sidebar():
    out = ['<aside class="side"><div class="brand"><div class="sph sph-bg"></div><div><b>PAVIR</b><span>Inteligencia Comercial</span></div></div>']
    for title, q, items in NAV:
        out.append(f'<div class="navlab"><span class="q">{q}</span>{title}</div>')
        for t, i, lab, dot in items:
            d = f'<span class="chch" style="background:{dot}"></span>' if dot else ""
            out.append(f'<label class="nav" data-t="{t}" for="dn-{t}">{ic(i)}{lab}{d}</label>')
    out.append(f'<div class="side-foot"><button class="themebtn" type="button" onclick="tgl()">{ic("sun", "i sun")}{ic("moon", "i moon")}<span>Tema claro / oscuro</span></button></div></aside>')
    return "".join(out)


def topbar(logo):
    upd = [("var(--src-pro)", "Prometheo", f"export {D.ACT}"), ("var(--src-erp)", "Producí", f"export {D.ACT}"), ("var(--src-meta)", "Meta Ads", f"export {D.ACT}"),
           ("var(--src-mail)", "Email", "28 sep 2026"), ("var(--src-wpp)", "WhatsApp", "29 sep 2026"), ("var(--src-goog)", "Google Ads", "pausado")]
    u = "".join(f'<span class="u"><span class="dt" style="background:{c}"></span>{n} <b>{d}</b></span>' for c, n, d in upd)
    return f'''<div class="topbar">
<div class="tb-l"><img class="tb-logo" src="{logo}" alt="AUREA Hub"><div class="hbrand"><span class="wm">PAVIR</span><span class="ic"><b>Inteligencia</b>Comercial</span></div></div>
<div class="tb-r"><span class="period">{ic("cal")}{D.PERIODO} <span>· vs {D.PREV}</span></span><span class="demo">{ic("info")}Demo · datos ilustrativos</span>
<div class="mode"><label for="mode-simple">{ic("rows")}Básico</label><label for="mode-adv">{ic("sliders")}Avanzado</label></div></div></div>
<div class="updbar">{ic("refresh", style="width:13px;height:13px")}Última actualización por fuente: {u}</div>
<div class="modehint bsc">{ic("rows")}<span><b>Modo básico:</b> lo esencial de cada pestaña, en palabras simples. Pasá a <b>Avanzado</b> para ver el detalle, los cruces y las siglas explicadas.</span></div>
<div class="modehint adv">{ic("sliders")}<span><b>Modo avanzado:</b> todo lo del básico, más el detalle técnico. Cada sigla se explica debajo del número.</span></div>'''


JS = r"""
(function(){try{var s=localStorage.getItem('pavir-theme');if(s)document.documentElement.setAttribute('data-theme',s);}catch(e){}})();
function tgl(){var r=document.documentElement,c=r.getAttribute('data-theme');var sd=window.matchMedia&&window.matchMedia('(prefers-color-scheme:dark)').matches;var n=c?(c==='dark'?'light':'dark'):(sd?'light':'dark');r.setAttribute('data-theme',n);try{localStorage.setItem('pavir-theme',n);}catch(e){}}
(function(){
  function sync(name,pre,sel,cls){var c=document.querySelector('input[name="'+name+'"]:checked');if(!c)return;var id=c.id.replace(pre,'');var els=document.querySelectorAll(sel);for(var i=0;i<els.length;i++){els[i].style.display=els[i].classList.contains(cls+id)?'block':'none';}}
  function all(){sync('nav','dn-','.panel','p-');sync('evo','ev-','.p-evolucion .stab','st-');sync('ins','in-','.p-insights .stab','st-');}
  function bind(n){var r=document.querySelectorAll('input[name="'+n+'"]');for(var i=0;i<r.length;i++){r[i].addEventListener('change',function(){all();if(this.name==='nav'){try{localStorage.setItem('pavir-tab',this.id);}catch(e){}window.scrollTo({top:0,behavior:'smooth'});}});}}
  ['nav','evo','ins'].forEach(bind);
  function init(){try{var t=localStorage.getItem('pavir-tab');var el=t&&document.getElementById(t);if(el){el.checked=true;}}catch(e){}all();}
  if(document.readyState!=='loading'){init();}else{document.addEventListener('DOMContentLoaded',init);}
})();
"""


def build():
    sphere = open(os.path.join(HERE, "assets", "sphere.txt")).read().strip()
    logo = open(os.path.join(HERE, "assets", "logo.txt")).read().strip()
    panels = [panorama(), evolucion(), ventacrm(), distribuidores(), corredores(), demanda(), criterio(), insights(),
              metaads(), googleads(), email(), whatsapp(), metaprom(), audiencias(), integraciones()]
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PAVIR · Inteligencia Comercial</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Arimo:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Newsreader:ital,opsz,wght@1,6..72,400;1,6..72,500;0,6..72,500&display=swap" rel="stylesheet">
<style>{minify(CSS)}
.sph-bg{{background-image:url({sphere})}}
{dyn_css()}
</style>
</head>
<body>
{sprite()}
{radios()}
<div class="shell">
{sidebar()}
<main class="main">
{topbar(logo)}
{"".join(panels)}
<div class="footer"><span class="orb"></span><b style="color:var(--ink2)">AUREA Hub</b> · Inteligencia Comercial sobre Prometheo · PAVIR · {D.PERIODO} · <b>datos ilustrativos (demo)</b>: la estructura es la real de Prometheo; las cifras, modeladas.</div>
</main>
</div>
<script>{JS}</script>
</body>
</html>'''
    # compactar espacios entre etiquetas
    import re
    html = re.sub(r">[ \t]*\n\s*<", "><", html)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(OUT, f"{len(html.encode('utf-8')) / 1024:.1f} KB")


if __name__ == "__main__":
    build()
