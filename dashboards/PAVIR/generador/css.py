"""Hoja de estilos del tablero de IC de PAVIR.

Tokens de marca AUREA (violeta, azul, rosa; Arimo + Newsreader) y componentes
compartidos por todas las pestañas. La esfera se define una sola vez como fondo.
"""

CSS = r"""
:root{
  --bg1:#E9E4F4;--bg2:#F4F2FA;
  --surface:#fff;--surface2:#FAF9FD;--inset:#F1EEF8;
  --glass:rgba(255,255,255,.62);--glass-brd:rgba(255,255,255,.7);
  --ink:#1E1A2E;--ink2:#4A4560;--ink3:#6F6888;--ink4:#9C94B6;
  --line:rgba(30,22,60,.11);--line2:rgba(30,22,60,.06);
  --vio:#7C5CBF;--blu:#5B8FD9;--pnk:#C77AA8;
  --vio-soft:#EDE7F9;--blu-soft:#E4EDFB;--pnk-soft:#F7E7F0;
  --grad:linear-gradient(103deg,#7C5CBF 0%,#5B8FD9 52%,#C77AA8 100%);
  --grad-soft:linear-gradient(135deg,#F1EBFB 0%,#E7EFFB 52%,#FAEBF3 100%);
  --good:#2F9469;--good-bg:#E3F3EA;--good-ink:#22714F;
  --warn:#B5751F;--warn-bg:#FBF0DD;--warn-ink:#8A5512;
  --crit:#D65A47;--crit-bg:#FBE8E4;--crit-ink:#A23E2B;
  --st-ok:#1E8E57;--st-warn:#F0B429;--st-warn-ink:#3D2B00;--st-bad:#D3362F;--st-off:#8C86A3;
  --src-pro:#2F9469;--src-erp:#A0612A;--src-meta:#4F73C4;--src-calc:#7C5CBF;--src-wpp:#1F9E7E;--src-mail:#B4649B;--src-goog:#D97706;
  --mejora:#2F9469;
  --r-s:12px;--r-m:16px;--r-l:20px;--r-xl:24px;
  --hel:'Arimo',system-ui,-apple-system,'Segoe UI',sans-serif;
  --serif:'Newsreader',Georgia,'Times New Roman',serif;
  --shadow:0 1px 2px -1px rgba(40,26,80,.10),0 8px 24px -12px rgba(70,44,130,.20);
  --shadow-lg:0 1px 2px -1px rgba(40,26,80,.10),0 18px 46px -18px rgba(70,44,130,.34);
}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){
  --bg1:#141225;--bg2:#1B1830;--surface:#221F36;--surface2:#282540;--inset:#1C1930;
  --glass:rgba(42,38,66,.6);--glass-brd:rgba(255,255,255,.08);
  --ink:#F2EFFA;--ink2:#CBC5E0;--ink3:#A39DBE;--ink4:#7A7398;
  --line:rgba(255,255,255,.11);--line2:rgba(255,255,255,.06);
  --vio-soft:#2C2550;--blu-soft:#22304F;--pnk-soft:#3A2740;
  --grad-soft:linear-gradient(135deg,#2A2350 0%,#22304F 52%,#3A2740 100%);
  --good:#54B98C;--good-bg:#1B3A2C;--good-ink:#86D8B1;
  --warn:#D89A47;--warn-bg:#3A2E1A;--warn-ink:#EBC07E;
  --crit:#E67A66;--crit-bg:#3B2320;--crit-ink:#F3A592;
  --st-ok:#2FAE6E;--st-bad:#E5534B;--st-off:#6F6990;
  --shadow:0 0 0 1px rgba(255,255,255,.07),0 14px 40px -20px rgba(0,0,0,.6);
  --shadow-lg:0 0 0 1px rgba(255,255,255,.08),0 22px 60px -22px rgba(0,0,0,.7);
}}
:root[data-theme=dark]{
  --bg1:#141225;--bg2:#1B1830;--surface:#221F36;--surface2:#282540;--inset:#1C1930;
  --glass:rgba(42,38,66,.6);--glass-brd:rgba(255,255,255,.08);
  --ink:#F2EFFA;--ink2:#CBC5E0;--ink3:#A39DBE;--ink4:#7A7398;
  --line:rgba(255,255,255,.11);--line2:rgba(255,255,255,.06);
  --vio-soft:#2C2550;--blu-soft:#22304F;--pnk-soft:#3A2740;
  --grad-soft:linear-gradient(135deg,#2A2350 0%,#22304F 52%,#3A2740 100%);
  --good:#54B98C;--good-bg:#1B3A2C;--good-ink:#86D8B1;
  --warn:#D89A47;--warn-bg:#3A2E1A;--warn-ink:#EBC07E;
  --crit:#E67A66;--crit-bg:#3B2320;--crit-ink:#F3A592;
  --st-ok:#2FAE6E;--st-bad:#E5534B;--st-off:#6F6990;
  --shadow:0 0 0 1px rgba(255,255,255,.07),0 14px 40px -20px rgba(0,0,0,.6);
  --shadow-lg:0 0 0 1px rgba(255,255,255,.08),0 22px 60px -22px rgba(0,0,0,.7);
}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
body{font-family:var(--hel);color:var(--ink);min-height:100vh;background:
  radial-gradient(1100px 620px at 82% -8%,rgba(124,92,191,.16),transparent 60%),
  radial-gradient(900px 560px at 5% 0%,rgba(91,143,217,.13),transparent 55%),
  linear-gradient(180deg,var(--bg1),var(--bg2) 46%)}
em{font-family:var(--serif);font-style:italic;font-weight:400}
b,strong{font-weight:700}
code{font-family:ui-monospace,'SFMono-Regular',Menlo,monospace;font-size:.92em;background:var(--inset);padding:1px 5px;border-radius:5px;color:var(--ink2)}
.tnum{font-variant-numeric:tabular-nums}
img{max-width:100%;display:block}
button{font-family:inherit}
svg.i{width:16px;height:16px;flex-shrink:0;display:inline-block;vertical-align:middle}
summary{list-style:none;cursor:pointer}summary::-webkit-details-marker{display:none}
.st{position:absolute;width:0;height:0;opacity:0;pointer-events:none}
.sph-bg{background-repeat:no-repeat;background-position:center;background-size:contain}
.grad-txt{background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}

/* ===== shell ===== */
.shell{display:flex;gap:18px;max-width:1380px;margin:0 auto;padding:18px 20px 40px;align-items:flex-start}
.side{position:sticky;top:18px;flex:0 0 228px;width:228px;align-self:flex-start;background:var(--glass);border:1px solid var(--glass-brd);border-radius:var(--r-xl);box-shadow:var(--shadow);backdrop-filter:blur(14px) saturate(1.3);-webkit-backdrop-filter:blur(14px) saturate(1.3);padding:14px 12px;display:flex;flex-direction:column;gap:3px;height:calc(100vh - 36px);overflow-y:auto;overscroll-behavior:contain;scrollbar-width:thin}
.brand{display:flex;align-items:center;gap:11px;padding:4px 8px 14px;margin-bottom:4px;border-bottom:1px solid var(--line2)}
.brand .sph{width:36px;height:36px;flex-shrink:0;filter:drop-shadow(0 4px 10px rgba(124,92,191,.35))}
.brand b{font-size:15px;font-weight:700;letter-spacing:-.02em;display:block;line-height:1.1}
.brand span{font-size:9.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--ink3)}
.navlab{display:flex;align-items:center;gap:7px;font-size:8.8px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--ink4);padding:12px 10px 5px}
.navlab .q{width:15px;height:15px;border-radius:5px;background:var(--inset);color:var(--ink3);display:inline-flex;align-items:center;justify-content:center;font-size:8.5px;letter-spacing:0}
.nav{display:flex;align-items:center;gap:10px;padding:8px 11px;border-radius:var(--r-s);cursor:pointer;font-size:12.8px;font-weight:600;color:var(--ink2);transition:background .14s,color .14s;user-select:none}
.nav svg.i{width:17px;height:17px;color:var(--ink3)}
.nav:hover{background:var(--inset)}
.nav .chch{margin-left:auto;width:7px;height:7px;border-radius:50%;flex-shrink:0}
.side-foot{margin-top:auto;padding-top:12px;border-top:1px solid var(--line2)}
.themebtn{display:flex;align-items:center;gap:9px;width:100%;padding:9px 11px;border-radius:var(--r-s);border:1px solid var(--line);background:var(--surface);color:var(--ink2);font-size:12px;font-weight:600;cursor:pointer}
.themebtn:hover{border-color:var(--vio)}
.themebtn .moon{display:none}
[data-theme=dark] .themebtn .sun{display:none}[data-theme=dark] .themebtn .moon{display:inline-block}
.main{flex:1 1 auto;min-width:0;max-width:100%}
.panel{display:none;min-width:0;animation:fade .25s ease-out}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.panel{animation:none}}

/* ===== topbar ===== */
.topbar{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:14px}
.tb-l{display:flex;align-items:center;gap:13px;min-width:0}
.tb-logo{height:26px;width:auto}
.hbrand{display:flex;align-items:center;gap:14px}
.hbrand .wm{font-size:36px;font-weight:800;letter-spacing:.01em;line-height:.85;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.hbrand .ic{font-family:var(--serif);font-style:italic;font-weight:500;font-size:19px;color:var(--ink2);border-left:2px solid var(--line);padding-left:14px;line-height:1.05}
.hbrand .ic b{display:block;font-family:var(--hel);font-style:normal;font-size:10px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:var(--vio)}
.tb-r{display:flex;align-items:center;gap:10px;margin-left:auto;flex-wrap:wrap}
.period{display:inline-flex;align-items:center;gap:7px;font-size:11.5px;font-weight:700;color:var(--ink2);background:var(--surface);border:1px solid var(--line);border-radius:var(--r-s);padding:8px 12px}
.period svg.i{color:var(--vio);width:15px;height:15px}
.period span{font-weight:500;color:var(--ink3)}
.demo{display:inline-flex;align-items:center;gap:6px;font-size:9.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--warn-ink);background:var(--warn-bg);border:1px dashed color-mix(in srgb,var(--warn) 55%,transparent);border-radius:20px;padding:5px 10px}
.demo svg.i{width:13px;height:13px}
.mode{display:inline-flex;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-s);padding:3px;gap:2px}
.mode label{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:700;color:var(--ink3);padding:7px 13px;border-radius:9px;cursor:pointer;white-space:nowrap}
.mode label svg.i{width:14px;height:14px}
.updbar{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;margin:-4px 0 14px;font-size:10.5px;color:var(--ink3)}
.updbar .u{display:inline-flex;align-items:center;gap:6px}
.updbar .u b{color:var(--ink2);font-weight:600}
.updbar .dt{width:7px;height:7px;border-radius:50%}
.modehint{display:flex;align-items:center;gap:10px;font-size:11.5px;color:var(--ink3);background:var(--surface);border:1px solid var(--line);border-radius:var(--r-s);padding:8px 12px;margin-bottom:14px}
.modehint svg.i{color:var(--vio)}
.modehint b{color:var(--ink2)}

/* ===== mode visibility: Básico muestra .bsc, Avanzado muestra .adv ===== */
#mode-simple:checked~.shell .adv{display:none!important}
#mode-adv:checked~.shell .bsc{display:none!important}

/* ===== common ===== */
.sec-head{margin:28px 0 14px}
.sec-head:first-child{margin-top:6px}
.eyebrow{display:flex;align-items:center;gap:9px;font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--ink3);margin-bottom:9px;flex-wrap:wrap}
.eb-orb{width:15px;height:15px;border-radius:50%;background:var(--grad);box-shadow:0 2px 6px -1px rgba(124,92,191,.5);flex-shrink:0}
h1.sec{font-size:27px;font-weight:700;letter-spacing:-.02em;line-height:1.1;text-wrap:balance}
h1.sec em{font-weight:400}
h2.sub{font-size:19px;font-weight:700;letter-spacing:-.015em;line-height:1.2;margin-bottom:4px}
h2.sub em{font-weight:400}
.lead{font-size:13px;color:var(--ink3);max-width:800px;line-height:1.55;margin-top:8px;text-wrap:pretty}
.lead b{color:var(--ink2);font-weight:600}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m);box-shadow:var(--shadow)}
.pad{padding:18px 20px}
.ghdr{display:flex;align-items:center;gap:8px;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--ink2);margin-bottom:13px;flex-wrap:wrap}
.ghdr>svg.i{color:var(--vio);width:16px;height:16px}
.ghdr .r{margin-left:auto;font-size:10.5px;font-weight:600;letter-spacing:0;text-transform:none;color:var(--ink3);display:inline-flex;align-items:center;gap:6px}
.note{font-size:11.5px;color:var(--ink3);line-height:1.5;margin-top:12px}
.note b{color:var(--ink2)}
.g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.g4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.gstart{align-items:start}
.span2{grid-column:span 2}.spanall{grid-column:1/-1}
.mt{margin-top:14px}.mt2{margin-top:22px}

/* chips */
.src{display:inline-flex;align-items:center;gap:4px;font-size:8.6px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:2px 7px 2px 5px;border-radius:20px;color:#fff;white-space:nowrap;vertical-align:middle;line-height:1.5}
.src svg.i{width:11px;height:11px;color:#fff}
.s-pro{background:var(--src-pro)}.s-erp{background:var(--src-erp)}.s-meta{background:var(--src-meta)}.s-calc{background:var(--src-calc)}.s-wpp{background:var(--src-wpp)}.s-mail{background:var(--src-mail)}.s-goog{background:var(--src-goog)}
.lvl{display:inline-flex;align-items:center;gap:4px;font-size:8.6px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:2px 7px;border-radius:20px;white-space:nowrap;border:1px solid;vertical-align:middle;line-height:1.4}
.lvl svg.i{width:10px;height:10px}
.l-hecho{color:var(--good-ink);border-color:color-mix(in srgb,var(--good) 40%,transparent);background:var(--good-bg)}
.l-senal{color:var(--src-meta);border-color:color-mix(in srgb,var(--blu) 40%,transparent);background:var(--blu-soft)}
.l-indicio{color:var(--warn-ink);border-color:color-mix(in srgb,var(--warn) 40%,transparent);background:var(--warn-bg)}
.l-proy{color:var(--vio);border-color:color-mix(in srgb,var(--vio) 45%,transparent);background:transparent;border-style:dashed}
.l-est{color:var(--ink3);border-color:var(--line);background:var(--surface2);border-style:dashed}
.own{display:inline-flex;align-items:center;gap:4px;font-size:8.6px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:2px 7px;border-radius:20px;white-space:nowrap;line-height:1.5}
.o-mkt{background:var(--blu-soft);color:var(--src-meta)}.o-ven{background:var(--good-bg);color:var(--good-ink)}.o-cob{background:var(--crit-bg);color:var(--crit-ink)}.o-aurea{background:var(--vio-soft);color:var(--vio)}
.chip{display:inline-flex;align-items:center;gap:5px;font-size:10.5px;font-weight:600;color:var(--ink2);background:var(--surface2);border:1px solid var(--line);border-radius:20px;padding:4px 10px;white-space:nowrap}
.chip svg.i{width:12px;height:12px;color:var(--ink3)}
.base{display:inline-flex;align-items:center;gap:5px;font-size:10.5px;font-weight:600;color:var(--ink3)}
.base svg.i{width:12px;height:12px}

/* delta */
.delta{display:inline-flex;align-items:center;gap:3px;font-size:11px;font-weight:700;white-space:nowrap}
.delta svg.i{width:12px;height:12px}
.d-good{color:var(--good)}.d-bad{color:var(--crit)}.d-flat{color:var(--ink3)}

/* estados alto contraste */
.est{display:inline-flex;align-items:center;gap:5px;font-size:10.5px;font-weight:800;padding:4px 10px 4px 7px;border-radius:20px;white-space:nowrap;line-height:1.2}
.est svg.i{width:13px;height:13px;color:inherit!important}
.est.ok{background:var(--st-ok);color:#fff}
.est.warn{background:var(--st-warn);color:var(--st-warn-ink)}
.est.bad{background:var(--st-bad);color:#fff}
.est.off{background:var(--st-off);color:#fff}
.estlegend{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;font-size:11px;color:var(--ink3);margin-bottom:12px}

/* banners */
.banner{display:flex;gap:13px;align-items:flex-start;border-radius:var(--r-m);padding:14px 16px;font-size:12.8px;color:var(--ink2);line-height:1.55;border:1px solid}
.banner b{color:var(--ink)}
.bn-ic{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.bn-ic svg.i{width:18px;height:18px;color:#fff}
.banner.good{background:var(--good-bg);border-color:color-mix(in srgb,var(--good) 32%,transparent)}.banner.good .bn-ic{background:var(--good)}
.banner.info{background:var(--vio-soft);border-color:color-mix(in srgb,var(--vio) 24%,transparent)}.banner.info .bn-ic{background:var(--grad)}
.banner.warn{background:var(--warn-bg);border-color:color-mix(in srgb,var(--warn) 34%,transparent)}.banner.warn .bn-ic{background:var(--warn)}
.banner.crit{background:var(--crit-bg);border-color:color-mix(in srgb,var(--crit) 30%,transparent)}.banner.crit .bn-ic{background:var(--crit)}

/* KPI */
.kpi{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m);padding:15px 15px 13px;box-shadow:var(--shadow);display:flex;flex-direction:column}
.k-top{display:flex;align-items:center;gap:9px;margin-bottom:10px}
.k-ic{width:32px;height:32px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:var(--vio-soft);flex-shrink:0}
.k-ic svg.i{width:17px;height:17px;color:var(--vio)}
.k-ic.blu{background:var(--blu-soft)}.k-ic.blu svg.i{color:var(--blu)}
.k-ic.pnk{background:var(--pnk-soft)}.k-ic.pnk svg.i{color:var(--pnk)}
.k-ic.grn{background:var(--good-bg)}.k-ic.grn svg.i{color:var(--good)}
.k-ic.amb{background:var(--warn-bg)}.k-ic.amb svg.i{color:var(--warn)}
.k-top .src{margin-left:auto}
.k-l{font-size:10px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--ink3);line-height:1.3}
.k-row{display:flex;align-items:flex-end;justify-content:space-between;gap:8px;margin-top:6px}
.k-n{font-size:28px;font-weight:700;letter-spacing:-.02em;line-height:.95;font-variant-numeric:tabular-nums}
.k-s{font-size:11px;color:var(--ink3);margin-top:7px;line-height:1.4}
.k-s b{color:var(--ink2)}
.k-ab{font-size:10px;color:var(--ink4);margin-top:5px;line-height:1.35;border-top:1px dashed var(--line);padding-top:6px}
.k-ab b{color:var(--ink3)}

/* bars */
.vcard{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m);padding:16px 17px;box-shadow:var(--shadow);min-width:0}
.bar-row{display:grid;grid-template-columns:1fr auto;gap:5px 10px;align-items:center;margin-bottom:10px}
.bar-row:last-child{margin-bottom:0}
.bar-lab{font-size:12px;color:var(--ink2);font-weight:500;display:inline-flex;align-items:center;gap:6px;flex-wrap:wrap;min-width:0}
.bar-lab svg.i{width:13px;height:13px;color:var(--ink3)}
.bar-val{font-size:11.5px;font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums;white-space:nowrap}
.bar-val span{color:var(--ink3);font-weight:600;margin-left:4px}
.bar-track{grid-column:1/-1;height:7px;border-radius:20px;background:var(--inset);overflow:hidden;display:flex}
.bar-fill{height:100%;border-radius:20px;background:var(--grad)}
.bar-track .seg{height:100%}
.bar-row.miss .bar-fill{background:repeating-linear-gradient(45deg,var(--warn) 0 4px,color-mix(in srgb,var(--warn) 55%,transparent) 4px 8px)}
.subl{display:flex;align-items:center;gap:7px;font-size:10.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--ink2);margin:0 0 11px}
.subl .dot2{width:8px;height:8px;border-radius:50%}
.stc{font-size:8px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;padding:2px 7px;border-radius:20px}
.sc-on{background:var(--good-bg);color:var(--good-ink)}.sc-off{background:var(--warn-bg);color:var(--warn-ink)}.sc-new{background:var(--vio-soft);color:var(--vio)}

/* tables */
.tblwrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
table{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}
thead th{font-size:9px;font-weight:700;letter-spacing:.03em;text-transform:uppercase;color:var(--ink3);text-align:right;padding:10px 11px;background:var(--surface2);white-space:nowrap}
thead th:first-child,tbody td:first-child{text-align:left}
thead th .src{margin-left:4px}
tbody td{padding:10px 11px;font-size:12px;text-align:right;border-top:1px solid var(--line);color:var(--ink2);white-space:nowrap}
tbody tr:hover td{background:var(--surface2)}
td.l,th.l{text-align:left!important}
td .sub{display:block;font-size:10px;color:var(--ink3);font-weight:500;margin-top:1px}
td.strong,td b{color:var(--ink);font-weight:700}
tr.tot td{background:var(--inset);font-weight:700;color:var(--ink)}
tr.hi td{background:color-mix(in srgb,var(--warn) 8%,transparent)}
td.cj{font-weight:700;color:var(--ink)!important;border-left:2px solid var(--vio);background:linear-gradient(90deg,var(--vio-soft),transparent)!important}
.anm{font-family:ui-monospace,Menlo,monospace;font-size:10.5px;color:var(--ink3);display:block;margin-top:1px}
.minibar{display:inline-block;width:64px;height:6px;border-radius:9px;background:var(--inset);vertical-align:middle;margin-left:7px;overflow:hidden}
.minibar i{display:block;height:100%;border-radius:9px}
td.heat{text-align:center!important;font-weight:700;font-size:11px}
.h4{background:var(--good-bg);color:var(--good-ink)}.h3{background:var(--blu-soft);color:var(--src-meta)}.h2{background:var(--warn-bg);color:var(--warn-ink)}.h1{background:var(--crit-bg);color:var(--crit-ink)}
.glos{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px 18px;margin-top:12px;padding:12px 14px;border-radius:var(--r-s);background:var(--surface2);border:1px solid var(--line2)}
.glos div{font-size:11px;color:var(--ink3);line-height:1.4}
.glos b{color:var(--ink2);font-weight:800;margin-right:4px}

/* ===== insight card: 3 subsectores ===== */
.igrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:13px;align-items:start}
.i3{--tone:var(--vio);background:var(--surface);border:1px solid var(--line);border-radius:var(--r-l);box-shadow:var(--shadow);overflow:hidden;border-top:3px solid var(--tone);min-width:0}
.i3>summary{padding:14px 16px 12px;display:flex;flex-direction:column;gap:10px}
.i3-top{display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.seal{display:inline-flex;align-items:center;gap:8px;font-size:11.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--tone);margin-right:auto}
.seal .sic{width:28px;height:28px;border-radius:9px;background:var(--tone);display:flex;align-items:center;justify-content:center}
.seal .sic svg.i{width:15px;height:15px;color:#fff}
.t-subir{--tone:var(--vio)}.t-subir .seal .sic{background:var(--grad)}
.t-mant{--tone:var(--good)}.t-corr{--tone:var(--warn)}.t-paus{--tone:var(--crit)}.t-prob{--tone:var(--blu)}
.t-motivo{--tone:var(--vio)}.t-urg{--tone:#B8558F}.t-avance{--tone:var(--blu)}.t-freno{--tone:var(--warn)}.t-filtro{--tone:#7A7392}.t-prior{--tone:var(--good)}
.i3-nm{font-size:15px;font-weight:700;line-height:1.3;letter-spacing:-.01em;color:var(--ink);text-wrap:pretty}
.i3-ctx{border:1px solid var(--line2);border-radius:12px;background:var(--surface2);overflow:hidden}
.cx{display:grid;grid-template-columns:22px 70px minmax(0,1fr);align-items:center;gap:8px;padding:6px 10px;font-size:11.5px}
.cx+.cx{border-top:1px solid var(--line2)}
.cx-ic{width:22px;height:22px;border-radius:7px;display:flex;align-items:center;justify-content:center}
.cx-ic svg.i{width:13px;height:13px}
.cx-k{font-size:8.6px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--ink3)}
.cx-v{color:var(--ink);font-weight:600;line-height:1.3;min-width:0}
.cx-v .anm{font-weight:500;overflow-wrap:anywhere}
.k-camp{background:#FDE9D6;color:#B4610F}.k-conj{background:var(--blu-soft);color:var(--src-meta)}.k-anun{background:var(--pnk-soft);color:#A8467F}
.k-seg{background:var(--vio-soft);color:var(--vio)}.k-src{background:var(--good-bg);color:var(--good-ink)}.k-base{background:var(--inset);color:var(--ink2)}
[data-theme=dark] .k-camp{background:#3A2A12;color:#F1B26A}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .k-camp{background:#3A2A12;color:#F1B26A}}
.i3-more{display:flex;align-items:center;gap:6px;font-size:11.5px;font-weight:700;color:var(--vio);border-top:1px solid var(--line2);padding-top:10px;margin-top:2px}
.i3-more svg.i{width:14px;height:14px;transition:transform .2s;margin-left:auto}
.i3-more .cl{display:none}
.i3[open] .i3-more .op{display:none}.i3[open] .i3-more .cl{display:inline}
.i3[open] .i3-more svg.i{transform:rotate(180deg)}
.i3>summary:hover .i3-more{text-decoration:underline}
.i3-sec{padding:12px 16px 14px;border-top:1px dashed var(--line)}
.i3-lab{display:flex;align-items:center;gap:7px;font-size:9px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);margin-bottom:9px}
.i3-lab .n{width:17px;height:17px;border-radius:6px;background:var(--inset);color:var(--ink2);display:inline-flex;align-items:center;justify-content:center;font-size:9px;letter-spacing:0}
.i3-lab .src,.i3-lab .lvl{margin-left:auto}
.i3-b{list-style:none;display:flex;flex-direction:column;gap:8px}
.i3-b li{font-size:12.3px;color:var(--ink2);padding-left:16px;position:relative;line-height:1.45}
.i3-b li::before{content:"";position:absolute;left:0;top:6px;width:6px;height:6px;border-radius:50%;background:var(--tone)}
.i3-b b{color:var(--ink)}
.res{display:flex;align-items:flex-start;gap:12px}
.res .big{font-size:27px;font-weight:800;letter-spacing:-.02em;line-height:1;color:var(--tone);font-variant-numeric:tabular-nums;flex-shrink:0;min-width:58px}
.res .rt{flex:1;min-width:0}
.res .txt{font-size:12px;color:var(--ink2);line-height:1.45}
.res .txt b{color:var(--ink)}
.cmp{position:relative;height:10px;border-radius:20px;background:var(--inset);margin:28px 2px 8px}
.cmp .fill{position:absolute;left:0;top:0;bottom:0;border-radius:20px;background:var(--tone)}
.cmp .mk{position:absolute;top:-5px;bottom:-5px;width:2.5px;border-radius:2px;background:var(--ink)}
.cmp .mk b{position:absolute;bottom:calc(100% + 4px);font-size:9.5px;font-weight:700;color:var(--ink2);white-space:nowrap;background:var(--surface);padding:0 3px;border-radius:4px}
.cmp .mk.c b{left:50%;transform:translateX(-50%)}.cmp .mk.lft b{left:-3px}.cmp .mk.rgt b{right:-3px}
.cmp-lg{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:10px;color:var(--ink3);margin-top:4px}
.cmp-lg span{display:inline-flex;align-items:center;gap:5px}
.cmp-lg .sw{width:16px;height:6px;border-radius:9px;background:var(--tone)}
.cmp-lg .sm{width:2.5px;height:11px;border-radius:2px;background:var(--ink)}
.i3-adv{background:var(--surface2)}
.i3-adv p{font-size:11.8px;color:var(--ink2);line-height:1.5}
.i3-adv p+p{margin-top:6px}
.kv{display:grid;grid-template-columns:repeat(auto-fit,minmax(92px,1fr));gap:8px;margin-top:9px}
.kv>div{background:var(--surface);border:1px solid var(--line2);border-radius:10px;padding:8px 9px}
.kv .v{font-size:15px;font-weight:700;font-variant-numeric:tabular-nums;line-height:1.1}
.kv .k{font-size:9.5px;color:var(--ink3);margin-top:3px;line-height:1.3}
.kv .k abbr{text-decoration:none;font-weight:800;color:var(--ink2)}

/* hierarchy legend campaña > conjunto > anuncio */
.hier{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-bottom:14px}
.hc{display:flex;gap:11px;align-items:flex-start;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m);padding:12px 14px;box-shadow:var(--shadow);position:relative}
.hc .cx-ic{width:34px;height:34px;border-radius:10px}
.hc .cx-ic svg.i{width:18px;height:18px}
.hc>div>b{font-size:13px;display:block}
.hc>div>span{font-size:11px;color:var(--ink3);line-height:1.4;display:block;margin-top:2px}
.hc>div>span b{color:var(--ink2)}
.hc .ar{position:absolute;right:-12px;top:50%;transform:translateY(-50%);z-index:2;width:16px;height:16px;color:var(--ink4)}
.hc:last-child .ar{display:none}

/* subtabs (radio) */
.subtabs{display:inline-flex;flex-wrap:wrap;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-s);padding:3px;gap:2px;margin-bottom:16px}
.subtabs label{font-size:12.3px;font-weight:700;color:var(--ink3);padding:8px 14px;border-radius:9px;cursor:pointer;display:inline-flex;align-items:center;gap:7px}
.subtabs label svg.i{width:14px;height:14px}
.stab{display:none}

/* group averages */
.grupal{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-bottom:16px}
.gv{background:var(--grad-soft);border:1px solid var(--line);border-radius:var(--r-m);padding:14px 16px;box-shadow:var(--shadow)}
.gv .l{font-size:9.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--ink3);display:flex;align-items:center;gap:6px}
.gv .l svg.i{width:13px;height:13px;color:var(--vio)}
.gv .n{font-size:25px;font-weight:800;letter-spacing:-.02em;margin-top:7px;font-variant-numeric:tabular-nums;line-height:1}
.gv .m{font-size:11px;color:var(--ink3);margin-top:5px;line-height:1.35}
.gv .m b{color:var(--ink2)}

/* split line */
.split{display:flex;align-items:center;gap:13px;margin:30px 0 16px}
.split .ln{flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent)}
.split b{font-size:10.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--ink3);display:inline-flex;align-items:center;gap:8px}

/* ===== panorama ===== */
.hero-grid{display:grid;grid-template-columns:1.62fr 1fr;gap:14px;margin-bottom:14px}
.hero{position:relative;overflow:hidden;border-radius:var(--r-xl);background:var(--grad);color:#fff;padding:22px 24px;box-shadow:var(--shadow-lg);isolation:isolate}
.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(120% 90% at 88% -20%,rgba(255,255,255,.34),transparent 55%);z-index:0}
.hero>*{position:relative;z-index:1}
.hero .hero-sph{position:absolute;right:-30px;top:-24px;width:150px;height:150px;opacity:.6;z-index:0;mix-blend-mode:screen}
.hero-top{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:6px}
.hero-kick{font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.85)}
.hero-per{font-size:10.5px;font-weight:600;color:#fff;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.24);padding:5px 11px;border-radius:20px}
.hero-h{font-size:24px;font-weight:700;line-height:1.15;letter-spacing:-.015em;margin:2px 0 6px;max-width:86%}
.hero-sub{font-size:12.3px;color:rgba(255,255,255,.9);line-height:1.5;max-width:90%;margin-bottom:14px}
.hero-sub b{color:#fff}
.chart-scale{display:flex;justify-content:space-between;font-size:9.5px;color:rgba(255,255,255,.78);margin-bottom:3px;font-weight:600}
.hchart{position:relative}
.hchart svg{width:100%;height:110px;display:block;overflow:visible}
.chart-x{display:flex;justify-content:space-between;font-size:9px;color:rgba(255,255,255,.7);margin-top:5px;font-weight:600}
.endtag{position:absolute;right:-2px;top:30px;background:#fff;color:var(--vio);font-weight:700;font-size:11px;padding:4px 9px;border-radius:9px;box-shadow:0 4px 12px rgba(0,0,0,.2);line-height:1.15}
.endtag span{display:block;font-size:8px;color:#6F6888;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
.hero-stats{display:grid;grid-template-columns:repeat(3,1fr);background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.22);border-radius:var(--r-m);overflow:hidden;margin-top:14px}
.hs{padding:11px 13px;text-align:center}
.hs+.hs{border-left:1px solid rgba(255,255,255,.2)}
.hs .l{font-size:9px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.82);margin-bottom:4px}
.hs .v{font-size:21px;font-weight:700;line-height:1}
.hs .m{font-size:9.5px;color:rgba(255,255,255,.78);margin-top:3px}
.hero-pink{display:flex;flex-direction:column;border-radius:var(--r-xl);overflow:hidden;box-shadow:var(--shadow-lg)}
.hp-top{background:linear-gradient(135deg,#C77AA8,#9E6BC0);color:#fff;padding:18px 20px;position:relative;overflow:hidden;flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:14px}
.hp-top::before{content:"";position:absolute;inset:0;background:radial-gradient(120% 80% at 90% -10%,rgba(255,255,255,.3),transparent 55%)}
.hp-top>*{position:relative}
.hp-row{display:flex;align-items:center;justify-content:space-between;gap:8px}
.hp-ic{width:40px;height:40px;border-radius:12px;background:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.25);display:flex;align-items:center;justify-content:center}
.hp-ic svg.i{width:21px;height:21px;color:#fff}
.hp-chip{font-size:10px;font-weight:700;color:#fff;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.25);padding:5px 10px;border-radius:20px}
.hp-l{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.88);margin-bottom:3px}
.hp-v{font-size:34px;font-weight:700;letter-spacing:-.02em;line-height:1}
.hp-d{font-size:11.5px;color:rgba(255,255,255,.92);margin-top:6px;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.hp-d .pin{background:rgba(255,255,255,.22);padding:3px 8px;border-radius:20px;font-weight:700;font-size:10.5px}
.hp-foot{background:var(--surface);padding:13px 16px;display:flex;align-items:center;gap:10px}
.hp-foot .mini{flex:1}
.hp-foot .mini b{font-size:15px;font-weight:700;display:block;line-height:1}
.hp-foot .mini span{font-size:9.5px;color:var(--ink3);text-transform:uppercase;letter-spacing:.04em;font-weight:600}
.hp-spk{width:100%;height:56px;display:block;overflow:visible}
.hp-sp{width:1px;align-self:stretch;background:var(--line)}
.inout{display:grid;grid-template-columns:1.25fr 1fr;gap:14px}
.io-h{display:flex;align-items:center;gap:10px;margin-bottom:14px}
.io-ic{width:34px;height:34px;border-radius:11px;display:flex;align-items:center;justify-content:center}
.io-ic svg.i{width:18px;height:18px;color:#fff}
.io-h b{font-size:15px;display:block}
.io-h span{font-size:11.5px;color:var(--ink3)}
.io-h .tot{margin-left:auto;text-align:right}
.io-h .tot b{font-size:20px;font-variant-numeric:tabular-nums}
.io-h .tot span{font-size:9.5px;text-transform:uppercase;letter-spacing:.04em;font-weight:700}
.mkgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px 22px}
.mkgrid.two{grid-template-columns:repeat(2,minmax(0,1fr))}
.obase{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px;padding-top:12px;border-top:1px dashed var(--line)}
.recorrido{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:9px}
.rec{background:var(--surface2);border:1px solid var(--line2);border-radius:var(--r-m);padding:13px 13px;position:relative;min-width:0}
.rec .rs{font-size:9px;font-weight:800;color:var(--ink4);letter-spacing:.05em;display:flex;align-items:center;gap:5px}
.rec .rs svg.i{width:12px;height:12px}
.rec .n{font-size:24px;font-weight:800;letter-spacing:-.02em;line-height:1;margin:6px 0 3px;font-variant-numeric:tabular-nums}
.rec .l{font-size:11.5px;font-weight:600;color:var(--ink2)}
.rec .c{display:inline-block;margin-top:8px;font-size:10px;font-weight:700;color:var(--vio);background:var(--vio-soft);padding:3px 8px;border-radius:20px}
.rec .c.sm{color:var(--ink3);background:var(--inset)}
.rec.cut{border-style:dashed;border-color:color-mix(in srgb,var(--warn) 50%,transparent);background:var(--warn-bg)}
.rec.cut .c{background:var(--surface);color:var(--warn-ink)}
.dec{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.dec-item{display:flex;flex-direction:column;gap:10px;padding:15px;border-radius:var(--r-m);border:1px solid var(--line);background:var(--surface);box-shadow:var(--shadow);border-top:3px solid var(--dc)}
.dec-h{display:flex;align-items:center;gap:9px}
.dec-ic{width:32px;height:32px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0;background:var(--dc)}
.dec-ic svg.i{width:16px;height:16px;color:#fff}
.dec-h b{font-size:14.5px}
.dec-h .own{margin-left:auto}
.dec-p{display:flex;gap:9px;align-items:flex-start;font-size:12px;color:var(--ink2);line-height:1.5}
.dec-p+.dec-p{padding-top:9px;border-top:1px dashed var(--line)}
.dec-p .pi{width:22px;height:22px;border-radius:7px;background:var(--inset);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}
.dec-p .pi svg.i{width:12px;height:12px;color:var(--ink2)}
.dec-p b{color:var(--ink)}
.dec-p .k{display:block;font-size:8.6px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--ink3);margin-bottom:2px}

/* ===== funnel steps ===== */
.fsteps{display:grid;grid-template-columns:repeat(var(--n,6),minmax(0,1fr));gap:8px}
.fs{background:var(--surface2);border:1px solid var(--line2);border-radius:var(--r-m);padding:12px 12px 13px;min-width:0;display:flex;flex-direction:column}
.fs .t{display:flex;justify-content:space-between;align-items:center;font-size:9px;font-weight:800;color:var(--ink4);letter-spacing:.05em}
.fs .t .p{color:var(--vio);font-size:10px}
.fs .l{font-size:12px;font-weight:700;color:var(--ink);margin-top:8px;line-height:1.25}
.fs .v{font-size:11px;color:var(--ink3);margin-top:3px}
.fs .v b{color:var(--ink2);font-size:13px}
.fs .pass{margin-top:auto;padding-top:10px}
.fs .pass span{display:inline-flex;align-items:center;gap:4px;font-size:10px;font-weight:800;padding:3px 8px;border-radius:20px;background:var(--vio-soft);color:var(--vio)}
.fs .bar{height:5px;border-radius:9px;background:var(--inset);margin-top:9px;overflow:hidden}
.fs .bar i{display:block;height:100%;background:var(--grad);border-radius:9px}
.fs.leak{border-color:color-mix(in srgb,var(--crit) 40%,transparent);background:var(--crit-bg)}
.fs.leak .pass span{background:var(--crit);color:#fff}
.fs.dim{border-style:dashed}
.fs.dim .pass span{background:var(--inset);color:var(--ink3)}

/* stage cards */
.stage{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-l);padding:17px 18px;box-shadow:var(--shadow);border-top:3px solid var(--stc)}
.stage .sh{display:flex;align-items:center;gap:9px}
.stage .sh .dec-ic{background:var(--stc);width:30px;height:30px}
.stage h4{font-size:15px;font-weight:700}
.stage .ssub{font-size:11.5px;color:var(--ink3);margin:6px 0 12px;line-height:1.4}
.stage .qty{font-size:34px;font-weight:800;letter-spacing:-.03em;line-height:1;font-variant-numeric:tabular-nums}
.stage .qty small{font-size:12px;font-weight:600;color:var(--ink3);letter-spacing:0}
.stage .rowl{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:8px 0;border-top:1px solid var(--line2);font-size:12px;margin-top:4px}
.stage .rowl .k{color:var(--ink3);display:inline-flex;align-items:center;gap:7px;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.03em}
.stage .rowl .k svg.i{width:13px;height:13px}
.stage .rowl .v{font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums}
.stage .act{margin-top:10px;padding-top:11px;border-top:1px solid var(--line2);font-size:12px;color:var(--ink2);line-height:1.45;display:flex;gap:8px}
.stage .act svg.i{color:var(--stc);width:15px;height:15px;margin-top:1px}

/* ===== subsector "Cómo mejorar el CRM" ===== */
.subsec{border-radius:28px;padding:24px 22px 22px;margin-top:30px;position:relative}
.subsec.mejora{background:color-mix(in srgb,var(--good) 7%,var(--bg2));border:1px solid color-mix(in srgb,var(--good) 26%,transparent)}
.subsec.alt{background:color-mix(in srgb,var(--vio) 6%,var(--bg2));border:1px solid color-mix(in srgb,var(--vio) 22%,transparent)}
.ss-h{display:flex;gap:14px;align-items:flex-start;margin-bottom:18px}
.ss-ic{width:46px;height:46px;border-radius:14px;display:flex;align-items:center;justify-content:center;flex-shrink:0;background:var(--mejora);box-shadow:0 8px 18px -8px color-mix(in srgb,var(--mejora) 70%,transparent)}
.subsec.alt .ss-ic{background:var(--grad)}
.ss-ic svg.i{width:23px;height:23px;color:#fff}
.ss-k{font-size:10px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--good-ink)}
.subsec.alt .ss-k{color:var(--vio)}
.ss-h h2{font-size:24px;font-weight:700;letter-spacing:-.02em;line-height:1.15;margin-top:3px}
.ss-h h2 em{font-weight:400}
.ss-h p{font-size:12.8px;color:var(--ink2);line-height:1.55;margin-top:6px;max-width:820px}
.ss-lab{display:flex;align-items:center;gap:8px;font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--ink3);margin:24px 0 11px}
.ss-lab .n{width:20px;height:20px;border-radius:7px;background:var(--surface);border:1px solid var(--line);display:inline-flex;align-items:center;justify-content:center;font-size:10px;color:var(--ink2);letter-spacing:0}
.ss-lab:first-of-type{margin-top:0}

/* hallazgo (insight vistoso) */
.hallazgo{position:relative;overflow:hidden;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-xl);box-shadow:var(--shadow-lg)}
.hallazgo::before{content:"";position:absolute;left:0;right:0;top:0;height:4px;background:var(--grad)}
.hz-top{padding:22px 24px 6px;display:flex;gap:16px;align-items:flex-start}
.hz-badge{display:inline-flex;align-items:center;gap:7px;font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:var(--grad);padding:6px 12px;border-radius:20px;white-space:nowrap}
.hz-badge svg.i{width:13px;height:13px;color:#fff}
.hz-t{font-size:30px;font-weight:700;letter-spacing:-.025em;line-height:1.08;margin-top:10px;text-wrap:balance}
.hz-t em{font-weight:400}
.hz-s{font-size:13px;color:var(--ink2);line-height:1.55;margin-top:9px;max-width:780px}
.hz-s b{color:var(--ink)}
.hz-body{display:grid;grid-template-columns:240px minmax(0,1fr);gap:22px;padding:16px 24px 22px;align-items:center}
.donut{position:relative;width:200px;height:200px;margin:0 auto}
.donut svg{width:100%;height:100%;transform:rotate(-90deg)}
.donut .ctr{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.donut .ctr b{font-size:30px;font-weight:800;letter-spacing:-.02em;line-height:1}
.donut .ctr span{font-size:10px;color:var(--ink3);max-width:110px;line-height:1.3;margin-top:4px}
.dlg{display:flex;flex-direction:column;gap:6px;margin-top:12px}
.dlg div{display:flex;align-items:center;gap:7px;font-size:11px;color:var(--ink2)}
.dlg i{width:10px;height:10px;border-radius:3px;flex-shrink:0}
.dlg b{margin-left:auto;font-variant-numeric:tabular-nums}
.emb{display:flex;flex-direction:column;gap:13px}
.emb-r{display:grid;grid-template-columns:minmax(0,210px) minmax(0,1fr) 54px;gap:12px;align-items:center}
.emb-n{font-size:12.5px;font-weight:700;line-height:1.25}
.emb-n span{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;color:var(--ink3);margin-top:3px}
.emb-n span svg.i{width:12px;height:12px}
.emb-t{height:16px;border-radius:6px;background:var(--inset);overflow:hidden;display:flex}
.emb-t i{display:block;height:100%}
.emb-v{font-size:16px;font-weight:800;text-align:right;font-variant-numeric:tabular-nums}
.emb-lg{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:10.5px;color:var(--ink3);margin-top:14px}
.emb-lg span{display:inline-flex;align-items:center;gap:6px}
.emb-lg i{width:12px;height:12px;border-radius:3px}
.c-auto{background:var(--grad)}
.c-man{background:repeating-linear-gradient(-45deg,var(--warn) 0 5px,color-mix(in srgb,var(--warn) 62%,#fff) 5px 9px)}
.c-none{background:var(--inset);border:1px solid var(--line)}
.hz-foot{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:1px solid var(--line)}
.hz-foot>div{padding:14px 18px;display:flex;gap:10px;align-items:flex-start;font-size:12px;color:var(--ink2);line-height:1.45}
.hz-foot>div+div{border-left:1px solid var(--line)}
.hz-foot svg.i{width:18px;height:18px;flex-shrink:0;margin-top:1px}
.hz-foot b{color:var(--ink)}

/* insight aislado (card clave) */
.key{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-l);box-shadow:var(--shadow);overflow:hidden;border-left:5px solid var(--kc,var(--warn))}
.key-h{display:flex;gap:14px;align-items:flex-start;padding:18px 20px}
.key-ic{width:40px;height:40px;border-radius:12px;background:var(--kc,var(--warn));display:flex;align-items:center;justify-content:center;flex-shrink:0}
.key-ic svg.i{width:20px;height:20px;color:#fff}
.key-k{display:flex;align-items:center;gap:8px;font-size:9.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3);flex-wrap:wrap}
.key-t{font-size:18px;font-weight:700;letter-spacing:-.015em;line-height:1.3;margin-top:5px;text-wrap:pretty}
.key-t em{font-weight:400}
.key-s{font-size:12.8px;color:var(--ink2);line-height:1.55;margin-top:7px}
.key-s b{color:var(--ink)}
.key-stats{display:grid;grid-template-columns:repeat(var(--n,3),minmax(0,1fr));border-top:1px solid var(--line)}
.key-stats>div{padding:12px 18px}
.key-stats>div+div{border-left:1px solid var(--line)}
.key-stats .v{font-size:22px;font-weight:800;letter-spacing:-.02em;font-variant-numeric:tabular-nums;line-height:1}
.key-stats .k{font-size:10.5px;color:var(--ink3);margin-top:4px;line-height:1.35}
.key-adv{border-top:1px dashed var(--line);background:var(--surface2);padding:16px 20px 18px}
.key-adv h5{display:flex;align-items:center;gap:8px;font-size:10px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--ink2);margin-bottom:12px}
.key-adv h5 svg.i{color:var(--vio);width:14px;height:14px}
.dgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.dgrid .vcard{box-shadow:none}

/* steps (qué cambiar) */
.steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.stp{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-l);box-shadow:var(--shadow);display:flex;flex-direction:column;overflow:hidden}
.stp-h{display:flex;align-items:center;gap:11px;padding:15px 16px 0}
.stp-n{width:34px;height:34px;border-radius:11px;background:var(--grad);color:#fff;font-size:15px;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.stp-h b{font-size:14.5px;line-height:1.25}
.stp-d{padding:10px 16px 14px;font-size:12px;color:var(--ink2);line-height:1.5;flex:1}
.stp-d b{color:var(--ink)}
.stp-tags{display:flex;flex-wrap:wrap;gap:6px;padding:0 16px 14px}
.stp-f{display:flex;align-items:flex-start;gap:8px;padding:11px 16px;background:var(--surface2);border-top:1px solid var(--line);font-size:11px;color:var(--ink3);line-height:1.4}
.stp-f svg.i{width:14px;height:14px;color:var(--good);margin-top:1px}
.stp-f b{color:var(--ink2)}

/* conclusión */
.concl{margin-top:22px;border-radius:var(--r-l);background:var(--good-bg);border:1px solid color-mix(in srgb,var(--good) 32%,transparent);display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);overflow:hidden}
.concl-l{padding:20px 22px;display:flex;gap:14px;align-items:flex-start}
.concl-l .bn-ic{background:var(--good);width:40px;height:40px;border-radius:12px}
.concl-l .bn-ic svg.i{width:20px;height:20px;color:#fff}
.concl-l b.t{display:block;font-size:17px;letter-spacing:-.01em;color:var(--ink);line-height:1.25}
.concl-l p{font-size:12.5px;color:var(--ink2);line-height:1.55;margin-top:6px}
.concl-r{padding:16px 20px;border-left:1px solid color-mix(in srgb,var(--good) 25%,transparent);display:flex;flex-direction:column;gap:8px;justify-content:center;background:color-mix(in srgb,var(--surface) 55%,transparent)}
.concl-r div{display:flex;align-items:center;gap:10px;font-size:12px;color:var(--ink2)}
.concl-r .n{width:22px;height:22px;border-radius:7px;background:var(--good);color:#fff;font-size:11px;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.concl-r b{color:var(--ink)}
.concl-r .c{margin-left:auto;font-size:9px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--good-ink);white-space:nowrap}

/* compare B2B/B2C */
.vs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0;border:1px solid var(--line);border-radius:var(--r-l);overflow:hidden;background:var(--surface);box-shadow:var(--shadow)}
.vs-c{padding:16px 18px}
.vs-c+.vs-c{border-left:1px solid var(--line)}
.vs-h{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.vs-h .io-ic{width:36px;height:36px}
.vs-h b{font-size:15px;display:block}
.vs-h span{font-size:11px;color:var(--ink3)}
.vs-row{display:flex;justify-content:space-between;gap:10px;padding:7px 0;border-top:1px solid var(--line2);font-size:12px;color:var(--ink3)}
.vs-row b{color:var(--ink);font-variant-numeric:tabular-nums}

/* corredores scorecards */
.scgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;align-items:start}
.sc{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-l);box-shadow:var(--shadow);overflow:hidden}
.sc-h{display:flex;align-items:center;gap:11px;padding:14px 15px 10px}
.sc-av{width:38px;height:38px;border-radius:12px;background:var(--grad-soft);border:1px solid var(--line);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;color:var(--vio);flex-shrink:0}
.sc-h b{font-size:13.5px;display:block;line-height:1.2}
.sc-h span{font-size:10.5px;color:var(--ink3)}
.sc-h .est{margin-left:auto}
.sc-m{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:1px solid var(--line2);border-bottom:1px solid var(--line2)}
.sc-m>div{padding:9px 12px}
.sc-m>div+div{border-left:1px solid var(--line2)}
.sc-m .v{font-size:16px;font-weight:800;font-variant-numeric:tabular-nums;line-height:1.05}
.sc-m .k{font-size:9.5px;color:var(--ink3);margin-top:3px;line-height:1.25}
.sc-obj{padding:10px 15px 2px}
.sc-obj .cmp{margin:24px 0 6px}
.sc-p{display:flex;gap:9px;padding:9px 15px;font-size:11.5px;color:var(--ink2);line-height:1.45;align-items:flex-start}
.sc-p+.sc-p{border-top:1px dashed var(--line)}
.sc-p .pi{width:22px;height:22px;border-radius:7px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.sc-p .pi svg.i{width:12px;height:12px}
.sc-p b{color:var(--ink)}
.sc-p .k{display:block;font-size:8.6px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--ink3);margin-bottom:1px}
.pi-good{background:var(--good-bg);color:var(--good)}.pi-up{background:var(--vio-soft);color:var(--vio)}

/* meta en prometheo (imagen 1 adaptada) */
.metagrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;align-items:start}
.mt3{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-xl);padding:20px;box-shadow:var(--shadow)}
.mt3-hd{display:flex;justify-content:space-between;align-items:center;margin-bottom:13px}
.mt3-ic{width:46px;height:46px;border-radius:14px;display:flex;align-items:center;justify-content:center;background:var(--grad)}
.mt3-ic svg.i{width:22px;height:22px;color:#fff}
.mt3 h3{font-size:19px;font-weight:700;letter-spacing:-.01em}
.mt3 .what{font-size:12px;color:var(--ink3);margin:5px 0 14px;line-height:1.45}
.mt3 .seen{display:flex;align-items:center;gap:7px;font-size:9.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);margin-bottom:9px}
.mt3 .seen svg.i{width:13px;height:13px;color:var(--vio)}
.acts{display:flex;flex-direction:column;gap:8px}
.act{display:flex;align-items:flex-start;gap:10px;background:var(--surface2);border:1px solid var(--line);border-radius:var(--r-s);padding:10px 11px}
.a-ic{width:26px;height:26px;border-radius:8px;background:var(--vio-soft);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.a-ic svg.i{width:14px;height:14px;color:var(--vio)}
.a-t{flex:1;font-size:11.8px;color:var(--ink2);line-height:1.45}
.a-t b{color:var(--ink)}
.a-t .go{display:flex;align-items:center;gap:5px;margin-top:5px;font-size:10.5px;font-weight:700;color:var(--src-meta)}
.a-t .go svg.i{width:12px;height:12px}
.mt3-f{margin-top:12px;padding-top:12px;border-top:1px dashed var(--line);display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:11px;color:var(--ink3)}
.mt3-f b{color:var(--ink2)}

/* audiencias */
.aucard{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m);overflow:hidden;box-shadow:var(--shadow);margin-bottom:10px}
.au-s{display:flex;align-items:center;gap:14px;padding:14px 17px}
.au-ic{width:40px;height:40px;border-radius:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0;background:var(--grad)}
.au-ic svg.i{width:20px;height:20px;color:#fff}
.au-t{flex:1;min-width:0}
.au-n{font-size:14px;font-weight:700;display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.au-badge{font-size:9.5px;font-weight:800;padding:2px 8px;border-radius:6px}
.au-ss{font-size:11.5px;color:var(--ink3);margin-top:3px}
.au-c{font-size:24px;font-weight:700;letter-spacing:-.02em;line-height:1;text-align:right;flex-shrink:0;font-variant-numeric:tabular-nums}
.au-c span{display:block;font-size:9px;color:var(--ink3);font-weight:600;text-transform:uppercase;letter-spacing:.04em;margin-top:3px}
.chev{color:var(--ink3);transition:transform .2s;flex-shrink:0;display:inline-flex}
details[open]>summary .chev{transform:rotate(180deg)}
.au-d{padding:0 17px 15px 71px}
.au-d ul{list-style:none;display:flex;flex-direction:column;gap:6px}
.au-d li{font-size:12px;color:var(--ink2);padding-left:15px;position:relative;line-height:1.45}
.au-d li::before{content:"";position:absolute;left:0;top:7px;width:5px;height:5px;border-radius:50%;background:var(--grad)}
.meter{height:8px;border-radius:9px;background:var(--inset);position:relative;margin:8px 0 4px;overflow:visible}
.meter i{display:block;height:100%;border-radius:9px}
.meter .th{position:absolute;top:-4px;bottom:-4px;width:2px;background:var(--ink)}

/* mincard (desplegables) */
.mincard{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m);box-shadow:var(--shadow);overflow:hidden;margin-bottom:10px}
.mincard>summary{display:flex;align-items:center;gap:13px;padding:13px 16px}
.mc-ic{width:30px;height:30px;border-radius:9px;background:var(--vio-soft);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.mc-ic svg.i{width:15px;height:15px;color:var(--vio)}
.mc-t{flex:1;min-width:0}.mc-t b{font-size:13.5px}
.mc-t span{font-size:11px;color:var(--ink3);display:block;margin-top:1px}
.mc-v{font-size:16px;font-weight:700;font-variant-numeric:tabular-nums;flex-shrink:0;text-align:right}
.mc-v small{display:block;font-size:8.5px;color:var(--ink3);text-transform:uppercase;letter-spacing:.03em;font-weight:600}
.mc-body{border-top:1px solid var(--line);padding:12px 14px}

/* campaign summary (meta ads) */
.bigcamp{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:13px}
.bc{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-l);padding:17px 17px 16px;box-shadow:var(--shadow);border-top:3px solid var(--bcac)}
.bc-hd{display:flex;align-items:center;gap:8px;margin-bottom:4px}
.bc-hd .cx-ic{width:26px;height:26px}
.bc-nm{font-size:15.5px;font-weight:700;letter-spacing:-.01em}
.bc-hd .obj{margin-left:auto}
.obj{display:inline-flex;align-items:center;gap:4px;font-size:9px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;padding:3px 9px;border-radius:20px;white-space:nowrap;background:var(--vio-soft);color:var(--vio)}
.bc-o{font-size:11.3px;color:var(--ink3);margin-bottom:14px;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.bc-o b{color:var(--ink2)}
.bc-big{display:flex;align-items:flex-end;gap:7px}
.bc-big .n{font-size:38px;font-weight:700;letter-spacing:-.03em;line-height:.85;font-variant-numeric:tabular-nums}
.bc-big .u{font-size:12px;color:var(--ink3);font-weight:600;padding-bottom:4px}
.bc-cap{font-size:11.5px;color:var(--ink3);margin:6px 0 13px}
.bc-cap b{color:var(--ink2)}
.bc-row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.bc-row>div{background:var(--surface2);border:1px solid var(--line2);border-radius:var(--r-s);padding:9px 10px}
.bc-row .v{font-size:17px;font-weight:700;letter-spacing:-.01em;line-height:1;font-variant-numeric:tabular-nums}
.bc-row .k{font-size:9px;color:var(--ink3);text-transform:uppercase;letter-spacing:.03em;font-weight:600;margin-top:4px;line-height:1.3}
.bc-row+.bc-row{margin-top:8px}
.bc-verd{margin-top:13px;padding-top:12px;border-top:1px solid var(--line2);font-size:12px;color:var(--ink2);line-height:1.45;display:flex;gap:8px;align-items:flex-start}
.bc-verd svg.i{color:var(--bcac);margin-top:1px}
.bc-verd b{color:var(--ink)}
.camp{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m);overflow:hidden;box-shadow:var(--shadow);margin-bottom:11px}
.camp-s{display:flex;align-items:center;gap:13px;padding:14px 17px}
.camp-t{flex:1;min-width:0}
.camp-n{font-size:14px;font-weight:700;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.camp-o{font-size:11px;color:var(--ink3);margin-top:2px}
.camp-m{display:flex;gap:18px;flex-shrink:0}
.camp-m>div{text-align:right}
.camp-m .v{font-size:15px;font-weight:700;font-variant-numeric:tabular-nums;line-height:1}
.camp-m .k{font-size:8.5px;color:var(--ink3);text-transform:uppercase;letter-spacing:.03em;font-weight:600}
.camp .tblwrap{border-top:1px solid var(--line)}
.srclegend{display:flex;flex-wrap:wrap;gap:10px 18px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m);padding:12px 15px;box-shadow:var(--shadow);margin-bottom:14px}
.slg{display:flex;align-items:center;gap:8px;font-size:11.5px;color:var(--ink3);line-height:1.35;flex:1;min-width:190px}
.slg b{color:var(--ink2)}
.iobar{display:flex;gap:9px;flex-wrap:wrap;align-items:center;margin:4px 0 16px}
.iobtn{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:700;border-radius:11px;padding:9px 14px;cursor:pointer;border:1px solid var(--line);background:var(--surface);color:var(--ink2);box-shadow:var(--shadow)}
.iobtn:hover{border-color:var(--vio)}
.iobtn svg.i{width:15px;height:15px;color:var(--vio)}
.iobtn.primary{background:var(--grad);color:#fff;border:none}.iobtn.primary svg.i{color:#fff}
.iobtn.locked{opacity:.6;cursor:not-allowed}
.iobtn .lk{font-size:8.5px;font-weight:800;letter-spacing:.03em;text-transform:uppercase;background:var(--inset);color:var(--ink3);padding:2px 6px;border-radius:5px}
.iohint{font-size:11px;color:var(--ink3);margin-left:auto}

/* charts */
.chart{width:100%;display:block;overflow:visible}
.chart text{font-family:var(--hel);fill:var(--ink3);font-size:10px}
.chart .gl{stroke:var(--line);stroke-width:1}
.chart .lbl{fill:var(--ink2);font-weight:700;font-size:10px}
.chart-lg{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:10.5px;color:var(--ink3);margin-top:8px}
.chart-lg span{display:inline-flex;align-items:center;gap:6px}
.chart-lg i{width:12px;height:12px;border-radius:3px}
.spark{width:96px;height:26px;display:inline-block;vertical-align:middle;overflow:visible}

/* integraciones */
.bridge{background:var(--grad-soft);border:1px solid var(--line);border-radius:var(--r-l);padding:20px 22px;text-align:center;margin-bottom:14px}
.bridge .eq{font-size:15px;font-weight:700;color:var(--ink);margin:4px 0 8px}
.bridge .eq b{color:var(--vio)}
.bridge p{font-size:12.5px;color:var(--ink3);max-width:680px;margin:0 auto;line-height:1.55}
.intg-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:13px}
.intg{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-l);padding:22px 18px 18px;box-shadow:var(--shadow);text-align:center}
.intg .ci{width:52px;height:52px;border-radius:15px;display:flex;align-items:center;justify-content:center;margin:0 auto 12px;background:var(--surface2);border:1px solid var(--line)}
.intg .ci svg.i{width:26px;height:26px}
.intg h4{font-size:14.5px;font-weight:700}
.intg p{font-size:11.5px;color:var(--ink3);margin-top:5px;line-height:1.45}
.intg .stt{position:absolute;top:12px;right:12px;font-size:8.5px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;padding:3px 8px;border-radius:20px}
.stt.on{background:var(--good-bg);color:var(--good-ink)}.stt.off{background:var(--inset);color:var(--ink3)}.stt.pause{background:var(--warn-bg);color:var(--warn-ink)}
.intg.avail{border-style:dashed}
.intg.avail .ci{filter:grayscale(.6);opacity:.75}
.intg.live{border-color:color-mix(in srgb,var(--good) 40%,transparent)}
.intg-on{background:color-mix(in srgb,var(--good) 8%,transparent);border:1px solid color-mix(in srgb,var(--good) 24%,transparent);border-radius:var(--r-l);padding:13px}
.intg .bases{display:flex;flex-wrap:wrap;justify-content:center;gap:5px;margin-top:10px}
.order3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.srcrow{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,2fr) auto;gap:12px;align-items:center;padding:11px 0;border-top:1px solid var(--line2);font-size:12px}
.srcrow:first-child{border-top:none}
.srcrow .nm{font-weight:700;color:var(--ink);display:flex;align-items:center;gap:8px}
.srcrow .ds{color:var(--ink3);line-height:1.4}
.srcrow .dt{font-size:10.5px;color:var(--ink3);text-align:right;white-space:nowrap}
.srcrow .dt b{color:var(--ink2);display:block}

.empty{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:24px 18px;text-align:center;border:1px dashed var(--line);border-radius:var(--r-m);color:var(--ink3);font-size:12px;background:var(--surface2)}
.empty svg.i{width:22px;height:22px;color:var(--ink4)}
.empty b{color:var(--ink2);font-size:12.5px}
.quote{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-m);padding:14px 15px;box-shadow:var(--shadow)}
.quote h5{display:flex;align-items:center;gap:7px;font-size:10px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--ink2);margin-bottom:10px}
.quote h5 svg.i{color:var(--vio);width:14px;height:14px}
.quote p{font-family:var(--serif);font-style:italic;font-size:14px;color:var(--ink2);line-height:1.4;padding:7px 0;border-top:1px solid var(--line2)}
.quote p:first-of-type{border-top:none}
.footer{margin-top:36px;padding-top:18px;border-top:1px solid var(--line);display:flex;align-items:center;gap:10px;font-size:11px;color:var(--ink3);flex-wrap:wrap}
.footer .orb{width:14px;height:14px;border-radius:50%;background:var(--grad)}

/* ===== responsive ===== */
@media (max-width:1180px){
  .igrid,.metagrid,.scgrid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .recorrido{grid-template-columns:repeat(3,minmax(0,1fr))}
  .fsteps{grid-template-columns:repeat(4,minmax(0,1fr))}
}
@media (max-width:1080px){
  .hero-grid,.inout{grid-template-columns:1fr}
  .g3,.dgrid,.steps,.order3,.intg-grid,.bigcamp,.dec{grid-template-columns:repeat(2,minmax(0,1fr))}
  .g4,.grupal{grid-template-columns:repeat(2,minmax(0,1fr))}
  .hz-body{grid-template-columns:1fr}
  .mkgrid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .glos{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width:860px){
  .shell{flex-direction:column;padding:0 12px 30px}
  .side{position:sticky;top:0;z-index:30;width:100%;flex:none;height:auto;max-height:none;overflow-y:visible;flex-direction:row;flex-wrap:nowrap;overflow-x:auto;gap:4px;padding:9px 10px;border-radius:0 0 var(--r-l) var(--r-l)}
  .side .brand,.side .navlab{display:none}
  .nav{flex-shrink:0;white-space:nowrap}
  .side-foot{margin:0 0 0 auto;padding:0;border:none;flex-shrink:0}
  .themebtn span{display:none}
  .concl{grid-template-columns:1fr}.concl-r{border-left:none;border-top:1px solid color-mix(in srgb,var(--good) 25%,transparent)}
  .hz-foot{grid-template-columns:1fr}.hz-foot>div+div{border-left:none;border-top:1px solid var(--line)}
  .hier{grid-template-columns:1fr}.hc .ar{display:none}
}
@media (max-width:720px){
  .g2,.g3,.g4,.igrid,.metagrid,.scgrid,.dgrid,.steps,.order3,.intg-grid,.bigcamp,.dec,.grupal,.mkgrid,.mkgrid.two,.vs{grid-template-columns:1fr}
  .vs-c+.vs-c{border-left:none;border-top:1px solid var(--line)}
  .span2{grid-column:auto}
  .recorrido{grid-template-columns:repeat(2,minmax(0,1fr))}
  .fsteps{grid-template-columns:repeat(2,minmax(0,1fr))}
  .hero-stats{grid-template-columns:1fr}.hs+.hs{border-left:none;border-top:1px solid rgba(255,255,255,.2)}
  .camp-m{display:none}
  .key-stats{grid-template-columns:1fr}.key-stats>div+div{border-left:none;border-top:1px solid var(--line)}
  .emb-r{grid-template-columns:1fr 48px}.emb-t{grid-column:1/-1;grid-row:2}
  .hz-t{font-size:24px}
  .srcrow{grid-template-columns:1fr}.srcrow .dt{text-align:left}
  .au-d{padding-left:17px}
  .glos{grid-template-columns:1fr}
  .hbrand .wm{font-size:28px}.hbrand .ic{font-size:15px}
  .tb-r{margin-left:0}
}
@media (max-width:440px){
  .hero-h{max-width:100%;font-size:20px}.hero-sub{max-width:100%}
  h1.sec{font-size:22px}
  .subsec{padding:18px 14px;border-radius:20px}
}
"""
