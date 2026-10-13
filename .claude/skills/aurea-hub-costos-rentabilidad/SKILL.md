---
name: aurea-hub-costos-rentabilidad
description: Criterio de costos y rentabilidad de Prometheo para AUREA Hub. Fuente única de los tres costos del cliente (suscripción de Prometheo, saldo de IA en tokens y mensajes de WhatsApp que cobra Meta desde el 1/10/2026), tarifas de Meta en pesos, ventana de 72 h de Click to WhatsApp, API vs coexistencia vs QR, medición del consumo de IA, costo por conversación, casos EDFAN y TKVA y rentabilidad. Usala SIEMPRE que haya que cotizar, explicar o proyectar costos de Prometheo, armar un aviso de costos a un cliente, calcular rentabilidad o ahorro, armar la pestaña de consumo y costos de un tablero de IC, revisar un deck o propuesta con precios de plataforma, o decidir una acción para bajar el costo de IA o de Meta. Activar ante "costos", "cuánto cuesta", "tokens", "saldo de IA", "Meta cobra", "tarifa de WhatsApp", "coexistencia", "rentabilidad", "ahorro", "plan Enterprise", "costo por conversación".
---

# Costos y rentabilidad de Prometheo (AUREA Hub)

Esta skill es la **fuente única** de cualquier número de costo de Prometheo, Meta o IA. Las
demás skills (calificación, metodología, tableros de IC, conocimiento de IC, documentos)
apuntan acá y no copian tarifas. Si una skill dice otra cosa, **manda esta** y la otra se corrige.

El documento madre completo, con todas sus fuentes, está en
`references/criterio-costos-v1.md` (versión 1, 13/10/2026). Leelo entero antes de cotizar,
proyectar o escribir un aviso a un cliente.

## Las marcas de confianza (se respetan en todo lo que se escriba)

[META] verificado en documentación oficial · [PROMETHEO] publicado por Prometheo · [CASO]
medido en un cliente · [CÁLCULO] cuenta de AUREA · [A CONFIRMAR] fuente parcial · [DEROGADO]
superado. Ante el cliente nunca se presenta un [A CONFIRMAR] como dato.

## Lo esencial en una pantalla

**Tres costos que no se mezclan nunca.** *Prometheo cobra la inteligencia, Meta cobra el canal.*

| Costo | Tipo | Quién cobra | Valor de referencia |
|---|---|---|---|
| Suscripción | Fijo | Prometheo | Basic USD 49 · Pro USD 99 · **Enterprise USD 149 (recomendado)**. Ninguno incluye IA |
| Saldo de IA | Variable por uso | Prometheo | **USD 0,40 por conversación para proyectar** (USD 0,30 es piso); medido USD 0,34 a 0,48 |
| Mensajes de WhatsApp | Variable por mensaje | Meta, directo al cliente | Servicio y utilidad **ARS 37,68** · marketing **ARS 89,56** (Argentina, lista, sin impuestos) |

**Meta desde el 1/10/2026.** Cobra la respuesta de la agente o del equipo por API (servicio),
sin descuento por volumen, con **1.000 mensajes de servicio gratis por mes por número**. La
**ventana de 72 h de Click to WhatsApp** es gratis solo si se responde dentro de las 24 h y el
contacto escribe desde el celular; corre desde la respuesta. La tarifa depende del país del
número que recibe (Uruguay: ARS 16,38 y 107,24). QR no paga por mensaje; en coexistencia lo
que sale desde la app es gratis y lo de la API se cobra.

**Consumo de IA.** Crear tags y variables no consume: consume la extracción automática en cada
conversación, aunque no asigne nada. Si el saldo llega a cero, la agente deja de responder.
Fórmula: consumo = saldo inicial − saldo final **+ recargas del período**. Con cortes de saldo,
el costo por charla se calcula **sobre charlas procesadas**, no sobre todas.

**Rentabilidad (rangos, no promesas).** Con USD 0,40, 20% de margen y Enterprise: total USD 273
a 648 por mes contra USD 1.200 a 2.400 a mano, **ahorro de 67% a 77%**. Meta va aparte como
gasto de marketing.

## Derogados: no usar nunca más

| Derogado | Qué lo reemplaza |
|---|---|
| "Desde USD 149/mes" como piso de plataforma | Plan recomendado Enterprise USD 149; el mínimo es USD 49 |
| "Servicio gratis dentro de las 24 h" / "Meta cobra solo campañas o recontactos" | Meta cobra el servicio desde el 1/10/2026, con 1.000 gratis por mes |
| "72 h gratis desde un anuncio" sin condiciones | Corre desde la respuesta, responder en 24 h, contacto desde el celular |
| "~USD 20 cada 2.000 chats" (USD 0,01 por chat) | Desde USD 0,30 por conversación, medido por cuenta; proyectar con USD 0,40 |
| "≈ USD 0,20 por conversación" (TKVA) | ≈ USD 0,34 con los números del propio documento |
| Tarifas de Meta en USD (0,0618 / 0,026) | Rate card oficial en pesos (ARS 89,56 / 37,68) |
| "Septiembre costó 24% menos por charla" / "las charlas se acortaron" (EDFAN) | Artefactos de los cortes de saldo; costo por charla procesada ≈ USD 0,48 |
| "~80% de ahorro" con unitario USD 0,30 | 67% a 77% con unitario USD 0,40 |
| Recarga automática como primer paso | Medir primero y cargar un monto semanal medido; la recarga automática viene activada de fábrica y se avisa en el onboarding |

## Cómo trabajar según la tarea

- **Cotizar o proyectar un cliente.** Sección 7 del documento madre: unitario USD 0,40, 20% de
  margen, plan recomendado, Meta aparte y en pesos. Siempre como rango.
- **Aviso de costos de Meta a un cliente.** Secciones 3 y 5.3: mensajes salientes reales del
  panel (si no los hay, es [A CONFIRMAR]), cupo de 1.000, peso de la pauta por Click to WhatsApp.
- **Tablero de IC, pestaña de consumo y costos.** Ver abajo.
- **Acción para bajar costos.** Catálogo de la sección 6, en formato card de
  `aurea-data-action-driven` (verbo, dueño, efecto, guardiana, score). Guardiana obligatoria:
  que el ahorro no baje el % de calificación con la definición del cliente.
- **Deck o propuesta.** Revisar contra la tabla de derogados antes de entregar.

## En el tablero de IC (pestaña "Consumo y costos")

| Bloque | Qué muestra | Regla |
|---|---|---|
| Consumo de IA | USD del período, costo por conversación procesada, reparto (conversación, extracción, Smart Tags, soporte) | Fuente: panel "Entendé tu consumo". Cargar saldo no es consumir |
| Cortes de saldo | Días sin saldo, conversaciones sin procesar, contactos sin respuesta | Es también un faltante de datos: se declara en Integraciones |
| Costo de Meta | Mensajes salientes por categoría, cupo de 1.000 usado, costo en ARS | Fuente: factura de Meta o panel. Sin dato real, escenario rotulado [CÁLCULO] |
| Puerta de entrada | % de conversaciones desde Click to WhatsApp | Explica por qué el costo de Meta está cerca de cero o no |
| Acciones | Cards del catálogo de la sección 6 | Score con techo según el nivel del dato central |

## Pendientes abiertos

Los siete huecos de la sección 9 del documento madre (mensajes reales desde el 1/10, API o
coexistencia en EDFAN, variables manuales, costo exacto por charla, riesgo del QR, documentos
client-facing a corregir, tarifa de Uruguay con impuestos). Se cierran actualizando el
documento madre y subiendo la versión en `references/CHANGELOG.md`.

## Mejora continua

1. Un dato nuevo entra al documento madre con su marca de confianza y fecha.
2. Si reemplaza algo, lo viejo se marca [DEROGADO] y se suma a la tabla de derogados de arriba.
3. Se versiona en `references/CHANGELOG.md`.
4. Barrido: buscar el dato viejo en las skills que apuntan acá (calificación, metodología,
   conocimiento de IC, tableros de IC) y corregirlo.

## Skills relacionadas

`aurea-data-action-driven` (formato de card y score) · `aurea-hub-criterio-calificacion-leads`
(palancas de ahorro ligadas a la calificación) · `aurea-metodologia` (decisiones de diseño
que bajan el consumo) · `aurea-ic-dashboard` (pestaña de consumo y costos) ·
`aurea-ic-conocimiento` (cómo se cuentan precio y rentabilidad).
