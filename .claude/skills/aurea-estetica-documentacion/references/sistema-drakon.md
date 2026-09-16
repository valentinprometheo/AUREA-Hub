# Sistema de diseño DRAKON (el canónico para decks)

Este es el sistema **real** con el que está hecho el deck de DRAKON, y es el que hay que
usar para que un documento salga como DRAKON (bandas oscuras, price cards, callouts,
íconos, paleta completa). Vive en `assets/deck/aurea-drakon.css` (43 KB) y su ejemplo de
oro completo es `assets/ejemplos/drakon-ventas-marketing.html`. Un demo mínimo validado:
`assets/ejemplos/demo-sistema-drakon.html`.

## La regla fundamental (misma doctrina que el NDA): CLONAR, no reconstruir

**No armes un deck a mano desde cero ni con un kit reducido.** El error caro y repetido es
inventar clases o usar una versión pobre del CSS: sale pelado, sin íconos, sin bandas, sin
paleta. En vez de eso:

1. **Cloná** `assets/ejemplos/drakon-ventas-marketing.html` (o el demo mínimo) a tu carpeta.
2. Mantené intactos el `<head>` (los 3 links de fuente), el `<style>` (o el `<link>` a
   `aurea-drakon.css`), el contenedor `<main class="container">` con la `<nav class="topnav">`,
   y la estructura de secciones con sus clases.
3. **Reemplazá solo el contenido** (textos, números, íconos por otro del set) usando las
   MISMAS clases. No cambies los nombres de clase, no inventes clases nuevas.
4. Render y QA (abajo). Si un ícono sale como cuadradito o una banda sale blanca, es que se
   rompió una clase o el contenedor: volvé a la estructura de DRAKON.

Por qué: el CSS depende de nombres de clase y de un contenedor exactos. El contenedor es
`<main class="container">` (NO `.wrap`, que no existe y rompe el ancho y las bandas).

## Contenedor y estructura base

```html
<body>
<main class="container">
  <nav class="topnav">...índice navegable (opcional pero recomendado en el deck largo)...</nav>
  <section class="hero"> ... </section>
  <section class="sec band bv"> ... </section>     <!-- banda oscura azul -->
  <section class="sec"> ...grids de cards... </section>
  ...
</main>
</body>
```

`<head>`: los 3 `<link>` de Google Fonts (Arimo + Fraunces) y el CSS. Copialos de DRAKON tal cual.

## Vocabulario de componentes (clases REALES, con markup de ejemplo)

Todos salen de DRAKON. Copiá el snippet y cambiá el contenido.

### Eyebrow (con orbe) + encabezado de sección
```html
<div class="sec-head">
  <span class="eyebrow"><span class="ob"></span>Cómo entra la demanda hoy</span>
  <h2>Consultas por todos lados, <em>cargadas a mano</em>.</h2>
  <p>Lo que se ve en la operación comercial, antes de tocar nada.</p>
</div>
```

### Banda numerada (oscura) · `band bv` (azul) / `band bm` (violeta)
Fondo oscuro, número grande, ícono en caja, título blanco. Es lo que da el "peso" a DRAKON.
```html
<section class="sec band bv">
  <div class="band-in">
    <div class="band-num">01</div>
    <div class="band-ic"><svg class="ic" ...>...</svg></div>
    <div>
      <div class="band-eye">Qué encontró AUREA</div>
      <div class="band-title">Diagnóstico de la operación</div>
      <div class="band-sub">Canales dispersos y sin trazabilidad de qué consulta cierra.</div>
    </div>
  </div>
</section>
```

### Feature card · `feat` (ícono en caja con gradiente + título + desc)
```html
<div class="grid-3">
  <div class="feat"><div class="feat-ic"><svg class="ic" ...>...</svg></div>
    <div class="feat-title">3 canales dispersos</div>
    <div class="feat-desc">WhatsApp, Instagram y mail, cargados a mano.</div></div>
  ... (3 en el grid) ...
</div>
```

### Callout · `callout` (bloque destacado con ícono grande)
```html
<div class="callout"><div class="c-ic"><svg class="ic" ...>...</svg></div>
  <div><div class="c-eye">La base arranca en Mercado Libre</div>
  <div class="c-title">De ahí se nutre Prometheo.</div>
  <div class="c-desc">Texto explicativo con <strong>negritas</strong>.</div></div></div>
```

### Price card · `price` (clara) / `price dark` (oscura, foco)
```html
<div class="price dark"><div class="price-title">Consultoría e implementación</div>
  <div class="price-val">USD 850 / mes</div>
  <ul><li>{check}<span>Discovery, diseño del CRM y del agente</span></li>
      <li>{check}<span>Integración de canales y calificación</span></li></ul></div>
```
Variante clara agrega `<div class="price-lbl">Plataforma</div>` arriba y `<div class="price-usd">nota</div>`.

### Lista con checks · `checks` (viñeta = círculo relleno con tilde blanca)
```html
<ul class="checks"><li>{check}<span>Ítem uno</span></li><li>{check}<span>Ítem dos</span></li></ul>
```
El check es: `<svg class="ic" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" fill="currentColor"/><path d="M8 12.5l2.5 2.5 5-5.5" stroke="#fff" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>`

### Otros componentes disponibles (mismo criterio, ver DRAKON para el markup exacto)
- **`cc` / `cc-ic` / `cc-t` / `cc-v`** — card de canal (ej. "UN CANAL INCLUIDO · USD 200/mes").
- **`hs` / `hs-n` / `hs-ic` / `hs-t` / `hs-d` / `hs-tag`** — hotspot numerado (pasos con pill).
- **`mline` / `md` / `ml-label` / `leader` / `ml-val`** — renglón de precio con línea de puntos.
- **`ctype` / `ct-n` / `ct-t`** — tarjeta de etapa/tipo con checks.
- **`eco` / `eco-b`** — diagrama de ecosistema (Generan → Convertimos → Medimos).
- **`pill acc`** — etiqueta chica de acento. **`ob`** — orbe del eyebrow. **`mini-orb`** — orbe del footer/nav.
- **`pipeline`** (embudo) — usar el markup de DRAKON, NO inventar `pipe-step`.

## Íconos (set real: 20 íconos inline `<svg class="ic">`)

Los íconos son SVG inline con `class="ic"`, `viewBox="0 0 24 24"`, `stroke="currentColor"`,
`stroke-width="1.85"` (estilo Tabler). Toman el color del contexto (blanco en bandas, violeta
en cajas). **Nunca** un icon-font ni CDN (salen cuadraditos vacíos del lado del cliente).
Para conseguir uno: copialo del `drakon-ventas-marketing.html` (tiene 20 únicos: mensajes,
ojo, robot, ruta, reloj, mundo, edificio, usuarios, target, refresh, mail, whatsapp, check,
etc.). El kit `aurea_kit.py` también expone `icon("nombre")` para un one-pager simple.

## Dos caminos, y cuándo usar cada uno

- **Deck que debe verse como DRAKON (propuesta, presupuesto, deck oficial):** CLONÁ el sistema
  DRAKON (este archivo). Es la única forma de tener bandas, price cards, callouts y paleta completa.
- **One-pager mínimo y rápido:** `aurea_kit.py` (`aurea_page`, `icon`, `eyebrow`) alcanza, pero
  es una versión reducida: no tiene bandas oscuras, cc, hs ni price dark. Si el resultado se ve
  "plano", es porque estás en el kit reducido: pasá a clonar DRAKON.

## QA de deck (obligatorio antes de entregar)

Render real (screenshot) y revisá:
- [ ] Logo AUREA en portada (ver `uso-de-marca.md`).
- [ ] Ningún ícono sale como cuadradito/tofu. Si pasa, se rompió una clase o falta el SVG inline.
- [ ] Las bandas `band bv`/`band bm` tienen fondo OSCURO y título blanco (no blanco sobre blanco).
- [ ] Las secciones de gradiente se alternan (no todo blanco plano).
- [ ] Las price cards `dark` son navy con checks verdes; las claras con su price-val.
- [ ] Contenedor `<main class="container">` presente (no `.wrap`).
- [ ] Paleta: azul-violeta-rosa de baja saturación, sin colores chillones.
