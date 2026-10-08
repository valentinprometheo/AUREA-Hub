# 00-INDEX — Biblioteca de Referentes AUREA Hub

**Tabla maestra de los casos reales que sirven como inspiración para nuevos clientes.**

---

## Cómo se usa esta biblioteca

Cuando arrancás un cliente nuevo:

1. Identificá el rubro del cliente
2. Buscá en esta tabla el referente más cercano (mismo rubro o rubro parecido)
3. Abrí el archivo del referente y leelo antes de empezar el diseño
4. El referente NO se copia: te da el patrón macro, las variables que probablemente vas a necesitar, los embudos típicos. El detalle se adapta al cliente nuevo.

---

## Estado actual de los referentes

| Cliente | Rubro | Estado | Modelo | Patrón principal que aporta |
|---|---|---|---|---|
| **MIA App** | App / Marketplace inmobiliario | 🟡 Prototipo (final ~26 mayo 2026) | v7 puro | Modelo v7 limpio · 5 procesos paralelos · severidad 24/7 · multi-canal |
| **BETROX** | Mobiliario | 🟡 Prototipo (final ~26 mayo 2026) | v7 puro | Showroom como conversión · B2B arquitectos · terminología técnica · ciclo largo |
| **G&D Developers** | Desarrollista inmobiliario | 🟡 Prototipo (final ~26 mayo 2026) | v1 (alineado a v7) | Tipología macro = proyecto · Tokko como catálogo · B2B inmobiliarias · sensibles fiscales |
| **EDFAN Productos** | Insumos construcción | 🟡 Prototipo (final ~26 mayo 2026) | v1 | Categoría + tipo cliente como doble dimensión · PrestaShop · B2B aplicadores |
| **EDFAN Real Estate** | Desarrollista inmobiliario | ❌ Descartado | v1 con 22 tags | Desactualizado al modelo v7, no integrar como referente |

---

## Cómo elegir el referente correcto

### Si el cliente nuevo es desarrollista inmobiliario

→ **Referente principal: G&D Developers**
→ Particularidades a buscar en el cliente nuevo:
- ¿Usa Tokko? (modalidad B)
- ¿Atiende inmobiliarias? (canal B2B)
- ¿Tiene proyectos co-comercializados con otros desarrollistas?
- ¿Tiene temas fiscales sensibles (blanqueo, crédito hipotecario)?

### Si el cliente nuevo es de mobiliario

→ **Referente principal: BETROX**
→ Particularidades a buscar:
- ¿Tiene showroom? (es punto de conversión #1)
- ¿Atiende B2B (arquitectos, decoradores, paisajistas)?
- ¿Tiene terminología técnica diferenciadora?
- ¿Ciclo de decisión es largo (1-3 meses)?

### Si el cliente nuevo es de insumos para construcción

→ **Referente principal: EDFAN Productos**
→ Particularidades a buscar:
- ¿Usa PrestaShop? (modalidad B)
- ¿Atiende aplicadores profesionales? (canal B2B)
- ¿Tipología macro tiene doble dimensión (categoría + tipo cliente)?

### Si el cliente nuevo es app / marketplace / software

→ **Referente principal: MIA App**
→ Particularidades a buscar:
- ¿Tiene 4-5 procesos paralelos?
- ¿Tiene casos de severidad alta (bugs, fraude)?
- ¿Multi-canal de entrada?
- ¿App móvil → variable sistema_operativo necesaria?

### Si el cliente nuevo es inmobiliaria tradicional

→ **Sin referente formal todavía**
→ Construir como caso fundacional. Documentar patrones para crear skill futura.

---

## Cómo se actualiza esta biblioteca

### Cuándo sumar un cliente nuevo como referente

Un cliente se vuelve referente cuando cumple los 3 criterios:

1. **Cierre completo de Etapa 2** (DOCX y Prompt aprobados por el cliente)
2. **Mínimo 15 días en producción** sin regresiones críticas
3. **Patrón identificable** que aporta algo nuevo a la metodología

Si un cliente cumple los 3, seguir `00-protocolo-incorporar-nuevo-referente.md` para destilarlo.

### Cuándo se descarta un referente

Un referente se descarta de la biblioteca si:

- Está desactualizado respecto al modelo de reglas vigente (caso EDFAN RE con 22 tags)
- Hubo problemas críticos en producción que no se resolvieron
- El patrón fue reemplazado por uno más limpio en otro cliente

Cuando se descarta, marcar en la tabla con ❌ y dejar el archivo con nota explicativa para que futuros consultores entiendan por qué no usarlo.

---

## Plantilla mínima para un caso de referencia

Cada archivo en esta carpeta sigue esta estructura:

```markdown
# Caso de referencia — [Cliente]

**Rubro:** [...]
**Fecha del proyecto:** [mes año]
**Estado:** [Activo / Histórico / Descartado]
**Reglas Diseño Prometheo aplicadas:** [versión, ej: vigente / inicial / etc]

---

## Resumen ejecutivo en 5 líneas
[Qué es el cliente, qué hace, por qué fue elegido como referente]

## Variables (con las 3 capas)
### Capa 1 — Núcleo transversal
[...]
### Capa 2 — Por rubro
[...]
### Capa 3 — Específicas del cliente
[...]

## Smart Tags
[Cuántas, cuáles, justificación]

## Embudos
[Cuántos, qué etapas tiene cada uno]

## Patrón principal que aporta
[Qué descubrimos en este cliente que se generalizó a la metodología]

## Decisiones operativas específicas
[Cosas que el cliente decidió que NO son patrón del rubro, son
particularidades suyas]

## Aprendizajes y errores
[Qué salió bien, qué reharíamos]
```

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Protocolo para sumar referente nuevo | `00-protocolo-incorporar-nuevo-referente.md` |
| Caso MIA App | `PROTOTIPO-mia-app.md` |
| Caso BETROX | `PROTOTIPO-betrox.md` |
| Caso G&D Developers | `PROTOTIPO-g-d-developers.md` |
| Caso EDFAN Productos | `PROTOTIPO-edfan-productos.md` |
| Patrones por rubro (general) | `../../05-rubros/` |
