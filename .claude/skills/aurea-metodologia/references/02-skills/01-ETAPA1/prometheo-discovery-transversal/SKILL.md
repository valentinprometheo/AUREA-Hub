---
name: prometheo-discovery-transversal
description: >
  Skill base para la etapa de Discovery de cualquier cliente de Prometheo (CRM con IA).
  Usar SIEMPRE que se trabaje con un discovery. Se usa junto con skill vertical del rubro
  y después de la auditoría web (Paso 0). Genera 4 documentos output: Doc 1 (síntesis/biblia),
  Doc 2 (asincrónico — solo lo que falta), Doc 3 (accesos y drive), Doc 4 (preguntas clave
  de aprobación — resumen ejecutivo para validar sin releer todo). Incluye convenciones UX/UI
  de colores, framework de seguimientos, métricas core Prometheo, y transición a Etapa 2.
  Activar ante: discovery, formulario, pre-work, reunión, bloques, DDV, entregables,
  seguimientos, métricas, aprobación, transición etapa 2.
---

# SKILL: DISCOVERY TRANSVERSAL — METODOLOGÍA PROMETHEO

## ACOPLE
Se usa con: skill auditoría web (Paso 0, antes) + skill vertical del rubro (siempre).
Si falta la vertical, pedir a Valentín que identifique el rubro.

---

## SECCIÓN 1 — CONTEXTO Y RESTRICCIONES

Valentín Zas (AUREA), consultor Master Partner de Prometheo. 4 verticales: desarrollista inmobiliario, mobiliario, insumos para construcción, inmobiliaria.

**Fases:** F1 Descubrimiento (sem 1-2, gate: DDV) → F2 Diseño (sem 2-4, gate: prompt+5 simulaciones) → F3 Lanzamiento (sem 4-6, gate: 50 conv.) → F4 Monitoreo (mes 2+).

**Restricciones plataforma:** 1 asistente todos los canales | archivos NO son KB (se envían con "/") | Smart Tags: 15-25 palabras | Variables: tipos Texto/Link/Número/Texto largo/Precio/Opciones | Seguimientos: 1 tag por seguimiento | WA API: 23hs sin plantilla, después Meta template | WA QR: sin restricción | Planes: Base/Pro/Enterprise | Saldo IA = tokens.

---

## SECCIÓN 2 — PRINCIPIOS

1. Conversacional, no formulario. Captura en vivo, traducción en frío.
2. Reemplaza → Variable. Se acumula → Smart Tag.
3. Funnel 3 niveles (lead / oportunidad / producto). No mezclar.
4. KPI primero → después taxonomía.
5. Precios = pregunta más crítica. NUNCA asumir.
6. MVP primero. Mejor poco y bien.
7. Una frase → puede tocar Variable, Smart Tag, calificación, contenido, KPI, funnel.
8. Cada vertical tiene su tipología macro.

---

## SECCIÓN 3 — SISTEMA DE DISCOVERY

**Paso 0:** Auditoría web+IG (skill propia). Genera Doc 0 interno + adapta plantilla formulario.
**Pre-work:** Doc 2 (asincrónico) pre-llenado con Doc 0, entre reuniones.
**R1 (60-90min):** B0, B1, B2, B7, B8 — con preguntas cerradas del Doc 0.
**R2 (60-90min):** B3, B4, B5, B6, B9, B10, B11, B12 (y B13/B2B si aplican).
**R3 (solo si hace falta):** +3 líneas, desacuerdo lead calificado, routing complejo.
**Síntesis:** Consultor arma Doc 1 → cliente aprueba vía Doc 4.

### Bloques del Discovery (resumen — la vertical llena los slots específicos)

> Estructura oficial completa en `01-metodologia/01-ETAPA1-Discovery/02-PASO2-Discovery/estructura-discovery.md`. Resumen operativo:

**B0 Objetivo y dolor:** Qué lograr en 60-90 días, dolor principal, expectativa de mejora.
**B1 Equipo y herramientas:** Quién vende, cómo se reparten leads, herramientas, canales de entrada. Slot vertical: lógica reparto rubro.
**B2 Cartera macro:** Todo lo que venden con su lógica. Regla Tokko/ERP. Slot vertical: tipología macro.
**B3 Calificación:** Tipos de contacto, 3-5 criterios, presupuesto, señales. Slot vertical: tipos rubro.
**B4 FAQs y objeciones:** Top FAQs + top objeciones + manejo. Slot vertical: objeciones rubro.
**B5 Flujo y seguimientos:** Objetivo del agente, proceso de venta, 7 puntos de seguimientos.
**B6 Tono y voz:** Voseo/tuteo, nombre del agente, formalidad, emojis, prohibidas, chat ejemplo.
**B7 Canales:** Canales activos, WA API/QR, plan Prometheo, pauta.
**B8 Autonomía:** ⚠️ PRECIOS. ¿Puede dar? ¿Rangos? ¿Del sistema? Qué decide solo / qué escala.
**B9 Contenidos:** Brochures, fichas, videos. Archivos con "/" pero NO lee contenido.
**B10 KPI y baseline:** 5 métricas core Prometheo (ver abajo) + KPI del rubro (slot vertical).
**B11 Excepciones:** VIP, referidos, campañas, promos.
**B12 Derivación a humano:** Cuándo deriva, a quién, con qué info se pasa el lead, qué pasa si el humano no responde.
**B13 Logística (condicional):** Activar cuando el rubro tiene la logística como variable clave (envío, retiro, instalación, plazos, zonas). Aplica a mobiliario, insumos, e-commerce físico. NO aplica a desarrollista (la logística de obra va en B2). Slot vertical: qué se releva.
**B2B (condicional):** Intermediarios del rubro. Slot vertical define tipos.

### 5 métricas core Prometheo (preguntar el "antes")
1. Velocidad respuesta (3X): "¿Cuánto tardan hoy en responder?"
2. Leads calificados (+55%): "De 100 consultas, ¿cuántas son leads reales?"
3. Capacidad sin sumar equipo (3X): "¿Cuántas consultas/día? ¿Se pierden alguna?"
4. Satisfacción (+25%): "¿Miden? ¿Quejas por demora?"
5. Ventas (+25-250%): "¿Ventas/mes digital? ¿Ticket promedio?"

---

## SECCIÓN 4 — SEGUIMIENTOS

### Mecánica Prometheo
Chats → globito Seguimientos. Campos: título, 1 solo tag, canal, delay, texto, adjuntos, franja horaria, repeticiones (5x máx). Condiciones: tag presente + delay cumplido + asistente encendido + solo conv. nuevas. Sin tag = genérico. Avanzado: AND/OR tags+variables (Fase 2). WA API 23hs → plantilla Meta. Lead responde → se cancela.

### Errores típicos
Muchos tags (necesita TODOS). Texto vago sin CTA. Horarios irrespetuosos. Sin objetivo claro. Delays inventados.

### 7 puntos del negocio (relevar en B5)
1. Etapas proceso venta
2. Tiempos reales de decisión por etapa
3. Qué es urgente vs qué no
4. Objetivo por etapa (1 seguimiento = 1 objetivo)
5. Automatización vs humano
6. Sensibilidad horaria
7. Segmentos clave

### Ficha modelo
```
Título | Objetivo | Etapa funnel | Tag (1 solo) | Canal | Delay | Texto (contexto + pregunta cerrada) | Franja | Repeticiones | Si responde | Fase (MVP/F2)
```

### Timing por temperatura
Caliente: 30min–2hs–24hs | Tibio: 4hs–24hs–72hs | Frío: 72hs–7días | Reactivación: 15–30–60 días

---

## SECCIÓN 5 — LOS 4 DOCUMENTOS OUTPUT

### Convenciones UX/UI (Doc 1, Doc 2 y Doc 4)
- ✏️ **Texto en azul** = instrucciones para editar o completar
- ✏️ **Texto en naranja** = NOTA INTERNA AUREA = info para el consultor, no requiere acción del cliente
- ✏️ **Texto en gris** = A FUTURO = post-lanzamiento
- **"¿Esta información es correcta? Sí / No"** = al final de CADA sección. El cliente borra lo que no corresponda.
- **"Si algo no es correcto o falta información, editen directamente en este documento."** = al final de cada sección.

### Doc 1 — Síntesis de discovery (la "biblia")
**Genera:** Consultor post-reuniones. **Edita:** Cliente. **Aprueba:** Cliente vía Doc 4.

Secciones:
1. Ficha del cliente (nombre, vertical, responsable, equipo, CRM, canales, web, trayectoria)
2. Estado por bloque — semáforo: ✅ completo | ⚠️ parcial | ❌ faltante + "tenemos / falta"
3. Información relevada por bloque del Discovery — todo lo dicho en reuniones, con Sí/No por sección
4. Variables (datos únicos por lead) — tabla en lenguaje del cliente: dato | tipo | valores posibles
5. Situaciones detectadas (Smart Tags en lenguaje humano) — tabla: situación | categoría | para qué
6. Etapas del proceso (funnel 3 niveles) — qué mueve el agente vs qué el equipo
7. Definición de lead calificado — criterios por segmento si aplica
8. Seguimientos diseñados — fichas completas MVP
9. Checklist completitud — 15 entregables: # | punto | estado | tenemos | falta
10. Observaciones — notas internas AUREA (naranja) + recomendaciones técnicas

### Doc 2 — Información asincrónica (solo lo que falta)
**Genera:** Consultor post-R1, pre-llenado con Doc 0. **Completa:** Cliente entre reuniones.

Principios: solo lo que falta ("ya tenemos X, falta Y"). Lenguaje de negocio. "Respondan como hablarían entre ustedes." Sin jerga CRM.

Secciones (adaptadas por rubro con la skill vertical):
- Fichas por producto/línea (pre-llenadas con Doc 0)
- FAQs + insight clave que no puede faltar en cada respuesta
- Objeciones + "cómo las manejan hoy"
- Fichas de reunión/visita (tipo, objetivo, duración, horario, responsable)
- Seguimientos que hacen hoy de forma manual
- Tono: nombre agente, adjetivos marca, palabras prohibidas, chat ejemplo
- Señales de calificación pendientes
- Baseline métricas (consultas/semana, visitas, cotizaciones, conversión)

**⚠️ Regla anti-duplicación Doc 2 vs Doc 3:** La información se pide UNA SOLA VEZ. Si un dato va en Doc 2 (ej: "¿qué FAQs tienen?"), NO se repite en Doc 3. Si va en Doc 3 (ej: "subir brochure al Drive"), NO se pide en Doc 2. Cuando hay ambigüedad, marcar explícitamente: "Esto lo contestás en el Doc 2, no acá" o "Esto lo subís al Drive (Doc 3), no acá."

### Doc 3 — Accesos y documentación
**Genera:** Consultor, pre-llenado con Doc 0. **Completa:** Cliente (Sí/No por ítem).

**Estructura canónica:** el Doc 3 se arma según el template `doc3-accesos-documentacion-template.md` (en `01-metodologia/01-ETAPA1-Discovery/02-PASO2-Discovery/`). Ese template es la fuente de verdad de qué categorías de material lo componen, la estructura de carpetas Drive y el material crítico mínimo. No re-listar acá su contenido — si el template cambia, esta skill ya queda alineada.

Lo propio de esta skill respecto al Doc 3:
- Se pre-llena con lo detectado en el Doc 0 (auditoría web).
- El cliente lo completa de forma asincrónica (Sí/No por ítem, "subir al Drive, no contestar acá").
- Aplica la regla anti-duplicación con el Doc 2 (ver arriba).

### Doc 4 — Preguntas clave de aprobación (NUEVO)
**Genera:** Consultor post-Doc 1 completo. **Responde:** Cliente. **Función:** Aprobar el discovery sin releer todo el Doc 1.

Propósito: El Doc 1 es largo. El cliente no lo va a releer completo para aprobar. El Doc 4 extrae las 10-15 preguntas más críticas que, si están bien, validan todo el resto. Además, hace que el cliente se sienta comprendido ("entendimos tu negocio así, ¿es correcto?").

Estructura:
```
DOC 4 — VALIDACIÓN DE DISCOVERY
Cliente: [nombre]
Fecha: [fecha]

Leímos todo lo que nos compartieron. Antes de diseñar el agente, necesitamos
confirmar que entendimos bien estos puntos clave. Son [N] preguntas cortas.

1. OBJETIVO
"Entendemos que lo que más les importa es [X]. ¿Es correcto? Sí / No"

2. LEAD CALIFICADO
"Un lead calificado para ustedes es alguien que [criterios]. ¿Está bien? Sí / No"
"Si un lead no cumple estos criterios, [lo que hace el agente]. ¿De acuerdo? Sí / No"

3. PRECIOS Y AUTONOMÍA
"El agente [puede/no puede] mencionar precios. [detalle]. ¿Confirmado? Sí / No"

4. DERIVACIÓN
"Cuando el lead necesita hablar con una persona, va a [nombre]. ¿Correcto? Sí / No"
"Los reclamos van a [persona/proceso]. ¿Correcto? Sí / No"

5. TONO
"El agente se llama [nombre] y habla [descripción tono]. ¿OK? Sí / No"

6. SEGUIMIENTOS
"Vamos a configurar [N] seguimientos automáticos: [resumen]. ¿De acuerdo? Sí / No"

7. PRIORIDAD MVP
"Arrancamos con [productos/líneas MVP]. ¿Confirmado? Sí / No"

8. EXCEPCIONES
"Si preguntan si es IA: [respuesta]. VIP: [regla]. ¿OK? Sí / No"

APROBACIÓN
"Con estas confirmaciones, avanzamos al diseño del agente.
Firma/nombre: ___________
Fecha: ___________"
```

Las preguntas exactas se generan a partir del Doc 1 de cada cliente. La skill vertical aporta las preguntas críticas del rubro.

### Secuencia temporal
1. Antes de R1: Doc 0 (auditoría web, interno)
2. Post R1: Doc 1 draft + Doc 2 + Doc 3 se envían al cliente
3. Entre reuniones: Cliente completa Doc 2 y Doc 3
4. Post R2: Doc 1 se actualiza con info de R2 + asincrónico
5. Post Doc 1 completo: Doc 4 se envía para aprobación rápida
6. Doc 4 aprobado = gate → Etapa 2

---

## SECCIÓN 6 — ENTREGABLES Y TRANSICIÓN A ETAPA 2

### 15 entregables + 2 implícitos
1-13: Objetivo, lead calificado, funnel, variables, tags, derivación, tono, contenidos, autonomía, KPI, responsables, tipología macro, routing.
14 (implícito): Seguimientos validados con ficha.
15 (implícito): Baseline métricas core (5 métricas "antes").

### Transición Etapa 1 → Etapa 2
Cuando Doc 4 está aprobado:
- Doc 1 → DDV → input principal del diseño de prompt (13 secciones)
- Doc 2 completado → alimenta secciones 5 (info producto) y 9 (objeciones) del prompt
- Doc 3 completado → habilita configuración técnica (canales, archivos, calendario)
- Para Etapa 2 usar la metodología completa (13 secciones del prompt, 5 componentes de diseño)

---

## SECCIÓN 7 — INSTRUCCIONES CLAUDE

### Al recibir pedido:
1. ¿Tiene Doc 0? Si no → skill auditoría web
2. ¿Qué rubro? → skill vertical
3. ¿Qué docs existen? ¿Qué bloques están ✅/⚠️/❌?
4. Cada dato → clasificar: Variable / Smart Tag / Funnel / Calificación / Derivación / Autonomía / Seguimiento / KPI

### Al generar docs:
- Doc 1: convenciones UX/UI (azul/naranja/gris, Sí/No). Variables y Tags en lenguaje del cliente.
- Doc 2: solo lo que falta. Pre-llenar con Doc 0. Marcar si algo va en Doc 3 en vez de acá.
- Doc 3: Sí/No por ítem. Marcar si algo va en Doc 2 en vez de acá.
- Doc 4: extraer 10-15 preguntas críticas del Doc 1. Tono empático ("entendimos que...").

### Reglas críticas:
Variable vs Smart Tag | Funnel 3 niveles | Tokko/ERP | Precios NUNCA asumir | MVP primero | 1 tag por seguimiento | Plan Prometheo verificar | Archivos NO son KB | Cada [FLEXIBLE] requiere pregunta
