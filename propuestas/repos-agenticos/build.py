import json, re, sys, os

SK = '/root/.claude/skills/synced/e5e088ec-a33a-47f8-8002-c411ab3c7a6e_4557b365-5fbc-48bf-942d-18617b74dd22/aurea-estetica-documentacion/assets'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]

src = open(SK + '/ejemplos/drakon-ventas-marketing.html').read()
CSS = src[src.find('<style>') + 7:src.find('</style>')]
LOGO = open(SK + '/deck/logo.txt').read().strip()
SPHERE = open(SK + '/deck/sphere.txt').read().strip()
_ic = json.load(open(HERE + '/icons.json'))
NAMES = ['sliders', 'chat', 'check', 'arrow', 'eye', 'globe', 'clock', 'store', 'dollar', 'route',
         'bolt', 'target', 'trend', 'doc', 'users', 'bulb', 'mail', 'robot', 'frame', 'refresh']
IC = dict(zip(NAMES, _ic))
CHK = IC['check']

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Arimo:ital,wght@0,400;0,500;0,600;0,700;1,400;1,700&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300;1,9..144,400&display=swap" rel="stylesheet">')

# Ajustes de plataforma (no tocan el sistema): nav sticky respetando el safe-area.
PLATFORM_CSS = '.topnav{top:env(safe-area-inset-top,0px)}'


def checks(items):
    return '<ul class="checks">' + ''.join(f'<li>{CHK}<span>{i}</span></li>' for i in items) + '</ul>'


def head(eye, h2, p):
    return f'<div class="sec-head"><span class="eyebrow"><span class="ob"></span>{eye}</span><h2>{h2}</h2><p>{p}</p></div>'


def feat(ic, t, d, extra=''):
    return f'<div class="feat"><div class="feat-ic">{IC[ic]}</div><div class="feat-title">{t}</div><div class="feat-desc">{d}</div>{extra}</div>'


def callout(ic, eye, t, d):
    return f'<div class="callout"><div class="c-ic">{IC[ic]}</div><div><div class="c-eye">{eye}</div><div class="c-title">{t}</div><div class="c-desc">{d}</div></div></div>'


def band(kind, num, ic, eye, t, sub, id_=''):
    pre = f'<div id="{id_}"></div>' if id_ else ''
    return (pre + f'<section class="sec band {kind}"><div class="band-in"><div class="band-num">{num}</div><div class="band-ic">{IC[ic]}</div>'
            f'<div><div class="band-eye">{eye}</div><div class="band-title">{t}</div><div class="band-sub">{sub}</div></div></div></section>')


def chan(ic, t, sub, items):
    lis = ''.join(f'<li>{IC["arrow"]}<span>{i}</span></li>' for i in items)
    s = f'<div style="font-size:12.5px;color:var(--ink-3);margin:-6px 0 12px;font-style:italic">{sub}</div>' if sub else ''
    return f'<div class="chan"><div class="ch-h"><div class="ch-ic">{IC[ic]}</div><div class="ch-t">{t}</div></div>{s}<ul>{lis}</ul></div>'


def ctype(cls, n, t, items, tag, tagcls=''):
    return (f'<div class="ctype {cls}"><div class="ct-n">{n}</div><div class="ct-t">{t}</div>'
            f'<ul class="checks" style="margin:6px 0 12px">' + ''.join(f'<li>{CHK}<span>{i}</span></li>' for i in items) +
            f'</ul><div class="ct-tag {tagcls}">{tag}</div></div>')


def hs(n, ic, t, d, tag):
    return f'<div class="hs"><div class="hs-n">{n}</div><div class="hs-ic">{IC[ic]}</div><div class="hs-t">{t}</div><div class="hs-d">{d}</div><div class="hs-tag"><span class="pill acc">{tag}</span></div></div>'


def hsteps(steps):
    return '<div class="hsteps">' + f'<div class="harrow">{IC["arrow"]}</div>'.join(hs(*s) for s in steps) + '</div>'


def qcard(ic, t, d):
    return f'<div class="qcard"><div class="q-ic">{IC[ic]}</div><div class="q-t">{t}</div><div class="q-d">{d}</div></div>'


def gap(color, h, d):
    return f'<div class="gap"><div class="g-h"><span class="g-dot" style="background:{color}"></span>{h}</div><div class="g-d">{d}</div></div>'


def mcard(lbl, v, d, hi=False):
    return f'<div class="mcard{" hi" if hi else ""}"><div class="mc-lbl">{lbl}</div><div class="mc-v">{v}</div><div class="mc-d">{d}</div></div>'


def grid(n, items, style=''):
    st = f' style="{style}"' if style else ''
    return f'<div class="grid-{n}"{st}>' + ''.join(items) + '</div>'


def page(title, nav, sections, closer_h2, closer_p, footer_r, script=''):
    return (f'<title>{title}</title>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n{FONTS}\n'
            f'<style>{CSS}\n{PLATFORM_CSS}</style>\n'
            f'<main class="container">{nav}{"".join(sections)}'
            f'<section class="closer"><div class="closer-text" style="text-align:left">'
            f'<div class="brand-lockup" style="margin-bottom:22px"><img class="hero-logo" src="{LOGO}" alt="AUREA Hub" style="height:74px;width:auto"></div>'
            f'<span class="eyebrow"><span class="ob"></span>En una línea</span><h2>{closer_h2}</h2><p>{closer_p}</p></div><div class="closer-sphere"><img src="{SPHERE}" alt=""></div></section>'
            f'<footer><div class="fm"><span class="mini-orb"></span>AUREA Hub · Master Partner Oficial de Prometheo CRM</div><div>{footer_r}</div></footer>'
            f'{script}</main>\n')


def hero(eyes, h1, lead, items):
    e = ''.join(f'<span class="eyebrow"><span class="ob"></span>{x}</span>' for x in eyes)
    its = ''.join(f'<div class="hitem"><div class="hn">{IC[ic]}</div><div class="ht">{t}</div></div>' for ic, t in items)
    return (f'<section class="hero" style="--acc:#7C5CBF"><div class="brand-lockup"><img class="hero-logo" src="{LOGO}" alt="AUREA Hub"></div>'
            f'<div class="hero-eyebrows">{e}</div><h1>{h1}</h1><p class="lead">{lead}</p>'
            f'<div class="stack" style="margin-top:22px;gap:14px">{its}</div></section>')


def eco():
    return (f'<div class="eco"><div class="eco-row">'
            f'<div class="eco-col"><div class="eco-lbl">Generan</div><div class="eco-card cgen"><div class="eco-name">PAID PILOT</div>'
            f'<div class="eco-b">{IC["target"]}<span>Research y gate de budget</span></div><div class="eco-b">{IC["eye"]}<span>Tracking y auditoría de pauta</span></div></div></div>'
            f'<div class="eco-arrow"><span>leads</span>{IC["arrow"]}</div>'
            f'<div class="eco-col"><div class="eco-lbl">Convertimos</div><div class="eco-card ccon"><div class="eco-name">AUREA</div>'
            f'<div class="eco-b">{IC["robot"]}<span>Prometheo + metodología</span></div><div class="eco-b">{IC["chat"]}<span>Agente, prompts, testing</span></div></div></div>'
            f'<div class="eco-arrow"><span>ventas</span>{IC["arrow"]}</div>'
            f'<div class="eco-col"><div class="eco-lbl">Medimos</div><div class="eco-card cmed"><div class="eco-name">AUREA</div>'
            f'<div class="eco-b">{IC["trend"]}<span>Inteligencia Comercial</span></div></div></div>'
            f'</div></div>')


# ---------- contenido compartido ----------

DIAG = ('<section class="sec "><div class="diagbox"><div class="db-eye">Punto de partida · cómo trabaja AUREA hoy</div>'
        '<h3>Tenemos el método escrito. Falta la memoria y la columna que genera.</h3>'
        '<div class="db-lead">AUREA ya tiene su metodología en skills: discovery, calificación de leads, corrección de prompts, '
        'tableros de IC, costos de Prometheo y la estética de marca. Lo que todavía no tenemos resuelto son tres cosas, y cada repo '
        'resuelve una parte.</div><div class="gaps">'
        + gap('#E84545', 'Contexto que se pierde', 'Cada sesión con Claude arranca de cero: quién es el cliente, en qué ronda está, qué se decidió. Lo reexplicamos a mano.')
        + gap('#E84545', 'El dato de la pauta', 'La IC necesita que los anuncios lleguen identificados y medidos. Hoy dependemos de cómo trabaja cada agencia.')
        + gap('#E8943A', 'Mejora continua manual', 'Los aprendizajes de cada entrega se anotan a mano y no hay un chequeo periódico de la salud de las skills.')
        + '</div></div></section>')

CIRCLE = ('<div id="circulo"></div><section class="sec "><div class="circle-wrap"><div class="cw-eye">Dónde encaja cada repo</div>'
          '<h3>El Paid Pilot completa el círculo. El <em>Second Brain</em> lo sostiene.</h3>' + eco() +
          '<div class="cw-foot" style="margin-top:18px">El <strong>Second Brain</strong> no es una columna más: es la carpeta y las rutinas donde viven todos los clientes, '
          'las decisiones y las skills de AUREA, para que cada frente arranque sabiendo dónde está parado.</div></div></section>')

SB_WHAT = ('<section class="sec tv">' + head('Qué es', 'Una carpeta que Claude <em>lee al arrancar</em>.',
           'Archivos de texto plano, ordenados con el método PARA, con un índice maestro chico que le dice al agente dónde vive cada cosa. MIT, versión 3.5.0.')
           + grid(3, [feat('doc', 'Índice + carpetas', '<strong>CLAUDE.md</strong> como mapa, <strong>ESTADO.md</strong> como tablero, y carpetas Inbox, Proyectos, Áreas, Recursos y Archivo. Cada proyecto con su propio CLAUDE.md y log de decisiones.'),
                      feat('users', 'Un coach por escalones', '<strong>/brain-coach</strong> arma el sistema con vos, de a un nivel: identidad, primer proyecto, atajos, skill propia, rutina conectada, orquestador y auditoría.'),
                      feat('bolt', 'Toolkit de 24 comandos', 'Recetas listas desde el día uno: <strong>/brain-verify</strong>, <strong>/brain-decide</strong>, <strong>/brain-dreaming</strong>, <strong>/brain-panel</strong>, <strong>/brain-spec</strong>, entre otras. Se pueden tomar de a una.')])
           + '<div style="margin-top:16px">' + callout('bulb', 'Por qué funciona', 'El agente trae solo el archivo que la tarea necesita.',
                                                    'En vez de cargar todo, lee el índice y abre uno o dos archivos chicos. La ventana de contexto queda liviana y cualquier persona del equipo puede abrir y editar las piezas a mano. Corre en <strong>Cowork y Claude Code</strong>, y otros agentes lo leen vía AGENTS.md.') + '</div></section>')

SB_USES = [
    feat('store', 'Un proyecto por cliente', 'EDFAN, DRAKON, PAVIR, TKVA, EAF y MAMUT, cada uno con su CLAUDE.md: rubro, etapa, ronda de feedback, criterio de lead calificado y log de decisiones. Se termina el "te cuento de nuevo".'),
    feat('clock', '/brain-dreaming nocturno', 'Lee el día (Gmail, Calendar, reuniones en Granola, tareas) y deja en el log de cada cliente lo verificable. Lo que pide una decisión queda marcado, no se aplica solo.'),
    feat('check', '/brain-verify antes de mandar', 'Gate de cada entregable: chequea que cumpla lo pedido y fact-checkea números, fechas y claims. Es la regla de <strong>números defendibles</strong> convertida en paso obligatorio.'),
    feat('sliders', '/brain-decide para aprobaciones', 'Arma una botonera con el dato, la recomendación y el impacto de cada decisión. Encaja con el Doc 4 de discovery (preguntas clave de aprobación).'),
    feat('eye', '/brain-panel sobre propuestas', 'De 2 a 5 revisores con miradas distintas sobre una propuesta, un deck o un prompt antes de que salga al cliente.'),
    feat('refresh', '/brain-evalskill y /brain-audit', 'Formalizan la mejora continua: evalúan cada skill AUREA contra su propio SKILL.md y revisan la salud del sistema, con rutina semanal.'),
    feat('chat', '/brain-triage', 'Brief del día cruzando mail, calendario y tareas: qué cliente espera respuesta, qué reunión viene y qué entregable vence.'),
    feat('mail', '/brain-transcribe', 'Transcribe audios de reuniones con Whisper en la máquina local. Sirve para material de clientes que no queremos subir a la nube.'),
    feat('doc', '/brain-spec y /brain-messirve', 'Spec: el contrato numerado antes de un entregable. Messirve: el filtro para lo que llega de afuera (como estos dos repos) contra lo que ya tenemos.'),
]

SB_USE = ('<section class="sec tv">' + head('Usos concretos', 'Lo que <em>le resuelve</em> a AUREA.',
          'Las skills de AUREA siguen siendo la fuente de verdad del método. El brain les agrega memoria por cliente, rutinas y controles antes de entregar.')
          + grid(3, SB_USES) + '<div style="margin-top:16px" class="stack">'
          + callout('target', 'Cómo se conecta con lo que ya tenemos', 'Las skills AUREA entran en la tabla "Mis skills".',
                    'Cada skill existente (metodología, IC, prompts, estética, costos) queda registrada en el índice con su frase gatillo. El brain no las reemplaza: las ordena y las hace disparables desde cualquier proyecto de cliente.')
          + callout('frame', 'Lo que no tomamos', 'ppt-builder, redactar y publicar quedan afuera.',
                    'Para decks y propuestas ya tenemos <strong>aurea-estetica-documentacion</strong>, con su sistema de marca. Y <strong>publicar</strong> sube archivos a un host externo: con material de clientes bajo NDA, no lo activamos.')
          + '</div></section>')

SB_BEFORE = ('<section class="sec tv">' + head('Antes y después', 'La diferencia se nota <em>en la segunda sesión</em>.', 'Un pedido típico de AUREA, con y sin el brain.')
             + grid(2, [chan('chat', 'Hoy', 'Cada sesión arranca de cero.', [
                 'Pegamos el contexto del cliente, la ronda y el último prompt.',
                 'Buscamos a mano qué se acordó en la reunión anterior.',
                 'El aprendizaje de la entrega queda en el chat y se pierde.']),
                 chan('robot', 'Con el brain', 'El agente ya sabe dónde está parado.', [
                     '"Sacá la v13 del prompt de EDFAN": lee el CLAUDE.md del cliente y el log de feedback.',
                     'El dreaming ya cargó lo que se dijo en la reunión de ayer.',
                     '/brain-doc al cierre deja la decisión registrada para la próxima.'])])
             + '</section>')

PP_WHAT = ('<section class="sec tm">' + head('Qué es', 'Validar un canal pago <em>con un tope que corta</em>.',
           'Un playbook Lean Startup para correr un piloto chico en Google y Meta: cada etapa cierra con una decisión de seguir, pivotar o matar, con un número adelante. MIT, versión 1.7.2.')
           + hsteps([('1', 'doc', 'Plan', 'Qué se vende, a quién, budget y quién cierra.', 's0'),
                     ('2', 'globe', 'Research', 'Keywords, ads de competidores y tamaño de audiencia.', 's1a a s1d'),
                     ('3', 'dollar', 'Experimento', 'CAC contra LTV en 4 escenarios y gate de budget.', 's2a a s2c'),
                     ('4', 'bolt', 'Ejecución', 'Copy, landings, campañas y tracking.', 's3a a s3f'),
                     ('5', 'refresh', 'Operación', 'Reporte "cómo venimos", veredicto y postmortem.', 's4a y s4b')])
           + '<div style="margin-top:16px">' + grid(3, [
               feat('route', '16 pasos', 'Un orquestador fino y una skill por sub-etapa. Cada una se puede pedir suelta: "armá los números de X", "investigá los competidores de Y".'),
               feat('users', '6 roles de paid media', 'Google Ads, Meta Ads, creativos, tracking, analista de términos de búsqueda y auditor de cuentas. Sirven con campañas ya corriendo.'),
               feat('frame', '7 componentes', 'Lead magnet y nurture, cold outreach, A/B, captura y CRM, agendamiento, WhatsApp y GEO (aparecer citado en ChatGPT y Perplexity).')]) + '</div>'
           + '<div style="margin-top:16px">' + callout('bulb', 'La idea que más nos sirve', 'Derecho de piso contra impuesto evitable.',
                                                    'Hay gasto que es el precio de aprender lo que no se podía saber antes, y gasto desperdiciado que se corta desde el día uno. Y los <strong>kill criteria se acuerdan antes de prender</strong>, no cuando se acaba el presupuesto.') + '</div></section>')

PP_USES = ('<section class="sec tm">' + head('Usos concretos', 'Tres formas de <em>usarlo</em> en AUREA.',
           'De menor a mayor compromiso. Las dos primeras no cambian la oferta; la tercera es una decisión de negocio.')
           + grid(3, [
               ctype('timp', '01', 'Reforzar la Inteligencia Comercial', [
                   '<strong>tracking-specialist</strong>: UTMs, Pixel, CAPI y conversiones para que cada lead llegue con su anuncio identificado.',
                   '<strong>campaign-auditor</strong> y <strong>search-query-analyst</strong>: auditoría de la pauta de la agencia cada 4 semanas.',
                   '<strong>s2a</strong>: CAC contra LTV en escenarios, alineado con la skill de costos y rentabilidad.'], 'Ahora', 'timp'),
               ctype('timp', '02', 'Enriquecer el Paso 0 y el discovery', [
                   '<strong>s1c</strong>: swipe de los anuncios que corren los competidores del cliente (Meta Ad Library).',
                   '<strong>s1b</strong>: volúmenes de búsqueda y CPC del rubro en Google.',
                   'Llega a la primera reunión con un Doc 0 que ya sabe qué busca el mercado.'], 'Ahora', 'timp'),
               ctype('sel', '03', 'Un piloto propio de AUREA', [
                   'Validar con un tope de budget si Google o Meta nos traen clientes a un CAC que cierre.',
                   'Segmento candidato: desarrollistas de Buenos Aires y expositores de CAFIRA (ya tenemos las bases).',
                   '<strong>cold-outreach</strong> sobre esas bases, con volumen escalonado y freno automático.'], 'A decidir', 'sel')])
           + '<div style="margin-top:16px" class="stack">'
           + callout('target', 'Una tensión a resolver', 'Prometheo convierte demanda, no la genera.',
                     'Ofrecer "pilotos de canal" a clientes nos metería en el terreno de las agencias partner. La propuesta es usar el método <strong>junto con la agencia</strong>: ella opera la pauta, AUREA aporta el gate, el tracking y la lectura en IC.')
           + callout('frame', 'Lo que no tomamos', 'Los componentes de WhatsApp y CRM ya los resuelve Prometheo.',
                     'De <strong>canal-whatsapp</strong> y <strong>captura-y-crm</strong> rescatamos solo patrones (anti-loop, escalamiento a humano, upsert sin duplicados) para el diseño del agente. Las landings en Next y Vercel quedan para cuando haya capacidad de desarrollo.')
           + '</div></section>')

PP_REQ = ('<section class="sec tm">' + head('Qué necesita para correr', 'Accesos y <em>costos</em> antes de empezar.',
          'El método corre con cualquier asistente que lea markdown, pero varias etapas tocan APIs con credenciales.')
          + grid(3, [qcard('globe', 'Google Ads', 'Cuenta con <strong>Keyword Planner</strong> para volúmenes y CPC. Para un piloto propio, una cuenta de AUREA.'),
                     qcard('users', 'Meta', 'Token de <strong>Graph API</strong> para el tamaño de audiencias y acceso a Ad Library. Apify para el swipe de competidores (pago por uso).'),
                     qcard('sliders', 'Opcional', 'El clasificador en volumen (jev) es experimental y no hace falta: sin él, cada paso corre por su camino normal.')])
          + '</section>')

PLAN = ('<section class="sec tv">' + head('Plan de implementación', 'Cuatro fases, <em>de lo interno a lo nuevo</em>.',
        'Primero ordenamos cómo trabajamos. Después sumamos lo que fortalece la oferta actual. Al final, lo que abre algo nuevo. Cada fase cierra con un OK antes de la siguiente.')
        + grid(2, [
            ctype('timp', 'Fase 1 · semanas 1 y 2', 'Base del brain de AUREA', [
                'Instalar el plugin y armar identidad y voz de AUREA.',
                'Un proyecto por cliente activo, con su log de decisiones.',
                'Registrar las skills AUREA en "Mis skills" con sus frases.'], 'Interno', 'timp'),
            ctype('timp', 'Fase 2 · semanas 3 y 4', 'Rutinas y controles', [
                '/brain-triage diario y /brain-doc al cerrar cada sesión.',
                '/brain-dreaming conectado a Gmail, Calendar y Granola.',
                '/brain-verify como gate de todo entregable al cliente.'], 'Interno', 'timp'),
            ctype('tmc', 'Fase 3 · semanas 4 a 6', 'Paid Pilot dentro de IC', [
                'Checklist de tracking (UTMs, CAPI) en el onboarding de IC.',
                'Auditoría de pauta mensual con los roles auditor y analista.',
                'Research de keywords y ads de competidores en el Paso 0.'], 'Oferta actual', 'tmc'),
            ctype('sel', 'Fase 4 · semanas 6 a 10', 'Piloto propio de AUREA', [
                'Plan, research y modelo CAC contra LTV del segmento elegido.',
                'Kill criteria acordados antes de prender el primer gate.',
                'Postmortem y aprendizajes a la metodología, gane o pierda.'], 'A decidir', 'sel')])
        + '<p class="note" style="margin-top:12px;font-style:italic;color:var(--ink-3)">Los tiempos son de referencia, para un equipo chico trabajando en paralelo con los clientes.</p></section>')

KPIS = ('<section class="sec tv">' + head('Cómo sabemos si funciona', 'Tres <em>señales</em> para medir.',
        'Sin promesas de ahorro: medimos la línea de base en la Fase 1 y comparamos al cierre de cada fase.')
        + grid(3, [mcard('Contexto', 'Cero reexplicación', 'Sesiones de cliente que arrancan sin pegar contexto a mano'),
                   mcard('Calidad', '100% verificado', 'Entregables al cliente que pasan por /brain-verify antes de salir'),
                   mcard('Piloto', 'CAC medido', 'Veredicto del gate con un número adelante y postmortem escrito', True)], 'margin-bottom:12px')
        + '</section>')

RISKS = ('<section class="sec tv"><div class="diagbox"><div class="db-eye">Riesgos y cómo los cubrimos</div>'
         '<h3>Lo que hay que cuidar antes de instalar.</h3><div class="gaps">'
         + gap('#E84545', 'Datos de clientes', 'El brain vive en una carpeta sincronizada. Va en el Drive de AUREA con permisos del equipo, y el material bajo NDA no se publica.')
         + gap('#E8943A', 'Skills que se pisan', 'Algunos comandos se superponen con skills AUREA (decks, redacción). Regla: ante dos opciones, manda la skill de AUREA.')
         + gap('#E8943A', 'Mantenimiento', 'Los dos repos cambian seguido. Una persona revisa el changelog una vez por mes antes de actualizar.')
         + '</div></div></section>')

DECIDE = ('<div id="decisiones"></div><section class="sec tm">' + head('Para cerrar con el CTO', 'Cuatro <em>decisiones</em> pendientes.', 'Con esto resuelto arrancamos la Fase 1.')
          + grid(2, [qcard('users', '¿Un brain compartido o uno por persona?', 'Recomendamos <strong>uno compartido de AUREA</strong> (clientes y método) y una carpeta personal de identidad por persona.'),
                     qcard('target', '¿Piloto de canal como servicio?', 'Recomendamos empezar <strong>solo interno y con agencias partner</strong>, y decidir después del piloto propio.'),
                     qcard('dollar', '¿Budget del piloto propio?', 'A definir con el modelo CAC contra LTV de la Fase 4, con un primer gate chico y kill criteria por escrito.'),
                     qcard('refresh', '¿Quién mantiene el sistema?', 'Un responsable que corre /brain-audit los sábados y revisa el changelog de los repos una vez por mes.')])
          + '</section>')


def propuesta():
    nav = ('<nav class="topnav"><div class="nv-brand"><span class="mini-orb"></span>AUREA · Repos agénticos</div>'
           '<a class="v" href="#circulo">El círculo</a>'
           '<span class="sepv">SECOND BRAIN</span><a class="v" href="#sb-que">Qué es</a><a class="v" href="#sb-uso">Usos</a>'
           '<span class="sepv">PAID PILOT</span><a class="m" href="#pp-que">Qué es</a><a class="m" href="#pp-uso">Usos</a>'
           '<span class="sepv">·</span><a href="#plan">Plan</a><a href="#decisiones">Decisiones</a></nav>')
    secs = [hero(['AUREA · PROPUESTA INTERNA', 'RECOMENDACIÓN DEL CTO'],
                 'Dos repos para que AUREA <em>recuerde</em> y <em>valide antes de gastar</em>.',
                 'Analizamos agentic-second-brain y agentic-paid-pilot, de Bruno Gielczynsky, contra la metodología de AUREA. Acá va qué hace cada uno, en qué nos sirve, qué dejamos afuera y un plan de implementación en cuatro fases.',
                 [('doc', '<strong style="color:#2E5A9E">Agentic Second Brain:</strong> la memoria de AUREA. Clientes, decisiones y skills en una carpeta que Claude lee al arrancar.'),
                  ('target', '<strong style="color:#5B3E9E">Agentic Paid Pilot:</strong> el método para generar y validar demanda paga con un tope que corta, y para medir mejor la pauta.')]),
            DIAG, CIRCLE,
            '<section class="divider dv" id="sb"><div class="dv-eye">Parte 1 de 2</div><h2>Agentic Second Brain</h2><p>Cómo trabaja AUREA: memoria por cliente, rutinas y controles antes de entregar.</p></section>',
            band('bv', '01', 'doc', 'brunogiel/agentic-second-brain', 'Qué es', 'Un segundo cerebro en texto plano, armado con un coach, más un toolkit de comandos.', 'sb-que'),
            SB_WHAT,
            band('bv', '02', 'target', 'Aplicado a AUREA', 'En qué nos sirve', 'Nueve usos concretos sobre nuestra operación de consultoría e implementación.', 'sb-uso'),
            SB_USE, SB_BEFORE,
            '<section class="divider dm" id="pp"><div class="dv-eye">Parte 2 de 2</div><h2>Agentic Paid Pilot</h2><p>La columna que genera: research, gate de budget, tracking y auditoría de pauta.</p></section>',
            band('bm', '01', 'route', 'brunogiel/agentic-paid-pilot', 'Qué es', 'Un playbook de 5 etapas para validar un canal de adquisición digital con un tope de inversión.', 'pp-que'),
            PP_WHAT,
            band('bm', '02', 'target', 'Aplicado a AUREA', 'En qué nos sirve', 'Tres usos, de reforzar la IC a correr un piloto propio de adquisición.', 'pp-uso'),
            PP_USES, PP_REQ,
            band('bv', '03', 'route', 'La propuesta', 'Plan de implementación', 'Cuatro fases en diez semanas, con validación entre cada una.', 'plan'),
            PLAN, KPIS, RISKS, DECIDE]
    script = ('<script>document.documentElement.style.scrollBehavior="smooth";'
              'const links=[...document.querySelectorAll(".topnav a")];'
              'const map=links.map(a=>({a,t:document.querySelector(a.getAttribute("href"))})).filter(x=>x.t);'
              'const obs=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){const id="#"+e.target.id;links.forEach(l=>l.classList.toggle("active",l.getAttribute("href")===id));}})},{rootMargin:"-45% 0px -50% 0px"});'
              'map.forEach(x=>obs.observe(x.t));</script>')
    return page('Propuesta Repos Agénticos', nav, secs, 'Que AUREA <em>recuerde</em>, y que valide <em>antes de gastar</em>.',
                'El Second Brain ordena cómo trabajamos.<br>El Paid Pilot completa el círculo comercial.<br>Las skills de AUREA siguen siendo el método.',
                'Propuesta interna · Repos agénticos', script)


# ---------- presentación (modo slides) ----------

SLIDE_CSS = ('html{scroll-snap-type:y proximity}'
             '.slides>section{scroll-snap-align:start;min-height:100vh}'
             '.slides>section:not(.closer){display:flex;flex-direction:column;justify-content:center}'
             '.slides>section.closer{align-content:center}'
             '.slides>section.divider h2{font-size:clamp(40px,7vw,76px)}'
             '.slide-ctl{position:fixed;right:calc(16px + env(safe-area-inset-right,0px));bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:60;'
             'display:flex;gap:6px;align-items:center;background:rgba(251,250,254,.94);border:1px solid var(--line-2);border-radius:999px;padding:6px 8px;'
             'font:600 12px var(--hel);color:var(--ink-2);box-shadow:0 10px 26px -14px rgba(31,27,46,.4)}'
             '.slide-ctl button{border:0;background:var(--aurea-purple-50);color:var(--aurea-purple-deep);width:30px;height:30px;border-radius:50%;cursor:pointer;font:700 15px var(--hel)}'
             '.slide-ctl button:focus-visible{outline:2px solid var(--aurea-purple);outline-offset:2px}'
             '.slide-ctl span{min-width:52px;text-align:center;font-variant-numeric:tabular-nums}'
             '@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto!important}}')

SL_TWO = ('<section class="sec tv">' + head('Los dos repos en una frase', 'Uno para <em>recordar</em>, otro para <em>validar</em>.', 'Los dos son MIT, texto plano y se pueden adoptar por partes.')
          + grid(2, [chan('doc', 'Agentic Second Brain', 'La memoria de AUREA.', [
              'Una carpeta que Claude lee al arrancar: clientes, decisiones y skills.',
              'Un coach que lo arma por escalones y 24 comandos listos.',
              'Rutinas: brief del día, ciclo nocturno, verificación antes de mandar.']),
              chan('target', 'Agentic Paid Pilot', 'La columna que genera.', [
                  'Playbook Lean Startup de 5 etapas para un canal pago.',
                  'Gate de budget con kill criteria acordados antes de prender.',
                  '6 roles de paid media y 7 componentes de funnel reusables.'])]) + '</section>')

SL_SB_USE = ('<section class="sec tv">' + head('Second Brain aplicado a AUREA', 'Seis usos que <em>cambian el día a día</em>.', 'Las skills AUREA siguen siendo el método; el brain les suma memoria y controles.')
             + grid(3, SB_USES[:6]) + '</section>')

SL_PP_USE = ('<section class="sec tm">' + head('Paid Pilot aplicado a AUREA', 'Tres usos, <em>de menor a mayor compromiso</em>.', 'Las dos primeras refuerzan la oferta actual. La tercera es una decisión de negocio.')
             + grid(3, [qcard('trend', 'Reforzar la IC', 'Tracking (UTMs, CAPI) para que cada lead llegue con su anuncio, y <strong>auditoría de la pauta</strong> de la agencia cada 4 semanas.'),
                        qcard('globe', 'Enriquecer el Paso 0', 'Swipe de los anuncios de la competencia y volúmenes de búsqueda del rubro antes de la primera reunión.'),
                        qcard('target', 'Piloto propio', 'Validar con un tope si Google o Meta nos traen clientes (desarrollistas BA, CAFIRA) a un CAC que cierre.')])
             + '<div style="margin-top:16px">' + callout('frame', 'Lo que no tomamos', 'WhatsApp y CRM ya los resuelve Prometheo.',
                                                      'Rescatamos solo patrones para el diseño del agente. Y los pilotos para clientes, siempre <strong>junto con la agencia partner</strong>: Prometheo convierte demanda, no la genera.') + '</div></section>')

SL_PLAN = ('<section class="sec tv">' + head('La propuesta', 'Cuatro fases en <em>diez semanas</em>.', 'De lo interno a lo nuevo, con un OK entre cada fase.')
           + '<div class="tline">'
           + f'<div class="harrow">{IC["arrow"]}</div>'.join([
               '<div class="tl"><div class="tl-eye">Semanas 1 y 2</div><div class="tl-t">Base del brain</div><div class="tl-d">Identidad, un proyecto por cliente, skills AUREA registradas</div><div class="tl-v">Interno</div></div>',
               '<div class="tl"><div class="tl-eye">Semanas 3 y 4</div><div class="tl-t">Rutinas y controles</div><div class="tl-d">Triage, dreaming y verify como gate</div><div class="tl-v">Interno</div></div>',
               '<div class="tl"><div class="tl-eye">Semanas 4 a 6</div><div class="tl-t">Paid Pilot en IC</div><div class="tl-d">Tracking, auditoría de pauta, research en Paso 0</div><div class="tl-v">Oferta actual</div></div>',
               '<div class="tl acc"><div class="tl-eye">Semanas 6 a 10</div><div class="tl-t">Piloto propio</div><div class="tl-d">Gate de budget, kill criteria y postmortem</div><div class="tl-v">A decidir</div></div>'])
           + '</div></section>')

SL_DECIDE = ('<section class="sec tm">' + head('Para cerrar hoy', 'Cuatro <em>decisiones</em>.', 'Con esto resuelto arrancamos la Fase 1 la semana que viene.')
             + grid(2, [qcard('users', 'Brain compartido o por persona', 'Recomendamos uno compartido de AUREA y una carpeta personal de identidad por persona.'),
                        qcard('target', 'Pilotos como servicio', 'Recomendamos empezar solo interno y con agencias partner.'),
                        qcard('dollar', 'Budget del piloto propio', 'Sale del modelo CAC contra LTV de la Fase 4, con un primer gate chico.'),
                        qcard('refresh', 'Responsable del sistema', 'Una persona que audita los sábados y revisa los changelogs una vez por mes.')]) + '</section>')


def presentacion():
    secs = [hero(['AUREA · PRESENTACIÓN', 'REPOS RECOMENDADOS POR EL CTO'],
                 'Dos repos para que AUREA <em>recuerde</em> y <em>valide antes de gastar</em>.',
                 'Qué son, en qué nos sirven y cómo los implementamos. Usá las flechas del teclado o los botones de abajo para avanzar.',
                 [('doc', '<strong style="color:#2E5A9E">Agentic Second Brain</strong> · memoria, rutinas y controles.'),
                  ('target', '<strong style="color:#5B3E9E">Agentic Paid Pilot</strong> · generar y validar demanda paga con un tope.')]),
            DIAG, SL_TWO, CIRCLE,
            '<section class="divider dv"><div class="dv-eye">Parte 1 de 2</div><h2>Agentic Second Brain</h2><p>Cómo trabaja AUREA: memoria por cliente, rutinas y controles antes de entregar.</p></section>',
            SB_WHAT, SL_SB_USE, SB_BEFORE,
            '<section class="divider dm"><div class="dv-eye">Parte 2 de 2</div><h2>Agentic Paid Pilot</h2><p>La columna que genera: research, gate de budget, tracking y auditoría de pauta.</p></section>',
            PP_WHAT, SL_PP_USE, SL_PLAN, RISKS, SL_DECIDE]
    script = ('<div class="slide-ctl" aria-label="Navegación de diapositivas"><button id="sl-prev" type="button" aria-label="Anterior">‹</button>'
              '<span id="sl-n">1 / 1</span><button id="sl-next" type="button" aria-label="Siguiente">›</button></div>'
              '<script>(function(){const S=[...document.querySelectorAll(".slides>section")];const n=document.getElementById("sl-n");let cur=0;'
              'function upd(){n.textContent=(cur+1)+" / "+S.length;}'
              'function go(i){cur=Math.max(0,Math.min(S.length-1,i));S[cur].scrollIntoView({behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"});upd();}'
              'const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){cur=S.indexOf(e.target);upd();}})},{rootMargin:"-50% 0px -50% 0px"});S.forEach(s=>io.observe(s));'
              'document.getElementById("sl-prev").onclick=()=>go(cur-1);document.getElementById("sl-next").onclick=()=>go(cur+1);'
              'addEventListener("keydown",e=>{if(["ArrowRight","ArrowDown","PageDown"," "].includes(e.key)){e.preventDefault();go(cur+1);}'
              'else if(["ArrowLeft","ArrowUp","PageUp"].includes(e.key)){e.preventDefault();go(cur-1);}});upd();})();</script>')
    html = page('Presentación Repos Agénticos', '', secs, 'Que AUREA <em>recuerde</em>, y que valide <em>antes de gastar</em>.',
                'El Second Brain ordena cómo trabajamos.<br>El Paid Pilot completa el círculo comercial.<br>Las skills de AUREA siguen siendo el método.',
                'Presentación · Repos agénticos', script)
    return html.replace('<main class="container">', '<main class="container slides">').replace(PLATFORM_CSS + '</style>', PLATFORM_CSS + SLIDE_CSS + '</style>')


os.makedirs(OUT, exist_ok=True)
open(OUT + '/propuesta-repos-agenticos.html', 'w').write(propuesta())
open(OUT + '/presentacion-repos-agenticos.html', 'w').write(presentacion())
print('ok')
