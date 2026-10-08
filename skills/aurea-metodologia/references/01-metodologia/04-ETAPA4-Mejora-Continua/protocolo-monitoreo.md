# Protocolo de Monitoreo

> **Paso:** 5 (Implementación + Go-Live + Monitoreo)
> **Sub-fase:** Monitoreo continuo post Go-Live
> **Duración:** 15+ días iniciales → relación de mejora continua
> **Pre-requisito:** Go-Live MVP completado

---

## Filosofía

El Monitoreo es donde el sistema **se vuelve realmente bueno**. Las primeras 2 semanas de operación generan más aprendizajes que todo el Discovery. No hay que tratarlo como "el cierre del proyecto" sino como **el arranque de la relación de mejora continua**.

**Regla:** la métrica más importante no es el % de respuestas correctas. Es **qué % de leads que NO habrían sido atendidos antes, ahora reciben atención**. Eso es valor real.

---

## Las 4 dimensiones del Monitoreo

### 1. Volumen y throughput

| KPI | Cómo medir | Frecuencia |
|---|---|---|
| Consultas entrantes totales | Conteo en Prometheo | Diaria |
| Consultas respondidas por el agente | Conteo en Prometheo | Diaria |
| Conversaciones derivadas a humano | Conteo de #derivar_a_humano | Diaria |
| Tiempo promedio de primera respuesta | Stat de Prometheo | Semanal |

### 2. Calidad de respuesta

| KPI | Cómo medir | Frecuencia |
|---|---|---|
| % conversaciones con respuesta acertada | Muestreo manual (10% conversaciones random) | Semanal |
| % conversaciones con info incorrecta | Muestreo manual | Semanal |
| % conversaciones con tono inadecuado | Muestreo manual | Semanal |
| Casos límite no resueltos | Detección por equipo humano | Continuo |

### 3. Funnel comercial

| KPI | Cómo medir | Frecuencia |
|---|---|---|
| Leads que avanzan a calificados | Movimiento en embudo | Semanal |
| Leads que avanzan a visita / demo | Movimiento en embudo | Semanal |
| Conversión a venta | Movimiento final | Mensual |
| Comparación vs baseline pre-agente | Cruce con datos históricos | Mensual |

### 4. Operación del equipo humano

| KPI | Cómo medir | Frecuencia |
|---|---|---|
| Tiempo que el vendedor dedica por lead | Tiempo desde derivación hasta cierre | Semanal |
| % leads derivados con ficha completa | Auditoría aleatoria | Semanal |
| Satisfacción del equipo humano | Encuesta interna corta | Mensual |
| Casos donde el equipo "tuvo que volver a preguntar" cosas | Reporte cualitativo | Semanal |

---

## Ritmo de Monitoreo

### Primeras 2 semanas post Go-Live (intensivo)

**Diario:**
- Revisión de todas las conversaciones del día
- Detección de gaps inmediatos
- Ajustes menores aplicados al día siguiente
- Standup corto con el cliente (15 min al final del día)

**Semanal:**
- Reunión de 45 min con cliente
- Reporte: volumen + calidad + funnel
- Decisiones de ajuste

### Semanas 3-8 (consolidación)

**Semanal:**
- Revisión muestreada (no todas las conversaciones)
- Detección de patrones, no de casos puntuales
- Reunión con cliente cada 2 semanas

**Quincenal:**
- Reporte ejecutivo con métricas de las 4 dimensiones
- Ajustes estructurales si aparecen patrones

### Mes 3 en adelante (régimen de mejora continua)

**Mensual:**
- Reporte completo de funnel + comparación vs baseline
- Reunión de revisión con cliente
- Roadmap de Fase 2 (features postergadas del MVP)

**Trimestral:**
- Revisión profunda con cliente
- Decisiones sobre evolución del agente
- Posibles ampliaciones de scope

---

## Tipos de ajuste post-launch

### Ajuste cosmético (puede hacerse rápido)
- Cambio de tono en una respuesta puntual
- Ajuste de redacción
- Corrección de typo

**Tiempo de implementación:** < 1 día
**Aprobación necesaria:** AUREA puede aplicarlo, avisar al cliente

### Ajuste de contenido (requiere validación)
- Nueva FAQ
- Nueva objeción y manejo
- Actualización de info de un proyecto/producto

**Tiempo de implementación:** 1-3 días
**Aprobación necesaria:** confirmación del cliente

### Ajuste estructural (requiere rediseño)
- Nuevo Smart Tag
- Nueva variable
- Cambio en lógica de derivación
- Cambio en flujo conversacional

**Tiempo de implementación:** 1-2 semanas
**Aprobación necesaria:** decisión del cliente + actualización del DOCX/Prompt/Guía

### Fase 2 (features postergadas)
- Funcionalidad que estaba marcada como "Post-MVP" en el diseño original
- Nueva integración
- Nuevo canal

**Tiempo de implementación:** depende del scope
**Aprobación necesaria:** propuesta comercial nueva o ampliación de scope

---

## Reporte de Monitoreo — Estructura tipo

### Reporte Semanal (durante primeras 2 semanas)

```
REPORTE SEMANAL — [CLIENTE]
Semana del [fecha] al [fecha]

📊 VOLUMEN
- Consultas totales: N
- Resueltas por agente: N (X%)
- Derivadas a humano: N (X%)
- Tiempo promedio de respuesta: X min

✅ CALIDAD (muestreo de N conversaciones)
- Respuestas acertadas: X%
- Info incorrecta detectada: X%
- Tono adecuado: X%

🎯 FUNNEL
- Leads calificados esta semana: N
- Visitas agendadas: N
- Vs semana anterior: +/- X%

⚠️ HALLAZGOS
- [Gap 1]: descripción + propuesta
- [Gap 2]: descripción + propuesta

✏️ AJUSTES APLICADOS
- [Ajuste 1]: descripción
- [Ajuste 2]: descripción

📅 PRÓXIMA SEMANA
- [Plan]
```

### Reporte Mensual (régimen continuo)

Mismo formato pero con:
- Comparación vs baseline pre-agente
- Tendencia mensual de cada métrica
- Roadmap de Fase 2 actualizado

---

## Cuándo el cliente termina la relación con AUREA

Posibilidades:

**A) Régimen permanente con AUREA** — mantiene la consultoría mensual para mejora continua y nuevas features

**B) Transferencia al implementador interno del cliente** — cuando el cliente tiene equipo técnico propio que puede mantener el agente, AUREA hace transferencia de conocimiento

**C) Cierre formal** — algunos clientes solo necesitan el MVP y se manejan solos después

**Para cualquiera de las 3:** AUREA queda como referencia disponible. La metodología sigue documentada en el Drive del cliente.

---

## Métricas de éxito del proyecto completo

Al cierre de los primeros 3 meses, evaluar:

| Métrica | Pregunta clave |
|---|---|
| Volumen | ¿Atendimos más consultas que antes? |
| Calidad | ¿El nivel de respuesta es comparable o superior al humano? |
| Funnel | ¿Mejoró la conversión a visita / venta? |
| Equipo | ¿El equipo humano usa mejor su tiempo ahora? |
| Cliente final | ¿Los compradores están satisfechos con la experiencia? |

Si la respuesta a 4 de 5 es SÍ → proyecto exitoso. Si es menos, hay que rediseñar partes.
