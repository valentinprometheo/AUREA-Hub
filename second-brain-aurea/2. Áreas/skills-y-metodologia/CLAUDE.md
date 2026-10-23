# Skills y metodología

Área permanente: el estado del sistema de skills de AUREA en claude.ai.

## Versiones
| Skill | Instalada | Lista para subir | Notas |
|---|---|---|---|
| `aurea-metodologia` | v1.30 (23/10) | v1.31 en `skills-corregidas/2026-10-23/` | auditor 0 fallas · 0 alertas contra v1.30 |
| 18 skills más | 23/10 | `skills-corregidas/2026-10-23/` | renombres, costos vigentes, ruteo de decks, chequeo 8 |
| `aurea-hub-criterio-calificacion-leads` | v1.1 | v1.2 (redirección) | desinstalar cuando esté la v1.31 |

Auditoría completa: `auditorias/2026-10-23-ecosistema-skills.md` (repo AUREA-Hub).

## Reglas del ecosistema
- **Un tema, un dueño.** La metodología es la fuente de las skills `prometheo-*`; las sueltas se
  reinstalan desde `references/02-skills/` en cada versión, nunca se editan aparte.
- **Una skill por zip**, un solo `SKILL.md`, descripción de 1024 caracteres como máximo.
- **Antes de subir una versión:** `auditar.py` de la metodología contra la anterior y
  `herramientas/auditar_ecosistema.py` sobre todas las skills. Con fallas, no se sube.
- Las skills guardan doctrina; los clientes y su estado viven en este brain.

## Pendientes para la v1.32
- [ ] Tres nombres viejos dentro de las copias internas de la metodología: `aurea-crm-graphics`
  (= `prometheo-crm-graphics`), `aurea-diseno-etapa2` (= `prometheo-etapa2-design`) y
  `prometheo-etapa2-prompt` (¿`prometheo-etapa2-design` o `05-estructura-prompt-agente.md`? a confirmar).
- [ ] Nombres de variables: formato natural o snake_case (decisión de Valen, pendiente desde v1.29).
- [ ] Si se aprueba el modelo de paquetes, actualizar precios en `aurea-ic-conocimiento` y
  `aurea-estetica-documentacion`.
- [ ] Repo gbrain: ver qué mejoras trae (pendiente, cuando Valen lo pida).
