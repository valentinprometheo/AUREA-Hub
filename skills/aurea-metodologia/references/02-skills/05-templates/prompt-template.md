# Skill — Generar Prompt del Agente

**Skill operativa para que Claude genere el Prompt V1 (o iteraciones V2/V3) del agente IA.**

---

## Cuándo activar

Cuando Valentín pide "generar el Prompt V[N] para [cliente]" durante Etapa 2.

---

## Inputs requeridos

1. DOCX de Diseño de CRM aprobado (o en desarrollo paralelo en Ronda 1)
2. Los 4 docs del Discovery
3. Skill maestra y vertical del rubro
4. Caso de referencia (si aplica)

---

## Estructura del Prompt (14 secciones + 3 anexos)

### Secciones obligatorias
1. Identidad del agente
2. Tono, voz y estilo de comunicación
3. Roles y prioridades
4. Identificación del tipo de usuario
5. Catálogo de productos / servicios (modalidad A/B/C)
6. Materiales y links
7. Conversión (cómo se cierra la consulta)
8. Variables (lista completa con prompt de extracción)
9. Smart Tags (2 base + justificadas si hay más)
10. Derivación (regla maestra + tipos)
11. Objeciones y respuestas
12. Casos límite
13. Seguimientos (fórmula + textos literales / prompts contextuales)
14. Horarios de operación

### Anexos opcionales
- Anexo A — Glosario rubro-específico
- Anexo B — Palabras prohibidas / limitadas
- Anexo C — Checklist de validación pre Go-Live

---

## Diferencias clave con el DOCX

| Aspecto | DOCX cliente-facing | Prompt |
|---|---|---|
| Audiencia | Cliente | Sistema (Prometheo) |
| Tono | Pedagógico, visual | Operativo, directo |
| Sintaxis técnica | Entre paréntesis | Protagonista |
| Emoji | (emoji de saludo) | Emoji real elegido |
| Gráficos | 8 obligatorios | Ninguno |
| Bloques feedback | Sí | No |
| Formato | .docx | .md |

---

## Formato técnico

- **Markdown plano** (.md)
- Headers `##` para cada sección
- Tablas markdown para variables, smart tags, etc.
- Versionado: `[Cliente] - Prompt - V[N].md`

---

## Reglas inviolables

1. **NO hardcodear lo que vive en Tokko/PrestaShop.** Solo estructura macro.
2. **2 Smart Tags base.** Si hay más, justificar y validar con bot Prometheo.
3. **Variable router obligatoria** si hay 2+ embudos.
4. **Cada follow-up con 4 condiciones explícitas** (tag + variable router + variable estado + tiempo).
5. **Glosario obligatorio** si el rubro tiene terminología técnica.
6. **Checklist pre Go-Live obligatorio** en Anexo C.

---

## Validación pre-entrega

| Check | Cómo verificar |
|---|---|
| 14 secciones obligatorias | Contar headers ## |
| 2 Smart Tags base mínimo | Sección 9 |
| Variable router proceso_actual (si hay 2+ embudos) | Sección 8 |
| tipo_derivacion con valores rubro | Sección 10 |
| Cada follow-up con 4 condiciones | Sección 13 |
| Horarios confirmados con cliente | Sección 14 |
| No hay catálogo hardcodeado (si modalidad B) | Sección 5 |
| Objeciones del Discovery presentes | Sección 11 |
| Glosario si rubro lo requiere | Anexo A |
| Checklist pre Go-Live presente | Anexo C |

---

## Iteraciones (V2, V3, ...)

Cuando el cliente pide cambios:
1. **Surgical edits, no regeneración total**
2. Identificar la sección específica
3. Mostrar el diff o la sección modificada
4. Incrementar versión: V1 → V2 → V3

---

## Errores frecuentes

- Hardcodear datos de Tokko/PrestaShop
- 5+ Smart Tags sin justificación
- Follow-ups con condiciones incompletas
- Olvidar el glosario rubro-específico
- Olvidar el checklist pre Go-Live
- Versión Prompt sin actualizar al iterar
