---
consultar-cuando: Etapa 2 diseño de prompt, cliente con catálogo digital o fuente de datos externa
disparadores: "integración", "PrestaShop", "Tokko", "Google Sheets", "consultar precio", "cómo busca el agente"
fuente-única-de: reglas de consulta a fuentes de datos (genéricas + por fuente)
combina-con: rubro correspondiente, 05-estructura-prompt-agente, principios-transversales-agente
---

# Reglas de integración con catálogo digital

> **Propósito:** Documentar las 6 reglas que todo prompt con integración a catálogo digital (PrestaShop, Tokko, ficha.info, Bejerman, etc.) debe respetar.
> **Aplica a:** ~90% de los clientes AUREA Hub (mobiliario, insumos, real estate, inmobiliaria tradicional, retail).
> **Origen:** Feedback técnico de soporte Prometheo (Gastón) sobre cuenta BETROX — 15 mayo 2026.
> **Status:** Reglas inviolables. Integradas al Reglas Diseño de Prometheo by AUREA.

---

## Por qué existe este documento

En la cuenta de BETROX se detectó que la integración con PrestaShop no se estaba usando. La conclusión inicial fue "problema de integración", pero el soporte de Prometheo identificó que **el problema era el prompt**:

- El prompt bloqueaba consultas de precio si el lead no estaba calificado.
- El prompt no distinguía entre "buscar producto" y "consultar precio".
- El prompt restringía URLs a un mapa canónico que estaba vacío.
- El naming interno de productos no era único.

Estos 4 errores no son específicos de BETROX. Aparecen en cualquier prompt que tenga integración a catálogo digital si no se documenta explícitamente cómo manejarla.

**Las 6 reglas de este documento previenen ese error en todos los clientes futuros.**

---

## Regla 1 — La calificación del lead NUNCA bloquea consultas concretas

### Definición
Aunque el lead no esté calificado (no se sabe si es consumidor final, profesional, recurrente, etc.), el agente debe responder consultas atómicas de producto: precio, link, ficha técnica, disponibilidad, características.

### Problema que resuelve
Prompts mal escritos bloquean preguntas simples ("¿cuánto sale la POSITANO 1.60?") esperando que el lead se identifique primero. Eso rompe la conversación y le hace sentir al lead que el bot es burocrático.

### Implementación en el prompt
La sección de "parámetros fijos" o "calificación previa" debe incluir explícitamente esta cláusula:

> "Aunque `tipo_usuario = desconocido`, el agente PUEDE responder consultas atómicas de producto: precio puntual, link, ficha técnica, disponibilidad. La calificación es prioritaria para flujos comerciales (cotización, derivación, cross-sell), pero no para responder preguntas concretas."

### Cómo distinguir
| Acción | Requiere calificación previa | Puede ejecutarse sin calificación |
|---|---|---|
| Cotización formal | ✅ Sí | ❌ No |
| Cross-sell o upselling | ✅ Sí | ❌ No |
| Derivación al comercial | ✅ Sí | ❌ No |
| Consulta de precio puntual | ❌ No | ✅ Sí |
| Envío de link de producto | ❌ No | ✅ Sí |
| Envío de ficha técnica | ❌ No | ✅ Sí |
| Confirmación de disponibilidad | ❌ No | ✅ Sí |

---

## Regla 2 — Búsqueda de producto ≠ Consulta de precio

### Definición
Son dos operaciones distintas con tools distintos. El prompt debe declararlas como pasos separados, no como una operación monolítica.

### Problema que resuelve
Si el prompt solo tiene "consultar precio", el agente falla cuando el lead nombra un producto de forma imperfecta. Necesita primero resolver el producto (búsqueda tolerante), recién después consultar precio.

### Implementación en el prompt
Declarar 3 operaciones independientes con tools propios:

```
Paso 1 — Resolver producto:
[BUSCAR_PRODUCTO: NOMBRE_REFERIDO_POR_EL_CLIENTE]

Paso 2 — Si el producto fue identificado, consultar precio:
[CONSULTA_PRECIO: CLAVE_INTERNA_MODELO, MEDIDA]

Paso 3 — Si la integración devuelve URL, usarla en la respuesta:
[OBTENER_LINK: CLAVE_INTERNA_MODELO]
```

### Por qué importa el orden
- **BUSCAR primero:** el lead nombra el producto con su jerga. Match tolerante.
- **PRECIO segundo:** solo si BUSCAR encontró el producto. Usa la clave interna oficial.
- **LINK tercero:** opcional, según el caso. Usa la URL devuelta por la integración.

---

## Regla 3 — Match de producto debe ser tolerante

### Definición
La búsqueda de producto debe aceptar nombres imperfectos, sinónimos, variantes ortográficas, y referencias parciales.

### Problema que resuelve
El lead escribe "neuquen" (sin tilde), "Positano 160", "la mesa redonda esa", "huevera". El sistema debe encontrar el producto incluso con esa imperfección.

### Implementación en el prompt
Cuando se invoca `[BUSCAR_PRODUCTO]`, el parámetro es el texto literal del lead, no una versión "limpia". La integración (PrestaShop, Tokko, etc.) resuelve el match.

Si la integración devuelve múltiples candidatos, el agente:
1. Pregunta al lead con foto o detalle para desambiguar
2. NO asume el primer candidato

Si la integración devuelve 0 resultados:
1. NO asume que el producto no existe
2. Pide captura, link, o más contexto al lead
3. Si persiste el match en blanco, deriva al comercial

### Frase prohibida en estos casos
> "Ese producto no existe en mi catálogo."

### Frase de reemplazo
> "Ese nombre no me figura con esa denominación exacta. ¿Puede ser que lo hayas visto con otro nombre? Si me pasás captura o link, lo identifico al toque."

---

## Regla 4 — URLs devueltas por la integración son siempre válidas

### Definición
Cualquier URL que la integración (PrestaShop, Tokko, etc.) devuelva es canónica por definición. El agente puede usarla sin restricción.

### Problema que resuelve
Prompts con "mapa de URLs canónicas" cerrado bloquean URLs reales que la integración devuelve. Resultado: el agente encuentra el producto, pero se frena al compartir el link.

### Implementación en el prompt
Distinguir tres categorías de URLs:

| Tipo de URL | Comportamiento |
|---|---|
| **URLs devueltas por la integración** (`[OBTENER_LINK: CLAVE_INTERNA]`) | Siempre válidas. Se comparten directamente. |
| **URLs inventadas por el agente** (construidas desde el nombre del producto) | Siempre prohibidas. |
| **URLs estáticas fuera del catálogo principal** (videos de aplicación o explicativos, fichas PDF que no están en e-commerce, materiales de marketing) | NO van hardcoded en el prompt. Viven en una fuente externa de acceso compartido (Google Drive, YouTube, Vimeo, Notion, Dropbox, Google Sheets, o equivalente). |

### Por qué las URLs externas NO van hardcoded en el prompt

Los URLs externos (videos, fichas técnicas PDF, materiales de comunicación) cambian con frecuencia. Si los hardcodeás en el prompt:
- Cada vez que se actualizan, hay que modificar el prompt
- El cliente no puede actualizarlos por su cuenta — depende de AUREA
- El cliente termina con material desactualizado en producción

**Solución correcta:** estos URLs viven en una **fuente externa de acceso compartido** (Google Drive con permisos abiertos, YouTube, Vimeo, Notion, Dropbox compartido, Google Sheets embebido, o equivalente). El cliente actualiza directo ahí, sin tocar el prompt.

**Ejemplos típicos de qué vive en qué fuente:**

| Tipo de URL externa | Fuentes típicas |
|---|---|
| Videos de aplicación / explicativos / institucionales | YouTube, Vimeo |
| Fichas técnicas PDF | Google Drive compartido, Dropbox compartido |
| Catálogos extendidos / brochures | Google Drive compartido |
| Materiales de marketing actualizables | Notion, Drive |
| Listas con links dinámicos a múltiples productos | Google Sheets embebido |

La fuente específica la define cada cliente según su workflow operativo — AUREA no impone una herramienta. Lo que sí impone es que **no vayan en el prompt**.

### Paso de descubrimiento obligatorio en Etapa 2

Durante el diseño del prompt, AUREA pregunta al cliente:

1. *"¿Dónde tenés documentada la base de datos del catálogo principal?"* (sistema integrable como PrestaShop o Tokko, Google Sheets, planillas locales, etc.)

2. *"¿Hay URLs que el agente vaya a necesitar compartir y que no estén en la integración principal?"* — caso típico: videos de aplicación o explicativos, fichas técnicas PDF que viven aparte del e-commerce, materiales de marketing.

3. *"¿En qué fuente externa querés tener esos URLs?"* — el cliente elige según su workflow (Google Drive, YouTube, Vimeo, Notion, Dropbox, Google Sheets, etc.). AUREA no impone una herramienta.

Para los URLs detectados en las preguntas 2 y 3, AUREA documenta la fuente externa donde van a vivir, NO los pone en el prompt.

### Reformulación de "NO INVENTAR LINKS"
Antes (prompt típico problemático):
> "NUNCA inventás URLs. Solo enviás URLs de la lista canónica."

Después (formulación correcta):
> "NUNCA inventás URLs construyéndolas desde el nombre del producto. SÍ usás URLs devueltas por la integración (siempre válidas). Las URLs estáticas fuera del catálogo se consultan en la fuente externa documentada (Google Drive, YouTube, Notion, Dropbox, Google Sheets, o equivalente), NO se hardcodean en el prompt."

---

## Regla 5 — Unificación de naming interno de productos

### Definición
Cada producto tiene UNA clave interna única que se usa en toda la cadena de tools. Las variantes (nombre comercial, jerga del cliente, nombre técnico, SKU, y sinónimos del lead final) mapean a esa clave.

### Problema que resuelve
Cuando el mismo producto aparece referido como "POSITANO", "Positano 160", "mesa POSITANO 1.60m", "positano grande" en distintos lugares del prompt y en las consultas reales del lead, las búsquedas fallan por inconsistencia.

### Implementación en el prompt: tabla de 3 columnas separadas

La tabla de equivalencias tiene **3 columnas distintas**, no una sola lista mezclada:

| Columna | Qué contiene | Quién la mantiene | Cuándo se completa |
|---|---|---|---|
| **clave_interna** | El nombre técnico único oficial. Ejemplo: `POSITANO_1.60` | Consultor AUREA con criterio + auditoría web del cliente | Etapa 2 inicial |
| **variantes_tecnicas** | SKU del cliente, nombre comercial oficial, nombre en sistema fuente. Ejemplo: `SKU-MP-POS-160`, `"POSITANO 1.60m"` | Cliente (es info de su catálogo) | Etapa 2 inicial, validada con cliente |
| **variantes_lead** | Cómo lo escribe un lead que no conoce el producto: jerga, errores ortográficos, formas coloquiales. Ejemplo: `"positano"`, `"la grande"`, `"mesa redonda esa"` | Inicial: consultor con criterio. Iterativo: post Go-Live con conversaciones reales | Etapa 2 (parcial) + Monitoreo (completo) |

### Por qué separar las 3 columnas

Las **variantes técnicas** son **deterministas**: el cliente las saca de su sistema fuente (PrestaShop, Bejerman, Tokko). Son objetivas y estables.

Las **variantes del lead** son **probabilísticas**: nadie sabe cómo va a escribir el lead. Son subjetivas y crecen con el tiempo.

Mezclar las dos en una sola columna mete ruido en el match tolerante (Regla 3). El sistema termina haciendo match con variantes técnicas raras (SKU complejos) mientras ignora variantes coloquiales obvias del lead.

### Ejemplo completo

```
PRODUCTO: Mesa Positano de 1.60m

clave_interna: POSITANO_1.60

variantes_tecnicas:
  - SKU-MP-POS-160
  - "POSITANO 1.60m"
  - "Mesa Positano 1.60"
  - codigo_bejerman_x12345

variantes_lead:
  - "positano"
  - "Positano"
  - "Positano 1.60"
  - "POSITANO grande"
  - "la mesa redonda esa"  → ambigua, requiere repregunta
  - "positano de uno sesenta"
  - "mesa de hormigón redonda" → ambigua, requiere repregunta
```

### Quién construye el naming unificado

**El consultor AUREA**, durante Etapa 2, con criterio profesional + auditoría web del cliente.

El cliente NO construye el naming unificado — no tiene visión transversal de cómo se ven todos los prompts. El cliente sí VALIDA la columna `variantes_tecnicas` (porque es su catálogo).

### Cómo se completa la columna `variantes_lead`

**En Etapa 2 (inicial):** el consultor anticipa las variantes obvias con criterio:
- Variantes ortográficas (con/sin acentos, con/sin mayúsculas, con/sin guiones)
- Variantes coloquiales obvias ("la grande", "la chica")
- Sinónimos típicos del rubro

**Post Go-Live (iterativo):** se completa con datos reales:
- Cada conversación nueva donde el lead nombró el producto de una forma no contemplada
- Esa variante nueva se agrega a la columna `variantes_lead`
- Si la variante es ambigua (puede ser 2+ productos), se documenta como "requiere repregunta"

### Realismo de la regla

**No siempre va a ser perfecto.** Habrá conversaciones donde el lead use una variante que no está en la tabla. Para esos casos:

1. El match tolerante (Regla 3) intenta resolver con similitud
2. Si la similitud no es clara, el agente repregunta (no asume)
3. Cada variante nueva detectada se agrega a la tabla
4. La tabla crece con el tiempo

La tabla NUNCA está "cerrada y completa". Es un activo vivo que mejora con cada conversación.

---

## Regla 6 — Prioridad explícita de respuesta

### Definición
El prompt debe declarar explícitamente, al inicio de la sección de producto/consulta, las 3 prioridades de respuesta en orden:

1. **Respuesta directa** — si el agente tiene la info en su prompt hardcodeado (FAQ, regla de negocio, info estática)
2. **Consultar integración** — si la info vive en sistema externo (precio, stock, link, ficha técnica)
3. **Derivar a humano** — si nada de lo anterior resuelve

### Problema que resuelve
Sin esta prioridad explícita, el agente:
- Deriva consultas que podría responder solo (degrada la experiencia)
- Inventa respuestas que debería consultar (rompe la confianza)
- Consulta integración para info que es hardcoded (latencia innecesaria)

### Implementación en el prompt
En la sección de "Información del producto" o equivalente:

```
PRIORIDAD DE RESPUESTA — orden estricto:

1. RESPONDER DIRECTO si la info está en este prompt:
   - FAQs oficiales
   - Características del material/marca
   - Política de envío, garantía, mantenimiento
   - Reglas de combinación entre productos
   - Lógica de recomendación por superficie/uso

2. CONSULTAR INTEGRACIÓN si la info es dinámica:
   - Precio actual
   - Stock disponible
   - Link directo al producto
   - Ficha técnica PDF
   - Imágenes del producto en ambiente

3. DERIVAR A HUMANO si nada de lo anterior aplica:
   - Cotización personalizada
   - Caso especial fuera de catálogo
   - Negociación de descuentos
   - Postventa o reclamo
```

---

## Checklist de auditoría de un prompt existente

Cuando audites un prompt con integración a catálogo, validá las 6 reglas:

- [ ] **Regla 1:** ¿Las consultas atómicas (precio, link, ficha) se pueden ejecutar sin calificar al lead? Revisar sección de "calificación previa" o "parámetros fijos".
- [ ] **Regla 2:** ¿El prompt tiene 3 tools separados (BUSCAR_PRODUCTO, CONSULTA_PRECIO, OBTENER_LINK), o todo está colapsado en "consultar precio"?
- [ ] **Regla 3:** ¿La búsqueda acepta nombres imperfectos? ¿Hay frase de fallback para producto no encontrado que NO asume "no existe"?
- [ ] **Regla 4:** ¿El "no inventar URLs" distingue entre URLs inventadas (prohibidas) vs URLs devueltas por integración (válidas)?
- [ ] **Regla 5:** ¿Existe tabla de equivalencias con `clave_interna` única por producto? ¿Las invocaciones de tools la usan?
- [ ] **Regla 6:** ¿La sección de producto declara explícitamente la prioridad: directo / integración / humano?

Si alguna respuesta es **No**, ese prompt está bloqueando o degradando la integración.

---

## Aplicabilidad por rubro

| Rubro | Integración típica | Aplican las 6 reglas |
|---|---|---|
| Mobiliario | PrestaShop, Bejerman | ✅ Todas |
| Insumos construcción | PrestaShop, e-commerce propio | ✅ Todas |
| Real estate (desarrollista) | Tokko | ✅ Todas — el catálogo son proyectos/unidades |
| Inmobiliaria tradicional | ficha.info, Tokko | ✅ Todas — el catálogo son propiedades |
| Retail / e-commerce | Shopify, WooCommerce, PrestaShop | ✅ Todas |
| Marketplace inmobiliario (MIA) | API propia | ✅ Todas |

Las 6 reglas son universales para clientes con catálogo digital. La única variante por rubro es **qué llamamos "producto"**: mueble, insumo, proyecto, unidad, propiedad. La lógica de las 6 reglas no cambia.

---

## Caso de referencia: BETROX (Catalina V1.6 → V1.7)

El prompt de Catalina V1.6 fallaba en 4 de las 6 reglas:
- Regla 1: bloqueada (sec 1B.1 dice "no podés cotizar sin saber tipo_usuario")
- Regla 2: bloqueada (solo tiene CONSULTA_PRECIO, no BUSCAR_PRODUCTO)
- Regla 4: bloqueada (mapa de URLs vacío con whitelist estricta)
- Regla 5: bloqueada (no hay tabla de equivalencias formal)

La V1.7 aplica los 6 cambios documentados en `aplicacion-betrox-v1.6-a-v1.7.md` (entregable operativo, fuera del ZIP de metodología).

---

## Mantenimiento de este documento

Cuando aparezca un patrón nuevo en feedback de soporte de Prometheo o de cualquier cliente, se evalúa si es:
- **Variante de una regla existente** → se agrega como ejemplo en la regla correspondiente
- **Regla nueva** → se documenta como Regla 7, 8, etc.
- **Específica de un rubro** → se agrega al archivo del rubro (`06-rubros/0X-*.md`), no acá

Responsable: Valentín Zas con apoyo del soporte técnico de Prometheo.

---

# DOCTRINA POR FUENTE (Sheets / Tokko / PrestaShop)

> Las 6 reglas de arriba son genéricas a cualquier catálogo. Esta parte es lo que cambia
> según la **fuente de datos concreta**, destilado de los tres prompts en producción. El
> insight clave: **las reglas de consulta dependen de la fuente, no del rubro.** El próximo
> cliente con Sheets necesita lo mismo que G&D aunque sea de otro rubro; el próximo con
> Tokko, lo mismo que EDFAN; el próximo con PrestaShop, lo mismo que BETROX. Por eso esto se
> consulta por el eje INTEGRACIÓN del router, cruzando rubros.

## Cómo se elige la fuente (criterio AUREA)

- Dato **dinámico** (precio, stock, disponibilidad, lo que cambia) → fuente externa, nunca
  hardcodeado en el prompt.
- Dato **fijo** (posicionamiento, amenities de diseño, vocabulario, lógica de venta) →
  hardcodeado en el prompt.
- La fuente externa es **fuente única** de lo dinámico: el prompt no duplica esos datos, los
  consulta. Si un dato dinámico aparece en el prompt, es solo contexto interno y lleva una
  regla anti-memoria que prohíbe responderlo sin consultar.

---

## Fuente: GOOGLE SHEETS — caso de referencia G&D Developers

Sheets como base dinámica de unidades y proyectos, conectada a Prometheo. Reglas de consulta
que el prompt debe instruir:

- **Hojas y su función.** UNIDADES (datos vivos de cada unidad), PROYECTOS (datos de
  proyecto: dirección, link_maps, link_video_obra, estado_obra, etapa_actual),
  FINANCIACION (esquemas por proyecto), OBRAS_FINALIZADAS (solo para reconocer si una obra
  que menciona el lead es del cliente; no se ofrece). Una hoja interna (INTERNO_PROYECTOS)
  NO se habilita.
- **Búsqueda fresca cada turno.** Cada pregunta de dato dispara una búsqueda NUEVA en el
  mismo turno, aunque sea repregunta sobre el mismo proyecto. Nunca responder de lo que se
  recordó de una búsqueda anterior: ese lote era parcial.
- **Verificación del lote (la regla más fina).** El sistema puede devolver los resultados
  desordenados aunque se pidan ordenados. Por eso, antes de responder, se recorre TODO el
  lote y se elige el valor correcto a mano: el de menor precio para un "desde", el de mayor
  m² para "el más grande". El primer resultado NO es necesariamente la respuesta.
- **Una sola búsqueda por ficha.** Para armar la ficha de un proyecto, una búsqueda del
  proyecto entero filtrando disponibles, no una por tipología. Salvaguarda: si el lote llega
  al límite de elementos, repetir por tipología para no perder las más caras.
- **Columnas estructuradas ganan sobre notas.** Los datos duros (tipología, piso, precio,
  m², estado) salen de las columnas, nunca del texto de `notas_unidad`. Las notas solo
  enriquecen (ej. "con parrilla propia").
- **Precio siempre disponible.** Todos los proyectos activos tienen precio cargado, incluso
  los de pozo. Prohibido decir que un precio "se está actualizando" o "está a confirmar":
  eso es inventar una excusa. Primero se busca; solo si el Sheet realmente no devuelve nada,
  se usa el fallback de derivación.
- **Entrega textual.** La fecha de entrega se dice exactamente como figura en su columna
  (no se convierte de semestre a cuatrimestre ni al revés).

### Diseño de la base en Google Sheets — criterio, lógica y buenas prácticas (experiencia G&D)

> Lo de arriba es cómo se CONSULTA la base. Esto es cómo se DISEÑA, que es una decisión previa
> y determina si la consulta va a funcionar. Destilado del diseño real de G&D (6 hojas, verificado
> contra la planilla). Reutilizable en cualquier cliente Sheet-First, de cualquier rubro.

**Arquitectura por grano — una hoja = una unidad de análisis.** Cada hoja tiene un grano
distinto y no repite lo de otra:
- `UNIDADES` — una fila por unidad (Proyecto, unidad_id, tokko_id, publicada_en_tokko,
  tipologia, m2_cubiertos, m2_totales, piso, orientacion, disposicion, tipo_balcon,
  tiene_terraza, tiene_parrilla, precio_usd, estado, es_exclusiva, notas_unidad). Es la
  fuente de verdad del stock.
- `PROYECTOS` — una fila por proyecto (dirección, barrio, link_maps, estado_obra,
  etapa_actual, fecha_entrega_cuatrimestre, perfil_ideal, diferencial_unico, amenities,
  terminaciones, flags de renta con sus montos, gastos, estado_comercializacion,
  ultima_actualizacion, link_video_obra, co_comercializa_con).
- `FINANCIACION` — una fila por proyecto × modalidad (many-to-one respecto de proyecto):
  anticipo, cuotas, moneda, ajuste, tna, condiciones. Vive aparte justamente porque un
  proyecto tiene varias modalidades.
- `RESUMEN_UNIDADES` — hoja **derivada**, una fila por proyecto × tipología, con el "desde"
  ya calculado (precio_min, unidad_mas_barata, m2 min/max, piso min/max). Es un atajo de
  lectura para responder "desde/mín/máx" en una sola consulta.
- `OBRAS_FINALIZADAS` — catálogo histórico, solo para reconocer clientes recurrentes.
- Hoja interna del equipo — rotulada en la propia hoja "NO conectar ni habilitar en
  Prometheo". El routing y los responsables no llegan al agente.

**Criterio de diseño (por qué está así):**
- **Fuente única de datos vivos.** El prompt no tiene ni un precio ni un m². El cliente
  actualiza el Sheet sin tocar el prompt. Es lo que hace sostenible la operación.
- **IDs legibles y jerárquicos.** `unidad_id` sigue PROYECTO-PISO-LETRA (`MOCA2-P18-A`). Sirve
  de clave estable y de puente entre hojas (RESUMEN apunta a un `unidad_id` de UNIDADES).
- **Complementariedad con Tokko, no duplicación.** `tokko_id` y `publicada_en_tokko` mapean
  qué unidad está en Tokko. Sheet y Tokko suman, no repiten.
- **Hoja derivada con la de detalle como fuente de verdad.** RESUMEN acelera el "desde", pero
  si difiere de UNIDADES, **gana UNIDADES**. La derivada nunca gobierna el dato.
- **Dominios controlados** en las columnas por las que el agente filtra (`estado`:
  disponible/reservada/bloqueado; `tipologia`; `estado_comercializacion`: activo/stand-by).
- **Precio vacío, nunca 0, cuando la unidad no es vendible** (reservada/bloqueada): poner 0
  contaminaría los mínimos.
- **Datos textuales que el agente repite literal viven ya formateados** en la columna
  (`fecha_entrega_cuatrimestre` guarda "2do Cuatrimestre 2026", no un mes a convertir).
- **Flags + montos condicionados** (`tiene_renta_desde_pozo` + `renta_monto_Xamb`) en vez de
  meter la lógica en el prompt.
- **`estado_comercializacion` = stand-by** para excluir del catálogo lo que no se ofrece
  todavía (proyectos en pozo sin lanzar) sin borrarlo.

**Buenas prácticas reutilizables (para el próximo cliente Sheet-First):**
1. Grano explícito por hoja + ID estable como clave; hoja derivada solo si el atajo lo justifica.
2. Datos duros en columnas; una columna de notas solo enriquece, nunca gobierna un dato.
3. `estado` como dominio cerrado, y el agente siempre filtra por `disponible`.
4. Precio ausente = celda vacía, nunca 0 ni texto.
5. Lo que el agente repite literal, ya formateado en la columna.
6. Flags + montos condicionados en vez de lógica en el prompt.
7. Un campo para excluir sin borrar (`estado_comercializacion`).
8. Hoja interna separada y rotulada "no conectar".
9. **Agregar columnas al final del esquema, nunca intercalar** (por la restricción de refresco
   destructivo, ver abajo).

**Hallazgos y problemas detectados en una base real (para no repetirlos):**
- **Hoja derivada desincronizada (el más grave).** En G&D, `RESUMEN_UNIDADES.unidad_mas_barata`
  apuntaba a IDs que no existen en UNIDADES (`MOCA2-P3-V`, `9JULIO-P3-D`) e incluía tipologías
  que UNIDADES no tiene cargadas. Causa: RESUMEN se mantenía a mano y no se recalculaba al
  editar UNIDADES. Es el origen directo del "no encuentro la ficha". **Regla: la hoja derivada
  se genera por fórmula o script, nunca a mano; si difiere de la de detalle, gana la de
  detalle.** (Carga del cliente, no imputable a Prometheo.)
- **Un mismo concepto codificado de dos formas.** "Reventa" vivía como valor de `estado`
  (`estado = "reventa"`) en un proyecto y como texto libre en `notas_unidad` ("Es reventa") en
  otro. El agente necesita detectar el concepto de forma única. **Regla: un hecho, un solo
  lugar y un solo formato** (reventa como estado o como flag propio, nunca en notas).
- **Columnas huérfanas o de bajo aporte.** `es_exclusiva` estaba vacía en toda la hoja;
  `tiene_terraza` casi siempre "no". Se pagan en cada consulta sin aportar. Revisar y sacar lo
  que no tiene finalidad real.
- **Desnormalización pesada.** `terminaciones_highlights`, `gastos_posesion` y
  `gastos_escritura` eran idénticos palabra por palabra en las 10 filas de PROYECTOS. Eso es
  dato de política, no de proyecto: va a una hoja de condiciones generales o al prompt como
  regla, no repetido en cada fila (infla cada lectura).
- **Dominios inconsistentes.** `publicada_en_tokko` mezclaba "no"/"sí"/"si"/vacío;
  `orientacion` mezclaba mayúsculas y minúsculas. Si el agente o un filtro comparan exacto,
  falla. Normalizar los dominios controlados.
- **El "desde" puede ser engañoso** si el más barato es una reventa (que solo se vende de
  contado): el agente tiene que ser coherente entre el "desde" que muestra como gancho y la
  condición de pago de esa unidad.

**Trazabilidad columna ↔ regla del prompt** (cada decisión de la base se conecta con una regla):
`estado` → filtrar disponible + sin-stock-es-alternativa + verificación del lote ·
`unidad_mas_barata`/`precio_min` (RESUMEN) → regla del "más barato", con UNIDADES de respaldo ·
`m2_cubiertos` vs `m2_totales` → superficie totales por defecto, cubiertos a pedido ·
`fecha_entrega_cuatrimestre` → entrega textual sin convertir ·
`tiene_renta_desde_pozo` + montos → renta desde pozo solo donde el flag está en sí, solo contado ·
`estado_comercializacion` = stand-by → no ofrecer ese proyecto ·
`notas_unidad "Es reventa"` / `estado = reventa` → reventas siempre de contado ·
`link_video_obra` vacío → no ofrecer un video que no existe ·
`co_comercializa_con` → atender sin derivar al co-comercializador ·
hoja interna → el agente no verbaliza routing ni nombres.

**Ruteo por grano como primera decisión de búsqueda.** Antes de buscar, el agente decide en
qué hoja según la pregunta: RESUMEN para "desde"/mín-máx, UNIDADES para detalle de unidad,
PROYECTOS para info general, FINANCIACION para pago, OBRAS_FINALIZADAS para reconocer un
recurrente. El ruteo por grano aplica a cualquier base multi-hoja.



Tokko como CRM inmobiliario con el stock vivo. Reglas de consulta:

- **Qué sale de Tokko vs qué sale del catálogo embebido.** De Tokko: precio, disponibilidad,
  stock, m², piso, orientación cardinal, ubicación interna (frente/contrafrente/lateral),
  tipologías hoy disponibles, apto crédito por unidad, fecha de entrega, estado de obra,
  planos de unidad. Del catálogo embebido en el prompt: amenities, posicionamiento,
  características generales, tipologías de diseño del proyecto. Se complementan, no se
  contradicen.
- **Tipología del proyecto vs unidades disponibles hoy (distinción crítica).** Son dos
  planos. "El proyecto tiene 1, 2, 3 y 4 ambientes" (diseño del edificio, sale de la ficha)
  es distinto de "hoy hay monoambientes disponibles" (stock vivo, sale de Tokko). Nunca se
  reduce el proyecto al subset disponible de hoy.
- **Regla anti-memoria.** Aunque el prompt tenga números, son contexto interno; no habilitan
  responder sin Tokko. Toda pregunta cuya respuesta cambie con el tiempo va primero a Tokko.
- **Discreción de la herramienta.** Nunca se nombra "Tokko" ni "el sistema" ni "mi sistema
  de precios" al lead. Se da el dato como una vendedora que lo tiene a mano (ver principio
  transversal "no exponer la herramienta").
- **Fallback hablando de personas.** Si Tokko no devuelve el dato: "lo confirmo con el
  equipo y le paso los valores", nunca "el sistema no me devuelve".
- **Conversión de fecha a cuatrimestre** (regla del cliente): nunca el mes exacto de Tokko;
  se convierte al cuatrimestre.
- **Anti-patrones.** El prompt de EDFAN documenta 21 anti-patrones operativos de Tokko
  (responder stock de memoria, usar catálogo como stock vivo, confirmar binarios sin
  verificar, etc.). Son reutilizables para cualquier cliente con Tokko.
- **Límite: el agente no puede declarar parcial lo que la integración no marca como parcial
  (pregunta abierta a ITESA).** En un caso real, ante consultas equivalentes la búsqueda
  devolvió tres subconjuntos distintos de proyectos (primero A/B/C, después D, después
  D/E/A), y el agente afirmó "no hay unidades de otras tipologías" cuando sí las había. El
  prompt puede instruir "aclará que mostrás algunos de N", pero el agente **no puede saber
  que la lista está incompleta si la integración no le devuelve el total.** La verificación
  del lote mitiga el orden, no la parcialidad. Preguntas abiertas a ITESA, no supuestos:
  ¿hay límite de resultados por consulta y el agente puede saber que quedó truncada?, ¿por
  qué cambia el conjunto entre consultas equivalentes (ranking, aleatoriedad, paginación)?,
  ¿el agente puede leer el total para decir "le muestro 3 de 14"?, ¿cómo se consulta a nivel
  emprendimiento y no de unidad? Registrado como reporte formal al proveedor.

## Fuente: PRESTASHOP — caso de referencia BETROX

PrestaShop como catálogo de e-commerce. Reglas de consulta:

- **El MODELO es la clave.** La búsqueda se hace por el nombre del modelo tal como lo
  escribió el cliente ("positano", "sit 45"), no por el tipo de mueble (mesa/banco, que
  ensucia la búsqueda) ni por el nombre del archivo de foto.
- **Búsqueda escalonada (4 intentos).** Intento 1: nombre completo como lo dijo el cliente.
  Intento 2: el modelo solo, sin el tipo. Intento 3: modelo con el tipo antepuesto. Intento
  4: el modelo en otra grafía (con/sin tilde, mayúsculas). Solo si los cuatro dan 0 se va al
  fallback. No rendirse al primer intento.
- **Buscar ≠ leer precio ≠ obtener link.** Tres operaciones en orden: buscar el producto,
  tomar el precio de la medida pedida, usar la URL si la devuelve la integración. Nunca se
  construye una URL a mano.
- **Precio por medida.** En BETROX cada medida tiene su precio; si la búsqueda devuelve
  precio para al menos una medida, siempre se da una referencia real (nunca estimada).
- **Hoy sin consulta por categorías (limitación vigente, dato clave para el futuro).**
  PrestaShop hoy se consulta solo por características de producto, NO por categorías. Por eso
  la categoría comercial "destacados" (que crea el cliente) está **hardcodeada como lista
  provisoria en el prompt**, con mantenimiento manual. Cuando ITESA habilite la consulta por
  categoría, esa lista fija se reemplaza por consulta en vivo y se deja de mantener a mano.
  Toda lista hardcodeada de este tipo lleva su nota de provisionalidad y su condición de
  reemplazo.
- **Bloqueantes confirmados con ITESA (recurrentes, van a Anexo B de la Guía de Implementador
  de cualquier cliente con PrestaShop):**
  - **Precio real por medida:** que el agente devuelva el precio real de cada medida es un
    bloqueante histórico repetido — confirmar explícitamente en cada cliente nuevo antes de dar
    por sentado que funciona.
  - **Cuadro "Detalles de producto" no expuesto:** PrestaShop tiene un cuadro de atributos
    (ej. Base, Tapa, Formato en BETROX) que hoy el agente NO puede leer — solo lee título y
    descripción. Esto bloquea que el agente responda forma o material de base sin derivar. Pedir
    a ITESA que exponga ese cuadro es un pendiente de Go-Live, no una mejora de Fase 2.

### ERP interno vs ERP integrado — dos casos distintos, no confundir

No todo sistema de gestión del cliente se integra al agente. Distinguir:

- **ERP interno, fuera de alcance del agente** (caso BETROX/Bejerman): sincroniza
  administración, producción y stock, de uso exclusivo del equipo. El agente no lo consulta ni
  lo necesita. Se documenta en el Setup de la Guía de Implementador como "NO se integra", para
  que quede explícito que fue una decisión, no un olvido.
- **ERP integrado a medida** (ver `AUREA-Acuerdo-Alcance-y-Objetivos`, bloque de integraciones):
  cuando el cliente sí necesita que el agente consulte o escriba en su ERP (ej. sincronizar
  stock y precios), se evalúa como integración a medida vía **Prometheo Connect / Atlas**, se
  cotiza aparte y se define su alcance como cualquier otra integración de este archivo.

**Criterio de decisión:** preguntar en discovery si el agente necesita LEER o ESCRIBIR algo del
ERP para conversar con el lead. Si la respuesta es no (el ERP es puramente administrativo/interno),
queda fuera de alcance sin más. Si la respuesta es sí, es integración a medida por Connect/Atlas.

### PrestaShop — comportamientos confirmados (ampliación con caso BETROX)

Qué devuelve y por lo tanto se consulta (nunca se hardcodea): precio por medida, medidas incluida
la ALTURA, forma, variantes, colores, disponibilidad, link, material de tapa, material de base y
fotos. Reglas de uso: mapeo estricto de campos (una medida recibe etiqueta largo/ancho/diámetro/
altura solo si PrestaShop la devuelve así; nunca por posición); el dato que devuelve se da
(prohibido "el catálogo no lo especifica" si está en el resultado); resultado parcial es un tercer
caso distinto de "sin resultados" y de "sin precio" (se acota o se da lo que vino, sin frase de
sistema).

Lo que NO se le pide: la categoría "destacados" no se consulta en vivo (lista hardcodeada con
mantenimiento manual hasta que ITESA lo habilite); precios cerrados de productos a medida (se
derivan).

Restricciones de plataforma confirmadas: (a) el **orden de envío de varias imágenes no es
controlable** → una foto por mensaje, identificada por nombre del producto, no por posición ("la
del medio" no se usa); (b) el envío por nombre de archivo no estaba documentado → verificar con
soporte qué garantiza la integración antes de diseñar sobre un mecanismo; (c) **el adjunto pisaba
el texto de la respuesta** (resuelto por Prometheo): al enviar foto/video, al cliente le llegaba
solo la frase de adjuntar; era de plataforma, no de prompt; una vez resuelto, las reglas de
"mensajes separados" quedaron huérfanas y se revirtieron por "el archivo complementa, nunca
reemplaza".

**Checklist para el próximo cliente con PrestaShop:** qué atributos devuelve este catálogo (no
asumir que son los de otro cliente); si "destacados" se consulta en vivo o se mantiene a mano;
cómo se comporta el envío de archivos (verificar que tenga el fix del adjunto); asumir que el orden
de varias imágenes no es controlable; toda regla sobre archivos se escribe como resultado esperado,
no como mecánica de envío.

## Método transferible de integración (doctrina general, no solo PrestaShop)

> Salió del caso del adjunto de BETROX, pero aplica a cualquier integración. Es el mejor caso real
> del ciclo completo prompt → mitigación → escalar → solución de plataforma → revertir huérfano.

- **La regla de las tres veces.** Si una regla se refuerza tres veces con redacciones correctas y
  sigue fallando, el fallo no es de redacción. Frenar, leer todas las evidencias juntas buscando un
  patrón de ejecución, y considerar que es de plataforma. (Es el mismo criterio del patrón 11 y de
  la regla del barrido: una regla muy reforzada que igual falla es sospechosa.)
- **Separar la mitigación de la solución.** Mientras la plataforma no arregla la causa, se puede
  mitigar en el prompt (ej. texto y archivo en dos mensajes). Pero la mitigación **se marca como
  tal**: cuando la plataforma resuelve la causa, la mitigación queda huérfana (describe un bug que
  ya no existe) y hay que revertirla. No revertirla ensucia el prompt.
- **El prompt define el RESULTADO, no el MECANISMO.** La mejor versión de una regla de este tipo no
  dice "mandá el texto en un mensaje y el archivo en otro" (asume cómo funciona técnicamente el
  envío); dice "el archivo complementa la respuesta y nunca la reemplaza; si falta el texto, la
  respuesta está incompleta". Define el resultado y deja el mecanismo del lado de la plataforma. Es
  más robusto: si mañana cambia la mecánica del envío, la regla sigue valiendo. **Es la regla de
  oro de la integración.** Conecta con el principio transversal 17.
- **Escalar con hipótesis y evidencia, no con queja.** Al proveedor se le lleva el patrón concreto,
  las capturas y una pregunta puntual y técnica ("¿el envío de un archivo anula el texto de esa
  interacción?"), no "el agente no saluda". Eso permite que lo arreglen del lado correcto. Ver
  `gestion-proveedor-itesa.md`.

**Regla de oro:** el prompt describe QUÉ tiene que recibir el cliente, no CÓMO lo entrega
técnicamente la plataforma. Una regla que asume el funcionamiento interno de la integración es
frágil; una que define el resultado es robusta.

---

## PLACEHOLDERS DE MENSAJE (seguimientos y recordatorios) — ver framework-seguimientos.md

Los placeholders de este archivo son de **archivo** (`/Render-`, `/Brochure-`, referenciados
desde el prompt). Existen otros dos sistemas de placeholder, de **mensaje**, que viven en
`framework-seguimientos.md`: los de seguimientos (variables mapeadas en la plantilla de Meta) y
los de recordatorios (sintaxis de barra `/Nombre` libre en el texto). Los tres sistemas no son
intercambiables — ver la tabla comparativa en ese archivo antes de diseñar un prompt o una guía
nueva.

---

## MAPEO ESTRICTO DE CAMPOS — anti-alucinación de datos (transversal a las tres fuentes)

Regla dura confirmada en los dos prompts vivos (Martina 5.7, Catalina 1.1), transversal a
cualquier integración. El agente **no reinterpreta un dato para completar una respuesta**:

- Una dimensión o un valor solo recibe una etiqueta si la integración la devuelve con esa
  etiqueta. **Nunca se convierte un valor por posición** (el segundo número de una medida
  compuesta no es "la altura" por intuición; un valor suelto no es "el piso" por orden).
- Etiquetas condicionadas a otro atributo: "diámetro" solo si la forma es redonda o hay campo
  explícito; "frente/contrafrente" solo si viene ese campo. Un dato no se deduce de otro.
- **Consistencia entre turnos:** un atributo ya validado en la conversación no cambia en un
  turno posterior sin una consulta nueva que lo justifique. Si un resultado nuevo contradice
  a uno anterior, no se elige al azar: se verifica con el equipo.
- **Autochequeo antes de enviar:** forma declarada + etiquetas de medida + valores deben ser
  compatibles entre sí.

Es la bajada operativa del principio transversal 11 (exactitud del dato por encima de la
fluidez) al nivel de la integración.

## INCONSISTENCIA DE RESULTADOS Y PARCIALIDAD NO DECLARADA (límite de plataforma)

Hallazgo de campo (reporte a ITESA, agente Martina / Tokko): ante consultas equivalentes o
cada vez más amplias, la búsqueda puede devolver **subconjuntos distintos** de resultados sin
criterio visible, y **sin avisar que el resultado es parcial**. Esto tiene una consecuencia
doctrinaria importante:

- **El agente no puede declarar parcial lo que la integración no le dice que es parcial.** La
  regla "aclará que mostrás algunos de N" solo se puede cumplir si el agente conoce el total.
  Si la integración no devuelve el total ni marca truncamiento, el agente no tiene cómo saber
  que la lista quedó incompleta.
- **Mitigación desde el prompt (lo que sí controlamos):** el panorama de entidades (qué
  proyectos/categorías existen) sale del catálogo embebido, que es completo y estable; las
  unidades/precios salen de la integración, consulta por consulta. Nunca se afirma "no hay" a
  partir de un resultado parcial: una ausencia solo se afirma contrastando contra el catálogo
  embebido. Esto conecta con la "verificación del lote" de la sección de Sheets.
- **Lo que depende de ITESA (pregunta abierta, va a `pendientes-itesa.md`):** si hay límite de
  resultados por consulta, si el agente puede saber que la respuesta quedó truncada, si puede
  conocer el total, y cómo se consulta a nivel entidad (panorama) vs unidad. Hasta que ITESA
  responda, la mitigación de arriba es el techo de lo que el prompt puede hacer.

---

## SISTEMA DE PLACEHOLDERS PROVISORIOS (transversal a las tres fuentes)

Patrón de diseño que aparece en los tres prompts: el prompt se diseña con **huecos marcados**
que el consultor o el cliente reemplazan por assets reales después. El prompt los pide a
medida que se arma, para reemplazarlos bien más tarde.

- **Qué es un placeholder.** Una referencia interna a un archivo que el sistema adjunta
  (render, brochure, plano, foto, video, carta de colores). El lead nunca ve el texto del
  placeholder: ve el archivo adjunto. Si el placeholder aparece como texto en la respuesta,
  está mal.
- **Estado de cada placeholder (parte del diseño).** Cada placeholder lleva su estado:
  cargado / pendiente de subir / a comprimir (peso > límite). Ejemplos reales: en EDFAN,
  `/Render-SUITCH-1` marcado ✗ (pendiente que el cliente lo suba) y brochures marcados ⚠️
  (comprimir a <15 MB); en BETROX, el Apéndice mapea producto↔archivo y `[VIDEO_MOB_URBANO_2]`
  está pendiente de carga.
- **Regla de exactitud.** El nombre del placeholder es el nombre EXACTO del archivo cargado
  (verbatim, con sus espacios y mayúsculas). Un carácter distinto rompe el adjunto. Por eso
  el mapeo de assets se entrega con los nombres tal cual del Drive.
- **Por qué importa para el método.** Permite diseñar el prompt completo antes de tener los
  assets finales: se deja el hueco con su estado, se entrega, y el reemplazo por el archivo
  real es un paso posterior y trazable. El estado "pendiente" es además la lista de lo que
  hay que pedirle al cliente.
