# TKVA — Caso de referencia · Material cliente-facing de Etapa 1

Outputs reales del **Paso 1 de Etapa 1** (Pre-Discovery) del cliente TKVA, un
desarrollista inmobiliario. Son los 2 documentos que el cliente recibe **antes de la
primera reunión de Discovery**.

## Qué hay en esta carpeta

| Archivo | Qué es | Formato real |
|---|---|---|
| `AUREA Hub - Bienvenida TKVA.pdf` | Doc de Bienvenida // Kickoff | PDF (se generó como DOCX y se exportó a PDF para enviar) |
| `Guia-Metodologica-TKVA.md` | Guía Metodológica | El original es un Google Doc; este `.md` conserva el texto |

## Para qué sirve

Es el **caso de referencia de la skill `prometheo-docs-kickoff`**. Cuando esa skill genera
el material pre-discovery de un cliente nuevo, usa estos dos documentos como patrón de
tono, nivel de detalle y estructura.

- El Doc de Bienvenida es referencia del módulo `doc-bienvenida.md`.
- La Guía Metodológica es referencia del módulo `guia-metodologica.md`.

## Notas del caso

- **Rubro:** desarrollista inmobiliario — mismo rubro que G&D Developers y EDFAN RE.
- **Consultor asignado:** Rodrigo Buono (la Sección 5 del Doc de Bienvenida lo presenta).
- La Guía Metodológica de TKVA **no enlaza** los 3 documentos del Discovery, porque cuando
  se envió todavía no existían. Es el caso válido "los docs no existen aún" — ver la regla
  de links condicionales en el módulo `guia-metodologica.md` de la skill.

## Diferencia con las otras carpetas de casos

Esta carpeta es de **documentos cliente-facing de Etapa 1 (Paso 1)**. Las otras carpetas de
`08-casos-referencia/` son de otros momentos: `G-D-Developers-real-estate/` y
`BETROX-mobiliario/` son del Discovery (Paso 2), `MIA-App-marketplace/` es de Etapa 2.
TKVA no entra en la tabla de referentes de diseño del `00-INDEX-referentes.md` porque esa
tabla es de patrones de diseño de CRM (variables, tags, embudos), no de documentos.
