# 01 — Operativa y Decisiones de Etapa 2

**Manual operativo para diseñar el CRM + Prompt del agente IA en Prometheo.**

---

## Cuándo aplicar este manual

- Cliente con Discovery cerrado (Doc 1, 2, 3, 4 aprobados)
- Cliente quiere arrancar a configurar el agente IA en Prometheo
- Vos sos el consultor que ejecuta el diseño

Si el cliente no tiene Discovery cerrado, primero ejecutar Etapa 1.

---

## Qué se entrega al final de Etapa 2

### Para el cliente (Ronda 1)

1. **DOCX Diseño de CRM** — presentación visual cliente-facing con 8 gráficos y feedback inline. Aprobar antes de avanzar.
2. **Prompt V1 del agente** — markdown con 14 secciones + 3 anexos. Aprobar antes de avanzar.

### 🛑 Punto de control obligatorio entre Ronda 1 y Ronda 2

### Para el equipo de implementación (Ronda 2 — solo después de aprobación cliente)

3. **Guía de Implementador** — documento operativo para configurar Prometheo paso a paso.

### Para AUREA (paralelo a todo)

4. **Patrones del rubro** — documento interno que destila aprendizajes para crear la skill vertical si no existe, o sumar al manual si ya existe.

---

## Las 3 preguntas obligatorias antes de arrancar

Antes de empezar a generar contenido, confirmar con el cliente:

### 1. ¿Cuál es la modalidad de catálogo?

| Modalidad | Dónde vive la info de productos/servicios | Cuándo aplica |
|---|---|---|
| **A — Hardcoded en el prompt** | Toda la info está dentro del prompt | Cliente con catálogo fijo que no cambia (5-15 productos/servicios estables) |
| **B — Integrado por API / fuente externa** | Plataforma externa (Tokko, PrestaShop, sitio web propio) | Catálogo dinámico que cambia frecuentemente |
| **C — Híbrido** | Estructura en prompt, detalles en fuente externa | Cliente con categorías fijas pero precios/stock variables |

**Por qué importa:** define qué va en la Sección 5 del prompt (info por producto), cuántas variables hardcodeadas, si la guía de implementador requiere paso de integración, qué tan rápido podés iterar.

### 2. ¿Qué plan de Prometheo tiene contratado el cliente?

- **Basic (49 USD/mes):** funcionalidades core, sin push 24/7
- **Pro (99 USD/mes):** suma push 24/7 fuera de horario laboral
- **Enterprise (149 USD/mes):** suma integraciones avanzadas + multi-equipo

**Por qué importa:** no diseñar funcionalidades que el plan del cliente no soporta. Si el cliente está en Basic y necesita push 24/7, hay que upgradearlo antes de Go-Live.

### 3. ¿Hay fecha de Go-Live definida?

Si sí, planificar Ronda 1 + Ronda 2 + testing + capacitación + monitoreo hacia atrás desde esa fecha. Si no, proponer plazo realista al cliente.

---

## Las 6 decisiones más sensibles del diseño

Estos son los puntos donde se cometen más errores. Tomarlas explícitamente con el cliente, no asumir.

### Decisión 1 — Tag vs Variable

Cuando aparece una clasificación nueva (ej: "el lead quiere financiación"), decidir si modelarlo como Smart Tag o Variable.

**Test rápido:**

```
La clasificación, ¿genera una acción operativa concreta?
(acción operativa = apagar agente, mandar notificación, disparar follow-up,
                    derivar a otro casillero)

├── SÍ → Smart Tag
└── NO → Variable
```

**Regla v7:** si dudás, va a ser Variable. Solo es Tag si NO podés modelar la acción operativa de otra manera.

### Decisión 2 — Cantidad de Smart Tags

**Modelo v7 (validado por bot oficial Prometheo):** 2 Smart Tags base por cliente.

- `#seguimiento_activo` — habilita follow-ups automáticos
- `#derivar_a_humano` — apaga el agente, notifica al área correspondiente

Si el cliente requiere más tags, **primero probar si se puede modelar con Variables**. Solo crear tag adicional si:
- Hay acción operativa específica que no se logra con Variables
- El cliente lo requiere explícitamente como ya validado en su operación

### Decisión 3 — Cantidad de Embudos

| Patrón | Cantidad típica de Embudos |
|---|---|
| Cliente simple (1 línea de negocio) | 1-2 embudos |
| Cliente intermedio (venta + soporte + FAQ) | 3-4 embudos |
| Cliente complejo (multi-rubro o multi-canal) | 5-6 embudos |

**Más de 6 embudos = revisar.** Probablemente se puedan agrupar.

### Decisión 4 — Variables del catálogo: hardcodear o no

**Regla:** lo que está en Tokko/PrestaShop/fuente externa, NO se hardcodea en el prompt.

**Excepción:** estructura general del catálogo (categorías macro, líneas de producto) sí va en el prompt, porque le da al agente el mapa general.

### Decisión 5 — Cantidad de Seguimientos

| Patrón | Cantidad de follow-ups |
|---|---|
| MVP estándar | 3-5 follow-ups |
| Cliente con ciclo de venta largo (mobiliario, real estate) | 4-7 follow-ups |
| Cliente con urgencia operativa (soporte 24/7) | 1-2 follow-ups solo en venta |

**Distribución por proceso:**
- Embudo Venta concentra la mayoría (típicamente 60-80% de los follow-ups)
- Embudo Soporte solo si aplica (check de resolución)
- Embudo FAQ solo si quedan consultas sin resolver

### Decisión 6 — Plantillas Meta para WhatsApp

```
¿El follow-up se dispara dentro de las 24hs del último mensaje del usuario?
├── Sí → Mensaje libre OK, sin plantilla Meta
└── No → Requiere plantilla Meta pre-aprobada
        ↓
    ¿La plantilla ya existe en la cuenta de Meta del cliente?
    ├── Sí → Listar plantilla a usar en la Guía de Implementador
    └── No → Bloque "ANTES DE GO-LIVE": cliente solicita aprobación a Meta
            (proceso 24-72hs, no se puede saltear)
```

---

## El workflow completo de Etapa 2

### Paso 1 — Setup del Project en Claude

1. Crear Project nuevo en Claude.ai
2. Project Instructions: pegar las skills `prometheo-etapa2-design/` + `prometheo-crm-graphics/` + `project-instructions-universal.md`
3. Project Knowledge: subir Doc 1, 2, 3, 4 del Discovery + caso de referencia del rubro (si aplica)
4. Skill vertical del rubro: cargar también en Project Instructions o Knowledge según corresponda

### Paso 2 — Lectura del Discovery

Antes de generar nada, Claude tiene que confirmar que leyó:
- Los 4 documentos del Discovery
- La skill maestra y la de gráficos
- El caso de referencia del rubro (si existe)

**Output del paso 2:** resumen de 5 líneas del cliente + listado de ambigüedades del Discovery (cosas que faltan o están poco claras).

### Paso 3 — Diseño de las Reglas Diseño de Prometheo by AUREA

En este orden:

1. **Embudos** — qué procesos paralelos atiende el agente
2. **Variables transversales** — datos que se llenan siempre
3. **Variable router** (`proceso_actual`) — decide qué variable de estado se activa
4. **Variables de estado por proceso** — una por embudo
5. **Smart Tags** — siguiendo modelo v7 (2 tags base)
6. **Variables operativas** (severidad, tipo_derivacion)
7. **Seguimientos** — fórmula de 4 requisitos

### Paso 4 — Generación de Ronda 1 (DOCX + Prompt)

**DOCX cliente-facing:**
- Aplicar las 10 convenciones AUREA (ver `04-convenciones-docx-cliente.md`)
- Incluir los 8 gráficos visuales (ver skill `prometheo-crm-graphics`)
- Bloques de feedback inline para que el cliente apruebe sección por sección

**Prompt del agente:**
- 14 secciones + 3 anexos (ver `05-estructura-prompt-agente.md`)
- Las fórmulas de seguimiento tienen que ser leíbles, no solo sintaxis técnica
- Aplicar el tono y voseo según el cliente

### 🛑 Paso 5 — Punto de control

Pausar la generación. Pasar al cliente:
- El DOCX
- El Prompt (opcional — algunos clientes prefieren solo el DOCX)

Esperar feedback. Si hay cambios → surgical edits sobre los archivos existentes (no regenerar de cero).

### Paso 6 — Generación de Ronda 2 (Guía de Implementador)

Solo después de aprobación del cliente. Generar guía operativa con 10 bloques (ver `06-estructura-guia-implementador.md`).

### Paso 7 — Documentación de patrones (paralelo a todo)

Durante toda la sesión, ir registrando patrones del rubro en archivo separado. Cuando se cierre el cliente, mover ese archivo a `01-metodologia/05-rubros/[rubro].md`.

---

## Reglas operativas innegociables

### Regla 1 — Surgical edits, no regeneración total

Cuando el cliente pide cambios, identificar la sección específica y modificar solo eso. Nunca regenerar un DOCX o Prompt entero por un cambio puntual. Razón: pérdida de contexto + más errores.

### Regla 2 — Nunca asumir comportamiento de Prometheo

Si surge una duda sobre cómo funciona la plataforma (regla de Smart Tags, sintaxis de seguimientos, comportamiento de variables), **consultar al bot oficial de Prometheo antes de avanzar**. No inventar.

### Regla 3 — Todo lo que está en fuente externa, NO se hardcodea

Tokko, PrestaShop, sitio web propio. Sus datos no entran al prompt. El prompt solo conoce la estructura general del catálogo, no los datos específicos.

### Regla 4 — El cliente nunca ve sintaxis técnica

En el DOCX cliente-facing, las cosas técnicas (proceso_actual=venta) van entre paréntesis y en font reducido. El protagonista es la frase comprensible ("Cuando la conversación es sobre comprar").

### Regla 5 — 1 sola Smart Tag activa por conversación (modelo v7)

Cuando aparece `#derivar_a_humano`, se retira `#seguimiento_activo`. Como regla operativa o nativa según lo que confirme el bot oficial. Esta es la regla más violada históricamente.

### Regla 6 — Las reglas de distribución se completan colaborativamente

Nunca asumir a quién va cada tipo de derivación. Dejar tabla con responsables en blanco para que el cliente la complete. Es patrón estándar AUREA.

### Regla 7 — Anti-duplicación

Cada pieza de información se documenta UNA SOLA VEZ en el manual. Si aparece en dos lugares, uno cita al otro. Razón: mantenibilidad.

---

## Errores frecuentes a evitar

| Error | Síntoma | Cómo evitarlo |
|---|---|---|
| Crear demasiados Smart Tags | El cliente termina con 10+ tags y se vuelve inmanejable | Test rápido tag vs variable, regla v7 |
| Hardcodear el catálogo en el prompt | Cada cambio de catálogo requiere editar el prompt | Modalidad B o C según corresponda |
| No validar comportamiento con bot oficial | Diseño que asume features que Prometheo no soporta | Consultar bot oficial antes de avanzar |
| Mezclar lenguaje técnico en DOCX cliente | Cliente no entiende y se traba en el feedback | Aplicar convención "frase comprensible primero" |
| Olvidar el punto de control entre rondas | Generar Guía de Implementador antes de aprobación cliente del DOCX/Prompt | Workflow obligatorio en 2 rondas |
| Inventar nombres de archivos PDF | "ficha-microcemento.pdf" sin confirmar que existe | Usar PLACEHOLDER explícito hasta listar Drive del cliente |
| Asumir franja horaria de follow-ups | "L-V 9-18hs" sin preguntar al cliente | Es decisión por cliente, levantar en Discovery |
| Mezclar regla operativa con regla nativa | "Cuando aparece tag X se retira Y" como si fuera automático cuando es manual | Documentar explícitamente cuál es cuál |

---

## Cómo medir si Etapa 2 salió bien

| Métrica | Cómo se mide | Target |
|---|---|---|
| **Velocidad de aprobación del DOCX** | Días desde entrega Ronda 1 hasta cliente aprueba | < 5 días hábiles |
| **Cantidad de iteraciones del DOCX** | Cuántas versiones (v1, v2, v3) hasta aprobación | Máximo 3 |
| **Cantidad de surgical edits** | Cuántos cambios puntuales pidió el cliente | Hasta 15 cambios = OK · más = revisar Discovery |
| **Tiempo de generación de Guía de Implementador** | Días desde aprobación cliente hasta entrega Guía | < 3 días hábiles |
| **Cantidad de re-trabajos en Etapa 3** | Cuántas veces se vuelve a modificar el prompt en Implementación | Máximo 2 (uno post-testing, uno post-Go-Live día 1) |

Si alguna métrica falla repetidamente: revisar el Discovery, no el Diseño.

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Reglas Diseño de Prometheo by AUREA (las 24 reglas) | `03-reglas-diseno-prometheo-by-aurea.md` |
| Convenciones del DOCX | `04-convenciones-docx-cliente.md` |
| Estructura del Prompt (14 secciones) | `05-estructura-prompt-agente.md` |
| Estructura de la Guía (10 bloques) | `06-estructura-guia-implementador.md` |
| Trazabilidad Etapa 1 → Etapa 2 | `02-trazabilidad-etapa1-etapa2.md` |
| Particularidades del rubro | `../05-rubros/[rubro].md` |
| Caso de referencia | `../08-casos-referencia/[caso].md` |
