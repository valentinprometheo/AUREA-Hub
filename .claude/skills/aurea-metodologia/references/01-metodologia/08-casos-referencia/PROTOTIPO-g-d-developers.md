# PROTOTIPO — G&D Developers

**Estado:** Reservado para versión final
**Fecha estimada de entrega:** ~26 mayo 2026
**Rubro:** Desarrollista inmobiliario
**Reglas Diseño Prometheo aplicadas:** versión inicial (alineada a Reglas vigentes)

---

## Patrón principal que aporta

Referente principal para clientes desarrollistas inmobiliarios. Aporta:
- Tipología macro = **proyecto** (no zona, no unidad — el proyecto es la unidad central del CRM)
- Catálogo en Tokko (modalidad B)
- Canal B2B con inmobiliarias (derivación automática en MVP)
- Temas fiscales sensibles (blanqueo, crédito hipotecario → derivación)
- Programa "Invertí en m²" para inversores
- Variable `objetivo_busqueda` que gobierna preguntas posteriores (inversión vs uso personal)
- 4 embudos: Venta + Derivación B2B + FAQ + Excepciones

---

## Variables (3 capas) — esquema

### Capa 1 — Núcleo transversal
- `proceso_actual` (implícito por embudo en v1)
- `canal_origen`
- `tipo_contacto` (comprador_final / inmobiliaria)
- `objetivo_busqueda` (inversion / uso_personal)
- `tipo_derivacion`

### Capa 2 — Por rubro (Desarrollista inmobiliario)
- `proyecto_interes`
- `zona_interes`
- `tipo_unidad`
- `presupuesto`
- `finalidad` (vivienda / inversion_renta / reventa / diversificacion)
- `forma_de_pago`

### Capa 3 — Específicas de G&D
- Catálogo de 10 proyectos (MOCA2, JULIO3, FEEL_BE, AGUILAR, FEEL_PA, etc.)
- Renta de Feel Palermo USD 300/500 hasta posesión
- Referidos VIP de Dani, Gabi, Nico o Luis

---

## Smart Tags
- `#seguimiento_activo`
- `#derivar_a_humano`

(Modelo v7 limpio — 2 tags base. Es uno de los primeros casos donde aplicamos v7 limpio.)

---

## Embudos
1. Venta (calificando → info_enviada → visita_agendada → visita_realizada → reservado/cerrado)
2. Derivación B2B (inmobiliarias)
3. FAQ y consultas
4. Excepciones (VIP / blanqueo / crédito hipotecario)

---

## Decisiones operativas específicas
- En MVP: agendamiento de visitas NO autónomo (humano cierra agenda)
- En MVP: B2B inmobiliarias se deriva automáticamente, no se atiende con flujo propio
- objetivo_busqueda gobierna preguntas: si inversion, puede preguntar valor m². Si uso_personal, NO se pregunta valor m².
- Co-comercialización con Cesarprop en 9 de Julio Estudios 3
- vendedor_asignado NO se modela como variable — Prometheo lo resuelve nativo

---

## Aprendizajes y errores
- (a completar con la versión final)

---

> 📝 NOTA: Este archivo es un prototipo. La versión final detallada se entrega ~26 mayo 2026.

---

## 📎 Archivos de referencia disponibles

En la subcarpeta `G-D-Developers-real-estate/` están los 3 documentos de Etapa 1 reales de G&D, como **templates de cómo se ven los entregables de Discovery de un desarrollista inmobiliario**:

| Archivo | Qué es | Sirve de referencia para |
|---|---|---|
| `G-D-Developers-Doc1-Sintesis.docx` | Doc 1 — Síntesis de Discovery (cliente-facing) | Cómo se estructura la "biblia" del cliente: ficha, bloques, semáforo, categorías CRM en lenguaje de negocio |
| `G-D-Developers-Doc2-Asincronico.docx` | Doc 2 — Información pendiente | Cómo se piden los datos faltantes sin duplicar lo ya relevado |
| `G-D-Developers-Doc3-Accesos.docx` | Doc 3 — Accesos y documentación | Cómo se piden accesos + estructura del Drive por proyecto |

Son la referencia canónica del rubro real estate para los 3 outputs de Etapa 1.
