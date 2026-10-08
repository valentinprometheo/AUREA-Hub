---
consultar-cuando: diseño de CRM, prompt o seguimientos; auditoría de consumo; tablero de IC
disparadores: "tokens", "saldo de IA", "consumo", "ahorro", "costo por conversación", "Meta cobra"
fuente-única-de: las decisiones de diseño que bajan el consumo de IA
combina-con: restricciones-plataforma-prometheo, embudos-y-tags, framework-seguimientos
---

# Ahorro de tokens en el diseño del CRM

> El detalle (tarifas, método de medición, consejos de Prometheo Soporte, números de EDFAN)
> vive en la skill `criterio-calificacion-leads` › `references/ahorro-de-tokens.md`. Acá van
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
6. **Una respuesta en un solo mensaje** (revisar mensajes humanizados) desde que Meta cobra
   los mensajes de servicio fuera de pauta (1/10/2026).
7. **Recarga automática con piso** en el go-live (restricción 8).

## Control en Etapa 4
Comparar el costo por conversación del panel de consumo antes y después de cada cambio, un
cambio por vez. El tablero de IC lo muestra en la pestaña "Consumo de Tokens - CRM".
