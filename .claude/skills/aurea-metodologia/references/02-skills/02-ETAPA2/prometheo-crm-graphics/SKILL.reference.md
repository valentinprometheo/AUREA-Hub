# SKILL — `prometheo-crm-graphics`

**Metodología visual para gráficos de DOCX cliente-facing de Etapa 2 (Diseño de CRM)**
**AUREA Hub × Prometheo**

Versión: 1.0 · Octubre 2026
Caso de referencia: MIA App
Validado con: bot oficial de Prometheo

---

## PROPÓSITO DE LA SKILL

Esta skill permite generar gráficos visuales para los DOCX cliente-facing que se entregan al final de Etapa 2 (Diseño del CRM y del Prompt). El objetivo es que un cliente sin formación técnica entienda el modelo conceptual del CRM con un golpe de vista.

**Regla de oro:** un cliente debe poder mirar un gráfico durante 5 segundos y entender la idea. Si no, el gráfico falló.

---

## A — PRINCIPIOS GENERALES DEL ESTÁNDAR VISUAL AUREA

### 1. Frase comprensible primero, código entre paréntesis después

**SIEMPRE:**
- Texto principal en lenguaje humano (frase comprensible).
- Código técnico entre paréntesis abajo, font-size más chico, opacidad reducida (~0.7).

```
✅ Correcto:
   "Por qué canal entró"
   (canal)

❌ Incorrecto:
   "canal"   (solo código)
   "Variable canal"   (palabra técnica como protagonista)
```

### 2. Color por significado, no por orden

No ciclar entre colores como un arcoíris. Asignar color según la categoría conceptual del elemento. Máximo 3 colores semánticos por gráfico.

### 3. Cajas, no listas

Los gráficos no son listas con bullets. Son cajas conectadas por flechas. Cada concepto = una caja. Cada relación = una flecha. Si una caja necesita más de 3 líneas de texto, partila en 2.

### 4. Jerarquía visual clara

Cada gráfico tiene un orden de lectura obligatorio:

```
Título principal (font ~14px medium, top center)
   ↓
Subtítulo opcional (font ~12px regular, opacity 0.7)
   ↓
Bloques principales (cards con borde y fondo)
   ↓
Flechas direccionales (centradas, conectando bloques)
   ↓
Texto explicativo final (al pie del gráfico, opcional)
```

### 5. Sentence case, sin emojis decorativos

Todos los labels en sentence case ("Variables transversales", no "VARIABLES TRANSVERSALES" ni "Variables Transversales"). Excepción: nombres propios técnicos como WhatsApp, Prometheo, MIA.

Los emojis solo aplican si tienen significado funcional (ej: 📨 para "Mensaje del usuario"). Nunca como adorno.

### 6. Texto siempre dentro de las cajas

Ningún texto debe quedar fuera de su caja contenedora. Si se desborda, agrandar la caja, no achicar el texto.

### 7. Flechas centradas y claras

- Cada flecha tiene origen y destino claros.
- Se dibujan entre el centro de las cajas.
- No cruzar flechas si se puede evitar.
- Texto sobre flechas solo si la relación no se entiende sin etiquetar.

### 8. Workflow de generación en 2 pasos

1. **Prototipo SVG inline** primero — liviano, rápido de iterar, no consume muchos tokens.
2. **Validación visual con el usuario** — aprobar shape, contenido, jerarquía, colores.
3. **PNG en alta calidad** después — generar con matplotlib o equivalente, DPI ≥ 200, embebido en DOCX con `python-docx`.

---

## B — PALETA COMPLETA AUREA

| Color | Hex | Uso |
|---|---|---|
| Morado | `#7C5CBF` | Banners principales (Roles, Autonomía, Embudos, Reglas Distribución, Próximos Pasos) · Variables transversales · Proceso Seguridad |
| Naranja / ámbar | `#E8943A` | Banners (Smart Tags, Seguimientos, Pendientes) · Routers / decisiones / paso clave |
| Azul | `#5B8FD9` | Banners (Modificaciones, Variables) · Proceso FAQ · Análisis / identificación |
| Verde | `#4CAF80` | Banners (Estrategia, Escenarios) · Proceso Venta · Habilitadores positivos |
| Rojo | `#E84545` | Proceso Soporte · Errores · Items críticos |
| Coral | `#F37D6E` | Acciones del agente · Disparos de mensaje · Tags operativas |
| Teal | `#3FA89E` | Áreas humanas / destinos finales (Comercial, Soporte Técnico, Trust & Safety) |
| Gris | `#7A7A7A` | Contenedores neutros · Inicio / fin de flujos · Postventa |
| Oscuro | `#2D2D3D` | Banner Autonomía · Headers de tabla |

**Notas técnicas:**
- Cards: borde lateral grueso del color del banner, fondo claro derivado del mismo color a baja saturación.
- Stroke en bordes de cajas: 0.5px (líneas finas, look refinado). Excepción: 2px para destacar el "paso clave" en gráficos de flujo.
- Border-radius en cajas: 8-12px.

---

## C — CONVENCIONES TRANSVERSALES

### Color por proceso (CRM)

Aplica en embudos y sus tags de estadío, follow-ups, reglas de distribución:

| Proceso | Color |
|---|---|
| Venta | Verde |
| Soporte | Rojo |
| FAQ | Azul |
| Seguridad | Morado |
| Postventa | Gris |

### Color por categoría conceptual

| Categoría | Color | Aplicación |
|---|---|---|
| Variables transversales | Morado | Datos del usuario que aplican siempre |
| Decisiones | Naranja/ámbar | Lo que define el rumbo (ej. la variable padre) |
| Acciones del agente | Coral | Disparo de mensaje, tag operativa |
| Áreas humanas | Teal | Destinos de derivación |
| Contenedores neutros | Gris | Start/end, mensajes del usuario |

### Color por estado de aprobación del cliente (en bloques de feedback)

| Estado | Color de fondo |
|---|---|
| Pendiente de feedback | Amarillo pálido |
| Con cambios solicitados | Naranja claro |
| Aprobado | Verde claro |

### Color por criticidad

| Nivel | Color |
|---|---|
| Crítico | Rojo / coral |
| Urgente | Naranja |
| Normal | Sin color especial |

---

## D — RELACIÓN ENTRE GRÁFICOS Y TEXTO

Los gráficos no son ilustraciones decorativas. Son **el contenido principal** de cada sección. El texto narrativo los acompaña, no al revés.

### Estructura recomendada de cada sección del DOCX

```
1. Banner de sección (ancho completo, color de la categoría)
   ↓
2. Card explicativo corto (3-4 bullets máx) — el "por qué" del modelo
   ↓
3. Gráfico overview (uno por sección)  ← la pieza principal
   ↓
4. Tablas técnicas con valores literales (las decisiones concretas)
   ↓
5. Gráfico arquitectura/detalle (si aplica)
   ↓
6. Card "EJEMPLO PARA QUE SE ENTIENDA" (storytelling con persona ficticia)
   ↓
7. Bloque de feedback (amarillo pálido, espacio para anotaciones del cliente)
```

### Reglas de integración

- **El gráfico va antes que la tabla técnica.** El cliente primero entiende la idea visualmente, después ve los detalles.
- **El texto narrativo no repite lo que muestra el gráfico.** Si el gráfico ya dice "5 procesos paralelos", el texto introduce concepto, no lo repite.
- **El bloque "EJEMPLO PARA QUE SE ENTIENDA" cierra la sección.** Es la forma de aterrizar el modelo en una persona ficticia ("Imaginate que llega Juan…").

---

## E — INVENTARIO DE GRÁFICOS

### Resumen

| # | Nombre | Sección | Estado |
|---|---|---|---|
| 1 | Mapa de Embudos (overview) | Embudos | ⚠️ Diseñado pero no implementado |
| 2 | Overview de Variables | Variables | ✅ Aprobado |
| 3 | Arquitectura de Variables | Variables | ✅ Aprobado |
| 4 | Overview de Smart Tags | Smart Tags | ✅ Aprobado |
| 5 | 3 Escenarios de Ejemplo (1 por escenario) | 3 Escenarios | ✅ Aprobado |
| 6 | Cómo se dispara un Seguimiento (fórmula) | Seguimientos | ✅ Aprobado |
| 7 | Overview de Seguimientos | Seguimientos | ✅ Aprobado |
| 8 | Cómo funciona la Derivación | Reglas de Distribución | ✅ Aprobado |
| 9 | Notificaciones Urgentes 24/7 | Reglas de Distribución | ⚠️ Diseñado pero no implementado |

---

## GRÁFICO 1 — MAPA DE EMBUDOS (overview)

> **Estado: Diseñado pero no implementado en el DOCX entregado de MIA. Referencia futura.**

### 1. Nombre
Mapa de Embudos / Overview de Procesos

### 2. Sección del DOCX
Sección "Embudos", al inicio (antes de las tablas con etapas detalladas).

### 3. Qué comunica
"El agente atiende N procesos paralelos en simultáneo. Cada uno tiene su propio recorrido."

### 4. Tipo de diagrama
Cards en grilla horizontal (una columna por proceso).

### 5. Estructura visual concreta
- 1 título superior: "N procesos paralelos que el agente atiende en simultáneo"
- N cajas en fila o grilla 2x3 (depende del número de embudos del cliente)
- Cada caja con:
  - Nombre del proceso (frase comprensible) en bold
  - Nombre técnico abajo entre paréntesis, opacity 0.7
  - 2-3 etapas principales del embudo como sub-bullets

### 6. Reglas de color y jerarquía
- Cada caja con el color del proceso correspondiente (verde Venta, rojo Soporte, azul FAQ, morado Seguridad, gris Postventa).
- Título principal en color oscuro, sentence case.
- Sin elemento dominante: todas las cajas tienen el mismo peso visual (procesos paralelos, no jerárquicos).

### 7. Tipografía y estilo
- Título: ~14px medium, color oscuro
- Nombre del proceso: 14px bold
- Nombre técnico: 10px regular, opacity 0.7
- Etapas: 11px regular

### 8. Especificaciones técnicas
- Dimensiones SVG: 680x320 (para 5 embudos en fila)
- DPI PNG final: 200
- Sin sombras ni gradientes

### 9. Casos de uso
- Transversal a todos los clientes que tengan más de 1 embudo.
- Especialmente útil cuando el modelo tiene 4+ procesos paralelos (porque sin gráfico se vuelve difícil de explicar).

### 10. Anti-patrones
- ❌ Cajas con jerarquía visual diferente (los procesos son paralelos, no hay uno "más importante").
- ❌ Listar más de 4-5 etapas por embudo en este gráfico (saturás visualmente — las etapas detalladas van en tablas, no acá).
- ❌ Mezclar colores fuera de la convención por proceso.

---

## GRÁFICO 2 — OVERVIEW DE VARIABLES

### 1. Nombre
Overview de Variables / Las dos categorías

### 2. Sección del DOCX
Sección "Variables", inmediatamente después del título de sección y de la explicación general (antes de las tablas técnicas).

### 3. Qué comunica
"Las variables son los datos que el agente captura. Hay dos tipos: las transversales (siempre) y las de estado (solo la del proceso activo)."

### 4. Tipo de diagrama
Comparativa de 2 columnas grandes lado a lado.

### 5. Estructura visual concreta (actualizado v1.21)
- Título superior: "Las variables son los datos que el agente captura de cada conversación"
- Subtítulo: "para que después podamos filtrar, segmentar y disparar seguimientos"
- 3 columnas lado a lado:
  - **Transversales (morado):** las que aplican a toda conversación (canal, perfil, zona...)
  - **Padre e hija (ámbar):** la variable que ordena el perfil y la que depende de ella
  - **Inteligencia comercial (teal):** objeción, dolor, disparador, pedido fuera de catálogo
- Pie del gráfico: "La etapa del lead no es una variable: la dice su etiqueta de estadío"

### 6. Reglas de color y jerarquía
- Cada columna con su color de categoría; la variable padre destacada con borde 1px.
- Título y subtítulo en color oscuro neutro.

### 7. Tipografía y estilo
- Título: 14px medium · Subtítulo: 12px regular, opacity 0.7
- Encabezados de columna: 16px bold · Texto de cada caja: 12-13px · Pie: 11px, opacity 0.75

### 8. Especificaciones técnicas
- Dimensiones SVG: 680x440 · DPI PNG final: 200

### 9. Casos de uso
Transversal a todos los clientes. Es el gráfico que abre la sección Variables.

### 10. Anti-patrones
- ❌ Dibujar variables de etapa (`estado_X`) o una variable que decide en qué embudo está el lead (modelo derogado en v1.21).
- ❌ Listar valores específicos en este gráfico (eso va en las tablas técnicas).
- ❌ Usar más texto del necesario en cada caja (3-5 palabras máximo).

---

## GRÁFICO 3 — VARIABLES PADRE E HIJA (reemplaza "Arquitectura de variables", v1.21)

### 1. Nombre
Variables padre e hija.

### 2. Sección del DOCX
Sección Variables, después de la tabla.

### 3. Qué comunica
"Algunas variables solo se completan según el valor de otra." Ej.: la finalidad de la
inversión solo se pregunta si la persona es inversora.

### 4. Tipo de diagrama
Flujo top-down con una decisión y dos ramas.

### 5. Estructura visual concreta
- Arriba: caja ámbar con la variable padre en frase comprensible + código entre paréntesis
  (ej. "¿Para qué compra? (objetivo_busqueda)")
- Dos ramas: "Inversión" → caja con la variable hija (ej. "¿Renta, reventa o diversificar?
  (inversion_finalidad)"); "Uso propio" → caja gris "no aplica, queda vacía"
- Al costado: la etiqueta de perfil que espeja a la padre (ej. Inversor)
- Pie: "Vacío en la hija no es dato faltante: es que no corresponde"

### 6. Reglas de color y jerarquía
- Padre en ámbar (decisión), hija en morado (variable), rama vacía en gris.

### 7. Especificaciones técnicas
- Dimensiones SVG: 680x400 · DPI PNG final: 200

### 8. Anti-patrones
- ❌ Volver al gráfico viejo de una variable que decide en qué embudo está el lead y ramifica
  a variables de etapa por proceso (`estado_X`). Ese modelo quedó derogado.

---

## GRÁFICO 4 — OVERVIEW DE SMART TAGS

### 1. Nombre
Overview de Smart Tags / Las etiquetas operativas

### 2. Sección del DOCX
Sección "Smart Tags", al inicio.

### 3. Qué comunica (actualizado v1.21)
"Cada lead lleva una etiqueta por dimensión: en qué etapa está, qué tipo de contacto es y,
si aplica, una excepción."

### 4. Tipo de diagrama
Tres franjas horizontales, una por dimensión.

### 5. Estructura visual concreta
- Título: "Las etiquetas muestran de un vistazo dónde está y quién es cada lead"
- Franja 1 — Estadío: una fila por embudo con sus etapas en orden (cajas del color de cada tag)
- Franja 2 — Perfil del contacto: ej. Uso propio · Inversor · Inmobiliaria · Proveedor
- Franja 3 — Excepción: ej. Contacto VIP
- En las tags que disparan acción, una nota abajo (ej. Derivado: "apaga al asistente y avisa al equipo")
- Pie (caja gris): "Una sola etiqueta por dimensión: un lead puede ser En Conversación + Inversor + Contacto VIP a la vez"

### 6. Reglas de color y jerarquía
- Cada tag con su color de Prometheo (6 disponibles, ver restricción 19); la etapa de
  derivación destacada con borde 1px porque apaga al asistente.

### 7. Tipografía y estilo
- Nombre de tag: 14px bold · Nota de acción: 11px italic opacity 0.7 · Pie: 13-14px

### 8. Especificaciones técnicas
- Dimensiones SVG: 680x460 · DPI PNG final: 200

### 9. Casos de uso
Transversal a todos los clientes. Imprescindible para explicar la regla de una tag por dimensión.

### 10. Anti-patrones
- ❌ Dibujar el modelo viejo de 2 tags operativas (`#seguimiento_activo` + `#derivar_a_humano`) o la regla "1 sola tag activa" (derogados).
- ❌ Mezclar en la misma franja tags de dimensiones distintas.

---

## GRÁFICO 5 — 3 ESCENARIOS DE EJEMPLO

### 1. Nombre
Escenario 1, 2, 3 (uno por escenario)

### 2. Sección del DOCX
Sección "3 Escenarios de Ejemplo", uno por escenario (3 gráficos consecutivos con el mismo patrón).

### 3. Qué comunica
"Así se conecta todo en un caso real: desde el mensaje del usuario hasta la acción del agente."

### 4. Tipo de diagrama
Flujo top-down completo con 4 niveles.

### 5. Estructura visual concreta (idéntico para los 3 escenarios, cambia solo el contenido)

```
[Título del escenario] (ej: "Escenario 1 — Usuario nuevo pregunta por MIA")
   ↓
Caja gris arriba: "Mensaje por [canal]:" + texto entre comillas del mensaje del usuario
   ↓ (flecha)
Caja ámbar: "Embudo: [NOMBRE]" + etiqueta de estadío que recibe
   ↓ (flecha)
Subtítulo: "Datos que el agente captura"
   ↓
Grilla 2x2 con 4 cajas (3 moradas + 1 del color del proceso): variables que se llenan
   ↓ (flecha)
Caja ámbar: "Smart Tag: [tag]" + código entre paréntesis
   ↓ (flecha)
Subtítulo: "Qué hace el agente"
   ↓
3 cajas teal verticales:
  - "Respuesta inmediata" + descripción
  - "Notificación al equipo" + descripción
  - "Seguimiento programado" + descripción
```

### 6. Reglas de color y jerarquía
- Caja gris arriba (mensaje del usuario) = punto de entrada neutro.
- Cajas ámbar para Embudo y Smart Tag = decisiones del agente.
- Grilla de variables: 3 cajas en morado (transversales) + 1 caja en color del proceso (estado).
- Cajas teal abajo = acciones del agente hacia el equipo humano.

### 7. Tipografía y estilo
- Título del escenario: 14px bold
- Mensaje del usuario: 14px (es la frase clave que arranca el flujo, debe leerse fácil)
- Cajas ámbar (Embudo, Smart Tag): 14px bold
- Variables capturadas: 12px regular
- Acciones del agente: 12px regular con label en font-weight 500

### 8. Especificaciones técnicas
- Dimensiones SVG: 680x720
- DPI PNG final: 200

### 9. Casos de uso
Transversal a todos los clientes. Los 3 escenarios deben mostrar **3 procesos diferentes** (ej: Venta, Soporte, FAQ) para cubrir el espectro del modelo.

### 10. Anti-patrones
- ❌ Los 3 escenarios del mismo proceso (no muestran la diversidad del modelo).
- ❌ Mensaje del usuario sin texto entrecomillado (pierde realismo).
- ❌ Solo 1 acción del agente (deben ser 3: respuesta inmediata, notificación, seguimiento programado).
- ❌ Mezclar colores de embudo (si el escenario es Venta, el embudo va en verde implícito o ámbar — pero las variables de estado van en verde).

---

## GRÁFICO 6 — CÓMO SE DISPARA UN SEGUIMIENTO (FÓRMULA)

### 1. Nombre
Fórmula del Seguimiento / Las 3 condiciones

### 2. Sección del DOCX
Sección "Seguimientos", reemplaza la card explicativa antigua. Va antes del Overview de Seguimientos.

### 3. Qué comunica
"Para que un seguimiento se dispare, tienen que coincidir 3 condiciones al mismo tiempo (etapa, exclusión y tiempo). Si falta una, no se dispara."

### 4. Tipo de diagrama
Capas apiladas verticalmente (una sobre otra) con flecha al disparo final.

### 5. Estructura visual concreta
- Título: "Las 3 condiciones tienen que coincidir al mismo tiempo"
- Subtítulo: "si falta una sola, el seguimiento NO se dispara"
- 3 capas horizontales apiladas verticalmente (mismo ancho, una sobre otra):

```
Capa 1 (color del embudo):
  Label superior: "Requisito 1 — en qué etapa quedó el usuario"
  Frase principal: "Etapa: está conversando con el asistente"
  Código entre paréntesis: "(etiqueta En Conversación)"

Capa 2 (gris):
  Label superior: "Requisito 2 — a quién NO le escribimos"
  Frase principal: "Todavía no lo tomó el equipo"
  Código: "(no tiene la etiqueta Derivado)"

Capa 3 (verde):
  Label superior: "Requisito 3 — cuánto esperar antes de escribir"
  Frase principal: "Tiempo: pasaron 24hs sin respuesta"
  Código: "(24hs)"
```

- Flecha gruesa hacia abajo (stroke-width 2px).
- Caja final coral con borde 1px: "El agente envía el mensaje" + ejemplo entre comillas.
- Pie del gráfico: "si el usuario responde antes de las 24hs, el seguimiento se cancela solo"

### 6. Reglas de color y jerarquía
- Las 3 capas conservan los colores semánticos del sistema:
  - Etapa → color del embudo
  - Exclusión → gris
  - Tiempo → verde (positivo, "tiempo cumplido")
- El disparo final en coral (acción del agente).
- La flecha entre capas y el disparo es **más gruesa** (2px) para enfatizar el momento del disparo.

### 7. Tipografía y estilo
- Label superior de cada capa: 11px medium opacity 0.6 (sutil, no compite con la frase principal)
- Frase principal: 14px bold
- Código entre paréntesis: 10px opacity 0.7
- Caja del disparo: título 14px bold + ejemplo 12px regular

### 8. Especificaciones técnicas
- Dimensiones SVG: 680x480
- DPI PNG final: 200

### 9. Casos de uso
Transversal a todos los clientes. Es la pieza pedagógica clave para que el cliente entienda cuándo sale un seguimiento y cuándo se cancela.

### 10. Anti-patrones
- ❌ Usar la palabra "Capa" en lugar de "Requisito" (Valentín validó "Requisito" como término más natural).
- ❌ Las 4 capas separadas con espacios grandes (deben estar pegadas, sugiriendo "apilamiento" / superposición).
- ❌ Usar la sintaxis técnica como protagonista (`Tag + Variable + Variable + Tiempo`) — el bot oficial confirmó que la fórmula se entiende mejor desarmada en componentes pedagógicos.
- ❌ Olvidar el pie del gráfico sobre la cancelación automática.

---

## GRÁFICO 7 — OVERVIEW DE SEGUIMIENTOS

### 1. Nombre
Overview de Seguimientos / Distribución por Proceso

### 2. Sección del DOCX
Sección "Seguimientos", después del Gráfico 6.

### 3. Qué comunica
"Tenemos N seguimientos automáticos para arrancar, distribuidos por proceso."

### 4. Tipo de diagrama
Cards agrupadas en bloques por proceso.

### 5. Estructura visual concreta
- Título: "X seguimientos automáticos para arrancar"
- Subtítulo: "cada uno se dispara cuando se cumplen 4 requisitos al mismo tiempo"
- Bloque grande **verde** (Venta): "Proceso de venta — N seguimientos" + N cards mini, una por follow-up
- Bloque mediano **rojo** (Soporte): "Proceso de soporte — N seguimientos" + cards
- Bloque mediano **azul** (FAQ): "Proceso de FAQ — N seguimientos" + cards
- Pie del gráfico (caja ámbar con borde 1px): "Cada seguimiento se cancela solo si el usuario responde antes" + horario de envío

### 6. Reglas de color y jerarquía
- El bloque de Venta es el más grande (típicamente tiene más follow-ups).
- Bloques de Soporte y FAQ del mismo tamaño relativo.
- El pie del gráfico en ámbar para que destaque (es la regla operativa principal).

### 7. Tipografía y estilo
- Encabezado de cada bloque: 16px bold
- Subtítulo de cada bloque: 12px regular opacity 0.75
- Cards mini de cada follow-up: título 14px bold + descripción 12px + tiempo 10px opacity 0.7

### 8. Especificaciones técnicas
- Dimensiones SVG: 680x540
- DPI PNG final: 200

### 9. Casos de uso
Transversal. Aplicable a cualquier modelo con follow-ups distribuidos en más de 1 proceso.

### 10. Anti-patrones
- ❌ Bloques del mismo tamaño cuando uno tiene 3 follow-ups y otro 1 (visualmente sugiere paridad falsa).
- ❌ Olvidar mencionar la cancelación automática + horario en el pie.
- ❌ Mezclar follow-ups de procesos distintos en el mismo bloque.

---

## GRÁFICO 8 — CÓMO FUNCIONA LA DERIVACIÓN

### 1. Nombre
Flujo de Derivación / El paso clave es calificar

### 2. Sección del DOCX
Sección "Reglas de Distribución", al inicio.

### 3. Qué comunica
"El agente nunca deriva en vacío. Antes de pasar el chat a un humano, califica el caso. Eso es lo más importante."

### 4. Tipo de diagrama
Flujo top-down con paso clave destacado.

### 5. Estructura visual concreta
- Título: "El agente nunca deriva en vacío — siempre califica primero"
- Caja gris arriba: "Llega una conversación" + "por cualquier canal"
- Flecha hacia abajo
- Caja azul: "El agente identifica el caso" + "¿es venta, soporte, seguridad o partnership?"
- Flecha hacia abajo (gruesa, 2px)
- **Caja ámbar GRANDE con borde 2px** (la más destacada del gráfico): "PASO CLAVE — Califica antes de derivar" en 16px + descripción 12px de qué info recopila
- Flecha hacia abajo (gruesa, 2px)
- Subtítulo: "Dispara la etiqueta de derivación"
- Caja coral: "Derivar a humano" + código
- 3 flechas hacia abajo desde la caja coral, divergiendo
- Texto opcional sobre las flechas: "según tipo_derivacion"
- 3 cajas teal abajo (destinos):
  - "Equipo Comercial" + nota "venta o partnership"
  - "Soporte Técnico" + nota "+ push 24/7 si crítico"
  - "Trust & Safety" + nota "casos sensibles"

### 6. Reglas de color y jerarquía
- **La caja del PASO CLAVE es la más destacada visualmente.** Borde 2px (vs 1px de las demás), texto 16px (vs 14px), ocupa más espacio.
- Cajas teal abajo del mismo tamaño (los destinos son paralelos, no jerárquicos).
- La flecha que entra y sale del PASO CLAVE es más gruesa (2px) para enfatizar el momento.

### 7. Tipografía y estilo
- Título principal: 14px medium
- Caja gris (start): 14px bold + 12px regular
- Caja azul (identificación): 14px bold + 12px regular
- **Caja ámbar (paso clave)**: 16px bold + 12px regular (font más grande)
- Caja coral (tag): 14px bold + 10px código
- Cajas teal (destinos): 14px bold + 10px nota italic

### 8. Especificaciones técnicas
- Dimensiones SVG: 680x580
- DPI PNG final: 200

### 9. Casos de uso
Transversal. Es el gráfico más importante de la sección Reglas de Distribución porque comunica un principio operativo crítico.

### 10. Anti-patrones
- ❌ La caja del paso clave del mismo tamaño que las demás (se pierde el énfasis pedagógico).
- ❌ Mostrar 2+ tags coral en este gráfico (modelo v7 = 1 sola tag de derivación).
- ❌ Cajas teal con colores distintos entre sí (los destinos son paralelos, todos teal).
- ❌ Olvidar el texto "según tipo_derivacion" en las flechas que dividen (sin él, no se entiende qué decide a qué área va).

---

## GRÁFICO 9 — NOTIFICACIONES URGENTES 24/7

> **Estado: Diseñado pero no implementado en el DOCX entregado de MIA. Referencia futura.**

### 1. Nombre
Notificaciones Urgentes / Casos críticos 24/7

### 2. Sección del DOCX
Sección "Reglas de Distribución", después del Gráfico 8 (si aplica al cliente).

### 3. Qué comunica
"Hay N casos que generan notificación urgente 24/7. Requieren plan Pro o Enterprise."

### 4. Tipo de diagrama
Comparativa de 2 columnas con destinos.

### 5. Estructura visual concreta
- Título: "X casos generan notificación urgente 24/7"
- Subtítulo: "requieren plan Pro o Enterprise de Prometheo"
- 2 columnas lado a lado:
  - **Columna izquierda (coral)**: "Error crítico" (caso 1)
    - Tipo de caso (ej: crash recurrente, pérdida de datos, no puede ingresar)
    - Flecha hacia abajo
    - Caja teal con destinatario: "Soporte Técnico (24/7)"
  - **Columna derecha (morado oscuro)**: "Seguridad escalada" (caso 2)
    - Tipo de caso (estafa, suplantación, datos comprometidos)
    - Flecha hacia abajo
    - Caja teal con destinatario: "Trust & Safety (24/7)"
- Pie del gráfico en gris: "Confirmar plan contratado con el equipo de Prometheo para que las notificaciones lleguen efectivamente fuera de horario laboral"

### 6. Reglas de color y jerarquía
- Coral para "Error crítico" (acción del agente + criticidad técnica).
- Morado oscuro para "Seguridad escalada" (color de proceso seguridad + criticidad).
- Cajas teal abajo (destinos humanos).
- Pie en gris (info del sistema).

### 7. Tipografía y estilo
- Título principal: 14px medium
- Encabezados de columna: 16px bold
- Descripción del caso: 12px regular
- Cajas teal: 14px bold

### 8. Especificaciones técnicas
- Dimensiones SVG: 680x360
- DPI PNG final: 200

### 9. Casos de uso
Solo para clientes que tienen casos urgentes 24/7 reales (típicamente apps con alto volumen, marketplaces, plataformas con datos sensibles).

### 10. Anti-patrones
- ❌ Hacer este gráfico para clientes que no tienen casos 24/7 (ej: BETROX o desarrollistas sin urgencia operativa).
- ❌ Olvidar el pie sobre el plan Pro/Enterprise (es un gating técnico que el cliente tiene que validar).

---

## CHECKLIST DE VALIDACIÓN DEL DOCX

Antes de entregar el DOCX al cliente, verificar:

- [ ] Los 7 gráficos confirmados están embebidos en su sección correspondiente
- [ ] Cada gráfico respeta el patrón visual del tipo correspondiente
- [ ] **Frase comprensible primero** en TODOS los textos de cajas
- [ ] **Código técnico solo entre paréntesis**, font más chico, opacity reducida
- [ ] **Color por significado** consistente entre gráficos (no arcoíris)
- [ ] **Sentence case** en TODOS los labels
- [ ] **Sin emojis decorativos**
- [ ] **Sin texto que se sale de las cajas**
- [ ] **Flechas direccionales centradas**
- [ ] **PNG de alta resolución** (DPI ≥ 200)
- [ ] **Tamaño de los gráficos ajustado a A4** con márgenes
- [ ] **Workflow de 2 pasos respetado:** prototipo SVG aprobado → PNG final embebido

---

## ANTI-PATRONES TRANSVERSALES (lecciones aprendidas)

Errores que cometimos en MIA y descartamos:

### Errores conceptuales
- ❌ Diseñar gráficos con sintaxis técnica (`tipo_usuario=inversor`) en lugar de lenguaje cliente-facing.
- ❌ Confundir variables con tags en los gráficos (mostrar variables como cajas de "tags").
- ❌ Diseñar gráficos basados en versiones anteriores del modelo (v5, v6) sin reflejar las decisiones del v7.
- ❌ Asumir comportamiento de Prometheo sin validar con bot oficial — siempre preguntar antes.

### Errores visuales
- ❌ Listas con bullets en lugar de cajas con flechas.
- ❌ Más de 3 colores semánticos en un mismo gráfico.
- ❌ Texto desbordado de las cajas (achicar texto en lugar de agrandar caja).
- ❌ Flechas no centradas o que cruzan otras flechas innecesariamente.
- ❌ Mayúsculas en labels (rompe la jerarquía visual y la legibilidad).
- ❌ Emojis decorativos sin función pedagógica.

### Errores de proceso
- ❌ Saltarse el paso del prototipo SVG y generar PNG directamente (cada iteración cuesta más).
- ❌ Generar los 8 gráficos sin validar uno primero (si hay un problema de estilo, se replica en todos).
- ❌ No registrar las decisiones aprobadas en memoria (cada conversación nueva tiene que reinventar el estilo).
- ❌ Mencionar Make/Zapier para cosas que Prometheo soporta nativamente (como combinación AND en seguimientos).

---

## EJEMPLOS DE APLICACIÓN

### Caso de referencia principal: MIA App (octubre 2026)

| Sección | Gráficos aplicados |
|---|---|
| Embudos | (no se aplicó Gráfico 1, era diseño futuro) |
| Variables | Gráfico 2 (Overview) + Gráfico 3 (Arquitectura) |
| Smart Tags | Gráfico 4 (Overview) |
| 3 Escenarios de Ejemplo | Gráfico 5 (3 versiones: Venta, Soporte, Partnership) |
| Seguimientos | Gráfico 6 (Fórmula) + Gráfico 7 (Overview) |
| Reglas de Distribución | Gráfico 8 (Derivación). Gráfico 9 quedó como diseño futuro. |

### Aplicaciones futuras pendientes

| Cliente | Vertical | Estado |
|---|---|---|
| EDFAN Real Estate | Desarrollista inmobiliario | Etapa 1 lista, Etapa 2 pendiente |
| EDFAN Productos | Insumos construcción | Etapa 1 en progreso |
| ZATOH | Insumos construcción | Etapa 1 lista |
| BETROX | Mobiliario | Etapa 1 + 2 en iteración |

---

## REFERENCIAS CRUZADAS CON OTRAS SKILLS AUREA

- `aurea-diseno-etapa2` (Skill maestra) — esta skill se invoca dentro del flujo de Etapa 2.
- `prometheo-vertical-real-estate` — vertical para desarrollistas inmobiliarios.
- `prometheo-vertical-mobiliario` — vertical para mobiliario.
- `prometheo-discovery-transversal` — Etapa 1 (precondición de Etapa 2).

---

**Fin de la skill `prometheo-crm-graphics` v1.0.**

*Si en futuras sesiones se descubren nuevos patrones visuales o se ajustan reglas, actualizar este documento y registrarlo en memoria como convención AUREA.*
