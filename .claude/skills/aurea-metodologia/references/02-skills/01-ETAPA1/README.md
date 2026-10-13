# 01-ETAPA1 — Skills de la Etapa 1 (Discovery)

Skills que operan la Etapa 1: desde la auditoría previa hasta el cierre del Discovery.

| Skill | Rol en la Etapa 1 |
|---|---|
| `prometheo-etapa1/` | Orquestadora — punto de entrada, coordina todas las demás |
| `prometheo-auditoria-web/` | Paso 1.1 — auditoría web + IG, genera el Doc 0 |
| `prometheo-docs-kickoff/` | Pasos 1.2-1.3 — Doc de Bienvenida + Guía Metodológica (cliente-facing) |
| `prometheo-formulario-real-estate/` | Paso 2.1 — formulario de reunión, rubro desarrollista |
| `prometheo-formulario-mobiliario/` | Paso 2.1 — formulario de reunión, rubro mobiliario |
| `prometheo-discovery-transversal/` | Paso 2.3 — genera los 4 documentos del Discovery |
| `prometheo-audit-doc1/` | Paso 2.4 — **auditor de calidad de Etapa 1**: verifica que el Doc 1 esté completo |

**Se complementan con:** las skills verticales de `00-TRANSVERSAL/` (aportan la lógica del
rubro al Discovery).

**Auditor de la etapa:** `prometheo-audit-doc1` cumple ese rol — controla la calidad del
output de Discovery antes de pasar a Etapa 2.
