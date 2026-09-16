# Auditoría de armado · qué entró y de dónde

Registro de trazabilidad del armado de esta skill: qué fuente aportó qué, qué se incluyó, qué se dejó afuera a propósito. Sirve para verificar que **entró todo** el material y para saber dónde vive cada cosa.

## Fuentes procesadas

| Fuente | Qué era | Qué aportó a esta skill |
|---|---|---|
| **SKILL - Template - Presentación Estética** (`aurea-deck-design`) | skill de estética del deck | Estética Familia A: reglas de render, voz, color, recetas de componentes. Consolidada en `estetica-deck.md` + `estetica-deck-system.md` |
| **Skill - Template - Documentación Formal** (tipo NDA) | skill de docx legal | Familia B completa: regla de no reconstruir, tokens, anatomía, QA. En `documentacion-formal.md` (+ `-tokens.md`, `-qa.md`) + template en `assets/nda/` |
| **Metodología-Outputs-AUREA-Hub** (`documentos-client-facing`) | skill conductora de 6 familias | El patrón conductor (clasificar → dependencias → pedir inputs → generar → presentar), las referencias más evolucionadas de estética (04/04b) y el kit del deck (`aurea_kit.py`, logo, esfera) |
| **AUREA-DRAKON-Ventas-y-Marketing.html** | deck oficial multi-sección real | Género "deck oficial" (`genero-deck-oficial.md`) y el catálogo de nuevos servicios (`nuevos-servicios.md`): modelo hub, Marketing 360, Inteligencia Comercial |
| **Aurea_Hub - Presupuesto para PAVIR.pdf** | presupuesto real (deck a PDF) | Género "presupuesto" (`genero-presupuesto.md`): estructura 01/02/03, nota de encuadre, cómo presentar los números |

## Lo que pediste, y dónde quedó

1. **"Auditá tu proceso para incluir todo"** → este archivo + el log semilla en `references/aprendizajes.md`. Se procesaron las 5 fuentes; ninguna quedó sin volcar.
2. **"Un sector de mejora continua / metodología para aprender mientras funciona y ofrecer mejoras"** → `references/mejora-continua.md` (el protocolo de 5 pasos) + `references/aprendizajes.md` (la memoria versionada). Enganchado en el flujo del `SKILL.md` como Paso 1 (leer) y Paso 7 (capturar).
3. **"Sumar más documentos clave: deck oficial, presupuestos, nuevos servicios"** →
   - Deck oficial: `references/genero-deck-oficial.md`
   - Presupuestos: `references/genero-presupuesto.md`
   - Nuevos servicios: `references/nuevos-servicios.md`

## Decisiones de alcance (qué NO entró, a propósito)

- **Familias 1, 2, 3 y 6 de la skill conductora** (Diseño de CRM, Carga de Contactos, Guión de Testing, Feedback de Demo) **no entran acá.** Esta skill es la capa de **estética + documentación** (deck y legal). Esas familias son metodología de Etapa 2/3 y viven en su propia skill. Si querés fusionarlas, se agregan como módulos sin tocar lo existente.
- **El template NDA** se incluyó como binario (`assets/nda/`), no se editó: es la fuente de verdad congelada.
- El presupuesto PAVIR es un PDF de una sola imagen (deck renderizado); se leyó su estructura, no se copió el binario (no es un asset reutilizable, es un ejemplo del género).

## Estructura final

```
aurea-estetica-documentacion/
├── SKILL.md                              conductor (2 familias + mejora continua)
├── AUDITORIA.md                          este archivo
├── assets/
│   ├── deck/  (aurea_kit.py, logo.txt, sphere.txt)   motor del deck
│   └── nda/   (NDA-AUREA-template-base.docx)          template legal oficial
└── references/
    ├── estetica-deck.md                  reglas y recetas de la estética
    ├── estetica-deck-system.md           tokens, componentes, assets
    ├── genero-propuesta-comercial.md     género propuesta (MAMUT)
    ├── genero-presupuesto.md             género presupuesto (PAVIR)   [nuevo]
    ├── genero-deck-oficial.md            género deck oficial (DRAKON)  [nuevo]
    ├── nuevos-servicios.md               oferta AUREA y cómo nombrarla [nuevo]
    ├── documentacion-formal.md           NDA / legal
    ├── documentacion-formal-tokens.md    tokens del template
    ├── documentacion-formal-qa.md        checklist QA legal
    ├── mejora-continua.md                cómo aprende la skill         [nuevo]
    └── aprendizajes.md                   log versionado de aprendizajes[nuevo]
```
