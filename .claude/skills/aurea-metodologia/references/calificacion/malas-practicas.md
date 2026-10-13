# Malas prácticas de calificación y búsqueda (catálogo para auditar)

Cada una con su origen. Sirven para auditar una cuenta, un prompt o un tablero.

| # | Mala práctica | Por qué está mal | Qué hacer | Origen |
|---|---|---|---|---|
| 1 | Medir "calificados" con un criterio propio de AUREA | El cliente decide qué es un buen lead; un criterio ajeno infla o achica el número | Pedir la definición en el discovery; si no hay, rotular "propuesta" | EDFAN: 350 con criterio propio vs 252 con la regla del cliente |
| 2 | "% calificados = leads con variables completas" | Mide cantidad de datos, no intención ni fit | Obligatorios + sumas del cliente | Métricas de rubro de la metodología (corregido en v1.20) |
| 3 | Metas de % de calificados sin fuente (70%, 80%) | No hay benchmark universal (Forrester) | La meta sale de la línea base del cliente | Ídem |
| 4 | Contar lo que el agente ofreció como lo que el lead pidió | La variable se llena con la oferta, no con la demanda | Prompt de variable: "solo lo que pide el lead" | EDFAN: 131 registros de Tipo Unidad con varias tipologías |
| 5 | Guardar 0 cuando el lead no dijo el dato | El 0 parece dato y rompe promedios | "Si no lo dice, dejala vacía" | EDFAN: 285 presupuestos en 0 sobre la demanda |
| 6 | Mezclar finalidad y tipo de contacto en una variable | Proveedores terminan como "Inmobiliaria" | Variable "Tipo de contacto" excluyente + finalidad como hija | EDFAN: 6 proveedores con Tipo Perfil = Inmobiliaria |
| 7 | Usar un tag existente con otro significado (ej. VIP para urgencia) | Rompe la dimensión del tag | Tag propio "Hot Lead" | EDFAN: Contacto VIP = ya compró |
| 8 | Hot lead como etapa del embudo | La urgencia convive con cualquier etapa | Tag de prioridad fuera del embudo | EDFAN |
| 9 | "Corto plazo" sin días | No se puede medir ni filtrar | Definir días en el discovery | EDFAN |
| 10 | Seguimiento disparado por dos tags donde uno es una etapa que se reemplaza | Lógica AND: nunca se dispara | Un tag por seguimiento | Auditoría de prompts EDFAN |
| 11 | Ruteo por finalidad que no queda registrado | El tablero no puede ver a quién se avisó | Notificación por variable + moderador asignado | EDFAN: inversores con el mismo moderador |
| 12 | Reuniones descritas en una variable y no en el campo o tag | El embudo humano parece vacío | Tag de visita o reunión al describirla | EDFAN: 38 descritas, 8 con tag, 0 en el campo nativo |
| 13 | Calificar en el primer mensaje, presupuesto primero | El lead abandona | Orden: necesidad, plazo, capacidad, presupuesto | HubSpot GPCT |
| 14 | No-demanda dentro del embudo y con el agente activo | Gasta tokens y ensucia las tasas | Separar antes de calificar; apagar el asistente | EDFAN: 41 de 47 proveedores siguieron conversando |
| 15 | Etapas humanas con prompt de IA | Se evalúan en cada charla sin necesidad | Tags manuales | Consejo 13 de Prometheo |
| 16 | Recalificar la base sin prueba chica ni conteo esperado | Gasta saldo y es difícil de auditar | Procedimiento de Mi Prometheo | Esta skill |
| 17 | Filtrar por un valor ambiguo (ej. Tipo Derivación = Inmobiliaria) | Significa otra cosa en compradores | Definir el valor antes de usarlo | EDFAN: 9 compradores con ese valor |
