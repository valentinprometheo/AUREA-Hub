# Roadmap — Metodología AUREA Hub × Prometheo

> Estado de la metodología y qué falta construir. Se actualiza junto con el `CHANGELOG.md`.
> **Última actualización:** 11 junio 2026 — ZIP v1.12.

---

## Cómo leer este roadmap

Cada ítem tiene un **estado** y una **prioridad**.

Estados: ✅ hecho · 🟡 parcial · ⬜ pendiente.
Prioridad: 🔴 alta (destraba trabajo facturable o algo bloqueado) · 🟠 media · ⚪ baja.

---

## Estado por Etapa

### Etapa 1 — Discovery — ✅ completa

| Componente | Estado |
|---|---|
| Metodología (auditoría web, pre-discovery, los 4 docs, validación de la Biblia) | ✅ |
| Skill orquestadora `prometheo-etapa1` | ✅ |
| Skills operativas (auditoria-web, docs-kickoff, discovery-transversal) | ✅ |
| Auditor de etapa (`prometheo-audit-doc1`) | ✅ |
| Verticales con skill + formulario: real estate, mobiliario | ✅ |

La Etapa 1 está operativa de punta a punta para los rubros real estate y mobiliario.

### Etapa 2 — Diseño del Agente — 🟡 parcial

| Componente | Estado |
|---|---|
| Metodología transversal (reglas de diseño, convenciones, restricciones, framework seguimientos, modelo embudos/tags, integraciones por rubro) | ✅ |
| Paso 2 — Diseño del Agente IA (protocolos de entrega, iteración, feedback de demo) | ✅ |
| Skill orquestadora `prometheo-etapa2-design` | ✅ |
| Skills operativas (crm-graphics, drive-audit-real-estate, diseno-agente-ia-feedback) | ✅ |
| Aprobación del camino B — propuestas de `reglas-revisadas-v1.11.md` (Reglas 1, 3, 6, 8/9/10) | 🟡 |
| Paso 1 — Diseño del CRM (protocolo escrito) | ⬜ |
| Paso 3 — Implementación del CRM (protocolo escrito) | ⬜ |
| Auditor de etapa | ⬜ |

### Etapa 3 — Lanzamiento — 🟡 parcial

| Componente | Estado |
|---|---|
| Metodología (protocolo de implementación, protocolo de Go-Live) | ✅ |
| Skills que operen la etapa | ⬜ |
| Auditor de etapa | ⬜ |

### Etapa 4 — Mejora Continua — 🟡 parcial

| Componente | Estado |
|---|---|
| Metodología (protocolo de monitoreo) | ✅ |
| Skills que operen la etapa | ⬜ |
| Auditor de etapa | ⬜ |

---

## Pendientes — ordenados por prioridad

### 🔴 Alta — destraba trabajo facturable o algo bloqueado

| # | Pendiente | Por qué es alta |
|---|---|---|
| 1 | **Vertical insumos-construcción** (skill vertical + formulario) | Clientes reales esperando: EDFAN Productos, ZATOH. Sin la skill, su discovery se hace a mano |
| 2 | **Vertical inmobiliaria-tradicional** (skill vertical + formulario) | Cliente de referencia: Paganini. Rubro con lógica propia (stock externo) no cubierta |
| 3 | **Punteros rotos detectados en la auditoría v1.7** | `references/plantilla.md` (lo referencian las 2 skills de formulario y no existe) y `documento-cero-template.md` (referenciado por la auditoría web). Romper un puntero deja una skill sin su input |

### 🟠 Media — completan la metodología

| # | Pendiente | Detalle |
|---|---|---|
| 4 | **Documentar Etapa 2 — Paso 1 (Diseño del CRM)** | Hoy solo el Paso 2 tiene protocolos. Falta el protocolo del Paso 1 |
| 5 | **Documentar Etapa 2 — Paso 3 (Implementación del CRM)** | Falta el protocolo del Paso 3 |
| 6 | **Auditores por etapa** (Etapa 2, 3, 4) | Skills de control de calidad, una por etapa. `audit-doc1` es el modelo. A diseñar con Valentín |
| 7 | **Skills de Etapa 3 y Etapa 4** | La metodología está escrita pero no hay skills que la operen |
| 8 | **Manual del Implementador / Capacitador** | Para onboardear gente nueva. Conviene hacerlo después de cerrar las 4 verticales, porque las referencia |

### ⚪ Baja — mejoras y consolidación

| # | Pendiente | Detalle |
|---|---|---|
| 9 | **Decisión de naming "modelo v7"** | Quedan menciones a "modelo v7" / "modelo conceptual v7" en archivos de metodología activa (operativa, protocolos de iteración/entrega, naming-convention, crm-graphics). Decidir si se renombran a "Reglas Diseño de Prometheo by AUREA" o se mantiene "v7" como nombre corto. Es criterio editorial |
| 10 | **Protocolo de UX de copiloto** | La "experiencia de ida y vuelta" — cómo las skills conversan con el implementador |
| 11 | **Reordenar descripciones del README** | Hecho en v1.7. Si se agregan skills, mantener el orden por etapa |
| 12 | **PDF metódico explicativo** | Material de presentación de la metodología |

---

## Dependencias entre pendientes

Algunas cosas tienen que hacerse en orden:

- **Manual del Implementador (#8)** conviene después de las **verticales (#1, #2)** — el manual las referencia.
- **Auditores por etapa (#6)** conviene después de **documentar los pasos faltantes de Etapa 2 (#4, #5)** — un auditor audita contra una metodología escrita.
- **Skills de Etapa 3 y 4 (#7)** dependen de que su metodología esté estable (ya lo está).

---

## Sugerencia de orden de trabajo

1. Verticales insumos-construcción e inmobiliaria-tradicional (#1, #2) — desbloquean clientes.
2. Resolver los punteros rotos (#3) — es rápido y evita que una skill falle.
3. Documentar Etapa 2 Pasos 1 y 3 (#4, #5).
4. Auditores por etapa (#6).
5. Skills de Etapa 3 y 4 (#7).
6. Manual del Implementador (#8).
7. El resto (#9-#12) — se intercala cuando hay margen.
