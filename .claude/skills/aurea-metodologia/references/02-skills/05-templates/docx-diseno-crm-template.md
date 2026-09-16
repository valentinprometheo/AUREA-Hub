# Skill — Generar DOCX de Diseño de CRM

**Skill operativa para que Claude genere el DOCX cliente-facing de Etapa 2.**

---

## Cuándo activar

Cuando Valentín pide "generar el DOCX de Diseño de CRM para [cliente]" durante Etapa 2.

---

## Inputs requeridos

1. Los 4 docs del Discovery (Doc 1, 2, 3, 4) — del cliente
2. Skill maestra `prometheo-etapa2-design/`
3. Skill `prometheo-crm-graphics/`
4. Skill vertical del rubro (si existe)
5. Caso de referencia del rubro (si existe)

---

## Estructura del DOCX (11 secciones obligatorias)

1. **Roles del agente** — qué hace, cómo se llama, identidad
2. **Estrategia + KPIs** — con columna "Por qué lo medimos"
3. **Autonomía del agente** — cards con palabras clave en bold
4. **Embudos** — qué procesos paralelos atiende
5. **Variables** — esquema 3 capas + tabla + ejemplo aplicado
6. **Smart Tags** — como cards con flecha →
7. **3 Escenarios de ejemplo** — vertical top-down con iconos
8. **Seguimientos** — fórmula pedagógica + lista
9. **Reglas de Distribución** — con columnas vacías para cliente
10. **Pendientes del equipo del cliente** — críticos vs normales
11. **Próximos pasos** — con placeholder del Drive

---

## Convenciones obligatorias

Aplicar las 10 convenciones AUREA (ver `04-convenciones-docx-cliente.md`):
1. Tabla KPIs con columna "Por qué lo medimos"
2. Reglas de Distribución con columnas vacías para cliente
3. Cards de autonomía con palabras clave en bold
4. Modificaciones antes→ahora con verde+bold
5. Smart Tags como cards con flecha →
6. Cards de Variables con ejemplo "Imaginate que llega Juan..."
7. Fórmula de seguimientos en 4 pasos pedagógicos
8. Sección "3 Escenarios de Ejemplo" obligatoria
9. Mensajes follow-up con (emoji de saludo)
10. "Próximos pasos" con placeholder al Drive

---

## Gráficos obligatorios (8)

1. Overview de Variables (Sección 5)
2. Arquitectura de Variables (Sección 5)
3. Overview de Smart Tags (Sección 6)
4-6. 3 Escenarios de ejemplo (Sección 7)
7. Fórmula de Seguimiento (Sección 8)
8. Distribución de Seguimientos por proceso (Sección 8)

---

## Paleta de colores

Aplicar según `01-paleta-y-colores.md`:
- Verde Venta · Rojo Soporte · Azul FAQ · Morado Seguridad · Teal Postventa · Naranja Smart Tags

---

## Bloques de feedback

Cada sección termina con un bloque amarillo `#FFF9D6` para que el cliente apruebe/comente:

```
💬 FEEDBACK — [Nombre de la sección]
☐ Aprobado     ☐ Con cambios     ☐ Necesita revisión
Comentarios: __________________________________________
```

---

## Formato técnico

- **Generar como `.docx`** (no markdown)
- Usar `python-docx` o equivalente
- Resolución de gráficos: 300 DPI mínimo
- Tipografía: cuerpo 11pt · títulos 14pt · tablas 10pt
- Versionado: `[Cliente] - Diseño de CRM.docx` (sin V en V1)

---

## Reglas inviolables

1. **Cliente nunca ve sintaxis técnica protagónica.** `proceso_actual = venta` va entre paréntesis.
2. **Las Reglas de Distribución se entregan incompletas** para que el cliente las complete.
3. **Los 3 escenarios muestran 3 procesos distintos.**
4. **Cada gráfico responde a 1 pregunta concreta.**

---

## Validación pre-entrega

| Check | Cómo verificar |
|---|---|
| Las 11 secciones obligatorias están | Revisar TOC |
| Las 10 convenciones aplicadas | Checklist convención por convención |
| Los 8 gráficos están | Contar gráficos |
| Bloques de feedback en cada sección | Verificar uno por uno |
| Paleta aplicada según convención | Hex exactos |
| Placeholder al Drive en próximos pasos | Sección 11 |

---

## Errores frecuentes

- Llenar Reglas de Distribución completas (van vacías para cliente)
- Sintaxis técnica como protagonista
- Olvidar columna "Por qué lo medimos" en KPIs
- Emojis decorativos en texto general
- Saltarse los bloques de feedback
