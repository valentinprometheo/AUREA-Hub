# Ahorro de tokens (consumo de IA y costo de Meta)

> **Fuente única de tarifas y costos: `aurea-hub-costos-rentabilidad`.** Acá quedan las palancas
> ligadas a la calificación. Si una cifra de este archivo difiere de esa skill, manda esa.

## Cómo se cobra (AUREA Hub · guía de saldo)
Tres componentes: suscripción de Prometheo (fija), **saldo de IA** (variable, se carga en el
perfil) y **costo de Meta** (mensajes de WhatsApp). Consume IA: cada respuesta del agente, los
seguimientos, los Smart Tags y variables (por conversación) y las integraciones (por consulta).
**Si el saldo llega a cero, el agente deja de responder.** La recarga automática viene activada
de fábrica (Perfil › Pagos › Saldo de tu cuenta, con piso y tope mensual configurables) y se
avisa en el onboarding. No se recomienda
como primer paso: el cliente mide primero cuánto gasta por mes y después decide.

## Meta desde el 1/10/2026 (Argentina, rate card oficial en pesos, por mensaje)
Servicio (respuesta de la agente o del equipo por API) ARS 37,68 · Utilidad ARS 37,68 ·
Marketing ARS 89,56. Precios de lista, sin impuestos. **1.000 mensajes de servicio gratis por
mes por número**, sin descuento por volumen. Ventana de Click to WhatsApp: 72 h gratis, desde
la respuesta, si se responde dentro de las 24 h y el contacto escribe desde el celular. Lo que
el equipo responde desde la app (coexistencia) no se cobra. Detalle y derogados en
`aurea-hub-costos-rentabilidad`.

> Derogado (13/10/2026): tarifas de Meta en USD (Marketing 0,0618, Utilidad 0,026) y "Click
> to WhatsApp gratis" sin condiciones.

## Cómo medir (método)
Saldo inicial, 3 a 7 días con todo activo, volúmenes registrados, costo unitario por tipo de
evento, proyección semanal × 4,33 con 20% de margen. Consumo = saldo inicial − saldo final
**+ recargas del período** (cargar saldo no es consumir). Con cortes de saldo, el costo por
charla se calcula sobre charlas procesadas. Comparar por costo por conversación,
mensajes y seguimientos, no solo dólares por día (consejo 20 de Prometheo).

## Palancas (ordenadas por impacto)
1. **Cero cortes de saldo.** Carga semanal con un monto medido (EDFAN: USD 75 por semana); la
   recarga automática, recién cuando el cliente ya sabe cuánto gasta. (EDFAN: 4 cortes, 177
   conversaciones sin registrar, 83 contactos sin respuesta.)
2. **Primera respuesta corta, el material después.** (EDFAN: 406 leads que escribieron una sola
   vez recibieron 1.930 mensajes del agente, 20% del total.) Máximo 60 palabras, una pregunta.
3. **Separar la no-demanda.** En real estate es regla: línea aparte para inmobiliarias,
   proveedores y desarrolladores, y tags que apagan el asistente.
4. **Solo variables que se usan.** Cada variable con prompt se evalúa en cada conversación
   (EDFAN: extracción = 16% del gasto). Las que casi no se completan pasan a manual; prompts cortos.
5. **Smart Tags sin prompt para etapas humanas** y sin tags huérfanos (consejo 13).
6. **Una respuesta en un mensaje** (apagar "humanizar mensajes"): cada bloque es un mensaje que
   Meta cobra.
6 bis. **Pauta por Click to WhatsApp, no por formulario:** la calificación y el primer
   seguimiento entran en las 72 h sin costo de Meta. Una línea aparte para no-demanda suma otro
   cupo de 1.000 mensajes gratis.
7. **Extracción de datos offline**: apagarla si no se usa (consejo 14).
8. **Un cambio por vez, medido.**

## Consejos de Prometheo Soporte (27/07/2026), resumen
Prompt: reducir sin perder reglas, cada regla una vez, estructura compacta, respuestas breves
(60 palabras), flujo de decisiones, pedir solo lo necesario, un ejemplo por tipo, sin
instrucciones imposibles, no estirar la charla, sin contradicciones, sin manuales internos.
Plataforma: tope de tokens de salida si existe, no cargar catálogos si hay integración,
separar permanente de variable, los archivos se envían (no se leen), Smart Tags útiles,
extracción offline, solo variables útiles, seguimientos segmentados, medir controlado.

## Referencia de costo (EDFAN, panel de Prometheo)
Julio USD 102,66 · agosto USD 212,89 (457 conversaciones) · septiembre USD 163,14 (461
conversaciones, con cerca de 10 días sin saldo). **Costo por charla procesada ≈ USD 0,48.**
Referencia de Prometheo: USD 0,30 es piso, no promedio; **para proyectar se usa USD 0,40**.
Reparto de septiembre: conversación 62%, extracción 16%, Smart Tags 6%, soporte 17%.

> Derogado (13/10/2026): "USD 0,35 por conversación" de septiembre (dividía por charlas que la
> IA no procesó) y "septiembre costó menos por charla".

## Cada cambio de ahorro es una card (`aurea-data-action-driven`)
Todo cambio de prompt, variables, tags o seguimientos para ahorrar tokens o mensajes se propone
como card con verbo, dueño, efecto esperado y **score**, y lleva **guardiana**: que no baje el %
de calificación con la definición del cliente ni aumenten los hot leads sin seguimiento.
