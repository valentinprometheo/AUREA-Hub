# Género · Guía de sugerencias / implementación

> Género dentro de la **Familia A (deck)**. Es el documento que acompaña una implementación: explica sugerencias, secuencias de mensajes, reglas de decisión y links al ebook. Caso de referencia corregido: `assets/ejemplos/guia-mia-seguimientos.html` (guía MIA).

Misma estética y sistema que DRAKON (ver `sistema-drakon.md`): se usa `aurea-drakon.css`, el logo y la esfera reales, y las bandas oscuras para separar partes. La guía agrega unos componentes propios (secuencia de toques, reglas, tomar/no-tomar, alternativas), que van estilados con los **mismos tokens de DRAKON** (un suplemento CSS chico), nunca con una paleta nueva.

## Errores típicos de este género (los que hacían que saliera "muy mal")

Auditado sobre una guía real que salió mal:
1. **Logo por URL de Drive** (`drive.google.com/thumbnail?id=...`) con un fallback de círculo + texto. No renderiza: aparece el fallback feo. **Prohibido.** Usar SIEMPRE el logo real embebido (`logo.txt` / `LOGO`). Ver `uso-de-marca.md`.
2. **Esfera hecha con `radial-gradient` de CSS.** Se ve barata. Usar SIEMPRE la esfera real (`sphere.txt` / `SPHERE`).
3. **Paleta de un solo violeta.** Plano. Usar la paleta completa de DRAKON (azul, violeta, verde, naranja, coral) y las bandas oscuras.
4. **Sin bandas oscuras.** Las partes (Parte 1, Parte 2) van con `band bv` / `band bm` para dar ritmo y peso, como DRAKON.

## Estructura

Hero (logo + esfera reales, eyebrow, h1, lead) → sección de encuadre con `ref` (tarjetas que enlazan al ebook) → por cada parte: `band bv`/`band bm` numerada + `callout` (el porqué) + `card` con el contenido (secuencia de toques, reglas, alternativas) + `card accent` con `checks` para las sugerencias → closer con esfera + links al ebook → footer con `mini-orb`.

## Componentes propios de la guía (suplemento, tokens DRAKON)

Están en el `<style>` del ejemplo `guia-mia-seguimientos.html`. Copiá de ahí:
- **`ref`** (`ref-ic` / `ref-k` / `ref-t` / `ref-go`) — tarjeta-link al capítulo del ebook.
- **`touches` / `touch`** (`t-when` / `t-n` / `t-ang` / `t-msg`) — secuencia de mensajes con tiempo y ángulo.
- **`rules` / `rule`** (`r-h` / `r-b`) — reglas de decisión con ícono.
- **`cols` / `col ok` / `col no`** — dos columnas verde (tomar) / coral (no tomar).
- **`alts` / `alt`** (`alt-h` / `alt-b`) — filas de alternativas, con `pill acc` para la recomendada.

## Regla de armado

**Cloná `guia-mia-seguimientos.html`** (head con fuentes + `aurea-drakon.css` inline + el suplemento) y reemplazá el contenido. No inventes una paleta ni un logo: los assets y los tokens ya están. QA de deck y de marca obligatorio (ver `sistema-drakon.md` y `uso-de-marca.md`).

## Cierre (closer): estructura y disposición

El `.closer` es un **grid de 2 columnas**. Estructura correcta (no usar sphere-side absoluto, que lo rompe):

```html
<section class="closer" style="grid-template-columns:1.15fr .85fr">
  <div class="closer-text" style="text-align:left"> eyebrow + h2 (con em) + p + closer-links </div>
  <div class="closer-sphere"><img src="{SPHERE}"></div>
</section>
```

**Preferencia de Valentín: la gráfica (esfera) va a la DERECHA y el texto a la IZQUIERDA.** Por eso el texto va primero (columna izquierda, `text-align:left`) y la esfera segunda (columna derecha). El default de DRAKON trae la esfera a la izquierda; para estos documentos se invierte.

## Voz y contacto (preferencias de Valentín)

- **Sin palabras de estilo ni de combate.** El lector es un implementador profesional. Nada de "ataque", "atacar", "cazar", "pelea". Verbos neutros y precisos: "seguimiento", "reactivación", "trabajar el lead". (Refuerza la regla transversal de voz de la skill.)
- **Contacto en cada sección y en el cierre.** Cada parte cierra con una nota tipo `.contact` ("¿Dudas con esta configuración? Escribinos: el equipo de AUREA las resuelve con ustedes.") y el cierre repite el ofrecimiento de acompañamiento. El componente `.contact` (icono en caja oscura + texto sobre `--aurea-purple-soft`) está en el ejemplo `guia-mia-seguimientos.html`.
- **Secuencia de seguimientos MIA (dato confirmado):** 6 horas → 7 días → 3 semanas.
- **Mensajes del agente:** tono claro y cordial, sin coloquialismos ("picando", etc.). Emojis como placeholder `(emoji de saludo)`, no reales, en el cuerpo del documento.
