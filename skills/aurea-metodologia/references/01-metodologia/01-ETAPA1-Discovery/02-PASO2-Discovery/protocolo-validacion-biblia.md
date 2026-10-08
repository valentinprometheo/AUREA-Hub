# Protocolo de validación de la Biblia

> **Propósito:** Cerrar formalmente la Etapa 1 con la Biblia validada como fuente oficial del negocio del cliente.
> **Cuándo se ejecuta:** Cuando los bloques del Discovery (ver `estructura-discovery.md`) tienen información suficiente para diseñar Etapa 2.

---

## Por qué importa la validación

La Biblia es la **fuente única de verdad** sobre la cual se construye toda Etapa 2 (reglas de diseño Prometheo + DOCX + Prompt + Guía Implementador). Si la Biblia tiene errores o info no validada, esos errores se propagan a todos los entregables posteriores.

**Regla:** ningún diseño de Etapa 2 puede arrancar sin Biblia validada y firmada por el cliente.

---

## Cuándo arrancar la validación

**Criterios de readiness:**

- [ ] Los bloques del Discovery tienen contenido suficiente (no necesariamente perfecto)
- [ ] Las preguntas críticas del Asincrónico están respondidas o marcadas como "no aplican"
- [ ] El Documento 3 tiene material crítico cargado (al menos 1 brochure/catálogo por tipología macro)
- [ ] El consultor revisó la Biblia y no detecta contradicciones internas

**Si falta algo crítico:** se programa una última reunión de cierre antes de arrancar la validación.

---

## Cómo se ejecuta la validación

### Paso 1 — Notificación al cliente

El consultor envía un mensaje al cliente:

> "Equipo de [CLIENTE], terminamos las reuniones de Discovery. El Documento 1 (la Biblia) está ahora en estado **'para validación'**. Les pedimos que la revisen en su tiempo, agreguen comentarios donde algo no esté claro o esté mal, y nos avisen cuando esté lista para firmar. Calculen 5-7 días para una revisión cómoda."

### Paso 2 — Revisión por el cliente

El cliente:
1. Lee la Biblia completa (todos los bloques del Discovery)
2. Agrega comentarios en Google Docs donde:
   - Hay un error de hecho
   - Falta contexto crítico
   - El consultor interpretó algo distinto a lo que quiso decir
   - Quiere agregar info nueva
3. Avisa cuando terminó

### Paso 3 — Iteración

El consultor:
1. Revisa todos los comentarios del cliente
2. Corrige lo correctible directamente en el doc
3. Para los puntos ambiguos: agenda una reunión corta (30-45 min) para resolver
4. Devuelve el doc actualizado al cliente

**Iteración esperada:** 1-3 ciclos. Si llega al 4to ciclo, hay un problema metodológico que conviene conversar.

### Paso 4 — Firma de la Biblia

Cuando el cliente confirma que "todo está bien":

1. Se agrega al inicio del documento un **callout de validación**:

```
═══════════════════════════════════════════════════════════
✅ BIBLIA VALIDADA — FUENTE OFICIAL
Validada por: [Nombre del cliente]
Fecha: [DD/MM/AAAA]
Versión: v1.0
═══════════════════════════════════════════════════════════
```

2. Se exporta una copia en PDF como respaldo (naming: `[CLIENTE] - Biblia v1.0 VALIDADA - [fecha].pdf`)
3. Se guarda en la carpeta de Drive del cliente, en `00 - Documentos del Discovery / Biblia validadas /`
4. Se sigue trabajando sobre el Google Doc para iteraciones futuras, pero la versión firmada queda como referencia

---

## Qué hacer si la Biblia cambia después de la validación

**Mucho más frecuente de lo que parece.** Durante Etapa 2 (Diseño), se descubren cosas que requieren ajustar la Biblia.

**Protocolo:**

1. El consultor identifica el cambio necesario
2. Lo comenta con el cliente
3. Si el cliente confirma, se actualiza la Biblia
4. Se actualiza el callout de validación a v1.1, v1.2, etc.

**Regla:** la Biblia es viva. Las versiones se acumulan, no se sobrescriben.

---

## Cómo se ve la Biblia firmada — ejemplo de callout

```
═══════════════════════════════════════════════════════════
✅ BIBLIA VALIDADA — FUENTE OFICIAL
TKVA — Versión 1.0
Validada por: [Nombre del cliente] el 22 mayo 2026
Próxima revisión obligatoria: antes del go-live (junio 2026)
═══════════════════════════════════════════════════════════

Esta Biblia es la fuente oficial sobre la cual se diseñará la
Etapa 2 (CRM + Agente IA + Implementador). Cualquier cambio
posterior debe ser registrado como nueva versión.

—— Equipo AUREA Hub
```

---

## Checklist final de validación

Antes de cerrar formalmente la Etapa 1, verificar:

- [ ] Los bloques del Discovery están completos (no necesariamente perfectos, pero sí completos)
- [ ] El cliente firmó el callout de validación
- [ ] PDF exportado y guardado en Drive
- [ ] Asincrónico cerrado o con preguntas restantes marcadas como "no críticas para Etapa 2"
- [ ] Documento 3 con material crítico mínimo cargado
- [ ] Consultor confirma internamente que la Biblia es suficiente para arrancar Paso 3

**Solo cuando todo esto está, se arranca el Etapa 2 (Diseño de las Reglas Diseño de Prometheo by AUREA).**
