# Rubro · Inmobiliaria tradicional (compra, venta, alquiler, tasación)

Estado: **propuesta a validar** en el discovery del primer cliente. Variables tomadas del molde
de `aurea-metodologia` (`04-inmobiliaria-tradicional.md`): `tipo_contacto`, `operacion`,
`tipo_propiedad`. Caso parcial de referencia: Paganini.

## 1. Tipo de contacto (antes de calificar)
| Valor | Qué se hace |
|---|---|
| Comprador / locatario | Se califica (embudo según operación) |
| Propietario que vende o alquila | **Otro embudo: captación.** No se califica como comprador |
| Broker externo / colega | Canal B2B o derivación |
| Proveedor | Se deriva sin calificar; el tag apaga el asistente |
La operación (venta, alquiler residencial, temporario, comercial) se identifica desde el primer
mensaje: cada una tiene su propio criterio.

## 2. Calificado · propuesta
| Condición | Tipo | Variable sugerida |
|---|---|---|
| Operación y tipo de propiedad que la inmobiliaria trabaja | Obligatorio | `operacion`, `tipo_propiedad` |
| Zona con cartera disponible | Obligatorio | `zona` |
| Capacidad de pago declarada (ahorro, crédito, venta de otra propiedad) | Suma | `forma_pago` |
| Presupuesto compatible con la cartera | Suma | `presupuesto` |
| Plazo de mudanza o de compra | Suma | `horizonte` |
| Requisitos del alquiler cumplidos (garantía, ingresos) | Suma (solo alquiler) | `garantia` |
Regla sugerida: obligatorios + al menos 2 sumas. Validar con el cliente.

## 3. Hot lead · señales sugeridas
Pide visita a una propiedad concreta · pide la ficha o el precio de una propiedad publicada ·
crédito pre-aprobado o dinero disponible · plazo de mudanza en días o semanas · en alquiler:
garantía lista y fecha de ingreso.

## 4. Criterio de oficio con fuente
- Crédito hipotecario (AR): cuota hasta 25% del ingreso, financia hasta 80%, 1 año de
  antigüedad laboral (ver fuentes). "¿Compra con crédito, ahorro o venta de otra propiedad?" es
  la pregunta de capacidad; si depende de vender, también es una oportunidad de captación.
- La mayoría de los compradores habla con un solo agente: la velocidad de respuesta decide.

## 5. Malas prácticas típicas del rubro
Mezclar al propietario que quiere vender con el comprador · preguntar ingresos o garantía al
principio · cuestionario largo (la metodología pide 5 a 7 preguntas como máximo, repartidas).

## 6. Preguntas para el discovery
¿Qué operaciones y tipos de propiedad trabajan? · ¿Qué es un comprador calificado para ustedes?
· ¿Y uno caliente? · ¿Cómo atienden a propietarios que quieren vender? · ¿Qué piden para alquilar?
