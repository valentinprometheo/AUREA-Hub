# Auditoría del ecosistema de skills AUREA · 23/10/2026

Alcance: las 21 skills propias de AUREA (aurea-*, prometheo-*, ic-*, documentos-client-facing),
con aurea-metodologia v1.30 como fuente de verdad del método. Método: comparación de archivos
(hash y similitud de texto), búsqueda de nombres de skills citados que no existen, de cifras de
costos y de términos derogados, más el auditor propio de la metodología (`scripts/auditar.py`).

## Resultado en una línea

La metodología está sana (auditor en verde). El riesgo está **alrededor**: skills sueltas que son
copias viejas de lo que la metodología ya actualizó, nombres de skills que cambiaron y no se
propagaron, y cifras de costos derogadas que siguen vivas en las skills de estética.

## Hallazgos, por prioridad

### P1 · Copias desactualizadas que se disparan solas

Cada una de estas skills existe dos veces: suelta (se activa por su descripción) y como copia
dentro de `aurea-metodologia/references/02-skills/`. Cuando divergen, la suelta gana el disparo
y trae la versión vieja.

| Skill suelta | Similitud con la copia de la metodología | Qué quedó viejo en la suelta |
|---|---|---|
| prometheo-discovery-transversal | 91% | **Numeración de bloques vieja:** B0 Equipo, B1 Objetivo. La vigente es B0 Objetivo y dolor, B1 Equipo y herramientas, y suma B12 (y B13/B2B). R2 no incluye B12 |
| prometheo-auditoria-web | 84% | Se llama "Paso 0 / Etapa 0". La vigente es **Paso 1.1 de la Etapa 1 (Pre-Discovery)** y dispara `prometheo-docs-kickoff` |
| prometheo-audit-doc1 | 99% | Diferencias menores |
| aurea-hub-criterio-calificacion-leads | 3 archivos distintos | `malas-practicas.md` (3,2 KB vs 5,0 KB) y `mi-prometheo-acciones-masivas.md` (3,7 KB vs 4,8 KB) están más completos en la metodología; `real-estate.md`, `inmobiliaria.md` y la plantilla también difieren |

Idénticas (sin riesgo hoy, pero se van a desincronizar en la próxima versión):
prometheo-vertical-real-estate, prometheo-vertical-mobiliario, prometheo-formulario-real-estate,
prometheo-formulario-mobiliario, prometheo-drive-audit-real-estate.

Contradicción interna de la metodología: la tabla de despacho del `SKILL.md` todavía dice
"Etapa 0 — auditoría web", mientras su propia copia de la skill dice "Paso 1.1 de la Etapa 1".

### P1 · Nombres de skills que no existen (referencias rotas)

| Se cita como | Se llama hoy | Lo citan |
|---|---|---|
| `aurea-hub-costos-rentabilidad` | `ic-costos-y-rentabilidad-de-prometheo` | 8 skills (ic-dashboard, ic-conocimiento, curaduría, performance-report, whatsapp, dashboard-design, calificación, corrección de prompts) |
| `aurea-dashboard-design` | `aurea-ic-dashboard-design` | 7 skills, incluido el Paso 7 del conductor `aurea-ic-dashboard` |
| `aurea-curaduria-dato` | `aurea-ic-curaduria-del-dato` | 3 skills |
| `prometheo-correccion-prompts` | `aurea-prometheo-corrección-prompts` | data-action-driven, ic-dashboard |
| `aurea-email-prometheo` / `aurea-whatsapp-prometheo` | `aurea-ic-email-marketing` / `aurea-ic-whatsapp-marketing` | ic-criterio-comercial |

El conductor de tableros (`aurea-ic-dashboard`) es el más afectado: 2 de sus 7 pasos
nombran una skill que no existe.

### P1 · Cifras de costos derogadas que siguen vivas

`ic-costos-y-rentabilidad-de-prometheo` (fuente única de costos) derogó el 13/10/2026:
"Licencia USD 150", "desde USD 149" como piso, y proyectar con USD 0,30 (se proyecta con
USD 0,40; 0,30 es piso). Siguen vigentes en:

- `aurea-estetica-documentacion/references/nuevos-servicios.md`: "desde ~USD 149/150 por canal,
  pendiente de unificar 149 vs 150".
- `estetica-deck.md` y `estetica-deck-system.md` (y sus copias en documentos-client-facing y
  aurea-deck-design): "Plan pendiente de unificar: USD 149 vs 150".
- **El ejemplo de oro `drakon-ventas-marketing.html`**: Licencia USD 150 y tokens USD 0,30 a 0,45.
  Como la regla es clonar ese archivo, cada deck nuevo nace con cifras derogadas si no se corrigen.

### P2 · Tres skills de deck que se disparan con lo mismo

`aurea-estetica-documentacion`, `documentos-client-facing` y `aurea-deck-design` responden a
"propuesta", "deck", "one-pager". Las dos últimas traen solo el kit reducido (`aurea_kit.py`), sin
`aurea-drakon.css` ni el ejemplo DRAKON: es exactamente la causa raíz de "sale plano" que la
propia skill de estética registró el 16/09. Las referencias de estética de documentos-client-facing
son copias al 100% de las de aurea-estetica-documentacion.

### P2 · Barrido de coherencia: 7 chequeos contra 8 (+1)

La metodología define **8 chequeos (+ el 9 cuando aplica)**; el 8 es "compatibilidad con la versión
del proveedor" (reescrituras de Prometheo/ITESA). `aurea-prometheo-corrección-prompts` sigue con
**siete**: cuando el proveedor reescribe un prompt, ese chequeo no corre.

### Sin hallazgos

- Términos derogados del modelo de tags (`proceso_actual`, `estado_venta`, "2 Smart Tags base",
  "Variable router", "4 condiciones"): ninguno vigente fuera de la metodología.
- `aurea-metodologia` v1.30: auditor en verde (la única falla es esperable al comparar la versión
  contra sí misma).

## Propuesta de corrección (sin tocar doctrina)

1. **Una sola copia.** Las skills prometheo-* sueltas pasan a ser punteros finos: descripción para
   el disparo + "seguí `aurea-metodologia/references/02-skills/<skill>/SKILL.reference.md`". Lo
   mismo para el módulo de calificación. Así la metodología es la única fuente.
2. **Renombres propagados** en las 21 skills (tabla de arriba), con línea "Actualización" en cada archivo.
3. **Costos:** reemplazar los "pendiente 149 vs 150" por un puntero a la skill de costos, y
   corregir las cifras del ejemplo DRAKON (marcado como instancia histórica del cliente o actualizado).
4. **Decks:** documentos-client-facing y aurea-deck-design derivan la estética a
   aurea-estetica-documentacion (una familia, una estética, un sistema).
5. **Corrección de prompts:** sumar el chequeo 8 (y el 9) desde metodologia-correccion-agente.md.
6. **Un chequeo de ecosistema** que corra junto a `auditar.py` en cada versión: referencias a skills
   inexistentes, copias divergentes y cifras derogadas. Es este mismo informe, automatizado.

Las skills se sincronizan desde claude.ai: los cambios se suben como un zip por skill, con un solo
SKILL.md cada uno (regla de empaquetado ya registrada).
