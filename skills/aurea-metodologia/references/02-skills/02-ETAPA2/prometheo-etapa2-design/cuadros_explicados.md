# MÓDULO: CUADROS "EXPLICADO:" — CUÁNDO Y CÓMO

Patrón visual heredado del HTML del DOCX de MIA. Cuando un concepto del modelo
CRM es difícil de explicar con una tabla o un párrafo, se agrega un sub-cuadro
gráfico tipo "Explicado:" dentro de la sección correspondiente.

**Ejemplo paradigmático:** el cuadro de `#seguimiento_activo` dentro de la
Sección 7 (Smart Tags) del DOCX de MIA.

---

## 5 DISPARADORES (cuándo agregar uno)

Agregar un cuadro "Explicado:" cada vez que un concepto cumpla **al menos uno**
de estos criterios:

### Disparador 1 — Lógica de mutua exclusión o cancelación automática
El concepto involucra que algo se ACTIVA y algo OTRO se DESACTIVA en simultáneo.

Ejemplos:
- `#seguimiento_activo` se retira cuando aparece `#derivar_a_humano`
- Una variable estado_X se "congela" cuando proceso_actual cambia
- Un seguimiento programado se cancela si el usuario responde

### Disparador 2 — Variables condicionales complejas
El valor de la variable depende del valor de OTRA variable o de una secuencia.

Ejemplos:
- `estado_venta` solo se llena si `proceso_actual = venta`
- `severidad_caso` solo se llena junto con `tipo_derivacion`
- Un campo "personalización" solo aplica si `tipo_producto = a_medida`

### Disparador 3 — Reglas de distribución con múltiples paths
El flujo se ramifica según el valor de una variable, y los paths son distintos.

Ejemplos:
- 6 tipos de derivación, cada uno a un área distinta
- Notificación 24/7 vs notificación horario laboral según severidad
- Routing comercial vs técnico según tipo de cliente

### Disparador 4 — Workflows multi-paso con bifurcaciones
El proceso tiene varios pasos, y en alguno se bifurca según condición.

Ejemplos:
- El agente captura → valida → si severidad alta dispara push 24/7, si no
  cola normal
- El agente atiende soporte → si en 24h sigue sin resolver, sube de prioridad
- El usuario inmobiliaria entra → si tiene < 10 publicaciones va a comercial
  común, si tiene > 10 va a partnership

### Disparador 5 — Conceptos que YA generaron preguntas en la reunión
El más importante. Si el cliente preguntó dos veces lo mismo, o dijo "no termino
de entender X", o pidió un ejemplo, ese concepto NECESITA su cuadro Explicado.

Este disparador es empírico — el consultor lo identifica durante o después de la
reunión.

---

## ESTRUCTURA DEL CUADRO "EXPLICADO:"

Todos los cuadros siguen la misma fórmula visual:

### Componentes
1. **Título principal**: el nombre exacto del concepto (con `#` si es Smart Tag,
   con código si es variable). Tipografía 15pt bold color oscuro.
2. **Subtítulo**: una sola frase que explica para qué sirve el concepto.
   Tipografía 12pt regular gris.
3. **3 a 5 bloques de color** apilados verticalmente con flechas conectándolos
   cuando hay secuencia. Cada bloque tiene:
   - Título corto del bloque
   - 2-3 bullets explicativos cortos (máx 12 palabras cada uno)
4. **Pie del cuadro** (opcional): regla operativa adicional o nota crítica.
   Fondo gris pálido.

### Paleta de bloques por función

- **Verde** (`VERDE_FILL`): disparador positivo, condición que se cumple,
  habilitación, aprobación
- **Ámbar/Naranja** (`AMBAR_FILL`): acción operativa, decisión, paso intermedio
- **Coral** (`CORAL_FILL`): resultado, acción del agente, mensaje enviado
- **Rojo** (`ROJO_FILL`): cancelación, error, exclusión, situación que termina
  el flujo
- **Azul** (`AZUL_FILL`): información, validación, captura de datos
- **Morado** (`MORADO_FILL`): variables, conceptos transversales
- **Gris** (`GRIS_FILL`): pie con regla, contexto general, neutro

---

## EJEMPLO PARADIGMÁTICO: cuadro de #seguimiento_activo

Fórmula visual del cuadro que ya está aprobado y embebido en el DOCX de MIA:

### Bloque 1 (verde) — "El agente la pone cuando se cumplen 3 cosas a la vez"
- El usuario mostró interés en MIA
- Todavía NO completó el objetivo
- El agente ya mandó toda la info que podía

### Bloque 2 (4 cards en fila — ámbar/morado/azul/verde)
"Para que el mensaje automático realmente se mande, tienen que coincidir las 4
condiciones al mismo tiempo:"
- Card 1 (ámbar): Tag activa → `#seguimiento_activo`
- Card 2 (morado): Proceso → `proceso_actual = venta`
- Card 3 (azul): Estado → `estado_venta = no_descargo`
- Card 4 (verde): Tiempo → `+ 24hs, 48hs o 72hs`

### Bloque 3 (coral) — "El agente envía el mensaje automático"
"según el seguimiento que corresponda (Seg.1, 2, 3, 4 o 5)"

### Bloque 4 (2 cards rojos en fila) — "El seguimiento se cancela en 2 situaciones"
- Card 1: El usuario responde → el follow-up se cancela automáticamente
- Card 2: Aparece `#derivar_a_humano` → se retira `#seguimiento_activo`

### Pie (gris)
"Los seguimientos SOLO se envían en horario laboral (L-V de 10 a 18hs)"

---

## OTROS CASOS QUE TÍPICAMENTE NECESITAN CUADRO "EXPLICADO:"

### Caso: Variable router (`proceso_actual` que decide qué `estado_X` se llena)
Disparador 2 + Disparador 5. Ya existe el Gráfico 3 (Arquitectura de Variables)
para esto, pero si el cliente sigue confundido se puede armar uno más enfocado.

### Caso: Smart Tag de derivación con sus 6 tipos y 2 severidades
Disparador 3 + Disparador 4. Ya existen los Gráficos 8 (Derivación) y 9
(Notificaciones 24/7), pero un cuadro Explicado de `#derivar_a_humano` puede
ayudar.

### Caso: Lógica de cierre de conversación post-handoff
Cuando el caso vuelve del humano al agente. Disparador 1 (cancelación de tags)
+ Disparador 4. NO existe gráfico transversal — se puede armar específico.

### Caso: Lógica de horario laboral vs 24/7
Disparador 3. Cuándo entra al horario laboral vs cuándo dispara push fuera de
horario. Disparador 5 — los clientes preguntan mucho esto.

### Caso: Multi-channel dispatch
Si el agente llega por canal A pero el follow-up sale por canal B (típico:
entró por Instagram pero hace follow-up por WhatsApp). Disparador 4.

### Caso: Cómo se leen las 2 Smart Tags juntas (OBLIGATORIO con modelo nuevo)
Con el modelo de "una tag por dimensión" (estadío + tipo de usuario + prioridad opcional), siempre incluir un
cuadro o bloque "Explicado:" que muestre cómo se combinan. Ejemplo: un lead
"En Conversación + #inversor + #contacto_vip" le dice al equipo, sin abrir el
chat: está siendo calificado, es inversor, y hay que priorizarlo. Disparador 5
(los clientes necesitan entender la lectura combinada). Puede ser un bloque
de texto explicativo en vez de SVG si el espacio es chico.

---

## CÓMO GENERAR EL SVG

Usar los helpers de la skill `aurea-crm-graphics`:

- **Dimensiones típicas**: 760×720 px (similar al `#seguimiento_activo`)
- **Tipografía**: Anthropic Sans con fallback (escapado como `&apos;` en XML)
- **Border-radius**: 8-12px en cards principales, 6-8px en sub-cards
- **Stroke**: 0.5-0.7 en cards normales, 1-1.5 en cards destacados
- **Flechas**: usar marker `arrow` definido en `svg_header()`
- **Encoding XML**: declaración UTF-8 explícita, escapar `&` como `&amp;`,
  comillas dobles dentro de atributos como `&quot;`

Pasos:
1. Generar el SVG con declaración `<?xml version="1.0" encoding="UTF-8"?>`
2. Convertir a PNG con cairosvg (1000-1400px width)
3. Optimizar con PIL `compress_level=9`
4. Embeber en el DOCX con ancho 16cm centrado

---

## CHECKLIST PARA CADA CUADRO "EXPLICADO:"

Antes de embeberlo:

- [ ] Título con `#` o código exacto del concepto
- [ ] Subtítulo de UNA sola frase
- [ ] 3-5 bloques de color (no más, no menos)
- [ ] Cada bloque con 2-3 bullets máximo
- [ ] Bullets cortos (< 12 palabras)
- [ ] Flechas conectando bloques cuando hay secuencia
- [ ] Pie con regla operativa o contexto
- [ ] Paleta consistente con función (verde=positivo, rojo=cancela, etc.)
- [ ] SVG con XML válido
- [ ] PNG optimizado < 200 KB
- [ ] Embebido a 16cm en DOCX, centrado
