---
consultar-cuando: cliente de mobiliario (muebles, equipamiento, deco, mobiliario urbano), diseño o iteración de su prompt/CRM
disparadores: "mobiliario", "muebles", "BETROX", "PrestaShop", "showroom", "cross-sell de muebles", "mobiliario urbano"
fuente-única-de: lógica comercial del rubro mobiliario
combina-con: principios-transversales-agente, integracion/prestashop, 00-sistema-fija-flexible
---

# 02 — Rubro Mobiliario

**Patrones consolidados del rubro mobiliario.**

---

## Definición del rubro

**Aplica a:** clientes que fabrican y/o venden:
- Muebles interior / exterior
- Muebles de baño y cocina (integrales)
- Mobiliario urbano (espacios públicos, plazas, parques)
- Equipamiento de hogar / oficina con catálogo de modelos identificables

**Características que definen el rubro:**
- Modelos con nombre propio (POSITANO, ATENEA, JAPAN, SIT 45, etc.)
- Showroom físico como punto de venta principal
- Mix de productos estándar + configurables + a medida
- Ciclo de decisión largo (1-3 meses consumidor final, hasta 6 meses B2B)
- B2B estructural con arquitectos, paisajistas, decoradores

**Clientes documentados:** BETROX (prototipo).

---

## Particularidades del rubro

### 1. Showroom como punto de conversión #1

El showroom es el activo comercial principal. Todo el agente está orientado a llevar al lead al showroom cuando sea posible.

Prioridad de conversión:
1. Visita física al showroom
2. Videollamada de co-diseño (si no puede venir)
3. Link directo al producto (último recurso, solo producto estándar)

### 2. Tipología macro = línea de producto

La unidad central del CRM es la línea de producto:
- Interior
- Exterior
- Baño_cocina
- Mobiliario_urbano
- Raw (productos crudos / industriales)

Cada línea tiene modelos específicos con nombre propio.

### 3. Mix de personalización

Cada cliente tiene un mix de:

| Tipo | Características | Comportamiento del agente |
|---|---|---|
| **Estándar** | Producto fijo, precio fijo, en stock | Puede cotizar autónomamente |
| **Configurable** | Producto base + opciones (color, medida en rango) | Da rangos, deriva para cotización final |
| **A medida** | Pieza única según specs | Captura datos y deriva siempre |
| **Proyecto integral** | Múltiples piezas coordinadas | Captura datos y deriva |

La variable `tipo_compra` segmenta estos casos.

### 4. B2B estructural

Los profesionales (arquitectos, paisajistas, decoradores) representan típicamente 25-40% del volumen.

**Lo que NO cambia entre B2B y B2C:**
- El precio (no hay tarifa diferenciada)

**Lo que SÍ cambia:**
- El trato (más técnico, conoce el producto)
- El flujo (foco en co-diseño en showroom)
- Los materiales adicionales (bloques CAD si aplica, fichas técnicas detalladas)
- La marca de agua en fotos (siempre, incluso para profesionales)

### 5. Ciclo de decisión largo

Implica:
- Más follow-ups que en rubros de ciclo corto (4-7 follow-ups típicos)
- Mensajes no agresivos (no presionar a cerrar)
- Reactivación de leads fríos a 60 días con tono distinto

### 6. Terminología técnica diferenciadora

Algunos rubros tienen materiales o procesos con jerga técnica:
- Hormigón liviano vs hormigón pulido vs hormigón vibrado
- Maderas: lapacho vs paraíso vs anchico
- Acabados: lacado, encerado, aceitado

El agente tiene que poder desambiguar y usar el lenguaje correcto.

---

## Patrones macro confirmados

### Variables transversales típicas

| Variable | Tipo | Notas |
|---|---|---|
| `proceso_actual` | Opciones | venta, faq, postventa, b2b, outlet |
| `tipo_usuario` | Opciones | consumidor_final, arquitecto, paisajista, decorador, constructora, municipio, cliente_recurrente, desconocido |
| `linea_producto` | Opciones | Set específico del cliente |
| `tipo_compra` | Opciones | estándar, configurable, a_medida, proyecto_integral |
| `producto_de_interés` | Texto | Modelo específico (libre por cantidad de modelos) |
| `medida_solicitada` | Texto | Medidas tal como las dice el cliente |
| `ciudad_zona` | Texto | Ciudad/zona del cliente o entrega |
| `canal` | Opciones | whatsapp, instagram, web, email, referido, meta_ads |
| `tipo_feedback` | Opciones | positivo, queja, sugerencia, ninguno |
| `tipo_derivacion` | Opciones | comercial, cocina_bano_cotizar, mu_brochure, postventa, b2b_especial, administrativa |
| `severidad_caso` | Opciones | alta, media, baja (en mobiliario típicamente "media" o "baja") |

### Smart Tags

Modelo v7: 2 tags base.
- `#seguimiento_activo`
- `#derivar_a_humano`

### Embudos típicos

5 embudos:

1. **Venta** (consulta → calificado → cotización → showroom → seña → producción → entrega)
2. **FAQ**
3. **Postventa** (reclamos de service, raros: 1 cada 3 meses)
4. **B2B Profesional** (arquitectos, paisajistas, decoradores)
5. **Outlet** (típicamente Fase 2)

### Seguimientos típicos

Por el ciclo largo:

- Follow-up 1: 24-48hs después de info enviada
- Follow-up 2: 7 días si no respondió
- Follow-up 3: 15-21 días (reactivación leve)
- Follow-up 4: 60 días (reactivación profunda)
- Follow-up de showroom: 1 día antes de la visita
- Follow-up post-showroom: 2-3 días después

---

## Reglas operativas específicas

### Regla 1 — Showroom es el cierre prioritario

Cuando el agente identifica que un lead está calificado, su próximo paso siempre es proponer visita al showroom. Si no puede, videollamada. Si tampoco, link al producto.

### Regla 2 — Cross-selling sutil

Para profesionales, los cross-sells naturales son:
- Mesa + bancos
- Mesada + bacha
- Mueble interior + mueble exterior coordinados

Pero NO agresivo. El cross-sell se hace en el showroom, no por chat.

### Regla 3 — Precio igual B2B y B2C

A diferencia de otros rubros, en mobiliario el precio es igual para ambos. El profesional pone su margen encima — eso lo gestiona el arquitecto, no el cliente AUREA.

### Regla 4 — Plazos siempre como estimado

Las piezas a medida no tienen plazo exacto. Comunicar siempre como rango ("15-30 días", "aproximadamente 3 meses").

Si el lead presiona por plazo exacto → derivar a humano.

### Regla 5 — Marca de agua siempre

Las fotos del catálogo van con marca de agua. Si un profesional pide fotos sin marca de agua para presentar a su cliente → derivar (decisión del equipo).

### Regla 6 — Cliente recurrente como valor de tipo_usuario

NO se modela como Smart Tag. Si el lead se identifica como recurrente, agente lo trata con tono cordial reconociendo el vínculo y deriva sin pasar por filtros.

### Regla 7 — Bloques CAD para profesionales

Algunos clientes ofrecen bloques CAD descargables para que arquitectos puedan diseñar incluyendo los modelos. Si aplica, hardcodear el link al recurso en sección 7 del prompt.

---

## KPIs típicos del rubro

| KPI | Cómo se mide | Target inicial |
|---|---|---|
| % de leads calificados | Leads con variables transversales / Total | 75%+ |
| Tiempo a primera respuesta | Mediana | < 10 minutos |
| % visitas a showroom agendadas | Visitas agendadas / leads calificados | 30-50% |
| % visitas realizadas | Visitas realizadas / visitas agendadas | 70-85% |
| Tasa de cierre | Seña / visitas realizadas | 25-40% |
| Tiempo de ciclo (consulta → seña) | Mediana en días | 30-60 días B2C, 60-120 B2B |

---

## Glosario rubro-específico

Adaptar según el cliente. Ejemplos:

| Término | Definición |
|---|---|
| Showroom | Espacio físico donde se exhiben los productos |
| Pieza a medida | Producto fabricado específicamente para el cliente |
| Pieza estándar | Producto del catálogo con specs fijas |
| Configuración | Personalización dentro de opciones predefinidas |
| Seña | Anticipo que confirma el pedido y arranca producción |
| Plazo de producción | Tiempo desde seña hasta listo para entrega |
| Bloques CAD | Archivos digitales para diseño profesional |
| Co-diseño | Proceso colaborativo entre cliente y equipo en showroom |

---

## Errores frecuentes a evitar

| Error | Consecuencia | Solución |
|---|---|---|
| Tratar a profesional como B2C | Pierde el lead profesional | Identificar tipo_usuario temprano |
| Cotizar autónomamente piezas a medida | Cotización mal hecha | Solo derivar para a medida |
| Mensajes largos en WhatsApp | Satura al cliente | Mensajes cortos, lleva al showroom |
| Plazos exactos para a medida | Lead se enoja con desviaciones | Siempre "estimado" |
| Mandar fotos sin marca de agua | Pérdida de control de marca | Marca de agua siempre |
| Asumir showroom solo como cierre | Pierde cross-sell | Showroom es para mostrar variedad también |
| Crear tag por tipo de cotización | 10+ tags inmanejables | Variable tipo_derivacion con valores |

---

## Integración con catálogo digital (PrestaShop / Bejerman)

Casi todos los clientes de mobiliario tienen catálogo digital. Los precios y stock viven en e-commerce (típicamente PrestaShop) y a veces se sincronizan desde un ERP (Bejerman, Tango, similar).

Esto significa que las 6 reglas de integración con catálogo del Reglas Diseño de Prometheo by AUREA (Reglas 16-21) **aplican siempre** en este rubro. Ver `../02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` para el detalle completo.

**Cómo aplicar en mobiliario:**

| Regla | Aplicación específica al rubro |
|---|---|
| 16 — No bloquear consultas atómicas | El cliente final de mobiliario suele preguntar precio antes de identificarse. NO calificar antes de responder precio. |
| 17 — Búsqueda separada de consulta | Implementar 3 tools: `[BUSCAR_PRODUCTO]`, `[CONSULTA_PRECIO]`, `[OBTENER_LINK]`. El nombre del modelo viene en el mensaje del lead. |
| 18 — Match tolerante | El lead nombra "positano", "Positano 1.60", "la POSITANO" — todos resuelven al mismo modelo. |
| 19 — URLs PrestaShop son válidas | Las URLs devueltas por la API del e-commerce son canónicas. Las URLs externas (videos de aplicación o explicativos, fichas PDF de instalación) NO van hardcoded en el prompt — viven en una fuente externa de acceso compartido (Drive, YouTube, Vimeo, Notion, Dropbox, Sheets, etc.) que el cliente elige. **Paso obligatorio en Etapa 2:** preguntar al cliente "¿dónde tenés documentada la base del catálogo?", "¿hay URLs externas que el agente vaya a usar?" y "¿en qué fuente las querés tener?" |
| 20 — Naming unificado | Cada modelo tiene `clave_interna` (ej: `POSITANO_1.60`). Tabla de 3 columnas separadas: clave_interna + variantes técnicas del catálogo (SKU, nombre comercial) + variantes del lead (jerga: "positano", "la grande", "mesa redonda"). |
| 21 — Prioridad de respuesta | Política de envío y mantenimiento: hardcodeadas. Precio y stock: integración. Cotización personalizada: derivar. |

**Productos que típicamente NO se consultan en la integración (van por humano):**
- Mesadas/islas/bachas a medida (cotización por m²)
- Proyectos integrales (cotización por proyecto)
- Configuraciones especiales fuera de catálogo

**Productos que SÍ se consultan:**
- Mobiliario interior estándar (mesas, bancos, consolas)
- Mobiliario exterior estándar
- Mobiliario urbano de línea
- Accesorios y deco
- Productos con stock disponible (tipo ZATOH en BETROX)

**Caso de referencia:** la actualización V1.6 → V1.7 del prompt de Catalina (BETROX) aplica las 6 reglas. Ver entrega operativa de BETROX.

---

## Patrones en evaluación

| Patrón | Cliente | Estado |
|---|---|---|
| Outlet 2x al año | BETROX | Fase 2 |
| Programa de descuento por volumen B2B | (ninguno aún) | Hipótesis |
| Mobiliario para hoteles / proyectos | BETROX (tipo_compra = proyecto_integral) | Variable, no patrón |
| Sincronización ERP → PrestaShop para precios | BETROX (Bejerman) | Específico del cliente |

---

## Próximos clientes a sumar

Cuando aparezca un nuevo cliente de mobiliario, documentar:
- Nuevas líneas de producto que no estaban contempladas
- Variables idiosincráticas
- Programas comerciales propios

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Caso de referencia BETROX | `../08-casos-referencia/PROTOTIPO-betrox.md` |
| Skill vertical mobiliario | `../../02-skills/00-TRANSVERSAL/prometheo-vertical-mobiliario/SKILL.md` |
| Reglas Diseño de Prometheo by AUREA | `../02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` |
| Reglas de integración con catálogo (PrestaShop, Bejerman) | `../02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` |
| Operativa Etapa 2 | `../02-ETAPA2-Diseno/01-operativa-y-decisiones.md` |

---

## Lógicas comerciales del rubro (destiladas de feedback en producción)

> Destiladas de procesar el feedback de corrección de BETROX (Catalina) sobre el agente en
> producción. Específicas de mobiliario. Las que también se vieron en desarrollista subieron
> a `principios-transversales-agente.md` y no se repiten acá.

### Cascada de recomendación (el orden del embudo de producto)

Ante una consulta genérica ("qué mesas tenés", "busco algo para el living"), no se vuelca
catálogo: se guía por una cascada, de a una lógica por turno, cada una habilita la siguiente:

**AMBIENTE → USO → FORMA → MATERIALES → MEDIDAS → COLORES.**

- **Ambiente:** casi siempre se infiere, no se pregunta (una mesada de cocina es para
  cocina). Solo se pregunta cuando se mezcla de verdad (una mesa de comedor puede ir en
  interior o galería).
- **Uso/función:** pregunta directa sin fotos si no quedó claro ("¿baja tipo ratona o alta
  de comedor?").
- **Forma — el gran filtro.** Es el eje que más acota. Si el cliente pide una forma, se le
  muestra SOLO esa forma, nunca se le cambia. Si no tiene preferencia, se muestra una de cada
  forma que contraste.
- **Materiales:** la tapa siempre es del material insignia (en BETROX, hormigón); la base
  varía (madera, caño). El material de la base sale de la fuente, no se asume.
- **Medidas:** estándar cotiza directo; personalizada deriva.
- **Colores:** se aclara que no varían el presupuesto y se manda la carta; no se recomienda
  color.

### La foto como interfaz inicial de la venta

En mobiliario la foto abre, casi siempre: ante una consulta de producto, primero va la foto y
debajo el nombre + descripción sintética + el dato concreto + el cierre. Aunque el cliente ya
haya nombrado el producto, igual se le manda la foto (es lo que ancla la conversación
visual). Única excepción: si ya se mandó esa foto en la misma conversación, no se repite.

### Productos similares linkeados

Modelos con la misma forma pero distinta combinación de materiales se llaman distinto pero se
ofrecen como "el mismo modelo en otra combinación". El diseño de la base de datos del cliente
los debe tener linkeados para poder recomendarlos como similares.

### Apto interior/exterior es general, no se recalca por producto

Cuando el atributo "apto interior y exterior" es general de la marca, se aclara una vez y no
se repite producto por producto. No se pregunta "¿es para interior o exterior?" como filtro
si no aporta a acotar.

### Estándar cotiza / personalizado deriva

Producto estándar de catálogo → se cotiza directo consultando la fuente. Producto a medida
(mesadas de cocina/baño, islas, bachas integradas, cambio de medida + base) → no se da precio
cerrado, se recolecta info mínima (medidas aproximadas, fotos del espacio, color, ubicación) y
se deriva. La derivación a la persona del equipo (en BETROX, Mariana) no se nombra de entrada:
se presenta la cotización como algo que "hacemos nosotros" y el nombre aparece recién en el
handoff real (caso del principio transversal "no exponer la herramienta / autopercepción
comercial").

### Cross-sell proactivo por combos canónicos

BETROX vende ambientes, no piezas sueltas. El cross-sell es proactivo (lo ofrece el agente),
se dispara una sola vez cuando el cliente confirma interés en un producto, y se ancla a ese
producto. Combos típicos: mesada de cocina → isla/desayunador; mesa de comedor → mesa baja
y/o consola; mesa de exterior → asiento; mesada de baño → bacha. Regla fina: el asiento
depende de la forma de la mesa (banco para rectangular, puff para redonda).

### Showroom: semilla y cierre, no CTA genérico

Ver la pieza en persona es parte de cómo se compra un mueble. El showroom se planta como
"semilla" una sola vez (un comentario que no pide nada) mientras el cliente está enganchado,
y se ofrece de forma directa y persuasiva recién en el cierre por interés (cuando el cliente
dice "me gusta"). No se usa como CTA de cualquier turno.

### Plazo de entrega como dato de venta

Como se fabrica a pedido (sin stock), el plazo se abre con el dato ("40 a 60 días desde que
confirmás"), nunca con la limitación ("no tengo el plazo exacto"). El plazo ayuda a cerrar:
se da siempre que lo piden, corto y una vez.

### Link de PrestaShop con placeholder

El link del producto se pasa cuando el cliente lo pide o avanza, usando la URL que devuelve la
integración (nunca construida a mano). Si el flujo necesita un link cargado con datos del
cliente, eso no se promete: PrestaShop no lo soporta. (Ver doctrina PrestaShop en
`08-reglas-integracion-catalogo.md`.)

---

## Estructura de CRM confirmada — caso BETROX (segundo cliente real del rubro)

> Confirma y amplía lo anterior con un caso de implementación completa (Guía de Implementador
> BETROX v1, agente Catalina, PrestaShop). Ver también `06-estructura-guia-implementador.md` para
> la tabla comparativa completa entre los tres clientes de referencia.

### Distribución: modelo de destino único (variante válida, no todos los clientes tienen equipo múltiple)

A diferencia de real estate (EDFAN/G&D reparten entre varias personas por especialidad o zona),
mobiliario en BETROX tiene **un único destino de derivación** (Mariana), que después distribuye
internamente por fuera de Prometheo según el caso. Cuando el destino es único, **alcanza con la
acción Notificaciones** en las tags de handoff — no hace falta activar el feature de reparto
equitativo de leads. Antes de diseñar reglas de distribución complejas, confirmar en discovery si
el cliente realmente tiene más de un destino posible.

### B2B (profesional / municipio) sin embudo propio

El profesional y el municipio recorren el **mismo Embudo 1** que cualquier lead — no hay un
Embudo B2B separado como en real estate. Lo que los distingue es el **modo de trabajo**, capturado
en variables (`Modo Trabajo`: Catálogo / Co-diseño, `Referencias Recibidas`: Sí/No), no un
recorrido propio. El aviso a Mariana lo dan las tags de tipología que ya notifican (Profesional,
Municipio); cuando abre el lead, ve `Modo Trabajo` = Co-diseño y sabe que trae un proyecto. Ver la
regla de decisión completa (cuándo un B2B necesita embudo propio y cuándo no) en
`06-estructura-guia-implementador.md`.

### KPI de cierre — framing propio del rubro

Mobiliario prioriza la **Tasa de cierre** (cuántas conversaciones terminan en venta o seña) como
KPI final explícito, con el **showroom como el activo comercial número 1** (la visita presencial
es donde mejor cierra). Es un framing distinto al de real estate, donde el KPI principal es el
% de reuniones agendadas sobre calificados — en mobiliario la venta puede cerrar sin reunión
formal (showroom espontáneo, WhatsApp directo), así que el objetivo se mide en el cierre mismo,
no en el paso intermedio de la reunión.

### Producto/condición externa vs interés del lead — caso Outlet

Que un producto esté en la sección Outlet de PrestaShop es un atributo del **catálogo** (se
consulta en runtime). Que el lead busque oportunidad de precio es un **interés del lead**, se
guarda en su propia variable (`Outlet Interes`). No se mezclan: la condición del producto nunca
se usa para inferir o registrar el interés del lead, y viceversa. Patrón general documentado en
`06-estructura-guia-implementador.md`.

---

## Candidatos a transversal detectados en mobiliario (esperan confirmación en otro rubro)

> Vistos con fuerza en BETROX (Catalina), pero en un solo rubro. Viven acá hasta que un rubro
> distinto los confirme; ahí suben a `logica-comercial-transversal.md` (ver regla de promoción).

- **Presentar un producto es una unidad de cuatro partes** (título + foto + info + CTA): una foto
  sola o un dato suelto no es una presentación. En real estate aparece de refilón como "brochure
  siempre con imágenes"; falta confirmarlo explícito.
- **Cross-sell por regla de correspondencia** entre productos (no cualquier complemento con
  cualquier pieza), una vez y sin bloquear el avance. En BETROX: mesa redonda → puff, recta →
  banco. El equivalente real estate (cochera complementaria) no está confirmado como el mismo
  patrón.
- **Una línea puede tener reglas de venta propias:** dentro de un mismo catálogo, una línea con
  reglas distintas (no se personaliza, tiene su apertura, su taxonomía). En BETROX: mobiliario
  urbano estándar vs interior a medida. El equivalente real estate (pozo vs a estrenar) no está
  confirmado como el mismo patrón.
- **Segmentación propia de una línea en su apertura** (BETROX: público/privado en mobiliario
  urbano).
- **Fabricación a medida como diferencial recurrente** que se ofrece seguido, salvo en la línea
  exceptuada (BETROX: interior/exterior a medida; urbano estándar).
