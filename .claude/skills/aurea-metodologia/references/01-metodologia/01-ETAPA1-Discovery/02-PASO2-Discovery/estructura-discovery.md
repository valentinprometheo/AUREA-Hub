# Estructura del Discovery — los bloques temáticos

> **FUENTE ÚNICA.** Este archivo es la única definición oficial de los bloques del
> Discovery de la metodología AUREA × Prometheo. Cualquier otro archivo (el template del
> Doc 1, las skills, los protocolos, el README) **referencia este archivo** — no vuelve a
> listar los bloques por su cuenta. Si un bloque cambia, se cambia acá y solo acá.

---

## Por qué este archivo existe

La estructura de bloques estuvo, durante varias versiones, copiada en varios archivos a la
vez (el Doc 1, las skills, el README). Las copias se desincronizaron: unas decían 12
bloques, otras 13, con numeraciones distintas. Eso causó reprocesos reales.

La solución es el principio de fuente única del ZIP: la estructura vive **en un solo
lugar**. Este. Los demás archivos apuntan acá.

---

## Los bloques

El Discovery se organiza en **14 bloques temáticos** (B0-B13) que cubren la totalidad del
negocio comercial del cliente, más bloques condicionales que se activan según el caso.

| # | Bloque | Qué releva | Alimenta en Etapa 2 |
|---|---|---|---|
| **B0** | Objetivo y dolor | Qué quiere lograr el cliente en 60-90 días, dolor principal, expectativa de mejora | Sección objetivo del prompt + encuadre del diseño |
| **B1** | Equipo y herramientas | Quién vende, cómo se reparten los leads, qué herramientas usan, canales de entrada | Reglas de distribución + autonomía |
| **B2** | Cartera macro | Tipología macro del rubro (proyectos / productos / líneas / inmuebles), atributos diferenciadores, regla Tokko/ERP | Sección cartera + variables por ítem |
| **B3** | Calificación | Criterios de buen lead, tipos de comprador, presupuesto, señales de intención | Variables de calificación |
| **B4** | FAQs y objeciones | Preguntas frecuentes top + objeciones recurrentes + cómo se manejan | Sección FAQs + manejo de objeciones |
| **B5** | Flujo y seguimientos | Recorrido del lead de la primera consulta a la venta, objetivo del agente, los 7 puntos de seguimientos | Sección flujo + diseño de seguimientos |
| **B6** | Tono y voz | Voseo/tuteo, formalidad, emojis, nombre del agente, palabras prohibidas | Sección tono del prompt |
| **B7** | Canales | Canales activos, WhatsApp API o QR, plan de Prometheo, pauta | Configuración de canales + plan |
| **B8** | Autonomía | Qué decide el agente solo, qué escala. ⚠️ Precios: el punto más sensible del discovery | Sección autonomía del prompt |
| **B9** | Contenidos | Brochures, fichas, videos. Archivos referenciados con "/" — el agente los envía pero no lee su contenido | Sistema de placeholders de assets |
| **B10** | KPI y baseline | Las 5 métricas core de Prometheo + los KPI propios del rubro, con su baseline actual | Tabla de KPI + medición |
| **B11** | Excepciones | Clientes VIP, referidos, trato preferencial, campañas, promos, situaciones que rompen las reglas | Sección excepciones + variables condicionales |
| **B12** | Derivación a humano | Cuándo deriva, a quién, con qué información se le pasa el lead al humano, qué pasa si el humano no responde | Reglas de distribución + Smart Tag de derivación |
| **B13** | Logística *(condicional)* | Envío, retiro, instalación, zonas de cobertura, plazos, costos, montos mínimos | Variables y sección de logística |

### Bloques condicionales

- **B13 — Logística.** Se activa cuando el rubro tiene la logística como variable clave de
  la venta: mobiliario, insumos para construcción, e-commerce físico. **No se activa** para
  desarrollista inmobiliario (ahí la "logística" es de obra y se releva dentro de B2).
- **B2B.** Bloque condicional sin número en la secuencia. Se activa cuando el cliente vende
  a intermediarios (inmobiliarias, arquitectos, estudios, revendedores). Releva la lógica
  específica del canal B2B del rubro.

> Por qué B12 y B13 no rompen la secuencia: B12 (Derivación) es un bloque **fijo** — se
> releva siempre. B13 (Logística) es **condicional** — por eso va último, para que el
> cliente que no lo necesita simplemente cierre en B12. B2B no lleva número porque su
> activación es transversal, no secuencial.

---

## Notas de diseño de la estructura

- **Derivación es bloque propio (B12).** No es un subpunto de Autonomía. La derivación
  tiene complejidad propia —a quién, cuándo, con qué información, con qué Smart Tag, qué
  pasa si el humano no contesta— y se releva, documenta y diseña como tema en sí mismo.
  B8 Autonomía se queda con "qué decide solo / qué escala / precios"; el "a quién y cómo
  deriva" vive en B12.
- **FAQs y objeciones van juntas (B4).** En una reunión de discovery se relevan en el mismo
  momento — el cliente no separa "lo que preguntan" de "lo que objetan". Mantenerlas en un
  bloque refleja cómo sale la información en la práctica.
- **Flujo y seguimientos van juntos (B5).** El seguimiento es la continuación del flujo
  cuando el lead deja de responder — son el mismo recorrido.

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| `doc1-discovery-biblia-template.md` | El Doc 1 se organiza con estos bloques — apunta acá, no los re-lista. |
| `protocolo-validacion-biblia.md` | La validación del Doc 1 verifica que estos bloques tengan contenido suficiente. |
| `prometheo-discovery-transversal` (skill) | Releva el negocio del cliente bloque por bloque siguiendo esta estructura. |
| Skills verticales y de formulario | Llenan los slots específicos de cada bloque según el rubro. |
| `protocolo-extension-metodologia.md` | Agregar o cambiar un bloque se hace **en este archivo**, y desde acá se propaga. |
