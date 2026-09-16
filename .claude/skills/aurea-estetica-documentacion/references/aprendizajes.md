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
