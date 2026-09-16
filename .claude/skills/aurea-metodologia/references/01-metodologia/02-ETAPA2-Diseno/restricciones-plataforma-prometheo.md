---
consultar-cuando: cualquier diseño de CRM, para no asumir comportamiento de Prometheo
disparadores: "restricciones de plataforma", "qué permite Prometheo", "colores de tags", "planes Prometheo"
fuente-única-de: restricciones confirmadas de la plataforma Prometheo
combina-con: embudos-y-tags, 03-reglas-diseno-prometheo-by-aurea, pendientes-itesa
---

# Restricciones de la Plataforma Prometheo

> Las limitaciones técnicas de Prometheo que condicionan el diseño. Tener siempre presente en la Etapa 2.

---

## Por qué importan

Prometheo es una plataforma con reglas propias. Diseñar algo que la plataforma no soporta genera un diseño que el cliente aprueba pero que después no se puede implementar. Estas restricciones son el marco técnico dentro del cual se diseña.

> ⚠️ Ante cualquier decisión de diseño no estándar o controvertida, validar con el bot oficial de Prometheo antes de avanzar. Estas restricciones son la base, pero la plataforma evoluciona.

---

## Las restricciones

> Las restricciones 1-8 son el marco base. Las 9-15 se incorporaron en v1.8 tras la
> investigación del GitBook oficial de Prometheo. Las 16-18 se incorporaron en v1.9 con los
> aprendizajes de la implementación de AUREA Hub como cliente de Prometheo.

### 1. Un solo asistente para todos los canales

Prometheo usa **un único asistente** para WhatsApp, Instagram, Facebook y web. No hay un asistente por canal. Las diferencias de comportamiento entre canales se resuelven con **bifurcaciones internas en el prompt**, no con asistentes separados.

### 2. Los archivos adjuntos NO son base de conocimiento

Los archivos que se cargan en Prometheo se **envían** al lead (con el comando `/`), no se **leen** como fuente de información. Prometheo no tiene RAG nativo. Todo lo que el agente necesita saber va hardcoded en el prompt (ver Regla 7).

### 3. Smart Tags — mini-prompt de 15-25 palabras

Cada Smart Tag se define con un mini-prompt corto, de entre 15 y 25 palabras, con el formato: *"Asigná este tag a las conversaciones donde detectes que [condición]"*.

### 4. Variables — tipos disponibles y prompt opcional

Los tipos de variable que soporta Prometheo son: **Texto**, **Link**, **Número**, **Texto largo**, **Precio** (con moneda) y **Opciones**. Para datos categóricos, preferir siempre **Opciones**; las de tipo Opciones piden además definir si admiten selección múltiple y cargar las opciones una por una.

Cada variable tiene un campo de **prompt opcional**:

- **Con prompt** — la IA completa la variable sola, a partir de la conversación.
- **Sin prompt** — la variable es de **carga manual**: la completa una persona.

Criterio de diseño: si el dato puede aparecer en la conversación, la variable lleva prompt; si es un dato interno que el lead nunca diría, es manual.

### 5. Seguimientos — se disparan por Smart Tag

Cada seguimiento se dispara por Smart Tags. Un seguimiento puede configurarse con **una** tag o con **varias**:

- **Con 1 tag** — el seguimiento se dispara cuando el lead tiene esa tag.
- **Con varias tags** — Prometheo aplica **lógica AND nativa**: el seguimiento se dispara solo cuando el lead tiene **TODAS** las tags configuradas. No es OR.
- **Sin ninguna tag** — un seguimiento puede configurarse para dispararse a leads que no tienen ninguna tag asignada.

> Aclaración importante: que la plataforma soporte varias tags por seguimiento (AND nativo) es un hecho técnico. La **decisión metodológica** de cuántas tags usar por seguimiento es otra cosa y se trata en las Reglas Diseño y en `framework-seguimientos.md`.

### 6. WhatsApp API — ventana de 23 horas

Con WhatsApp API oficial, se puede enviar un mensaje sin plantilla hasta **23 horas** después del último mensaje del lead. Pasado ese tiempo, se requiere una plantilla de Meta aprobada. Con WhatsApp QR no hay esta restricción. Instagram tiene una ventana de 24 horas.

### 7. Planes — Basic / Pro / Enterprise

| Plan | Qué habilita |
|---|---|
| **Basic** | Asistente IA + CRM completo. Canales: WhatsApp, Instagram, WebChat. Pre-calificación y seguimientos. Usuarios y chats ilimitados. Sin integraciones. |
| **Pro** | + 1 integración de marketplace, **Prometheo Connect**, notificaciones y derivaciones, Facebook chat. |
| **Enterprise** | + 2 integraciones de marketplace, campañas de envíos masivos, respuesta a comentarios en redes, Meta Ads, TikTok. |

Prometheo Connect está disponible **desde el plan Pro**. Las integraciones de marketplace son 1 en Pro y 2 en Enterprise. El precio del abono **no incluye** saldos de IA (ver restricción 8).

No se diseña lo que el plan contratado no soporta (ver Regla 17).

### 8. Saldo de IA = tokens

El consumo del asistente se mide en tokens (saldo de IA). Si el saldo llega a cero, **el asistente se detiene**. Hay que tenerlo presente al estimar volumen de conversaciones.

### 9. Smart Tags — las 3 acciones posibles

Una Smart Tag de acción puede disparar **exactamente 3 acciones**, no más:

| Acción | Qué hace | Plan |
|---|---|---|
| **Apagar asistente** | Detiene al agente en esa conversación | Todos |
| **Reactivar asistente** | Vuelve a encender al agente | Todos |
| **Notificación / derivación** | Avisa al equipo humano del caso | **Pro / Enterprise** |

La acción de notificación tiene **sub-opciones**: notificar según una variable, o notificar al moderador asignado a la conversación. Las acciones son de las **tags**, nunca de las etapas de embudo (ver `embudos-y-tags.md`, regla dura 2).

### 10. Seguimientos — repetición nativa

Un seguimiento se **auto-repite de 2 a 5 veces** sin necesidad de crear seguimientos separados. Tiene un **multiplicador de delay** que espacia cada reenvío (cada repetición espera más que la anterior). No hay que clonar el seguimiento para insistir varias veces.

### 11. Seguimientos — franja horaria

Cada seguimiento se configura con una **franja horaria** (desde/hasta hora) y **días permitidos**. Si un envío cae fuera del rango, **no se pierde**: se difiere al próximo rango permitido.

### 12. Seguimientos — placeholders vía plantilla con variables mapeadas

Los seguimientos **SÍ soportan placeholders**, pero no se escriben libres en el texto. El mecanismo es: se crea una **plantilla con variables** y esas variables se **mapean** en la configuración del seguimiento. No se escribe `{nombre}` suelto — se arma la plantilla con sus variables y se las asocia.

> Esto corrige el supuesto histórico de la metodología de que los follow-ups no soportaban personalización. La consecuencia metodológica (qué hacer con la Regla 6) se revisa en `reglas-revisadas-v1.11.md`.

### 13. Seguimientos — adjuntos

Un seguimiento admite hasta **10 archivos adjuntos**, con un máximo de **30 MB**. Formatos: PNG, JPEG, JPG, PDF, video y audio.

### 14. Prometheo Connect — constructor de endpoints API

**Prometheo Connect** es un constructor genérico de endpoints API: permite que el asistente **consulte y cree datos en cualquier sistema externo sin programar**, usando Variables para llenar el body de la request.

Disponible **desde el plan Pro** (ver restricción 7).

> Esto matiza el supuesto de "nunca sugerir Make / Zapier": Connect cubre de forma nativa mucho más de lo que la metodología asumía. **Pendiente fino:** confirmar con ITESA si el uso de Connect consume el cupo de "integración de marketplace" del plan (Pro = 1, Enterprise = 2) o es independiente — ver `pendientes-itesa.md`.

### 15. WhatsApp — dos tipos de conexión

Prometheo se conecta a WhatsApp de dos formas, con capacidades distintas:

| Conexión | Qué habilita | Limitaciones |
|---|---|---|
| **QR** | Sin costo de Meta. Mensajería estándar. | Sin plantillas, sin campañas, sin Meta Ads/Forms. |
| **API oficial** | Plantillas de Meta, campañas masivas, Meta Ads y Forms. | Meta cobra los costos de mensajería aparte. |

El cambio de QR a API (o viceversa) lo hace el **equipo técnico de Prometheo**, no se hace desde la interfaz. La ventana de 23 horas (restricción 6) aplica a la conexión API.

### 16. Match de Smart Tags — distingue tildes, no mayúsculas

Cuando Prometheo compara nombres de tags, el match **no distingue mayúsculas** pero **sí distingue tildes y acentos**. `construcción` y `Construcción` se toman como la misma tag; `construccion` sin tilde es **otra tag distinta**.

Esto importa sobre todo en la importación de contactos por Excel (ver restricción 17 y `importacion-contactos.md`): una tilde de diferencia hace que la tag no matchee.

### 17. Importación de contactos — las tags desconocidas se ignoran en silencio

En la importación de contactos por Excel, si el archivo trae una tag que **no existe** ya creada en la organización, Prometheo **no la crea ni da error**: simplemente no la asigna, y el contacto entra sin esa tag.

Es un fallo silencioso: no hay aviso. Por eso, antes de importar, hay que verificar que **todas** las tags del archivo existan ya creadas y escritas de forma idéntica (tildes incluidas). Procedimiento completo en `importacion-contactos.md`.

### 18. Variables — deben existir antes de importar

La importación de contactos solo permite **mapear una columna a una variable que ya exista** en Prometheo. Las variables tienen que estar creadas antes de preparar el Excel. En la plantilla de importación, las columnas de variable llevan el prefijo `var_` (ej. `var_empresa`, `var_prioridad`). Detalle en `importacion-contactos.md`.

### 19. Colores de Smart Tags — solo 6 disponibles, se repiten entre dimensiones

Prometheo ofrece exactamente **6 colores** para Smart Tags: Azul, Lila, Rosa, Durazno, Amarillo,
Verde. Con más de 6 dimensiones/etapas en un CRM (lo normal: estadío + tipología + prioridad,
multiplicado por 3 embudos), los colores se **repiten** entre dimensiones. Esto es esperado, no un
error de diseño: la dimensión se distingue por el **nombre** de la tag, no por su color. Criterio
de asignación reutilizable confirmado en BETROX: amarillo para entrada/instalador, azul para
activo, verde para positivo/ganado, lila para reunión/institucional, durazno para
handoff/profesional, rosa para cierre negativo/hot lead.

### 20. Acciones de Smart Tag — solo 3, y una de ellas requiere plan Enterprise

Las acciones disponibles sobre una Smart Tag son exactamente **3**: Apagar Asistente,
Notificaciones, Reactivar Asistente. **Notificaciones requiere plan Enterprise** (confirmado en
BETROX, donde el plan se contrató explícitamente por esta razón, además de por PrestaShop y
agendamiento). Antes de diseñar un CRM que dependa de avisos automáticos al equipo, confirmar el
plan del cliente.

### 21. Descripción de Embudo — campo que la IA lee para decidir asignación de tags

Cada Embudo se crea con un campo **Descripción** que el agente lee para decidir cuándo asignar las
tags de ese embudo. No es documentación decorativa: es una instrucción que el modelo consulta en
runtime. Al diseñar un embudo nuevo, la Descripción se redacta como instrucción operativa para la
IA (qué cubre el embudo, qué tipo de lead entra, cuándo salta a otro embudo), no como resumen para
humanos. Confirmado como patrón de diseño en BETROX; aplicable a cualquier cliente con más de un
embudo.

### 22. Refresco de integración destructivo (Sheets)

Modificar la estructura de un Google Sheet ya conectado (ej. dar de alta una columna nueva) no
permite refrescar conservando la configuración: obliga a **reconfigurar todas las hojas y columnas
de cero** (en G&D, 6 hojas y 66 columnas). Consecuencia de diseño: minimizar cambios de esquema,
**agregar columnas siempre al final** (nunca intercalar), versionar el esquema y planificar los
cambios en tandas. Confirmado en G&D; registrado como incidente imputable. Límite no documentado
por ITESA (ver pendientes).

### 23. Filtrado por estado no siempre confiable (Sheets)

Aun con la columna `estado` bien cargada y el prompt instruido para filtrar por `disponible`, el
agente terminaba ofreciendo unidades no disponibles; hubo que **eliminar físicamente** las filas
no vendibles de la base para que no aparecieran. No escala: un cliente con inventario grande no
puede borrar productos. Documentar el límite de volumen del filtrado. Confirmado en G&D;
incidente imputable. Se mitiga en el diseño (dominios limpios) pero no se elimina por prompt.

### 24. Límite de elementos por búsqueda, no documentado

No está documentado cuántos resultados devuelve una búsqueda como máximo, ni si el agente puede
saber que un lote quedó truncado. De ahí la salvaguarda de la ficha (si el lote llega al límite,
repetir por tipología). Pendiente de confirmar con ITESA el número exacto y si el agente puede
leer el total de resultados. Cruza con el reporte de inconsistencia de búsqueda de Tokko.

### 25. Método de consulta multi-hoja no documentado

Nunca se especificó cuántas búsquedas puede hacer el agente por turno ni la forma performante de
consultar un Sheet de varias hojas; se iteró a ciegas. Es una pregunta abierta a ITESA, no un
supuesto que se pueda dar por resuelto. Afecta a cualquier cliente Sheet-First.

---

| Restricción | Regla relacionada |
|---|---|
| 2 — Archivos no son KB | Regla 7 (no hay base de conocimiento separada) |
| 5 — Seguimientos por Smart Tag | Regla 1 y Regla 6 — los matices de AND nativo y "sin tag" están reflejados en la versión actual de ambas reglas (aplicado en v1.11). |
| 7 — Planes | Regla 17 (verificar plan antes de diseñar) |
| 9 — 3 acciones de Smart Tag | Regla 3 (acciones atadas a la tag) |
| 12 — Placeholders vía plantilla | Regla 6 (regla actualizada en v1.11). |
| 14 — Prometheo Connect | Matiza el supuesto "nunca sugerir Make/Zapier" — ver Regla 4. |
| 16, 17, 18 — Match de tags / import | Base técnica del procedimiento de `importacion-contactos.md`. |

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| `embudos-y-tags.md` | Las acciones de Smart Tag (restricción 9), los tipos de variable y el prompt opcional (restricción 4) son la base técnica del modelo de Tags, Variables y Embudos. |
| `importacion-contactos.md` | Las restricciones 16, 17 y 18 son la base técnica del procedimiento de importación. |
| `03-reglas-diseno-prometheo-by-aurea.md` | Las restricciones son la base técnica de varias reglas. |
| `prometheo-etapa2-design` (skill) | El diseño respeta estas restricciones. |
| `framework-seguimientos.md` | Las restricciones 5, 10, 11, 12 y 13 condicionan el diseño de seguimientos. |

---

## Hallazgos de campo — restricciones pendientes de confirmar

> **Ranura de extensión.** Acá se anota cualquier comportamiento de plataforma observado
> trabajando con clientes reales que **todavía no está confirmado** con el bot oficial o
> ITESA. Una restricción sube a la lista numerada de arriba **solo** después de validarse.
> Lo que sea duda sin urgencia operativa va a `pendientes-itesa.md`.
>
> Regla de oro: nunca asumir comportamiento de la plataforma. El hallazgo se registra para
> no perderlo, pero no se trata como restricción firme hasta confirmarse.

_(Sin hallazgos pendientes al cierre de v1.8.)_
