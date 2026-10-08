# 04 — Convenciones del DOCX Cliente-Facing

**Las 10 convenciones AUREA para presentar el diseño al cliente.**

---

## Qué es el DOCX cliente-facing

Es el documento que el cliente recibe al final de Etapa 2, junto con el Prompt. Se entrega en formato Word (.docx) para que pueda escribir feedback inline antes de aprobar.

**Audiencia:** dueño / decisor / equipo comercial del cliente. **No es técnico**, no entiende sintaxis de Prometheo. Le tiene que llegar visual y comprensible.

**Estructura macro (11 secciones):**

1. Roles del agente
2. Estrategia + KPIs
3. Autonomía del agente
4. Embudos
5. Variables
6. Smart Tags
7. 3 Escenarios de ejemplo
8. Seguimientos
9. Reglas de Distribución
10. Pendientes del equipo del cliente
11. Próximos pasos

Cada sección incluye un bloque de feedback amarillo al final para que el cliente apruebe/comente.

---

## Las 10 convenciones AUREA

### Convención 1 — Tabla KPIs con columna "Por qué lo medimos"

La tabla de KPIs siempre tiene 4 columnas, no 3:

| KPI | Qué mide | Cómo se mide | Por qué lo medimos |
|---|---|---|---|

La última columna ("Por qué lo medimos") es la más importante. Está en lenguaje cliente, no técnico. Explica qué decisión se toma con cada métrica.

**Razón:** sin esa columna, el cliente lee KPIs como dato técnico y no se conecta con la operación.

### Convención 2 — Reglas de Distribución con columnas para que el cliente complete

La tabla de Reglas de Distribución no se entrega completa. Se entrega con 2 columnas vacías para que el cliente las complete:

| Cuándo se dispara | tipo_derivacion | ¿Prometheo o WhatsApp? | Responsable (nombre/mail/tel) |
|---|---|---|---|
| Lead pide negociación | negociacion | ☐ ☐ | _______________ |

**Razón:** las decisiones operativas internas del cliente no se asumen. Es patrón estándar AUREA.

### Convención 3 — Cards de Autonomía con palabras clave en bold

Las dos columnas "Puede hacer" / "Nunca hace solo" se presentan como cards con bullets. **Las palabras clave de cada bullet van en bold**:

```
✅ PUEDE HACER
• Calificar al lead identificando zona, presupuesto y finalidad.
• Asesorar sobre zonas según perfil — **inversor** o **uso propio**.
• Mencionar **financiación**, cuotas y anticipo, sin negociar.
```

**Razón:** el cliente escanea el documento. El bold le permite captar la idea sin leer cada bullet completo.

### Convención 4 — Modificaciones antes→ahora con verde+bold

Cuando se actualiza una versión del DOCX y hay cambios respecto a la anterior, presentar la modificación como tabla antes→ahora con la columna "ahora" en bold y fondo verde claro:

| Antes | Ahora |
|---|---|
| Texto viejo | **Texto nuevo en bold y verde** |

**Razón:** el cliente identifica rápido qué cambió y no relee lo que ya estaba aprobado.

### Convención 5 — Smart Tags como cards con flecha →

Las Smart Tags se presentan visualmente como cards conectadas con una flecha entre el nombre y la subtitulación:

```
#seguimiento_activo → habilita follow-ups automáticos
```

No como tabla de 2 columnas separadas.

**Razón:** transmite mejor que la tag genera una acción consecuente.

### Convención 6 — Cards de Variables con ejemplo "Imaginate que llega Juan..."

Cada bloque de variables incluye un ejemplo aplicado con narrativa de persona ficticia:

```
EJEMPLO PARA QUE SE ENTIENDA

Imaginate que llega Juan por WhatsApp:
"Hola, vi su anuncio. Quiero un departamento en Palermo, tengo 100K."

El agente, sin que Juan se entere, llena estos casilleros:
• canal = whatsapp
• tipo_usuario = particular
• zona_interes = palermo
• presupuesto = 100000
• proceso_actual = venta

Resultado: el equipo ya sabe quién es Juan, qué busca y cuánto tiene,
sin haber leído el chat completo.
```

**Razón:** las variables son un concepto abstracto. El ejemplo lo aterriza.

### Convención 7 — Fórmula de seguimientos en 4 pasos pedagógicos

La fórmula del seguimiento NO se presenta como sintaxis técnica:

```
❌ Mal:
Disparo = #seguimiento_activo + proceso_actual=venta + estado_venta=info_enviada + 24hs
```

Se presenta como 4 requisitos visuales que coinciden al mismo tiempo:

```
✅ Bien:
Las 4 condiciones tienen que coincidir al mismo tiempo:

Requisito 1 — la etiqueta que habilita seguimientos
  Tag: el seguimiento está activo (#seguimiento_activo)

Requisito 2 — de qué proceso se trata
  Proceso: la conversación es de venta (proceso_actual = venta)

Requisito 3 — en qué etapa quedó el usuario
  Etapa: ya recibió toda la info (estado_venta = info_enviada)

Requisito 4 — cuánto esperar antes de escribir
  Tiempo: pasaron 24hs sin respuesta (24h)

→ El agente envía el mensaje
```

Y cerrar con un ejemplo aplicado completo.

### Convención 8 — Sección obligatoria "3 Escenarios de Ejemplo"

Entre Variables y Seguimientos, va una sección con **3 escenarios completos** que muestran cómo se conecta todo el modelo en casos concretos.

Cada escenario sigue el mismo patrón visual:

```
📨 Situación: mensaje del usuario entre comillas
🔄 Proceso identificado: embudo + variable router
💾 Variables que llena el agente: lista
🏷️ Smart Tags que se disparan: tag activa
⚡ Qué hace el agente:
   - Respuesta inmediata
   - Notificación al equipo
   - Seguimiento programado
```

Los 3 escenarios deben mostrar **3 procesos diferentes** (venta, soporte, FAQ) para cubrir el espectro.

**Razón:** es la pieza más útil del DOCX para que el cliente entienda el sistema en acción.

### Convención 9 — Mensajes follow-up con (emoji de saludo) en DOCX

En el DOCX, los mensajes literales de follow-up usan el placeholder `(emoji de saludo)`:

```
"(emoji de saludo) Hola [nombre], te llegó la info que te pasé?"
```

En el prompt de producción, va el emoji real elegido (👋, ☀️, etc.) o sin emoji.

**Razón:** dejar al cliente decidir qué emoji prefiere antes del Go-Live.

### Convención 10 — Próximos pasos con placeholder al Drive

La sección "Próximos pasos" siempre incluye un paso 1 con placeholder al Drive del cliente:

```
Paso 1 · Cerrar pendientes en el Drive
Ustedes completan los items de la sección 10 y suben los materiales
faltantes al Drive compartido: [PLACEHOLDER_LINK_DRIVE]
Responsable: equipo [CLIENTE] · Tiempo estimado: 5-7 días hábiles
```

El placeholder se reemplaza al entregar el DOCX final con el link real al Drive del cliente.

---

## Formato y estilo

### Tipografía
- Cuerpo de texto: 11pt
- Títulos de sección: 14pt bold
- Tablas: 10pt
- Bloques de feedback: 11pt sobre fondo amarillo claro

### Colores

Aplicar la paleta AUREA según categoría conceptual (ver `06-convenciones-aurea/01-paleta-y-colores.md`).

| Elemento | Color hex |
|---|---|
| Banner de sección (Estrategia) | Verde #4CAF80 |
| Banner de sección (Variables) | Azul #5B8FD9 |
| Banner de sección (Smart Tags) | Naranja #E8943A |
| Banner de sección (Roles/Autonomía) | Morado #7C5CBF |
| Cards de procesos Venta | Verde claro #E1F5EA |
| Cards de procesos Soporte | **Naranja claro #FFE5C2** |
| Cards de procesos FAQ | Azul claro #E3EEFC |
| Cards de procesos Urgencia/Alerta | **Rojo claro #FBE3E3** (nuevo) |
| Bloques de feedback (amarillo) | #FFF9D6 |
| Notas AUREA internas | Naranja claro #FFE5C2 |

### Iconos y emojis (USO LIMITADO)

Los iconos van solo en lugares específicos donde **agregan significado**:

| Icono | Cuándo se usa |
|---|---|
| ✅ | Encabezado de columna "Puede hacer" en Autonomía |
| ❌ | Encabezado de columna "Nunca hace solo" en Autonomía |
| 📨 | Etiqueta "Situación" en escenarios |
| 🔄 | Etiqueta "Proceso identificado" en escenarios |
| 💾 | Etiqueta "Variables que llena el agente" en escenarios |
| 🏷️ | Etiqueta "Smart Tags que se disparan" en escenarios |
| ⚡ | Etiqueta "Qué hace el agente" en escenarios |
| 🛑 | Punto de control entre rondas |

**No usar emojis decorativos** en texto general. No usar 🎯, 💡, 🚀, 📌 como adornos.

---

## Los 8 gráficos del DOCX

Cada sección del DOCX incluye gráficos visuales según la metodología de la skill `prometheo-crm-graphics`. Los 8 gráficos estándar son:

| # | Gráfico | Sección |
|---|---|---|
| 1 | Overview de Variables | Sección 5 (Variables) |
| 2 | Arquitectura de Variables (router + estados) | Sección 5 (Variables) |
| 3 | Overview de Smart Tags | Sección 6 (Smart Tags) |
| 4-6 | 3 Escenarios de ejemplo (flujo top-down completo) | Sección 7 (3 Escenarios) |
| 7 | Fórmula de Seguimiento (4 requisitos apilados) | Sección 8 (Seguimientos) |
| 8 | Distribución de Seguimientos por proceso | Sección 8 (Seguimientos) |

Adicionales según el cliente:
- Mapa de Embudos (si tiene 3+ embudos)
- Flujo de Derivación (en Sección 9)
- Notificaciones Urgentes 24/7 (solo si aplica)

Ver `02-skills/02-ETAPA2/prometheo-crm-graphics/SKILL.md` para detalles técnicos de cada gráfico.

---

## Bloques de feedback al final de cada sección

Cada sección termina con un bloque amarillo así:

```
💬 FEEDBACK — [Nombre de la sección]

Escriban su feedback / corrección sobre: [sección].

Pueden agregar notas directamente acá. Cuanto más detallado esté el
feedback escrito, más rápido avanzamos.

☐ Aprobado     ☐ Con cambios     ☐ Necesita revisión

Comentarios: __________________________________________________
              __________________________________________________
              __________________________________________________
```

**Razón:** el feedback inline es más rápido y trazable que una llamada o mail aparte.

---

## Notas AUREA internas

Algunas decisiones del diseño requieren explicación corta para que el cliente entienda **por qué** se tomó. Esas explicaciones van como cajas de fondo naranja claro tituladas "NOTA AUREA":

```
NOTA AUREA · [Título corto]
Texto breve (2-4 líneas) explicando la decisión.
```

Ejemplo real (de G&D):

```
NOTA AUREA · sobre vendedor_asignado
No creamos una variable "vendedor_asignado" porque Prometheo ya resuelve
la asignación de leads de forma nativa: por distribución equitativa entre
moderadores, por Smart Tag, o por una variable de routing. Cuál de estos
3 mecanismos usar es una decisión a validar con el cliente en la etapa
de implementación.
```

**Razón:** evita preguntas repetitivas del cliente.

---

## Pendientes del cliente — formato

La sección 10 lista las tareas pendientes que el cliente tiene que cerrar antes del Go-Live. Se divide en 2 niveles:

| Nivel | Cuándo aplica |
|---|---|
| **Críticos** | Sin esto no se puede avanzar al Go-Live |
| **Normales** | Pueden cerrarse en paralelo a la implementación técnica |

Cada item va con checkbox `☐` para que el cliente marque a medida que avanza.

---

## Lo que NO va en el DOCX cliente-facing

Las siguientes cosas son internas de AUREA y nunca van al cliente:

- Detalle de configuración técnica de Prometheo (eso va en la Guía de Implementador)
- Comparativa con otros clientes / referencias a casos AUREA
- Críticas al Discovery o señalamientos de inconsistencias
- Decisiones internas tomadas sin consultarle
- Patrones del rubro destilados (eso va al manual de AUREA, no al cliente)

---

## Errores frecuentes a evitar

| Error | Cómo evitarlo |
|---|---|
| Llenar todas las tablas de Reglas de Distribución antes de presentarle al cliente | Dejar columnas "Responsable" y "Canal" en blanco para que él complete |
| Usar sintaxis técnica como protagonista (proceso_actual=venta) | Frase comprensible primero, código entre paréntesis después |
| Olvidar la columna "Por qué lo medimos" en KPIs | Es columna obligatoria, no opcional |
| Usar emojis decorativos en texto general | Solo emojis con función pedagógica |
| Saltarse los bloques de feedback inline | Cada sección debe terminar con bloque amarillo |
| Generar el DOCX sin los 8 gráficos | Los gráficos son contenido principal, no decorativo |

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Operativa Etapa 2 | `01-operativa-y-decisiones.md` |
| Reglas Diseño de Prometheo by AUREA | `03-reglas-diseno-prometheo-by-aurea.md` |
| Estructura del Prompt | `05-estructura-prompt-agente.md` |
| Paleta y colores | `../06-convenciones-aurea/01-paleta-y-colores.md` |
| Metodología gráficos | `../06-convenciones-aurea/02-metodologia-graficos.md` |
| Skill de gráficos | `../../02-skills/02-ETAPA2/prometheo-crm-graphics/SKILL.md` |
