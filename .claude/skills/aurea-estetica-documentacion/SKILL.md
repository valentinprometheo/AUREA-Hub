---
name: aurea-estetica-documentacion
description: >-
  Estética y documentación de marca de AUREA Hub / Prometheo. Genera los documentos
  AUREA en dos familias que nunca se mezclan, más una capa de mejora continua.
  Familia A, estética deck HTML (base blanca, bandas de gradiente azul-violeta-rosa,
  esfera iridiscente, Helvetica + itálica Fraunces): propuestas, presupuestos, el
  deck oficial multi-sección, guías, one-pagers e institucionales; HTML por defecto,
  PDF de una hoja solo con aprobación. Familia B,
  documentación formal docx (NDA, acuerdos de confidencialidad, contratos, cláusulas,
  condiciones comerciales): SIEMPRE editando el template oficial, nunca reconstruido
  desde cero. Cubre los géneros clave: deck oficial, presupuesto (PAVIR), propuesta
  comercial (MAMUT), guía de consultoría y los nuevos servicios (Ventas + Marketing
  360 + Inteligencia Comercial, tipo DRAKON). Usala SIEMPRE que se pida crear, adaptar
  o iterar un documento, propuesta, presupuesto, deck, one-pager, guía, NDA, contrato
  o cláusula de AUREA / Prometheo, o se mencione la estética de AUREA.
---

# AUREA Hub · Estética y Documentación

## ⛔ PARA EMPEZAR (leé esto antes que nada, siempre)

**Para cualquier documento de Familia A (deck / guía / propuesta / presupuesto / one-pager): NO se arma a mano. Se CLONA un ejemplo real y se reemplaza el contenido.** Este es el primer paso, no una opción.

1. **Clasificá el género** (tabla más abajo) y elegí el ejemplo a clonar:
   - Guía de implementación → `assets/ejemplos/guia-mia-seguimientos.html`
   - Deck oficial / propuesta / presupuesto / institucional → `assets/ejemplos/drakon-ventas-marketing.html`
2. **Copiá ese archivo entero** y mantené intactos: el `<head>` (los 3 links de fuente), el `<style>` (o el `<link>` a `aurea-drakon.css`) y el `<main class="container">` con sus secciones.
3. **Reemplazá solo el contenido** (textos, números, íconos del set) usando las MISMAS clases. No inventes clases. No uses `.wrap`. No cambies el CSS.
4. **El logo y la esfera salen SIEMPRE de los assets embebidos** (`assets/deck/logo.txt`, `sphere.txt`). Nunca una URL de Google Drive, nunca una esfera de CSS, nunca un placeholder.
5. **Antes de entregar, QA por render** (ver `references/uso-de-marca.md` y `references/sistema-drakon.md`): logo real en portada y cierre, bandas oscuras con texto blanco, íconos que no salgan como cuadraditos, paleta completa (no mono-violeta).

Si te salteás esto, el documento sale plano y mal (logo roto, mono-violeta, sin bandas). El detalle completo está en `references/sistema-drakon.md` (deck) y `references/genero-guia.md` (guía). **Para Familia B (docx legal), el equivalente es: nunca reconstruir, editar el template oficial** (`references/documentacion-formal.md`).

---

Conductor, repositorio y generador de los documentos de marca AUREA. Hace cuatro cosas:

1. **Conductor.** Clasifica el pedido, ubica la familia y el género, chequea dependencias y pide los inputs que falten antes de generar.
2. **Repositorio.** Conoce la estética canónica de cada familia y de cada género. **No inventa formatos: respeta ESA estética, ninguna otra.**
3. **Generador.** Arma cada documento con su sistema propio (deck HTML con `aurea_kit.py`, o docx legal por template).
4. **Aprende mientras funciona.** Cada entrega deja un aprendizaje registrado y, al arrancar un documento nuevo, la skill revisa esos aprendizajes y te ofrece mejoras. Ver `references/mejora-continua.md`.

---

## Las dos familias (una estética cada una, nunca se mezclan)

Cada pedido cae en **una** familia. La familia define el formato y la estética.

| Familia | Qué es | Formato / estética (único) | Módulos |
|---|---|---|---|
| **A · Estética (deck)** | propuestas, presupuestos, deck oficial, guías, one-pagers, institucionales, decks de venta | **HTML** de marca: base blanca, bandas de gradiente azul-violeta-rosa a ~15%, esfera, Helvetica + itálica de acento. PDF de una hoja **solo con aprobación** | `references/estetica-deck.md` + `estetica-deck-system.md` (+ los géneros) |
| **B · Documentación formal** | NDA, acuerdo, contrato, cláusula, anexo, condiciones comerciales | **.docx** legal editando el **template oficial** (Calibri, violeta de marca, firmas). Nunca reconstruir desde cero | `references/documentacion-formal.md` (+ `-tokens.md`, `-qa.md`) |

### Regla del sistema de diseño (OBLIGATORIA)

**Para que un deck salga como DRAKON (bandas oscuras, price cards, callouts, íconos, paleta completa), se CLONA el sistema real de DRAKON, no se arma a mano.** El CSS canónico está en `assets/deck/aurea-drakon.css` (43 KB) y el ejemplo de oro en `assets/ejemplos/drakon-ventas-marketing.html`. Cloná ese HTML (head con fuentes + style + `<main class="container">` + secciones) y reemplazá solo el contenido con las mismas clases. **Nunca** inventes clases ni uses `.wrap` (no existe: rompe el ancho y las bandas). El kit `aurea_kit.py` es una versión **reducida** para un one-pager simple y NO tiene bandas, cc, hs ni price dark: si el resultado se ve plano, pasá a clonar DRAKON. Todo el vocabulario de componentes y el QA en `references/sistema-drakon.md`, leelo antes de armar cualquier deck.

### Regla de marca (OBLIGATORIA)

**Todo documento de la Familia A lleva el logo AUREA embebido desde la skill, en la portada y en el cierre. Siempre.** Los assets (logo, esfera) ya viven en `assets/deck/` y son byte-idénticos a los del deck real de DRAKON. Se usan con `from aurea_kit import LOGO, SPHERE` (o leyendo `assets/deck/logo.txt` / `sphere.txt`). **Nunca** buscar el logo en Drive, nunca una URL externa, nunca un placeholder, nunca aproximarlo. Entregar sin logo no es una opción. Detalle y QA de marca en `references/uso-de-marca.md`, leelo antes de armar cualquier deck.

### Regla de oro: una familia, una estética. Nunca mezclar.

- Una propuesta, presupuesto o guía visual va en el **deck HTML** (Familia A), **nunca** como docx de trabajo ni como PDF impreso desde el motor de Chromium.
- Un NDA o contrato va **editando el template oficial** (Familia B), **nunca** reconstruido con docx-js / python-docx desde cero.
- Si un pedido parece pedir dos estéticas a la vez, pará y preguntá cuál familia corresponde. No fusiones formatos.

---

## Géneros dentro de la Familia A (deck)

La estética es una sola; lo que cambia entre géneros es la **estructura narrativa** y el **timing**. Todos se arman clonando el sistema DRAKON (`references/sistema-drakon.md`), no con el kit reducido.

| Género | Qué es | Cuándo | Estructura / módulo |
|---|---|---|---|
| **Propuesta Comercial y Proyectual** | el "porqué" de un plan, adaptado a lo que el prospecto contó en la reunión (caso MAMUT) | post-reunión con un prospecto | `references/genero-propuesta-comercial.md` |
| **Presupuesto** | la estimación de inversión de un proyecto, como deck de referencia (caso PAVIR) | cuando el prospecto pide números | `references/genero-presupuesto.md` |
| **Deck oficial multi-sección** | el documento largo con índice de navegación que integra Ventas + Marketing (caso DRAKON) | presentación integral de la oferta completa | `references/genero-deck-oficial.md` |
| **Guía de sugerencias / implementación** | guías que acompañan una implementación (secuencias, reglas, links al ebook). Caso: guía MIA | acompaña la implementación | `references/genero-guia.md` |
| **One-pager / institucional** | one-pagers, piezas de marca sueltas | venta · institucional | estética base (`estetica-deck.md`) + sistema DRAKON |

Los **nuevos servicios** de AUREA (Ventas con Prometheo, Marketing 360, Inteligencia Comercial, el modelo hub) y cómo nombrarlos y presentarlos viven en `references/nuevos-servicios.md`. Léelo cuando el documento tenga que presentar la oferta o parte de ella.

---

## Cómo conducir (flujo)

Al activarse, **no asumas el entregable**. Conducí en este orden.

**Paso 0 · Clasificar familia y género (por la naturaleza del pedido).**

| Señales en el pedido | Familia · Género |
|---|---|
| "propuesta", "propuesta comercial", "plan de acción para [cliente]", "post-reunión", "tipo MAMUT", "el porqué" | A · Propuesta Comercial |
| "presupuesto", "cuánto sale", "estimación de inversión", "números del proyecto", "tipo PAVIR" | A · Presupuesto |
| "deck oficial", "el documento completo", "ventas y marketing juntos", "tipo DRAKON", "con índice" | A · Deck oficial |
| "guía", "one-pager", "deck", "institucional", "algo con la estética de AUREA", "para vender" | A · estética base |
| "NDA", "acuerdo", "confidencialidad", "contrato", "cláusula", "condiciones comerciales", "documento legal/formal" | B · Documentación formal |

Si el pedido es ambiguo entre dos familias o dos géneros, **preguntá cuál** antes de avanzar.

**Paso 1 · Revisar aprendizajes (mejora continua).** Antes de generar, leé `references/aprendizajes.md`: si hay un aprendizaje que aplica a este género o cliente, tenelo presente y, si corresponde, ofrecelo como mejora. Ver `references/mejora-continua.md`.

**Paso 2 · Ubicar cliente y momento.** Para qué cliente y en qué punto está.

**Paso 3 · Chequear dependencias antes de ofrecer generar.**
- Propuesta / Presupuesto sin los insights de la reunión → se vuelve genérico; pedí el ángulo central y los dolores concretos.
- Documentación formal (B): montos y datos del cliente confirmados; lo no confirmado va en placeholder rojo, nunca inventado.

**Paso 4 · Pedir lo que falta ANTES de generar.** Cada módulo trae su **checklist de inputs**. Corré el checklist contra lo que tengas. Si falta algo, **no inventes**: listá los gaps juntos y pedilos. Recién con los inputs (o con el OK de avanzar con placeholders marcados) generás.

**Paso 5 · Generar** con el sistema de la familia. Familia A: HTML por defecto, QA por chunks, PDF solo con aprobación. Familia B: unpack → editar XML → pack → QA visual.

**Paso 6 · Presentar.** Después de generar cualquier entregable, **siempre** presentá el archivo.

**Paso 7 · Registrar el aprendizaje.** Al cerrar la entrega (sobre todo si hubo corrección o algo que descubrimos), anotá el aprendizaje en `references/aprendizajes.md`. Ver `references/mejora-continua.md` para el formato y el protocolo.

---

## Principios transversales (valen para las dos familias)

- **Idioma y registro.** Español rioplatense, **voseo** (vos, tenés, podés). Cliente-facing: claro, sin jerga CRM cuando el lector es el cliente.
- **AUREA** siempre en mayúsculas y **sin tilde** en el cuerpo que escribimos nosotros. **Auditar TODAS las tildes** antes de entregar.
- **Cero em-dashes (—)** en texto que generemos: comas, puntos o paréntesis. En zonas heredadas de un template que el cliente ya validó, no se corrigen sin pedido explícito.
- **Voz de colega senior:** directa, sin relleno, verbos precisos y profesionales (no agresivos ni folklóricos). "Detectamos", no "Cazamos".
- **Números defendibles, no promesas.** Baselines realistas, cerrar con "valores de referencia, no promesas". Si cambia un número, revisá los porcentajes que dependen de él.
- **Arquitectura de marca (no confundir):** AUREA Hub = marca paraguas y ecosistema. Prometheo = producto de ventas activo (CRM + agente IA). La capa de consultoría = UX/estrategia. Prometheo ordena y convierte demanda existente, no la genera. Ver `references/nuevos-servicios.md`.
- **Single source of truth.** Cada dato vive en un solo lugar, sin duplicar entre documentos.
- **Correcciones aditivas, no regresivas.** Tocá solo lo pedido, no debilites lo que funciona; al entregar aclará qué cambió y qué NO se tocó. Cambios estructurales = nueva versión + changelog.
- **Nunca inventar datos** que no salieron del discovery o que el cliente no confirmó. Lo que falta se pide o va en placeholder.
- **Nada se entrega sin presentar** y sin QA línea por línea (huérfanas, tildes, alineaciones, íconos, contraste).

---

## Módulos (leé el que corresponda)

| Necesitás | Leé |
|---|---|
| Sistema de diseño DRAKON: cómo clonar el deck (OBLIGATORIO) | `references/sistema-drakon.md` |
| Uso de marca: logo, isotipo, esfera (OBLIGATORIO) | `references/uso-de-marca.md` |
| Estética del deck (reglas y recetas) | `references/estetica-deck.md` |
| Detalle de tokens, componentes y assets del deck | `references/estetica-deck-system.md` |
| Género: propuesta comercial y proyectual | `references/genero-propuesta-comercial.md` |
| Género: presupuesto | `references/genero-presupuesto.md` |
| Género: deck oficial multi-sección | `references/genero-deck-oficial.md` |
| Género: guía de sugerencias / implementación | `references/genero-guia.md` |
| Los servicios de AUREA y cómo nombrarlos | `references/nuevos-servicios.md` |
| Documentación formal (NDA, contratos) | `references/documentacion-formal.md` (+ `-tokens.md`, `-qa.md`) |
| Mejora continua (cómo aprende la skill) | `references/mejora-continua.md` |
| Log de aprendizajes | `references/aprendizajes.md` |

---

## Tooling (resumen; el detalle en cada módulo)

- **Deck HTML (Familia A):** copiá `assets/deck/` a tu directorio de trabajo (trae `aurea_kit.py`, `logo.txt`, `sphere.txt`). Escribí las `<section>` con las clases del sistema, envolvé con `aurea_page()`, guardá el `.html` (ese es el entregable). QA con `screenshot_html()` por chunks. PDF **solo con aprobación** vía `render_single_page_pdf()` (screenshot Playwright + img2pdf), **nunca** el motor de impresión de Chromium.
- **Auditar SIEMPRE antes de empaquetar o entregar:** `python scripts/audit.py` (estructura, un solo SKILL.md, description <=1024, referencias, assets, limpieza). No se entrega la skill con la auditoría en rojo.
- **DOCX legal (Familia B):** **nunca reconstruir.** Copiá `assets/nda/NDA-AUREA-template-base.docx`, unpack con `/mnt/skills/public/docx/scripts/office/unpack.py`, editá el XML quirúrgicamente, pack con `pack.py --original`, QA visual a PDF. Placeholders en rojo `C00000` bold, nunca `highlight: yellow`.
- **Dependencias del render del deck:** `playwright` (+ chromium) e `img2pdf`. En este entorno Chromium ya está en `/opt/pw-browsers`; no corras `playwright install`.
- **Google Drive:** subí el `.docx`/binario y abrilo con Google Docs; subir markdown lo renderiza como texto.
