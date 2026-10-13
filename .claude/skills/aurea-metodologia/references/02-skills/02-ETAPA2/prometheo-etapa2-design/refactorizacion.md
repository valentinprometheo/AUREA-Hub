# MÓDULO: DOC DE REFACTORIZACIÓN

Output 3 de Etapa 2. Es el documento que registra dos cosas:
- **Información pendiente** de los inputs de Etapa 1 que sigue sin estar
- **Inconsistencias detectadas** entre las fuentes (Doc 1 vs brochures vs auditoría
  web vs Doc 4)

Es **interno-cliente mixto**: el cliente lo ve para entender qué falta y qué
contradicciones hay, pero la lógica de cómo armarlo es interna del consultor.

---

## CUÁNDO SE GENERA

- **Siempre se genera**, aunque los inputs de Etapa 1 estén "completos"
- Si la Etapa 2 arrancó incompleta (sin Doc 4 cerrado, sin Doc 2 completo,
  etc.), este documento es CRÍTICO porque registra los gaps
- Si hay brochures, planos, fotos: revisarlos y comparar contra Doc 1
- Si NO hay inputs complementarios: el documento solo tendrá Sección A
  (pendientes) y Sección B vacía o reducida

---

## ESTRUCTURA DEL DOCUMENTO

### Portada
- Eyebrow: "AUREA Hub × Prometheo"
- Título: "[CLIENTE] — Doc de Refactorización"
- Subtítulo: "Información pendiente e inconsistencias detectadas"
- Fecha de la revisión

### Sección A — Información pendiente de Etapa 1

Tabla con las siguientes columnas:

| # | Qué falta | De qué input depende | Qué bloque del prompt afecta | Criticidad |
|---|---|---|---|---|

**Criticidad:**
- **Alta** (rojo): bloquea el Go-Live. Sin esto, el agente no puede salir.
  Ejemplos: responsables de derivación, mail de soporte, links oficiales,
  catálogo de productos.
- **Media** (naranja): bloquea calidad. El agente sale pero con respuestas
  genéricas o incompletas. Ejemplos: tono de voz específico, FAQs avanzadas,
  copys de seguimientos literales.
- **Baja** (gris): mejora opcional. El agente sale sin esto y funciona.
  Ejemplos: KPIs adicionales, casos borde no frecuentes, branding fino.

**Reglas para llenar:**
- Cada item se mapea a UN bloque del prompt (típico: B0–B11 del discovery)
- Si el item depende de múltiples inputs, listar todos
- La descripción debe ser específica, no genérica:
  - Mal: "Faltan los responsables"
  - Bien: "Falta el responsable de tipo_derivacion = legal con WhatsApp y mail"

### Sección B — Inconsistencias detectadas entre inputs

Tabla con las siguientes columnas:

| # | Tema | Fuente A dice | Fuente B dice | Hipótesis tomada | Validación pedida |
|---|---|---|---|---|---|

**Casos típicos de inconsistencia:**

1. **Brochure comercial vs Doc 1**:
   - Brochure dice "30 unidades disponibles", Doc 1 dice "25 unidades"
   - Brochure dice "entrega en marzo 2026", Doc 1 dice "Q2 2026"
   - Brochure menciona producto/servicio que Doc 1 no menciona

2. **Auditoría web vs Doc 1**:
   - Web tiene formulario de contacto, Doc 1 dice que solo entran por WhatsApp
   - Web menciona zona de cobertura X, Doc 1 menciona zonas X+Y+Z

3. **Doc 4 vs Doc 1**:
   - En Doc 4 cliente respondió A, pero Doc 1 (síntesis) dice B
   - Cliente cambió de opinión entre reuniones

4. **Material visual vs descripción**:
   - Las fotos del producto muestran terminación X, descripción dice terminación Y
   - Los planos muestran amenities W+Z, brochure dice W+X+Y

**Reglas para llenar:**
- Citar literal de cada fuente cuando sea posible (con referencia: "Doc 1, sección 4.2")
- La "Hipótesis tomada" es la decisión del consultor: cuál fuente prevalece y por qué
- La "Validación pedida" es la pregunta concreta para el cliente: "Confirmar que
  son 25 unidades (Doc 1) y no 30 (brochure)"

### Sección C (opcional) — Decisiones tomadas sin confirmación

Lista de cosas que el consultor decidió por su cuenta porque no había info, pero
que el cliente debería revisar. Ejemplo:
- "Seteamos el horario de seguimientos a L-V 10-18hs por defecto. Validar."
- "Asumimos que las inmobiliarias B2B se derivan a Comercial. Confirmar."

---

## TONO DEL DOCUMENTO

- **Neutral, no acusatorio.** Las inconsistencias no son "errores del cliente",
  son "puntos a resolver". Lenguaje constructivo.
- **Específico, no vago.** Cada item con dato concreto.
- **Accionable.** Cada item lleva a una pregunta o tarea concreta.

---

## INTEGRACIÓN CON LOS OTROS OUTPUTS

- Si la Sección A tiene items de criticidad ALTA → estos van también a la
  Sección 11 del DOCX de CRM ("Pendientes Críticos")
- Si la Sección B tiene inconsistencias resueltas (con hipótesis tomada) → la
  hipótesis se aplica al prompt y se documenta en este doc para que el cliente
  pueda revertir si está mal
- Si la Sección C tiene decisiones por defecto → se mencionan en el bloque de
  feedback de la sección correspondiente del DOCX

---

## CHECKLIST FINAL

- [ ] Portada con cliente, fecha, versión
- [ ] Sección A: tabla con qué falta + dependencia + bloque + criticidad
- [ ] Sección B: tabla con tema + fuente A vs B + hipótesis + validación
- [ ] Sección C (si aplica): decisiones tomadas sin confirmación
- [ ] Items críticos de Sección A están sincronizados con Sección 11 del DOCX
- [ ] Tono neutral y accionable
- [ ] OOXML válido si va en DOCX

---

## FORMATO DE SALIDA

Por defecto: **DOCX** con la misma paleta AUREA y el styles minimal del
DOCX de CRM (consistencia visual entre los 3 outputs).

Alternativa: **.md** si el cliente prefiere markdown — pero el output principal
es DOCX.

Tamaño esperado: 3-8 páginas (mucho más corto que el DOCX de CRM).
