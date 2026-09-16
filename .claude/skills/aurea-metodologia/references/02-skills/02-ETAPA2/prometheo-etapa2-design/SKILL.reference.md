---
name: prometheo-etapa2-design
description: >
  Skill maestra de Etapa 2 (Diseño) para clientes de Prometheo. Genera los 4 outputs
  finales que se entregan al cliente: (1) DOCX cliente-facing "Diseño de CRM" con
  metodología visual AUREA — banner→card→gráfico→tabla→ejemplo→feedback por sección,
  con cuadros SVG embebidos para puntos difíciles de explicar, (2) Prompt del agente
  en prosa redactada lista para pegar en Prometheo (formato V6 — sin tablas markdown,
  separadores ===), (3) Doc de Refactorización con inconsistencias entre inputs e info
  pendiente, (4) Excel/Sheets de Carga de Contactos para volcar la base histórica de
  leads al CRM desde el día 1 (alineado a embudos, tags y variables). Usa como inputs
  los outputs de Etapa 1 (Doc 1, 2, 3, 4) + auditoría web + skill vertical, opcionalmente
  brochures, planos, fotos, imágenes de productos (cuando no estén disponibles,
  ignorarlos). El consultor puede arrancar Etapa 2 antes de cerrar todos los inputs de
  Etapa 1. Modelo de tags vigente: 2 Smart Tags visibles por lead (ESTADÍO de embudo +
  TIPOLOGÍA) con opcional 3ª de PRIORIDAD combinable; las etapas de embudo SON tags; el
  estadío NO va en variable. Acopla con prometheo-discovery-transversal, aurea-crm-graphics,
  y la skill vertical correspondiente. Activar ante: "diseño de CRM", "prompt de agente",
  "etapa 2", "diseño del prompt", "refactorización", "excel de carga", "base de leads",
  "base de contactos", "armar los outputs", "Doc de CRM cliente-facing", "diseñar agente
  IA", o cuando Valentín diga "pasamos a etapa 2 con [cliente]".
---

# SKILL: ETAPA 2 — DISEÑO DE CRM Y PROMPT (PROMETHEO × AUREA)

## ACOPLE OBLIGATORIO

- **prometheo-discovery-transversal** — la metodología de Etapa 1 que produce los inputs.
- **aurea-crm-graphics** — la skill visual para todos los gráficos SVG.
- **Skill vertical del cliente** (real-estate, mobiliario, etc.) — define tipología macro y particularidades.

Si falta la vertical, pedir a Valentín que la identifique antes de avanzar.

---

## SECCIÓN 0 — ARQUITECTURA DE 3 CAPAS (el fundamento de todo)

El CRM de cualquier cliente se diseña en 3 capas que NO se mezclan. El DOCX, el
prompt y el Excel de carga son todos reflejos de estas 3 capas. Si las capas
están mal definidas, los 4 outputs heredan el error.

### Capa 1 — Embudos (el recorrido del lead)
Un embudo es un proceso por el que transita el lead. Cada embudo tiene:
- un **responsable claro** (el agente IA, o el equipo humano — nunca ambiguo)
- un **conjunto de etapas excluyentes** que el lead recorre en orden
- una **naturaleza propia** (calificación, transacción, gestión de relación)

**Regla de cuántos embudos:** un embudo separado se justifica solo cuando
**cambia el actor o cambia la naturaleza del proceso**. Si el recorrido es el
mismo, es el mismo embudo.

**Qué NO es un embudo (corrección conceptual clave):**
- **FAQ no es un embudo.** Es una interacción puntual sin estados que persistan.
  El lead pregunta, el agente responde, se cierra. No hay "estado actual de FAQ".
- **Excepciones no es un embudo.** Es un disparador de derivación que manda el
  lead al embudo correcto. No tiene recorrido propio.

(Esto fue un error en diseños iniciales que listaban 4 embudos: Venta, Derivación,
FAQ, Excepciones. El modelo correcto deja FAQ y Excepciones fuera de los embudos.)

**Arrancar minimalista:** si un proceso se gestiona 100% manual y por fuera del
sistema (típico B2B), su embudo arranca con pocas etapas y se expande cuando se
valida la dinámica real. No inventar estados que el cliente no usa.

### Capa 2 — Smart Tags (lo que se ve de un vistazo) — REGLA NUEVA AUREA

**La regla de las 2 Smart Tags visibles:**
> Todo lead muestra **dos** Smart Tags de un golpe de vista en el panel de Chats:
> su **ESTADÍO** (la etapa del embudo donde está) y su **TIPOLOGÍA** (la categoría
> más fuerte que lo diferencia). Opcionalmente una tercera de **PRIORIDAD** que
> se combina con la tipología.

Esta es la regla central. Todos los rubros se nomenclan así: estadío de embudo +
tipología (categoría fuerte) inmediatamente después.

**Sub-reglas de Smart Tags:**
- **Las etapas de embudo SON Smart Tags.** No son una cosa aparte. (Verificado
  en plataforma Prometheo.)
- **Las etapas son mutuamente excluyentes y se reemplazan al avanzar.** Un lead
  está en una sola etapa por embudo; al pasar a la siguiente, la tag anterior se
  reemplaza (no se acumulan). (Verificado en plataforma.)
- **Una tag de tipología se deriva de las variables, no se pide dos veces.** La
  variable captura el dato (ej. `objetivo_busqueda`), la tag lo muestra. Misma
  información, dos representaciones.
- **La tag de prioridad se combina, no es excluyente.** Un lead puede ser
  `#inversor + #contacto_vip` a la vez.
- **No diseñar tags con alta similitud semántica.** Si dos tags se leen casi
  igual, el equipo las confunde en el panel. (Ej. real: "Visita a Coordinar" vs
  "Visita Coordinada" → se renombró a "Por Coordinar" vs "Visita Agendada".)
- **Una tag se crea solo si genera una acción concreta o una distinción visual
  que el equipo necesita ver sin abrir el chat.** Si el detalle puede vivir en
  una variable y nadie necesita verlo de un vistazo, va a variable.

**Nota sobre el modelo MIA (histórico):** MIA usó 2 tags lógicas
(`#seguimiento_activo` + `#derivar_a_humano`) en lugar del modelo estadío +
tipología. Ese fue un modelo temprano. El modelo vigente y correcto para nuevos
clientes es el de las una tag por dimensión: estadío + tipo de usuario + prioridad opcional. Si se retoma MIA,
evaluar migración.

### Capa 3 — Variables (el detalle que se filtra)
Una variable es un dato puntual del lead que el agente captura silenciosamente.
Cada variable es una columna en el Excel de carga.

**Reglas de variables:**
- **Prefijo `var_`** para distinguirlas rápido en el Excel y en Prometheo.
- **El estadío NO va en variable.** Con el modelo "etapa = tag", las viejas
  variables de estado (`proceso_actual`, `estado_venta`, `estado_derivacion`)
  quedan redundantes y se eliminan. El estadío vive en la tag, no en columna.
- **Variable vs Tag — regla de decisión:** si el dato necesita verse de un
  vistazo en el panel para clasificar/agrupar → tag. Si es detalle puntual que
  se filtra o segmenta → variable.
- **Una variable puede gobernar a otras (router):** su valor habilita o bloquea
  preguntas posteriores. (Ej. real estate: `objetivo_busqueda=inversion` permite
  preguntar renta/m²; `uso_propio` no.)
- **Variables de handoff:** se llenan solo al derivar (ej. `tipo_derivacion`).

### Implicancia para los 4 outputs
- **DOCX:** la sección Embudos refleja Capa 1, la sección Smart Tags refleja
  Capa 2 (con las 2 tags visibles), la sección Variables refleja Capa 3.
- **Prompt:** instruye al agente a mover etapas (tags de estadío), asignar
  tipología, y capturar variables.
- **Doc Refactorización:** detecta inconsistencias en cualquiera de las 3 capas.
- **Excel de carga:** columna Estadío (Capa 1+2), columna Tipología (Capa 2),
  columna VIP (Capa 2 prioridad), columnas `var_` (Capa 3).

---

## SECCIÓN 1 — INPUTS Y FLEXIBILIDAD

### Inputs principales (ideales)
1. **Doc 1 (Síntesis/Biblia)** — la fuente principal de verdad
2. **Doc 2 (Asincrónico)** — pendientes que el cliente debía completar
3. **Doc 3 (Accesos)** — credenciales y links a Drive/Tokko/PrestaShop
4. **Doc 4 (Preguntas clave de aprobación)** — confirmaciones del cliente
5. **Doc 0 (Auditoría web)** — interno AUREA con hipótesis cerradas

### Inputs complementarios (opcionales, cruzados)
- Brochures comerciales del cliente
- Planos de proyectos (verticales real estate)
- Fotos de productos (verticales mobiliario, insumos)
- Imágenes de catálogo, paletas de color, materiales
- Conversaciones reales WhatsApp exportadas
- Prompts de otros agentes del cliente (si ya tiene IA)

### REGLA DE ARRANQUE FLEXIBLE
**Etapa 2 puede empezar antes de cerrar todos los inputs.** El consultor decide.
Si arranca incompleto: marcar en el Doc de Refactorización lo que falta y avanzar
con lo que hay. **Nunca inventar datos** — si falta, queda como pregunta o placeholder.

### REGLA DE INPUTS COMPLEMENTARIOS
Cuando hay brochures/planos/fotos: usarlos para validar, enriquecer y detectar
inconsistencias contra Doc 1. Cuando NO hay: ignorarlos sin pedirlos. Nunca
condicionar el avance a su existencia.

---

## SECCIÓN 2 — OUTPUTS (los 3 entregables)

### Output 1: DOCX "Diseño de CRM" (cliente-facing)
Documento principal de presentación al cliente. Sigue rigurosamente la metodología
visual AUREA. Detalle completo en **`docx_diseno_crm.md`**.

### Output 2: Prompt del agente (prosa redactada)
Archivo .md con el prompt listo para copiar y pegar en Prometheo. **Sin tablas
markdown ni cuadros visuales** — solo prosa redactada con separadores `===`. Detalle
completo en **`prompt_design.md`**.

### Output 3: Doc de Refactorización (interno + cliente-facing parcial)
Registra dos cosas: (a) información pendiente de los inputs de Etapa 1, (b)
incoherencias detectadas entre inputs (típico: brochure vs Doc 1). Detalle
completo en **`refactorizacion.md`**.

### Output 4: Excel/Sheets de Carga de Contactos
Planilla donde el cliente vuelca su base histórica de leads para que el agente
la tenga desde el día 1. Su estructura refleja las 3 capas (embudos, tags,
variables). Tiene 2 hojas: INSTRUCCIONES (enseña al cliente) y LEADS (donde
carga). Detalle completo en **`excel_carga_contactos.md`**.

---

## SECCIÓN 3 — ORDEN DE EJECUCIÓN

1. **Leer todos los inputs disponibles**, marcar los que faltan.
2. **Identificar la vertical** y cargar la skill vertical correspondiente.
3. **Detectar inconsistencias** entre inputs (Doc 1 vs brochures, Doc 1 vs auditoría
   web, Doc 1 vs Doc 4) → input para Doc de Refactorización.
4. **Diseñar el modelo conceptual** del CRM antes de generar nada:
   - Embudos (procesos paralelos del agente)
   - Variables transversales + variables de estado por embudo
   - Smart Tags (mínimas posibles, lógica 1 sola activa por conversación)
   - Seguimientos (formula de 4 condiciones)
   - Reglas de derivación
5. **Generar los gráficos SVG** según la skill `aurea-crm-graphics`.
6. **Armar el DOCX** siguiendo la estructura de 11 secciones (sección 4 abajo).
7. **Armar el prompt** en prosa redactada (formato V6).
8. **Armar el Doc de Refactorización**.
9. **Armar el Excel de carga de contactos** (si el cliente tiene base histórica).
10. **Validar antes de entregar:** OOXML, no tablas anidadas, styles.xml minimal;
    para el Excel, validar con recalc.py y confirmar Sheets de lectura plano.

---

## SECCIÓN 4 — ESTRUCTURA DEL DOCX (11 secciones obligatorias)

Cada sección sigue la fórmula visual: **banner → card explicativa → gráfico
overview → tabla técnica → gráfico arquitectura/detalle (si aplica) → card
"EJEMPLO PARA QUE SE ENTIENDA" → bloque de feedback amarillo**.

1. **Portada + "Qué es este documento"**
2. **Roles del Agente** (tabla 5 roles × estado MVP)
3. **Estrategia + KPIs** (mínimo 5, máximo 8 KPIs con columna "Por qué lo medimos")
4. **Autonomía** (tabla 2 columnas PUEDE/NO PUEDE con palabras clave en bold)
5. **Embudos** (gráfico mapa + tabla etapas + recorrido textual)
6. **Variables** (gráfico overview + tablas transversales/handoff/estado +
   gráfico arquitectura + card ejemplo storytelling)
7. **Smart Tags** (gráfico overview + tabla resumen + cuadro "Explicado:" para
   cada smart tag que sea difícil de entender — ver sección 7)
8. **3 Escenarios de Ejemplo** (3 gráficos verticales con mismo template,
   cubriendo procesos distintos)
9. **Seguimientos** (gráfico fórmula 4 condiciones + gráfico overview con
   distribución por proceso a 24h y 72h + tablas de mensajes literales)
10. **Reglas de Distribución** (gráfico derivación + gráfico notificaciones
    urgentes + tabla cliente-facing con columnas vacías para que complete)
11. **Pendientes del Equipo** + **Próximos Pasos**

Para detalle exhaustivo de cada sección ver **`docx_diseno_crm.md`**.

---

## SECCIÓN 5 — INVENTARIO DE GRÁFICOS TRANSVERSALES

Todos los gráficos son **transversales** (sirven para cualquier cliente). El contenido
cambia según vertical, el template visual no. Ver **`aurea-crm-graphics`** skill para
las especificaciones exactas de cada uno.

| # | Gráfico | Cuándo se usa |
|---|---|---|
| 1 | Mapa de Embudos | Sección 5 — siempre |
| 2 | Overview Variables | Sección 6 — siempre |
| 3 | Arquitectura Variables (router) | Sección 6 — siempre |
| 4 | Overview Smart Tags | Sección 7 — siempre |
| 5a/5b/5c | 3 Escenarios | Sección 8 — siempre, cubrir 3 procesos distintos |
| 6 | Fórmula Seguimiento (4 condiciones) | Sección 9 — siempre |
| 7 | Overview Seguimientos (distribución por proceso, 24h y 72h) | Sección 9 — siempre |
| 8 | Derivación (paso clave: califica antes) | Sección 10 — siempre |
| 9 | Notificaciones Urgentes 24/7 | Sección 10 — si hay plan Pro/Enterprise |
| 10 | Cuadro "Explicado:" #seguimiento_activo | Sección 7 — siempre |
| 11+ | Cuadros "Explicado:" adicionales | Cuando un punto es difícil de explicar |

---

## SECCIÓN 6 — CUÁNDO AGREGAR CUADROS "EXPLICADO:" ADICIONALES

Patrón heredado del HTML de MIA. Cada vez que un concepto del modelo CRM cumple
**al menos uno** de estos criterios, agregar un sub-cuadro tipo "Explicado:" con
gráfico SVG dentro de la sección correspondiente.

### Disparadores (cuándo agregar):
1. **Lógica de mutua exclusión o cancelación automática** (ej: #seguimiento_activo
   se retira cuando aparece #derivar_a_humano)
2. **Variables condicionales complejas** (ej: estado_X solo se llena si proceso_actual=X)
3. **Reglas de distribución con múltiples paths** (ej: 6 tipos de derivación, 2 destinos
   distintos según severidad)
4. **Workflows multi-paso con bifurcaciones** (ej: el agente captura → valida → deriva
   pero solo si severidad alta dispara push 24/7)
5. **Conceptos que ya generaron preguntas en la reunión con el cliente** — disparador
   empírico, el más importante.

### Estructura del cuadro "Explicado:":
- Título con `#nombre_concepto` o nombre exacto
- Subtítulo: una sola frase que explica para qué sirve
- 3-5 bloques de color siguiendo paleta AUREA (verde=disparador positivo,
  ámbar=acción operativa, coral=resultado, rojo=cancelación, gris=regla pie)
- Ejemplo concreto en uno de los bloques
- Pie con regla operativa adicional si corresponde

Ver **`cuadros_explicados.md`** para la guía completa con ejemplos.

---

## SECCIÓN 7 — REGLAS CRÍTICAS DEL DOCX

### Visuales (no negociables)
- **Banner** de sección: rectángulo color por tema, texto blanco bold 13pt
- **Card explicativa**: fondo pastel, borde izquierdo grueso 4pt color del tema,
  título bold + 3 bullets cortos
- **Tabla KPIs**: SIEMPRE incluir columna "Por qué lo medimos" en lenguaje
  cliente-facing (no técnico)
- **Tabla Reglas Distribución**: columna "Cuándo" en lenguaje cliente-facing
  ("El usuario quiere X pero pide humano"), NO sintaxis técnica. Agregar columnas
  vacías "Prometheo o WhatsApp" y "Responsable" para que el cliente complete
- **Card EJEMPLO PARA QUE SE ENTIENDA**: storytelling con persona ficticia
  ("Imaginate que llega Juan..."), bullets de variables capturadas, frase
  "Resultado:" en bold verde
- **Bloque de feedback** amarillo pálido al final de cada sección con: 3 checkboxes
  (Aprobado/Con cambios/Necesita revisión) + área "Comentarios" con líneas en blanco
- **Mensajes follow-up con texto literal**: usar placeholder `(emoji de saludo)`
  en DOCX cliente-facing. En el prompt va el emoji real (👋, ✅)
- **Próximos Pasos paso 1**: usar `[PLACEHOLDER_LINK_DRIVE]` para que cliente
  o consultor lo reemplace

### Técnicas (para que el preview de Claude funcione)
- **NO usar tablas anidadas** (max_depth=1). Si necesitás 2 columnas, usá una
  tabla 1×2 con celdas grandes
- **Reemplazar styles.xml** de python-docx por un styles.xml minimal (de Google Docs
  o referencia probada). Sin esto, peso > 1MB y preview falla
- **Eliminar stylesWithEffects.xml** y su referencia en Content_Types y rels
- **Validar OOXML** antes de entregar (validate.py)
- **PNGs a 1000px width** con compress_level=9, total imágenes < 1.5 MB

Detalle de los fixes XML en **`docx_xml_fixes.md`**.

---

## SECCIÓN 8 — REGLAS CRÍTICAS DEL PROMPT

### Formato (no negociable)
- **Prosa redactada corrida**, sin tablas markdown, sin cuadros visuales
- Separadores entre secciones: `===` (no headers markdown)
- 15 secciones canónicas + 3 anexos (ver `prompt_design.md`)
- Emojis reales en mensajes literales (no placeholders)
- Variables y Smart Tags en código exacto: `#seguimiento_activo`, `proceso_actual = venta`

### Reglas de contenido
- **Regla de hilo**: el agente NO interrumpe el tema declarado para mostrar menú
- **Lo que está en Tokko/CRM externo**: NO se hardcodea en el prompt
- **Lo que NO está en CRM externo**: SÍ va al prompt
- **Solo 1 Smart Tag activa por conversación** — esto se enforza vía instrucciones
  explícitas al agente
- **Variables que llena el agente automáticamente** vs **info que pide explícitamente**:
  separar claramente

Detalle exhaustivo en **`prompt_design.md`**.

---

## SECCIÓN 9 — DOC DE REFACTORIZACIÓN

Tercer entregable separado. Tiene 2 secciones obligatorias:

### Sección A — Información pendiente de inputs Etapa 1
Lista de cosas que el cliente prometió completar en Doc 2 pero no completó, o
que faltan resolver en Doc 4 antes del Go-Live. Cada item: qué falta, de qué
input depende, qué bloque del prompt afecta, criticidad (alta/media/baja).

### Sección B — Inconsistencias detectadas entre inputs
Lista de contradicciones entre fuentes. Ejemplo típico: el brochure dice "30
unidades" pero Doc 1 dice "25 unidades". Cada item: qué dice fuente A, qué dice
fuente B, qué hipótesis tomamos para el prompt, qué validación pedimos al
cliente.

Detalle completo en **`refactorizacion.md`**.

---

## SECCIÓN 10 — VALIDACIÓN ANTES DE ENTREGAR

Checklist obligatorio:

- [ ] Las 11 secciones del DOCX están presentes
- [ ] Todos los gráficos referenciados están embebidos como PNG
- [ ] OOXML pasa validación (validate.py)
- [ ] No hay tablas anidadas (max_depth=1)
- [ ] styles.xml fue reemplazado por minimal (peso < 800 KB)
- [ ] Cada sección tiene su bloque de feedback amarillo
- [ ] Tabla de Reglas de Distribución tiene columnas vacías para el cliente
- [ ] Próximos Pasos tiene placeholder del Drive
- [ ] Prompt está en prosa redactada sin tablas markdown
- [ ] Prompt usa separadores `===` y emojis reales
- [ ] Doc de Refactorización tiene sección A (pendientes) y B (inconsistencias)
- [ ] Si arranque fue incompleto, los gaps están documentados en Refactorización

Si algún item falla → no entregar, corregir primero.

---

## SECCIÓN 11 — REFERENCIA: MIA App como caso paradigmático

MIA es la primera implementación completa de esta metodología. **Usar como referencia
visual y estructural** pero **no copiar contenido**. Diferencias importantes a tener
en cuenta:

- MIA es marketplace/app, NO desarrollista. Su CRM apunta a descarga/registro/publicación,
  no a venta de propiedades.
- Para clientes desarrollistas inmobiliarios, la tipología macro es **proyecto/desarrollo**
  y los seguimientos siguen ciclo de obra, no ciclo de descarga.
- Para clientes de mobiliario, la tipología macro es **línea de producto** y los
  seguimientos siguen ciclo de personalización.
- Para clientes de insumos para construcción, la tipología macro es **categoría +
  tipo de cliente** y la lógica B2B vs B2C es central.

Cada vertical aporta sus particularidades — la skill vertical correspondiente las
define. Esta skill define la **estructura común**.

---

## ARCHIVOS AUXILIARES DE ESTA SKILL

| Archivo | Cuándo leerlo |
|---|---|
| `docx_diseno_crm.md` | Antes de empezar a generar el DOCX |
| `prompt_design.md` | Antes de empezar a generar el prompt |
| `refactorizacion.md` | Antes de empezar el Doc de Refactorización |
| `excel_carga_contactos.md` | Antes de generar el Excel/Sheets de carga de leads |
| `cuadros_explicados.md` | Cuando detectes un punto difícil de explicar |
| `docx_xml_fixes.md` | Si el DOCX no renderiza en preview |

Leer SIEMPRE este SKILL.md primero, después el módulo específico según
la fase de trabajo. Nunca leer todos los módulos a la vez (gasto innecesario
de tokens).

---

## REGLA DE ORO

**Methodology first, then improvements.** Si vas a proponer un cambio a la
metodología, primero ejecutá la metodología completa, después proponé.
Nunca improvises antes de dominar.

**Shortest path principle.** Si la skill ya tiene la respuesta, usala. Si
existe un módulo específico, leelo. No regeneres lógica que ya está codificada.

**Una frase puede tocar múltiples piezas.** Una sola respuesta del cliente
puede afectar Variable + Smart Tag + KPI + funnel + contenido del prompt.
Antes de generar, mapear esa frase contra todas las piezas.
