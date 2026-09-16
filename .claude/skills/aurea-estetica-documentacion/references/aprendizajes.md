# Log de aprendizajes · AUREA Estética y Documentación

Memoria de trabajo de la skill. Se **lee antes** de generar cada documento y se **escribe al cerrar** cada entrega relevante. El protocolo completo está en `mejora-continua.md`. El formato de cada entrada, abajo.

Regla corta: capturá correcciones, recetas que funcionaron, preferencias del usuario, datos de negocio confirmados y cosas que salieron mal. Lo que se repite o se confirma, ascendelo a la referencia canónica y marcalo `[ascendido]`. No infles el log con entradas de rutina.

---

## Formato de entrada

```
### [AAAA-MM-DD] · <género o área> · <cliente si aplica>
- **Qué pasó:** una línea
- **Aprendizaje:** la regla accionable para la próxima vez
- **Aplica a:** género / familia / cliente / transversal
- **Estado:** activo | ascendido → <archivo> | descartado por el usuario
```

---

## Aprendizajes semilla (extraídos del material fundacional)

Estos vienen de la experiencia ya codificada en las skills originales. Nacen como `activo` y en su mayoría ya viven en la doctrina; sirven de ejemplo del formato y de arranque del log.

### [2025-06] · Documentación formal · EDFAN
- **Qué pasó:** reconstruir el NDA desde cero con docx-js y Arial dio tres versiones rechazadas; recién partir del .docx real matcheó al 100%.
- **Aprendizaje:** nunca reconstruir un documento legal desde cero; editar el template oficial (unpack XML, edición quirúrgica, repack).
- **Aplica a:** Familia B (documentación formal)
- **Estado:** ascendido → documentacion-formal.md ("La regla fundamental")

### [2025-06] · Estética deck · transversal
- **Qué pasó:** el motor de impresión de Chromium (`page.pdf`) rompía los gradientes en la segunda columna de los grids.
- **Aprendizaje:** el PDF de una hoja se hace con screenshot full-page (Playwright) a img2pdf, nunca con el motor de impresión de Chromium.
- **Aplica a:** Familia A (deck)
- **Estado:** ascendido → estetica-deck.md ("Salida y render")

### [2025-06] · Estética deck · cards de precio
- **Qué pasó:** cards de precio hermanas quedaban escalonadas por largo de label, y el número en Helvética dura leía "muy duro".
- **Aprendizaje:** el número grande siempre en la itálica de acento (Fraunces); emparejar cards con un label gemelo, no a ojo.
- **Aplica a:** Familia A (deck), cards de precio
- **Estado:** ascendido → estetica-deck.md ("Recetas de componentes finos")

### [2025-08] · Presupuesto · PAVIR
- **Qué pasó:** el presupuesto necesita separar con claridad "documento de referencia" del "documento que se firma", para no confundirlo con el contrato.
- **Aprendizaje:** el hero del presupuesto lleva siempre la nota de encuadre ("propuesta comercial de referencia... es el documento que se firma") que lo distingue de la Familia B.
- **Aplica a:** género presupuesto
- **Estado:** ascendido → genero-presupuesto.md

### [2025] · Nuevos servicios · DRAKON
- **Qué pasó:** al integrar Ventas + Marketing en un solo deck, el círculo comercial solo cierra si el dato de la Inteligencia Comercial vuelve a los canales de generación.
- **Aprendizaje:** el orden es doctrina (ventas primero, marketing después) y el cierre siempre resuelve "el dato que vuelve".
- **Aplica a:** género deck oficial, nuevos servicios
- **Estado:** ascendido → genero-deck-oficial.md, nuevos-servicios.md

---

## Aprendizajes nuevos

<!-- Agregá acá las entradas nuevas, las más recientes arriba. -->

### [2026-09-16] · Empaquetado de la skill · claude.ai
- **Qué pasó:** subir un zip con varias skills juntas falla ("Zip must contain exactly one SKILL.md file. Currently there are 14"); el sistema exige un solo SKILL.md por paquete.
- **Aprendizaje:** una skill por zip, exactamente un archivo llamado SKILL.md; los demás .md van con otro nombre; description ≤ 1024 caracteres. Detalle en EMPAQUETADO.md.
- **Aplica a:** transversal (empaquetado)
- **Estado:** ascendido → EMPAQUETADO.md

### [2026-09-16] · Assets de marca · auditoría
- **Qué pasó:** se dudó si el logo, la esfera y la tipografía estaban bien integrados; se auditó decodificando los data URI y renderizando una página de prueba con Chromium.
- **Aprendizaje:** logo.txt (PNG 460×416) y sphere.txt (PNG 560×560) son reales y renderizan; la fuente de acento es Fraunces (confirmado igual en el deck real DRAKON), "Rischie" es solo un swap opcional futuro, no un archivo faltante. Manifiesto en assets/ASSETS.md con chequeo de integridad.
- **Aplica a:** transversal (Familia A)
- **Estado:** ascendido → assets/ASSETS.md

### [2026-09-16] · Referencias de diseño · transversal
- **Qué pasó:** los HTML/PDF/ZIP adjuntos a veces llegan vacíos a Claude (no se pueden leer), y el diseño exacto se aproximaba de memoria en vez de replicarlo.
- **Aprendizaje:** los ejemplos de diseño exactos se guardan como archivos DENTRO de la skill (`assets/ejemplos/`), no como adjuntos sueltos ni solo en memoria del proyecto; así viajan con la skill y siempre se pueden leer. Antes de armar un deck, abrir el ejemplo y copiar de ahí.
- **Aplica a:** transversal (Familia A)
- **Estado:** ascendido → genero-deck-oficial.md (`assets/ejemplos/drakon-ventas-marketing.html`)

### [2026-09-16] · Deck oficial · AUREA (institucional)
- **Qué pasó:** se sumó el `Aurea_Hub - Deck Oficial.pdf` como pieza institucional, distinta del deck de cliente (DRAKON).
- **Aprendizaje:** el género "deck oficial" tiene dos variantes (institucional AUREA vs. cliente), misma estética; el PDF oficial es la fuente de verdad del contenido institucional.
- **Aplica a:** género deck oficial
- **Estado:** ascendido → genero-deck-oficial.md
