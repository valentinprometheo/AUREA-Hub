# Reglas revisadas — historial de cambios al archivo oficial

> **Documento de historial.** Lista cada regla de `03-reglas-diseno-prometheo-by-aurea.md`
> que se modificó como consecuencia del modelo nuevo de Embudos/Tags/Variables. Las 4
> propuestas fueron aprobadas y aplicadas al archivo oficial en v1.11.
>
> Este documento se conserva para trazabilidad: qué cambió, por qué, contra qué texto viejo.
> Si en el futuro aparecen nuevas propuestas de cambio a reglas, este archivo es el modelo
> a seguir (texto viejo / nuevo / motivo) y nuevas propuestas arrancan con estado
> `PENDIENTE DE APROBACIÓN`.

---

## Cambios aplicados en v1.11

| Propuesta | Regla afectada | Estado |
|---|---|---|
| 1 | Regla 1 + Regla 2 (las dos cambian — la 1 al modelo estadío+tipología, la 2 deja de fijar tags universales) | ✅ APROBADA Y APLICADA |
| 2 | Regla 3 (acciones por tag, contempla etapa = tag) | ✅ APROBADA Y APLICADA |
| 3 | Regla 6 (placeholders sí soportados vía plantilla) | ✅ APROBADA Y APLICADA |
| 4 | Reglas 8/9/10 (alinear vocabulario embudo + estadío en tag) | ✅ APROBADA Y APLICADA |

---

---

## Resumen — qué cambia y qué no

Tras revisar las 20 reglas del archivo oficial contra el modelo nuevo:

- **Cambian de fondo:** Regla 1, Regla 6.
- **Reescritura menor (el principio sobrevive):** Regla 3.
- **Ajuste cosmético opcional:** Reglas 8, 9, 10 — usan "embudo" de forma compatible con el
  modelo nuevo, solo conviene alinear el vocabulario.
- **No se tocan:** el resto, incluida la Regla 4 (ya dice lo correcto sobre AND nativo y no
  menciona Make/Zapier).
- **El sesgo "menos tags = mejor"** no existe como regla numerada. Su único vehículo era la
  Regla 1 — al caerse esa, el sesgo desaparece solo. No hay nada que reescribir, solo
  verificar que ninguna regla nueva lo reintroduzca.

---

## PROPUESTA 1 — Regla 1: "1 sola Smart Tag activa por conversación"

**Estado:** APROBADA Y APLICADA — v1.11
**Tipo de cambio:** la regla se cae / se reemplaza.

### Texto viejo

> **Regla 1 — 1 sola Smart Tag activa por conversación.** En cualquier momento de una
> conversación existe exactamente 1 Smart Tag activa, no 2 ni 0. Si aparece una nueva, la
> anterior se retira automáticamente. Razón: Prometheo opera con un modelo de "estado
> actual del lead" basado en la tag vigente. [...] El diseñador del prompt debe pensar en
> las transiciones entre tags como una máquina de estados finita.

### Por qué cambia

El modelo nuevo confirmó que esta regla es **falsa a nivel plataforma**: una conversación
puede tener varias Smart Tags a la vez, y Chats las muestra todas al hacer hover. El
"estado actual del lead" no lo lleva la tag vigente — lo lleva la **etapa del embudo** (que
sí es excluyente) y las **variables**. La tag no es una máquina de estados; es una etiqueta
de visibilidad y/o un disparador de acción.

### Texto nuevo propuesto

> **Regla 1 — El estado del lead lo lleva el embudo, no la tag.** Una conversación puede
> tener varias Smart Tags a la vez. La posición del lead en el proceso comercial la define
> la **etapa del embudo** (excluyente: una sola por embudo, ver `embudos-y-tags.md`). Las
> Smart Tags no son una máquina de estados — son etiquetas de visibilidad operativa y/o
> disparadores de acción, y pueden coexistir.
>
> **Implicancia de diseño:** no se diseñan transiciones "retirar la tag anterior al poner
> la nueva". Cada tag se activa cuando su condición se cumple, con independencia de las
> demás. El recorrido del lead se modela en el embudo.

---

## PROPUESTA 2 — Regla 3: "Acciones atadas a la tag, no a tag+variable"

**Estado:** APROBADA Y APLICADA — v1.11
**Tipo de cambio:** reescritura — el principio central se mantiene, pero el modelo nuevo
(etapa de embudo = tag) corrige un matiz que en v1.8 se había planteado mal.

### Texto viejo

> **Regla 3 — Acciones atadas a la tag, no a tag+variable.** Las acciones operativas
> (notificar al comercial, apagar el agente, ejecutar follow-up) se disparan por la tag, no
> por combinaciones de tag con variables. [...]

### Por qué cambia

El principio central es correcto: los ejecutables se cuelgan de **Smart Tags**, no de
combinaciones tag+variable.

Lo que cambia es el matiz sobre el embudo. Una versión previa de esta propuesta agregaba
"las acciones tampoco se cuelgan de etapas de embudo". **Eso es falso** — quedó
desactualizado al verificar en plataforma que una etapa de embudo ES una Smart Tag (ver
`embudos-y-tags.md`). Como la etapa es una tag, una etapa **sí puede disparar ejecutables**.
No hay que prohibirlo: hay que decir que es válido y esperable.

### Texto nuevo propuesto

> **Regla 3 — Acciones atadas a la tag, no a tag+variable.** Las acciones operativas
> (notificar/derivar, apagar el agente, reactivarlo, ejecutar seguimientos) se disparan por
> la **Smart Tag**. No se disparan por combinaciones de tag+variable.
>
> Una etapa de embudo es una Smart Tag (ver `embudos-y-tags.md`): por lo tanto **una etapa
> de embudo puede disparar ejecutables**. Si una acción coincide con un momento del
> recorrido, se cuelga de la propia tag-etapa — no se crea una tag aparte.
>
> **Cómo resolver granularidad:** si necesitás disparar algo bajo una condición compuesta,
> creá una tag más específica, o usá un seguimiento con varias tags (AND nativo, ver
> restricción 5). Las 3 acciones posibles de una tag están en la restricción 9.

---

## PROPUESTA 3 — Regla 6: "Follow-ups con texto literal (sin variables dinámicas)"

**Estado:** APROBADA Y APLICADA — v1.11
**Tipo de cambio:** se invierte la premisa técnica; el default metodológico se revisa.

### Texto viejo

> **Regla 6 — Follow-ups con texto literal (sin variables dinámicas).** Los mensajes de
> follow-up automáticos en Prometheo NO soportan placeholders dinámicos [...]. Default
> metodológico AUREA: texto literal sin variables. [...]

### Por qué cambia

El GitBook confirmó que los seguimientos **sí soportan placeholders**, vía plantilla con
variables mapeadas (ver restricción 12). No se escribe `{nombre}` libre — se crea una
plantilla con variables y se las mapea en la config del seguimiento. La premisa técnica de
la regla vieja ("no soportan placeholders") es falsa.

Las dos estrategias-excepción que la regla vieja documentaba (follow-up como señal interna,
múltiples follow-ups por segmento) **siguen siendo válidas** como recurso — pero dejan de
ser el workaround obligado y pasan a ser opciones de diseño.

### Texto nuevo propuesto

> **Regla 6 — Follow-ups: placeholders vía plantilla con variables.** Los seguimientos de
> Prometheo soportan personalización mediante **plantillas con variables mapeadas** (ver
> restricción 12). No se escribe `{nombre}` libre en el texto: se crea la plantilla con sus
> variables y se las mapea en la configuración del seguimiento.
>
> **Default metodológico AUREA:** usar plantilla con variables cuando la personalización
> aporta (nombre, producto de interés, zona). Mantener el texto sobrio igual — la regla 12
> (saludo breve) sigue vigente.
>
> **Recursos de diseño adicionales** (ya no workarounds obligados): el follow-up como señal
> interna para que el agente arme el mensaje en runtime; o múltiples follow-ups por
> segmento. Se eligen según el caso.

---

## PROPUESTA 4 (opcional) — Reglas 8, 9, 10: alinear vocabulario "embudo"

**Estado:** APROBADA Y APLICADA — v1.11
**Tipo de cambio:** cosmético — aclaración de vocabulario, sin cambio de fondo.

### Situación

Las Reglas 8 ("variable router con +1 embudo"), 9 ("variables estado y tema separadas") y
10 ("funnel de 3 niveles") usan la palabra "embudo" de forma informal, como sinónimo de
"proceso comercial". El modelo nuevo convierte "Embudo" en una **entidad formal de
plataforma**. Las tres reglas **siguen siendo correctas** — no se contradicen con el modelo
nuevo — pero conviene que cada una aclare, con una línea, que "embudo" se usa en el sentido
de la entidad definida en `embudos-y-tags.md`, para que no haya ambigüedad.

### Propuesta

Agregar a las Reglas 8, 9 y 10 una nota corta del tipo: *"'Embudo' refiere a la entidad de
plataforma definida en `embudos-y-tags.md`."* Sin tocar el cuerpo de las reglas.

> Esta propuesta es opcional. Si Valentín prefiere no tocar reglas que funcionan, se
> rechaza sin costo — el `embudos-y-tags.md` ya fija el vocabulario y alcanza.

---

## Registro de decisiones

| Propuesta | Decisión | Fecha | Nota |
|---|---|---|---|
| 1 — Regla 1 | _pendiente_ | | |
| 2 — Regla 3 | _pendiente_ | | |
| 3 — Regla 6 | _pendiente_ | | |
| 4 — Reglas 8/9/10 | _pendiente_ | | |
