# 00-TRANSVERSAL — Skills que aplican a más de una etapa

Skills que **no pertenecen a una sola etapa** porque se usan en varias. Viven acá una sola
vez — no se duplican dentro de las carpetas de etapa.

| Skill | Qué es | Dónde se usa |
|---|---|---|
| `project-instructions-universal.md` | Instrucciones base de todo proyecto AUREA × Prometheo en Claude | Se carga al inicio de cualquier proyecto, antes de toda skill de etapa |
| `prometheo-vertical-real-estate/` | Slots verticales del rubro desarrollista inmobiliario | Etapa 1 (discovery) y Etapa 2 (diseño). Una sola copia |
| `prometheo-vertical-mobiliario/` | Slots verticales del rubro mobiliario | Etapa 1 (discovery) y Etapa 2 (diseño). Una sola copia |

**Por qué las verticales están acá y no en Etapa 1:** una skill vertical aporta la lógica
del rubro tanto al Discovery (Etapa 1) como al diseño del agente (Etapa 2). Ponerla en una
sola etapa sería inexacto, y duplicarla rompería la regla de fuente única. Por eso vive en
TRANSVERSAL: una copia, usada desde las dos etapas.
