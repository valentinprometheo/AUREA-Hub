# Protocolo de Iteración del Prompt

> **Paso:** 4 (Entrega Etapa 2)
> **Pre-requisito:** Prompt V1 entregado al cliente
> **Output:** Prompt versionado y aprobado

---

## Filosofía

El Prompt V1 NUNCA es el Prompt final. Es la **primera materialización** de las Reglas Diseño de Prometheo by AUREA y como tal, expone:

1. Lo que el cliente NO había podido visualizar en abstracto
2. Casos de uso que no aparecieron en Discovery
3. Tonos y formas que en la práctica no funcionan
4. Lógicas que en el papel parecían correctas pero al hablar suenan raras

**Regla:** la iteración del Prompt es donde el diseño se pule de verdad. Hay que entrarle con ganas, no con resistencia.

---

## Versionado

### Convención de naming

```
[CLIENTE] - Prompt - V[N].md
```

Ejemplos:
- `TKVA - Prompt - V1.md`
- `TKVA - Prompt - V2.md`
- `TKVA - Prompt - V3 FINAL.md`

### Cuándo crear una versión nueva

| Tipo de cambio | Acción |
|---|---|
| Ajuste menor de tono (1-3 frases) | Edición directa en la versión activa, sin crear nueva |
| Cambio en algún FAQ o ejemplo | Edición directa en la versión activa |
| Cambio en autonomía del agente | **Versión nueva** (es un cambio estructural) |
| Agregar/quitar Smart Tag | **Versión nueva** |
| Cambio en lógica de derivación | **Versión nueva** |
| Cambio en estructura del flujo | **Versión nueva** |

### Documentación de cambios entre versiones

Cada versión nueva debe llevar al inicio del archivo un **changelog**:

```markdown
## Changelog V2 ← V1 (22 mayo 2026)

**Cambios solicitados por TKVA después de demo:**
- Tono más sobrio en saludos iniciales (TKVA pidió menos calidez, más institucional)
- Agregar pregunta sobre destino del lead (vivienda vs inversión) antes de calificar
- Quitar mención a financiación en saludo (se mantiene solo si el lead pregunta)
- Agregar Smart Tag #consulta_unidad_disponible_proyecto_entregado

**Cambios internos AUREA (no solicitados, mejora del diseño):**
- Refactor de la sección 7 (manejo objeciones) — más conciso
- Variable `tipo_destino` agregada a la ficha
```

---

## Cómo se procesa el feedback del cliente

### Captura del feedback

El feedback de una demo se recoge en el **Documento de Feedback de Demo** — un DOCX
apaisado de dos columnas (captura de la respuesta del agente / corrección). Lo genera la
skill `prometheo-diseno-agente-ia-feedback`; su metodología está en
`protocolo-feedback-demo.md` (misma carpeta).

**Modalidad recomendada:**
1. El consultor completa el Documento de Feedback en vivo con el cliente durante la primera demo, para transferir el criterio de corrección.
2. Después el cliente sigue completándolo de forma asincrónica con su equipo.
3. Cada corrección se clasifica con la matriz de abajo antes de aplicarse al prompt.

> Para feedback del **diseño en abstracto** (no de la demo del agente), el cliente puede
> comentar directamente en el Google Doc del DOCX de diseño. El Documento de Feedback de
> Demo es específicamente para el feedback de la demo del agente funcionando.

### Clasificación de feedback

| Tipo | Acción | Ejemplo |
|---|---|---|
| **Crítico** | Aplicar siempre | "El agente no puede decir el precio" |
| **Mejora real** | Aplicar | "Sería mejor que pregunte el barrio antes" |
| **Cosmético** | Aplicar | "Cambiar 'hola' por 'buen día'" |
| **Ambiguo** | Repreguntar al cliente | "Que sea más cálido" → ¿qué significa "más cálido"? |
| **Contradice modelo v7** | Conversar | "Que use 3 Smart Tags a la vez" → no se puede |
| **Out of scope** | Postergar | "Que también responda en inglés" → Fase 2 |

### Conversaciones difíciles

**Cuando el cliente pide algo que rompe el modelo v7:**

No decir "no se puede". Decir:

> "Entiendo lo que querés lograr. La forma de hacerlo dentro del modelo de Prometheo es [opción A] o [opción B]. La que pediste no es viable porque [explicación breve]. ¿Cuál de las dos te parece mejor?"

Mantener al cliente en el lado de las decisiones, no en el lado de los problemas.

---

## Sesiones de iteración

### Estructura de una sesión típica (60-90 min)

| Bloque | Duración | Contenido |
|---|---|---|
| Demo del agente | 15 min | Mostrar conversaciones reales del agente con la versión actual |
| Recorrido del feedback | 30 min | Revisar punto por punto lo que el cliente marcó |
| Decisiones | 15 min | Cerrar qué se aplica, qué se posterga, qué se conversa más |
| Próximos pasos | 5 min | Definir cuándo viene la próxima demo |

### Cuándo termina la iteración

**Señales de que ya está:**
- El cliente dice "ya está, esto está redondo"
- En una demo, el cliente no marca ninguna corrección
- Se entran a discutir cosas muy menores (cosméticas)
- Llevamos 3+ iteraciones y los cambios son cada vez más chicos

**Señales de que falta:**
- El cliente todavía tiene dudas sobre cómo va a usarse en producción
- Aparecen casos de uso nuevos en cada demo
- Hay cambios estructurales pendientes (no cosméticos)

---

## Errores comunes en la iteración

### 1. Aplicar todo el feedback sin filtro

**Síntoma:** el prompt crece a 8000 palabras y se vuelve inconsistente
**Solución:** filtrar con la matriz de clasificación. No todo feedback merece aplicarse.

### 2. Discutir en vez de demostrar

**Síntoma:** se argumenta sobre el feedback en abstracto, el cliente no cede
**Solución:** mostrar en demo cómo se ve el feedback aplicado vs no aplicado. La práctica desempata.

### 3. No usar memoria del cliente

**Síntoma:** el cliente vuelve a marcar lo que ya se discutió en la iteración anterior
**Solución:** mantener un log de "decisiones cerradas" que se comparte con el cliente

### 4. Iteraciones sin demo

**Síntoma:** el cliente lee el .md del prompt y da feedback teórico
**Solución:** **siempre hay demo antes de iteración**. Sin demo, no hay feedback válido.

---

## Cuándo bloquear el Prompt

Cuando se alcanza la versión final aprobada por el cliente:

1. Renombrar el archivo: `[CLIENTE] - Prompt - V[N] FINAL.md`
2. Agregar callout al inicio:

```markdown
═══════════════════════════════════════════════════════════
✅ PROMPT VALIDADO — VERSIÓN FINAL
Validado por: [Nombre del cliente]
Fecha: [DD/MM/AAAA]
Versión: V[N]
═══════════════════════════════════════════════════════════
```

3. Exportar PDF de respaldo
4. Mover a la carpeta `Drive / [CLIENTE] / 03 - Entregables Etapa 2 / Aprobados /`
5. **Solo entonces** se genera la Guía Implementador (Ronda 2)

---

## Caso de referencia

El proceso de iteración de MIA App (Prompt V5 → V7 con reglas de diseño Prometheo rediseñado mid-iteración) es el caso de referencia.

**Lo que se aprendió en MIA:**
- A veces el feedback dispara un cambio estructural (no cosmético)
- Mejor pausar la iteración, rediseñar las Reglas Diseño de Prometheo by AUREA, y arrancar la versión nueva limpia
- No "parchear" cuando el problema es estructural
- Comunicar al cliente que va a haber una nueva versión "limpia" en vez de una iteración más
