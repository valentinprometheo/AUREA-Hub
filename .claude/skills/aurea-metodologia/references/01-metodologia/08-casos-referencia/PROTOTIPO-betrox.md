# PROTOTIPO — BETROX

**Estado:** Reservado para versión final
**Fecha estimada de entrega:** ~26 mayo 2026
**Rubro:** Mobiliario (hormigón liviano)
**Reglas Diseño Prometheo aplicadas:** Reglas Diseño de Prometheo by AUREA (puro)

---

> **Nota v1.21:** prototipo de mayo 2026, escrito con un modelo de tags que después quedó
> derogado. Las secciones de variables y Smart Tags ya están corregidas al modelo vigente.
> Para diseñar una cuenta, usá `02-ETAPA2-Diseno/arquitectura-crm-por-rubro.md` y el
> material real de la cuenta.

## Patrón principal que aporta

Referente principal para clientes de mobiliario. Aporta:
- Showroom como punto de conversión #1 (todo el agente apunta a llevar al lead al showroom)
- Ciclo de decisión largo (1-3 meses)
- B2B estructural con arquitectos, paisajistas y decoradores
- Terminología técnica del rubro (líneas: interior / exterior / baño_cocina / mobiliario_urbano / raw)
- Variable `producto_de_interés` con catálogo de modelos propios (POSITANO, ATENEA, JAPAN, SIT 45)
- Variable `medida_solicitada` libre (texto)
- 5 embudos paralelos (venta + faq + postventa + b2b + outlet)

---

## Variables (3 capas) — esquema

### Capa 1 — Núcleo transversal
- `canal`
- `tipo_usuario` (con valores: consumidor_final / arquitecto / paisajista / decorador / constructora / municipio / cliente_recurrente)
- `tipo_compra` (estándar / configurable / a_medida / proyecto_integral)
- `tipo_derivacion`

### Capa 2 — Por rubro (Mobiliario)
- `linea_producto`
- `ciudad_zona`
- `tipo_feedback`

### Capa 3 — Específicas de BETROX
- `producto_de_interés` (catálogo modelos: POSITANO, ATENEA, etc.)
- `medida_solicitada` (texto libre: "1.60m × 0.80m")
- `severidad_caso` (definida pero "no aplica" para BETROX hoy)

---

## Smart Tags
Una tag por dimensión:
- Estadío: las etapas de cada embudo
- Perfil del contacto: Consumidor Final · Profesional · Cliente Recurrente
- Excepción (opcional): Contacto VIP

(Ninguna variable guarda la etapa ni en qué embudo está el lead.)

---

## Embudos
1. Venta (cotización → showroom → seña → producción → entrega)
2. Postventa (reclamos de service, raro: 1 cada 3 meses)
3. B2B Profesional (arquitectos, paisajistas, decoradores)
(FAQ y Outlet no son embudos. Molde vigente: 4 embudos, ver `arquitectura-crm-por-rubro.md`.)

---

## Decisiones operativas específicas
- Cliente recurrente NO se modela como Smart Tag — se suma valor a `tipo_usuario`
- No hay casos de severidad 24/7 (no hay app con bugs, no hay datos sensibles)
- Sincronización Bejerman → PrestaShop como flujo de precios

---

## Aprendizajes y errores
- (a completar con la versión final)

---

> 📝 NOTA: Este archivo es un prototipo. La versión final detallada se entrega ~26 mayo 2026.

---

## 📎 Archivos de referencia disponibles

En la subcarpeta `BETROX-mobiliario/` está el ciclo completo de Etapa 1 de BETROX, como **templates de cómo se ve el Discovery de un cliente de mobiliario** — desde la captura cruda hasta el documento aprobable:

| Archivo | Qué es | Sirve de referencia para |
|---|---|---|
| `BETROX-Formulario-Completado.html` | El formulario de reunión completado en vivo | Cómo queda el formulario sincrónico después de la R1, con respuestas reales |
| `BETROX-Doc0-Analisis-Interno.html` | Doc 0 — Análisis de Discovery (interno AUREA) | Cómo se destila la reunión en un diagnóstico interno antes del Doc 1 |
| `BETROX-Doc1-Sintesis.html` | Doc 1 — Síntesis de Discovery (cliente-facing) | Cómo se estructura la "biblia" del cliente en el rubro mobiliario |

El formulario completado y el Doc 0 son **complementarios**: uno es la captura cruda de la reunión, el otro el análisis destilado. Juntos muestran cómo se pasa de la conversación al documento.
