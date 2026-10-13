---
name: prometheo-vertical-real-estate
description: >
  Skill vertical para clientes de Prometheo del rubro desarrollista inmobiliario (desarrolladores,
  constructoras con proyectos propios, desarrollos residenciales/comerciales). Usar SIEMPRE junto
  con prometheo-discovery-transversal y después de la auditoría web (Paso 0). Llena slots
  verticales: tipología macro (proyecto/desarrollo), variables por proyecto, Smart Tags,
  calificación inversores vs vivienda, canal B2B inmobiliarias, Tokko como CRM, reventa,
  financiación, renta de proyecto, routing por zona, seguimientos por etapa de obra.
  Cada regla marcada [FIJA] o [FLEXIBLE]. Caso de referencia: G&D Developers.
  Activar cuando el cliente sea: desarrollista, desarrollador inmobiliario, constructora con
  proyectos propios, emprendimientos inmobiliarios, real estate developer, o cuando Valentín
  mencione "vertical real estate", "desarrollista", "proyectos en pozo", "Tokko".
---

# SKILL VERTICAL: DESARROLLISTA INMOBILIARIO / REAL ESTATE

## ACOPLE
Con `prometheo-discovery-transversal` + skill auditoría web. Primero leer transversal.

## MARCADO
**[FIJA]** = no cambia entre clientes del rubro. **[FLEXIBLE]** = varía, incluye pregunta de discovery.

---

## SECCIÓN 1 — PERFIL DEL RUBRO

### Tipología macro: EL PROYECTO / DESARROLLO
[FIJA] Cada proyecto tiene su propia identidad, público, pricing y disponibilidad. El CRM se organiza primero por proyecto. A diferencia de mobiliario (por línea de producto) o construcción (por categoría de material), acá el eje es el proyecto/desarrollo.

### Características definitorias
1. [FIJA] **Venta high-ticket, ciclo largo.** El ticket es alto (decenas/cientos de miles de USD). El ciclo de decisión puede ser de semanas a meses. El agente califica y lleva a visita, no cierra.
2. [FIJA] **Inversores vs vivienda propia.** Son dos perfiles con criterios de calificación distintos. El inversor pregunta por rentabilidad, el usuario final por amenities y fecha de entrega. Preguntar siempre el porcentaje de cada uno.
3. [FIJA] **Estados de obra.** En pozo, en construcción, entrega inmediata, escritura directa. El estado define el precio, el riesgo percibido y el perfil del comprador.
4. [FLEXIBLE] **Tokko como CRM.** Muchos desarrollistas usan Tokko. Lo que está en Tokko NO se hardcodea en el prompt. Lo que NO está en Tokko SÍ (financiación, perfil ideal, amenities, fecha entrega). Pregunta: "¿Usan Tokko? ¿Qué tienen cargado ahí?"
5. [FLEXIBLE] **Reventa.** Algunos desarrollistas hacen reventa de unidades ya vendidas. Tiene un flujo distinto. Pregunta: "¿Hacen reventa? ¿Cuál es el proceso?"
6. [FLEXIBLE] **Renta de proyecto.** Algunos ofrecen renta garantizada al comprador (ej: USD 300/mes hasta entrega). Pregunta: "¿Ofrecen renta? ¿En qué proyectos? ¿Condiciones?"
7. [FLEXIBLE] **Frecuencia de actualización de precios.** Puede ser diaria, semanal o mensual. Si es diaria, impacta fuertemente en la autonomía del agente. Pregunta: "¿Con qué frecuencia actualizan precios?"
8. [FIJA] **La visita a la obra/showroom es el objetivo de conversión.** El agente busca agendar visita. Todo el flujo apunta ahí.
9. [FIJA] **Canal B2B con inmobiliarias.** Las inmobiliarias/brokers son canal importante. Tienen flujo, terminología y condiciones distintas. Activar B2B siempre.

---

## SECCIÓN 2 — SLOTS POR BLOQUE

### B0 — Equipo
Preguntas rubro: ¿Cuántos vendedores? ¿Se reparten por zona, por proyecto o por turno? ¿Quién supervisa? ¿Sin comisión o con comisión? ¿Todos quieren ver todas las ventas? ¿Van a centralizar WA?
[FLEXIBLE] Routing: por zona (ej: G&D: Sur→Celeste, Norte→Kevin/Fernanda), por proyecto, por tipo de lead, o rotativo.

### B1 — Objetivo y dolor
Dolores típicos: "Consultas poco calificadas de la agencia", "Duplicación entre canales", "Tokko inconsistente, no siempre cargan", "Seguimiento tedioso", "No priorizamos bien las oportunidades", "Cada vendedor con su WA, no centralizamos".

### B2 — Catálogo / Proyectos
[FIJA] Tipología: cada proyecto es una entidad con identidad propia.
Preguntas rubro:
- ¿Cuántos proyectos activos? ¿Cuáles aparecen en la web?
- Por cada proyecto: zona/barrio, estado de obra, tipos de unidad, perfil ideal de comprador, preguntas puntuales que reciben, financiación específica
- ¿Hacen reventa? ¿Cuál es el flujo?
- ¿Ofrecen renta de proyecto? ¿En cuáles? ¿Condiciones?
- ¿Qué hay en Tokko vs qué no? (financiación, perfil ideal, amenities, fecha entrega casi nunca están en Tokko)
- ¿Cuántos proyectos para MVP? (recomendación: 2-3 para arrancar)
[FLEXIBLE] Sistema: Tokko (lo más común), otro CRM, o nada. Pregunta: "¿Usan Tokko? ¿Qué tienen cargado?"

### B3 — Calificación
[FIJA] Tipos contacto: comprador final (vivienda), inversor, inmobiliaria/broker.
[FIJA] Calificación diferenciada:
- **Uso propio:** presupuesto, ubicación, fecha entrega deseada, etapa de desarrollo buscada.
- **Inversión:** los mismos + zona de mayor rentabilidad, objetivo (renta, reventa, diversificación patrimonial).
[FLEXIBLE] % inversores vs vivienda: varía mucho (G&D: 80/20). Pregunta: "¿Qué porcentaje son inversores vs vivienda propia?"
[FLEXIBLE] Señales de hot lead: presupuesto definido, pregunta disponibilidad específica, pide visita, menciona plazo, pregunta financiación. Variables de negociación (ej G&D: hasta 30% anticipo negociable). Pregunta: "¿Qué señales indican que un lead va en serio?"
[FLEXIBLE] Presupuesto mínimo: definir con la lista de precios (la propiedad más barata). Pregunta: "¿Cuánto sale la propiedad más barata hoy?"

### B4 — FAQs y objeciones
[FIJA] FAQs típicas: ¿Qué disponibilidad tiene esta obra? ¿Cuánto sale / valor m2? ¿En qué zonas tienen proyectos? ¿Qué tiene más rentabilidad? Tengo presupuesto X ¿qué tienen? ¿Cuotas/financiación?
[FLEXIBLE] Objeciones (manejo varía):
- **Precio/m2 alto:** argumentar trayectoria, calidad, ubicación, rentabilidad. Pregunta.
- **Plazo de entrega largo:** ofrecer entrega inmediata si tienen, o argumentar ventaja de compra en pozo. Pregunta.
- **No conocen la empresa:** trayectoria (+40 años G&D, Top 10, etc.). Pregunta.
- **Viendo otras opciones:** diferencial vs competencia. Pregunta.
- **Ubicación:** redirigir a otros proyectos en otra zona. Pregunta.

### B5 — Flujo y conversión
[FIJA] Objetivo agente: **llevar a la visita** (obra, showroom, oficina, o virtual). La visita es el evento de conversión. El agente no cierra, no negocia.
[FLEXIBLE] Tipos de visita: física a obra, showroom, oficina, videollamada. Cada tipo tiene su protocolo. Pregunta: "¿Qué tipos de visita hacen? ¿Horarios? ¿Anticipación?"
[FLEXIBLE] Frecuencia de visitas: G&D = 3-6/semana. Pregunta: "¿Cuántas visitas por semana hacen hoy?"
[FIJA] Recomendación: Google Calendar + Meet en vez de Calendly (integra nativamente con Prometheo).

### B6 — Tono
[FLEXIBLE] Suele ser formal pero accesible ("formales como pares"). Pregunta adjetivos, voseo/tuteo, emojis moderados. Particularidad del rubro: cuidado con "barato" (usar "económico"), no negociar precios en la conversación.

### B7 — Canales
[FLEXIBLE] WA suele ser principal. IG importante por contenido de renders/avances. ZonaProp/portales generan leads. Mail para listas de precios a inmobiliarias. Pregunta: "¿Van a centralizar WA en un número?" (prerrequisito para Prometheo).

### B8 — Autonomía
[FIJA] Preguntas críticas del rubro:
- ¿Puede pasar listas de precios? (G&D: sí, basarse en listas)
- ¿Puede mencionar financiación? (cuotas + anticipo OK, negociación se deriva)
- ¿Puede informar sobre renta de proyecto?
- ¿Puede dar valores de m2?
- ¿Los precios cambian diario? → evaluar si hardcodear o referir a lista
[FIJA] Prohibiciones absolutas: negociar precios/descuentos, prometer plazos no confirmados, hablar de cláusulas de boleto, comparar rentabilidad con números concretos (solo conceptual), dar precios exactos si se actualizan diario (solo rangos si autorizado).
[FLEXIBLE] Boleto: siempre lo gestiona el equipo humano. Pregunta: "¿El boleto lo hacen ustedes?"
[FLEXIBLE] Reclamos post-venta: derivar. Pregunta: "¿A quién? ¿Con qué datos?"

### B9 — Contenidos
[FLEXIBLE] Típicos: brochures por proyecto (PDF), renders, avances de obra (c/2 meses), lista de precios (actualización frecuente), planos de unidades tipo, videos/recorridos virtuales.
[FIJA] Regla lista de precios: si se actualiza diariamente, NO adjuntar como archivo fijo al agente (queda vieja). Evaluar integración con Tokko o referencia a la lista vigente.
[FIJA] Material distinto para inmobiliarias vs compradores. Preguntar qué envían a cada segmento.

### B2B — Inmobiliarias
[FIJA] Las inmobiliarias son canal crítico en real estate. Siempre activar este bloque.
- Se presentan como inmobiliarias (identificación fácil)
- Reciben lista de precios semanal
- Pueden pedir visita con su cliente
- Flujo diferenciado: en MVP derivar automáticamente. En Fase 2 pulir flujo propio.
[FLEXIBLE] ¿Tienen lista de precios diferenciada para inmobiliarias? ¿Comisión? ¿Condiciones especiales? Pregunta.

---

## SECCIÓN 3 — FINANCIACIÓN Y CONDICIONES COMERCIALES

[FIJA] Esta sección es propia de real estate. La financiación es parte de la conversación de venta y el agente necesita manejarla.

### Preguntas discovery
- [FLEXIBLE] ¿Qué esquemas de financiación ofrecen? (cuotas + anticipo, pozo + cuotas, contado, permuta). Varía por proyecto.
- [FLEXIBLE] ¿El agente puede mencionar financiación? ¿Hasta qué nivel de detalle? (G&D: cuotas y anticipo OK, negociación se deriva).
- [FLEXIBLE] ¿Hay renta garantizada? ¿En qué proyectos? ¿Condiciones? (G&D: USD 300/mes, contado, precio lista).
- [FLEXIBLE] ¿Ofrecen reventa? ¿Cuál es el flujo?
- [FLEXIBLE] ¿Aceptan permuta?
- [FLEXIBLE] ¿El anticipo mínimo es negociable? ¿Cuánto? (G&D: cobran mín 40%, negocian hasta 30%).

### Variables financiación
| Variable | Tipo | Regla |
|---|---|---|
| Forma de pago | Opciones (contado/financiado/pozo+cuotas/permuta) | [FLEX] Según esquemas del cliente |
| Rango de presupuesto | Precio | [FIJA] |

### Autonomía financiación
[FIJA] El agente puede informar condiciones generales de financiación. Nunca negociar anticipo, descuentos o condiciones especiales.

---

## SECCIÓN 4 — VARIABLES CRÍTICAS

| Variable | Tipo | Regla |
|---|---|---|
| Proyecto de interés | Opciones | [FLEX] Cargar proyectos activos |
| Estado del proyecto | Opciones (pozo/construcción/entrega inmediata/escritura directa) | [FIJA] |
| Tipo de operación | Opciones (venta primaria/reventa) | [FLEX] Solo si hacen reventa |
| Tipo de contacto | Opciones (comprador final/inmobiliaria/profesional) | [FIJA] |
| Finalidad | Opciones (vivienda/inversión con renta/reventa/diversificación) | [FIJA] |
| Tipo de unidad | Opciones (1amb/2amb/3amb/lote/cochera/local) | [FLEX] Según oferta |
| Rango presupuesto | Precio | [FIJA] |
| Forma de pago | Opciones | [FLEX] Según esquemas |
| Zona de interés | Texto | [FIJA] |
| Vendedor asignado | Opciones | [FLEX] Cargar equipo + regla zona |
| Canal de origen | Opciones | [FIJA] Estándar |

---

## SECCIÓN 5 — SMART TAGS

### Intención (verde)
#consulta_inicial, #quiere_visita (→follow-up + notif Pro), #quiere_financiación, #pidió_precio, #pidió_ficha.

### Calificación (azul)
#lead_calificado (→notif Pro, follow-up 4hs), #lead_exploratorio, #inversor, #usuario_final.

### Objeciones (rojo)
#objeción_precio, #objeción_timing, #objeción_ubicación, #objeción_confianza.

### Producto (violeta) — [FLEX]
#proyecto_[nombre] por cada proyecto activo.

### B2B (naranja)
#contacto_inmobiliaria (→apagar asistente en MVP).

### Operativos (gris)
#requiere_humano (→apagar asistente), #no_responde (→reactivación 72hs), #fuera_de_horario.

---

## SECCIÓN 6 — FUNNEL

**Nivel 2 — Oportunidad:**
Consulta → Visita agendada → Visita realizada → Propuesta enviada → Negociación → Reserva → Boleto → Escritura → Cerrada perdida (con motivo)

[FIJA] Agente mueve: Consulta → Visita agendada. Equipo mueve: todo lo demás.
[FIJA] Funnel largo (9 etapas). Es normal por el ticket y el ciclo de decisión.

**Nivel 3 — Estado del proyecto:**
En pozo → En construcción → Entrega inmediata → Escritura directa
[FIJA] Lo actualiza integración (Tokko) o el equipo.

---

## SECCIÓN 7 — SEGUIMIENTOS (fichas)

### Timing del rubro
- Consulta inicial: 24hs (interés tibio, están comparando)
- Lead calificado (pidió visita, presupuesto definido): 4hs
- Post-brochure: 48hs (mandó info, no respondió)
- Lead frío: 72hs
- Inmobiliaria: flujo propio (Fase 2)

### MVP
```
Título: Follow-up lead calificado
Objetivo: Proponer horarios de visita
Tag: #lead_calificado
Canal: WhatsApp
Delay: 4hs
Texto: "Estuvimos viendo tu consulta sobre [proyecto]. ¿Querés que coordinemos una visita para conocer el desarrollo en persona? Te puedo ofrecer [días/horarios]."
Franja: Lun-Vie 9-18, Sáb 10-13
Repeticiones: 1x a las 24hs
Si responde: Sigue IA → si agenda → Variable vendedor según zona
Fase: MVP
Regla: [FIJA]
```

```
Título: Follow-up genérico
Objetivo: Recontactar consultas sin clasificar
Tag: Sin tag
Canal: WhatsApp
Delay: 24hs
Texto: "¡Hola! Ayer nos consultaste por nuestros desarrollos. ¿Pudiste revisar la información? Estoy para ayudarte con cualquier duda."
Franja: Lun-Vie 9-18
Repeticiones: Sin
Si responde: Sigue IA
Fase: MVP
Regla: [FIJA]
```

```
Título: Follow-up post-brochure
Objetivo: Verificar si vio el material y ofrecer ampliar
Tag: #consulta_inicial
Canal: WhatsApp
Delay: 48hs
Texto: "Te había enviado info sobre [proyecto]. ¿Pudiste verla? Si te interesa, puedo contarte más sobre la financiación o coordinar una visita."
Franja: Lun-Vie 9-17
Repeticiones: Sin
Si responde: Sigue IA
Fase: MVP
Regla: [FIJA]
```

```
Título: Reactivación lead frío
Objetivo: Recuperar leads que no respondieron
Tag: #no_responde
Canal: WhatsApp
Delay: 72hs
Texto: "¿Pudiste avanzar con lo que estabas evaluando? Si querés, te cuento las novedades de [proyecto] o coordinamos una visita."
Franja: Lun-Vie 10-17
Repeticiones: Sin
Si responde: Sigue IA
Fase: MVP
Regla: [FIJA]
```

### Fase 2
- Seguimiento por proyecto específico (AND con Variable proyecto)
- Seguimiento inversor con argumento rentabilidad (AND Variable finalidad = inversión)
- Seguimiento inmobiliaria (flujo propio post-MVP)
- Reactivación con novedad de proyecto (avance de obra, nueva disponibilidad)

---

## SECCIÓN 8 — LO QUE NUNCA DEBERÍA HACER EL AGENTE

Todas [FIJA]:
- Negociar precios o descuentos
- Prometer plazos de entrega no confirmados
- Hablar de cláusulas de boleto
- Comparar rentabilidad con números concretos (solo conceptual)
- Dar precios exactos si se actualizan diariamente (solo rangos si autorizado)
- Aprobar condiciones de financiación fuera de las estándar
- Gestionar boleto o reserva
- Reclamos post-venta (derivar con datos)

---

## SECCIÓN 9 — KPI

| KPI | Tag/Variable | Regla |
|---|---|---|
| Respuesta <5 min | Auto Prometheo | [FIJA] |
| Visitas agendadas/semana | #quiere_visita | [FIJA] Métrica principal del rubro |
| Visitas realizadas vs agendadas | Equipo actualiza | [FIJA] |
| % leads calificados | #lead_calificado / total | [FIJA] |
| % inversores vs vivienda | Variable finalidad | [FIJA] |
| Tasa derivación | #requiere_humano | [FIJA] |
| Demanda por proyecto | #proyecto_[X] | [FLEX] |
| Recontacto exitoso | Resp follow-up / enviados | [FIJA] |
| Conversión consulta→visita | #quiere_visita / total | [FIJA] Clave |

---

## SECCIÓN 10 — PREGUNTAS CLAVE PARA DOC 4 (aprobación)

1. ¿Los proyectos activos para el agente son [lista]? ¿Correcto?
2. ¿El agente puede pasar listas de precios y mencionar financiación (cuotas+anticipo)?
3. ¿El objetivo del agente es llevar a la visita?
4. ¿Un lead calificado para inversión es [criterios] y para vivienda es [criterios]?
5. ¿Las inmobiliarias se derivan automáticamente al equipo humano?
6. ¿El routing por zona es: Sur→[nombre], Norte→[nombres]?
7. ¿Los reclamos post-venta se derivan a [persona/proceso]?
8. ¿Arrancamos MVP con [2-3 proyectos]?

---

## SECCIÓN 11 — INSTRUCCIONES CLAUDE

1. [FIJA] Verificar transversal activa.
2. [FIJA] En B2: preguntar por proyecto, no por producto. Cada proyecto es una entidad. Ficha por proyecto.
3. [FIJA] En B3: diferenciar calificación inversores vs vivienda. Preguntar porcentaje.
4. [FIJA] En B5: el objetivo es la visita. Todo el flujo apunta ahí.
5. [FIJA] Regla Tokko: lo que está no se hardcodea. Financiación, perfil ideal, amenities, fecha entrega casi nunca están en Tokko → van en texto en el prompt.
6. [FIJA] B2B con inmobiliarias se activa siempre. En MVP = derivar automáticamente.
7. [FIJA] Precios: si se actualizan diariamente, el agente no da precios exactos. Solo rangos o "basarse en lista vigente".
8. [FIJA] Financiación y renta de proyecto son secciones propias que no existen en otras verticales.
9. [FIJA] Para MVP: arrancar con 2-3 proyectos. No cargar todos desde el inicio.
