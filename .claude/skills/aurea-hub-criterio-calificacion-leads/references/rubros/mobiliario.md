# Rubro · Mobiliario (estándar, configurable, a medida, proyectos)

Estado: **propuesta a validar**. Caso de referencia: BETROX, en la metodología
(`02-mobiliario.md`): variables `tipo_usuario` y `tipo_compra`, showroom como conversión.

## 1. Tipo de contacto (antes de calificar)
| Valor | Qué se hace |
|---|---|
| Consumidor final | Se califica |
| Profesional: arquitecto, decorador, paisajista | Se califica; programa para profesionales |
| Constructora, municipio, proyecto integral | Canal B2B / proyecto |
| Cliente recurrente | Postventa o recompra |
| Proveedor | Se deriva sin calificar; el tag apaga el asistente |

## 2. Calificado · propuesta
| Condición | Tipo | Variable sugerida |
|---|---|---|
| Línea o producto que la empresa fabrica o vende | Obligatorio | `linea_producto` |
| Tipo de compra: estándar, configurable, a medida o proyecto | Obligatorio | `tipo_compra` |
| Medidas, plano o fotos del ambiente | Suma | `medidas` |
| Plazo (mudanza, obra, fecha de entrega) | Suma | `plazo` |
| Presupuesto o forma de pago | Suma | `presupuesto` / `forma_pago` |
| Zona de entrega cubierta | Suma | `zona` |
Regla sugerida: obligatorios + al menos 2 sumas.

## 3. Hot lead · señales sugeridas
Pide visita al showroom · manda medidas, plano o fotos · pide precio de un modelo concreto ·
fecha de mudanza o de fin de obra · profesional con proyecto en curso.

## 4. Criterio de oficio con fuente
- Programas para profesionales: validación de la profesión, 10% a 20% de descuento y a veces
  pedido mínimo (ver fuentes).
- Antes de la cita de showroom conviene tener tipo de proyecto, m² y estilo.

## 5. Malas prácticas típicas del rubro
Calificar antes de dar el precio (el consumidor final pregunta precio primero: regla 16) ·
tratar al profesional como consumidor final · un tag por tipo de cotización (usar variable).

## 6. Preguntas para el discovery
¿Qué compra vale la pena seguir (ticket, a medida, proyecto)? · ¿Cuándo un lead está listo
para el showroom? · ¿Tienen programa para profesionales?
