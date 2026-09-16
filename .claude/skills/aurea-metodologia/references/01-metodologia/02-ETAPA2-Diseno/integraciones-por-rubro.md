# Integraciones de Prometheo — mapa por rubro

> Las integraciones y canales que ofrece Prometheo, ordenados por las 4 verticales de
> AUREA. Sirve para decidir, en Etapa 2, qué integraciones tiene sentido proponerle a cada
> cliente según su rubro. Fuente: GitBook oficial de Prometheo
> (`prometheo.gitbook.io/prometheo/integraciones/`).

---

## Cómo leer este mapa

Una integración de Prometheo es una **capacidad de plataforma**, no un atributo del rubro.
El rubro no "tiene" integraciones — **elige** cuáles le sirven. Este archivo es la vista de
conjunto para tomar esa decisión.

Nivel de confianza de cada ficha:

- **[CONFIRMADO]** — leído a fondo en el GitBook, capacidad verificada.
- **[GITBOOK — DETALLE PENDIENTE]** — la integración existe y está listada, pero su página
  específica no se leyó a fondo. Para proponerla a un cliente con precisión, leer
  `prometheo.gitbook.io/prometheo/integraciones/[nombre]` antes.

> Regla de oro: si una integración está marcada DETALLE PENDIENTE, no se afirman sus
> límites ni su comportamiento fino sin leer su página. Se confirma antes de diseñar.

---

## Catálogo de integraciones y canales

### Integraciones de datos / CRM externos

| Integración | Qué hace | Confianza |
|---|---|---|
| **Google Sheets** | Lectura de catálogos: "coincidencia exacta" por variable y "búsqueda múltiple". También capta formularios. | [CONFIRMADO] |
| **Google Calendar** | Agenda de turnos. Recordatorios con variables dinámicas vía "/". Tipos de turno configurables: duración, descanso, anticipación, turnos simultáneos, Google Meet. | [CONFIRMADO] |
| **Tokko** | CRM inmobiliario. Sincroniza cada 2 horas. Puede crear leads automáticamente en Tokko disparado por Smart Tags. | [CONFIRMADO] |
| **WooCommerce** | Ecommerce sobre WordPress. | [GITBOOK — DETALLE PENDIENTE] |
| **Tienda Nube** | Ecommerce (plataforma LATAM). | [GITBOOK — DETALLE PENDIENTE] |
| **PrestaShop** | Ecommerce. Integración nativa. | [GITBOOK — DETALLE PENDIENTE] |
| **High Level** (ex Go High Level) | CRM / marketing all-in-one. | [GITBOOK — DETALLE PENDIENTE] |
| **Cloudbeds** | PMS hotelero. | [GITBOOK — DETALLE PENDIENTE] |
| **Clienty** | CRM. | [GITBOOK — DETALLE PENDIENTE] |
| **Dentalink** | Software de gestión odontológica. | [GITBOOK — DETALLE PENDIENTE] |
| **Mercado Libre** | Marketplace. | [GITBOOK — DETALLE PENDIENTE] |
| **Kommo** | CRM conversacional. | [GITBOOK — DETALLE PENDIENTE] |
| **HubSpot** | CRM / marketing. | [GITBOOK — DETALLE PENDIENTE] |
| **Prometheo Connect** | Constructor genérico de endpoints API: el asistente consulta y crea datos en cualquier sistema externo sin programar, usando Variables para el body. Cubre lo que no tiene integración nativa. | [CONFIRMADO] — planes pendientes con ITESA |

### Canales de conversación

| Canal | Nota | Confianza |
|---|---|---|
| **WhatsApp** | Canal principal. Dos conexiones — QR y API oficial (ver restricción 15). | [CONFIRMADO] |
| **Instagram** | Mensajería directa. | [CONFIRMADO] |
| **Instagram — comentarios** | Responder comentarios de IG. Solo plan Enterprise. | [CONFIRMADO] |
| **Facebook Messenger** | Mensajería directa. | [GITBOOK — DETALLE PENDIENTE] |
| **WebChat** | Chat embebido en sitio web. | [GITBOOK — DETALLE PENDIENTE] |
| **Mercado Libre — Preguntas** | Responder preguntas de publicaciones de ML. | [GITBOOK — DETALLE PENDIENTE] |
| **TikTok** | Mensajería. Solo plan Enterprise. | [GITBOOK — DETALLE PENDIENTE] |

---

## Mapa por vertical

> Para cada vertical: las integraciones **núcleo** (las que casi siempre aplican) y las
> **según caso** (dependen del setup del cliente). Sección extensible — un caso real puede
> mover una integración de "según caso" a "núcleo" o agregar una nueva observación.

### Desarrollista inmobiliario

*Clientes de referencia: G&D Developers, EDFAN Real Estate.*

| | Integraciones |
|---|---|
| **Núcleo** | **Tokko** (CRM inmobiliario estándar del rubro — lo que está en Tokko no se hardcodea en el prompt), **Google Calendar** (coordinación de visitas a obra / showroom), **WhatsApp**. |
| **Según caso** | **Google Sheets** (si el cliente maneja listas de precios o stock en planillas), **Instagram** (captación), **WebChat** (si tiene web con tráfico), **Meta Ads** vía WhatsApp API (si pauta). |
| **Connect** | Útil si el cliente tiene un ERP o sistema propio de gestión de proyectos sin integración nativa. |

### Mobiliario

*Cliente de referencia: BETROX.*

| | Integraciones |
|---|---|
| **Núcleo** | **WhatsApp**, **Google Calendar** (turnos de showroom). |
| **Según caso** | **Tienda Nube / WooCommerce** (si vende online), **Google Sheets** (catálogo / listas de precios), **Instagram** (canal de descubrimiento fuerte en este rubro), **Mercado Libre + ML Preguntas** (si vende en ese marketplace). |
| **Connect** | Útil si maneja un sistema de pedidos / producción a medida sin integración nativa. |

### Insumos y materiales para la construcción

*Clientes de referencia: EDFAN Productos, ZATOH.*

| | Integraciones |
|---|---|
| **Núcleo** | **WhatsApp**, **Google Sheets** (catálogos extensos de productos / listas de precios — habitual en este rubro). |
| **Según caso** | **PrestaShop / Tienda Nube / WooCommerce** (ecommerce — EDFAN Productos usa PrestaShop, que tiene integración nativa), **Mercado Libre + ML Preguntas**, **WebChat**. |
| **Connect** | Vía de entrada para sistemas de gestión mayorista / stock B2B sin integración nativa. |

> **Nota PrestaShop:** EDFAN Productos opera su ecommerce en PrestaShop, que **es una
> integración nativa de Prometheo**. No hace falta Connect ni mantener el catálogo en
> Sheets como workaround: se conecta directo. Confirmar con ITESA el alcance de la
> sincronización (catálogo, precios, stock) al diseñar.

### Inmobiliaria tradicional

*Cliente de referencia: Paganini Inmobiliaria.*

| | Integraciones |
|---|---|
| **Núcleo** | **WhatsApp**, **Google Calendar** (coordinación de visitas a propiedades). |
| **Según caso** | **Tokko** (si la inmobiliaria lo usa como CRM), **Google Sheets** (si el stock se maneja en planilla o catálogo externo tipo ficha.info), **Instagram**, **WebChat**. |
| **Connect** | Para portales o CRMs inmobiliarios sin integración nativa. |

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| `restricciones-plataforma-prometheo.md` | Restricción 14 (Connect) y 15 (conexiones WhatsApp) son la base técnica de este mapa. |
| `06-rubros/0X-[rubro].md` | Cada archivo de rubro puede referenciar la fila correspondiente de este mapa — la fuente del mapa vive acá. |
| `prometheo-etapa2-design` (skill) | Al diseñar el CRM se eligen integraciones a partir de este mapa. |
| Discovery (Etapa 1) | Preguntar siempre qué sistemas usa hoy el cliente — alimenta la columna "según caso". |

---

## Hallazgos de campo — integraciones pendientes de profundizar

> **Ranura de extensión.** Acá se registra: integraciones marcadas DETALLE PENDIENTE que se
> hayan leído y confirmado (para promoverlas a CONFIRMADO), integraciones nuevas que
> aparezcan en el GitBook, o aprendizajes de campo sobre cómo una integración se comporta
> con un cliente real.

- **Pendiente de lectura a fondo:** páginas del GitBook de WooCommerce, Tienda Nube,
  PrestaShop, High Level, Mercado Libre, Kommo, HubSpot y Meta Ads. Leer la página
  específica antes de proponer cualquiera de estas con detalle a un cliente.
- **Pendiente con ITESA:** si el uso de Prometheo Connect consume el cupo de "integración
  de marketplace" del plan o es independiente; alcance de la sincronización de PrestaShop
  (catálogo / precios / stock).
