# Skill — Generar Guía de Implementador

**Skill operativa para que Claude genere la Guía de Implementador (Ronda 2 de Etapa 2).**

---

## Cuándo activar

Cuando Valentín pide "generar la Guía de Implementador para [cliente]" DESPUÉS de la aprobación del DOCX y Prompt por parte del cliente.

🛑 **No generar antes de la aprobación.** Es punto de control obligatorio.

---

## Inputs requeridos

1. DOCX Diseño de CRM APROBADO por el cliente
2. Prompt V[N] APROBADO por el cliente
3. Doc 3 — Accesos del cliente
4. Datos del cliente: plan Prometheo, fecha Go-Live, equipo responsable

---

## Estructura de la Guía (10 bloques + 1 anexo)

### Bloques obligatorios
1. Información del cliente
2. Setup inicial de la cuenta Prometheo
3. Configuración de variables
4. Configuración de Smart Tags
5. Configuración de embudos / etapas
6. Configuración de seguimientos
7. Configuración de Reglas de Distribución
8. Carga del prompt del agente
9. Testing inhouse (mínimo 15 escenarios)
10. Capacitación al equipo del cliente

### Anexo
- Plan de monitoreo 15 días post Go-Live

---

## Audiencia y tono

| Aspecto | DOCX cliente | Guía Implementador |
|---|---|---|
| Audiencia | Cliente (no técnico) | Consultor AUREA (técnico) |
| Tono | Visual, pedagógico | Operativo, checklists |
| Gráficos | 8 obligatorios | Mínimos |
| Sintaxis Prometheo | Entre paréntesis | Protagonista |
| Formato | .docx | .md |

---

## Reglas inviolables

1. **Orden de creación de variables específico:** primero variable router, luego transversales, luego estados, luego operativas.
2. **Mínimo 15 escenarios de testing.** Si el cliente es complejo (4+ embudos), 25+.
3. **Tabla de Reglas de Distribución COMPLETA con responsables.** A diferencia del DOCX, acá los nombres ya están confirmados.
4. **Capacitación de 90 min mínimo.** No menos.
5. **Plan de monitoreo 15 días obligatorio.**

---

## Validación pre-entrega

| Check | Cómo verificar |
|---|---|
| Info del cliente completa | Bloque 1 |
| Plan Prometheo identificado | Bloque 1 y 2 coinciden |
| Variables con prompt de extracción | Bloque 3 |
| Smart Tags con disparador rubro-específico | Bloque 4 |
| Embudos con etapas claras | Bloque 5 |
| Follow-ups con 4 condiciones | Bloque 6 |
| Reglas de Distribución COMPLETAS | Bloque 7 |
| Path exacto del Prompt | Bloque 8 |
| Mínimo 15 escenarios de testing | Bloque 9 |
| Agenda de capacitación con horarios | Bloque 10 |
| Plan de monitoreo 15 días | Anexo |

---

## Errores frecuentes

- Generar la Guía antes de aprobación de DOCX+Prompt
- Dejar Reglas de Distribución incompletas (en DOCX van vacías, en Guía van completas)
- Menos de 15 escenarios de testing
- Capacitación de menos de 90 min
- Olvidar el plan de monitoreo
