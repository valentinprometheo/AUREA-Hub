---
name: "aurea-metodologia"
description: 'Metodología de consultoría AUREA × Prometheo para diseñar e implementar CRMs con agente de IA. Usala SIEMPRE que la tarea sea: diseñar o auditar un CRM de Prometheo (embudos, tags, variables), definir o medir la calificación de leads (lead calificado, hot lead, no fit, recalificar la base con Mi Prometheo, % de calificados), corregir o iterar el prompt de un agente, armar un guión de testing, diseñar seguimientos, trabajar una integración (Tokko, Google Sheets, PrestaShop), revisar el consumo de tokens, o generar un entregable de cliente (Diseño de CRM, Guía de Implementador, carga de contactos). Rutea por cuatro ejes (etapa, rubro, integración, transversal) y carga solo la parte que la tarea necesita. También se actualiza a sí misma: usala para integrar hallazgos o sacar una versión nueva ("actualizá la metodología", "integrá esto", "derogá tal regla").'
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
- `ahorro-de-tokens.md` — las decisiones de diseño que bajan el consumo de IA (no-demanda, variables, tags, prompt, seguimientos, cero cortes de saldo). Tarifas y costos: skill `aurea-hub-costos-rentabilidad`.
- Toda mejora propuesta (prompt, CRM, consumo) se presenta como card con score: skill `aurea-data-action-driven`.

## Calificación de leads — módulo `references/calificacion/`

Qué es un lead calificado y un hot lead para cada cliente, cómo se traduce a variables y tags,
cómo se mide y cómo se recalifica la base con Mi Prometheo. Se usa en B3 del discovery, en el
diseño de CRM (Etapa 2) y en el tablero de IC. La metodología no define un "% de calificados"
propio: usa la definición del cliente.

| Necesitás… | Leé |
|---|---|
| El criterio transversal y el paso a paso (empezá siempre acá) | `references/calificacion/00-criterio-calificacion.md` |
| El molde del rubro del cliente (cargá **uno solo**) | `references/calificacion/rubros/<rubro>.md` |
| Rubro nuevo | `references/calificacion/rubros/_plantilla-nuevo-rubro.md` |
| Recalificar contactos existentes | `references/calificacion/mi-prometheo-acciones-masivas.md` |
| Auditar una cuenta o un tablero | `references/calificacion/malas-practicas.md` |
| Evidencia externa (speed-to-lead, scoring, Meta) | `references/calificacion/fuentes-externas.md` |
| Tarifas y medición del consumo | `references/calificacion/ahorro-de-tokens-detalle.md` |

**Paso 0 obligatorio:** antes de proponer nada, pedí el rubro y el documento del discovery
donde el cliente define la calificación. Si no lo definió, el molde del rubro va como
propuesta a validar, rotulada así.

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

**Modelo de datos vigente (no confundir con versiones viejas):** el estadío del lead es una
tag del embudo; el perfil del contacto es una tag; la excepción (ej. Contacto VIP) es una tag;
las variables guardan datos del lead. Ninguna variable guarda la etapa ni en qué embudo está.

**Antes de cerrar una versión:** buscá en todo el skill la lista de términos derogados que
está en `metodologia-correccion-agente.md` (chequeo de la propia metodología). Si alguno
aparece fuera de un contexto marcado como derogado o histórico, la versión no se cierra.

## Actualizar esta skill (mejora continua)

Cuando haya que integrar mejoras, corregir o derogar doctrina, o sacar una versión nueva,
seguí `references/actualizar/procedimiento.md`. Resumen: copiá la versión vigente como
"anterior" y "nueva", clasificá cada mejora (patrón o instancia, rubro o transversal) con
`references/actualizar/protocolo-de-ingreso.md`, ubicala en su archivo dueño para
complementar sin superponer, propagá lo derogado, escribí la entrada del CHANGELOG y corré
`scripts/auditar.py` contra la anterior. Con fallas, no se entrega. Esta skill trae adentro su
propia forma de actualizarse.
