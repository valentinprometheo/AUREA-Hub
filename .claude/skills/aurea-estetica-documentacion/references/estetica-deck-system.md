# AUREA Hub: sistema de diseño (referencia)

Referencia completa del lenguaje visual AUREA. El motor está en `assets/deck/aurea_kit.py`
(CSS canónico `AUREA_CSS`, set de íconos SVG, helpers, render a PDF). Este documento
explica el *porqué* y *cómo* de cada decisión para poder componer documentos nuevos.

## Tabla de contenido
1. Filosofía visual
2. Tokens de color
3. Tipografía
4. Layout: secciones full-bleed y bandas de gradiente
5. Componentes
5b. Componentes finos (recetas aprendidas)
6. Íconos
7. Esfera y orbe (decoración)
8. Recetas de assets (logo y esfera: recorte sin fondo)
9. Reglas de contenido (voz, idioma, tildes, saltos de línea)
10. Render y salida

---

## 1. Filosofía visual
Documento estilo "landing premium en una sola hoja": base **blanca**, secciones de
ancho completo separadas por **bandas de gradiente de marca sutiles (~15%)**, como los
sectores de una página web. El texto manda; el color y el espacio dividen y jerarquizan.
Tipografía Helvetica para todo, con una itálica de acento (serif) para una o dos palabras
por título. Íconos lineales finos en SVG. Una esfera iridiscente y un orbe orgánico como
únicos elementos "de marca" decorativos, siempre secundarios y detrás del contenido.

## 2. Tokens de color (`:root` en `AUREA_CSS`)
- Tinta: `--ink #1F1B2E`, `--ink-2 #4B4660`, `--ink-3 #8783A0`, `--ink-4 #B5B1C7`.
- Líneas: `--line rgba(31,27,46,.08)`.
- Marca: `--aurea-purple #7C5CBF` (+ `-deep #5A3F94`, `-50 #EDE7F8`, `-soft #F7F4FC`),
  `--aurea-blue #5B8FD9`, `--aurea-green #4CAF80`, `--aurea-coral #F37D6E`,
  `--aurea-orange #E8943A`, `--aurea-teal #3FA89E` (cada uno con su `-50`).
- El **gradiente de marca** (de la web) es azul → violeta → rosa. Se usa SIEMPRE de forma
  minimalista: bandas a ~15%, una card de acento a ~20%, y solo el bloque focal (ej. "más
  ventas") a plena intensidad con texto blanco. **Baja saturación siempre; nunca chicloso.**

**Recetas de color por sub-sector (cards de color sobre fondo blanco).** Cuando una
sección tiene varios sub-bloques que hay que distinguir, la sección va blanca y cada card
lleva un tinte distinto y de baja saturación, para que contrasten sin gritar:
- Jerarquía / arquitectura → naranja baja saturación:
  `linear-gradient(122deg, rgba(232,148,58,.20), rgba(243,125,110,.15) 58%, rgba(255,229,194,.34))`,
  borde `rgba(232,148,58,.32)`, label `#B26A1B`, `<em>` `#C2671C`, padding extra.
- Exploración / preguntas → violeta suave: `--aurea-purple-soft`, borde `rgba(124,92,191,.16)`.
- Síntesis / cierre de loop → azul desaturado y más gradiente:
  `linear-gradient(125deg, #5F84C4, #7A82BD 50%, #9586BB)`, texto blanco, `<em>` `#EFEAFF`.

**Badge secundario desaturado** (ej. "Próximamente"): relleno de marca de baja saturación
`linear-gradient(135deg, #A99AD0, #9385C2)` + texto blanco. Presente pero sutil, contraste
justo. Nunca el violeta pleno para algo secundario.

**Conector/acento celeste** (ej. el "+" que fusiona dos cards): `--aurea-blue` sobre
`--aurea-blue-50`, no violeta. El celeste es el acento "frío" de la paleta.

## 3. Tipografía
- Cuerpo y títulos: **Helvetica** vía `Arimo` (sustituto métrico que sí embebe en PDF). Variable `--hel`.
- Acento itálico: variable `--accent`. Hoy es `Fraunces` italic como **stand-in de "Rischie"**.
  Rischie no está en Google Fonts: para usarla, agregar un `@font-face` con el `.woff2/.otf`
  y cambiar `--accent: 'Rischie', serif;`. Mantener un grosor liviano (300) coherente.
- Jerarquía por tamaño + peso: `h1` 700 (clamp 34-54px), `h2` 600 (30px), eyebrow 700 / 11px /
  uppercase / tracking .18em. La itálica de acento va en `<em>` dentro del título (1-2 palabras).
- `text-wrap: balance` en todos los títulos para evitar palabras huérfanas.

## 4. Layout: secciones full-bleed y bandas
- `<main class="container">` no limita ancho; cada `<section>` es full-bleed y centra su
  contenido con `padding-inline: max(26px, calc((100% - 1080px)/2))`. Ancho de contenido ~1080px.
- **Bandas alternadas**: `section:nth-of-type(even)` lleva el gradiente de marca a ~15%;
  las impares quedan blancas. El hero tiene un wash radial propio. Esto crea la sensación
  de "sectores" tipo web. Resultado: aire + color dividen sección de sección.
- **Resaltar un bloque puntual**: usar `.card.accent` (gradiente ~20% + borde + sombra) o,
  dentro de una sección, subir el fondo de un solo recuadro. No abusar: minimalista.
- **Aire entre subsectores**: cuando una sección tiene 2-3 bloques apilados, dejar
  ~28-30px de margen entre ellos. Espacio + color son las dos herramientas para separar.

## 5. Componentes (clases en `AUREA_CSS`)
- **Hero**: `.brand-lockup`(solo el logo) → `.hero-eyebrows`(dos líneas eyebrow JUNTAS como
  subgrupo, separadas del logo arriba y del `h1` abajo) → `h1` → `.lead`.
- **Encabezado de sección**: `.sec-head` con `eyebrow()` (orbe + texto) + `h2` (+`<em>`) + `p`.
- **Cards**: `.card` (con `.card-h`+`.card-ic`+`h3`+`p`), `.card.accent` (resaltada),
  `.feat` (chip de ícono + label + título + desc).
- **Listas**: `.checks` (con `check()`), `.hl` para subrayar un área clave por párrafo.
- **Datos**: `.stat` (en `.grid-4`), `.focal` (un número focal con gradiente pleno + flecha),
  `.bigstat` (56px) + `.quote-panel` (panel con gradiente y cita en itálica).
- **Dispositivos**: `.device` (captura tipo navegador con barra de puntos), `.phone-float`
  (teléfono flotante con sombra), `.device-wide` (mockup ancho centrado).
- **Tabla**: `.atable` (encabezado tinta, primera col en `-soft`, celdas `.muted` para "fuera de alcance").
- **Pipeline**: `.pipeline` con `.pipe-stage` (la última `.s5` va en gradiente pleno).
- **Presupuesto**: `.budget-card` (`.main` oscura para el fee principal).
- **Contacto**: `.contact-card` con `.contact-ic` (cuadrado tinta + ícono blanco).
- **Logos**: `.logos` (escala de grises, opacidad .74).
- **Cierre**: `.closer` (grid: esfera a un lado + texto a la derecha, sobre BLANCO).
- **Footer**: `<footer>` con `.mini-orb`.

## 5b. Componentes finos (recetas aprendidas)
- **Card de precio.** Número grande SIEMPRE en la itálica de acento (`--accent`), nunca en
  Helvética dura. Cero espacio blanco: `display:flex;flex-direction:column;justify-content:space-between`;
  agrupar arriba (label + precio + bullets) en un `<div>` y dejar la nota de cierre abajo
  como pie con divisor (`border-top` + `padding-top`). Alinear horizontalmente con la card
  vecina dándole un **label gemelo** (ej. "Precio por canal" frente a "Canales activos hoy")
  para que precio y badge caigan en la misma línea que la fila clave de la otra card. El
  precio y el badge secundario (ej. "USD 550 por 2 canales") van en una fila con
  `space-between`, centrados verticalmente.
- **Hero lead en frases-renglón.** Cada frase en su `<span>` block con `white-space:nowrap`
  (fuerza un renglón en el ancho del deck), negrita en el concepto que abre cada frase;
  resetear `nowrap` en el media query `<880px`. Aire generoso entre logo y eyebrows (~46px
  en `.brand-lockup`).
- **Banda teaser de producto.** El nombre del producto en su propio renglón (el 2 de 3),
  grande, en itálica de acento, blanco. La banda crece lo mínimo. Estructura: gancho →
  nombre (grande, itálico) → bajada. Mantener la flecha/ícono centrado vertical con todo el
  bloque.
- **Pie "Deja:" / footer de card a 2 renglones.** Interlineado `>=1.6` y `min-height` para
  que el pie de cards hermanas caiga en la misma línea.
- **Palabra de acento en listas.** Para más jerarquía, la itálica de acento sube a peso 400
  y +1px de tamaño (Fraunces trae 300 y 400 italic).
- **Cierre.** Coma para respirar y la clausula resolutiva entera en `<em>` (italica de
  acento). Ej: "De un asistente que responde, <em>a un negocio que vende mejor</em>.".

## 6. Íconos
- SIEMPRE inline SVG (`icon("nombre")` / `check()`), **nunca** un icon-font/CDN: la fuente
  no carga del lado del cliente y aparecen cuadraditos vacíos. El SVG embebido siempre rinde
  y hace el archivo portable.
- Tamaño por `font-size` del contenedor (el `.ic` usa `width:1em`). Color por `currentColor`.
- Cada recuadro lleva ícono coherente con su título. Set disponible en `ICON_NAMES`
  (world, users, briefcase, headset, bolt, trending-up, adjustments, target, scale, smile,
  mail, phone, map-pin, route, messages, refresh, robot, eye, coin, file-text, receipt, bulb,
  sparkles, building-community, building-store, clock, whatsapp, check, arrow-right).

## 7. Esfera y orbe
- **Orbe orgánico** (`.ob`): bullet ANTES de cada eyebrow. No es un círculo: forma blob con
  border-radius irregular y gradiente de marca de relleno.
- **Esfera iridiscente** (`SPHERE`): elemento secundario, SIEMPRE detrás del contenido
  (nunca delante de texto/cards). Usos: en el hero, chica y casi fuera de la página a la
  derecha (`.sphere-hero`); en el cierre, grande de un lado con el texto a la derecha.
  Usarla "cada tanto", no en cada sección.

## 8. Recetas de assets (recorte sin fondo)
Las imágenes embeben como data URI (PNG con alfa) para que el HTML/PDF sea portable.

**Logo** (viene sobre un damero casi blanco → "neutral key"): alfa = max(alfa por saturación
[sat>8..20], alfa por oscuridad [min-channel<220..180]). Conserva navy + color, borra el gris/blanco.

**Esfera** (viene sobre negro → máscara circular, la forma más limpia): 1) des-premultiplicar
sobre negro (`rgb = observado/alfa`) para limpiar el color del borde; 2) detectar centro y radio
por brillo; 3) dibujar un círculo anti-aliased con radio *0.99 (achicar un toque para comerse
cualquier resto oscuro del borde); 4) recortar al bounding box. Nunca dejar dejos negros.

Para regenerar con otra imagen, reusar el patrón PIL/numpy de estas recetas (PNG, LANCZOS,
GaussianBlur ~0.8 para el feather del círculo).

## 9. Reglas de contenido
- Español **rioplatense con voseo** en todo (vos, tenés, podés).
- **Cero em-dashes** en cualquier texto: usar comas, puntos o paréntesis.
- "AUREA" sin tilde en el cuerpo (nunca ÁUREA).
- **Tildes**: auditar SIEMPRE (acción, configuración, metodología, días, años, etc.).
- **Saltos de línea armónicos**: ningún título debe dejar una palabra huérfana sola en el
  segundo renglón (usar `text-wrap: balance` y, si hace falta, reescribir). Espaciado vertical
  parejo entre elementos apilados (logo → eyebrow → título); separar subgrupos con claridad.
- **Voz de colega senior:** directa, sin jerga corporativa, sin relleno. Verbos precisos y
  profesionales, nunca agresivos ni folklóricos (ej. "Detectamos", no "Cazamos"; sin
  metáforas de caza/pelea).
- **Síntesis:** una idea por renglón. En la bajada del hero, una frase por renglón con la
  negrita en el concepto que abre cada frase.
- **Números defendibles, no promesas.** Baselines realistas (el costo "a mano" se ancla en
  el piso real de mercado; un sueldo de entrada en IT no baja de ~USD 1.200/mes). Si cambia
  un número, revisar los porcentajes derivados. Cerrar con "valores de referencia, no promesas".
- **Títulos de sección que nombran el producto** cuando se presenta algo nuevo (ej.
  "Inteligencia Comercial.", no un claim ingenioso). El claim, de sublead.
- **Arquitectura de marca (no confundir):** AUREA Hub = paraguas y ecosistema; Prometheo =
  producto activo (sustancia y narrativa); consultoría = capa UX/CUX/estrategia. Usar
  Prometheo como sustancia sin reducir AUREA a Prometheo.
- Si el documento es de Prometheo: Prometheo ordena y convierte demanda existente, no la
  genera (eso es Bardo). Plan pendiente de unificar: USD 149 vs 150.

## 10. Render y salida
- **Entregable por defecto: HTML.** El PDF de una sola hoja se genera SOLO con aprobación
  del cliente.
- **PDF canónico:** `render_single_page_pdf()` del kit = screenshot full-page (Playwright,
  1200px, `device_scale_factor=2`) → `img2pdf`. Una página, sin pérdida, gradientes intactos.
- **Nunca** el motor de impresión de Chromium (`page.pdf`): rompe los gradientes en la
  segunda columna de los grids. `render_single_page_pdf_chromium()` queda solo de referencia.
- **QA por chunks** antes de entregar: `screenshot_html()` y revisar tildes, huérfanas,
  alineaciones, íconos y contraste, por tramos. Corregir y re-renderizar.
- **Correcciones aditivas, aisladas y no regresivas:** tocar solo lo pedido; aclarar qué
  cambió y qué no.
