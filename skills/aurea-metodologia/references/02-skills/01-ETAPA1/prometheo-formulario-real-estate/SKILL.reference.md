---
name: prometheo-formulario-real-estate
description: >
  Plantilla de formulario de reunión (sincrónico) para clientes de Prometheo del rubro
  desarrollista inmobiliario / real estate. Se completa EN VIVO durante la reunión con el
  cliente. Tiene 3 capas por pregunta: rosa (pre-llenado de la auditoría web), naranja
  (traducción CRM para explicar al cliente), azul (respuesta en reunión). Incluye 16
  secciones: objetivo, proyectos/desarrollos, equipo, calificación inversores vs vivienda,
  FAQs, objeciones, flujo/visitas, autonomía/precios/financiación, renta de proyecto,
  reventa, tono, canales, seguimientos, KPI/baseline, excepciones, B2B inmobiliarias.
  Usar SIEMPRE después de ejecutar la skill de auditoría web (Paso 0) y junto con la skill
  transversal y vertical de real estate. Activar cuando Valentín pida preparar el formulario
  de reunión, armar la guía de R1, generar el formulario para un desarrollista inmobiliario,
  o cuando diga "preparar reunión", "formulario", "guía de reunión" para un cliente de
  desarrollos, emprendimientos, proyectos en pozo, real estate.
---

# SKILL: FORMULARIO DE REUNIÓN — REAL ESTATE / DESARROLLISTA INMOBILIARIO

## PROPÓSITO

Generar el formulario que el consultor completa EN VIVO durante la reunión 1 con un cliente desarrollista inmobiliario. Es una guía de reunión con campos de captura, no un formulario asincrónico.

## CUÁNDO USARLA

Después de ejecutar la skill de auditoría web (Paso 0). El Doc 0 alimenta los bloques "De la web:". Sin Doc 0, las capas rosas quedan vacías.

## CÓMO FUNCIONA

3 capas por pregunta (ver skill transversal para detalle completo):
- 🔍 **Rosa** = pre-llenado de la web. Validar, no descubrir.
- 🟠 **Naranja** = traducción CRM. Para explicar al cliente.
- 🔵 **Azul** = respuesta en reunión. Completar en vivo.

Convenciones UX/UI: azul/naranja/gris, Sí/No por sección, "editen directamente".

## ESTRUCTURA (16 secciones + cierre)

| # | Sección | Bloque | Tiempo | Qué releva |
|---|---|---|---|---|
| 1 | Objetivo y dolor | B1 | 10 min | Qué lograr, dolor principal |
| 2 | Proyectos / desarrollos | B2 | 15 min | Ficha por proyecto, estado obra, Tokko, perfil ideal |
| 3 | Equipo y roles | B0 | 5 min | Quién vende, routing por zona |
| 4 | Calificación inversores vs vivienda | B3 | 15 min | Criterios diferenciados, %, presupuesto mínimo |
| 5 | FAQs e insights | B4 | 10 min | Top preguntas + insight diferencial |
| 6 | Objeciones | B4 | 10 min | Precio/m2, plazo, confianza, ubicación |
| 7 | Flujo, visitas y conversión | B5 | 10 min | Tipos de visita, horarios, GCal, objetivo agente |
| 8 | Autonomía, precios y financiación | B8 | 10 min | ⚠️ PRECIOS, listas, financiación, renta, boleto |
| 9 | Renta de proyecto | B8+vert | 5 min | En qué proyectos, condiciones |
| 10 | Reventa | B2+vert | 5 min | Flujo, pricing, derivación |
| 11 | Tono de voz | B6 | 5 min | Formal/cercano, nombre agente |
| 12 | Canales y marketing | B7 | 5 min | WA centralizado, IG, portales, pauta |
| 13 | Seguimientos | B5 | 5 min | 7 puntos, follow-ups actuales |
| 14 | KPI y baseline | B10 | 5 min | 5 métricas core + visitas/semana |
| 15 | Excepciones | B11 | 5 min | VIP/referidos, IA, campañas |
| 16 | B2B / inmobiliarias | B2B | 5 min | Derivación, lista precios, flujo |
| — | Cierre | — | 5 min | Resumen, próximos pasos |

**Tiempo total estimado: 90 minutos**

## PARTICULARIDADES DE REAL ESTATE QUE SIEMPRE VAN

- S2: fichas POR PROYECTO (no por línea de producto). Campos: zona, estado obra, tipos unidad, perfil ideal, preguntas puntuales, financiación específica, info que NO está en Tokko.
- S4: calificación DIFERENCIADA inversores vs vivienda propia. Preguntar porcentaje de cada uno.
- S8: distinguir "puede pasar lista de precios" de "puede dar precio exacto". Financiación (cuotas+anticipo) como sub-bloque. Pregunta de boleto.
- S9: renta de proyecto como sección propia (no existe en otras verticales).
- S10: reventa como sección propia (no existe en otras verticales).
- S16: inmobiliarias siempre se activan. En MVP = derivar automáticamente.

## LO QUE NO VA EN ESTE FORMULARIO

- Info detallada por proyecto que no está en Tokko → Doc 2 (fichas por proyecto)
- Accesos a Tokko, Meta Business, hosting → Doc 3
- Brochures, renders, planos, avances de obra → Doc 3 (subir al Drive)
- Lista de precios ejemplo → Doc 3

## INSTRUCCIONES PARA CLAUDE

### Al generar el formulario para un cliente:

1. Leer Doc 0 (auditoría web) del cliente.
2. Leer la plantilla base en `references/plantilla.md`.
3. Llenar bloques "🔍 De la web:" con datos del Doc 0.
4. Adaptar cantidad de fichas de proyecto a lo detectado en la web.
5. Si la web muestra proyectos con precios → anotar en S8.
6. Si la web tiene ZonaProp/portales → anotar en S12.
7. Si la web menciona inmobiliarias como canal → anotar en S16.
8. Generar como .md editable.

### Conexión con el sistema

```
Skill 1 (auditoría web) → Doc 0
    ↓
Doc 0 → pre-llena bloques rosas
    ↓
Esta skill → formulario adaptado al cliente
    ↓
Consultor llena en reunión → respuestas azules
    ↓
Post-reunión → transversal traduce → Doc 1 (síntesis)
    ↓
Lo que falta → Doc 2 (fichas proyecto) + Doc 3 (accesos/Tokko/Drive)
    ↓
Todo completo → Doc 4 (aprobación) → Gate → Etapa 2
```
