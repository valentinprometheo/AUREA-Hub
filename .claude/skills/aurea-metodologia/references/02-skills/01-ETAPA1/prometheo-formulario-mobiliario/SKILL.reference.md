---
name: prometheo-formulario-mobiliario
description: >
  Plantilla de formulario de reunión (sincrónico) para clientes de Prometheo del rubro
  mobiliario. Se completa EN VIVO durante la reunión con el cliente. Tiene 3 capas por
  pregunta: rosa (pre-llenado de la auditoría web), naranja (traducción CRM para explicar
  al cliente), azul (respuesta en reunión). Incluye 16 secciones: objetivo, líneas de
  producto, equipo, calificación, FAQs, objeciones, flujo/showroom/personalización,
  autonomía/precios, envío, pago, tono, canales, seguimientos, KPI/baseline, excepciones,
  B2B. Usar SIEMPRE después de ejecutar la skill de auditoría web (Paso 0) y junto con
  la skill transversal y vertical de mobiliario. Activar cuando Valentín pida preparar
  el formulario de reunión, armar la guía de R1, generar el formulario para un cliente
  de mobiliario, o cuando diga "preparar reunión", "formulario", "guía de reunión" para
  un cliente de muebles, equipamiento, decoración, mobiliario urbano o showroom.
---

# SKILL: FORMULARIO DE REUNIÓN — MOBILIARIO

## PROPÓSITO

Generar el formulario que el consultor completa EN VIVO durante la reunión 1 con un cliente de mobiliario. No es un formulario asincrónico que el cliente completa solo — es una guía de reunión con campos de captura.

## CUÁNDO USARLA

Después de ejecutar la skill de auditoría web (Paso 0). El Doc 0 de la auditoría alimenta los bloques "De la web:" de este formulario. Sin Doc 0, las capas rosas quedan vacías y se pierde la ventaja de preguntas cerradas.

## CÓMO FUNCIONA

### 3 capas por pregunta

Cada pregunta del formulario tiene 3 capas visibles:

**🔍 Rosa / "De la web"** — Pre-llenado por el Skill 1 (auditoría web+IG). Son datos que ya conocemos. El consultor los valida con el cliente en vivo: "Vi esto en la web, ¿es correcto?" No hay que descubrir, solo confirmar o corregir.

**🟠 Naranja / "Nota interna AUREA"** — Traducción CRM. Explica qué Variable, Smart Tag o sección del prompt alimenta este dato. El consultor la usa para explicarle al cliente el valor de lo que se le pregunta: "Esto lo pregunto porque después el agente va a poder [X]."

**🔵 Azul / "Respuesta en reunión"** — Campo donde el consultor captura la respuesta real del cliente en vivo.

### Convenciones UX/UI adicionales
- **Texto en gris** = A FUTURO = post-lanzamiento, no se trabaja ahora
- **"¿Esta información es correcta? Sí / No"** = al final de cada sección
- **"Si algo no es correcto o falta información, editen directamente"** = al final de cada sección

## ESTRUCTURA (16 secciones + cierre)

| # | Sección | Bloque | Tiempo | Qué releva |
|---|---|---|---|---|
| 1 | Objetivo y dolor | B1 | 10 min | Qué lograr en 60-90 días, dolor principal |
| 2 | Líneas de producto | B2 | 15 min | Líneas, ticket, plazo, estándar/config/medida, personalización, cross-sell, ERP/e-commerce |
| 3 | Equipo y roles | B0 | 5 min | Quién vende, quién cotiza, quién cierra, routing |
| 4 | Calificación de leads | B3 | 15 min | Tipos cliente, criterios calificado, señales, mínimos, conversión |
| 5 | FAQs e insights | B4 | 10 min | Top preguntas + insight clave de cada respuesta |
| 6 | Objeciones | B4 | 10 min | Top objeciones + manejo + Smart Tag que genera |
| 7 | Flujo, showroom, personalización | B5 | 10 min | Objetivo agente, fichas de visita, proceso personalización por etapas |
| 8 | Autonomía y derivación | B8 | 10 min | ⚠️ PRECIOS, capacidades agente, derivación, frase escalamiento |
| 9 | Envío y logística | B5+vert | 5 min | Flota, flete, zonas, colocación, retiro |
| 10 | Métodos y formas de pago | B8+vert | 5 min | Métodos, seña/saldo, índice CAC, condiciones profesionales |
| 11 | Tono de voz | B6 | 5 min | Adjetivos, voseo/tuteo, emojis, prohibidas, nombre agente |
| 12 | Canales y marketing | B7 | 5 min | Canales activos, volumen, pauta, API/QR, plan Prometheo |
| 13 | Seguimientos | B5 | 10 min | 7 puntos del negocio, seguimientos manuales actuales |
| 14 | KPI y baseline | B10 | 5 min | 5 métricas core Prometheo (antes) + métricas rubro |
| 15 | Excepciones | B11 | 5 min | VIP, IA, promos, outlet, sorteos, prohibiciones |
| 16 | B2B / profesionales | B2B | 5 min | Arquitectos, condiciones, terminología, flujo |
| — | Cierre | — | 5 min | Resumen, próximos pasos, responsable, materiales pendientes |

**Tiempo total estimado: 90 minutos**

## INSTRUCCIONES PARA CLAUDE

### Al generar el formulario para un cliente:

1. Leer el Doc 0 (auditoría web) del cliente.
2. Leer la plantilla base en `references/plantilla.md`.
3. Para cada sección, llenar los bloques "🔍 De la web:" con los datos del Doc 0.
4. Adaptar las tablas y opciones a las particularidades del cliente (ej: si la auditoría detectó 4 líneas, poner 4 filas en la tabla de S2).
5. Si el Doc 0 detectó hipótesis de tipología macro, pre-llenar la sección 2 con esa hipótesis.
6. Si la web tiene FAQ, pre-llenar la sección 5 con esas preguntas.
7. Si la web muestra precios, anotar en S8: "La web publica precios → hipótesis: el agente puede dar precios de lista."
8. Si la web tiene e-commerce, anotar plataforma en S2.7 y métodos de pago detectados en S10.
9. Generar el formulario como .md para que sea editable en Google Docs.

### Particularidades de mobiliario que siempre van:

- S2: incluir tabla de personalización (color, medida, material, terminación, combinaciones)
- S7.3: incluir proceso de personalización por etapas con "¿el agente puede?"
- S8.1: distinguir precios estándar vs personalizados
- S9: incluir colocación como pregunta
- S10.2: incluir seña/saldo, índice de actualización (CAC u otro)
- S16: siempre activar B2B (profesionales son relevantes en mobiliario)

### Lo que NO va en este formulario (va en Doc 2 o Doc 3):

- Fichas detalladas por producto con info que no está en sistema → Doc 2
- Accesos a plataformas (usuario, contraseña) → Doc 3
- Material para subir al Drive (brochures, fotos, renders) → Doc 3
- Capturas de WA reales → Doc 3 (se piden en S11 pero se suben al Drive)

## CONEXIÓN CON EL SISTEMA

```
Skill 1 (auditoría web) → genera Doc 0
                              ↓
Doc 0 → pre-llena bloques rosas de esta plantilla
                              ↓
Esta skill → genera formulario adaptado al cliente
                              ↓
Consultor llena en reunión → respuestas azules
                              ↓
Post-reunión → skill transversal traduce respuestas → Doc 1 (síntesis)
                              ↓
Lo que falta → Doc 2 (asincrónico) + Doc 3 (accesos/drive)
                              ↓
Todo completo → Doc 4 (aprobación) → Gate → Etapa 2
```
