# Aplicar el criterio a contactos existentes con Mi Prometheo

Mi Prometheo es el asistente interno de la cuenta (todos los planes). Hace cambios masivos de
tags: pregunta el tag de origen y el de destino, si se mantienen los demás tags y si el cambio
aplica a todo o a un rango de fechas de ingreso; también filtra por variables. **Siempre muestra
un «¿Confirmás?» antes de aplicar**, y cada conversación se revierte desde el panel derecho.
También crea y configura tags, variables y seguimientos. Fuente: https://prometheo.gitbook.io/prometheo/recursos-compartidos/mi-prometheo

## Por qué cada pedido se audita
No es irreversible, pero consume saldo de IA (entra en el bloque "Soporte" del panel de
consumo; en EDFAN pasó del 11% al 17% del gasto) y un pedido mal armado se paga dos veces: al
hacerlo y al revertirlo.

## Procedimiento
1. **Traducir el criterio a un filtro que Mi Prometheo pueda aplicar.** Filtra por tags, fecha
   de ingreso y variables con dato o con un valor. No filtra por cantidad de mensajes ni por
   "k de n" de forma confiable: elegí una combinación de variables (AND) que **implique** la regla.
   Ej. EDFAN: proyecto + tipología (obligatorios) + finalidad + estado de obra (2 sumas).
2. **Auditar contra el export (v1 → v2).** Contar cuántos contactos toma el filtro y cuántos
   cumplen la regla completa (precisión). Buscar lo que el filtro toma por error: contactos que
   no conversaron, variables llenadas con la oferta del agente, no-demanda, objeciones que
   contradicen una condición. Documentar qué cambió entre versiones.
3. **Prueba chica primero.** El lote más chico con valor real (en EDFAN, los 34 que pidieron
   visita o reunión). Si el conteo y los disparadores coinciden, recién ahí el lote grande.
4. **Conteo esperado dentro del prompt**, con un rango, y la orden de frenar si se aleja.
5. **Preguntar qué dispara el tag de destino** (seguimientos, notificaciones, acciones) antes
   de aplicar: un tag con seguimiento puede mandar mensajes con costo de plantilla.
6. **Un pedido por conversación**, para revertir cada uno por separado.
7. **Fecha de corte**: limitar por fecha de ingreso al período auditado (los contactos nuevos
   todavía no tienen variables).

## Plantilla de prompt
```
Quiero hacer un cambio masivo de tags[, primero como prueba chica].

Asistente: "[nombre del asistente]".
Contactos: los que hoy tienen el tag "[origen]" y [variables con dato / valor], con fecha de
ingreso entre el [dd/mm/aaaa] y el [dd/mm/aaaa].
Excluí a los que tengan alguno de estos tags: [no-demanda].
Cambio: pasar el tag "[origen]" a "[destino]" | agregar el tag "[destino]".
Mantener los demás tags de cada contacto: sí.

Antes de aplicar nada:
1) Decime cuántos contactos cumplen el filtro. Espero alrededor de [N]. Si te da menos de [a]
   o más de [b], frená y avisame antes de seguir.
2) Mostrame 5 contactos de ejemplo con su nombre y sus tags actuales.
3) Decime si el tag de destino dispara algún seguimiento, notificación o acción del asistente,
   y a quién le llega.
No apliques el cambio hasta que yo te confirme con "Sí, confirmar".
```

## Cómo leer el «¿Confirmás?»
Conteo dentro del rango · "mantener los demás tags: sí" · ningún ejemplo con tags de
no-demanda · los disparadores del destino son los esperados. Si algo no coincide: cancelar.

## Hot lead con Mi Prometheo
Crear el tag "Hot Lead" (fuera de los embudos), con mini-prompt de asignación de 15 a 25
palabras que liste las señales, y notificación según una variable (finalidad, zona o proyecto).
Aplicarlo primero a la señal más clara (reunión pedida), después al resto (plazo, contado).
