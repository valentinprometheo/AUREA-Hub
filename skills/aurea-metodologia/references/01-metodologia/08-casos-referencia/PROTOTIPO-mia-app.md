# PROTOTIPO — MIA App

**Estado:** Reservado para versión final
**Fecha estimada de entrega:** ~26 mayo 2026
**Rubro:** App / Marketplace inmobiliario
**Reglas Diseño Prometheo aplicadas:** Reglas Diseño de Prometheo by AUREA (puro)

---

## Patrón principal que aporta

Caso fundacional del modelo v7. Aporta:
- 5 procesos paralelos (Venta + Soporte + FAQ + Seguridad + Postventa)
- Casos de severidad 24/7 (bug crítico, fraude)
- Multi-canal de entrada (App + Web + WhatsApp + Instagram + Mail)
- Variable `sistema_operativo` (Android/iOS para link de descarga correcto)
- Variables operativas avanzadas (severidad_caso + tipo_derivacion)

---

## Variables (3 capas) — esquema

### Capa 1 — Núcleo transversal
- `proceso_actual` (router)
- `canal`
- `tipo_usuario`
- `intencion_principal`
- `tipo_derivacion`

### Capa 2 — Por rubro (App/Marketplace)
- `sistema_operativo`
- `tipo_feedback`

### Capa 3 — Específicas de MIA
- (a completar con la versión final)

---

## Smart Tags
- `#seguimiento_activo`
- `#derivar_a_humano`

(Modelo v7 limpio — 2 tags base)

---

## Embudos
1. Venta (descarga + registro + publicación)
2. Soporte técnico
3. FAQ general
4. Seguridad / fraude
5. Postventa

---

## Decisiones operativas específicas
- (a completar con la versión final)

---

## Aprendizajes y errores
- (a completar con la versión final)

---

> 📝 NOTA: Este archivo es un prototipo. La versión final detallada se entrega ~26 mayo 2026 con toda la información destilada del cliente. Mientras tanto, este prototipo sirve para que sepas que MIA es referente principal del rubro App/Marketplace y los patrones macro que aporta.

---

## 📎 Archivos de referencia disponibles

En la subcarpeta `MIA-App-marketplace/` están los outputs reales de MIA App como **templates paradigmáticos de Etapa 2**:

| Archivo | Qué es | Para qué sirve de referencia |
|---|---|---|
| `MIA-App-Prompt-V6.md` | Prompt completo del agente MIA en formato V6 (prosa redactada, separadores `===`, sin tablas markdown) | Referencia del **formato V6 del prompt** — cómo se redacta un prompt listo para pegar en Prometheo |
| `MIA-App-Diseno-de-CRM.html` | El DOCX "Diseño de CRM" cliente-facing de MIA exportado a HTML | Referencia **visual** del DOCX — las secciones, los cuadros "Explicado:", el patrón banner→card→gráfico→tabla→ejemplo→feedback |

Estos 2 archivos son la **referencia canónica** que usa la skill `prometheo-etapa2-design` para mostrar el estándar de calidad esperado.
