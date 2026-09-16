# Protocolo de Entrega al Cliente — 2 Rondas

> **Paso:** 4 (Entrega Etapa 2 visible)
> **Modalidad:** 2 rondas con iteración esperada
> **Pre-requisito:** Paso 3 completado (reglas de diseño Prometheo diseñado)

---

## Filosofía

La entrega al cliente NO es un evento único. Es un **proceso iterativo en 2 rondas** porque:

1. El cliente nunca tiene clara su propia visión hasta que la ve materializada
2. Ver el prompt funcionando dispara ajustes que no surgen leyendo un documento
3. La Guía Implementador depende del DOCX + Prompt aprobados — entregarla antes desperdicia trabajo

**Regla:** la iteración no es un fallo del proceso, es el proceso.

---

## Ronda 1 — DOCX cliente + Prompt V1

### Qué se entrega

| Entregable | Formato | Función |
|---|---|---|
| **DOCX cliente** | Word con 8 gráficos visuales | Que el cliente entienda el diseño SIN jerga técnica |
| **Prompt V1** | Markdown (.md) | Versión técnica del agente — se carga en Prometheo para demo |
| **Demo aplicada** | Conversación de WhatsApp simulada o real | Que el cliente vea al agente funcionando con datos reales |

### Cómo se ejecuta

1. **Generación local** — Se generan DOCX, Prompt y se prepara la demo
2. **Mail de entrega** — Se mandan los 3 entregables con un mensaje claro:

```
Equipo de [CLIENTE],
Adjuntamos los 2 documentos centrales del diseño:

1. [CLIENTE] - Diseño de CRM v1.docx
   Este documento es la visión cliente-facing del diseño:
   embudos, ficha del lead, momentos clave del agente,
   reglas de derivación. No tiene jerga técnica — está
   pensado para que ustedes puedan revisarlo con el equipo
   comercial completo.

2. [CLIENTE] - Prompt V1.md
   Este es el documento técnico del agente. Es lo que
   "habla" al cliente final cuando escribe. Lo van a ver
   funcionando en la demo.

3. Próximos pasos:
   - Pasamos una primera demo el [fecha sugerida]
   - Después ustedes lo revisan con calma
   - Nos juntamos en una reunión a marcar los ajustes
   - Iteramos hasta que esté redondo
```

3. **Demo del Prompt V1** — Reunión donde se muestra el agente respondiendo a casos reales
4. **Reunión de feedback** — Cliente marca ajustes (idealmente en el DOCX directamente con comentarios)

### Iteraciones esperadas

**Rango normal:** 2-4 iteraciones del Prompt V1 → V2 → V3 → versión final

Cada iteración:
- Cambios solicitados por el cliente se aplican al Prompt
- Se actualiza el DOCX si el cambio impacta las Reglas Diseño de Prometheo by AUREA
- Se vuelve a hacer demo si los cambios son significativos

### Criterio de aprobación de Ronda 1

El cliente confirma por escrito (mail o mensaje) que:
- El DOCX refleja el diseño que quieren
- El Prompt funciona como esperan en los casos típicos
- Están listos para arrancar la implementación

**Solo entonces se libera Ronda 2.**

---

## Ronda 2 — Guía Implementador

### Qué se entrega

| Entregable | Formato | Función |
|---|---|---|
| **Guía Implementador** | Markdown (.md) | Documento técnico para quien va a configurar Prometheo |

### Cómo se ejecuta

1. **Generación** — Se genera la Guía a partir del DOCX y Prompt aprobados
2. **Entrega al implementador** — Se envía al responsable de configurar Prometheo
3. **Sesión de transferencia** — Reunión técnica donde el consultor AUREA acompaña al implementador
4. **Validación técnica** — El implementador confirma que la Guía es suficiente para arrancar la implementación

### Iteraciones esperadas

**Rango normal:** 1-2 iteraciones. La Guía es más técnica y menos opinable.

Iteración típica:
- Implementador pregunta sobre un caso límite no cubierto
- AUREA actualiza la Guía con el detalle faltante
- Implementador confirma

### Criterio de aprobación de Ronda 2

El implementador confirma que puede empezar a cargar Prometheo siguiendo la Guía sin necesidad de consultas frecuentes.

**Solo entonces se arranca el Etapa 3 (Lanzamiento).**

---

## Tabla de progreso típica

| Hito | Día | Estado |
|---|---|---|
| Paso 3 completado | T0 | ✅ Reglas Diseño Prometheo cerradas internamente |
| Ronda 1 — DOCX + Prompt V1 entregados | T0 + 2 | 📤 Cliente recibe entregables |
| Demo Prompt V1 | T0 + 5 | 🎬 Demo en vivo |
| Reunión feedback | T0 + 7 | 💬 Cliente marca ajustes |
| Prompt V2 | T0 + 10 | 🔄 Iteración 1 |
| Reunión validación V2 | T0 + 12 | 💬 Más ajustes o aprobación |
| Prompt V3 / final | T0 + 15 | ✅ Aprobado |
| Ronda 2 — Guía Implementador | T0 + 17 | 📤 Entrega al implementador |
| Sesión de transferencia | T0 + 19 | 🛠️ Implementador entiende todo |
| Arranque Paso 5 | T0 + 21 | 🚀 Empieza carga en Prometheo |

**Total Paso 4 típico:** ~3 semanas para clientes de escala media

---

## Errores comunes a evitar

| Error | Consecuencia | Solución |
|---|---|---|
| Entregar Guía Implementador con Ronda 1 | Se reescribe la Guía cuando cambia el Prompt → trabajo perdido | Esperar a Ronda 2 |
| No hacer demo antes de pedir feedback | Cliente no entiende cómo "suena" el agente, da feedback desfocado | Demo obligatoria antes de cualquier feedback de fondo |
| Aceptar feedback sin filtro | Prompt se diluye intentando complacer a todos | Filtrar feedback con criterio AUREA + criterios v7 |
| No congelar el DOCX cuando se aprueba | Sigue cambiando, la Guía nunca queda sincronizada | Marcar DOCX como "v1.0 validado" cuando se aprueba |

---

## Conexión con otros documentos

- **Templates de Ronda 1:** `/02-skills/05-templates/docx-diseno-crm-template.md` + `/02-skills/05-templates/prompt-template.md`
- **Template de Ronda 2:** `/02-skills/05-templates/guia-implementador-template.md`
- **Convenciones DOCX:** `/01-metodologia/02-ETAPA2-Diseno/04-convenciones-docx-cliente.md`
- **Estructura del prompt:** `/01-metodologia/02-ETAPA2-Diseno/05-estructura-prompt-agente.md`
- **Estructura de la Guía:** `/01-metodologia/02-ETAPA2-Diseno/06-estructura-guia-implementador.md`
- **Protocolo de iteración del Prompt:** `protocolo-iteracion-prompt.md` (en esta misma carpeta)
