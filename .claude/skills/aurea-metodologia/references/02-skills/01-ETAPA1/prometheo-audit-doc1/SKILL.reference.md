---
name: prometheo-audit-doc1
description: >
  Skill de control de calidad para auditar si la información del formulario de discovery 
  (guía de reunión rellenada) fue transferida correcta y completamente al Doc 1 de Síntesis.
  Usar SIEMPRE después de generar un Doc 1. Compara dato por dato entre el documento fuente
  (formulario/guía rellenada) y el Doc 1 output. Genera un reporte de auditoría con estado
  por dato: ✅ transferido / ⚠️ parcial / ❌ faltante. Activar cuando Valentín diga "auditar",
  "control de calidad", "cotejar", "verificar doc 1", "se pasó todo?", "falta algo?",
  "revisar completitud", o cualquier pedido de validación de que la info se pasó correctamente
  del formulario al Doc 1.
---

# SKILL: AUDITORÍA DOC 1 — CONTROL DE CALIDAD

## PROPÓSITO
Verificar que ABSOLUTAMENTE TODA la información relevada en el formulario de discovery
(guía de reunión rellenada, pre-works, notas, documentos complementarios) fue transferida
correcta y completamente al Doc 1 de Síntesis. Ningún dato puede perderse en la traducción.

## CUÁNDO EJECUTAR
- Después de generar o actualizar un Doc 1
- Cuando Valentín pida cotejar, verificar o auditar
- Antes de enviar el Doc 1 al cliente para aprobación

## PROCESO DE AUDITORÍA

### Paso 1 — Extracción del documento fuente
Leer el documento fuente completo (formulario rellenado, HTML exportado de Google Docs, 
o cualquier formato). Extraer CADA pieza de información que el cliente proporcionó:

**Qué contar como "dato del cliente":**
- Respuestas directas a preguntas (incluso parciales)
- Notas tomadas durante la reunión
- INSIGHTs escritos por el consultor durante la charla
- Aclaraciones del cliente
- Datos implícitos (ej: nombres mencionados al pasar)
- Decisiones tomadas ("OPTAMOS POR ESTE")
- Correcciones o matices ("no exactamente, sino...")
- Info de documentos complementarios (tono de voz, accesos, etc.)

**Qué NO contar:**
- Preguntas sin responder (marcadas ☐ ASYNC sin respuesta)
- Texto del formulario template (las preguntas originales)
- Instrucciones del consultor (leyenda, agenda, tips)

### Paso 2 — Clasificación por bloque
Organizar cada dato extraído por bloque temático (los bloques del Discovery (ver estructura-discovery.md)).
Un dato puede pertenecer a más de un bloque si es transversal.

### Paso 3 — Cotejo contra Doc 1
Para cada dato extraído, buscar en el Doc 1 si:
- ✅ **TRANSFERIDO** — El dato aparece en el Doc 1 con su contenido completo y en el bloque correcto.
- ⚠️ **PARCIAL** — El dato aparece pero sintetizado, incompleto, o en un bloque incorrecto.
- ❌ **FALTANTE** — El dato NO aparece en el Doc 1.
- 🔄 **REUBICADO** — El dato fue movido a Doc 2 o Doc 3 (válido si corresponde por la regla anti-duplicación).

### Paso 4 — Reporte de auditoría
Generar un reporte con:

```
AUDITORÍA DOC 1 — [CLIENTE]
Fecha: [fecha]
Documento fuente: [nombre archivo]
Doc 1 auditado: [nombre archivo]

RESUMEN EJECUTIVO
- Total datos identificados: N
- ✅ Transferidos: N (%)
- ⚠️ Parciales: N (%)
- ❌ Faltantes: N (%)
- 🔄 Reubicados (Doc 2/3): N (%)

DETALLE POR BLOQUE

B0 — OBJETIVO Y DOLOR
| # | Dato del fuente | Estado | Ubicación en Doc 1 | Observación |
|---|-----------------|--------|---------------------|-------------|
| 1 | [dato textual]  | ✅/⚠️/❌ | [sección]        | [si parcial o faltante, qué falta] |

[...repetir por bloque...]

DATOS CRÍTICOS FALTANTES (si hay)
[Lista de datos que DEBEN estar y no están]

DATOS SINTETIZADOS QUE PERDIERON DETALLE (si hay)
[Lista de datos que se resumieron perdiendo info]

RECOMENDACIONES
[Qué hacer para completar]
```

## CRITERIOS DE CALIDAD

### Nivel de detalle requerido
- Las respuestas del cliente deben transferirse CON TODO SU DETALLE
- Los sinónimos y ejemplos mencionados deben mantenerse (ej: sinónimos de "Obra en Proyecto")
- Las aclaraciones específicas no se omiten (ej: "en la pregunta de venta de materiales esto NO se hace")
- Los números exactos se mantienen (ej: "+500m²", "mensual y algunos semanales")
- Las subcategorías se mantienen completas (ej: "constructor, diseñador de interiores, arquitectos, independientes, colocadores")

### Excepciones válidas
- Reorganizar la info en un bloque diferente al del formulario ES VÁLIDO si el bloque receptor es más apropiado
- Mover info al Doc 2 o Doc 3 ES VÁLIDO si corresponde por la regla anti-duplicación
- Mejorar la redacción ES VÁLIDO siempre que no se pierda contenido
- Agregar estructura visual (cajas, headers) ES VÁLIDO

### Lo que NO es válido
- Sintetizar perdiendo detalle
- Omitir aclaraciones del cliente
- Cambiar el sentido de lo que dijo el cliente
- Fusionar dos datos distintos en uno perdiendo la distinción
- Omitir INSIGHTs del consultor (son info valiosa)

## FORMATO DE OUTPUT
El reporte se genera como documento .docx con la estética ZATOH (mismas cajas de color):
- ✅ Verde = dato transferido correctamente
- ⚠️ Amarillo = dato parcial, necesita revisión
- ❌ Rojo = dato faltante, acción requerida
- 🔄 Azul = dato reubicado a Doc 2/3

## INSTRUCCIONES PARA CLAUDE

1. Leer COMPLETO el documento fuente — no saltear ninguna línea
2. Leer COMPLETO el Doc 1 a auditar
3. Extraer CADA dato del fuente como ítem individual
4. Cotejar uno por uno contra el Doc 1
5. Ser ESTRICTO: si un dato tiene 5 subcategorías en el fuente y el Doc 1 tiene 4, marcar ⚠️ PARCIAL
6. Los INSIGHTs del consultor cuentan como datos — el fuente los tiene, el Doc 1 los necesita (en naranja)
7. Las preguntas sin respuesta NO se auditan (no hay dato que transferir)
8. Generar el reporte completo con detalle por bloque
