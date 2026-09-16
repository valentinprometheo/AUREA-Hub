# Uso de marca (OBLIGATORIO) · logo, isotipo y esfera

Esta regla existe porque el error más caro y más repetido es entregar un documento
**sin el logo**, con un placeholder, o con el logo aproximado. No puede volver a pasar.
Los assets de marca **ya viven dentro de la skill** y son **byte-idénticos a los que usa
el deck real de DRAKON** (verificado por SHA256). No hay que buscarlos en ningún lado.

## La regla, en una línea

**Todo documento de la Familia A lleva el logo AUREA embebido desde la skill, en la
portada y en el cierre. Siempre. Sin excepción.**

## De dónde sale el logo (y de dónde NO)

- **SÍ:** desde el kit. `from aurea_kit import LOGO, SPHERE` (son data URIs completos, PNG
  transparente, listos para `<img src="{LOGO}">`). O, si generás fuera del kit, leyendo
  el data URI de `assets/deck/logo.txt` (logo) y `assets/deck/sphere.txt` (esfera).
- **NO:** nunca lo busques en Google Drive, ni pidas "el archivo del logo", ni uses una
  URL externa, ni lo dejes como placeholder o lockup de texto, ni lo aproximes con CSS.
  El asset está adentro de la skill. Usalo.

Si alguna vez trabajás en un chat donde el runtime de skills no está activo y no podés
abrir `assets/deck/logo.txt`, **decilo explícitamente y pedí que se corra en un entorno
con la skill cargada**, en vez de entregar sin logo. Entregar sin logo no es una opción.

## Los assets de marca

| Asset | Archivo | Qué es | Uso |
|---|---|---|---|
| **Logo (wordmark)** | `assets/deck/logo.txt` | "áurea" + orbe, transparente, PNG 460×416 | Portada (hero) y cierre. Es el logo principal. Idéntico a DRAKON. |
| **Esfera** | `assets/deck/sphere.txt` | esfera iridiscente, PNG 560×560 | Decoración secundaria, SIEMPRE detrás del contenido. Idéntica a DRAKON. |
| **Isotipo (marca sola)** | `assets/deck/isotipo.svg` (+ `isotipo.txt` data URI) | el orbe/marca sin el texto, **vector SVG escalable** | Favicon, lockups chicos, sellos, avatar. `from aurea_kit import ISOTIPO`. |

### Dónde va el logo en un deck

- **Portada / hero:** `<img class="hero-logo" src="{LOGO}">` dentro del `brand-lockup`. Con
  aire generoso hacia los eyebrows (~46px).
- **Cierre / footer:** el lockup de marca de cierre (mini-orbe + "AUREA Hub · Master Partner
  Oficial de Prometheo CRM"). Si el cierre es de tipo `closer`, además puede llevar la esfera.
- **Nunca** una sección de contenido sin ninguna presencia de marca arriba o abajo.

## QA de marca antes de entregar (obligatorio)

- [ ] El logo aparece en la portada y se ve nítido (no pixelado, no cortado).
- [ ] El logo o el lockup de marca aparece en el cierre.
- [ ] La esfera está detrás del contenido, nunca tapando texto o cards.
- [ ] Ningún placeholder de logo, ninguna URL externa, ningún "falta el logo".
- [ ] Render real (screenshot) confirmando los dos puntos de marca. Si no renderiza el
      logo, es un bug que se arregla antes de entregar, no una nota al pie.

## Estado del isotipo

El isotipo está **integrado como SVG vectorial** (`assets/deck/isotipo.svg`, también expuesto
como data URI en `isotipo.txt` y como constante `ISOTIPO` en el kit). Reproduce la marca
AUREA (orbe con mordida + accent flotante) con el gradiente iridiscente, y al ser vector es
nítido a cualquier tamaño (ideal para favicon y usos chicos). Si algún día se quiere el PNG
mesh exacto de la marca, se reemplaza el contenido de `isotipo.txt` por su data URI y listo;
la referencia por `ISOTIPO` no cambia.

## La esfera: dónde va y dónde NO

- **El hero NO lleva esfera flotante.** El logo áurea ya trae su propio orbe iridiscente; una esfera extra en la portada choca con el logo y ensucia. Regla blindada en el CSS (`.hero .sphere-side{display:none!important}`).
- **La esfera va solo en el cierre (closer), a la DERECHA** (ver `genero-guia.md`). Ese es su único lugar.
