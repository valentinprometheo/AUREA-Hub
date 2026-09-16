---
name: prometheo-etapa1
description: >
  Skill orquestadora de toda la Etapa 1 (Discovery) de la metodología AUREA Hub × Prometheo.
  Es el punto de entrada único para un implementador que arranca el Discovery de un cliente
  nuevo. NO contiene metodología propia: coordina las skills especializadas en el orden
  correcto y le dice al implementador qué hacer en cada paso. Cubre PASO 1 (Pre-Discovery:
  auditoría web, material cliente-facing) y PASO 2 (Discovery: formulario de reunión, las
  reuniones, los 4 documentos output, validación). Activar cuando el implementador diga
  "arranco un cliente nuevo", "empezar Etapa 1", "guiame el Discovery", "primer cliente",
  "qué hago ahora con [cliente]", o cuando no sepa por dónde empezar en Etapa 1.
---

# SKILL ORQUESTADORA — ETAPA 1 (DISCOVERY)

## QUÉ ES ESTA SKILL

Esta skill es el **mapa de ruta de la Etapa 1**. No reemplaza a las skills especializadas — las **coordina**. Si sos un implementador nuevo y no sabés por dónde empezar con un cliente, esta skill te lleva de la mano.

**Regla de oro:** esta skill te dice QUÉ hacer y EN QUÉ ORDEN. Las skills especializadas te dicen CÓMO hacer cada cosa.

---

## LA ETAPA 1 EN UNA VISTA

```
ETAPA 1 — DISCOVERY
│
├── PASO 1 — PRE-DISCOVERY (antes de hablar con el cliente)
│   ├── 1.1 Auditoría web + IG          → skill prometheo-auditoria-web
│   ├── 1.2 Doc de Bienvenida           → cliente-facing
│   └── 1.3 Guía Metodológica           → cliente-facing
│
└── PASO 2 — DISCOVERY (con el cliente)
    ├── 2.1 Preparar formulario reunión → skill prometheo-formulario-[rubro]
    ├── 2.2 Ejecutar la reunión R1      → en vivo
    ├── 2.3 Generar los 4 documentos    → skill prometheo-discovery-transversal
    │        Doc 1 Síntesis / Doc 2 Asincrónico / Doc 3 Accesos / Doc 4 Preguntas Clave
    ├── 2.4 Auditar el Doc 1            → skill prometheo-audit-doc1
    └── 2.5 Validar con el cliente      → gate de cierre
```

---

## ANTES DE EMPEZAR — QUÉ NECESITÁS

El implementador tiene que tener a mano:

1. **El rubro del cliente** — desarrollista inmobiliario / mobiliario / insumos construcción / inmobiliaria tradicional. Define qué skill vertical se usa.
2. **La URL de la web del cliente** y su perfil de Instagram.
3. **Las skills cargadas** en el proyecto Claude:
   - `prometheo-auditoria-web`
   - `prometheo-docs-kickoff`
   - `prometheo-discovery-transversal`
   - `prometheo-vertical-[rubro]` y `prometheo-formulario-[rubro]` (según rubro)
   - `prometheo-audit-doc1`

Si falta el rubro, preguntalo antes de avanzar. Si el rubro es insumos-construcción o inmobiliaria-tradicional, avisá que esas verticales todavía están pendientes de crear.

---

## PASO 1 — PRE-DISCOVERY

### 1.1 — Auditoría web + Instagram

**Skill a usar:** `prometheo-auditoria-web`

**Qué pasa:** se analiza la presencia digital del cliente para llegar a la reunión con preguntas cerradas, no abiertas.

**Output:** Doc 0 — Auditoría web (interno AUREA, el cliente no lo ve).

**Cómo arranca:** el implementador le pasa a Claude la URL + IG del cliente y activa la skill de auditoría.

**Cuándo está listo:** cuando el Doc 0 tiene el inventario pre-armado, las hipótesis de tipología macro, y las preguntas cerradas para la reunión.

### 1.2 — Doc de Bienvenida (cliente-facing)

**Skill a usar:** `prometheo-docs-kickoff`

**Qué es:** el primer documento que el cliente recibe, antes de la R1. Le muestra que llegamos a la reunión con un panorama de su negocio, le explica qué se va a diseñar, presenta las 4 etapas y define quién tiene que estar en la R1.

**Output:** Doc de Bienvenida — DOCX (cliente-facing). El implementador lo exporta a PDF antes de enviarlo.

**Cómo arranca:** con el Doc 0 ya generado, el implementador activa `prometheo-docs-kickoff` y le pasa los inputs del cliente (nombre, rubro, consultor asignado, N de reuniones estimado).

### 1.3 — Guía Metodológica (cliente-facing)

**Skill a usar:** `prometheo-docs-kickoff` (la misma — genera los 2 documentos en secuencia)

**Qué es:** explica al cliente cómo va a funcionar el Discovery — los 3 documentos vivos, la modalidad de cada uno, qué es la "Biblia", dónde vive todo.

**Output:** Guía Metodológica — DOCX que el implementador sube a Drive y abre como Google Doc nativo.

**Cierre del PASO 1:** el cliente recibió el Doc de Bienvenida y la Guía Metodológica, y está listo para la R1.

---

## PASO 2 — DISCOVERY

### 2.1 — Preparar el formulario de reunión

**Skill a usar:** `prometheo-formulario-[rubro]` (real-estate o mobiliario)

**Qué pasa:** se genera la plantilla del formulario de reunión, pre-llenada con lo que salió de la auditoría web (Doc 0). El formulario tiene 3 capas por pregunta: rosa (de la web), naranja (traducción CRM), azul (respuesta en vivo).

**Output:** formulario de reunión personalizado para el cliente.

### 2.2 — Ejecutar la reunión R1

**Qué pasa:** el implementador tiene la reunión con el cliente y completa la capa azul del formulario en vivo.

**Principio clave:** la reunión es conversacional. No se le pregunta al cliente sobre taxonomía CRM (Variables, Smart Tags). Se le pregunta sobre su negocio, y el implementador traduce después.

**Output:** formulario de reunión completado.

### 2.3 — Generar los 4 documentos de Discovery

**Skill a usar:** `prometheo-discovery-transversal` + la skill vertical del rubro

**Qué pasa:** a partir del formulario completado, se generan los 4 documentos output de la Etapa 1:

| Doc | Qué es | Quién lo usa |
|---|---|---|
| Doc 1 — Síntesis | La "biblia" del cliente | El cliente revisa y aprueba |
| Doc 2 — Asincrónico | Solo lo que falta | El cliente completa |
| Doc 3 — Accesos | Accesos + estructura Drive | El cliente completa |
| Doc 4 — Preguntas Clave | Resumen para aprobar sin releer | El cliente valida |

**Regla anti-duplicación:** un dato se pide una sola vez. Si va en Doc 2, no va en Doc 3.

### 2.4 — Auditar el Doc 1

**Skill a usar:** `prometheo-audit-doc1`

**Qué pasa:** se verifica que toda la información del formulario completado haya pasado correctamente al Doc 1. Es un control de calidad obligatorio.

**Output:** reporte de auditoría con estado por dato (✅ transferido / ⚠️ parcial / ❌ faltante).

**Si la auditoría detecta faltantes:** se corrigen antes de enviar el Doc 1 al cliente.

### 2.5 — Validar con el cliente

**Qué pasa:** el cliente recibe los 4 documentos. Revisa, edita, completa lo asincrónico, y aprueba.

**Gate de cierre de Etapa 1:** el Doc 4 (Preguntas Clave de Aprobación) está aprobado por el cliente. Además, todas las reglas [FLEXIBLE] de la skill vertical tienen respuesta.

**Cuando el gate se cumple:** la Etapa 1 está cerrada. Se pasa a la Etapa 2 (Diseño) — skill `prometheo-etapa2-design`.

---

## VERIFICACIÓN DE CIERRE DE ETAPA 1

Antes de pasar a Etapa 2, el implementador verifica:

- [ ] Doc 0 (auditoría web) generado
- [ ] Doc de Bienvenida y Guía Metodológica enviados al cliente
- [ ] Formulario de reunión completado en R1
- [ ] Los 4 documentos generados (Doc 1, 2, 3, 4)
- [ ] Doc 1 auditado con `prometheo-audit-doc1`, sin faltantes críticos
- [ ] Todas las reglas [FLEXIBLE] de la vertical tienen respuesta
- [ ] Doc 4 aprobado por el cliente

Si todo está tildado → Etapa 1 cerrada → arranca Etapa 2.

---

## ERRORES COMUNES A EVITAR

| Error | Por qué está mal |
|---|---|
| Saltear la auditoría web | Se llega a la reunión con preguntas abiertas, la reunión rinde menos |
| Preguntarle al cliente sobre Variables o Smart Tags | El cliente no sabe qué son. Se pregunta sobre el negocio, se traduce después |
| Generar el Doc 1 sin auditarlo | Se le manda al cliente un documento con datos faltantes |
| Pasar a Etapa 2 sin el Doc 4 aprobado | Se diseña sobre información no validada |
| Duplicar preguntas entre Doc 2 y Doc 3 | El cliente se confunde y se cansa |

---

## RELACIÓN CON OTRAS SKILLS

| Skill | Rol en Etapa 1 |
|---|---|
| `prometheo-auditoria-web` | Ejecuta el Paso 1.1 |
| `prometheo-docs-kickoff` | Ejecuta los Pasos 1.2 y 1.3 (Doc de Bienvenida + Guía Metodológica) |
| `prometheo-formulario-[rubro]` | Ejecuta el Paso 2.1 |
| `prometheo-discovery-transversal` | Ejecuta el Paso 2.3 (los 4 docs) |
| `prometheo-vertical-[rubro]` | Aporta los slots verticales en todo el Discovery |
| `prometheo-audit-doc1` | Ejecuta el Paso 2.4 |
| `prometheo-etapa2-design` | Toma el relevo cuando cierra la Etapa 1 |

---

## NOTA PARA EL IMPLEMENTADOR

Esta skill es tu hoja de ruta. Si en algún punto no sabés qué hacer, volvé acá y mirá en qué paso estás. Cada paso te dice qué skill especializada activar. No intentes hacer todo de memoria — el valor de la metodología AUREA está en seguir el orden.
