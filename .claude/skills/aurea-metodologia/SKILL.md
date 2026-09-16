---
name: aurea-metodologia
description: >-
  Metodología de consultoría AUREA × Prometheo para diseñar e implementar CRMs con agente de
  IA sobre la plataforma Prometheo. Usá este skill cuando la tarea sea: diseñar o auditar un
  CRM de Prometheo (embudos, tags, variables), corregir/auditar/iterar el prompt de un agente,
  armar un guión de testing, diseñar seguimientos o mensajería automatizada, trabajar una
  integración de catálogo (Tokko, Google Sheets, PrestaShop), o generar un entregable de
  cliente (Diseño de CRM, Guía de Implementador, carga de contactos, feedback de demo). Es un
  router por cuatro ejes (proceso/etapa, rubro, integración, transversal) que carga bajo
  demanda solo la rebanada de metodología que la tarea necesita, no el manual entero.
---

# AUREA × Prometheo — Router de la metodología

Esto es lo PRIMERO que se lee en cualquier tarea de consultoría. No tiene doctrina adentro:
es una tabla de despacho. Decidís qué estás haciendo y te dice qué recurso cargar. La
metodología no se lee de corrido como un manual, se consulta por partes y se ensambla.

Todo el contenido vive bajo `references/`, sin modificar. Este archivo apunta; no duplica.
La fuente viva del router es `references/01-metodologia/00-CONSULTA.md`, y el índice maestro
con la ficha de cada archivo es `references/README.md` y `references/01-metodologia/00-INDEX.md`.

## La idea: cuatro ejes que se combinan

Toda tarea es una intersección: un estadío, de un cliente, de un rubro, con una integración,
en una conversación nueva o con trayectoria. En vez de cargar todo, cargás solo la rebanada
que esa intersección necesita. Los cuatro ejes son ortogonales y se combinan sin duplicar
nada.

| Eje | Qué aporta | Cuándo se carga |
|---|---|---|
| PROCESO (estadío) | método del estadío, qué produce, qué necesita de input | siempre, según en qué etapa estés |
| RUBRO (vertical) | lógica comercial específica del rubro | si el cliente es de ese rubro |
| INTEGRACIÓN (fuente) | reglas de consulta a la fuente de datos | si el cliente usa esa integración |
| TRANSVERSAL (siempre activo) | principios de agente, reglas de modificación de prompt, placeholders | siempre, en toda tarea de diseño de prompt |

La potencia es la composición. "Etapa 2 · mobiliario · PrestaShop" = proceso-etapa2 +
rubro-mobiliario + integración-prestashop + transversales. Cuatro piezas chicas, no el
manual entero.

## Cómo se usa: declarás los ejes, cargás la intersección

Antes de arrancar, resolvé estas cuatro preguntas:

```
1. ¿En qué ESTADÍO estoy?      -> Etapa 0 / 1 / 2 (diseño) / 2 (iteración) / 3 / 4
2. ¿De qué RUBRO es el cliente? -> real-estate / mobiliario / insumos / inmobiliaria
3. ¿Qué INTEGRACIÓN usa?        -> Sheets / Tokko / PrestaShop / ninguna todavía
4. ¿Conversación NUEVA o con TRAYECTORIA?
```

Con eso sabés qué recursos abrir.

## Tabla de despacho por ESTADÍO (eje PROCESO)

| Estoy en… | Cargá (proceso) | Sumá según ejes |
|---|---|---|
| Etapa 0 — auditoría web | `references/02-skills/01-ETAPA1/prometheo-auditoria-web/SKILL.reference.md` | rubro (para saber qué buscar) |
| Etapa 1 — discovery | `references/01-metodologia/01-ETAPA1-Discovery/` + `references/02-skills/01-ETAPA1/prometheo-discovery-transversal/SKILL.reference.md` | rubro (slots verticales) |
| Etapa 2 — diseño CRM | `references/01-metodologia/02-ETAPA2-Diseno/embudos-y-tags.md` + `references/01-metodologia/02-ETAPA2-Diseno/arquitectura-crm-por-rubro.md` | rubro, transversal |
| Etapa 2 — diseño prompt | `references/01-metodologia/02-ETAPA2-Diseno/05-estructura-prompt-agente.md` | rubro + integración + transversal |
| Etapa 2 — iteración prompt | `references/01-metodologia/02-ETAPA2-Diseno/feedback-demo-iteracion.md` + `references/01-metodologia/02-ETAPA2-Diseno/metodologia-correccion-agente.md` | transversal + el prompt vigente del cliente |
| Etapa 2 → 3 — Guía de Implementador | `references/01-metodologia/02-ETAPA2-Diseno/06-estructura-guia-implementador.md` | integración + rubro + `framework-seguimientos.md` |
| Etapa 3 — lanzamiento | `references/01-metodologia/03-ETAPA3-Lanzamiento/` | integración (verificar carga) |
| Etapa 4 — monitoreo | `references/01-metodologia/04-ETAPA4-Mejora-Continua/` | métricas core |

## Tabla de despacho por RUBRO (eje RUBRO)

| Si el cliente es… | Cargá | Caso de referencia |
|---|---|---|
| Desarrollista inmobiliario | `references/01-metodologia/06-rubros/01-real-estate.md` | G&D, EDFAN RE, TKVA |
| Mobiliario | `references/01-metodologia/06-rubros/02-mobiliario.md` | BETROX |
| Insumos para construcción | `references/01-metodologia/06-rubros/03-insumos-construccion.md` | EDFAN Productos |
| Inmobiliaria tradicional | `references/01-metodologia/06-rubros/04-inmobiliaria-tradicional.md` | Paganini (parcial) |

El sistema [FIJA] / [FLEXIBLE] que usan las verticales está en
`references/01-metodologia/06-rubros/00-sistema-fija-flexible.md`.

## Tabla de despacho por INTEGRACIÓN (eje INTEGRACIÓN)

Las reglas de consulta dependen de la fuente, no del rubro. El próximo cliente con Sheets
necesita lo mismo que G&D, sea del rubro que sea. Todo vive en un archivo:
`references/01-metodologia/02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md`.

| Si el cliente usa… | Sección | Caso de referencia |
|---|---|---|
| Google Sheets | § Sheets | G&D Developers |
| Tokko | § Tokko | EDFAN Real Estate |
| PrestaShop | § PrestaShop | BETROX |

## TRANSVERSAL — se carga SIEMPRE en diseño/iteración de prompt (eje TRANSVERSAL)

Todos bajo `references/01-metodologia/02-ETAPA2-Diseno/`:

- `principios-transversales-agente.md` — los 17 principios de comportamiento del agente.
- `logica-comercial-transversal.md` — cómo VENDE el agente (calificar, objetar, cerrar); patrón vs instancia.
- `03-reglas-diseno-prometheo-by-aurea.md` — reglas de modificación de prompt (aditivo, aislado, no regresivo).
- `metodologia-correccion-agente.md` — cómo se procesa feedback, el barrido 8+1, el template de auditoría de entrega.
- `10-patrones-correccion-agente.md` — los 13 patrones para auditar un prompt vivo.
- `contradicciones-jerarquia.md` — cuando un bug puntual se repite en toda una familia (reglas que compiten).
- `guion-testing.md` — cómo se valida el agente (primos, PLATAFORMA, regresión).
- `gestion-proveedor-itesa.md` — cuando el proveedor entrega una reescritura o hay que elevar un incidente.
- `arquitectura-crm-por-rubro.md` — molde de embudos/tags/variables al arrancar una cuenta.
- `inteligencia-comercial-producto.md` — cuando se ofrece o diseña el producto de IC.
- `restricciones-plataforma-prometheo.md` — las restricciones técnicas que condicionan el diseño.
- `framework-seguimientos.md` — los 5 mecanismos de mensajería automatizada y los 3 sistemas de placeholder.

## Entregables de cliente (qué se produce en cada etapa)

El índice de qué documento cliente-facing se entrega en cada etapa está en
`references/01-metodologia/00-OUTPUTS-POR-ETAPA.md`. Los templates de los entregables viven
en `references/02-skills/05-templates/`. Convenciones visuales de marca:
`references/01-metodologia/07-convenciones-aurea/` (paleta, gráficos, naming).

## Modo NUEVA vs modo TRAYECTORIA

La dinámica cambia según si arrancás un cliente de cero o retomás uno con historia.

Conversación NUEVA (cliente de cero, o tarea sin contexto previo):
1. Resolvé los cuatro ejes.
2. Cargá el set mínimo de esa intersección.
3. Si falta un eje por definir (ej. todavía no sabés la integración porque estás en
   discovery), lo dejás abierto y se resuelve cuando aparezca.

Conversación con TRAYECTORIA (cliente ya conocido, seguir donde quedó):
1. No recargues la metodología entera. El cliente ya tiene ejes definidos (rubro +
   integración conocidos de la memoria del proyecto o de chats pasados).
2. Traé solo el delta que la tarea puntual necesita + el estado actual del cliente (el
   prompt vigente, el último doc, la última decisión).
3. El estado del cliente NO vive acá: estas referencias son doctrina, no historia de cliente.
   Para el estado, memoria del proyecto primero; si no alcanza, conversaciones pasadas.

## Cómo se mantiene este skill

La mejora continua se hace editando el recurso que corresponde bajo `references/` y
versionando el skill (nueva entrada en `references/CHANGELOG.md`), no reempacando un ZIP ni
copiando doctrina dentro de este `SKILL.md`. Este archivo solo rutea; si te encontrás pegando
doctrina acá, va como referencia.

Los aprendizajes nuevos entran por el archivo de su eje:
- lógica de un rubro -> el archivo de `references/01-metodologia/06-rubros/` de ese rubro;
- regla de una fuente de datos -> `08-reglas-integracion-catalogo.md`;
- patrón de comportamiento o de venta -> `principios-transversales-agente.md` o
  `logica-comercial-transversal.md`;
- patrón de corrección -> `10-patrones-correccion-agente.md`.

Criterio de promoción (ya escrito en la metodología, no lo inventes): una lógica sube a
transversal solo cuando la confirma un SEGUNDO RUBRO distinto, no un segundo cliente del
mismo rubro. La forma (patrón) sube a la metodología; el valor concreto de hoy (instancia)
queda en el material del cliente, fuera de estas referencias. El protocolo completo de
extensión está en `references/01-metodologia/protocolo-extension-metodologia.md`.
