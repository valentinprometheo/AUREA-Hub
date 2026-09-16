---
consultar-cuando: Etapa 2, diseño de mensajería automática, cualquier rubro
disparadores: "seguimientos", "follow-ups", "recordatorios", "campañas masivas", "plantillas WhatsApp", "mensajería automatizada"
fuente-única-de: los 5 mecanismos de mensajería automática de Prometheo
combina-con: embudos-y-tags, 08-reglas-integracion-catalogo (placeholders), el rubro correspondiente
---

# Sistema de Mensajería Automatizada — los 5 mecanismos

> Transversal a la Etapa 2. Prometheo tiene **cinco mecanismos** de mensajería automática, cada
> uno con un disparador y un alcance distinto. Los mecanismos 1 a 4 definen **cuándo** sale un
> mensaje; el mecanismo 5 define **cómo se formatea** ese mensaje cuando cae fuera de la ventana
> de 24 hs de WhatsApp. Por eso las plantillas (5) no compiten con los otros cuatro: los
> habilitan. Los cinco conviven; ninguno reemplaza a otro.
>
> **Nota de conexión con integraciones:** este archivo cubre los placeholders de **mensaje**
> (seguimientos y recordatorios). Son un sistema distinto de los placeholders de **archivo**
> (`/Render-`, `/Brochure-`) que vive en `08-reglas-integracion-catalogo.md`. No confundir los
> tres sistemas de placeholder — ver la tabla comparativa al final de este archivo.

---

## Cuadro resumen de los 5 mecanismos

| # | Mecanismo | Qué lo dispara | Alcance | Requiere |
|---|---|---|---|---|
| 1 | Seguimientos | El lead no contesta hace X tiempo | Uno a uno · automático | — |
| 2 | Recordatorios conversacionales | El lead pidió ser contactado en una fecha | Uno a uno · automático | Extensión Recordatorios (Marketplace, gratis) |
| 3 | Recordatorios programados | Una variable de Fecha y hora llega a su momento | Se define 1 vez · corre solo para todos | Extensión Recordatorios programados (Marketplace, Pro) |
| 4 | Campañas masivas | Envío puntual elegido por el equipo | Masivo · puntual | WhatsApp API oficial |
| 5 | Plantillas de WhatsApp (Meta) | No es disparador: es el formato obligatorio fuera de ventana 24 hs | Habilita a los 4 anteriores | WhatsApp API oficial para lo que caiga fuera de ventana |

**Nota de conexión:** con conexión por QR (no API oficial) solo están disponibles los mecanismos
1, 2 y 3. Las campañas masivas (4) y las plantillas de Meta (5) requieren WhatsApp API oficial.

---

## MECANISMO 1 — Seguimientos

Un seguimiento es un mensaje automático que el agente envía cuando un lead deja de responder.
Existe para **empujar** un lead de un estadío al siguiente — no es un recordatorio de cortesía,
es el mecanismo que mueve el embudo cuando el lead se frena. Se configura en Prometheo en
**Chats → ícono globito**.

### Mecánica de plataforma (campos)

| Campo | Qué define |
|---|---|
| Título | Nombre interno del seguimiento — convención: `[Estadío] - post [tiempo]` |
| Segmento (tags + variables) | Condiciones de inclusión y exclusión — ver corrección abajo |
| Canal | WhatsApp / Instagram / etc. |
| Delay | Cuánto espera desde el último mensaje / desde que entra al segmento |
| Texto | El mensaje que se envía (dos alternativas recomendadas para testear cuál engancha) |
| Adjuntos | Archivos opcionales |
| Franja horaria | En qué horario se permite enviar (ver Packs, más abajo) |
| Repeticiones | Hasta 5 veces, con multiplicador de delay que aumenta la espera entre intentos, sin crear seguimientos separados |

### ACTUALIZACIÓN CONFIRMADA — el segmento real de Prometheo (corrige versión anterior)

Versiones previas de este archivo indicaban que un seguimiento dispara por **una sola tag**, y
que la lógica AND de varias tags/variables era "Fase 2". El caso BETROX en producción confirma
que el modelo real y disponible **hoy** es más rico: cada seguimiento es un **segmento**, definido
por:

- **Condiciones de inclusión** por tags y variables, con dos modos: **TODAS** (AND) o **AL MENOS
  UNA** (OR).
- **Exclusiones**, marcando una condición como **"No tiene"** (ej. un seguimiento dispara por la
  tag `Calificado` pero se excluye si el lead ya tiene `Showroom Agendado`, `Videollamada
  Agendada` o `Derivado` — así no se dispara sobre alguien que ya avanzó).

Esta corrección no invalida la regla de diseño de fondo (1 seguimiento = 1 objetivo claro): lo que
cambia es que el segmento que lo dispara puede ser más preciso que una sola tag, usando
inclusión + exclusión.

### Los 6 criterios de redacción (invariables entre clientes)

Aplican a cualquier cliente, sin importar el rubro:

1. **El mensaje no puede asumir en qué quedó la conversación.** Un seguimiento dispara sobre
   cualquier lead que cumpla la condición, sin importar si la charla terminó a mitad de una
   pregunta, después de una ficha completa, o con el lead solo mirando. Frases que asumen el
   estado ("quedamos por la mitad", "seguimos viendo opciones") son incorrectas porque solo son
   verdad para un subconjunto de los casos reales.
2. **El mensaje es deliberadamente general.** La generalidad no es una limitación: es lo que hace
   que el mensaje sea coherente con cualquier conversación posible. Un mensaje genérico nunca
   queda mal; uno específico adivinado, queda mal seguido.
3. **Lo que personaliza no es el texto, es el estadío.** Cuanto más avanzado el estadío, menos
   conversaciones distintas caben ahí, y más específico puede ser el mensaje sin riesgo de sonar
   fuera de lugar. En un estadío temprano (ej. "En Conversación") no se sabe nada de lo
   conversado: el mensaje retoma en general. En un estadío avanzado (ej. "Por Coordinar" /
   "Calificado") ya se sabe que el lead califica y hay interés real: el mensaje puede hablar
   puntualmente de coordinar la visita.
4. **Las variables son la segunda fuente de personalización.** Lo que sí se sabe con certeza del
   lead (su proyecto de interés, su nombre) se puede insertar vía variables — personalización
   real sin adivinar. Requiere que la variable esté cargada; si no lo está, el mensaje cae al
   texto plano o se rompe.
5. **Un solo cierre por mensaje.** Cada seguimiento cierra con UNA sola pregunta o invitación.
   Nunca dos.
6. **La decoración va al inicio, nunca al cierre.** Frases de calor ("un gusto haber charlado",
   "quedé con ganas") van al principio si aplican. El cierre es siempre la pregunta o invitación.

### Convención de nombre

Formato: `[Estadío] - post [tiempo]`. Ejemplos: `En conversación - post 4hs`, `Por coordinar -
post 14 días`. El nombre es autoexplicativo: cualquiera que lo vea en la plataforma entiende qué
hace sin abrir nada.

### Los tres packs de ventana horaria (patrón reutilizable)

| Pack | Franja | Usar para |
|---|---|---|
| Pack 1 · 12/7 | Todos los días, 8:00 a 20:00 | Seguimientos de 4hs, donde el valor es llegar el mismo día |
| Pack 2 · 12/5 | Lunes a viernes, 8:00 a 20:00 | Seguimientos de 72hs, que pueden esperar al lunes sin perder efecto |
| Pack 3 · 8/5 | Lunes a viernes, 9:00 a 17:00 | Seguimientos de 14 días y envíos a base histórica, sin urgencia |

Si el tiempo se cumple fuera de la franja del pack, el mensaje espera a la primera hora hábil del
siguiente período permitido. No se pierde.

**Nota de cadencia:** la cadencia 4hs / 72hs / 14 días es del rubro desarrollo inmobiliario, donde
el ciclo de decisión es largo. Cada rubro tiene su propia periodicidad, que se releva en discovery
(bloque B5) — ver "Timing por temperatura" abajo para el criterio general, y el caso G&D para un
ejemplo completo aplicado.

### Variable "Reasignación Moderador" — patrón reutilizable cross-rubro

Cuando el cliente tiene equipo humano de ventas que puede tomar una conversación antes de que
dispare el primer seguimiento automático, se usa esta variable (Sí/No) para condicionar el
timing: si un vendedor ya intervino (`Reasignación Moderador` = Sí), el primer seguimiento espera
más (ej. 24hs en vez de 4hs) para no pisarlo, y su plantilla de Meta va en categoría **Utility**
(porque es seguimiento a algo que ya gestionó una persona) en vez de **Marketing**. Reutilizable
tal cual en cualquier cliente con vendedores humanos en el embudo.

### Presentación Completa vs Corta

El agente se presenta distinto según sea el primer contacto de un hilo o un reenganche posterior:
- **Presentación Completa** ("Hola [nombre], te habla [Agente] de [Empresa]") va en el primer
  seguimiento de una serie.
- **Presentación Corta** ("Hola [nombre], soy [Agente] de [Empresa] de nuevo") va en los
  reenganches posteriores dentro del mismo hilo.

### Timing por temperatura del lead (criterio general, previo al detalle por rubro)

| Temperatura | Timing de los seguimientos |
|---|---|
| Caliente | 30 min – 2 hs – 24 hs |
| Tibio | 4 hs – 24 hs – 72 hs |
| Frío | 72 hs – 7 días |
| Reactivación | 15 – 30 – 60 días (según rubro) |

### Caso de referencia completo — G&D Developers (desarrollo inmobiliario)

Mensajes definitivos validados por el cliente, con sus alternativas para testear cuál engancha
mejor. Las alternativas varían principalmente en el **gancho comercial** de cierre.

**Estadío: En Conversación** (certeza sobre el lead: que escribió y dejó de contestar, nada más;
mensaje necesariamente general)

- *En conversación - post 4hs* (empuja al mismo estadío, reinicia el hilo; 4hs sin respuesta;
  Pack 1 · 12/7; plantilla Meta `conversacion_4hs`, Marketing):
  > "Hola, soy [Agente] de [Empresa] de nuevo. Quedé a disposición para lo que necesites.
  > ¿Retomamos? Me quedo atenta, gracias."
  Alternativas: "Cualquier duda que te haya quedado, la resolvemos por acá." / "Tal vez haya algo
  más que te pueda interesar. ¿Seguimos viendo?" / "Quedé pendiente de tu respuesta. ¿Retomamos
  cuando puedas?"

- *En conversación - post 72hs* (72hs sin respuesta; Pack 2 · 12/5; plantilla
  `conversacion_72hs`, Marketing):
  > "Hola, te habla [Agente] de [Empresa]. ¿Pudiste pensar un poco más tu búsqueda? Tal vez
  > tengamos algo que te puede interesar. Cualquier duda la resolvemos por acá. Gracias."

- *En conversación - post 14 días* (último intento de la serie; 14 días sin respuesta; Pack 3 ·
  8/5; plantilla `conversacion_14dias`, Marketing):
  > "Hola, te habla nuevamente [Agente] de [Empresa]. Si seguís con la búsqueda, tenemos opciones
  > que tal vez se puedan ajustar bien si sigue activa. ¿Charlamos? Me quedo atenta, gracias."

**Estadío: Por Coordinar** (certeza: el lead califica, hay interés real, y hay un vendedor que
tomó el caso; el mensaje puede hablar de coordinar la visita porque eso es lo que todos los leads
de este estadío necesitan)

- *Por coordinar - post 4hs* (sin gestión humana; empuja a Visita Agendada; condición extra:
  `Reasignación Moderador` NO es "Sí"; Pack 1 · 12/7; plantilla `coordinar_4hs`, Marketing):
  > "Hola, te habla [Agente] de [Empresa]. Un gusto haber charlado con vos hoy. ¿Coordinamos la
  > visita para que lo veas en persona? Me quedo atenta, gracias."

- *Por coordinar - post 4hs* (con gestión humana; mismo empuje; condición extra:
  `Reasignación Moderador` ES "Sí"; espera 24hs en vez de 4; plantilla `coordinar_24hs`, **Utility**
  porque es seguimiento a algo ya gestionado por el equipo):
  > "Hola, te habla [Agente] de [Empresa]. Vengo del equipo para acompañar la coordinación.
  > ¿Avanzamos con la visita para que lo veas en persona? Me quedo atenta, gracias."

- *Por coordinar - post 72hs* (Pack 2 · 12/5; plantilla `coordinar_72hs`, Marketing):
  > "Hola, soy [Agente] de [Empresa] de nuevo. Te escribo por la visita que quedamos en
  > coordinar. ¿Te viene bien algún día de esta semana? Me quedo atenta, gracias."

- *Por coordinar - post 14 días* (Pack 3 · 8/5; plantilla `coordinar_14dias`, Marketing):
  > "Hola, te habla nuevamente [Agente] de [Empresa]. Pasó un tiempo desde que hablamos. Si sigue
  > activo tu interés, tal vez valga la pena coordinar la visita. ¿Charlamos? Me quedo atenta,
  > gracias."

---

## MECANISMO 2 — Recordatorios conversacionales

El agente detecta, dentro de la charla, cuando el lead pide ser contactado en una fecha futura, y
lo agenda solo, sin que nadie configure nada por adelantado. Lo habilita la extensión
**Recordatorios (Gratis)** del Marketplace de Prometheo.

**Cuándo dispara:** una fecha o período que el lead mencionó en la conversación. Ejemplos:
"escribime en marzo", "estoy de viaje, contactame en dos semanas", "todavía no estoy listo,
hablemos el mes que viene".

**A favor:** gratis; rescata leads con objeción de timing que de otro modo se perderían; cero
carga manual, el agente lo detecta conversando.

**A tener en cuenta:** depende de que el agente detecte y registre bien la fecha en la charla;
solo aplica a fechas que surgen de la conversación; hay que validar en testing que el agente la
capture correctamente.

**Ejemplo de mensaje (recontacto diferido):**
> "Hola /Nombre, te habla el asistente. Habíamos quedado en contactarte por estos días para
> retomar tu búsqueda. ¿Seguís interesado? Gracias."

---

## MECANISMO 3 — Recordatorios programados

Se definen **una sola vez**, apuntando a una variable de tipo **Fecha y hora**, y se disparan
solos para cada lead cuando llega su momento. Lo que se carga en cada lead no es el recordatorio,
es el valor de la fecha en su variable; el recordatorio en sí se configura una vez y corre para
todos. Requiere la extensión **Recordatorios programados (Pro)** del Marketplace.

**Cuándo dispara:** una variable de Fecha y hora llega a su momento. Se puede configurar para que
salga el mismo día, o X horas/días antes. Admite condiciones de inclusión y exclusión por tags y
variables. Ejemplo: variable `Reunión Física - Fecha/Hora` → recordatorio pre-visita que sale el
día anterior.

**A favor:** se define una vez y corre solo para todos los leads con fecha cargada; no necesita
integración con Google Calendar, alcanza con la variable de fecha; admite condiciones de
inclusión/exclusión por tags y variables; admite adjuntos (hasta 10 archivos, máx. 30 MB).

**A tener en cuenta:** requiere extensión Pro; si la variable de fecha no está cargada o es
pasada, el recordatorio no dispara; solo usar con vencimientos o fechas reales — urgencia
inventada quema la confianza.

**Ejemplo de mensaje (pre-visita):**
> "Hola /Nombre, te recuerdo tu visita a /Proyecto mañana a las /Hora en /Dirección. ¿Seguís en
> pie? Cualquier cambio, avisame."

### Troubleshooting — "Ningún contacto coincide con el filtro"

El recordatorio programado actúa sobre leads que **ya existen** y cumplen las condiciones **en
ese momento**. Ese mensaje aparece cuando Prometheo no encontró ninguno al armar el recordatorio.
Revisar estos cuatro puntos antes de insistir:
1. ¿El lead tiene la variable de fecha y hora completa?
2. ¿La fecha es futura (no pasada ni vacía)?
3. ¿El lead cumple todos los tags y variables del filtro?
4. ¿Alguna exclusión lo está dejando afuera?

Para probarlo rápido: cargar una fecha futura en un lead existente y armar el filtro apuntando
solo a ese contacto. Si aparece, el mecanismo funciona.

---

## MECANISMO 4 — Campañas masivas

Un envío puntual a un segmento de contactos definido por tags, variables, fecha, horario y
mensaje. A diferencia del recordatorio programado (donde cada lead recibe el mensaje en su propia
fecha), la campaña dispara para **todos los del segmento en el mismo momento**. Se configura con
condiciones de inclusión y exclusión, sin tocar el prompt. Requiere WhatsApp API oficial.

**Cuándo dispara:** un envío puntual elegido por el equipo, en la fecha y horario configurados,
para todos los que cumplan las condiciones del filtro.

**A favor:** configuración rápida (tags + variables + fecha + horario + mensaje); incluir y
excluir por tags y variables arma públicos precisos en minutos; ideal para novedades,
lanzamientos y activación de base por tandas.

**A tener en cuenta:** requiere WhatsApp API oficial (no QR); requiere plantilla de Meta aprobada
(categoría Marketing); riesgo para la calidad del número si muchos silencian o bloquean — enviar
por tandas, no toda la base de golpe.

**Ejemplo de mensaje (novedad de proyecto):**
> "Hola /Nombre, te cuento que sumamos novedades en /Proyecto. Si seguís con la búsqueda, me
> decís y te muestro qué hay. Gracias."

---

## MECANISMO 5 — Plantillas de WhatsApp (Meta)

Fuera de la ventana de 24 hs de WhatsApp, ningún mensaje puede salir sin una plantilla aprobada
por Meta. No son un mecanismo de disparo: son el **formato** que todos los mecanismos anteriores
necesitan para llegar cuando la ventana está cerrada. Se crean en **Conexiones → WhatsApp →
Plantillas** y tardan entre 24 y 48 hs en aprobarse.

### Categorías

| Categoría | Cuándo se usa | Ejemplos |
|---|---|---|
| **Marketing** | Reactivación, campañas, primer contacto, novedades. Todo lo que el negocio inicia sin que el lead lo haya pedido. | Seguimientos de reactivación, campañas masivas, vencimientos comerciales |
| **Utility** | Seguimiento a algo que el lead ya inició o acordó. Sin oferta, sin intención comercial. | Recordatorio de visita agendada, confirmación de derivación |
| **Authentication** | Exclusivamente para códigos de verificación (OTP). No admite contenido comercial. | No aplica en la mayoría de los casos de uso comercial |

**Regla de decisión rápida:** si el mensaje reengancha, ofrece o inicia el contacto → Marketing.
Si da seguimiento a algo ya acordado, sin oferta → Utility. **Ante la duda, declarar Marketing:**
Meta recategoriza lo que esté mal declarado y puede rechazarlo.

### Campos de una plantilla

Nombre interno (minúsculas, números y guion bajo, máx. 60 caracteres, no se puede cambiar
después) · Idioma (Spanish) · Categoría (Marketing/Utility/Authentication) · Formato (Solo texto
por default; también Con título, Imagen, Video o Documento) · Cuerpo (máx. 1024 caracteres, con
variables entre llaves `{Nombre}`) · Ejemplos de variables (un ejemplo por variable) · Botones
(hasta 3, máximo 2 URL y 1 teléfono) · Revisión y envío a Meta (24 a 48 hs).

---

## La barra `/` — sintaxis de variable en recordatorios (distinta de seguimientos)

En los **recordatorios** (mecanismos 2 y 3) de Prometheo, la barra `/` inserta y mapea variables
del lead dentro del mensaje: Prometheo reemplaza cada variable por el valor real al enviar
(`/Nombre`, `/Proyecto`, `/Hora`, `/Dirección`, `/Responsable`). En los **seguimientos**
(mecanismo 1), la personalización funciona a través de plantillas con variables mapeadas en la
configuración de la plantilla de Meta, no con la sintaxis de barra libre en el texto. Antes de
programar cualquier mensaje, verificar que las variables estén completas en los contactos
alcanzados: una variable vacía puede enviarse como texto literal o romper el mensaje.

## Los tres sistemas de placeholder — no intercambiables

| Sistema | Sintaxis | Dónde vive | Para qué |
|---|---|---|---|
| Placeholder de **archivo** | `/Render-NOMBRE`, `/Brochure-NOMBRE` (sin extensión) | Prompt del agente | Referenciar un adjunto (brochure, render, plano, video) que el sistema envía; nunca se muestra al lead como texto. Doctrina completa en `08-reglas-integracion-catalogo.md`. |
| Placeholder de **seguimiento** | Variables mapeadas en la configuración de la plantilla de Meta | Plantilla de WhatsApp (mecanismo 1 y 4) | Personalizar un mensaje de seguimiento o campaña con datos del lead |
| Placeholder de **recordatorio** | Barra `/Nombre` libre en el texto | Recordatorios conversacionales y programados (mecanismos 2 y 3) | Personalizar un recordatorio con datos del lead, sintaxis distinta de la de seguimientos |

No confundir los tres al diseñar un prompt o una guía de implementador: cada uno se configura en
un lugar distinto de Prometheo y con una sintaxis distinta.

---

## Los 7 puntos del negocio a relevar (Discovery, bloque B5)

Antes de diseñar cualquiera de los 5 mecanismos, en el Discovery se relevan estos 7 puntos:

1. **Etapas del proceso de venta** — los pasos desde consulta hasta cierre.
2. **Tiempos reales de decisión por etapa** — cuánto tarda normalmente cada paso.
3. **Qué es urgente vs qué no** — dónde se pierde el lead si no se responde rápido.
4. **Objetivo por etapa** — 1 seguimiento = 1 objetivo claro.
5. **Automatización vs humano** — si el lead responde, ¿sigue la IA o pasa a un humano?
6. **Sensibilidad horaria** — ¿se permite seguir fuera de horario? ¿fines de semana?
7. **Segmentos clave** — ¿el seguimiento a un segmento es distinto al de otro?

---

## Errores típicos a evitar

| Error | Por qué está mal |
|---|---|
| Textos vagos sin CTA | El lead no sabe qué responder, el seguimiento no convierte |
| Horarios irrespetuosos | Mandar fuera de la franja del pack quema la relación con el lead |
| Delays inventados sin datos reales | El timing tiene que salir de los tiempos reales del negocio (punto 2 de arriba) |
| Asumir el estado de la charla en el texto | Ver criterio de redacción 1 — el mensaje tiene que servir para cualquier caso real |
| Recordatorio con fecha inventada | Solo usar con vencimientos o fechas reales (mecanismo 3) |
| Toda la base de una vez en una campaña | Enviar por tandas (mecanismo 4) |

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| `prometheo-discovery-transversal` (skill) | El bloque B5 releva los 7 puntos |
| `03-reglas-diseno-prometheo-by-aurea.md` | Regla 6 (texto literal) y Regla 1 (tags por dimensión) |
| `restricciones-plataforma-prometheo.md` | Restricciones de acción de tag, colores, plan Enterprise para Notificaciones |
| `08-reglas-integracion-catalogo.md` | Sistema de placeholders de archivo (distinto de los de mensaje, ver tabla arriba) |
| `embudos-y-tags.md` | Los seguimientos disparan por tag de estadío — ver el modelo de segmento actualizado |
| `06-estructura-guia-implementador.md` | La Guía de Implementador carga cada seguimiento como ficha completa: segmento + canal + tiempo + mensaje |
| `prometheo-etapa2-design` (skill) | Diseña los seguimientos con la ficha modelo |
| `06-rubros/01-real-estate.md` | Caso de referencia G&D con los mensajes completos y sus alternativas |
