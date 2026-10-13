# 00 — Sistema [FIJA] / [FLEXIBLE]

> Cómo se marcan las reglas dentro de las skills verticales de cada rubro.

---

## Qué es

Cada skill vertical (real estate, mobiliario, insumos, inmobiliaria) tiene reglas que definen cómo se diseña un agente de ese rubro. Cada regla está marcada con una de dos etiquetas: **[FIJA]** o **[FLEXIBLE]**.

El sistema existe para que el consultor sepa, de un vistazo, qué puede variar entre clientes del mismo rubro y qué no.

---

## [FIJA]

Una regla **[FIJA]** no cambia entre clientes del mismo rubro. Es una restricción estructural del rubro. Se aplica siempre, sin preguntarle al cliente.

**Ejemplo (real estate):** *"La tipología macro es el proyecto/desarrollo."* — Esto es fijo: todo desarrollista organiza su negocio por proyectos. No se pregunta, se aplica.

---

## [FLEXIBLE]

Una regla **[FLEXIBLE]** varía según el cliente. La skill vertical incluye:
- El **rango de variabilidad** (entre qué opciones puede moverse)
- La **pregunta de discovery** que la define

Si la pregunta de discovery no se hizo, la regla queda **sin definir** y no se puede diseñar esa parte del agente.

**Ejemplo (real estate):** *"¿El agente puede dar precios?"* — Esto es flexible: depende del cliente. La skill indica el rango ([PUEDE] / [NO PUEDE] / [RANGOS]) y la pregunta que lo define (bloque B8).

---

## Cómo se usa en la práctica

### Al diseñar un cliente

El consultor recorre las reglas de la skill vertical:
- Las **[FIJA]** se aplican directamente
- Las **[FLEXIBLE]** se resuelven con la respuesta del cliente relevada en Discovery

### Al evaluar si un Discovery está completo

Antes de pasar a Etapa 2, se verifica que **todas las reglas [FLEXIBLE] del rubro tengan respuesta**. Las que no la tengan van a la lista de preguntas pendientes del Doc 2 (asincrónico).

> Esta verificación es un check obligatorio del gate de cierre de Etapa 1.

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| Las 4 skills verticales (`prometheo-vertical-*`) | Cada regla de esas skills está marcada [FIJA] o [FLEXIBLE] |
| `prometheo-discovery-transversal` (skill) | El gate de cierre verifica las [FLEXIBLE] |
| Doc 2 — Asincrónico | Las [FLEXIBLE] sin respuesta van ahí |
| Doc 4 — Preguntas Clave de Aprobación | Las [FLEXIBLE] resueltas se validan ahí |
