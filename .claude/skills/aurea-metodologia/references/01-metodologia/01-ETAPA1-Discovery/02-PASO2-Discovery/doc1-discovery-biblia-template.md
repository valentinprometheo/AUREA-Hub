# Doc 1 — Discovery (Biblia) — Template

> **Tipo:** Cliente-facing + interno AUREA (mixto)
> **Modalidad:** Sincrónico — se llena en vivo durante cada reunión
> **Plataforma:** Google Doc compartido en carpeta cliente
> **Estado al cierre:** Fuente oficial validada y congelada

---

## Propósito

Es el documento central de Etapa 1. Cuando se cierra, queda como la **Biblia del negocio del cliente**: la fuente oficial sobre la cual se diseña todo lo demás (Etapa 2, prompt, CRM, campañas).

**Regla:** ningún diseño de Etapa 2 puede contradecir lo que diga la Biblia validada. Si surge contradicción, se actualiza la Biblia primero.

---

## Estructura: los bloques del Discovery

La Biblia se organiza en los **bloques temáticos del Discovery**, que cubren la totalidad
del negocio comercial del cliente. Cada bloque tiene preguntas específicas, y cada pregunta
se completa con la estructura de 4 partes.

> **La estructura de bloques está definida en un solo lugar:**
> `estructura-discovery.md` (fuente única). Este template **no re-lista los bloques** —
> sigue los que define ese archivo: B0-B13 más los condicionales B13 Logística y B2B. Si la
> estructura de bloques cambia, se cambia en `estructura-discovery.md`, no acá.

### Estructura de cada pregunta

| Campo | Contenido |
|---|---|
| **Por qué te preguntamos esto** | Explicación breve de para qué nos sirve la información — cómo alimenta al agente, al CRM o a las campañas |
| **La pregunta concreta** | La pregunta tal como aparece en la conversación. Se repregunta según las respuestas. |
| **Lo que ya sabemos** | Lo inferido del análisis previo (auditoría web + IG del Paso 1) |
| **Lo que nos cuentan** | Espacio en blanco donde se tipea en vivo. Es la fuente oficial al final. |

---

## Cómo se completa la Biblia

### Durante la reunión

1. **Pantalla compartida** — el consultor abre el documento
2. **Bloque por bloque** — se va abriendo según el orden lógico del día
3. **Tipeo en vivo** — se transcribe lo que el cliente cuenta
4. **Repregunta natural** — se va profundizando según las respuestas
5. **No se interpreta en vivo** — se transcribe; la traducción CRM es trabajo posterior

### Después de la reunión

1. Se ordena lo transcripto
2. Se identifican gaps que van al Doc 2 (Asincrónico)
3. Se actualiza "Lo que ya sabemos" con lo nuevo aprendido

---

## Validación

**Cuándo:** al cierre de Etapa 1, cuando los bloques del Discovery tienen información suficiente

**Cómo:**
1. Se envía al cliente el link al Google Doc
2. El cliente revisa, agrega comentarios, corrige
3. Iteración hasta que el cliente firma
4. **Se congela** como fuente oficial (notificación visual: "Biblia validada — fuente oficial")

Ver `protocolo-validacion-biblia.md` para el detalle.

---

## Caso de referencia

El documento "Diseño de CRM — MIA App" + "GD Developers — Etapa 1 — Formulario" + "EDFAN — Etapa 1 — Formulario" son los 3 casos de referencia de Biblias completas.

**Lo que MIA hizo especialmente bien:**
- Bloques bien separados, sin mezclar temas
- Repreguntas que profundizan en ejemplos concretos
- Distinción clara entre MVP y Fase 2

**Lo que GD Developers hizo especialmente bien:**
- Detección temprana de discrepancias entre lo declarado y lo encontrado en Drive
- Bloque B11 (excepciones) con casos reales del cliente

---

## Convenciones AUREA en la Biblia

- **Colores de anotación interna:**
  - 🔵 Pregunta pendiente
  - 🟠 Nota AUREA (no cliente-facing)
  - ⚪ Por confirmar
  - 🟢 Confirmado por cliente
  - 🔴 Bloqueante para Etapa 2

- **Formato preguntas:** título B[N] · Tema → preguntas numeradas

- **Naming archivo:** `[CLIENTE] - Discovery (Biblia) - v[N].docx` cuando se exporte
