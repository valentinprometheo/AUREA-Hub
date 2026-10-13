# PROTOTIPO — EDFAN Productos

**Estado:** Reservado para versión final
**Fecha estimada de entrega:** ~26 mayo 2026
**Rubro:** Insumos para construcción
**Reglas Diseño Prometheo aplicadas:** versión inicial

---

> **Nota v1.21:** prototipo de mayo 2026, escrito con un modelo de tags que después quedó
> derogado. Las secciones de variables y Smart Tags ya están corregidas al modelo vigente.
> Para diseñar una cuenta, usá `02-ETAPA2-Diseno/arquitectura-crm-por-rubro.md` y el
> material real de la cuenta.

## Patrón principal que aporta

Caso fundacional del rubro insumos para construcción. Aporta:
- Tipología macro doble dimensión: categoría_producto + tipo_cliente
- Catálogo en PrestaShop (modalidad B)
- Canal B2B con aplicadores profesionales (estructural en el rubro)
- Routing por tipo de cliente, NO por zona
- Diferenciación de tono según tipo_usuario (aplicador → técnico, particular → didáctico)
- Manejo de fichas técnicas como PDFs adjuntos (no como base de conocimiento)

---

## Variables (3 capas) — esquema

### Capa 1 — Núcleo transversal
- `canal`
- `tipo_usuario` (aplicador / particular / arquitecto / constructora)
- `intencion_principal`
- `tipo_derivacion`

### Capa 2 — Por rubro (Insumos construcción)
- `categoria_producto`
- `volumen_estimado_m2`
- `zona_obra` (a validar)

### Capa 3 — Específicas de EDFAN Productos
- (a completar con la versión final)

---

## Smart Tags
Una tag por dimensión:
- Estadío: las etapas de cada embudo
- Perfil del contacto: Particular · Aplicador · Arquitecto · Constructora
- Excepción (opcional): Contacto VIP

(Ninguna variable guarda la etapa ni en qué embudo está el lead.)

---

## Embudos (probables, a validar con cliente)
1. Venta B2C (particulares)
2. Venta B2B (aplicadores y constructoras)
3. Soporte técnico de aplicación
(FAQ general no es embudo: se responde dentro del embudo de venta.)

---

## Decisiones operativas específicas
- Modalidad híbrida: PrestaShop para stock/precios + Drive para fichas técnicas (PDFs)
- Tono adaptado por tipo_usuario detectado
- Desambiguación de terminología (microcemento ≠ cemento alisado ≠ hormigón pulido)

---

## Aprendizajes y errores
- (a completar con la versión final)

---

> 📝 NOTA: Este archivo es un prototipo. La versión final detallada se entrega ~26 mayo 2026. Este cliente todavía está en proceso de cierre de Etapa 2.
