---
consultar-cuando: el cliente pregunta por Inteligencia Comercial, se ofrece o diseña ese producto, se confunde con Mejora Continua
disparadores: "inteligencia comercial", "dashboard", "el puente entre campañas y ventas", "export de Prometheo", "DRAKON", "paneles"
fuente-única-de: qué es Inteligencia Comercial como producto, sobre qué corre, qué requiere
combina-con: logica-comercial-transversal (las 6 variables de IC), embudos-y-tags (dónde se capturan), overview del proyecto
---

# Inteligencia Comercial — el producto

> Producto de AUREA, distinto de la consultoría/implementación y de la Mejora Continua. Este
> archivo dice qué es, sobre qué corre y qué requiere. Los datos que explota se capturan durante
> la implementación (las 6 variables de inteligencia comercial, ver `logica-comercial-transversal.md`
> y `embudos-y-tags.md`); acá se explotan.

---

## Qué es (y qué NO es)

Inteligencia Comercial es un **dashboard** que cruza lo que el agente captura en las
conversaciones con la inversión en pauta, para cerrar el círculo entre marketing y ventas: qué
campaña trae leads que **cotizan** (no solo que consultan), qué objeta la gente, qué demanda no
está cubierta, cómo evoluciona todo mes a mes.

Tres cosas importantes sobre su encuadre:
- **Es un producto independiente.** No es un plan de Mejora Continua ni una etapa de la
  implementación. Funciona solo, sobre cualquier cuenta con Prometheo activo.
- **No es obligatorio ni se implementa por defecto en todas las cuentas.** Es parte de la oferta
  de servicios de AUREA y se contrata aparte. (El posicionamiento comercial y la carta de venta
  están en el deck oficial de AUREA y en la carta de Inteligencia Comercial.)
- **No se confunde con Mejora Continua.** Mejora Continua afina el agente (prompt, CRM);
  Inteligencia Comercial explota los datos que el agente ya captura para decisiones de negocio.
  Se pueden contratar juntas o por separado.

---

## Sobre qué corre — el export de Prometheo

El dashboard se construye sobre el **export de la base de datos de Prometheo** de la cuenta. Ese
export trae, para cada contacto, sus **Smart Tags** y sus **Variables pobladas** (proyecto,
tipología, destino, presupuesto, forma de pago, origen, zona, objeción, etc.), más el campo de
anuncio/origen de contacto. Es la misma estructura para cualquier cuenta en Prometheo, así que el
dashboard se arma igual en todas: cuando la cuenta esté cargada, exporta esa estructura y los
paneles se llenan solos.

Consecuencia de diseño para la implementación: **la calidad del dashboard depende de que las
variables se hayan diseñado y capturado bien.** Las 6 variables de inteligencia comercial
(Objeción Principal + Frase Literal, Pedido Fuera de Catálogo + Detalle, Dolor Principal,
Disparador Compra) son la materia prima de los paneles de señales e insights. Diseñar bien esas
variables en la implementación es lo que hace posible este producto después.

---

## El dashboard — 6 paneles

1. **Panorama.** Las señales del mes con su variación: leads, tasa de calificación, CPL, CPA de
   cotización, cotizaciones, enriquecimiento de perfil, audiencia semilla, ROAS. Foto del mes con
   comparación a 6 meses.
2. **Campañas.** Atribución real por campaña: qué creativo trae a los que **cotizan**, no a los
   que solo consultan. Por campaña: leads, tasa de calificación, visitas, cotizaciones, CPL, y
   una acción sugerida (subir / mantener / optimizar).
3. **Meta (el puente con Meta).** La conexión con la pauta: qué pasa entre el anuncio y la venta.
4. **Audiencias.** Perfiles listos para semilla de Lookalike, a partir de los leads enriquecidos.
5. **Señales / Insights accionables.** Lo que sale de las variables de IC: objeciones rankeadas,
   demanda no cubierta (pedidos fuera de catálogo), dolores y disparadores. Es la lectura
   cualitativa que ninguna herramienta de pauta da.
6. **Tendencia.** La evolución mes a mes de todo lo anterior (snapshots).

---

## Requisitos y viabilidad

- **Requiere WhatsApp API oficial + plan Enterprise** de Prometheo (por las notificaciones, el
  volumen y el export completo).
- **Viabilidad validada por el desarrollista:** el producto está en desarrollo y se comprobó que
  se puede construir completo contra un **export real** de Prometheo (caso TKVA: variables
  pobladas confirmadas, no solo tags). No depende de inventar nada nuevo sobre lo que ya se vende.
- **Caso de referencia: DRAKON** (leads de maquinaria). La maqueta de 6 paneles de la propuesta
  se cruzó contra el export real de otra cuenta andando (TKVA) para confirmar que, cuando DRAKON
  esté cargado, tendrá la misma estructura y el dashboard se arma igual. Los datos de la maqueta
  DRAKON son ilustrativos; la estructura es real.

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| `logica-comercial-transversal.md` | las 6 variables de IC son el patrón dual (Opciones + Texto largo) que alimenta los paneles de señales |
| `embudos-y-tags.md` | dónde y cómo se capturan esas variables en el diseño del CRM |
| `restricciones-plataforma-prometheo.md` | requisitos de plan (Enterprise) y de canal (WhatsApp API) |
| Deck oficial de AUREA / carta de Inteligencia Comercial | el posicionamiento comercial y la venta del producto (material client-facing, no metodología) |

> Nota de alcance: este archivo documenta el producto para que el equipo sepa qué es, sobre qué
> corre y qué requiere. La construcción técnica del dashboard (en BaseA, sobre el export) es
> trabajo del desarrollista; el detalle de implementación técnica no vive en este ZIP.
