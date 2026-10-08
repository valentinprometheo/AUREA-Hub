# 03 — Reglas Diseño de Prometheo by AUREA

**Las 24 reglas inviolables del diseño AUREA × Prometheo.**

Validado con el bot oficial de Prometheo + feedback técnico de soporte. Aplica a TODOS los clientes.

---

## Qué son las Reglas Diseño de Prometheo by AUREA

Son las reglas con las que AUREA Hub diseña agentes IA en Prometheo. Surgen después de validar comportamientos reales con el bot oficial y con casos productivos. La versión actual evolucionó de iteraciones anteriores hasta consolidarse en estas 24 reglas — el changelog detallado vive al final del archivo.

**Estas reglas no son recomendaciones. Son innegociables.** Violarlas produce:
- Agentes que no funcionan como esperado
- DOCX cliente-facing que confunden al cliente
- Configuraciones en Prometheo que fallan en producción
- Decisiones que el bot oficial de Prometheo no soporta
- Integraciones con catálogo (PrestaShop, Tokko, etc.) que se rompen en silencio

---

## Vista resumen — las 24 reglas en 4 bloques

### Bloque 1 — Smart Tags y variables (Reglas 1-10)

Modelado de datos en Prometheo. Define cómo se estructuran las etiquetas y campos que el agente usa para tomar decisiones operativas.

| # | Regla | Qué dice |
|---|---|---|
| 1 | 1 sola Smart Tag activa por conversación | En cualquier momento existe exactamente 1 tag activa, no 2 ni 0. Si aparece una nueva, la anterior se retira. |
| 2 | Tags base obligatorias | Todo cliente tiene mínimo 2 tags: `#seguimiento_activo` (habilita follow-ups) y `#derivar_a_humano` (apaga al agente). |
| 3 | Acciones atadas a la tag, no a tag+variable | Las acciones operativas (notificar, apagar agente) se disparan por la tag, no por combinaciones de tag con variables. |
| 4 | Seguimientos avanzados con AND nativo | Prometheo soporta nativamente lógica AND (tag + variable + tiempo). No hace falta Make ni Zapier para esto. |
| 5 | Variables condicionales en extracción | El prompt de extracción de una variable puede tener condiciones (extraer solo si X). Se documenta dentro del prompt de la variable. |
| 6 | Follow-ups con texto literal (sin variables dinámicas) | Los mensajes de follow-up NO soportan placeholders dinámicos (`{nombre}`, `{producto}`). **Default metodológico: texto literal sin variables.** Si el caso requiere personalización profunda, hay 2 excepciones documentadas (ver detalle de Regla 6 abajo). |
| 7 | No hay base de conocimiento separada | Todo lo crítico vive hardcoded en el prompt. Prometheo no tiene RAG nativo. Si hay catálogo dinámico, se conecta vía integración (ver Bloque 4). |
| 8 | Variable router obligatoria con +1 embudo | Si el agente maneja 2+ embudos comerciales, debe existir una variable router (`proceso_actual`, `tipo_consulta`) que define cuál está activo. |
| 9 | Variables estado y tema separadas | Una variable guarda *estado* del lead (calificando, cotizando, derivado), otra guarda *tema* (qué producto, qué zona). Nunca se mezclan en un solo campo. |
| 10 | Funnel de 3 niveles | El funnel se modela en 3 niveles separados: estado del lead, estado de la oportunidad, estado del producto/proyecto. Nunca se mezclan ni se intercambian. |

### Bloque 2 — Comunicación y tono (Reglas 11-14)

UX conversacional. Define cómo el agente le habla al lead y cómo se ve la información en pantalla.

| # | Regla | Qué dice |
|---|---|---|
| 11 | Calificar antes de derivar | El agente nunca deriva en frío. Antes de pasarle un lead a un humano, captura mínimo: tipo de derivación + **prioridad** + resumen del caso en 1 frase. |
| 12 | Saludo breve en follow-ups | Los mensajes de follow-up no se presentan ("Hola, soy X"). El agente retoma directo desde donde quedó la conversación. |
| 13 | Convención de nombres internos | Variables, tags, claves internas se nombran en minúsculas con guión bajo (`tipo_usuario`, `#derivar_a_humano`). Sin espacios, sin mayúsculas iniciales, sin acentos, sin caracteres especiales. |
| 14 | Color por proceso (convención visual) | En los gráficos del DOCX: verde=venta, **naranja=soporte**, azul=FAQ, morado=seguridad, gris=postventa, **rojo=urgencia/alerta**. Sin excepciones por capricho del cliente. |

### Bloque 3 — Operativa de diseño (Reglas 15-18)

Proceso AUREA. Define cómo se construye el entregable y qué se verifica antes de diseñar.

| # | Regla | Qué dice |
|---|---|---|
| 15 | MVP primero, complejidad después | Cada feature se evalúa contra el MVP. Si no es crítica para Go-Live, va a Fase 2. Mejor lanzar con poco bien hecho que tarde con todo. |
| 16 | Emoji real en prompt vs (emoji de saludo) en DOCX | En el DOCX cliente-facing, el placeholder es `(emoji de saludo)` para que el cliente decida. En el prompt de producción, va el emoji real elegido. |
| 17 | Verificar el Plan Prometheo antes de diseñar | Antes de diseñar, verificar el plan contratado (Base / Pro / Enterprise). No se diseña lo que el plan no soporta. |
| 18 | Precios: nunca asumir que el agente puede darlos | El agente no da precios por defecto. Se releva explícitamente en Discovery y se documenta como [PUEDE] / [NO PUEDE] / [RANGOS]. |

### Bloque 4 — Integración con catálogo digital (Reglas 19-24)

Arquitectura de tools. Aplica a clientes con catálogo externo (PrestaShop, Tokko, ficha.info, Bejerman, e-commerce propio). Cubre ~90% de los clientes AUREA.

| # | Regla | Qué dice |
|---|---|---|
| 19 | Calificación no bloquea consultas atómicas | Aunque el lead no esté calificado, el agente puede responder precio, link y ficha técnica. La calificación solo es obligatoria para cotización, derivación y cross-sell. |
| 20 | Búsqueda de producto ≠ Consulta de precio | Son 3 tools separados: `[BUSCAR_PRODUCTO]` → `[CONSULTA_PRECIO]` → `[OBTENER_LINK]`. Nunca colapsados en uno solo. |
| 21 | Match de producto tolerante | La búsqueda acepta nombres imperfectos, sinónimos, variantes ortográficas. Si no hay match, el agente NO asume que el producto no existe — pide captura o link. |
| 22 | URLs devueltas por la integración son válidas | URLs de la API (PrestaShop, Tokko) son canónicas por definición. URLs estáticas fuera del catálogo principal (videos, fichas PDF, materiales de marketing) NO van hardcoded en el prompt — viven en una fuente externa de acceso compartido (Drive, YouTube, Vimeo, Notion, Dropbox, Sheets, o equivalente) que el cliente elige según su workflow. |
| 23 | Naming unificado | Cada producto tiene una `clave_interna` única. La tabla de equivalencias tiene **3 columnas separadas**: clave_interna oficial, variantes técnicas del cliente, variantes que usa el lead final. |
| 24 | Prioridad explícita de respuesta | El prompt declara: 1° responder directo (hardcoded), 2° consultar integración (dinámico), 3° derivar a humano (todo lo demás). |

---

# Detalle de las 24 reglas

A continuación, el desarrollo extenso de cada regla con ejemplos, razones y casos de aplicación.

## Bloque 1 — Smart Tags y variables

### Regla 1 — Una Smart Tag por dimensión

Un lead puede llevar varias Smart Tags al mismo tiempo, pero **solo una por cada dimensión**. Una dimensión es una pregunta sobre el lead cuyas respuestas son mutuamente excluyentes entre sí.

**Dimensiones canónicas hoy:**

| Dimensión | Pregunta | Mutuamente excluyentes |
|---|---|---|
| **Estadío** | ¿En qué etapa del proceso está? | Sí — el lead está en una sola etapa de cada embudo |
| **Tipo de usuario** | ¿Qué clase de contacto es? | Sí — ej. Inversor / Cliente final / Inmobiliaria |
| **Prioridad** *(opcional)* | ¿Es prioritario? | Sí — se asigna o no (Contacto VIP) |

**Lectura típica de un lead:** 2 tags visibles (estadío + tipo de usuario). Si aplica, 3 (sumando prioridad).

**Razón:** el panel de Chats muestra las tags al hover. Dos tags del **mismo cajón** rompen la legibilidad (no se sabe en qué columna contar el lead). Tags de **dimensiones distintas** coexisten sin problema porque cada una responde una pregunta distinta.

**Implementación:**
- Las etapas de embudo SON Smart Tags (la dimensión estadío vive en el embudo).
- La tag de tipo de usuario se deriva de una variable (ej. `var_objetivo_busqueda`).
- Las dimensiones nuevas se admiten si no se superponen con las existentes.
- No diseñar tags con alta similitud semántica — el equipo las confunde.

**Modelo desarrollado:** ver `embudos-y-tags.md` para el modelo completo, las sub-reglas operativas y la corrección conceptual (FAQ y Excepciones no son embudos).

### Regla 2 — Tags operativas mínimas del agente

Todo agente tiene como mínimo las **tags de estadío** del embudo principal (al menos una de inicio del recorrido y una de derivación a humano). Los nombres concretos se definen por cliente según el modelo de embudos diseñado.

**Razón:** sin tags de estadío, el embudo no puede operar y el agente no puede entregar leads al equipo humano. Son el mínimo para que el ciclo conversación → seguimiento → derivación funcione.

**Naming:** siempre con `#` adelante, snake_case, en español. Los nombres se eligen pensando en cómo se leen en el panel de Chats (ver Regla 1 — no similitud semántica).

> **Nota histórica:** versiones anteriores de esta regla fijaban tags universales (`#seguimiento_activo` + `#derivar_a_humano`). Ese modelo lo usó MIA App como caso temprano. El modelo vigente, validado con G&D Developers y la implementación AUREA, deja los nombres concretos de tags al diseño de cada cliente y le pide solo el mínimo funcional (estadío del embudo).

### Regla 3 — Acciones atadas a la tag, no a tag+variable

Las acciones operativas (notificar/derivar, apagar el agente, reactivarlo, ejecutar seguimientos) se disparan por la **Smart Tag**. No se disparan por combinaciones de tag+variable.

Una etapa de embudo **es** una Smart Tag (ver `embudos-y-tags.md`): por lo tanto **una etapa de embudo puede disparar ejecutables**. Si una acción coincide con un momento del recorrido, se cuelga de la propia tag-etapa — no se crea una tag aparte.

**Razón:** Prometheo enlaza acciones a tags, no a estados compuestos. Y como la etapa es tag, no hay separación artificial "etapa vs tag operativa".

**Cómo resolver granularidad:** si necesitás disparar algo bajo una condición compuesta, creá una tag más específica, o usá un seguimiento con varias tags (AND nativo — ver Regla 4 y restricción 5 en `restricciones-plataforma-prometheo.md`). Las 3 acciones posibles de una tag están en la restricción 9.

### Regla 4 — Seguimientos avanzados con AND nativo

Prometheo SÍ soporta nativamente lógica AND para disparar follow-ups: tag + variable + tiempo.

**Ejemplo:** "Disparar follow-up si `#seguimiento_activo` AND `estado_venta_material = cotizacion_orientativa_enviada` AND `+24hs sin respuesta`".

**Razón:** no hace falta Make, Zapier ni integración externa para esto. Está dentro de Prometheo.

### Regla 5 — Variables condicionales en extracción

El prompt de extracción de una variable puede tener condiciones lógicas. La variable solo se actualiza si se cumple la condición declarada.

**Ejemplo:** `tipo_inmueble` solo se extrae si `tipo_obra = reforma`. En obra nueva, esa variable no aplica y queda vacía.

**Implementación:** la condición se documenta dentro del prompt de la variable, no como regla externa.

### Regla 6 — Follow-ups: placeholders vía plantilla con variables

Los seguimientos de Prometheo **SÍ soportan personalización** mediante **plantillas con variables mapeadas** (ver restricción 12 en `restricciones-plataforma-prometheo.md`). No se escribe `{nombre}` libre en el texto: se crea la plantilla con sus variables y se las mapea en la configuración del seguimiento.

**Default metodológico AUREA:** usar plantilla con variables cuando la personalización aporta valor real (nombre, producto de interés, zona). Mantener el texto sobrio igual — la Regla 12 (saludo breve) sigue vigente.

**Recursos de diseño adicionales** (ya no workarounds obligados):

| Estrategia | Cuándo usarla |
|---|---|
| **Plantilla con variables mapeadas** | Default. Personalización directa en el follow-up. |
| **Follow-up como señal interna al agente** | El follow-up dispara al agente para retomar la conversación; el agente arma el mensaje en runtime. Se usa cuando hace falta personalización profunda que la plantilla no cubre. |
| **Múltiples follow-ups por segmento** | En vez de 1 follow-up genérico, N follow-ups distintos (uno por segmento) y se dispara el que corresponde por tag/variable. Se usa cuando hay 3-5 segmentos claros con mensajes muy distintos. |

**Por qué importa:** versiones anteriores de esta regla decían que los follow-ups NO soportaban placeholders. El GitBook oficial confirmó que sí los soportan vía plantilla mapeada.

### Regla 7 — No hay base de conocimiento separada

Prometheo no tiene RAG nativo (Retrieval Augmented Generation). Todo lo crítico para el agente vive hardcoded en el prompt.

**Excepción:** si hay catálogo dinámico (productos, propiedades, unidades), se conecta vía integración externa (PrestaShop, Tokko, ficha.info). Ver Bloque 4.

**Razón:** esto obliga a que el prompt sea autocontenido. FAQs, reglas de negocio, lógica de recomendación: todo debe estar escrito explícitamente en el prompt.

### Regla 8 — Variable router obligatoria con +1 embudo

Si el agente maneja 2 o más embudos comerciales (ej: venta_material vs venta_obra vs postventa), debe existir una **variable router** que define cuál está activo en cada momento.

**Naming típico:** `proceso_actual`, `tipo_consulta`, `embudo_activo`.

**Por qué:** sin esta variable, las reglas de follow-up y las acciones del agente no saben en qué contexto operan.

> "Embudo" refiere a la entidad de plataforma definida en `embudos-y-tags.md` (conjunto ordenado de tags-etapa).

### Regla 9 — Variables estado y tema separadas

Una variable guarda el **estado** del lead en un proceso (calificando, cotizando, derivado, perdido). Otra variable guarda el **tema** (qué producto consulta, qué zona, qué proyecto).

**Nunca se mezclan en un solo campo.**

**Razón:** el estado y el tema cambian de forma independiente. Mezclarlos rompe la trazabilidad y dificulta las reglas de follow-up.

**Ejemplo correcto:**
- `var_estado_venta = cotizacion_orientativa_enviada`
- `var_producto_de_interes = MicroCemento`

**Ejemplo INCORRECTO:**
- `var_estado = cotizando_microcemento` (mezcla estado con tema)

> **Importante — actualización v1.11:** el **estadío principal** del lead (la etapa del embudo donde está) **NO va en variable**: es una tag (ver Regla 1 y `embudos-y-tags.md`). Las variables de estado que esta regla contempla son **estados auxiliares o complementarios** del proceso, no la posición del lead en el embudo. Los nombres `proceso_actual` / `estado_*` como variables de estadío quedan obsoletos.

### Regla 10 — Funnel de 3 niveles

El funnel del CRM se modela en **3 niveles separados** que nunca se mezclan ni se intercambian:

| Nivel | Qué describe | Ejemplo de estados |
|---|---|---|
| **Estado del lead** | La persona/contacto | nuevo, en conversación, calificado, derivado, perdido |
| **Estado de la oportunidad** | El negocio potencial | consulta inicial, cotización enviada, en negociación, ganada, caída |
| **Estado del producto/proyecto** | El item específico de interés | disponible, reservado, en pausa, agotado |

**Razón:** los 3 niveles avanzan de forma independiente. Un lead puede estar "calificado" mientras su oportunidad está en "cotización enviada" y el producto que le interesa está "disponible". Mezclar los 3 en un solo campo de estado destruye la trazabilidad y hace imposible diseñar reglas de follow-up precisas.

**Aplicación práctica:** el **estado del lead principal** vive como **tag de estadío** (regla 1 + `embudos-y-tags.md`). Los estados auxiliares (oportunidad, producto) viven como variables. El nivel "producto/proyecto" suele venir del catálogo externo (Tokko, PrestaShop) — ver Bloque 4.

---

## Bloque 2 — Comunicación y tono

### Regla 11 — Calificar antes de derivar

El agente nunca deriva en frío al equipo humano. Antes de pasarle un lead a un comercial, captura como mínimo 3 datos:

1. **Tipo de derivación** (`tipo_derivacion`): qué tipo de caso es (cotización, postventa, B2B, administrativa, etc.)
2. **Prioridad** (`prioridad`): alta, media o baja
3. **Resumen del caso** en 1 frase

**Razón:** el comercial humano recibe el caso ya contextualizado. No tiene que reconstruir la conversación desde cero.

**Nota:** la variable se llama **prioridad** (en español, claro), no "severidad" ni "urgencia".

### Regla 12 — Saludo breve en follow-ups

Los mensajes de follow-up automáticos no se presentan ("Hola, soy X, asistente de Y"). El agente retoma directo desde donde quedó la conversación.

**Ejemplo correcto:** "Hola, te quería retomar la consulta sobre la POSITANO. ¿Avanzamos?"

**Ejemplo INCORRECTO:** "Hola, soy Catalina de BETROX. Te quería retomar la consulta sobre la POSITANO..."

**Razón:** repetir la presentación en cada follow-up suena robótico y delata que es un mensaje automático.

### Regla 13 — Convención de nombres internos

Variables, tags y claves internas se nombran siguiendo estas reglas:

- **Minúsculas** (sin mayúsculas iniciales)
- **Separadas por guión bajo** (no espacios, no guión medio)
- **Sin acentos** (`tipo_usuario`, no `tipo_usuário`)
- **Sin caracteres especiales** (no `&`, no `/`, no `()`)
- **En español** cuando se trata de la lógica del negocio del cliente

**Ejemplos correctos:** `tipo_usuario`, `#derivar_a_humano`, `proceso_actual`, `m2_superficie`.

**Ejemplos INCORRECTOS:** `TipoUsuario`, `tipo-usuario`, `tipo usuario`, `#DerivarAHumano`.

**Razón:** consistencia visual y técnica. Facilita debugging y mantenimiento del prompt.

### Regla 14 — Color por proceso (convención visual)

En los gráficos del DOCX cliente-facing, cada proceso comercial tiene un color asignado. **Sin excepciones por capricho del cliente.**

| Proceso | Color | Hex |
|---|---|---|
| Venta | Verde | #4CAF80 |
| Soporte | **Naranja** | #E8943A |
| FAQ | Azul | #5B8FD9 |
| Seguridad | Morado | #7C5CBF |
| Postventa | Gris | #7A7A7A |
| **Urgencia / alerta** | **Rojo** | #E84545 |

**Cambio respecto a versiones anteriores:** el rojo dejó de representar "soporte" y pasó a representar "urgencia/alerta". Soporte ahora es naranja.

**Razón:** rojo es un color de alarma/criticidad en convenciones internacionales. Soporte es un proceso normal del negocio, no una emergencia. Naranja es el color correcto.

---

## Bloque 3 — Operativa de diseño

### Regla 15 — MVP primero, complejidad después

Cada feature propuesta se evalúa contra el MVP (Producto Mínimo Viable). Si no es crítica para el Go-Live, va a Fase 2.

**Criterio de evaluación:**
- ¿El agente puede funcionar sin esta feature en Go-Live? → Si la respuesta es sí, va a Fase 2.
- ¿El cliente puede operar sin esta feature en Go-Live? → Si la respuesta es sí, va a Fase 2.
- ¿Hay riesgo de que la feature rompa otras cosas en MVP? → Va a Fase 2.

**Razón:** mejor lanzar con poco bien hecho que tarde con todo. Los clientes prefieren un agente operativo en 4 semanas que uno "perfecto" en 6 meses.

### Regla 16 — Emoji real en prompt vs (emoji de saludo) en DOCX

En el DOCX cliente-facing, el placeholder es `(emoji de saludo)` o similar — el cliente decide qué emoji prefiere.

En el prompt de producción, va el emoji real elegido (ej: 👋, ☀️, 🙂) o sin emoji si el cliente prefiere.

**Razón:** el DOCX es para que el cliente apruebe el diseño. Si ponemos un emoji concreto, el cliente puede objetar el emoji en lugar del diseño. El placeholder evita esa fricción.

### Regla 17 — Verificar el Plan Prometheo antes de diseñar

Antes de diseñar cualquier funcionalidad, verificar qué Plan de Prometheo tiene contratado el cliente: **Base**, **Pro** o **Enterprise**. No se diseña lo que el plan no soporta.

| Plan | Qué habilita |
|---|---|
| **Base** | Asistente IA + CRM |
| **Pro** | + notificaciones y derivaciones |
| **Enterprise** | + campañas masivas, TikTok, comentarios de Instagram |

**Razón:** diseñar derivaciones automáticas para un cliente con Plan Base, o campañas masivas para un Plan Pro, genera un diseño imposible de implementar. El cliente aprueba algo que después no se puede cargar. La verificación del plan es un check previo obligatorio en la Etapa 2.

**Aplicación práctica:** si el diseño ideal requiere un plan superior al contratado, se marca como [FASE 2 — requiere upgrade de plan] y se le explica al cliente la diferencia.

### Regla 18 — Precios: nunca asumir que el agente puede darlos

El agente **no da precios por defecto**. Que pueda o no darlos es una decisión explícita que se releva en Discovery (bloque B8 — Autonomía) y se documenta como una de tres opciones:

| Marcado | Significado |
|---|---|
| **[PUEDE]** | El agente da el precio directamente |
| **[NO PUEDE]** | El agente nunca da precio, deriva o pide datos |
| **[RANGOS]** | El agente da un rango o un "desde", nunca el precio cerrado |

**Razón:** el precio es la decisión más sensible del diseño. Asumir que el agente puede darlo cuando el cliente no lo autorizó genera conflictos comerciales graves (precios desactualizados, descuentos no autorizados, competencia que ve la lista). Asumir que NO puede cuando sí podía hace al agente inútil. Siempre se pregunta explícitamente y se documenta por escrito.

**Conexión:** esta regla se cruza con el Bloque 4 (integración con catálogo). Si el precio vive en un sistema externo actualizado (PrestaShop, Tokko), el agente puede leerlo de ahí — pero igual hay que confirmar que está autorizado a comunicarlo.

---

## Bloque 4 — Integración con catálogo digital

Las 6 reglas siguientes aplican a todo cliente cuyo prompt tenga integración con catálogo externo (PrestaShop, Tokko, Bejerman, ficha.info, e-commerce propio). El detalle completo de cada regla con ejemplos está en `08-reglas-integracion-catalogo.md`. Acá la versión integrada a las Reglas Diseño de Prometheo by AUREA.

### Regla 19 — Calificación no bloquea consultas atómicas

Aunque `tipo_usuario = desconocido`, el agente debe responder consultas atómicas de producto: precio, link, ficha técnica, disponibilidad. La calificación es prioritaria para flujos comerciales (cotización, derivación, cross-sell), pero no para preguntas concretas.

**Frase típica de prompt mal escrito (evitar):**
> "NO podés cotizar [...] sin saber tipo_usuario."

**Frase de reemplazo correcta:**
> "Aunque tipo_usuario sea 'desconocido', el agente PUEDE responder consultas atómicas de producto. La calificación es prioritaria solo para flujos comerciales (cotización, derivación, cross-sell)."

**Razón:** prompts mal escritos bloquean preguntas simples ("¿cuánto sale la POSITANO 1.60?") esperando que el lead se identifique primero. Eso rompe la conversación.

### Regla 20 — Búsqueda de producto ≠ Consulta de precio

Son 3 operaciones distintas con tools distintos. El prompt debe declararlas como pasos separados:

```
Paso 1 — Resolver producto:
[BUSCAR_PRODUCTO: NOMBRE_REFERIDO_POR_EL_CLIENTE]

Paso 2 — Si el producto fue identificado, consultar precio:
[CONSULTA_PRECIO: CLAVE_INTERNA_MODELO, MEDIDA]

Paso 3 — Si la integración devuelve URL, usarla en la respuesta:
[OBTENER_LINK: CLAVE_INTERNA_MODELO]
```

**Razón:** si el prompt solo tiene "consultar precio", el agente falla cuando el lead nombra un producto de forma imperfecta. Necesita primero resolver el producto (búsqueda tolerante), recién después consultar precio.

### Regla 21 — Match de producto tolerante

La búsqueda de producto acepta nombres imperfectos, sinónimos, variantes ortográficas, y referencias parciales.

Si la integración devuelve 0 resultados:
1. El agente NO asume que el producto no existe
2. Pide captura, link, o más contexto al lead
3. Si persiste el match en blanco, deriva al comercial

**Frase prohibida:** "Ese producto no existe en mi catálogo."
**Frase de reemplazo:** "Ese nombre no me figura con esa denominación exacta. ¿Puede ser que lo hayas visto con otro nombre? Si me pasás captura o link, lo identifico al toque."

### Regla 22 — URLs devueltas por la integración son válidas

Distinguir 3 categorías de URLs:

| Tipo de URL | Comportamiento |
|---|---|
| **URLs devueltas por la integración** (`[OBTENER_LINK: CLAVE_INTERNA]`) | Siempre válidas. Se comparten directamente. |
| **URLs inventadas por el agente** (construidas desde el nombre del producto) | Siempre prohibidas. |
| **URLs estáticas fuera del catálogo principal** (videos de aplicación o explicativos, fichas PDF que no están en e-commerce, materiales de comunicación) | NO van hardcoded en el prompt. Viven en una fuente externa de acceso compartido (Google Drive, YouTube, Vimeo, Notion, Dropbox, Google Sheets, o equivalente) porque cambian dinámicamente. La fuente la elige el cliente según su workflow. |

**Paso de descubrimiento obligatorio en Etapa 2:** durante el diseño del prompt, AUREA pregunta al cliente:

1. *"¿Dónde tenés documentada la base de datos del catálogo principal?"* (sistema integrable como PrestaShop o Tokko, Google Sheets, planillas locales, etc.)
2. *"¿Hay URLs que el agente vaya a necesitar compartir y que no estén en la integración principal?"* — caso típico: videos de aplicación o explicativos, fichas técnicas PDF que viven aparte del e-commerce, materiales de marketing.
3. *"¿En qué fuente externa querés tener esos URLs?"* — el cliente elige (Google Drive, YouTube, Vimeo, Notion, Dropbox, Google Sheets, etc.) según su workflow.

Las URLs secundarias detectadas en esos pasos NO se ponen en el prompt como placeholders. Se documentan en la **fuente externa de acceso compartido** que el cliente eligió, para poder actualizarlas sin tocar el prompt.

**Razón:** los URLs externos cambian con frecuencia (videos se reemplazan, PDFs se actualizan). Hardcodearlos en el prompt obliga a tocar el prompt cada vez que se actualizan, lo que es costoso operativamente.

### Regla 23 — Naming unificado

Cada producto tiene UNA clave interna única que se usa en toda la cadena de tools. Las variantes (técnicas y del lead final) mapean a esa clave.

**Tabla de equivalencias con 3 columnas separadas:**

| Columna | Qué contiene | Quién la mantiene | Cuándo se completa |
|---|---|---|---|
| **clave_interna** | El nombre técnico único oficial. Ejemplo: `POSITANO_1.60` | Consultor AUREA (con criterio + auditoría web del cliente) | Etapa 2 inicial |
| **variantes_tecnicas** | SKU, nombre comercial, nombre en sistema fuente del cliente. Ejemplo: `SKU-MP-POS-160`, `"POSITANO 1.60m"` | Cliente (es info de su catálogo) | Etapa 2 inicial, validada con cliente |
| **variantes_lead** | Cómo lo escribe un lead que no conoce el producto. Ejemplo: `"positano"`, `"la grande"`, `"mesa redonda esa"` | Inicial: consultor con criterio. Iterativo: se completa post Go-Live con conversaciones reales | Etapa 2 (inicial) + Monitoreo (iterativo) |

**Razón para separar las 3 columnas:** las variantes técnicas son **deterministas** (las saca del sistema fuente). Las variantes del lead son **probabilísticas** (nunca sabés cómo va a escribir el lead). Mezclarlas mete ruido en el match tolerante (Regla 21).

**Quién construye:** el naming unificado lo construye el consultor AUREA durante Etapa 2, no el cliente. El cliente valida la columna de variantes técnicas. La columna de variantes del lead se completa iterativamente con datos reales de conversaciones post Go-Live.

**Realismo de la regla:** no siempre va a ser perfecto. El match tolerante (Regla 21) cubre los casos donde el naming no tiene el sinónimo todavía. La tabla se va completando con cada conversación nueva que aporta un sinónimo no contemplado.

### Regla 24 — Prioridad explícita de respuesta

El prompt declara explícitamente, al inicio de la sección de producto/consulta, las 3 prioridades de respuesta en orden:

1. **Respuesta directa** — si el agente tiene la info en su prompt hardcodeado (FAQs, política, regla de combinación)
2. **Consultar integración** — si la info vive en sistema externo (precio, stock, link, ficha técnica)
3. **Derivar a humano** — si nada de lo anterior resuelve

**Razón:** sin esta prioridad explícita, el agente:
- Deriva consultas que podría responder solo (degrada experiencia)
- Inventa respuestas que debería consultar (rompe confianza)
- Consulta integración para info que es hardcoded (latencia innecesaria)

---

## Anti-patrones (lo que NO se hace)

| Anti-patrón | Por qué está mal |
|---|---|
| Múltiples Smart Tags activas a la vez | Rompe Regla 1, genera ambigüedad en follow-ups |
| Variables con espacios en el nombre | Rompe Regla 13, falla en tools |
| Follow-up con `{nombre}` esperando reemplazo | Rompe Regla 6, el lead recibe "{nombre}" literal |
| Calificar al lead antes de responder un precio | Rompe Regla 19, rompe la conversación |
| Inventar URLs desde el nombre del producto | Rompe Regla 22, el lead recibe links rotos |
| Mezclar SKU, nombre comercial y jerga del lead en una sola columna | Rompe Regla 23, hace fallar el match tolerante |
| Decir "ese producto no existe" cuando la búsqueda no encontró match | Rompe Regla 21, el lead se va |

---

## Las 3 capas de variables (regla complementaria a la 8)

Las variables del prompt se organizan en 3 capas según su origen y mantenimiento:

| Capa | Origen | Ejemplos | Mantenimiento |
|---|---|---|---|
| **Núcleo transversal** | Definidas por AUREA, aplican a todos los clientes | `tipo_usuario`, `proceso_actual`, `prioridad` | AUREA (no cambia entre clientes) |
| **Por rubro** | Definidas por AUREA según rubro (real estate, mobiliario, etc.) | `superficie_destino`, `estado_obra`, `tipo_inmueble` (en real estate) | AUREA por rubro (cambia entre rubros) |
| **Del cliente** | Específicas del negocio del cliente concreto | `proyecto_de_interes` (lista de proyectos específicos de ese desarrollista) | Cliente (las completa él en Etapa 1) |

Esta separación facilita el reuso: las capas Núcleo y Rubro se reutilizan entre clientes del mismo rubro. Solo la capa Cliente se construye desde cero.

---

## Nota sobre la UX de Onboarding (proyecto futuro)

Durante el diseño de las Reglas 16-21 surgió una idea más amplia: **diseñar Claude como copiloto sistemático del consultor durante toda la consultoría del cliente nuevo**. El objetivo es que el flujo de discovery (Etapa 1) y diseño (Etapa 2) se ejecute como una conversación guiada con Claude (preguntas con opciones a elegir), no como una redacción solitaria de prompt.

**Alcance mínimo del proyecto futuro:** Etapas 1 + 2 de la metodología AUREA, dejando abierto si abarca también Etapa 3 (Lanzamiento) y Etapa 4 (Mejora Continua) o más.

**Status:** `[futuro / proyecto separado: UX de onboarding etapas 1 + 2 como mínimo]`

No se implementa en esta versión del ZIP. Merece sesiones dedicadas para diseñar: flujo conversacional, skills específicas, project instructions, templates de respuesta, sistema de memoria.

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Operativa de Etapa 2 | `01-operativa-y-decisiones.md` |
| Trazabilidad Etapa 1 → Etapa 2 | `02-trazabilidad-etapa1-etapa2.md` |
| Convenciones del DOCX | `04-convenciones-docx-cliente.md` |
| Reglas de integración con catálogo (detalle de Reglas 16-21) | `08-reglas-integracion-catalogo.md` |
| Paleta y colores | `../07-convenciones-aurea/01-paleta-y-colores.md` |
| Casos de referencia (BETROX, MIA, G&D, EDFAN) | `../08-casos-referencia/` |
