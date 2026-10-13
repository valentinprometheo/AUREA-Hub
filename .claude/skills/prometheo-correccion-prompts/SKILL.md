---
name: prometheo-correccion-prompts
description: >-
  Corrección de prompts de agentes IA de Prometheo / AUREA. Se activa al modificar el prompt
  de un agente a partir del documento de Feedback del Agente IA (filas evidencia a
  corrección) o de capturas sueltas que manda el cliente. Método: correcciones aditivas,
  aisladas y no regresivas, entregadas por SECTOR COMPLETO (de encabezado numerado a
  encabezado numerado), fusionando sectores contiguos en un bloque único (13 y 14, 8 y 9),
  con una sola excepción para sectores con placeholders de archivos. Ninguna versión se
  entrega sin correr antes el BARRIDO DE COHERENCIA de siete chequeos, volcado en la matriz
  de auditoría del cliente. Usala ante "corregí el prompt", "aplicá estas correcciones",
  "iterá el prompt", "sacá la v13", "pasame la sección corregida", "ronda 2 de feedback",
  "el agente sigue respondiendo mal", o capturas para corregir. Es metodológica: no
  incorpora lógica comercial de ningún cliente.
---

# Skill - Corrección de Prompts de Agentes IA (Prometheo / AUREA)

Esta skill gobierna la **edición del prompt de un agente**. No es una skill de documentos
client-facing: no genera entregables para el cliente, opera sobre el texto del prompt.

## Cuándo se activa

Cuando AUREA modifica el prompt de un agente IA de Prometheo a partir de:

- el documento de **Feedback del Agente IA** (filas evidencia → corrección), o
- **capturas sueltas** de conversaciones reales que manda el cliente.

Lo que esta skill NO hace: definir lógica comercial de un cliente (qué se ofrece, cómo se
califica, reglas de financiación, zonas, precios). Eso vive en la metodología general y en
las skills verticales. Acá se documenta el **método**, no el contenido.

---

## El método (ya vigente)

- **Aditiva.** Se suma la regla nueva, no se reescribe el prompt entero por una corrección.
- **Aislada.** Cada corrección entra por su propio lado, sin arrastrar cambios de conveniencia.
- **No regresiva.** No se debilita lo que ya funciona. Al entregar se aclara qué cambió y qué
  NO se tocó.
- **Por sector completo.** La unidad de entrega es el sector, de encabezado numerado a
  encabezado numerado. Detalle en `references/01-entrega-por-sector-completo.md`.
- **Matriz de auditoría por cliente.** Cada corrección aplicada deja fila. Detalle en
  `references/03-matriz-auditoria.md`.
- **La última corrección manda.** Si dos rondas se pisan sobre el mismo punto, gana la más
  reciente.

## Lo que esta actualización agrega

- **BARRIDO DE COHERENCIA**, paso obligatorio antes de entregar cualquier versión, parcial o
  completa. Siete chequeos. Detalle en `references/02-barrido-de-coherencia.md`.
- **SCORE DATA-DRIVEN POR FILA** (actualización 13/10/2026, skill `aurea-data-action-driven`).
  Cada corrección lleva en la matriz cuánto se apoya en datos (0 a 100%): una captura suelta no
  pesa lo mismo que el mismo error en 40 conversaciones. El score no frena la corrección:
  ordena la prioridad y dice cuánto es evidencia y cuánto criterio. Detalle en
  `references/03-matriz-auditoria.md`.

---

## Regla dura 0: sin prompt vigente no se corrige

No se corrige de memoria, ni sobre una versión anterior, ni sobre una reconstrucción. Antes
de tocar nada tiene que estar a la vista el **texto literal de la versión en demo** (la que
generó el feedback). Si no está, se pide y se frena.

Motivo: las dos reglas duras de esta skill (sector completo y barrido de coherencia) operan
sobre el texto real. Sin el texto real, el sector que entregás no reemplaza nada: lo pisa.

---

## El flujo, en siete pasos

**1. Leer TODO el feedback antes de tocar nada.** Una corrección puede contradecir o matizar
a otra dentro de la misma ronda. Se lee el conjunto primero. Si el feedback viene en capturas
marcadas, la crítica vive en el cruce captura + marca: hay que ver la marca, no solo el texto
de la celda.

**2. Clasificar cada corrección por capa.**
- **Dato / fuente:** el dato existe en la integración (Sheets, Tokko, PrestaShop) y el agente
  no lo tomó, o lo tomó mal. Se corrige en la fuente o en cómo el prompt instruye consultarla.
- **Terminología:** el agente usó una palabra incorrecta del oficio. Se corrige con
  vocabulario obligatorio o prohibido.
- **Lógica conversacional:** el agente condujo mal la conversación (orden, ritmo,
  calificación, derivación). Se corrige con una regla de comportamiento.

**3. Detectar el patrón.** Varias filas suelen ser el mismo problema de fondo. Se corrige el
patrón una vez, no ocho veces. Ocho "reitera" distintos son un solo principio. Contá en
cuántas conversaciones aparece cada patrón: ese número es la base del score de la fila.

**3 bis. Correcciones por costo.** Si una corrección se motiva en el consumo de tokens o en el
costo de Meta (mensajes más cortos, apagar "humanizar mensajes", primera respuesta con una
sola pregunta), lleva **guardiana**: que no baje el % de calificación con la definición del
cliente. Costos y tarifas: skill `aurea-hub-costos-rentabilidad`.

**4. Mapear cada regla a su sector.** Antes de escribir una línea, dejá anotado qué sector o
sectores toca cada regla. Ese mapeo decide después cómo se entrega y es la primera columna de
la matriz.

**5. Escribir la corrección como regla trazable.** El formato canónico, que hace el prompt
auditable contra el feedback:

```
REGLA [N] - [NOMBRE EN MAYÚSCULAS]. [enunciado]. Aplica a: [casos]. No aplica a: [casos].
(Caso real: [cita verbatim de lo que el agente respondió mal].)
```

**6. Correr el BARRIDO DE COHERENCIA.** Obligatorio, siete chequeos, antes de entregar.
Detalle en `references/02-barrido-de-coherencia.md`. **Sin barrido, la versión no se entrega.**

**7. Entregar por sector completo y volcar el resultado en la matriz.** Entrega en
`references/01-entrega-por-sector-completo.md`; matriz y checklist en
`references/03-matriz-auditoria.md`.

---

## Las dos reglas duras

### Regla A - Se entrega el SECTOR COMPLETO

Toda corrección se entrega como uno o más **sectores completos**, reescritos de punta a punta,
listos para seleccionar el sector viejo y pegar el nuevo encima. Nunca un diff, nunca "cambiá
la línea X", nunca "agregá esto después de tal párrafo".

Si la ronda toca **sectores contiguos**, se fusionan en un solo bloque continuo (13 y 14 se
entregan como bloque "13 + 14"; 8, 9 y 10 como bloque "8 a 10"). La detección es automática:
no se pregunta, se detecta y se fusiona.

**Única excepción:** sectores que contienen placeholders de archivos (brochures, renders,
fotos, videos, planos). Ahí, y solo ahí, la entrega puede ser parcial, para no reescribir
nombres de archivo que tienen que ser verbatim.

Detalle y bordes en `references/01-entrega-por-sector-completo.md`.

### Regla B - Ninguna versión se entrega sin BARRIDO DE COHERENCIA

El método aditivo verifica que una regla **esté** en el texto. No verifica que sea
**coherente** con el resto del prompt. Ese punto ciego ya costó rondas de retrabajo reales en
producción. A partir de ahora el proceso valida presencia **y** coherencia, con siete
chequeos:

1. Presencia
2. Contradicción entre reglas
3. Propagación de mecanismo
4. Estructura huérfana
5. Referencias cruzadas
6. Ámbito de cada regla
7. Reconciliación entre rondas

Se corre **antes de entregar cualquier versión, parcial o completa**, y su resultado se vuelca
en la **matriz de auditoría del cliente**. Detalle y evidencia en
`references/02-barrido-de-coherencia.md`.

---

## Registro y estilo

- Español rioplatense, voseo.
- **AUREA** siempre en mayúsculas, sin acento.
- Cero em-dashes en el texto que generemos (comas, puntos, paréntesis).
- Dentro del prompt: prosa redactada corrida, sin tablas markdown, separadores `===`, emojis
  reales en mensajes literales, Variables y Smart Tags en código exacto.
- Voz de colega senior: directa, sin relleno.
- **Cambio estructural = versión nueva + changelog.** No se parchea lo que es estructural.
- **Nunca inventar.** Ninguna regla comercial que no haya salido del discovery o del feedback.

---

## Módulos

| Tema | Leé |
|---|---|
| Entrega por sector completo, sectores contiguos, excepción de placeholders | `references/01-entrega-por-sector-completo.md` |
| Barrido de coherencia (los 7 chequeos, con la evidencia que los originó) | `references/02-barrido-de-coherencia.md` |
| Matriz de auditoría y checklist de cierre para pegar | `references/03-matriz-auditoria.md` |
| Ayuda mecánica para los chequeos 1, 3, 4 y 5 | `scripts/barrido.py` |
