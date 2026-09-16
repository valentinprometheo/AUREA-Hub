# 00 — Protocolo para Incorporar un Nuevo Referente

**Cómo destilar un cliente real en un caso de referencia formal.**

---

## Cuándo aplicar este protocolo

Cuando un cliente cumple los 3 criterios:

1. ✅ Etapa 2 cerrada (DOCX y Prompt aprobados)
2. ✅ Mínimo 15 días en producción sin regresiones críticas
3. ✅ Patrón identificable que aporta algo a la metodología

Si falta alguno, esperar antes de sumarlo a la biblioteca.

---

## Proceso de incorporación (5 pasos)

### Paso 1 — Identificar el patrón principal que aporta

Antes de empezar a escribir, respondé esta pregunta:

> "¿Qué tiene este cliente que los referentes existentes NO tienen?"

Ejemplos de patrones únicos:

| Cliente | Patrón único que aporta |
|---|---|
| MIA App | Casos de severidad alta + multi-canal de entrada + variable sistema_operativo |
| BETROX | Showroom como punto de conversión + ciclo largo (1-3 meses) + B2B con arquitectos |
| G&D Developers | Catálogo en Tokko + B2B con inmobiliarias + temas fiscales sensibles |
| EDFAN Productos | PrestaShop + doble dimensión categoría/tipo cliente + B2B aplicadores |

Si no podés identificar un patrón único, **el cliente NO se vuelve referente**. Se queda como cliente normal y la biblioteca no crece.

### Paso 2 — Destilar las variables en 3 capas

Tomá la lista completa de variables del cliente y separalas:

**Capa 1 — Núcleo transversal AUREA:**
Variables que aparecen también en otros clientes (canal, tipo_usuario, intencion_principal, tipo_derivacion, etc.).

**Capa 2 — Por rubro:**
Variables específicas del rubro que se repiten en otros clientes del mismo rubro (ej: en desarrollista: proyecto_interes, zona_interes, tipo_unidad).

**Capa 3 — Del cliente:**
Variables idiosincráticas que solo aplican a este cliente (ej: MIA tiene `sistema_operativo` porque es app móvil).

Documentar cada capa por separado.

### Paso 3 — Identificar decisiones de diseño que se generalizan vs específicas

Recorrer las decisiones tomadas durante Etapa 2 y clasificarlas:

| Tipo de decisión | Ejemplo | Acción |
|---|---|---|
| **Se generaliza al rubro** | "Para desarrollistas, hardcodear horarios de visita" | Sumar al archivo `05-rubros/[rubro].md` |
| **Se generaliza a AUREA** | "Cuando aparece tag X, retirar tag Y manualmente" | Sumar al Reglas Diseño de Prometheo by AUREA |
| **Es específica del cliente** | "G&D atiende también propiedades de Cesarprop (co-comercialización)" | Documentar en el archivo del referente como "Decisiones específicas" |

### Paso 4 — Redactar el archivo del referente

Usar la plantilla del INDEX. Estructura mínima:

```markdown
# Caso de referencia — [Cliente]

**Rubro:** [...]
**Fecha del proyecto:** [...]
**Estado:** Activo
**Reglas Diseño Prometheo aplicadas:** Reglas Diseño de Prometheo by AUREA

## Resumen ejecutivo en 5 líneas

## Variables (3 capas)
### Capa 1 — Núcleo
### Capa 2 — Por rubro
### Capa 3 — Específicas

## Smart Tags
## Embudos
## Patrón principal que aporta
## Decisiones operativas específicas
## Aprendizajes y errores
```

Guardar en `../08-casos-referencia/[CLIENTE].md`.

### Paso 5 — Actualizar la tabla maestra

Sumar el cliente nuevo a `00-INDEX-referentes.md` con:
- Nombre
- Rubro
- Estado: Activo
- Modelo aplicado
- Patrón principal en 1 línea

### Paso 6 — Si aparece un rubro nuevo, crear la skill vertical

Si el cliente es de un rubro que todavía no tiene skill vertical formal:

1. Documentar los patrones del rubro en `01-metodologia/05-rubros/[rubro].md`
2. Cuando haya **2+ clientes del mismo rubro nuevo**, crear la skill formal en `02-skills/00-TRANSVERSAL/`
3. La skill se basa en los patrones comunes a los 2 clientes, no en uno solo

---

## Reglas para mantener calidad de la biblioteca

### Regla 1 — Máximo 1 referente por patrón

Si MIA ya es referente por "casos de severidad 24/7", un cliente nuevo con el mismo patrón NO se vuelve segundo referente. O reemplaza a MIA (si el nuevo es mejor) o se queda como cliente normal.

### Regla 2 — Los referentes envejecen

Cada 6 meses, revisar la biblioteca:
- ¿Hay referentes que ya no están alineados al modelo de reglas vigente?
- ¿Hay patrones que se actualizaron y los referentes están desactualizados?

Si sí, marcar el referente como "histórico" y actualizar la tabla. Mantener el archivo con nota explicativa.

### Regla 3 — Los descartes se documentan

Cuando se descarta un referente (como EDFAN RE con 22 Smart Tags), el archivo SE MANTIENE pero con nota visible al inicio:

```markdown
> ⚠️ ARCHIVO DESCARTADO COMO REFERENTE
> Razón: [explicación]
> Fecha de descarte: [fecha]
> Qué tomar en cuenta: [si hay algo útil que mirar]
```

**Por qué se mantiene:** futuros consultores pueden encontrarlo y necesitan saber por qué NO usarlo.

### Regla 4 — El INDEX se actualiza con cada cambio

Cualquier modificación en la biblioteca (nuevo referente, descarte, cambio de estado) se refleja en `00-INDEX-referentes.md` el mismo día.

---

## Plantilla para evaluar si un cliente se vuelve referente

Antes de incorporarlo, completar esta evaluación:

```markdown
# Evaluación de referente — [Cliente]

## Criterios obligatorios
☐ Etapa 2 cerrada con aprobación cliente
☐ Mínimo 15 días en producción sin regresiones críticas
☐ Patrón identificable que aporta a la metodología

## Patrón único que aporta
[Describir en 2-3 líneas qué tiene este cliente que los referentes
existentes no tienen]

## Comparación con referentes existentes
- ¿Se solapa con [Referente A]? Sí/No · Justificación
- ¿Se solapa con [Referente B]? Sí/No · Justificación

## Decisión
☐ Se incorpora como referente nuevo
☐ Se descarta — patrón ya cubierto por referente existente
☐ Reemplaza a un referente existente (cuál: ___)

## Si se incorpora, próximos pasos
1. Destilar variables en 3 capas
2. Redactar archivo `[CLIENTE].md`
3. Actualizar tabla maestra
4. Si rubro nuevo: crear archivo en `05-rubros/`
```

---

## Cómo se genera valor con la biblioteca

La biblioteca no es un repositorio histórico. Es **input directo para acelerar nuevos proyectos**.

Cuando arrancás un cliente nuevo:

```
1. Mirar el INDEX → ¿qué referente es el más cercano?
   ↓
2. Abrir el archivo del referente
   ↓
3. Tomar de ahí:
   - Variables de Capa 1 (las copiás casi tal cual)
   - Variables de Capa 2 si es del mismo rubro
   - Estructura de embudos típica
   - Patrones de Smart Tags
   - Reglas operativas que se generalizan
   ↓
4. Ajustar al cliente nuevo:
   - Variables de Capa 3 (idiosincráticas)
   - Detalles del rubro si hay particularidades
   ↓
5. Ahorrás 30-50% del tiempo de Etapa 2
```

Sin biblioteca, cada cliente arranca desde cero. Con biblioteca bien mantenida, cada cliente arranca a partir de un caso parecido y solo iterás sobre las diferencias.

---

## Para profundizar

| Tema | Archivo |
|---|---|
| INDEX de referentes | `00-INDEX-referentes.md` |
| Manual operativo de Etapa 2 | `../01-operativa-y-decisiones.md` |
| Reglas Diseño de Prometheo by AUREA | `../03-reglas-diseno-prometheo-by-aurea.md` |
| Patrones por rubro | `../../05-rubros/` |
| Skills verticales | `../../../02-skills/00-TRANSVERSAL/` |
