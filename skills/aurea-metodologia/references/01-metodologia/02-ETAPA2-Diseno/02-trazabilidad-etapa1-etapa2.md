# 02 — Trazabilidad Etapa 1 → Etapa 2

**Cómo cada hallazgo del Discovery se convierte en una decisión de diseño concreta.**

---

## Por qué importa este documento

La metodología no es "hacer Etapa 1" + "hacer Etapa 2" como procesos separados. La conexión entre ambas es donde se juega la calidad final del agente. Cada cosa que descubrís en Discovery tiene que producir una decisión específica en Diseño. Si una decisión de Diseño no tiene fuente en Discovery, hay 2 opciones:
1. Volver a Discovery a confirmar
2. Marcar la decisión como "supuesto AUREA" y validar con el cliente

Este documento sistematiza esos puentes para que ningún hallazgo se pierda.

---

## Mapa maestro de trazabilidad

| Hallazgo de Etapa 1 | Patrón en Etapa 2 | Sección del DOCX/Prompt impactada |
|---|---|---|
| Cliente menciona N procesos distintos (venta, soporte, FAQ, etc.) | N embudos + variable router `proceso_actual` | Sección Embudos · Variables |
| Cliente tiene catálogo en Tokko/PrestaShop/sitio externo | Modalidad B o C — NO hardcodear productos | Sección 5 del prompt · Variables hardcodeadas |
| Cliente menciona urgencia 24/7 en algún tipo de caso | Variable `severidad_caso` + seguimiento avanzado de tiempo cero | Variables operativas · Reglas de Distribución |
| Cliente trabaja con intermediarios (arquitectos, inmobiliarias, aplicadores) | Canal B2B en sección 4 del prompt + variable `tipo_usuario` | Roles del agente · Variables transversales |
| Cliente tiene tipologías muy distintas | Tipología macro cambia según rubro | Sección 4 del prompt · Smart Tags |
| Cliente menciona terminología técnica crítica del rubro | Hardcodear desambiguación en prompt | Sección 2 del prompt (Tono y voz) |
| Cliente tiene equipo de 2+ personas para atender leads derivados | Tabla de routing por `tipo_derivacion` | Sección Reglas de Distribución |
| Cliente menciona objeciones recurrentes | Set de objeciones en sección 11 del prompt | Sección 11 del prompt (Objeciones) |
| Cliente tiene plantillas Meta WhatsApp para outbound | Mensajes de follow-up post-24hs usan plantillas | Seguimientos · Guía de Implementador |
| Cliente menciona showroom / oficina física | Showroom como punto de conversión en sección 7 | Sección 7 del prompt (Conversión) |
| Cliente menciona casos específicos VIP / urgentes | Regla operativa de prioridad en Reglas de Distribución | Reglas de Distribución |

---

## Trazabilidad por bloque temático

Esta sección detalla cómo se mueve cada tipo de información del Discovery a Etapa 2.

### Bloque A — Identidad y roles del agente

**Qué viene de Etapa 1:**
- Nombre del cliente, marca, tono institucional
- Rubro y modelo de negocio
- Funciones operativas que el agente tiene que cumplir
- Funciones que NO debe cumplir (límites)

**Cómo se traduce en Etapa 2:**

| Hallazgo Discovery | Decisión en Diseño |
|---|---|
| El cliente quiere que el agente venda, califique leads y derive | Roles del agente: Vender + Calificar + Derivar |
| El cliente quiere que el agente responda FAQ pero NO negocie | Roles: sumar Responder FAQ · explicitar NO Negociar en autonomía |
| Tono de marca = formal y técnico | Sección 2 prompt: tono formal, voseo o usted según país |
| El agente tiene nombre propio (Veronica, Martina, Catalina) | Sección 1 prompt: identidad del agente |
| El cliente tiene línea ética explícita (no hacer X) | Sección 3 prompt: límites de autonomía |

### Bloque B — Variables transversales

**Qué viene de Etapa 1:**
- Datos críticos que el cliente quiere capturar de cada lead
- Segmentaciones que el cliente hace hoy manualmente
- Información que el cliente pide siempre al lead

**Cómo se traduce en Etapa 2:**

| Hallazgo Discovery | Decisión en Diseño |
|---|---|
| Cliente segmenta por canal de origen | Variable `canal` (Opciones) |
| Cliente distingue particulares vs B2B vs profesionales | Variable `tipo_usuario` (Opciones con valores rubro-específicos) |
| Cliente segmenta por finalidad (inversión, vivienda, uso propio) | Variable `intencion_principal` o `finalidad` (Opciones) |
| Cliente pregunta presupuesto | Variable `presupuesto` (Precio) |
| Cliente pregunta zona / ubicación | Variable `zona_interes` o `ciudad_zona` (Opciones o Texto según rubro) |

### Bloque C — Smart Tags y derivación

**Qué viene de Etapa 1:**
- Casos donde el agente debe escalar a humano
- Áreas del equipo del cliente (comercial, soporte, postventa, legal)
- Reglas operativas internas (lead VIP, blanqueo, fuera de catálogo)

**Cómo se traduce en Etapa 2:**

| Hallazgo Discovery | Decisión en Diseño |
|---|---|
| Cliente menciona N tipos de caso que se derivan a humano | Variable `tipo_derivacion` con valores rubro-específicos |
| Cliente tiene 1 sola persona que recibe todo | Single point of derivation — Smart Tag `#derivar_a_humano` |
| Cliente tiene equipo dividido por especialidad | Tabla de routing por `tipo_derivacion` |
| Cliente menciona casos críticos 24/7 | Variable `severidad_caso` con valor "alta" + seguimiento de tiempo cero |

### Bloque D — Embudos y procesos

**Qué viene de Etapa 1:**
- Procesos que el cliente atiende hoy (venta, soporte, FAQ, postventa, etc.)
- Cuántos canales de entrada tiene (WhatsApp, Instagram, Mail, Web, Portales)
- Volumen estimado de consultas por proceso

**Cómo se traduce en Etapa 2:**

| Hallazgo Discovery | Decisión en Diseño |
|---|---|
| Cliente menciona 1 proceso principal | 1 embudo · variable router opcional |
| Cliente menciona 3-5 procesos paralelos | 3-5 embudos + variable router `proceso_actual` obligatoria |
| Un proceso tiene 80%+ del volumen | Ese embudo es el "principal", recibe más follow-ups |
| Hay procesos con bajo volumen pero alta criticidad | Embudo dedicado con derivación rápida (no perderlo en el principal) |

### Bloque E — Seguimientos

**Qué viene de Etapa 1:**
- En qué momento del proceso se pierden leads hoy
- Cuándo el equipo del cliente hace follow-up manual
- Cuándo el lead "se enfría" según el cliente

**Cómo se traduce en Etapa 2:**

| Hallazgo Discovery | Decisión en Diseño |
|---|---|
| Cliente menciona que pierde leads a las 24hs sin respuesta | Follow-up 1 = 24hs después del estado X |
| Cliente menciona que después de 72hs ya está perdido | Follow-up final = 72hs |
| Cliente menciona reactivación de leads fríos a la semana | Follow-up adicional a los 7 días con tono diferente |
| Cliente tiene proceso de visita / showroom con día específico | Follow-up de confirmación 1 día antes a las 17hs |

### Bloque F — Tono y voz

**Qué viene de Etapa 1:**
- Conversaciones reales del cliente con leads (capturas WhatsApp)
- Manual de marca o lineamientos comunicacionales
- Frases típicas del equipo del cliente

**Cómo se traduce en Etapa 2:**

| Hallazgo Discovery | Decisión en Diseño |
|---|---|
| Cliente usa "usted" formal | Tono formal en sección 2 del prompt · "usted" en mensajes |
| Cliente usa voseo rioplatense | Tono cercano profesional · voseo en mensajes |
| Cliente no usa emojis | Sin emojis en mensajes del agente |
| Cliente tiene terminología técnica diferenciadora | Hardcodear glosario en sección 2 · forbidden words si aplica |
| Cliente menciona objeciones recurrentes con respuestas fijas | Sección 11 del prompt: objeciones con respuestas literales |

---

## Patrones que solo se descubren en Etapa 2 (retroalimentación a Etapa 1)

Hay cosas que solo emergen al diseñar y deberían volver a Etapa 1 como preguntas estándar para futuros clientes.

### Hallazgo retro 1 — Embudos múltiples requieren pregunta explícita en Discovery

**Antes:** asumíamos que el cliente tenía 1 o 2 procesos.

**Después:** descubrimos en MIA que hay clientes con 5 procesos paralelos. Si no preguntás explícitamente en Discovery "¿cuántos procesos paralelos atiende tu equipo?", llegás a Etapa 2 sin datos para modelar bien los embudos.

**Acción:** sumar a Etapa 1 la pregunta:
- "¿Cuántos tipos de consultas distintas reciben? Ej: ventas, soporte técnico, postventa, FAQ, partnership, otros."

### Hallazgo retro 2 — Modalidad de catálogo requiere identificación temprana

**Antes:** decidíamos modalidad A/B/C en Etapa 2.

**Después:** descubrimos que esa decisión cambia mucho la carga de trabajo de Etapa 2. Conviene tomarla en Etapa 1.

**Acción:** sumar a Etapa 1 la pregunta:
- "¿El catálogo de productos/servicios está en una plataforma (Tokko, PrestaShop, sitio web)? ¿O viven solo en el prompt del agente?"

### Hallazgo retro 3 — Casos de urgencia 24/7 son frecuentes pero ocultos

**Antes:** asumíamos que el cliente no tenía urgencias 24/7.

**Después:** descubrimos en MIA que hay apps que sí tienen casos críticos (bug crítico, fraude). En desarrollistas también aparece (lead VIP en fin de semana). En desarrollistas inmobiliarios aparece con leads VIP.

**Acción:** sumar a Etapa 1 la pregunta:
- "¿Tienen algún tipo de caso que requiera respuesta humana fuera de horario laboral? Ej: error crítico, seguridad, lead VIP."

### Hallazgo retro 4 — La franja horaria de follow-ups es decisión por cliente

**Antes:** asumíamos "L-V 10-18hs" como default.

**Después:** descubrimos que cada cliente tiene su franja según cuándo responden sus leads. EDFAN RE midió que responden mejor 18-21hs.

**Acción:** sumar a Etapa 1 la pregunta:
- "¿Tienen registrado en qué horarios responden mejor sus leads? Ej: en horario laboral, después del trabajo, fines de semana."

### Hallazgo retro 5 — Terminología técnica del rubro requiere validación

**Antes:** asumíamos que "lo que dice la web del cliente" era suficiente.

**Después:** descubrimos que hay rubros con terminología ambigua (revestimientos continuos: microcemento ≠ cemento alisado ≠ hormigón pulido) que el agente tiene que poder desambiguar.

**Acción:** sumar a Etapa 1 la pregunta:
- "¿Hay términos técnicos de tu rubro que los clientes confunden? ¿Cómo desambiguás vos cuando un lead usa una palabra ambigua?"

---

## Cómo registrar nuevos puentes Etapa 1 → Etapa 2

Cada vez que descubras un hallazgo nuevo que cruza ambas etapas:

1. Sumalo a la tabla maestra de este documento
2. Si genera una pregunta nueva para Etapa 1, sumarla a `02-etapa1-discovery/` (cuando se complete el manual de Etapa 1)
3. Si modifica un patrón existente, marcarlo con fecha de actualización

---

## Plantilla para documentar un nuevo puente

```markdown
### Puente N — [Nombre descriptivo]

**Hallazgo Discovery:** [qué descubrís en Etapa 1]
**Cliente donde apareció:** [nombre]
**Fecha:** [mes año]
**Patrón en Diseño:** [cómo se traduce en Etapa 2]
**Impacto:** [qué sección del DOCX/Prompt/Guía se modifica]
**Acción de retroalimentación a Etapa 1:** [si aplica, qué pregunta nueva sumar]
```

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Operativa de Etapa 2 (cómo se ejecuta) | `01-operativa-y-decisiones.md` |
| Reglas Diseño de Prometheo by AUREA (las reglas) | `03-reglas-diseno-prometheo-by-aurea.md` |
| Discovery (Etapa 1) | `../02-etapa1-discovery/` (pendiente de documentar) |
| Patrones por rubro | `../05-rubros/[rubro].md` |
