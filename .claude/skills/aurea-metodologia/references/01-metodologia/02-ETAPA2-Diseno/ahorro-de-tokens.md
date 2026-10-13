---
consultar-cuando: diseño de CRM, prompt o seguimientos; auditoría de consumo; tablero de IC
disparadores: "tokens", "saldo de IA", "consumo", "ahorro", "costo por conversación", "Meta cobra"
fuente-única-de: las decisiones de diseño que bajan el consumo de IA
combina-con: restricciones-plataforma-prometheo, embudos-y-tags, framework-seguimientos
---

# Ahorro de tokens en el diseño del CRM

> El detalle (método de medición, consejos de Prometheo Soporte, números de EDFAN) vive en
> `references/calificacion/ahorro-de-tokens-detalle.md`. **Tarifas, costo por conversación y
> rentabilidad: fuente única en la skill `aurea-hub-costos-rentabilidad`.** Acá van
> solo las decisiones de diseño que se toman en Etapa 2 y se controlan en Etapa 4.

## Decisiones de diseño
1. **Separar la no-demanda antes de calificar.** Tipo de contacto excluyente; proveedores y
   desarrolladores con tag que apaga el asistente. En real estate: línea de WhatsApp aparte
   para inmobiliarias, proveedores y desarrolladores ([FIJA] en `06-rubros/01-real-estate.md`).
2. **Variables: solo las que se usan, con prompt corto.** Cada variable con prompt se evalúa en
   cada conversación (EDFAN: extracción = 16% del gasto). Las raras pasan a manual.
3. **Smart Tags: sin prompt para etapas humanas, sin tags huérfanos** (regla dura 11 de
   `embudos-y-tags.md`).
4. **Prompt: primera respuesta corta, el material cuando el lead contesta.** Máximo 60
   palabras, una pregunta por mensaje (consejos 4 y 17 de Prometheo). EDFAN: los leads que
   escribieron una sola vez recibieron el 20% de los mensajes del agente.
5. **Seguimientos solo con oportunidad pendiente** (Hot Lead, Calificado), un tag por
   seguimiento, excluyendo cerrados. Fuera de la ventana usan plantilla y Meta los cobra.
6. **Una respuesta en un solo mensaje** (apagar "humanizar mensajes"): desde el 1/10/2026 Meta
   cobra cada respuesta por API como mensaje de servicio (ARS 37,68, con 1.000 gratis por mes
   por número).
7. **Cero cortes de saldo en el go-live** (restricción 8): la recarga automática viene activada
   de fábrica y se avisa en el onboarding; si el cliente prefiere medir primero, carga semanal
   con un monto medido.
8. **Pauta por Click to WhatsApp, no por formulario:** la calificación y el primer seguimiento
   entran en la ventana de 72 h sin costo de Meta (si se responde dentro de las 24 h y el
   contacto escribe desde el celular).
9. **Cada cambio de ahorro, como card con score y guardiana** (`aurea-data-action-driven`): que
   el ahorro no baje el % de calificación con la definición del cliente.

> Actualización v1.24: antes la decisión 7 era "Recarga automática con piso" como regla del
> go-live; ahora es "cero cortes", con la recarga automática como opción y no como primer
> paso. Por qué: criterio de costos v1 (13/10/2026), el cliente mide primero cuánto gasta.

## Control en Etapa 4
Comparar el costo por conversación del panel de consumo antes y después de cada cambio, un
cambio por vez. El tablero de IC lo muestra en la pestaña de consumo y costos (IA y Meta).
Consumo = saldo inicial − saldo final + recargas; con cortes de saldo, costo por charla procesada.
