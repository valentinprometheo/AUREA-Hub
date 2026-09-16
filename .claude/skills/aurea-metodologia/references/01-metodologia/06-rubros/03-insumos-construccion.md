---
consultar-cuando: cliente de insumos/materiales para construcción, diseño o iteración de su prompt/CRM
disparadores: "insumos", "materiales de construcción", "revestimientos", "EDFAN Productos", "Paula", "ZATOH", "carpetas", "asesoramiento técnico de obra"
fuente-única-de: lógica comercial del rubro insumos para construcción
combina-con: principios-transversales-agente, integracion correspondiente, 00-sistema-fija-flexible
---

# 03 — Rubro Insumos para Construcción

**Patrones del rubro insumos para construcción.**

> ⚠️ **ESTADO: [VALIDADO PARCIAL]**
> Este archivo se basa en un único cliente fundacional (EDFAN Productos) en Etapa 2 todavía no cerrada. Los patrones son **hipótesis** que se confirman cuando aparezca el segundo cliente del rubro. Mientras tanto, usar como guía orientativa pero esperar variaciones según el próximo cliente.

---

## Definición del rubro

**Aplica a:** clientes que comercializan productos para la construcción y/o aplicación profesional:
- Revestimientos continuos (microcemento, cemento alisado, hormigón pulido)
- Pinturas industriales
- Aditivos para hormigón
- Aislaciones
- Productos de impermeabilización

**Características que parecen definir el rubro:**
- Catálogo con productos técnicos identificables por nombre comercial
- B2B estructural con aplicadores profesionales (estructural, no opcional)
- Manejo de fichas técnicas como activo crítico
- Tono adaptativo según tipo de usuario (técnico vs didáctico)
- Múltiples canales de venta (directo + distribuidores + aplicadores)

**Clientes documentados:** EDFAN Productos (en Etapa 2, prototipo).

---

## Particularidades del rubro (HIPÓTESIS — validar con próximo cliente)

### 1. Tipología macro doble dimensión

A diferencia de otros rubros donde la tipología es una sola variable (proyecto en real-estate, línea en mobiliario), insumos parece tener doble dimensión:

- **Categoría de producto** (microcemento / cemento alisado / aditivo / pintura / etc.)
- **Tipo de cliente** (aplicador / particular / arquitecto / constructora)

Las dos dimensiones juntas definen el flujo del agente y el tono de respuesta.

### 2. B2B con aplicadores como canal estructural

Los aplicadores profesionales son canal estructural (no opcional):
- Compran volumen
- Tienen relación directa con el fabricante
- Esperan trato técnico, no didáctico
- Suelen pedir fichas técnicas detalladas

### 3. Fichas técnicas como activo crítico

Cada producto tiene ficha técnica en PDF con:
- Componentes
- Especificaciones de aplicación
- Rendimiento por m²
- Tiempos de secado
- Cuidados post-aplicación

Estas fichas son inputs críticos del prompt — se cargan como adjuntos al asistente y se envían con "/" cuando el lead las pide o cuando es aplicador.

### 4. Catálogo en PrestaShop (al menos en el cliente fundacional)

EDFAN Productos usa PrestaShop como fuente de stock y precios. Modalidad C (híbrida):
- Estructura general en prompt
- Stock + precios consultados a PrestaShop en runtime
- Fichas técnicas como PDFs adjuntos

### 5. Tono adaptativo según `tipo_usuario`

- Si `tipo_usuario = aplicador / arquitecto / constructora`:
  - Tono técnico
  - Usar terminología precisa
  - Mandar ficha técnica completa
  - Asumir conocimiento del rubro

- Si `tipo_usuario = particular`:
  - Tono didáctico
  - Explicar términos técnicos
  - NO mandar ficha técnica completa (saturación)
  - Foco en uso final + recomendación de aplicador profesional

### 6. Terminología técnica ambigua

El rubro tiene términos que el cliente confunde:
- Microcemento ≠ cemento alisado ≠ hormigón pulido
- Pintura impermeabilizante ≠ membrana líquida ≠ aislación termo-acústica
- Aditivo plastificante ≠ acelerante ≠ retardante

El agente tiene que poder desambiguar preguntando por uso, espesor, ubicación, etc.

---

## Patrones macro HIPOTÉTICOS

### Variables transversales propuestas

| Variable | Tipo | Notas |
|---|---|---|
| `proceso_actual` | Opciones | venta, soporte_aplicacion, faq, derivacion |
| `tipo_usuario` | Opciones | aplicador, particular, arquitecto, constructora |
| `canal` | Opciones | whatsapp, instagram, mail, web, mercadolibre |
| `categoria_producto` | Opciones | microcemento, cemento_alisado, aditivo, pintura, aislacion, otro |
| `intencion_principal` | Opciones | cotizar, asesoramiento_tecnico, comprar_directo, ficha_tecnica |
| `volumen_estimado_m2` | Número | m² para cotización |
| `zona_obra` | Texto | Ubicación de la obra/aplicación |
| `tipo_derivacion` | Opciones | comercial, soporte_tecnico, b2b_volumen, postventa, reclamo |

### Smart Tags

Modelo v7: 2 tags base. Mismo patrón que otros rubros.

### Embudos típicos propuestos

4 embudos:

1. **Venta B2C** (particulares)
2. **Venta B2B** (aplicadores, arquitectos, constructoras)
3. **Soporte técnico de aplicación** (preguntas sobre cómo aplicar productos ya comprados)
4. **FAQ general**

### Seguimientos típicos propuestos

- Follow-up 1: 24hs después de info enviada (B2C)
- Follow-up 2: 3-5 días si no respondió
- Follow-up 1 B2B: 48hs (B2B es más lento)
- Follow-up post-cotización: 7 días
- Follow-up post-compra (si se logra cerrar venta automatizada): 5 días para asistencia técnica

---

## Reglas operativas propuestas

### Regla 1 — Identificar tipo_usuario temprano

El agente tiene que identificar en los primeros 2-3 mensajes si el lead es:
- Aplicador / arquitecto / constructora → tono técnico
- Particular → tono didáctico

Señales:
- "Para una obra que estoy haciendo" → aplicador / arquitecto / constructora
- "Me lo recomendó un albañil" → particular
- "Necesito el rendimiento exacto" → aplicador / arquitecto
- "¿Sirve para mi balcón?" → particular

### Regla 2 — Fichas técnicas según tipo_usuario

- Aplicador / arquitecto / constructora → ficha técnica completa
- Particular → resumen en chat, ficha solo si la pide

### Regla 3 — Desambiguar terminología

Si el lead usa un término ambiguo:
```
Lead: "Quiero alisado de cemento"
Agente: "Para asesorarte mejor, ¿buscás revestimiento decorativo
(microcemento, 2-3mm de espesor) o industrial (cemento alisado,
5-10mm)? ¿Y es para interior o exterior?"
```

### Regla 4 — Volumen estimado para B2B

Cuando se detecta B2B, capturar siempre `volumen_estimado_m2`. Este dato dispara descuentos por volumen y rutea a comercial mayorista.

### Regla 5 — Reclamos siempre se derivan

Si el lead reporta problema con producto ya aplicado, derivar siempre a soporte técnico. NO improvisar respuestas — depende mucho del caso (mala aplicación, mal stock, condiciones ambientales).

### Regla 6 — No prometer rendimientos exactos

Cada producto tiene rendimiento variable según superficie, condiciones, técnica de aplicación. Comunicar siempre como rango ("8-12 m² por kilo dependiendo del soporte").

---

## KPIs típicos del rubro (HIPÓTESIS)

| KPI | Cómo se mide | Target inicial estimado |
|---|---|---|
| % de leads calificados | Leads con tipo_usuario y categoria_producto / Total | 70%+ |
| Tiempo a primera respuesta | Mediana | < 15 minutos |
| % B2B identificados correctamente | B2B clasificados / B2B totales | 85%+ |
| Tasa de derivación correcta a soporte técnico | Derivaciones correctas / Total derivaciones a soporte | 80%+ |
| % de fichas enviadas (B2B) | Fichas enviadas / leads B2B | 90%+ |

---

## Glosario rubro-específico (a expandir)

| Término | Definición |
|---|---|
| Microcemento | Revestimiento continuo de 2-3mm, base cementicia, acabado sedoso |
| Cemento alisado | Revestimiento continuo, espesor 5-10mm, acabado rústico |
| Hormigón pulido | Revestimiento monolítico, 8-12cm, pulido a máquina |
| Aplicador | Profesional que aplica productos en obra |
| Rendimiento | m² que rinde por kilo o litro de producto |
| Tiempo de secado | Período antes de poder usar la superficie |
| Soporte | Superficie donde se aplica el producto |
| Imprimación | Tratamiento previo a la aplicación principal |

---

## Errores frecuentes propuestos (a validar)

| Error | Consecuencia | Solución |
|---|---|---|
| Tratar a aplicador como particular | Aplicador siente que no le hablan en su jerga | Identificar tipo_usuario temprano + tono técnico |
| Mandar ficha técnica completa a particular | Saturación + abandona | Resumen en chat, ficha solo si pide |
| Improvisar respuesta a reclamo | Mala info técnica + reputación | Derivar siempre a soporte técnico |
| Confundir microcemento con cemento alisado | Cotización equivocada | Desambiguar terminología siempre |
| Prometer rendimiento exacto | Cliente se enoja si no cumple | Comunicar como rango |
| No capturar volumen en B2B | Pérdida de oportunidad de descuento por volumen | volumen_estimado_m2 obligatoria en B2B |

---

## Qué validar con el próximo cliente del rubro

Cuando aparezca un segundo cliente de insumos para construcción, validar:

1. ¿La doble dimensión categoría/tipo_usuario aplica? ¿O es solo de EDFAN?
2. ¿Los 4 embudos propuestos son los correctos? ¿Faltan? ¿Sobran?
3. ¿La variable `volumen_estimado_m2` es relevante para todos?
4. ¿La terminología ambigua aparece en otros segmentos del rubro?
5. ¿El patrón de fichas técnicas como adjuntos al asistente se mantiene?
6. ¿PrestaShop es el catálogo estándar del rubro o un caso particular de EDFAN?

Si las respuestas son consistentes con EDFAN, **estos patrones pasan de [VALIDADO PARCIAL] a [VALIDADO]** y la skill vertical puede crearse formalmente.

---

## Integración con catálogo digital (PrestaShop)

En insumos para construcción, PrestaShop es la integración estándar (caso EDFAN, ZATOH, y muy probablemente otros del rubro). Las 6 reglas de integración con catálogo del Reglas Diseño de Prometheo by AUREA (Reglas 16-21) **aplican siempre** en este rubro. Ver `../02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` para el detalle completo.

**Cómo aplicar en insumos construcción:**

| Regla | Aplicación específica al rubro |
|---|---|
| 16 — No bloquear consultas atómicas | El profesional (arquitecto, constructor) pide precio o ficha técnica antes de calificarse. NO trabar. |
| 17 — Búsqueda separada de consulta | Tools `[BUSCAR_PRODUCTO]`, `[CONSULTA_PRECIO]`, `[OBTENER_LINK]`. Especialmente importante porque el lead suele nombrar el producto con jerga ("cemento alisado" puede ser microcemento o hormigón alisado). |
| 18 — Match tolerante | Manejar terminología ambigua: "alisado", "cemento decorativo", "piso continuo" requieren BUSCAR_PRODUCTO con repregunta si hay match múltiple. |
| 19 — URLs PrestaShop son válidas | Las URLs devueltas por la API son canónicas. Las URLs externas (videos de aplicación, fichas técnicas PDF, materiales de marketing) NO van hardcoded — viven en una fuente externa de acceso compartido (Drive, YouTube, Vimeo, Notion, Dropbox, Sheets, etc.) que el cliente elige. **Paso obligatorio en Etapa 2:** preguntar al cliente "¿dónde está documentado el catálogo?", "¿hay URLs externas (videos, PDFs) que el agente vaya a usar?" y "¿en qué fuente las querés tener?" |
| 20 — Naming unificado | Cada producto tiene `clave_interna` que mapea a su SKU en PrestaShop. Tabla de 3 columnas separadas: clave_interna + variantes técnicas (SKU del cliente, nombre comercial) + variantes del lead (jerga ambigua del rubro: "alisado", "cemento", "piso continuo", "concreto pulido"). Las variantes ambiguas se marcan como "requiere repregunta". |
| 21 — Prioridad de respuesta | FAQs técnicas, recomendación por superficie, combinaciones Sistema: hardcoded. Precio, stock, ficha técnica PDF: integración. Cotización a obra: derivar. |

**Productos típicos del rubro que SÍ se consultan en PrestaShop:**
- Productos estándar con precio publicado
- Productos con stock y presentación definida
- Kits armados
- Accesorios y consumibles

**Productos que NO se consultan (derivar a humano):**
- Productos sin precio publicado (figura "consultar")
- Productos para obra grande (cotización por proyecto)
- Productos B2B exclusivos (aplicadores autorizados con precio diferenciado)
- Cotizaciones con descuento por volumen

**Caso de referencia:** el prompt de Paula (EDFAN Productos) tiene una versión preliminar de estas reglas, pero está pendiente de auditoría completa. Ver `PROTOTIPO-edfan-productos.md`.

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Caso de referencia EDFAN Productos | `../08-casos-referencia/PROTOTIPO-edfan-productos.md` |
| Reglas Diseño de Prometheo by AUREA | `../02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` |
| Reglas de integración con catálogo | `../02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` |
| Operativa Etapa 2 | `../02-ETAPA2-Diseno/01-operativa-y-decisiones.md` |

---

## Lógicas comerciales confirmadas (primera evidencia real del rubro — EDFAN Productos / Paula)

> Hasta acá el archivo era hipotético. Esta sección es la PRIMERA evidencia de campo del
> rubro, destilada de la reunión 2 con EDFAN Productos (agente Paula). Lo de abajo deja de
> ser hipótesis y pasa a confirmado. Cuando se sume un segundo cliente del rubro, lo que
> coincida sube a patrón consolidado.

### Dos flujos distintos: asesoramiento vs material

El rubro tiene dos intenciones de entrada que se atienden distinto:

- **Flujo asesoramiento:** el lead pregunta cómo resolver un problema técnico (qué producto
  usa para tal situación, cómo se aplica). El agente asesora desde el conocimiento del oficio.
- **Flujo material:** el lead ya sabe qué quiere y pide precio/disponibilidad/cantidad. El
  agente cotiza o deriva según corresponda.

El agente detecta cuál de los dos flujos es antes de responder: no cotiza cuando el lead pide
asesoramiento, ni asesora de más cuando el lead solo quiere el material.

### Tres tipos de usuario (la calificación del rubro)

La pregunta de calificación central es quién es el lead, porque cambia el lenguaje y la
profundidad de la respuesta:

- **Arquitecto / diseñador:** habla en términos de proyecto, especificación, m². Tolera y
  espera densidad técnica.
- **Constructor / aplicador:** habla en términos de ejecución, rendimiento, cómo se aplica.
- **Cliente final:** habla en términos de resultado, no de producto. Necesita traducción, no
  jerga.

La densidad de la repregunta y el nivel técnico de la respuesta se ajustan al perfil. Es el
mismo principio transversal de "calificar antes de mostrar", aplicado al lenguaje técnico.

### m² antes que zona

En este rubro el dato que dimensiona la consulta es la superficie (m²), no la zona. La
cantidad de material, el rendimiento y la cotización dependen de los m². Por eso se pregunta
m² temprano, antes que la ubicación.

### El cliente asesora pero no necesariamente ejecuta

Caso EDFAN Productos: la empresa asesora sobre carpetas (cómo resolverlas, qué producto) pero
NO las ejecuta. El agente tiene que separar claramente "te asesoro sobre cómo hacerlo / qué
producto usar" de "lo hacemos nosotros". No prometer ejecución de servicios que el cliente no
presta. Esta distinción se fija en discovery por cliente.

### Densidad de repregunta según perfil

Cuánto repreguntar antes de responder depende del perfil: a un arquitecto se le puede pedir la
especificación fina (tipo de sustrato, condición de obra); a un cliente final se le hace una
pregunta simple y se asume el resto con criterio. No se interroga a un cliente final con la
densidad técnica de un profesional.

### Terminología profesional del oficio (fidelidad léxica)

El rubro tiene vocabulario propio que el agente debe respetar para sonar del oficio: "carpeta"
(no "estructura"), "fisura" (no "lesión"), "aplicar" (no "apoyar"). Es el mismo patrón de
fidelidad terminológica que en los otros rubros (BETROX con "hormigón liviano", G&D con
"patio" no "terraza"): el vocabulario correcto del oficio se carga como obligatorio/prohibido
en el prompt, y sale del testing con el cliente.
