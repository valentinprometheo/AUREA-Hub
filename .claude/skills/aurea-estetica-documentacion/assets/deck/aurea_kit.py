# -*- coding: utf-8 -*-
"""
AUREA Hub — design kit.
Provides the canonical AUREA stylesheet, the inline-SVG icon set, the brand
assets (logo + sphere), HTML page wrappers, and a single-page PDF renderer.

Typical use:
    from aurea_kit import aurea_page, render_single_page_pdf, icon, check, LOGO, SPHERE
    inner = '''<section class="hero"> ... </section> <section class="sec"> ... </section>'''
    html = aurea_page("AUREA · Propuesta", inner)
    open("out.html","w",encoding="utf-8").write(html)
    render_single_page_pdf("out.html", "out.pdf")
"""
import os, json

_HERE = os.path.dirname(os.path.abspath(__file__))
def _read(p):
    with open(os.path.join(_HERE, p), encoding="utf-8") as f:
        return f.read().strip()

# Brand assets as data URIs (transparent PNG, ready to drop into <img src=...>)
LOGO   = _read("logo.txt")     # full AUREA wordmark + orb, transparent
SPHERE = _read("sphere.txt")   # iridescent glass sphere, perfect circular cut

# ---------------------------------------------------------------- FONTS
# Body + titles: Helvetica (Arimo = metric-compatible, embeds in PDF via Google Fonts).
# Italic accent: Fraunces italic is the stand-in for "Rischie" (Rischie is not on
# Google Fonts; to use it, add an @font-face with the .woff2 and swap the family).
FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Arimo:ital,wght@0,400;0,500;0,600;0,700;1,400;1,700'
 '&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300;1,9..144,400&display=swap" rel="stylesheet">')

# ---------------------------------------------------------------- ICONS (inline SVG)
def icon(name, extra="", sw="1.85"):
    """Return an inline <svg> for `name`. Sized by parent font-size (width:1em).
    Color follows currentColor. Never use an icon webfont — it fails to load
    on the client and renders as empty squares."""
    if name == "check":
        return check(extra)
    inner = _ICON_PATHS.get(name, '<circle cx="12" cy="12" r="4" fill="currentColor" stroke="none"/>')
    cls = "ic" + ((" " + extra) if extra else "")
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{inner}</svg>')

def check(extra="", circle="currentColor"):
    """Filled circular check. `circle` defaults to currentColor (so the parent's
    color drives it: purple for primary, green for success, etc.)."""
    cls = "ic" + ((" " + extra) if extra else "")
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none">'
            f'<circle cx="12" cy="12" r="10" fill="{circle}"/>'
            f'<path d="M8 12.5l2.5 2.5 5-5.5" stroke="#fff" stroke-width="2.1" '
            f'stroke-linecap="round" stroke-linejoin="round"/></svg>')

_ICON_PATHS = {
 "arrow-right": '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
 "world": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 6a3.2 3.2 0 0 1 0 6"/><path d="M21 20a6 6 0 0 0-4.5-5.4"/>',
 "users-group": '<circle cx="8" cy="9" r="2.4"/><circle cx="16" cy="9" r="2.4"/><path d="M3.5 19a4.5 4.5 0 0 1 9 0"/><path d="M12.5 19a4.5 4.5 0 0 1 8-3.6"/>',
 "briefcase": '<rect x="3" y="7.5" width="18" height="12.5" rx="2.2"/><path d="M8.5 7.5V6a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v1.5"/><path d="M3 13h18"/>',
 "headset": '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="2.5" y="13" width="3.8" height="6" rx="1.5"/><rect x="17.7" y="13" width="3.8" height="6" rx="1.5"/><path d="M20 19a4 4 0 0 1-4 3h-2"/>',
 "bolt": '<path d="M13 3L5 13.5h6l-1 7.5L19 10.5h-6z"/>',
 "trending-up": '<path d="M3 17l6-6 4 4 8-8"/><path d="M16 7h5v5"/>',
 "adjustments": '<path d="M4 6h9"/><path d="M17 6h3"/><circle cx="15" cy="6" r="2"/><path d="M4 12h3"/><path d="M11 12h9"/><circle cx="9" cy="12" r="2"/><path d="M4 18h9"/><path d="M17 18h3"/><circle cx="15" cy="18" r="2"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.6" fill="currentColor" stroke="none"/>',
 "scale": '<path d="M4 9V4h5"/><path d="M20 9V4h-5"/><path d="M4 15v5h5"/><path d="M20 15v5h-5"/>',
 "smile": '<circle cx="12" cy="12" r="9"/><path d="M9 10h.01"/><path d="M15 10h.01"/><path d="M8.5 14.5a4 4 0 0 0 7 0"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2.4"/><path d="M3.5 7.5l8.5 6l8.5-6"/>',
 "phone": '<path d="M5 4h3.5l1.8 4.5l-2.3 1.4a11 11 0 0 0 4.9 4.9l1.4-2.3l4.5 1.8V18a2 2 0 0 1-2 2A15 15 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 "map-pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/>',
 "route": '<circle cx="6" cy="18.5" r="2"/><circle cx="18" cy="5.5" r="2"/><path d="M8 18.5h6a3.5 3.5 0 0 0 0-7h-4a3.5 3.5 0 0 1 0-7h6"/>',
 "messages": '<path d="M4 4h13a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H9l-4 3v-3H4a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1z"/><path d="M8 8.5h7M8 11h4"/>',
 "refresh": '<path d="M20 11a8 8 0 0 0-13.7-5.6L4 7.5"/><path d="M4 4v3.5h3.5"/><path d="M4 13a8 8 0 0 0 13.7 5.6L20 16.5"/><path d="M20 20v-3.5h-3.5"/>',
 "robot": '<rect x="5" y="9" width="14" height="10" rx="3"/><path d="M12 9V5"/><circle cx="12" cy="4" r="1.2"/><circle cx="9.5" cy="13.5" r="1" fill="currentColor" stroke="none"/><circle cx="14.5" cy="13.5" r="1" fill="currentColor" stroke="none"/><path d="M9.8 16.5h4.4"/><path d="M3 13v2M21 13v2"/>',
 "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>',
 "coin": '<circle cx="12" cy="12" r="9"/><path d="M14.8 9.3a3 3 0 0 0-5.3 1.9c0 1.6 1.3 2.1 3 2.6s3 1 3 2.6a3 3 0 0 1-5.3 1.9"/><path d="M12 6.4v11.2"/>',
 "file-text": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/><path d="M9 12h6M9 15h6M9 18h4"/>',
 "receipt": '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/>',
 "bulb": '<path d="M9.3 16a5 5 0 1 1 5.4 0"/><path d="M9.3 16h5.4v1.8a2.7 2.7 0 0 1-5.4 0z"/><path d="M10.5 21h3"/>',
 "sparkles": '<path d="M12 4l1.6 4.4L18 10l-4.4 1.6L12 16l-1.6-4.4L6 10l4.4-1.6z"/><path d="M18.5 14.5l.6 1.6 1.6.6-1.6.6-.6 1.6-.6-1.6-1.6-.6 1.6-.6z" fill="currentColor" stroke="none"/>',
 "building-community": '<path d="M3 21h18"/><path d="M5 21V7l5-3v17"/><path d="M10 21V10l8-3v14"/><path d="M14 11h.01M14 14h.01M14 17h.01"/>',
 "building-store": '<path d="M3.5 9l1.4-4.5h14.2L20.5 9"/><path d="M4 9a2.4 2.4 0 0 0 4.8 0 2.4 2.4 0 0 0 5.6 0 2.4 2.4 0 0 0 4.8 0"/><path d="M5 9.5V21h14V9.5"/><path d="M9.5 21v-5.5h4V21"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "whatsapp": '<path d="M3 21l1.6-4.8A8 8 0 1 1 7.2 18.4z"/><circle cx="9.3" cy="12" r="1" fill="currentColor" stroke="none"/><circle cx="12.5" cy="12" r="1" fill="currentColor" stroke="none"/><circle cx="15.7" cy="12" r="1" fill="currentColor" stroke="none"/>',
}
ICON_NAMES = sorted(list(_ICON_PATHS.keys()) + ["check"])

# ---------------------------------------------------------------- STYLESHEET
AUREA_CSS = r"""
:root{
  --ink:#1F1B2E; --ink-2:#4B4660; --ink-3:#8783A0; --ink-4:#B5B1C7;
  --paper:#FFFFFF; --line:rgba(31,27,46,0.08); --line-2:rgba(31,27,46,0.14);
  --aurea-purple:#7C5CBF; --aurea-purple-deep:#5A3F94; --aurea-purple-50:#EDE7F8; --aurea-purple-soft:#F7F4FC;
  --aurea-blue:#5B8FD9; --aurea-blue-50:#E3EEFC; --aurea-green:#4CAF80; --aurea-green-50:#E1F5EA;
  --aurea-orange:#E8943A; --aurea-orange-50:#FFE5C2; --aurea-teal:#3FA89E; --aurea-coral:#F37D6E; --aurea-coral-50:#FDE3DE;
  --hel:'Arimo','Helvetica Neue',Helvetica,Arial,sans-serif;
  --accent:'Fraunces',serif;   /* italic accent; swap for Rischie when available */
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{font-family:var(--hel);color:var(--ink);line-height:1.5;-webkit-font-smoothing:antialiased;background:#FFFFFF;overflow-x:hidden}
.ic{width:1em;height:1em;display:inline-block;vertical-align:-0.14em;flex-shrink:0}

/* ---- full-bleed, website-style sections ---- */
.container{max-width:none;margin:0;padding:0}
.hero,.sec,.closer{position:relative;overflow:hidden;
  padding-left:max(26px,calc((100% - 1080px)/2));padding-right:max(26px,calc((100% - 1080px)/2))}
.hero{padding-top:60px;padding-bottom:54px}
.sec{padding-top:58px;padding-bottom:58px}
footer{padding-left:max(26px,calc((100% - 1080px)/2));padding-right:max(26px,calc((100% - 1080px)/2));padding-bottom:40px}
/* alternating brand-gradient bands (~15% — present but text stays readable) */
main > section:nth-of-type(even){background:linear-gradient(118deg, rgba(118,168,255,0.15) 0%, rgba(150,120,236,0.13) 46%, rgba(255,138,200,0.15) 100%)}
main > section:nth-of-type(odd){background:#FFFFFF}
main > section.hero{background:radial-gradient(ellipse 60% 56% at 82% 24%, rgba(140,175,255,0.22), transparent 60%),radial-gradient(ellipse 46% 50% at 97% 4%, rgba(255,160,210,0.18), transparent 60%),#FFFFFF}

/* ---- organic orb bullet (use before every eyebrow, not a plain circle) ---- */
.ob{width:15px;height:15px;flex-shrink:0;border-radius:58% 42% 56% 44% / 52% 58% 42% 48%;
  background:radial-gradient(circle at 32% 30%,#FFC9E6,#BBB2FF 38%,#83CDF1 66%,#7C5CBF);
  box-shadow:0 2px 7px rgba(124,92,191,.34);transform:rotate(-8deg)}

/* ---- type ---- */
.eyebrow{font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--aurea-purple);display:inline-flex;align-items:center;gap:9px;margin-bottom:14px}
.hero-eyebrows{display:flex;flex-direction:column;gap:6px;margin-bottom:26px}
.hero-eyebrows .eyebrow{margin:0}
h1{font-family:var(--hel);font-weight:700;font-size:clamp(34px,5vw,54px);line-height:1.05;letter-spacing:-.025em;color:var(--ink);margin-bottom:18px;max-width:900px;text-wrap:balance}
h1 em,.sec-head h2 em,.closer h2 em{font-family:var(--accent);font-style:italic;font-weight:300}
.lead{font-size:17px;line-height:1.55;color:var(--ink-2);max-width:760px;margin-bottom:14px}
.lead strong{font-weight:600;color:var(--ink)}
.sec-head{margin-bottom:28px}
.sec-head h2{font-family:var(--hel);font-weight:600;font-size:30px;line-height:1.16;letter-spacing:-.02em;color:var(--ink);max-width:840px;text-wrap:balance}
.sec-head p{margin-top:14px;font-size:15px;line-height:1.62;color:var(--ink-2);max-width:760px}
.sec-head p strong,.note strong{color:var(--ink);font-weight:600}
.note{font-size:14.5px;line-height:1.65;color:var(--ink-2)}

/* ---- highlight (brand "marker" underline area) ---- */
.hl{background:linear-gradient(120deg,rgba(124,92,191,.22),rgba(91,143,217,.18));border-radius:5px;padding:.04em .22em;-webkit-box-decoration-break:clone;box-decoration-break:clone;font-weight:600;color:var(--ink)}

/* ---- brand logo (transparent, lives on white) ---- */
.brand-lockup{margin-bottom:30px}
.hero-logo{width:250px;max-width:64%;height:auto;display:block}

/* ---- layout helpers ---- */
.split{display:grid;grid-template-columns:1.1fr .9fr;gap:34px;align-items:center}
.split.rev{grid-template-columns:.9fr 1.1fr}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.grid-4{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}

/* ---- cards ---- */
.card{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:24px 26px}
.card-h{display:flex;align-items:center;gap:12px;margin-bottom:12px}
.card-ic{width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,var(--aurea-purple),var(--aurea-blue));color:#fff;display:flex;align-items:center;justify-content:center;font-size:22px}
.card-h h3{font-size:19px;font-weight:700;letter-spacing:-.015em;color:var(--ink)}
.card p{font-size:13.5px;line-height:1.6;color:var(--ink-2)}
.card p strong{color:var(--ink);font-weight:600}
/* accent card: use the brand gradient to make ONE box stand out (minimalist, ~20%) */
.card.accent{background:linear-gradient(120deg, rgba(118,168,255,0.20) 0%, rgba(150,120,236,0.18) 48%, rgba(255,138,200,0.20) 100%);border:1px solid rgba(124,92,191,0.24);box-shadow:0 14px 34px -16px rgba(124,92,191,0.36)}

/* icon-chip card (icon + label + title + desc) */
.feat{background:#FFFFFF;border:1px solid var(--line);border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:10px}
.feat-ic{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,var(--aurea-purple),var(--aurea-blue));color:#fff;display:flex;align-items:center;justify-content:center;font-size:20px}
.feat-label{font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--aurea-purple)}
.feat-title{font-weight:700;font-size:17px;letter-spacing:-.015em;color:var(--ink);line-height:1.25}
.feat-desc{font-size:13px;line-height:1.55;color:var(--ink-2)}

/* checks list */
.checks{list-style:none;display:flex;flex-direction:column;gap:14px}
.checks li{display:flex;gap:12px;align-items:flex-start;font-size:15.5px;font-weight:600;color:var(--ink);line-height:1.4}
.checks li .ic{color:var(--aurea-purple);font-size:22px;margin-top:1px}

/* stats */
.stat{background:#FFFFFF;border:1px solid var(--line);border-radius:16px;padding:24px 18px;text-align:center;display:flex;flex-direction:column;gap:6px;align-items:center}
.stat-ic{width:42px;height:42px;border-radius:12px;background:var(--aurea-purple-50);color:var(--aurea-purple);display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:4px}
.stat-num{font-family:var(--hel);font-weight:800;font-size:30px;letter-spacing:-.03em;color:var(--ink)}
.stat-lbl{font-size:12px;color:var(--ink-2);font-weight:600;line-height:1.35}
/* hero figure for one focal metric (uses the vibrant brand gradient + white text) */
.focal{display:flex;align-items:center;justify-content:center;gap:20px;border-radius:18px;padding:22px;color:#fff;
  background:linear-gradient(110deg,#5B8FD9 0%,#7C5CBF 42%,#B06FC6 70%,#F3A2B6 100%);box-shadow:0 20px 46px -18px rgba(124,92,191,.6)}
.focal .big{font-family:var(--hel);font-weight:800;font-size:34px;letter-spacing:-.03em}
.focal .vic{width:42px;height:42px;border-radius:50%;background:rgba(255,255,255,.22);display:flex;align-items:center;justify-content:center;font-size:24px}
.focal .w{font-family:var(--accent);font-style:italic;font-weight:300;font-size:30px}

/* big stat rows (e.g. 69% / 31%) + gradient quote panel */
.bigstat{display:flex;gap:22px;align-items:baseline;padding:20px 0;border-top:1px solid var(--line)}
.bigstat:first-child{border-top:none;padding-top:4px}
.bs-num{font-family:var(--accent);font-weight:300;font-size:56px;line-height:.9;color:var(--ink);min-width:130px;letter-spacing:-.02em}
.bs-txt{font-size:15px;color:var(--ink-2);line-height:1.5}
.bs-txt strong{color:var(--ink);font-weight:600}
.quote-panel{background:linear-gradient(140deg,#CDBEEF 0%,#BCC6EC 46%,#EBC6DF 100%);border-radius:20px;padding:34px 32px;display:flex;flex-direction:column;justify-content:center;border:1px solid rgba(255,255,255,.5)}
.quote-panel .eyebrow{color:var(--aurea-purple-deep);margin-bottom:16px}
.quote-panel .q{font-family:var(--accent);font-style:italic;font-weight:300;font-size:21px;line-height:1.42;color:var(--ink)}
.quote-panel .q strong{font-weight:400;text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}

/* device frame (laptop/browser screenshot) + floating phone */
.device{border-radius:18px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 70px -28px rgba(31,27,46,.45);background:#fff}
.device-bar{display:flex;align-items:center;gap:7px;padding:11px 16px;background:#F1EFF7;border-bottom:1px solid var(--line)}
.device-bar i{width:10px;height:10px;border-radius:50%;display:block}
.device img{width:100%;display:block}
.phone-float{display:flex;justify-content:center;align-items:center}
.phone-float img{filter:drop-shadow(0 26px 44px rgba(31,27,46,.3))}
.device-wide{display:flex;justify-content:center}
.device-wide img{width:100%;max-width:780px;height:auto;filter:drop-shadow(0 26px 48px rgba(31,27,46,.16))}

/* table (roles / data) */
.atable-wrap{background:#FFFFFF;border:1px solid var(--line);border-radius:16px;overflow:hidden}
.atable{width:100%;border-collapse:collapse;font-size:12.5px}
.atable thead th{background:var(--ink);color:#fff;padding:13px 14px;text-align:left;font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.atable thead th:first-child{background:linear-gradient(135deg,var(--aurea-purple),var(--aurea-purple-deep))}
.atable tbody td{padding:13px 14px;vertical-align:top;border-top:1px solid var(--line);color:var(--ink-2);line-height:1.45}
.atable tbody td:first-child{font-weight:700;color:var(--ink);background:var(--aurea-purple-soft)}
.atable tbody td.muted{background:rgba(184,176,199,.10);color:var(--ink-3);font-style:italic}

/* numbered pipeline / stages */
.pipeline{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
.pipe-stage{border-radius:12px;padding:14px 14px 16px;display:flex;flex-direction:column;gap:6px;border:1px solid var(--aurea-purple-50)}
.pipe-stage .pipe-num{font-family:var(--accent);font-weight:300;font-size:18px;color:var(--aurea-purple);line-height:1}
.pipe-stage .pipe-name{font-size:13px;font-weight:700;color:var(--ink);letter-spacing:-.01em}
.pipe-stage .pipe-desc{font-size:11px;color:var(--ink-2);line-height:1.4}
.pipe-stage.s5{background:linear-gradient(135deg,var(--aurea-purple),var(--aurea-purple-deep));border-color:transparent;color:#fff}
.pipe-stage.s5 .pipe-num,.pipe-stage.s5 .pipe-desc{color:rgba(255,255,255,.85)}
.pipe-stage.s5 .pipe-name{color:#fff}

/* budget cards */
.budget-card{background:#FFFFFF;border:1px solid var(--line);border-radius:14px;padding:20px 22px;display:flex;flex-direction:column;gap:8px}
.budget-card.main{background:linear-gradient(135deg,#1F1B2E,#3E3556);color:#fff;border:none}
.budget-label{font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--aurea-purple)}
.budget-card.main .budget-label{color:#B8B0FF}
.budget-title{font-weight:700;font-size:15px;color:var(--ink)}
.budget-card.main .budget-title{color:#fff}
.budget-main-val{font-family:var(--accent);font-style:italic;font-weight:300;font-size:30px;color:#fff;letter-spacing:-.01em}
.budget-val{font-family:var(--hel);font-weight:700;font-size:22px;color:var(--ink);letter-spacing:-.02em}
.budget-when{font-size:11.5px;line-height:1.45;color:var(--ink-3)}
.budget-card.main .budget-when{color:rgba(255,255,255,.65)}

/* contact cards */
.contact-card{background:#FFFFFF;border:1px solid var(--line);border-radius:16px;padding:18px 20px;display:flex;align-items:center;gap:16px}
.contact-ic{width:48px;height:48px;border-radius:13px;background:var(--ink);color:#fff;display:flex;align-items:center;justify-content:center;font-size:22px}
.contact-l{font-size:15px;font-weight:700;color:var(--ink)}
.contact-v{font-size:13px;color:var(--ink-2);word-break:break-word}

/* logos row */
.logos{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:26px 46px;padding:26px 20px;background:rgba(255,255,255,.6);border:1px solid var(--line);border-radius:18px}
.logos img{height:40px;width:auto;filter:grayscale(1);opacity:.74}
.logos img.sq{height:50px}

/* decorative sphere: secondary, BEHIND content, never in front of text/cards */
.sphere-side{position:absolute;z-index:0;pointer-events:none}
.hero>*{position:relative;z-index:1}
.hero .sphere-side{z-index:0}
.sphere-hero{right:-120px;top:118px;width:208px;opacity:.82}
.sphere-side img{width:100%;display:block}

/* closer: sphere on one side, text right-aligned, on WHITE for impact */
.closer{background:#FFFFFF;display:grid;grid-template-columns:.85fr 1.15fr;gap:46px;align-items:center;padding-top:66px;padding-bottom:74px}
.closer .closer-sphere{display:flex;justify-content:center}
.closer .closer-sphere img{width:100%;max-width:270px;height:auto;filter:drop-shadow(0 22px 44px rgba(124,92,191,.28))}
.closer .closer-text{text-align:right}
.closer h2{font-family:var(--hel);font-weight:600;font-size:clamp(24px,3.2vw,32px);line-height:1.2;letter-spacing:-.02em;color:var(--ink);margin-bottom:14px;text-wrap:balance}
.closer p{font-size:14.5px;line-height:1.6;color:var(--ink-2)}
.closer p strong{color:var(--ink);font-weight:700}

/* footer */
footer{display:flex;justify-content:space-between;align-items:center;font-size:11px;color:var(--ink-3);flex-wrap:wrap;gap:10px;border-top:1px solid var(--line);padding-top:22px}
footer .fm{display:flex;align-items:center;gap:8px}
.mini-orb{width:14px;height:14px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#FFC2E0,#B8B0FF 35%,#7CC8F0 70%,#7C5CBF)}

@media(max-width:880px){
  .split,.split.rev,.grid-2,.grid-3,.grid-4,.pipeline,.closer{grid-template-columns:1fr}
  .grid-4,.grid-3{grid-template-columns:1fr 1fr}
  .closer .closer-text{text-align:center}
  .sphere-hero{display:none}
}
"""

# ---------------------------------------------------------------- PAGE WRAPPER
def aurea_page(title, inner_html, extra_css=""):
    """Wrap section HTML into a full AUREA document.
    `inner_html` should be the <section> blocks (hero, sec..., closer) + optional <footer>,
    placed directly; this wraps them in <main class="container">."""
    return ('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            f'<title>{title}</title>{FONT_LINK}'
            f'<style>{AUREA_CSS}\n{extra_css}</style></head><body>'
            f'<main class="container">{inner_html}</main></body></html>')

# ---------------------------------------------------------------- RENDER (screenshot + PDF)
# REGLA DEL PROYECTO: el entregable por defecto es el HTML. El PDF de una sola hoja
# se genera SOLO cuando el cliente lo aprueba, y SIEMPRE por el camino canonico de
# abajo (screenshot full-page -> img2pdf). NUNCA usar el motor de impresion de
# Chromium (page.pdf): rompe los gradientes (sobre todo en la segunda columna de
# los grids). Dep: pip install img2pdf  (y playwright + chromium).

def screenshot_html(html_path, png_path, width=1200, scale=2, settle_ms=1300):
    """Screenshot full-page de un HTML AUREA. Es el raster canonico del deck.
    Usalo para QA (revisar por chunks: tildes, huerfanas, alineaciones, iconos,
    contraste) y como fuente del PDF. width=1200, device_scale_factor=2."""
    from playwright.sync_api import sync_playwright
    url = "file://" + os.path.abspath(html_path)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": width, "height": 1000}, device_scale_factor=scale)
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_timeout(settle_ms)
        pg.screenshot(path=png_path, full_page=True)
        b.close()
    return png_path

def render_single_page_pdf(html_path, pdf_path, width=1200, scale=2):
    """PDF de una sola hoja por el camino CANONICO: screenshot full-page (Playwright,
    1200px, device_scale_factor=2) -> img2pdf (sin perdida, una pagina a la altura
    total). Preserva los gradientes tal cual se ven en pantalla.
    NO usa el motor de impresion de Chromium. Generar solo con aprobacion del cliente."""
    import tempfile, img2pdf
    fd, png = tempfile.mkstemp(suffix=".png"); os.close(fd)
    try:
        screenshot_html(html_path, png, width=width, scale=scale)
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(png))
    finally:
        if os.path.exists(png):
            os.remove(png)
    return pdf_path

def render_single_page_pdf_chromium(html_path, pdf_path, width=1200):
    """DEPRECADO. Usa el motor de impresion de Chromium (page.pdf): ROMPE los
    gradientes. Conservado solo como referencia historica; preferi siempre
    render_single_page_pdf() (screenshot + img2pdf)."""
    from playwright.sync_api import sync_playwright
    url = "file://" + os.path.abspath(html_path)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": width, "height": 1000}, device_scale_factor=2)
        pg.emulate_media(media="screen")
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_timeout(1200)
        H = pg.evaluate("Math.ceil(document.body.scrollHeight)")
        pg.pdf(path=pdf_path, width=f"{width}px", height=f"{H+2}px",
               print_background=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
        b.close()
    return pdf_path

def eyebrow(text):
    """Eyebrow with the organic orb bullet (always use this, not a bare label)."""
    return f'<span class="eyebrow"><span class="ob"></span>{text}</span>'
