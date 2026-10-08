# Protocolo de Go-Live

> **Paso:** 5 (Implementación + Go-Live + Monitoreo)
> **Sub-fase:** Testing → Soft Launch → Go-Live MVP
> **Duración:** ~2 semanas
> **Pre-requisito:** Implementación en Prometheo completada

---

## Filosofía

El Go-Live tiene **3 sub-fases progresivas**, no es un evento único. Cada sub-fase valida cosas distintas con riesgo creciente:

1. **Testing interno** — riesgo cero (solo equipo AUREA + cliente)
2. **Soft launch** — riesgo bajo (tráfico limitado)
3. **Go-live MVP** — operación al 100%

**Regla:** no se salta etapas. Saltar testing o soft launch siempre genera retrabajo costoso.

---

## Sub-fase 1 — Testing interno (3-5 días)

### Objetivo

Validar que el agente responde correctamente a los **20 casos más típicos** identificados en Discovery, sin que nadie del cliente final esté hablando con él.

### Cómo se ejecuta

1. **Definir los 20 casos de testing** — extraídos del Discovery (B4 FAQs + B5 Objeciones + casos típicos)
2. **Equipo AUREA + cliente conversan con el agente** desde sus propios WhatsApp
3. **Cada conversación se documenta** — qué se preguntó, qué respondió el agente, qué tendría que haber respondido
4. **Se marcan los gaps** — en una tabla de "Hallazgos del Testing"

### Tabla de testing

| # | Caso | Mensaje del usuario | Respuesta del agente | Esperado | OK/❌ | Acción |
|---|---|---|---|---|---|---|
| 1 | Consulta inicial proyecto X | "Hola, info Drago Select" | [respuesta] | [esperado] | ✅ | — |
| 2 | Pregunta de precio sin calificar | "¿Cuánto sale?" | [respuesta] | [esperado] | ❌ | Ajustar lógica de precios |
| ... | ... | ... | ... | ... | ... | ... |

### Criterio de pase a Soft Launch

- 18 de 20 casos resueltos correctamente (90%)
- Los 2 casos restantes son ajustes menores (no estructurales)
- Cliente confirma que está cómodo con el comportamiento

---

## Sub-fase 2 — Soft Launch (1 semana)

### Objetivo

Validar que el agente funciona con **tráfico real pero limitado**. Detecta casos que no aparecieron en Testing por ser difíciles de prever.

### Cómo se ejecuta

#### Opción A — Por canal

Activar el agente solo en **1 canal** (ej: solo WhatsApp, no Instagram). Los otros canales siguen en modo manual del equipo humano.

#### Opción B — Por horario

Activar el agente solo en **horarios fuera de oficina** (cuando el equipo humano no está). Durante horario de oficina, sigue atendiendo el equipo humano.

#### Opción C — Por proyecto / producto

Activar el agente solo para **consultas de 1 proyecto / producto específico**. Para los demás, sigue el flujo manual.

**Cuál elegir:** depende del cliente. Para desarrollistas, suele ser Opción C (1 proyecto piloto). Para insumos/mobiliario, Opción A es más común.

### Monitoreo durante Soft Launch

- **Diario:** revisar las conversaciones del día anterior (todas)
- **Identificar gaps:** lo que respondió mal, lo que escaló mal, lo que no resolvió
- **Ajustar diariamente:** cambios chicos al prompt si aparecen patrones

### Métricas mínimas de Soft Launch

| Métrica | Objetivo |
|---|---|
| % conversaciones resueltas sin escalado humano | > 60% |
| Tiempo de respuesta promedio | < 30 segundos |
| Errores graves (info incorrecta, tono inadecuado) | < 5% de conversaciones |
| Satisfacción del cliente (encuesta interna) | "Estoy cómodo con lo que veo" |

### Criterio de pase a Go-Live MVP

- Las métricas mínimas están alcanzadas
- El cliente confirma que está listo para escalar
- No hay bugs estructurales pendientes

---

## Sub-fase 3 — Go-Live MVP

### Objetivo

Agente atendiendo el **100% de consultas entrantes** según el alcance MVP definido.

### Qué incluye el MVP

Solo lo aprobado en el Prompt final + Guía Implementador. **Nada más.**

Lo que NO entra al MVP (queda para Fase 2):
- Funcionalidades marcadas como "Post-MVP" en el diseño
- Integraciones complejas con sistemas legacy
- Multi-idioma
- Personalización avanzada por segmento

### Anuncio del Go-Live

#### Interno (cliente)
- Mail a todo el equipo del cliente: "El agente está en vivo a partir de hoy. Acá los puntos a tener en cuenta..."
- Reunión corta con vendedores para repasar cómo reciben los leads derivados

#### Externo (cliente final)
- En general, **NO se anuncia que es un agente IA**
- Si el cliente quiere comunicar la novedad, AUREA ayuda con el copy
- La conversación se diseña para sentirse natural, no para identificarse como bot

### Primeras 72 horas post Go-Live

**Monitoreo intensivo:**
- Consultor AUREA disponible en horario hábil
- Revisión de las primeras 50 conversaciones reales
- Ajustes diarios si aparecen problemas
- Comunicación constante con el cliente

### Criterio de cierre de Go-Live (transición a Monitoreo continuo)

- 1 semana de operación sin bugs estructurales
- Métricas dentro del rango esperado
- Equipo humano cómodo con cómo reciben los leads derivados
- Cliente firma que el MVP está operando como diseñado

---

## Checklist completo del Go-Live

### Pre Go-Live (semana previa)

- [ ] Implementación en Prometheo 100% completa
- [ ] Testing interno con 20 casos aprobado
- [ ] Soft Launch ejecutado con métricas mínimas alcanzadas
- [ ] Cliente listo para el cambio
- [ ] Equipo humano del cliente capacitado (sesión de transferencia)
- [ ] Mail de anuncio interno preparado
- [ ] Consultor AUREA bloqueado para monitoreo intensivo primeras 72hs

### Día del Go-Live

- [ ] Activar el agente en TODOS los canales del MVP
- [ ] Mail de anuncio interno enviado
- [ ] Primera conversación real monitoreada en tiempo real
- [ ] Sin bugs en las primeras 5 conversaciones

### Post Go-Live (primeras 72 horas)

- [ ] Revisión de las primeras 50 conversaciones
- [ ] Reunión rápida con cliente al final de cada día
- [ ] Ajustes menores aplicados si aparecen
- [ ] No hay alertas críticas

---

## Plan de rollback

**Si algo sale muy mal:**

1. **Desactivar el agente** en Prometheo (1 click)
2. **Volver a flujo manual** del equipo humano
3. **Diagnosticar la causa** en reunión urgente AUREA + cliente
4. **Corregir** y volver a Soft Launch
5. **Comunicar internamente** al equipo del cliente qué pasó

**Regla:** mejor hacer rollback temprano que mantener un agente roto operando.
