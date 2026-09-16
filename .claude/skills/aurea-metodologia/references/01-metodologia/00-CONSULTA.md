# 00 — CONSULTA · Router de la metodología

> Esto es lo PRIMERO que se lee en cualquier conversación de trabajo. No tiene contenido
> de metodología: es una tabla de despacho. Decí qué estás haciendo y te dice qué cargar.
> La metodología no se lee de corrido como un manual: se consulta por partes y se ensambla.

---

## La idea: cuatro ejes que se combinan

Toda tarea de consultoría es una intersección: **un estadío, de un cliente, de un rubro,
con una integración, en una conversación nueva o con trayectoria.** En vez de cargar el
manual entero, cargás solo la rebanada que esa intersección necesita.

El contenido está partido en cuatro ejes ortogonales (se combinan libremente, sin
duplicar nada):

| Eje | Qué aporta | Cuándo se carga | Dónde vive |
|---|---|---|---|
| **PROCESO** (estadío) | método del estadío, qué produce, qué necesita de input | siempre (según en qué etapa estés) | `01-ETAPA1...` `02-ETAPA2...` `03-ETAPA3...` `04-ETAPA4...` |
| **RUBRO** (vertical) | lógica comercial específica del rubro | si el cliente es de ese rubro | `06-rubros/` |
| **INTEGRACIÓN** (fuente de datos) | reglas de consulta a la fuente | si el cliente usa esa integración | `02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` |
| **TRANSVERSAL** (siempre activo) | principios de agente, reglas de modificación de prompt, placeholders | siempre, en toda tarea de diseño | `02-ETAPA2-Diseno/principios-transversales-agente.md`, `03-reglas-diseno-prometheo-by-aurea.md`, `metodologia-correccion-agente.md` |

La potencia es la composición. **"Etapa 2 · mobiliario · PrestaShop"** = proceso-etapa2 +
rubro-mobiliario + integración-prestashop + transversales. Cuatro piezas chicas, no el
manual entero. Eso es lo que mantiene la consulta barata y precisa.

---

## Cómo se usa: declarás los ejes, cargás la intersección

Antes de empezar cualquier tarea, resolvé estas cuatro preguntas. Con eso sabés exactamente
qué archivos abrir.

```
1. ¿En qué ESTADÍO estoy?      → Etapa 0 / 1 / 2 (diseño) / 2 (iteración) / 3 / 4
2. ¿De qué RUBRO es el cliente? → real-estate / mobiliario / insumos / inmobiliaria
3. ¿Qué INTEGRACIÓN usa?        → Sheets / Tokko / PrestaShop / ninguna (todavía)
4. ¿Conversación NUEVA o con TRAYECTORIA?
```

### Tabla de despacho por ESTADÍO

| Estoy en… | Cargá (proceso) | Más (según ejes) |
|---|---|---|
| **Etapa 0 — auditoría web** | `02-skills/.../prometheo-auditoria-web` | rubro (para saber qué buscar) |
| **Etapa 1 — discovery** | `01-ETAPA1-Discovery/` + skill discovery-transversal | rubro (slots verticales) |
| **Etapa 2 — diseño CRM** | `02-ETAPA2-Diseno/01-PASO1-Diseno-CRM/` + `embudos-y-tags.md` + `arquitectura-crm-por-rubro.md` | rubro, transversal |
| **Etapa 2 — diseño prompt** | `05-estructura-prompt-agente.md` | rubro + **integración** + transversal |
| **Etapa 2 — iteración prompt** | `feedback-demo-iteracion.md` + `metodologia-correccion-agente.md` | transversal + el prompt vigente del cliente |
| **Etapa 2 → Etapa 3 — Guía de Implementador** | `06-estructura-guia-implementador.md` | integración + rubro + `framework-seguimientos.md` (5 mecanismos de mensajería) |
| **Etapa 3 — lanzamiento** | `03-ETAPA3-Lanzamiento/` | integración (verificar carga) |
| **Etapa 4 — monitoreo** | `04-ETAPA4-Mejora-Continua/` | métricas core |

### Tabla de despacho por INTEGRACIÓN (cruza todos los rubros)

Esta es la que más acelera el próximo prompt: las reglas de consulta dependen de la
**fuente**, no del rubro. El próximo cliente con Sheets necesita lo mismo que G&D, sea del
rubro que sea.

| Si el cliente usa… | Cargá la sección | Caso de referencia |
|---|---|---|
| **Google Sheets** | `08-reglas-integracion-catalogo.md` § Sheets | G&D Developers |
| **Tokko** | `08-reglas-integracion-catalogo.md` § Tokko | EDFAN Real Estate |
| **PrestaShop** | `08-reglas-integracion-catalogo.md` § PrestaShop | BETROX |

### TRANSVERSAL — se carga SIEMPRE en diseño/iteración de prompt

- `principios-transversales-agente.md` — los 17 principios de comportamiento del agente.
- `logica-comercial-transversal.md` — cómo VENDE el agente (calificar, objetar, cerrar); patrón vs instancia.
- `03-reglas-diseno-prometheo-by-aurea.md` — reglas de modificación de prompt (aditivo,
  aislado, no regresivo).
- `metodologia-correccion-agente.md` — cómo se procesa feedback, el barrido 8+1 y el template
  de auditoría de entrega.
- `10-patrones-correccion-agente.md` — los 13 patrones para auditar un prompt vivo.
- `contradicciones-jerarquia.md` — cuando un bug puntual se repite en toda una familia (reglas que compiten).
- `guion-testing.md` — cómo se valida el agente (primos, PLATAFORMA, regresión).
- `gestion-proveedor-itesa.md` — cuando el proveedor entrega una reescritura o hay que elevar
  un incidente.
- `arquitectura-crm-por-rubro.md` — molde de embudos/tags/variables al arrancar una cuenta.
- `inteligencia-comercial-producto.md` — cuando se ofrece o diseña el producto de IC.

---

## Modo NUEVA vs modo TRAYECTORIA

La dinámica cambia según si arrancás un cliente de cero o retomás uno con historia.

### Conversación NUEVA (cliente de cero, o tarea sin contexto previo)
1. Resolvé los cuatro ejes (arriba).
2. Cargá el set mínimo de esa intersección.
3. Si falta un eje por definir (ej. todavía no sabés la integración porque estás en
   discovery), lo dejás abierto y se resuelve cuando aparezca.

### Conversación con TRAYECTORIA (cliente ya conocido, seguir donde quedó)
1. **No recargues la metodología entera.** El cliente ya tiene ejes definidos (rubro +
   integración conocidos de la memoria del proyecto o de chats pasados).
2. Traé solo el **delta** que la tarea puntual necesita + el **estado actual** del cliente
   (el prompt vigente, el último doc, la última decisión).
3. Ejemplo: *"seguí el prompt de BETROX donde quedamos"* → no recarga toda la metodología
   de mobiliario; trae la pieza puntual + reglas de modificación + el prompt vigente de
   Catalina.

> Para recuperar el estado de un cliente con trayectoria: memoria del proyecto primero;
> si no alcanza, buscar en conversaciones pasadas. El estado del cliente NO vive en el ZIP
> (el ZIP es doctrina, no historia de cliente).

---

## Dos ejemplos completos de consulta

**"Arranco un cliente nuevo de insumos para construcción, Etapa 1."**
→ proceso: `01-ETAPA1-Discovery/` + skill discovery-transversal
→ rubro: `06-rubros/03-insumos-construccion.md`
→ integración: todavía no (falta discovery)
→ transversal: no aplica aún (no hay diseño de prompt todavía)
Cargás discovery + insumos. Nada de mobiliario ni PrestaShop.

**"Seguí el prompt de EDFAN, ajustar la lógica de financiación."** (trayectoria)
→ cliente conocido: real-estate + Tokko
→ delta: sección financiación de `06-rubros/01-real-estate.md`
→ transversal: `03-reglas-diseno-prometheo-by-aurea.md` (modificación aditiva, no regresiva)
→ estado: el prompt vigente de Martina
No recargás la metodología entera de real-estate.

---

## Auto-ruteo: cada archivo declara cuándo se consulta

Los archivos de contenido llevan un encabezado corto (estilo `description` de skill) que
declara cuándo son relevantes y con qué se combinan:

```
---
consultar-cuando: Etapa 2, diseño de prompt, rubro mobiliario
disparadores: "diseñar prompt de muebles", "agente PrestaShop", "BETROX"
fuente-única-de: lógica comercial mobiliario
combina-con: transversales, integracion/prestashop
---
```

Eso hace que la metodología se comporte como el ecosistema de skills: cada archivo sabe
cuándo entra y con qué se ensambla. No hace falta recordar dónde está cada cosa: el router
y los encabezados lo resuelven.

---

## Mapa rápido de los cuatro ejes (para no perderse)

```
01-metodologia/
  00-CONSULTA.md          ← estás acá (router)
  00-INDEX.md             ← índice maestro de archivos
  01-ETAPA1-Discovery/    ┐
  02-ETAPA2-Diseno/       ├ EJE PROCESO (estadío)
  03-ETAPA3-Lanzamiento/  │
  04-ETAPA4-Mejora-Continua/ ┘
  06-rubros/              ← EJE RUBRO (vertical)
  02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md  ← EJE INTEGRACIÓN (fuente)
  02-ETAPA2-Diseno/principios-transversales-agente.md ┐
  02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md ├ EJE TRANSVERSAL
  02-ETAPA2-Diseno/metodologia-correccion-agente.md   ┘
  00-OUTPUTS-POR-ETAPA.md ← índice de qué documento se entrega en cada etapa
                            (los templates viven en la skill documentos-client-facing)
```
