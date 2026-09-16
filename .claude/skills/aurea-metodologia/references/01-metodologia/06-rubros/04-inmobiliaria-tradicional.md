# 04 — Rubro Inmobiliaria Tradicional

**Patrones del rubro inmobiliaria tradicional (cartera de propiedades de terceros).**

> ⚠️ **ESTADO: SIN CLIENTE FUNDACIONAL TODAVÍA**
> Este archivo es un placeholder estructurado con hipótesis basadas en investigación general del rubro y referencia parcial (Paganini Inmobiliaria). Cuando aparezca el primer cliente real, se valida y se completa.

---

## Definición del rubro

**Aplica a:** clientes que comercializan propiedades de terceros (no proyectos propios):
- Inmobiliarias residenciales
- Inmobiliarias comerciales
- Brokers independientes con cartera
- Plataformas locales de listados con vendedores asociados

**NO aplica a:** desarrollistas inmobiliarios con proyectos propios (ver `01-real-estate.md`).

---

## Diferencias clave vs Desarrollistas

| Dimensión | Desarrollista | Inmobiliaria tradicional |
|---|---|---|
| Catálogo | Set cerrado y propio (10-30 proyectos) | Cartera abierta (cientos de propiedades) |
| Tipología macro | Proyecto | Propiedad individual |
| Stock | Propio, controlado | De terceros, dinámico |
| Relación con vendedores | Empleados / equipo propio | Vendedores asignados a cada propiedad |
| Decisión de precio | Centralizada | Negociada con dueño |
| Velocidad de rotación | Lenta (años por proyecto) | Rápida (meses por propiedad) |
| Canal externo | Inmobiliarias intermediarias (B2B) | Otros brokers / portales |

Estas diferencias hacen que la tipología macro, los embudos y las variables sean **estructuralmente distintas**.

---

## Particularidades del rubro (HIPÓTESIS)

### 1. Tipología macro = propiedad individual

La unidad central NO es el proyecto, es la **propiedad**. Cada propiedad tiene:
- ID único (ficha.info o portal interno)
- Tipo (casa, depto, ph, local, terreno)
- Operación (venta, alquiler)
- Vendedor asignado externo
- Estado (disponible, reservada, vendida)

### 2. Catálogo dinámico

La cartera cambia constantemente. Modalidad B obligatoria (integración con catálogo externo). Hardcodear propiedades en el prompt es inviable.

### 3. Variable `vendedor_asignado_externo`

A diferencia de un desarrollista (donde el equipo está dentro), una inmobiliaria asigna cada propiedad a un vendedor específico (a veces externo). El agente tiene que:
- Identificar qué propiedad consulta el lead
- Derivar al vendedor asignado de esa propiedad

### 4. Rapidez de calificación

El ciclo de decisión es más corto que en desarrollista (típicamente 1-6 meses contra 6-24 meses). Implica:
- Calificación rápida en pocos mensajes
- Menos follow-ups que en desarrollista
- Tono más operativo, menos consultivo

### 5. Cross-sell por tipo de propiedad

Si el lead consulta por casa y no aparece nada → ofrecer depto. Si busca alquiler y no aparece → ofrecer venta si presupuesto alcanza. El cross-sell por tipo es natural en el rubro.

### 6. Múltiples operaciones simultáneas

Una inmobiliaria atiende:
- Venta
- Alquiler tradicional
- Alquiler temporario
- Alquiler comercial

La variable `operacion` segmenta estos casos desde el primer mensaje.

---

## Patrones macro HIPOTÉTICOS

### Variables transversales propuestas

| Variable | Tipo | Notas |
|---|---|---|
| `proceso_actual` | Opciones | venta, alquiler, faq, derivacion |
| `tipo_contacto` | Opciones | comprador, locatario, vendedor_propio, broker_externo |
| `operacion` | Opciones | venta, alquiler_residencial, alquiler_temporario, alquiler_comercial |
| `tipo_propiedad` | Opciones | casa, depto, ph, local, terreno, oficina |
| `zona_interes` | Texto | Barrios o zonas (cartera amplia, libre) |
| `presupuesto` | Precio | USD o ARS |
| `cantidad_ambientes` | Número | Para residencial |
| `propiedad_id` | Texto | ID en ficha.info / portal interno |
| `vendedor_asignado_externo` | Texto | Nombre del vendedor asignado a la propiedad |
| `canal` | Opciones | whatsapp, instagram, zonaprop, argenprop, web, referido |
| `tipo_derivacion` | Opciones | comercial, alquileres, administrativa, legal, vendedor_externo |

### Smart Tags

Modelo v7: 2 tags base. Mismo patrón.

### Embudos típicos propuestos

3-4 embudos:

1. **Venta** (consulta → calificado → visita_agendada → visita_realizada → reserva → cerrado)
2. **Alquiler** (consulta → calificado → visita → reserva → contrato_firmado)
3. **FAQ y consultas generales**
4. **Derivación a vendedor externo** (cuando la propiedad consultada tiene vendedor específico)

### Seguimientos típicos propuestos

- Follow-up 1: 4-8hs después de info enviada (rubro más rápido que desarrollista)
- Follow-up 2: 24hs si no respondió
- Follow-up 3: 5 días (reactivación leve)
- Follow-up de visita: 2hs antes (recordatorio)
- Follow-up post-visita: 24hs después

---

## Reglas operativas propuestas

### Regla 1 — Identificar operación temprano

El agente tiene que identificar en los primeros 2-3 mensajes si la consulta es de venta o alquiler. Esto rutea a embudos distintos con procesos distintos.

### Regla 2 — Captura rápida de variables clave

En 3-5 mensajes el agente tiene que tener:
- `operacion`
- `tipo_propiedad`
- `zona_interes`
- `presupuesto`
- `cantidad_ambientes`

Si falta alguna, hacer una pregunta puntual. No saturar con cuestionario.

### Regla 3 — Cross-sell por tipo cuando no hay match

Si la búsqueda es muy específica y no aparece nada, ofrecer alternativa cercana:
- Busca casa → no hay → ofrecer depto con patio
- Busca alquiler → no hay → ofrecer venta si presupuesto alcanza

### Regla 4 — Derivación al vendedor de la propiedad

Cuando el agente identifica la `propiedad_id` específica que interesa al lead, deriva al `vendedor_asignado_externo` de esa propiedad. NO al equipo comercial general.

### Regla 5 — Catálogo dinámico, NO hardcodear

Todo va por integración con ficha.info, portal interno o equivalente. El prompt solo conoce la estructura general (zonas, tipos, rangos de precio).

### Regla 6 — Tono profesional cercano

A diferencia del desarrollista (más consultivo), inmobiliaria tradicional es más operativo. Mensajes cortos, directos, voseo. Menos asesoramiento, más eficiencia para coordinar visitas.

---

## KPIs típicos del rubro (HIPÓTESIS)

| KPI | Cómo se mide | Target inicial estimado |
|---|---|---|
| % de leads calificados | Leads con variables clave / Total | 80%+ |
| Tiempo a primera respuesta | Mediana | < 5 minutos |
| % visitas agendadas | Visitas / leads calificados | 30-45% |
| % visitas realizadas | Visitas realizadas / agendadas | 70-80% |
| Tasa de cierre | Reservas / visitas realizadas | 10-20% (más rotación que desarrollista) |
| Tiempo de ciclo (consulta → reserva) | Mediana en días | 30-60 días |

---

## Glosario rubro-específico (a expandir)

| Término | Definición |
|---|---|
| Cartera | Conjunto de propiedades que la inmobiliaria comercializa |
| Vendedor asignado | Persona responsable de una propiedad específica |
| Tasación | Valoración del valor de mercado de una propiedad |
| Reserva | Compromiso firme de compra/alquiler |
| Boleto | Contrato de compraventa |
| Comisión | Porcentaje que cobra la inmobiliaria por intermediar |
| Tenant | Locatario (alquiler comercial) |
| Lease | Contrato de alquiler |
| Hot leads | Leads con alta intención de compra |

---

## Errores frecuentes propuestos (a validar)

| Error | Consecuencia | Solución |
|---|---|---|
| Hardcodear propiedades en el prompt | Catálogo se desactualiza diariamente | Modalidad B obligatoria |
| No identificar operación temprano | Rutea mal y pregunta cosas irrelevantes | Operación en los primeros mensajes |
| Saturar con cuestionario de calificación | Lead abandona | 5-7 preguntas máximo, distribuidas naturalmente |
| Derivar a comercial general en vez de vendedor asignado | Mala experiencia + pérdida de relación vendedor-propiedad | Capturar propiedad_id + derivar a vendedor específico |
| Tono consultivo largo | Cliente se aburre | Tono operativo, mensajes cortos |
| Ignorar cross-sell por tipo | Pérdida de oportunidad | Si no hay match exacto, ofrecer alternativa cercana |

---

## Qué validar con el primer cliente del rubro

Cuando aparezca el primer cliente de inmobiliaria tradicional, validar:

1. ¿`propiedad_id` es variable obligatoria o flexible según cliente?
2. ¿`vendedor_asignado_externo` se modela como variable de texto o se resuelve por Tokko nativo?
3. ¿Los 3-4 embudos propuestos son los correctos?
4. ¿Alquiler temporario y alquiler residencial van en mismo embudo o separados?
5. ¿La rapidez de calificación se cumple en la práctica?
6. ¿El cross-sell por tipo es estructural o decisión por cliente?

Si las respuestas son consistentes, **estos patrones pasan a [VALIDADO PARCIAL]**.
Cuando aparezca un segundo cliente y se confirmen, pasan a [VALIDADO] y la skill vertical puede crearse.

---

## Referente parcial existente

**Paganini Inmobiliaria** (no es cliente activo pero hay perfil de referencia disponible):
- Vertical inmobiliaria con catálogo externo (ficha.info)
- Rapid calificación: operación + tipo + presupuesto
- Listados estructurados con bullets
- Cross-sell por tipo (casa → depto)
- Derivación a vendedor nombrado por WhatsApp
- Tono profesional cercano, voseo, sin emojis
- Memoria de sesión

Usar como referencia parcial mientras no haya cliente activo del rubro.

---

## Integración con catálogo digital (ficha.info / Tokko / portales)

En inmobiliaria tradicional la integración estándar es **ficha.info** o **Tokko CRM**. A diferencia del rubro desarrollista, acá el catálogo son **propiedades de terceros** (los propietarios son externos a la inmobiliaria) y el stock es mucho más dinámico — entran y salen propiedades a diario.

Las 6 reglas de integración con catálogo del Reglas Diseño de Prometheo by AUREA (Reglas 16-21) **aplican siempre** en este rubro. Ver `../02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` para el detalle completo.

**Cómo aplicar en inmobiliaria tradicional:**

| Regla | Aplicación específica al rubro |
|---|---|
| 16 — No bloquear consultas atómicas | El lead pregunta "¿tienen alquileres en Belgrano?" antes de identificarse. El agente responde con info de ficha.info sin pedir calificación previa. |
| 17 — Búsqueda separada de consulta | Tools `[BUSCAR_PROPIEDAD]`, `[CONSULTA_DETALLES]`, `[OBTENER_LINK_FICHA]`. Búsqueda por: zona, ambientes, operación (venta/alquiler), precio. |
| 18 — Match tolerante | El lead nombra "Belgrano R", "Belgrano residencial", "el de Cabildo y Olleros" — el match tolerante resuelve a propiedades específicas. Si hay varias, repregunta. |
| 19 — URLs ficha.info son válidas | Las URLs devueltas por ficha.info (link a la ficha de la propiedad, link a publicaciones en portales como Zonaprop / MercadoLibre Inmuebles) son canónicas. Las URLs externas (videos de tour virtual, planos extras, materiales adicionales) viven en una fuente externa de acceso compartido (Drive, YouTube, Vimeo, Notion, Dropbox, Sheets, etc.) que el cliente elige. **Paso obligatorio en Etapa 2:** preguntar "¿usás ficha.info, Tokko, o ambos?", "¿qué materiales externos tenés disponibles por propiedad?" y "¿en qué fuente los querés tener?" |
| 20 — Naming unificado | Cada propiedad tiene `clave_interna` (típicamente el ID interno de ficha.info o Tokko). Tabla de 3 columnas: clave_interna + variantes técnicas (código de propiedad en ficha.info, código MLS, código MercadoLibre) + variantes del lead (jerga: "el de Cabildo", "el departamento de Belgrano con balcón", "la casa de Olivos"). |
| 21 — Prioridad de respuesta | Lógica de zonas, FAQs del rubro (cómo se firma una reserva, qué docs piden), política de comisión: hardcoded. Disponibilidad y precio: ficha.info. Visita a la propiedad y firma: derivar al agente humano. |

**Particularidad del rubro:** el stock **cambia más rápido que en cualquier otro rubro**. Propiedades se sacan del listado en horas (se alquilan, el dueño se arrepiente, se cambia el precio). La integración tiene que ser en tiempo real, sin cache.

**Otra particularidad:** las propiedades pueden estar publicadas en **múltiples portales** (Zonaprop, MercadoLibre Inmuebles, Argenprop, Properati). El agente debe entender que el link a la propiedad en ficha.info es la fuente de verdad, pero puede haber links externos al portal específico que el lead vio.

**Productos típicos del rubro que SÍ se consultan en ficha.info:**
- Propiedades por zona/barrio
- Disponibilidad en tiempo real
- Precio actual de venta o alquiler
- Link a la ficha completa
- Fotos y plano de la propiedad

**Productos que NO se consultan (derivar a humano):**
- Coordinación de visitas a la propiedad
- Negociación de precio
- Trámite de reserva o seña
- Validación de papeles del lead (DNI, garantes, etc.)
- Propiedades exclusivas (sin publicar todavía)

**Caso de referencia:** Paganini Inmobiliaria (referencia parcial, no es cliente activo de AUREA Hub pero su workflow sirve como inspiración).

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Reglas Diseño de Prometheo by AUREA | `../02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` |
| Rubro Real Estate (desarrollistas) | `01-real-estate.md` |
| Reglas de integración con catálogo (ficha.info, Tokko, portales) | `../02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` |
| Operativa Etapa 2 | `../02-ETAPA2-Diseno/01-operativa-y-decisiones.md` |
