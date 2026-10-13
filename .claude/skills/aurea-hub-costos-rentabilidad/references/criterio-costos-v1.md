# Criterio de costos y rentabilidad de Prometheo

Documento madre interno de AUREA Hub. Reúne el 100% de lo trabajado en esta conversación: costos fijos y variables de Prometheo, el cobro de WhatsApp de Meta desde octubre de 2026, el consumo de IA (tokens), la rentabilidad para el cliente y las decisiones que AUREA toma con cada dato. Es la fuente de verdad para avisos a clientes, decks, propuestas y tableros de Inteligencia Comercial.

Versión 1 · 13 de octubre de 2026 · uso interno.

## Cómo leer las marcas de confianza

- **[META]** verificado en documentación oficial de Meta (developers.facebook.com o business.whatsapp.com).
- **[PROMETHEO]** publicado por Prometheo (web, blog o panel de la plataforma).
- **[CASO]** medido en un cliente real de AUREA.
- **[CÁLCULO]** cuenta propia de AUREA sobre datos verificables.
- **[A CONFIRMAR]** dato con fuente parcial, de terceros, o que depende de información que todavía no tenemos.
- **[DEROGADO]** criterio anterior que quedó superado; se deja para trazabilidad.

Toda card de acción de este documento lleva un **score data-driven** (0 a 100%), calculado con la rúbrica de la skill `aurea-data-action-driven`.

---

## 1. El modelo de costos: tres componentes

Fuente: Prometheo, *Modelo de TOKENS*, *Handoff de facturación*; Meta. [PROMETHEO] [META]

Un cliente de Prometheo paga tres cosas distintas, que conviene no mezclar nunca:

| Componente | Qué es | Tipo | Quién cobra | Referencia |
|---|---|---|---|---|
| Suscripción Prometheo | Abono mensual de la plataforma. No incluye IA. | Fijo | Prometheo | USD 49 / 99 / 149 según plan (ver sección 2) |
| Saldo de IA (tokens) | Se carga en dólares dentro de Prometheo y se consume cada vez que la IA trabaja. | Variable, por uso | Prometheo | Se mide por cuenta (ver sección 4) |
| Costo Meta | Mensajes salientes por WhatsApp API oficial. | Variable, por mensaje | Meta, directo al portfolio | Desde ARS 37,68 por mensaje en Argentina (ver sección 3) |

Reglas que sostienen el modelo:

- Los modelos de IA (OpenAI, Gemini, Claude) vienen integrados en Prometheo. El cliente no contrata nada aparte: el consumo de esos modelos se paga contra el saldo de IA. [PROMETHEO]
- El saldo de IA lo maneja el cliente, con su tarjeta. Al alta se cobran USD 10 que van a saldo y se habilita recarga automática, configurable desde el perfil. [PROMETHEO]
- Si el saldo llega a cero, la agente deja de responder (restricción 8 de la plataforma). [PROMETHEO] [CASO: ver sección 5, cortes de EDFAN]
- El costo Meta lo factura Meta directo al portfolio del cliente, no Prometheo. [META]
- Frase de marca: "Prometheo cobra la inteligencia, Meta cobra el canal."

---

## 2. Costos fijos: planes de Prometheo

Fuente: prometheo.ai/#pricing, octubre 2026. [PROMETHEO]

| Plan | Precio/mes | Qué incluye | Integraciones de marketplace |
|---|---|---|---|
| **Basic** | USD 49 | CRM completo, WhatsApp/Instagram/WebChat, precalificación y seguimientos, usuarios y chats ilimitados, onboarding autogestionado | 0 |
| **Pro** | USD 99 | Todo lo de Basic + notificaciones + Facebook chat + onboarding híbrido | 1 |
| **Enterprise** | USD 149 | Todo lo de Pro + respuesta a comentarios + campañas masivas + Meta Ads y TikTok + 1 llamada de onboarding y 2 mensuales | 2 |

Ningún abono incluye saldo de IA.

**Criterio de AUREA sobre el plan.** Recomendamos **Enterprise (USD 149)** por defecto, porque trae dos integraciones de marketplace, lo que nos deja conectar Tokko más otra fuente sin recotizar, y habilita campañas masivas y Meta Ads, que son parte del valor que vendemos. Basic y Pro existen y son válidos para clientes sin integraciones; cuando los usemos, el deck debe decir "plan recomendado: Enterprise", no "desde USD 149".

> **[DEROGADO]** "AUREA desde ~USD 149/mes" presentado como piso de la plataforma. USD 149 es el plan recomendado (Enterprise), no el mínimo. El mínimo real de plataforma es USD 49. A corregir en el deck oficial y en Costos y Rentabilidad.

Facturación de Prometheo: emite el día 15, cobra el mes por adelantado, prorratea el alta. Baja con formulario; el saldo remanente no se reembolsa pero queda en la cuenta. [PROMETHEO]

---

## 3. Costo variable 1: WhatsApp y Meta

### 3.1 Qué cambió el 1° de octubre de 2026

Fuente: Meta, *Pricing for non-template messages*. [META]

- Meta **cobra los mensajes de servicio** (las respuestas de texto libre dentro de la ventana de 24 h), que no se cobraban desde noviembre de 2024. [META]
- Meta **cobra también la utilidad enviada como respuesta dentro de la ventana de 24 h**, gratis desde el 1 de julio de 2025. [META]
- La respuesta que envía **una persona o un agente de IA de terceros** (como Prometheo) es un **mensaje de servicio** y entra en este cobro. [META]
- El mensaje de servicio **cuesta lo mismo que uno de utilidad** en cada mercado y **no tiene descuento por volumen**. [META]
- Cada número de empresa tiene **1.000 mensajes de servicio gratis por mes**, que no se acumulan. [META]

Antes del cobro nuevo, las plantillas (marketing, utilidad, autenticación) **ya se cobraban** por entrega. Lo único nuevo es el cobro de la respuesta y de la utilidad dentro de la ventana. [META]

> **[DEROGADO]** "Servicio: gratis dentro de las 24 h" y "Costo Meta solo si salen campañas o recontactos". Falso desde el 1/10/2026. A corregir en Tokens, Handoff, Costos y Rentabilidad, y en el one-pager de TKVA.

### 3.2 Tarifas oficiales en pesos, Argentina

Fuente: Meta, rate card en ARS, vigente desde el 1/10/2026 (archivos CSV y PDF oficiales). [META]

| Tipo de mensaje | Categoría | Tarifa (ARS por mensaje) | Descuento por volumen |
|---|---|---|---|
| Respuesta de la agente o del equipo por API | Servicio | **37,6798** | No |
| Plantilla de utilidad | Utilidad | **37,6798** | Desde 100.001 msj/mes (−5%) |
| Plantilla de autenticación | Autenticación | **37,6798** | Desde 120.001 msj/mes (−5%) |
| Plantilla de marketing | Marketing | **89,5620** | No |

- Meta factura Argentina en pesos desde el 1 de abril de 2026. Son precios de lista: se suman los impuestos de la factura. [META]
- Los "40 pesos por mensaje" que reportan los clientes son el ARS 37,68 redondeado. [CÁLCULO]
- Ningún cliente de AUREA alcanza el primer tramo de descuento (100.000 mensajes/mes). Para todos rige el precio de lista. [CÁLCULO]
- **La tarifa depende del país del número que recibe.** Un número de Uruguay entra en "Rest of Latin America": servicio y utilidad **ARS 16,3762**, marketing **ARS 107,2425**. Importa para cuentas como Nexchange. [META]

### 3.3 Ventana gratuita de 72 h (Click to WhatsApp)

Fuente: Meta, *Pricing on the WhatsApp Business Platform*. [META]

Un contacto que escribe desde un anuncio de Click to WhatsApp o un botón de página de Facebook abre una ventana gratuita, con tres condiciones que hay que respetar:

- La ventana **corre desde tu respuesta**, no desde que el contacto escribe: si respondés dentro de las 24 h, ese mensaje es gratis y abre la ventana. [META]
- Dura **72 h**, y dentro de ellas todo lo que envíes es gratis, incluso plantillas de marketing. [META]
- Solo aplica si el contacto escribe **desde la app de Android o iOS**; escritorio y web no cuentan. [META]
- Pasadas las 72 h, el seguimiento se cobra como cualquier mensaje. [META]

> **[DEROGADO]** "72 h gratis desde un anuncio" sin condiciones. La ventana corre desde la respuesta, exige responder dentro de 24 h y que el contacto escriba desde el celular.

### 3.4 Qué consume y qué no: API, coexistencia y QR

Fuente: Meta, *API solutions for WhatsApp Business App Users* y guía de coexistencia; Prometheo, blog del 6/7/2026. [META] [PROMETHEO]

El costo de Meta solo existe sobre la **API oficial**. La conexión por QR no paga por mensaje.

| | API oficial | Coexistencia (app + API, mismo número) | QR |
|---|---|---|---|
| Costo de Meta por mensaje | Sí, con 1.000 respuestas gratis/mes | Lo de la app es gratis; lo de la API se cobra | Sin costo por mensaje |
| Plantillas, campañas, reconexión +24 h | Sí | Sí, solo desde la API | No |
| Click to WhatsApp (72 h gratis) | Sí | Sí | A evaluar |
| Mejor uso | Ventas con agente, pauta, campañas | Agente por API + equipo a mano desde la app | Atención y soporte |
| A tener en cuenta | Conexión oficial | Tope de 20 msj/seg; se desactivan las listas de difusión de la app | Estabilidad según escala y uso |

Detalle de coexistencia, verificado con Meta: [META]

- Lo que el negocio envía **desde la app** de WhatsApp Business sigue siendo gratis; lo que sale **por Cloud API** paga la tarifa de la API.
- Lo enviado desde la app **no crea, extiende ni afecta** las ventanas de conversación ni el precio de la API.
- Las plantillas solo se pueden mandar desde la API, no desde la app.
- Límites: tope fijo de 20 mensajes por segundo y listas de difusión de la app desactivadas.

**[A CONFIRMAR]** El riesgo de bloqueo del QR por mensajería masiva o automatización no autorizada lo sostienen proveedores de WhatsApp y notas de prensa, no una fuente de Meta citable. No afirmarlo como dato ante el cliente hasta cerrarlo con documentación oficial.

### 3.5 Cómo bajar el costo de Meta

Prometheo recomienda cinco prácticas; AUREA agrega dos. [PROMETHEO] [CÁLCULO]

1. Optimizar el prompt para convertir en menos mensajes: pedir lo clave en las dos primeras respuestas. [PROMETHEO]
2. No dividir respuestas en bloques (apagar "humanizar mensajes"): cada bloque es un mensaje facturable. [PROMETHEO]
3. Evaluar QR o coexistencia para líneas de puro soporte. [PROMETHEO]
4. No llevar todo a WhatsApp: que el agente responda en Instagram, Facebook y TikTok donde el lead escribe. [PROMETHEO]
5. Usar integraciones (Connect, Atlas) para que el agente no pregunte lo que ya está en un sistema. [PROMETHEO]
6. **Pauta por Click to WhatsApp, no por formulario:** concentra la calificación y el primer seguimiento en las 72 h sin costo. [AUREA]
7. **Segunda línea = segundo cupo:** una línea aparte para no-demanda suma otros 1.000 mensajes gratis. [AUREA]

---

## 4. Costo variable 2: consumo de IA (tokens)

### 4.1 De qué depende el consumo

Fuente: Prometheo, *Costos y Rentabilidad*, *Modelo de TOKENS*. [PROMETHEO]

No hay precio fijo por lead. Cinco factores mueven el consumo: volumen de conversaciones, largo del prompt, integraciones conectadas, Smart Tags y variables con IA, y seguimientos o campañas redactados por la IA.

### 4.2 Qué consume y qué no, dentro del CRM

Fuente: Prometheo, panel "Entendé tu consumo". [PROMETHEO]

- **Crear tags y variables no consume por sí solo.** Lo que consume es la **extracción automática con IA**: analizar cada conversación para decidir si asigna un tag o guarda una variable. [PROMETHEO]
- Ese análisis **consume aunque al final no asigne nada.** [PROMETHEO]
- Si un tag o una variable se gestiona **solo de forma manual**, no hay consumo de IA por esa gestión. [PROMETHEO]
- El desglose por cuenta está en Mi Perfil › Saldo disponible › "Entendé tu consumo". [PROMETHEO]

**Implicancia para el diseño del CRM.** Dejar automático lo que alimenta la calificación; pasar a manual (o acortar su prompt) lo que la IA evalúa en cada charla y casi nunca completa. Siempre con medición previa en "Entendé tu consumo", no a ciegas. [AUREA]

**Dos embudos, criterio AUREA.** Recepción y calificación está automatizado. Venta y cierre lo marca el equipo; hay un diseño nuevo para asignarlo también de forma automática. Los tags de venta y cierre **no se apagan**: el objetivo es que estén medidos, porque sin medición el cliente no sabe qué convierte. Que un tag de etapa humana se use poco no es un costo para recortar: es señal de que el embudo humano no se está registrando. [AUREA]

### 4.3 Cómo se mide: "se mide, no se adivina"

Fuente: Prometheo, *Costos y Rentabilidad*; método AUREA. [PROMETHEO] [AUREA]

Método de prueba real (3 a 7 días): cargar saldo, anotar saldo inicial, correr con todo activo, anotar volúmenes, calcular unitarios, proyectar al mes con 20% a 30% de colchón.

Fórmulas:
- Consumo IA = saldo inicial − saldo final **+ recargas del período**.
- Costo por lead = consumo IA ÷ cantidad de leads.
- Mensual = semanal × 4,33.

**Nota de método [CASO: EDFAN].** Si el cliente recarga durante el período, "saldo inicial − saldo final" deja de ser el consumo: hay que sumar las recargas, o usar directamente el detalle del panel. Cargar saldo no es consumir.

**Nota de método [CASO: EDFAN, cortes].** El saldo solo se consume cuando hay saldo cargado. Si la cuenta se quedó sin saldo varios días, el consumo del mes refleja menos días de trabajo que el calendario, mientras que la cantidad de charlas cuenta el mes entero. No leer un consumo bajo como "bajó la demanda" sin antes revisar los cortes. Ver sección 5.

### 4.4 Unitario de referencia

Fuente: test real y casos medidos. [CASO] [CÁLCULO]

| Evento | Referencia Prometheo | Medido en AUREA | Criterio |
|---|---|---|---|
| Lead atendido | USD 0,30 | USD 0,34 a 0,47 por conversación (ver sección 5) | **El USD 0,30 es piso, no promedio.** Para proyectar, usar USD 0,40. [AUREA] |

> **[DEROGADO]** "~USD 20 cada 2.000 chats" del deck oficial (= USD 0,01 por chat). No coincide con ningún caso real: lo medido es 35 a 47 veces mayor. Reemplazar por "desde USD 0,30 por conversación, medido por cuenta". [AUREA]

> **[DEROGADO]** El AllInOne de TKVA ubicaba a Prometheo en "≈US$0,20 por conversación". Con los números del propio documento da ≈0,34. Corregir antes de que el cliente lo use. [CASO: TKVA]

---

## 5. Caso real EDFAN Real Estate (jul–sep 2026)

Fuente: panel de consumo de Prometheo y tablero de IC de EDFAN. [CASO]

### 5.1 Consumo de saldo de IA

| Mes | Consumo | Conversaciones | Sin procesar por IA |
|---|---|---|---|
| Julio | USD 102,66 | arranque | — |
| Agosto | USD 212,89 | 457 | 41 |
| Septiembre | USD 163,14 | 461 | 90 |

Reparto del gasto de septiembre (panel): conversación USD 101,15 · extracción de datos USD 26,10 (16%) · Smart Tags USD 9,79 (6%) · soporte USD 27,73 (17%, subió del 11%). Extracción + Smart Tags = 22% del gasto, que se cobra por conversación aunque el lead no compre. [CASO]

### 5.2 Los cuatro cortes de septiembre (lectura corregida)

La IA se cortó por saldo agotado en cuatro momentos: 24–27/08, 02–06/09, 17–19/09 y desde el 29/09. En septiembre estuvo sin saldo **cerca de 10 días**. Consecuencias: 177 conversaciones sin resumen, tags ni variables, y 83 contactos sin respuesta. [CASO]

Por eso:

- **El consumo de septiembre refleja unos 20 días activos**, no 30. Consumo por día con IA activa ≈ **USD 8,16**, no USD 5,44. [CÁLCULO]
- **El costo por charla procesada ≈ USD 0,48** (promedio de agosto USD 0,51 y septiembre USD 0,44, sobre charlas efectivamente procesadas). El USD 0,35 del panel divide por todas las charlas, también las que la IA no procesó, y subestima. [CÁLCULO]
- **No es cierto que "las charlas se acortaron" ni que "bajó el costo por charla".** Esas lecturas eran artefactos de los cortes. [CÁLCULO]

> **[DEROGADO]** "Septiembre costó 24% menos por charla" y "las charlas se acortaron (6,1 → 3,8 mensajes)". Ambas nacían de dividir por charlas sin procesar.

### 5.3 Estimación del costo de Meta de EDFAN desde el 1/10

Sobre unos 3.000 mensajes enviados por mes (9.736 del 04/07 al 08/10), a ARS 37,68 pasados los 1.000 gratis. [CÁLCULO]

| Escenario | Mensajes cobrables | Costo Meta aprox. |
|---|---|---|
| Pauta actual (75% desde anuncios) | ~750, bajo el cupo | ≈ ARS 0 a 3.000 |
| Pauta baja al 30% | ~1.100 | ≈ ARS 41.400 |
| Sin pauta | ~2.000 | ≈ ARS 75.360 |

Es un piso: lo que sale pasadas las 72 h, o a quien escribió desde la computadora, se cobra. El dato real sale de la factura de Meta de octubre. [CÁLCULO]

### 5.4 Objeción del cliente y respuesta

El cliente dijo que el reporte no refleja el consumo porque carga saldo cada semana. Respuesta: el reporte mide consumo por conversación desde el panel, no recargas. El contrato de EDFAN (pago único) no regula el consumo; el monitoreo mensual es lo que cubre Mejora Continua. [CASO]

### 5.5 Segundo caso: TKVA

Julio USD 25,08 (configuración), agosto USD 137,99 (primer mes completo, 406 charlas), septiembre a completar. Costo por conversación de agosto ≈ USD 0,34, con el ruido administrativo todavía adentro. La línea administrativa nueva es palanca estructural. [CASO]

---

## 6. Decisiones con cada dato (action-driven)

Las acciones que AUREA propone al cliente salen de un dato curado y llevan verbo, dueño, efecto medible, guardiana y score. Catálogo base, reutilizable entre clientes; los números son del caso EDFAN.

| Verbo · dueño | Acción | Efecto esperado | Score |
|---|---|---|---|
| Corregir · AUREA | Carga semanal de saldo con monto medido (USD 75/sem) para cero cortes | Cero cortes; no se pierden leads que ya costaron pauta | 75% |
| Activar · Ventas | Reconectar a 134 calificados sin seguimiento con plantilla | ARS 5.049 si es utilidad, ARS 12.001 si es marketing | 76% |
| Corregir · AUREA | Primera respuesta con la entrega + una pregunta; apagar humanizar | −1.118 envíos en el período (de 4,8 a 2 por lead) | 85% |
| Proteger · Marketing | Sostener Click to WhatsApp como puerta de entrada | Mantiene el costo de Meta cerca de cero | 72% |
| Corregir · AUREA | Diagnóstico de tags y variables; pasar a manual lo que no se completa | Baja el 22% del gasto que hoy va a extracción | 75% |
| Separar · Dirección | Línea aparte para inmobiliarias y proveedores | ≈ USD 24/mes menos de IA + cupo propio de 1.000 msj | 66% |
| Decidir · Dirección | Días sin pauta: apagar todo (A) vs apagar solo la respuesta (B) | B ahorra ~57% y conserva la lectura del negocio | 69% |

Criterio transversal: la recarga automática no se recomienda como primer paso. La mayoría de los clientes mide primero cuánto gastan por mes y después decide; la recarga automática viene activada de fábrica y hay que avisarlo en el onboarding. [AUREA] [PROMETHEO]

---

## 7. Rentabilidad para el cliente

Fuente: Prometheo, *Costos y Rentabilidad*, deck oficial; recálculo AUREA. [PROMETHEO] [CÁLCULO] Rangos, no promesas.

Comparación base: a mano ~USD 1.200/mes (un sueldo parcial que cubre solo el horario) contra Prometheo con AUREA.

Escenarios recalculados con unitario USD 0,40 (no USD 0,30), 20% de margen, suscripción Enterprise USD 149, Meta aparte:

| Concepto mensual | Bajo (216 leads) | Medio (433) | Alto (866) |
|---|---|---|---|
| IA con 20% de margen | USD 124 | USD 249 | USD 499 |
| Suscripción Prometheo | USD 149 | USD 149 | USD 149 |
| **Total con AUREA** | **USD 273** | **USD 398** | **USD 648** |
| Costo a mano | USD 1.200 | USD 1.200 | USD 2.400 |
| **Ahorro** | **≈ 77%** | **≈ 67%** | **≈ 73%** |

El ahorro se sostiene arriba del 60% en los tres escenarios incluso con el unitario más realista, así que el argumento comercial no se cae; solo deja de estar subestimado el costo. [CÁLCULO]

Argumentos de soporte: el agente crece en costo más despacio que el equipo; los números son piso (no cuentan leads de noche ni seguimientos que nadie hace); Meta va aparte como gasto de marketing. "El ahorro es real si está bien monitoreado desde el principio y bien diseñado. Por eso existe Mejora Continua."

---

## 8. Dónde se monetiza el criterio

Fuente: deck de Mejora Continua, área IC. [PROMETHEO] [AUREA]

- **Mejora Continua Start (USD 200/mes):** estabilidad. El agente afinado y el consumo controlado. El cliente tiende a gastar menos.
- **Mejora Continua Pro (USD 300/mes):** escalabilidad. Funciones nuevas (agendado, campañas), tablero a medida, **un informe mensual de Inteligencia Comercial del CRM** (lo que el cliente contrató, no de marketing). El cliente sabe que va a gastar más porque contrata más funciones.
- **Regla:** cada función de escalabilidad que activemos se comunica con su costo estimado en tokens y en Meta antes de activarla. [AUREA]
- **Inteligencia Comercial (USD 200/mes + USD 50 por canal extra):** del dato a la decisión. El tablero que mide consumo de IA y de Meta, muestra qué anuncio trae compradores y convierte cada número en una acción con dueño.

---

## 9. Huecos abiertos (pendientes de cerrar)

1. **[A CONFIRMAR]** Mensajes salientes reales de cada cliente desde el 1/10. Los trae Valen del panel de Prometheo. Reemplazan el "A medir" de los avisos.
2. **[A CONFIRMAR]** Si EDFAN está por API pura o en coexistencia. Con coexistencia, lo que el equipo responde desde la app es gratis.
3. **[A CONFIRMAR]** Variables de EDFAN: ¿todas manuales? Si lo son, el gasto de extracción (USD 26,10) viene de Smart Tags automáticos o de la extracción offline, no de variables. Resolver con el diagnóstico de Mi Prometheo.
4. **[A CONFIRMAR]** Costo por charla procesada exacto: falta el detalle diario del panel de septiembre.
5. **[A CONFIRMAR]** Riesgo de bloqueo del QR, con fuente de Meta.
6. Actualizar los documentos client-facing con todo lo anterior: one-pager TKVA, deck oficial (unitario y "desde USD 149"), Tokens, Handoff, Costos y Rentabilidad.
7. **[A CONFIRMAR]** Tarifa exacta en pesos para Uruguay con impuestos, contra una factura real (Nexchange).

---

## 10. Fuentes

**Meta.** Pricing on the WhatsApp Business Platform; Pricing for non-template messages; API solutions for WhatsApp Business App Users (PDF) y guía de onboarding de usuarios de la app (coexistencia); rate card en ARS vigente 1/10/2026 (CSV y PDF oficiales). [META]

**Prometheo.** prometheo.ai/#pricing (planes); blog "WhatsApp empieza a cobrar los mensajes" (6/7/2026); panel "Entendé tu consumo"; documentos Modelo de TOKENS, Handoff de facturación, Costos y Rentabilidad, deck oficial, deck de Mejora Continua. [PROMETHEO]

**Casos AUREA.** EDFAN Real Estate (panel jul–sep 2026, tablero de IC); TKVA (jul–ago 2026). [CASO]

**Skills AUREA.** aurea-data-action-driven (score, verbos, anatomía de card); aurea-metodologia. [AUREA]
