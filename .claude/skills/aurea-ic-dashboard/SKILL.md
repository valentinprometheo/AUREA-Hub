---
name: aurea-ic-dashboard
description: Conductor de punta a punta para crear, actualizar o auditar un tablero de Inteligencia Comercial de AUREA (HTML autocontenido sobre Prometheo, Meta, Tokko y canales) para cualquier cliente (EDFAN, DRAKON, PAVIR, TKVA, EAF o nuevos). Ordena el trabajo en pasos y carga en cada uno la skill que corresponde (aurea-metodologia, aurea-ic-curaduria-del-dato, aurea-hub-criterio-calificacion-leads, aurea-ic-criterio-comercial, skills de canal, aurea-ic-performance-report, aurea-dashboard-design), y pide los insumos que falten antes de armar nada, incluida la definición de lead calificado del cliente. Usala SIEMPRE que se pida "armá el tablero", "tablero de IC", "dashboard de inteligencia comercial", "actualizá el tablero de [cliente]", "nueva quincena / nuevo mes del tablero", "auditá el tablero", o se comparta un export de Prometheo para reportar.
---

# Tablero de Inteligencia Comercial · conductor

Esta skill no reemplaza a las demás: **las ordena**. Cada paso carga una skill
especializada y no se pasa al siguiente sin cerrar el anterior.

Propuesta de valor que el tablero tiene que explicar adentro:
**Meta ve hasta el clic. Prometheo ve del clic a la venta. El cruce por ID de anuncio es el producto.**

## Estructura del tablero (pestañas)

La estructura de referencia es el tablero **EAF V3**. El canal no es una sección
aparte de la lógica: cada pestaña responde una de cinco preguntas del cliente.

| Pregunta | Pestañas |
|---|---|
| ¿Cómo venimos? | Panorama · Evolución |
| ¿Qué pide el mercado? | Venta · CRM · pestañas del rubro (en EAF: Cursos y cupos, Alumnos y ex alumnos, Demanda de cursos) · Criterio comercial · Insights |
| ¿Qué trajo resultado? | Meta Ads · Google Ads · Email Marketing · WhatsApp Marketing · Meta en Prometheo |
| ¿Qué hago ahora? | Audiencias (listas para la pauta: personalizados, similares, exclusiones) · recomendaciones con dueño |
| ¿De dónde sale esto? | Integraciones (fuentes, estado y última actualización) |

Pestañas que se suman cuando aplican:
- **Consumo de Tokens - CRM**: obligatoria en real estate (regla [FIJA] de la
  metodología) y recomendada en todas las cuentas con datos del panel de consumo.
- **Calidad de datos**: donde viven los faltantes y lo No reportable.

Un canal sin datos en el período no se borra: muestra un estado vacío diseñado.

---

## Cadena de skills (cómo se invocan)

En cada paso, **invocá la skill con la herramienta Skill** antes de trabajar el paso, no
alcanza con recordar su contenido. Orden y nombres:

| Paso | Skill |
|---|---|
| 1 | `aurea-metodologia` |
| 2 | `aurea-ic-curaduria-del-dato` |
| 3 | `aurea-hub-criterio-calificacion-leads` (solo el archivo del rubro del cliente) |
| 4 | `aurea-ic-criterio-comercial` |
| 5 | `aurea-ic-email-marketing`, `aurea-ic-whatsapp-marketing` (según canales) |
| 6 | `aurea-ic-performance-report` |
| 7 | `aurea-dashboard-design` |

Si un nombre exacto no existe en el entorno, buscá la skill cuya descripción coincida
(las de esta familia se llaman "Aurea IC - ..." y "Aurea Hub - ..."). Si no existe
ninguna, seguí con `references/cuerpo-de-conocimiento.md` y **avisale al usuario qué
skill faltó**; nunca la reemplaces en silencio.

---

## Paso 0 · Insumos (pedí lo que falte, no supongas)

| Insumo | Obligatorio | Si falta |
|---|---|---|
| Cliente y rubro | Sí | Preguntar |
| **Definición de lead calificado y hot lead del cliente** (Doc 1, bloque B3, o formulario de reunión) | Sí | Usar el molde del rubro rotulado "propuesta a validar". El número de calificados no titula |
| Período (quincena o mes) y período anterior para deltas | Sí | Preguntar |
| Export de Prometheo (contactos, tags, variables, conversación) | Sí | No se arma el tablero |
| Línea base del discovery (bloque B10: velocidad, calificados, capacidad, satisfacción, ventas) | Recomendado | "¿Cómo venimos?" compara solo contra el período anterior |
| Tablero anterior del cliente, si existe | Si es actualización | Se arma desde cero |
| Perfil de venta del cliente y capa variable elegida | Sí | Resolver en el paso 4 |
| Panel de consumo de IA de Prometheo (USD por mes, reparto, cortes de saldo) | Real estate: sí | Sin pestaña de tokens; se declara |
| Export de Meta (gasto, alcance, por anuncio y día) | No | Faltante de integración: sin CPL ni ROAS, se declara |
| Tokko (catálogo) | Solo real estate | "Zona con proyecto" y "tipología existente" se aproximan desde el export y se declara |
| Campañas de email / WhatsApp masivo | Si las hubo | Estado vacío en esa pestaña |
| Registro de cierre del equipo | No | Faltante de proceso: no hay ciclo cerrado, se declara |

Requisito del producto: WhatsApp API oficial y plan Enterprise de Prometheo. Decí
explícitamente si los datos son **reales o modelados**.

## Paso 1 · CRM aguas arriba → `aurea-metodologia`

Entender cómo está diseñado el CRM del cliente antes de leer el export: embudos (cada
etapa es una Smart Tag), una tag por dimensión, variables padre e hija condicional,
corte embudo del agente vs embudo humano. Lo que el CRM no registró no se puede reportar.

Cargá solo la rebanada que el tablero usa: el rubro, `inteligencia-comercial-producto.md`
y, si hay dudas de captura, `embudos-y-tags.md`. No cargues la metodología entera.

## Paso 2 · Curaduría del dato → `aurea-ic-curaduria-del-dato`

Correr su procedimiento de auditoría completo antes de diseñar una sola card:
cobertura real por columna, escalera de evidencia, base curada, denominadores
declarados, citas, faltantes por tipo.

Salida de este paso: una tabla variable → cobertura → origen → nivel → pestaña donde vive.

## Paso 3 · Calificación de leads → `aurea-hub-criterio-calificacion-leads`

Cargá el SKILL y **solo** el archivo del rubro del cliente. Con la definición del cliente:

1. **Separar antes de calificar.** La base curada sale de la variable "Tipo de contacto":
   solo el comprador entra a la calificación; B2B, proveedores y similares van aparte.
2. **Calificados = obligatorios + al menos k de n sumas**, con la regla del cliente.
   Nunca "cantidad de variables completas" ni un criterio propio de AUREA.
3. **Rango estricto y amplio** cuando hay condiciones aproximadas (por ejemplo, sin
   catálogo de Tokko, o con variables que mezclan lo que ofreció el agente con lo que
   pidió el lead). Se dice qué falta para que sea exacto.
4. **Por qué no califican**: desglose por condición que falta (sin obligatorio, menos
   de k sumas, No Fit con motivo).
5. **Hot leads** (tag de prioridad, con 1 señal alcanza, plazo en días): cantidad, hot
   sin seguimiento ni derivación, hot que no califican, tiempo de derivación en minutos
   y ruteo registrado.
6. **Etapa declarada vs etapa por evidencia**: la evidencia es la definición del
   cliente. Se muestran las dos columnas mientras no converjan.
7. **Cambio de criterio**: si el número cambió por definición, el tablero muestra el
   anterior y el nuevo.
8. **Sin benchmark de % de calificados.** La meta sale de la línea base del cliente.
9. Auditar la cuenta con `references/malas-practicas.md` y llevar cada hallazgo a
   Calidad de datos con su arreglo.

Caso de referencia (EDFAN, export al 08/10/2026, 874 consultas de compra): 252
calificados con la regla del cliente, 176 en la lectura estricta. El criterio anterior
de AUREA ("3 de 4 campos") daba 350 y sobreestimaba 98.

## Paso 4 · Criterio comercial → `aurea-ic-criterio-comercial`

Elegir la capa variable según el perfil del cliente, medir los cinco campos del núcleo
(problema, impacto, causa raíz, disparador, resultado de contacto) y decidir qué puede
mostrarse según su nivel de evidencia. Se lee **sobre los calificados del paso 3**: el
cruce impacto × disparador ordena a quién llamar primero dentro de los que ya califican.

## Paso 5 · Atribución y canales

- Atribución por ID de anuncio y calidad por anuncio (respuesta, identificación,
  **calificación con la definición del cliente**, hot leads, derivación) con la misma
  definición de cohorte en todo el tablero. Las reglas de atribución y ciclo de vida
  están en `aurea-ic-curaduria-del-dato`; detalle en `references/cuerpo-de-conocimiento.md`.
- **Solo si el período tuvo campañas de email:** invocá `aurea-ic-email-marketing`.
- **Solo si el período tuvo WhatsApp masivo:** invocá `aurea-ic-whatsapp-marketing`.
- **Audiencias:** cada lista declara su tag de origen. Los calificados y los hot leads
  son la semilla de público similar (Lookalike desde 1.000 coincidencias reales); los
  clientes actuales y la no-demanda son exclusión. La señal a Meta (Conversions API,
  evento QualifiedLead) solo vale si el tag de calificado está bien cargado.
- **Consumo de Tokens - CRM** (con el archivo `references/ahorro-de-tokens.md` de la
  skill de calificación): costo por conversación, reparto del gasto (conversación,
  extracción, Smart Tags, soporte), cortes de saldo y conversaciones perdidas,
  mensajes a leads que escribieron una sola vez, y en real estate la línea aparte para
  no-demanda. Los cortes de saldo son también un faltante de datos: se declaran.

## Paso 6 · Lectura y recomendaciones → `aurea-ic-performance-report`

Con los números ya curados, escribí la lectura del período. No puede usar nada que la
curaduría haya dejado en Indicio o No reportable, no cita benchmarks genéricos y no usa
como meta las cifras sin fuente de las tablas de KPIs del rubro.

## Paso 7 · Diseño y armado → `aurea-dashboard-design`

Doctrina Básico / Avanzada (un número, un nombre), KPI con delta obligatorio, embudo
como pasos y no a escala, color semántico separado del de marca, modo oscuro, estados
vacíos, fecha de actualización por fuente, chips de cobertura y tags de nivel de la
curaduría. HTML autocontenido, assets en WebP, objetivo de peso menor a 250 KB.

## Paso 8 · Control antes de entregar

- [ ] Checklists de curaduría, calificación y criterio comercial completos.
- [ ] El número de calificados usa la definición del cliente (o dice "propuesta a validar"), con rango si hay aproximaciones.
- [ ] Hot leads como prioridad, no como etapa; "corto plazo" en días.
- [ ] Cotejar cifra por cifra contra la fuente (evita dos criterios de cohorte en la misma pantalla).
- [ ] Ninguna cifra suma Meta + Prometheo.
- [ ] Cada lista de Audiencias declara su tag de origen y su tamaño real.
- [ ] Cada recomendación enlaza a un hallazgo con base, y no usa datos por debajo de Señal.
- [ ] Cada pestaña tiene datos o un estado vacío diseñado que dice por qué no.
- [ ] Faltantes de integración (Meta, cierre, cortes de saldo) declarados en Integraciones.
- [ ] El switch Básico / Avanzada cambia algo en todas las vistas.
- [ ] Peso del HTML verificado; las últimas pestañas cargan.

## Referencias

- `references/cuerpo-de-conocimiento.md`: el producto, el caso EDFAN, el estado de la
  atribución, lo que se puede y no se puede medir, y el vocabulario común. Sus cifras
  de calificados de EDFAN (386 / 381) son anteriores a la definición del cliente: valen
  las del paso 3.
