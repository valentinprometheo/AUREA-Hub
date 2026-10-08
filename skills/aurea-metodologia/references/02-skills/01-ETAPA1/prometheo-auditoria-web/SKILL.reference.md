---
name: prometheo-auditoria-web
description: >
  Paso 1.1 de la Etapa 1 (Pre-Discovery) de consultoría e implementación de Prometheo.
  Analiza web + Instagram del cliente ANTES de la primera reunión. Su output (el Doc 0)
  alimenta la plantilla de formulario del rubro, permite adaptar el discovery a las
  particularidades de cada cliente, y dispara la generación del material cliente-facing
  pre-discovery (skill prometheo-docs-kickoff). Genera Doc 0 (interno AUREA) con inventario
  pre-armado, preguntas cerradas, hipótesis de tipología macro, y gaps. Activar cuando
  Valentín diga "paso 0", "paso 1.1", "auditoría web", "cliente nuevo", "preparar R1", o
  cuando comparta URL/IG de un cliente. Se ejecuta al inicio de la Etapa 1, antes de los
  documentos cliente-facing y del discovery. La skill vertical del rubro define qué buscar
  específicamente en la web.
---

# SKILL: AUDITORÍA WEB — PASO 1.1 DE ETAPA 1 (PRE-DISCOVERY)

## PROPÓSITO

Es el primer paso de la Etapa 1 (Discovery), dentro del Paso 1 (Pre-Discovery). El consultor analiza la presencia digital del cliente (web + IG) con Claude para:
- Llegar a R1 con preguntas cerradas ("Vi que tienen X, ¿es correcto?")
- Generar hipótesis de tipología macro que se valida en reunión
- Pre-armar inventario de productos/servicios/categorías
- Detectar gaps entre lo que publican y lo que probablemente es la operación real
- Evaluar si la estructura de categorización publicada se mantiene para el CRM
- Pre-llenar las fichas del formulario asincrónico (Doc 2) con lo que ya está publicado
- Adaptar la plantilla de formulario del rubro a las particularidades del cliente

## CUÁNDO Y CÓMO

Valentín entrega URL de web + perfil de IG. Claude analiza con web_fetch y genera Doc 0. Es trabajo interno de AUREA — el cliente no ve este documento. El Doc 0 luego se usa para personalizar la plantilla del formulario del rubro antes de enviarlo.

## QUÉ ANALIZAR

### 1. Arquitectura de información de la web
- Navegación principal/secundaria, secciones, organización
- Jerarquía de productos: ¿por marca? ¿categoría? ¿uso? ¿material? ¿línea?
- Naming: ¿consistente o caótico? ¿técnico o comercial?
- Páginas clave: home, catálogo, contacto, nosotros, sucursales/showroom
- Hipótesis de tipología macro (la skill vertical define cuál es la esperada para el rubro)
- **Output:** "La web organiza por [X]. ¿Vamos a mantener esa estructura para el CRM?"

### 2. Productos / servicios / catálogo
- Cantidad de productos/categorías visibles
- Nivel de detalle de cada ficha: descripción, foto, especificaciones, precio, stock
- Precios: ¿publican? ¿"consultar"? ¿lista descargable? → anticipa B8 (autonomía)
- Stock: ¿muestran disponibilidad? ¿indicadores de stock?
- E-commerce: ¿carrito? ¿se puede comprar online? ¿qué plataforma? (PrestaShop, WooCommerce, Tienda Nube, MercadoLibre)
- Marcas: ¿propias o multimarca?
- Personalización: ¿mencionan opciones configurables? ¿a medida?
- **Output:** Tabla de inventario pre-armado (categoría | productos | precio visible | ficha | estado)

### 3. Canales de contacto y conversión
- WhatsApp: ¿botón? ¿número? ¿mensaje pre-armado?
- Instagram: perfil, seguidores, frecuencia de posteo, tipo de contenido, highlights
- Formulario de contacto: ¿existe? ¿campos? ¿funciona?
- Email, teléfono, dirección/showroom/sucursales
- CTAs: "cotizar", "comprar", "consultar", "agendar visita"
- **Output:** "El botón de WA va a [número]. ¿Es el que van a usar con Prometheo?"

### 4. Instagram (análisis específico)
- Bio: qué dice, links, categoría
- Contenido: ¿producto? ¿lifestyle? ¿institucional? ¿promocional?
- Highlights: ¿organizados por línea/categoría? ¿info útil?
- Frecuencia de posteo: ¿activo o abandonado?
- Comentarios/DMs: ¿responden? ¿rápido?
- Promociones activas: ¿descuentos? ¿outlet? ¿sorteos?
- **Output:** Hipótesis sobre volumen de consultas por IG y tipo de lead que llega

### 5. Información para pre-llenado
Extraer datos que alimentan directamente los bloques del discovery:
- B2 (catálogo): lista de categorías/productos → pre-llenar fichas del Doc 2
- B4 (FAQs): si la web tiene sección FAQ → pre-cargar preguntas
- B7 (canales): WA, IG, formulario, email → ya mapeados
- B8 (precios): si publican o no → anticipa conversación de autonomía
- B9 (contenidos): brochures, fichas técnicas, fotos, videos en la web
- Envío/pago: si mencionan zonas, costos, métodos → pre-llenar sección vertical

### 6. Gaps y oportunidades
- Info que debería estar y no está (precios ausentes, categorías vacías, links rotos)
- Inconsistencias entre secciones o entre web e IG
- Canales muertos (botón WA roto, IG inactivo, formulario que no funciona)
- Diferencia entre branding y operación probable
- Productos que parecen desactualizados
- **Output:** Hipótesis de gaps para validar en R1

## FORMATO DEL DOC 0

```
DOC 0 — AUDITORÍA WEB (INTERNO AUREA)
Cliente: [nombre]
URL web: [url]
IG: [@perfil]
Fecha: [fecha]
Rubro: [vertical]
Analizado por: Valentín Zas — AUREA Hub

1. RESUMEN EJECUTIVO
Tipología macro detectada | Productos/categorías | Canales | Estado web | Gaps principales

2. ARQUITECTURA DE INFORMACIÓN
[Análisis navegación, jerarquía, naming]
Hipótesis tipología: [...]
Pregunta R1: "¿Mantienen esta estructura?"

3. INVENTARIO PRE-ARMADO
| Categoría/Línea | Productos visibles | Precio | Ficha | Estado |
(esto pre-llena Doc 2)

4. INSTAGRAM
Bio | Contenido | Highlights | Frecuencia | Promos activas
Hipótesis: [...]

5. CANALES MAPEADOS
WA: [número, estado] | IG: [perfil, seg] | Formulario: [existe/no] | Email | Showroom
Preguntas R1: [...]

6. PRECIOS Y AUTONOMÍA (anticipa B8)
¿Publican? ¿Lista? ¿Consultar? ¿E-commerce con precios?
Hipótesis: [nivel de autonomía probable]

7. ENVÍO, PAGO Y LOGÍSTICA (anticipa vertical)
¿Mencionan envío? ¿Zonas? ¿Costos? ¿Métodos de pago?
Preguntas R1: [...]

8. CONTENIDOS DETECTADOS
Brochures, fichas, fotos, videos, FAQs en web
(esto pre-llena Doc 3)

9. GAPS Y OPORTUNIDADES
[Lista de inconsistencias, hipótesis]

10. PREGUNTAS CERRADAS PARA R1 (consolidado)
[Todas las preguntas organizadas por bloque]

11. ADAPTACIONES A LA PLANTILLA DEL RUBRO
[Qué cambiar en la plantilla de formulario estándar del rubro para este cliente]
```

## CONEXIÓN CON EL SISTEMA

El Doc 0 es el insumo de **dos caminos paralelos** del Paso 1:

```
                    ┌─→ PASO 1.2 + 1.3 — Material cliente-facing
                    │   skill prometheo-docs-kickoff
DOC 0 (auditoría) ──┤   · Doc de Bienvenida (Sección 1 = datos del Doc 0)
                    │   · Guía Metodológica
                    │
                    └─→ PASO 2 — Discovery
                        · Plantilla de formulario adaptada al cliente
                        · Pre-llena Doc 2 (fichas producto) + Doc 3 (accesos/contenidos)
                        · Preguntas cerradas para R1
```

Detalle:
- Doc 0 → **dispara** → skill `prometheo-docs-kickoff` (Paso 1.2 y 1.3). La Sección 1 del Doc de Bienvenida ("Lo que ya sabemos de [CLIENTE]") se construye **directamente** con los datos verificados del Doc 0.
- Doc 0 → alimenta → Plantilla de formulario adaptada al cliente (Paso 2.1).
- Doc 0 → pre-llena → Doc 2 (fichas producto) + Doc 3 (accesos/contenidos).
- Doc 0 → genera → Preguntas cerradas para R1.
- Skill vertical del rubro → define → Qué buscar específicamente en la web.

## CIERRE DEL PASO 1.1 — HANDOFF

Cuando el Doc 0 está completo (las 11 secciones del formato), el Paso 1.1 está cerrado.
**El paso siguiente es generar el material cliente-facing.**

Al terminar el Doc 0, Claude le indica al implementador:

> "El Doc 0 está listo. El siguiente paso del Paso 1 es generar los 2 documentos que el
> cliente recibe antes de R1: el Doc de Bienvenida y la Guía Metodológica. Eso lo hace la
> skill `prometheo-docs-kickoff`, que usa este Doc 0 como input. Para arrancar voy a
> necesitar: el consultor asignado a la cuenta y el N estimado de reuniones de Discovery.
> ¿Avanzamos con eso?"

No generar el material cliente-facing dentro de esta skill — es responsabilidad de
`prometheo-docs-kickoff`. Esta skill solo **cierra con el handoff**: deja el Doc 0 listo y
señala explícitamente cuál es el próximo paso y qué skill lo ejecuta.

## REGLAS PARA CLAUDE

1. Si hay URL → analizarla con web_fetch. Sin URL no hay auditoría.
2. Si hay IG → analizarlo. Mucha info comercial está solo en IG, no en la web.
3. No inventar datos. "No encontrado en web — validar en R1."
4. Cada hallazgo → pregunta cerrada concreta para R1.
5. Las hipótesis se marcan como hipótesis, no como hechos.
6. El inventario pre-armado se usa para pre-llenar Doc 2. Mantener formato tabular.
7. Registrar plataforma de e-commerce si existe (PrestaShop, Woo, TN) → impacta integración.
8. Registrar showroom/sucursales → impacta B0, B5, routing.
9. La sección 11 (adaptaciones a la plantilla) es clave: dice qué cambiar en la plantilla genérica del rubro para este cliente específico.
10. Al cerrar el Doc 0, hacer siempre el handoff: indicar que el próximo paso es `prometheo-docs-kickoff` y pedir los inputs que esa skill necesita (consultor asignado, N de reuniones). No generar el material cliente-facing acá.
