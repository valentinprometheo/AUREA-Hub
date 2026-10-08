---
name: criterio-calificacion-leads
description: Criterio de Calificación de Leads en el CRM (AUREA Hub × Prometheo). Define qué es un lead calificado y un hot lead para cada cliente, cómo se traduce cada condición a variables, tags y embudos de Prometheo, cómo se audita y se mide en el tablero de Inteligencia Comercial, cómo se aplica de forma masiva con Mi Prometheo y cómo se cuida el consumo de tokens. Capa transversal más un archivo por rubro (real estate, inmobiliaria, construcción, mobiliario, escuelas y más); carga solo el rubro necesario. Usala SIEMPRE que haya que definir, auditar, medir o corregir la calificación de leads, diseñar el hot lead, separar no-demanda (inmobiliarias, proveedores) del embudo, armar prompts de Mi Prometheo para recalificar contactos, o revisar el ahorro de tokens de una cuenta. Activar ante "calificado", "lead calificado", "hot lead", "calificación", "criterio de calificación", "lead scoring", "no fit", "recalificar", "re-etiquetar contactos", "qué es un buen lead", "ahorro de tokens", "consumo de IA".
---

# Criterio de Calificación de Leads en el CRM

La calificación decide a quién llama el equipo, qué seguimiento recibe cada lead, qué
aprende la pauta y cuánto saldo de IA se gasta. Es un tema sensible: un número de
"calificados" mal definido mueve presupuesto y prioridades con un dato falso. Esta skill
existe para que el criterio sea **del cliente, explícito, medible y auditable**.

Caso de origen: EDFAN Real Estate (octubre 2026). Con un criterio propio de AUREA el
tablero mostró 350 calificados; con la regla que definió el cliente eran 252 (176 en la
lectura estricta). Ese error es el motivo de esta skill.

---

## Paso 0 · Antes de trabajar, pedí dos cosas (no supongas)

1. **El rubro del cliente.** Si el contexto ya lo dice (cliente conocido, export, conversación
   previa), confirmalo en una línea. Si no, preguntalo.
2. **El documento del discovery donde el cliente define la calificación**: la sección de
   calificación del Doc 1 (biblia), el formulario de reunión o una definición escrita como
   "Lead calificado / Hot lead" con obligatorios, sumas y señales. Pedilo siempre.

Si el cliente todavía no definió la calificación, usá el molde del rubro como **propuesta a
validar**, rotulada así en todo entregable. Nunca presentes un criterio de AUREA como si
fuera el del cliente, y nunca titules un número de calificados con un criterio no validado.

## Paso 1 · Cargá solo lo que la tarea necesita

| Necesitás… | Leé |
|---|---|
| El molde del rubro del cliente | **Solo** `references/rubros/<rubro>.md` (uno) |
| Rubro nuevo, sin archivo | `references/rubros/_plantilla-nuevo-rubro.md` |
| Citar evidencia externa (speed-to-lead, orden de preguntas, scoring, Meta) | `references/fuentes-externas.md` |
| Aplicar el criterio a contactos existentes con Mi Prometheo | `references/mi-prometheo-acciones-masivas.md` |
| Auditar una cuenta o un tablero ya armado | `references/malas-practicas.md` |
| Consumo de IA, tokens y costo de Meta | `references/ahorro-de-tokens.md` |

| Rubro | Archivo | Estado |
|---|---|---|
| Real estate · desarrollista (pozo, construcción, entrega) | `rubros/real-estate.md` | Validado con cliente (EDFAN) |
| Inmobiliaria tradicional (compra, alquiler, tasación) | `rubros/inmobiliaria.md` | Propuesta a validar |
| Construcción · insumos y materiales para obra | `rubros/construccion.md` | Propuesta a validar |
| Mobiliario | `rubros/mobiliario.md` | Propuesta a validar |
| Escuelas de cursos y carreras | `rubros/escuelas.md` | Propuesta a validar |
| (rubro nuevo) | crear desde `_plantilla-nuevo-rubro.md` | — |

No cargues los otros rubros "por las dudas": cada archivo es autosuficiente junto con este.

---

## Paso 2 · El modelo transversal (vale para todos los rubros)

### 2.1 Separar antes de calificar
No todo el que escribe es demanda. Antes de calificar se clasifica el **tipo de contacto**
en valores excluyentes (comprador / canal B2B / proveedor / otro que corresponda al rubro).
Solo el comprador entra a la calificación. El canal B2B tiene su propio embudo; los
proveedores y similares se derivan sin calificar y con el asistente apagado.
- En Prometheo: una variable de Opciones "Tipo de contacto", con la finalidad (vivienda,
  inversión, etc.) como variable hija solo para compradores. No mezclar en una misma
  variable la finalidad con el tipo de contacto.

### 2.2 Calificado = obligatorios + sumas
- **Obligatorios** (fit mínimo): lo que el negocio efectivamente vende. Si falta uno, no
  califica, por más datos que haya. Ej.: proyecto o zona que se comercializa, tipología que existe.
- **Sumas**: condiciones que acercan a la compra (intención, finalidad, capacidad de pago,
  plazo, compatibilidad con el producto). La regla es "todos los obligatorios + al menos k de n sumas".
- **Descalificación explícita** (No Fit) con motivo: busca algo que no existe, zona sin
  producto, operación que no se ofrece. Tiene que existir señal negativa o pasa cualquiera.
- Calificar por **cantidad de datos** no es calificar: un lead con cinco variables sobre algo
  que la empresa no vende no está calificado.

### 2.3 Hot lead = señales de intención, no una etapa
- El hot lead se define por **señales** (alcanza con 1): pide visita o reunión, pide precio o
  disponibilidad de algo concreto, compra ya o en el corto plazo, tiene el dinero, vuelve
  sobre lo mismo. Se adaptan por rubro.
- **Es una prioridad, no una etapa**: un tag propio ("Hot Lead") que convive con la etapa del
  embudo, con notificación inmediata al asesor (por variable si el ruteo depende de la
  finalidad o la zona) y prioridad en el seguimiento.
- Hot no implica calificado: un lead puede mostrar urgencia antes de dar los datos.
- **Definí el plazo en días.** "Corto plazo" sin número no se puede medir ni filtrar.
  Referencia externa: hot = listo en 3 meses o menos (ver fuentes).

### 2.4 Orden conversacional
Captura pasiva primero (lo que trae el anuncio y lo que el lead ya dijo), después necesidad y
plazo, después capacidad, y el presupuesto al final. Una pregunta por mensaje, sin
interrogatorio, sin re-preguntar lo que ya está. No trabar consultas atómicas: responder el
eje que trajo al lead antes de calificar (regla 16 de la metodología).

### 2.5 Traducción a Prometheo
Cada condición del cliente se traduce a una variable (tipo y valores) o a un tag, en una tabla
explícita. Reglas:
- La variable captura, el tag muestra (el tag es espejo de la variable, no fuente).
- Lo que el agente **ofreció** no es lo que el lead **pidió**: si una variable puede llenarse
  con la oferta del agente (ej. tipologías listadas), su prompt tiene que pedir solo lo
  declarado por el lead.
- "Compatible" (presupuesto, plazo, estado de obra) solo se puede medir si existe el dato del
  producto (catálogo, precios). Si no está, se mide "declarado" y se dice que es aproximado.
- Las etapas que marca el equipo no necesitan prompt de IA (ahorran tokens).

### 2.6 Velocidad y ruteo
El valor del lead cae rápido con el tiempo (ver fuentes: speed-to-lead). El agente responde
al instante; el hot lead se notifica al humano en el momento y se mide en minutos. El ruteo
(quién atiende qué) se registra en el CRM: si no se ve en el export, no existe para el tablero.

### 2.7 Medir sin maquillar (liga con `aurea-ic-curaduria-del-dato`)
- Usá la definición del cliente. Si hay partes aproximadas, mostrá un **rango** (lectura
  estricta y amplia) y explicá qué falta para que sea exacto.
- Cada condición lleva su cobertura y su nivel de evidencia. Las que no se pueden medir se
  dicen ("no medible con este export").
- Si cambiás de criterio entre versiones de un tablero, decilo en el tablero, con el número
  anterior y el nuevo.
- Ningún benchmark de "% de calificados" sin fuente. La meta sale de la línea base del cliente.

### 2.8 Aplicarlo a contactos existentes
Cuando el criterio cambia o se define tarde, se recalifica la base con Mi Prometheo por lotes
filtrados por variables, con prueba chica primero, conteo esperado y auditoría de precisión
contra el criterio. Procedimiento completo en `references/mi-prometheo-acciones-masivas.md`.

### 2.9 Devolver la señal a la pauta
El objetivo es que la pauta aprenda de los calificados y hot leads, no de los mensajes.
Requisito: el tag bien cargado. Detalle técnico (Conversions API para mensajería) en fuentes.

### 2.10 Tokens
La calificación también es un tema de costo: cada conversación paga extracción de variables
y Smart Tags. Separar la no-demanda, apagar el asistente con proveedores, dejar manuales las
variables sin uso y no mandar material antes de que el lead responda son ahorro directo.
Ver `references/ahorro-de-tokens.md`. **En real estate es regla** proponer una línea de
WhatsApp aparte para inmobiliarias y proveedores y medirlo en el tablero.

---

## Paso 3 · Entregables típicos

1. **Definición del cliente, normalizada** (tabla): condición · obligatoria o suma · regla
   (todos + k de n) · descalificaciones · señales hot · plazo de "corto plazo" en días · ruteo.
2. **Traducción a Prometheo** (tabla): condición · variable o tag · tipo y valores · prompt
   de extracción corto · cómo se mide en el export · nivel de evidencia.
3. **Medición** en el tablero: calificados (rango), hot leads, por qué no califican los demás,
   qué es aproximado, corrección frente a versiones anteriores.
4. **Prompts de Mi Prometheo** auditados para aplicarlo a la base.
5. **Ahorro de tokens** ligado a la calificación.

## Checklist antes de entregar
- [ ] Pedí (o confirmé) rubro y documento de discovery con la definición del cliente.
- [ ] Cargué solo el archivo del rubro.
- [ ] La no-demanda está separada antes de calificar, con valores excluyentes.
- [ ] Obligatorios, sumas y regla k de n explícitos; descalificación con motivo.
- [ ] Hot lead como tag de prioridad con ruteo; "corto plazo" en días.
- [ ] Ninguna variable mezcla lo que ofreció el agente con lo que pidió el lead.
- [ ] El número de calificados usa la definición del cliente, con rango si hay aproximaciones.
- [ ] Ningún benchmark sin fuente.
- [ ] Cada acción masiva tiene prueba chica, conteo esperado y forma de revertir.
- [ ] Ahorro de tokens considerado (y en real estate, la línea separada propuesta).

## Mejora continua de esta skill
- Un hallazgo de un cliente entra al archivo de su rubro como **instancia** (con el nombre
  del cliente). Sube a este `SKILL.md` como **patrón transversal** solo cuando lo confirma un
  segundo rubro distinto (mismo criterio de promoción que `aurea-metodologia`).
- Rubro nuevo: copiar `_plantilla-nuevo-rubro.md`, completarlo con el discovery del primer
  cliente y sumarlo a la tabla del Paso 1.
- Cada cambio se anota en `references/CHANGELOG.md`.

## Skills relacionadas
`aurea-metodologia` (diseño de embudos, tags y variables) · `aurea-ic-curaduria-del-dato`
(qué número se muestra) · `aurea-ic-criterio-comercial` (campos de problema, impacto y
disparador) · `aurea-ic-dashboard` (tablero) · `prometheo-discovery-transversal` y los
formularios de rubro (dónde se releva la definición del cliente).
