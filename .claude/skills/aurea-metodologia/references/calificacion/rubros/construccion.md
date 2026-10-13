# Rubro · Construcción (venta de insumos y materiales para obra)

Estado: **propuesta a validar**. Caso de referencia: EDFAN Productos (agente Paula), en la
metodología (`03-insumos-construccion.md`): tres tipos de usuario y "m² antes que zona".

## 1. Tipo de contacto (antes de calificar)
| Valor | Qué se hace |
|---|---|
| Cliente final (particular con obra) | Se califica; lenguaje simple |
| Profesional: arquitecto o diseñador | Se califica; acepta especificación técnica |
| Constructor, aplicador o contratista | Se califica; potencial de recompra |
| Corralón o revendedor | Canal B2B (condiciones de reventa) |
| Proveedor | Se deriva sin calificar; el tag apaga el asistente |

## 2. Calificado · propuesta
| Condición | Tipo | Variable sugerida |
|---|---|---|
| Producto o categoría que la empresa vende | Obligatorio | `categoria_producto` |
| Superficie (m²) o cantidad | Obligatorio | `m2` / `cantidad` |
| Tipo de usuario identificado | Suma | `tipo_usuario` |
| Zona de entrega cubierta | Suma | `zona_entrega` |
| Etapa o fecha de la obra | Suma | `etapa_obra` / `fecha_necesidad` |
| Forma de pago o cuenta corriente | Suma (B2B) | `forma_pago` |
Regla sugerida: obligatorios + al menos 2 sumas.

## 3. Hot lead · señales sugeridas
Manda un cómputo o una lista con cantidades · pide cotización con fecha de entrega · la obra ya
arrancó o tiene fecha · profesional que vuelve a comprar · pregunta stock para retirar.

## 4. Criterio de oficio con fuente
- El contratista compra volumen y repite; el particular suele comprar una vez (ver fuentes).
  El potencial de recompra pesa en la prioridad.
- El precio es la objeción más sensible en contratistas (dato viejo, usar con cuidado).

## 5. Malas prácticas típicas del rubro
Preguntar la zona antes que los m² · cotizar cuando el lead pidió asesoramiento (o al revés) ·
prometer ejecución que la empresa no presta · hablarle con jerga técnica a un particular.

## 6. Preguntas para el discovery
¿Qué vuelve a un pedido "calificado" (m² mínimos, zona, tipo de cliente)? · ¿Qué es un pedido
urgente? · ¿Venden a corralones? · ¿Tienen cuenta corriente para profesionales?
