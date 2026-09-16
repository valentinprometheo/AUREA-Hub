# 04 · Presentación estética (deck HTML de marca)

> Familia de output: propuestas, guías y decks one-pager con diseño gráfico de marca AUREA. Estética: landing premium en una hoja (gradiente azul-violeta-rosa de baja saturación, esfera iridiscente, Helvetica + itálica de acento). **Salida HTML por defecto; PDF solo con aprobación.** No inventar otra estética: esta es la única para esta familia.

Las reglas transversales (voseo, cero em-dashes, AUREA sin tilde, correcciones aditivas) viven en el SKILL.md del conductor; acá están las reglas y recetas **propias de esta estética**, que son las que no se negocian. El detalle completo de tokens, componentes y recetas de assets está en `references/estetica-deck-system.md`.


Construí documentos de marca AUREA (propuestas, guías, decks de una hoja) con un
lenguaje visual consistente. Todo el motor (CSS canónico, íconos SVG, assets de
marca, render) vive en `assets/deck/aurea_kit.py`. La referencia completa del sistema
está en `references/estetica-deck-system.md`, leela cuando necesites el detalle de tokens,
componentes o las recetas de assets.

## Qué es la estética en una frase
Landing premium en una sola hoja: base blanca, secciones full-bleed separadas por
bandas de gradiente de marca sutiles (~15%) como una web, Helvetica + una itálica de
acento, íconos SVG finos, orbe orgánico en los eyebrows y una esfera iridiscente
secundaria detrás del contenido.

## Salida y render (regla del proyecto, no negociable)
- **El entregable por defecto es el HTML.** El PDF de una sola hoja se genera SOLO
  cuando el cliente lo aprueba.
- **PDF por el camino canónico: screenshot full-page (Playwright, 1200px,
  device_scale_factor=2) hacia img2pdf** (sin pérdida, una página a la altura total).
  Usá `render_single_page_pdf()` del kit, que ya hace exactamente esto.
- **Nunca con el motor de impresión de Chromium** (`page.pdf`): rompe los gradientes,
  sobre todo en la segunda columna de los grids. (`render_single_page_pdf_chromium`
  queda solo como referencia histórica, no usar.)
- Antes de entregar: render del HTML con `screenshot_html()` y **QA por chunks**
  (tildes, huérfanas, alineaciones, íconos, contraste, esfera detrás). Corregí y
  volvé a renderizar.

## Voz y síntesis (editorial)
- **Voseo rioplatense** en todo (vos, tenés, podés). **Cero em-dashes**: comas,
  puntos o paréntesis. **"AUREA" sin tilde** en el cuerpo. **Auditar TODAS las tildes**
  antes de entregar.
- **Voz de colega senior:** directa, sin jerga corporativa, sin relleno.
- **Verbos precisos y profesionales, nunca agresivos ni folklóricos.** Ej: "Detectamos"
  los errores, no "Cazamos". Evitar metáforas de caza o pelea.
- **Síntesis: una idea por renglón.** En la bajada del hero, una frase por renglón,
  con la negrita en el concepto que abre cada frase. Cada renglón cierra en punto y no
  deja huérfanas.
- **Números defendibles, no promesas.** Los baselines tienen que ser realistas: el
  costo "a mano" se ancla en el piso real de mercado (un sueldo de entrada en IT no baja
  de ~USD 1.200/mes, no lo subestimes). Cerrá con "valores de referencia, no promesas".
  Si cambia un número, revisá los porcentajes que dependen de él (ahorro, etc.).
- **Títulos de sección que NOMBRAN el producto** cuando se presenta algo nuevo. Ej:
  h2 "Inteligencia Comercial.", no un claim ingenioso ("Saber qué funciona, sin
  adivinar."). El claim ingenioso, si suma, va de sublead. Claridad sobre ingenio en
  secciones de producto.
- **Cierre con ritmo:** una coma para respirar, y la cláusula resolutiva entera en la
  itálica de acento. Ej: "De un asistente que responde, *a un negocio que vende mejor*."
  Valor recurrente de cierre: "Venimos a potenciar lo humano. La tecnología es un
  copiloto, no un reemplazo."
- **Arquitectura de marca (no confundir):** AUREA Hub = marca paraguas y ecosistema
  futuro. Prometheo = producto activo (sustancia y narrativa comercial). La capa de
  consultoría = UX/CUX/estrategia. Usá Prometheo como sustancia y dirección sin reducir
  AUREA a Prometheo.

## Reglas no negociables (estructura y forma)
- **Íconos siempre en SVG inline** (`icon()` / `check()`), nunca un icon-font/CDN: la
  fuente no carga del lado del cliente y salen cuadraditos vacíos.
- **Ritmo y alineación del texto (regla estética, no negociable):**
  - **Todo a la izquierda.** Cuerpo, listas, bajadas y notas se alinean a la izquierda.
    Dentro de una misma sección no conviven alineaciones distintas. Único centrado
    permitido: cards de un solo número focal (stat) como patrón deliberado y consistente;
    nunca texto corrido ni listas. Si una card tiene lista o párrafo, va a la izquierda
    completa (precio incluido).
  - **Cierre de renglón.** Cada renglón cierra en punto, o queda deliberadamente más
    corto que el anterior. Prohibidas las huérfanas (una palabra colgada en el último
    renglón de un título o párrafo). Si un título deja huérfana, se reescribe o se ajusta
    ancho/quiebre (`text-wrap: balance/pretty` o `<br>` manual).
  - **Interlineado y espaciado parejos.** El espacio entre renglones y entre elementos
    apilados es uniforme dentro del mismo bloque. En el hero, las dos líneas de eyebrow
    van JUNTAS como subgrupo, separadas del logo arriba (dejar aire generoso, ~46px) y
    del título abajo.
  - **Números en grilla = nivelados.** En tableros/stats con varias columnas, los números
    arrancan a la misma altura (label de alto fijo) y los badges/deltas quedan nivelados
    entre sí. Nunca escalonados por largo de label. Gap fijo entre número y badge.
  - **Sin espacio blanco en cards:** el contenido llena de punta a punta. Si sobra alto,
    distribuir con `space-between` (y anclar la nota de cierre como pie con divisor para
    que la distribución lea deliberada) o sumar contenido. Nunca dejar un vacío colgando.
  - **Alineación pixel perfect (checklist):**
    - Íconos de bullet centrados ópticamente con su primera línea; columna de ícono de
      ancho fijo para que el texto arranque siempre en la misma x.
    - Filas de chips/tags ocupan TODO el ancho del recuadro, distribuidas con
      `space-between`, nunca amontonadas a un costado dejando vacío.
    - Cards vecinas: alinear los tops y los divisores internos. Si el contenido difiere en
      altura, igualar con `min-height` para que los divisores/"Deja:" caigan en la misma
      línea.
    - Cards lado a lado: el elemento de mayor jerarquía de cada una (precio grande, fila
      clave, título) arranca a la misma altura horizontal. Para emparejarlas, darle a la
      card de precio un **label gemelo** del de la card vecina (ej. "Precio por canal"
      frente a "Canales activos hoy"), no a ojo.
    - Badges/etiquetas junto a un eyebrow o título van 100% centrados verticalmente con
      él (misma línea), con márgenes en cero.
  - **Antes de entregar**, revisar línea por línea: izquierda coherente, sin huérfanas,
    sin renglones que rompan el ritmo, números y badges nivelados, íconos y divisores al
    pixel.
- **Gradiente minimalista, baja saturación** (ver "Color, fondos y contraste").
- **Esfera**: secundaria y SIEMPRE detrás del contenido (nunca delante de texto/cards).

## Color, fondos y contraste
- **Gradiente de marca** azul, violeta, rosa, SIEMPRE de baja saturación. Bandas a
  ~15%, una card de acento a ~20%, y solo el bloque focal a plena intensidad con texto
  blanco. Nunca "chicloso".
- **Diferenciar sub-sectores con cards de color sobre fondo BLANCO**, no una sección de
  color con cards planas. Cuando una sección presenta varios sub-bloques que hay que
  distinguir, la sección va blanca y cada card lleva un tinte distinto y de baja
  saturación, para que contrasten sin gritar. Recetas validadas:
  - **Jerarquía / arquitectura**: gradiente naranja de baja saturación
    `linear-gradient(122deg, rgba(232,148,58,.20), rgba(243,125,110,.15) 58%, rgba(255,229,194,.34))`,
    borde `rgba(232,148,58,.32)`, label `#B26A1B`, `<em>` `#C2671C`. Más padding para
    subir jerarquía.
  - **Exploración / preguntas**: tinte violeta suave `--aurea-purple-soft`, borde
    `rgba(124,92,191,.16)`.
  - **Síntesis / cierre de loop**: azul desaturado y más gradiente
    `linear-gradient(125deg, #5F84C4, #7A82BD 50%, #9586BB)`, texto blanco, `<em>`
    lavanda muy claro `#EFEAFF`.
  - La regla: cada sub-sector, un color distinto = el lector entiende al toque que "esto
    es otra cosa".
- **Badges secundarios desaturados.** Un badge tipo "Próximamente" va con relleno de marca
  de baja saturación (`linear-gradient(135deg, #A99AD0, #9385C2)`) y texto blanco:
  presente pero deliberadamente sutil, con contraste justo. Nunca el violeta pleno para
  algo secundario (grita demasiado).
- **Conector/acento celeste.** Los elementos conectores (ej. el "+" que fusiona dos cards)
  van en el celeste del logo (`--aurea-blue` sobre `--aurea-blue-50`), no siempre en
  violeta. El celeste es el acento "frío" de la paleta.
- **Texto blanco sobre color:** contraste suficiente para leer; para elementos secundarios
  puede ser "lo justo" si se busca a propósito que no llame la atención.

## Recetas de componentes finos (lo aprendido)
- **Card de precio (regla, no opción):** el número grande SIEMPRE en la itálica de acento
  (Fraunces), nunca en Helvética dura (queda "muy duro"). Cero espacio blanco: `flex`
  column + `space-between`, agrupar arriba (label + precio + bullets) y dejar la nota de
  cierre abajo como pie con divisor (`border-top` + `padding-top`). Alinear con la card
  vecina vía label gemelo. Precio principal y badge secundario (ej. "USD 550 por 2
  canales") en una fila con `space-between`, centrados verticalmente.
- **Hero lead en frases-renglón:** cada frase en su `<span>` block con `white-space:nowrap`
  (fuerza un renglón en el ancho del deck), negrita en el concepto que abre cada frase,
  resetear `nowrap` por debajo de 880px. Aire generoso entre logo y eyebrows.
- **Banda teaser de producto:** al presentar un producto nuevo dentro de una banda de
  gradiente, el NOMBRE del producto va en su propio renglón (el 2 de 3), grande, en
  itálica de acento, blanco. La banda crece solo lo mínimo. Estructura: gancho, nombre
  (grande, itálico), bajada explicativa.
- **Pie "Deja:"/footer de card a 2 renglones:** interlineado `>= 1.6` y `min-height` para
  que el pie de cards hermanas caiga en la misma línea.
- **Palabra de acento en listas:** para más jerarquía, subir la itálica de acento a peso
  400 y +1px de tamaño (Fraunces trae 300 y 400 italic).

## Flujo de trabajo
1. Copiá `assets/deck/` a tu directorio de trabajo (trae `aurea_kit.py`, `logo.txt`, `sphere.txt`) y agregalo al path.
2. Escribí el HTML interno: una serie de `<section>` usando las clases del sistema
   (ver `references/estetica-deck-system.md` §5). Empezá por `hero`, terminá con `closer` + `<footer>`.
   - Eyebrows con `eyebrow("texto")` (incluye el orbe orgánico).
   - Una o dos palabras del título en `<em>` (itálica de acento).
   - Cada recuadro con un ícono coherente: `icon("nombre")`. Set en `aurea_kit.ICON_NAMES`.
   - Logo del hero: `<img class="hero-logo" src="{LOGO}">`. Esfera: `SPHERE`.
3. Envolvé con `aurea_page(title, inner_html)` y guardá el `.html`. **Ese es el entregable.**
4. **QA:** `screenshot_html("doc.html","full.png")` y revisá por chunks. Corregí y repetí.
5. **PDF solo con aprobación:** `render_single_page_pdf("doc.html","doc.pdf")` (screenshot
   + img2pdf). Nunca el motor de impresión de Chromium.
6. Entregá con `present_files` (el HTML siempre; el PDF cuando se aprobó).

**Correcciones:** siempre aditivas, aisladas y no regresivas. Tocá solo lo pedido, no
debilites lo que ya funciona, y al entregar aclará qué cambió y qué NO se tocó.

## Estructura típica de un documento
`hero` (logo + subgrupo de eyebrows + h1 con acento + lead), secciones de contenido
(`.sec-head` + grids de `.card`/`.feat`/`.stat`, tablas `.atable`, `.pipeline`, `.device`,
`.bigstat`+`.quote-panel`, `.focal`, `.budget-card`, cards de precio), `closer` (esfera +
texto a la derecha, sobre blanco), `<footer>`. Las bandas de color se alternan solas por
`nth-of-type`.

## Ejemplo mínimo
```python
import sys; sys.path.insert(0, "assets/deck")
from aurea_kit import aurea_page, render_single_page_pdf, screenshot_html, eyebrow, icon, check, LOGO, SPHERE

inner = f'''
<section class="hero">
  <div class="brand-lockup"><img class="hero-logo" src="{LOGO}"></div>
  <div class="hero-eyebrows">
    {eyebrow("Master Partner Oficial de Prometheo")}
    {eyebrow("Propuesta · Junio 2026")}
  </div>
  <h1>Diseñamos una estrategia para que <em>vendas más</em>.</h1>
  <p class="lead">Primero ordenamos el outbound que ya hacés, liberamos al equipo para cerrar.</p>
  <div class="sphere-side sphere-hero"><img src="{SPHERE}"></div>
</section>

<section class="sec">
  <div class="sec-head">{eyebrow("Cómo cambia la operación")}
    <h2>Tres frentes que cambian el <em>día a día</em>.</h2></div>
  <div class="grid-3">
    <div class="feat"><div class="feat-ic">{icon("messages")}</div>
      <div class="feat-label">Atención</div><div class="feat-title">Una sola interfaz</div>
      <div class="feat-desc">Todos los canales entran a un solo lugar.</div></div>
    <div class="feat"><div class="feat-ic">{icon("robot")}</div>
      <div class="feat-label">Calificación</div><div class="feat-title">Un agente que califica solo</div>
      <div class="feat-desc">Al equipo solo le llegan oportunidades reales.</div></div>
    <div class="card accent"><div class="card-h"><div class="card-ic">{icon("refresh")}</div>
      <h3>Seguimientos</h3></div><p>El sistema recontacta al que se enfría. Nada se cae.</p></div>
  </div>
</section>

<section class="closer">
  <div class="closer-sphere"><img src="{SPHERE}"></div>
  <div class="closer-text">{eyebrow("En una línea")}
    <h2>Ordenamos la venta y dejamos el terreno listo para <em>escalar</em>.</h2>
    <p>No vendemos una herramienta suelta, diseñamos el proceso para <strong>vender más</strong>.</p>
  </div>
</section>

<footer><div class="fm"><div class="mini-orb"></div><span>AUREA Hub · Master Partner Oficial de Prometheo CRM</span></div>
  <span>aureahub.com.ar</span></footer>
'''

html = aurea_page("AUREA · Propuesta", inner)
open("propuesta.html","w",encoding="utf-8").write(html)   # entregable por defecto
screenshot_html("propuesta.html","full.png")              # QA por chunks
# render_single_page_pdf("propuesta.html","propuesta.pdf")  # SOLO con aprobación
```

## Cambiar/agregar assets
- Para una **fuente Rischie** real: agregar `@font-face` (woff2/otf) vía `extra_css` en
  `aurea_page(...)` y poner `--accent:'Rischie',serif`.
- Para recortar un **logo o esfera nuevos** sin fondo, seguir las recetas de
  `references/estetica-deck-system.md` §8 (neutral-key para logo sobre damero; máscara circular
  para esfera sobre negro). Guardar el data URI en un `.txt` y reemplazar `LOGO`/`SPHERE`.
- Para incrustar **capturas de pantalla** (dashboards, teléfonos), embeberlas como data URI
  (JPEG si son opacas, PNG si tienen transparencia) y montarlas en `.device` / `.phone-float`.

## Notas
- Las fuentes (Arimo + Fraunces) se cargan por link de Google Fonts; el screenshot espera a
  `networkidle` antes de capturar.
- Dependencias del render: `playwright` (+ chromium) e `img2pdf`.
- Si el documento es de Prometheo, recordá: Prometheo ordena y convierte demanda existente,
  no la genera (eso es Bardo). Plan pendiente de unificar: USD 149 vs 150.
