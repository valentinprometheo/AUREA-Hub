# Género · Deck oficial multi-sección

> Género dentro de la **Familia A (deck)**. Es el documento **largo, con índice de navegación**, que integra toda la oferta AUREA en un solo hilo: Ventas (Prometheo) primero, Marketing y medición después.

## Dos variantes del deck oficial

Este género tiene dos usos, misma estética y misma estructura de fondo:

1. **Deck Oficial institucional (AUREA).** El deck maestro de marca: presenta a AUREA Hub, Prometheo y la oferta completa, sin adaptar a un cliente puntual. Es la pieza de referencia canónica del look y la narrativa institucional. Documento fuente: **`Aurea_Hub - Deck Oficial.pdf`** (deck renderizado con esta estética; vive en el Drive de AUREA como la versión vigente). Cuando armes o actualices el deck institucional, partí de ese documento como fuente de verdad de contenido y orden, y respetá su copy validado.
2. **Deck oficial de cliente.** El mismo formato largo con índice, pero adaptado a un prospecto concreto: integra su Ventas + Marketing con sus datos y dolores. Caso de referencia: **DRAKON — Ventas & Marketing**.

> **Referencia de diseño exacta (leerla antes de armar un deck oficial):** el HTML real de DRAKON vive en `assets/ejemplos/drakon-ventas-marketing.html`. No lo aproximes de memoria: abrilo y copiá de ahí la estructura, las tipografías, los gradientes y el armado de secciones e índice. Es la fuente de verdad del look de este género.

La diferencia es el **contenido y el destinatario**, no la estética ni la mecánica de render. Lo que sigue aplica a las dos; donde diga "[CLIENTE]", en el institucional va AUREA/el rubro genérico.

Usa la estética de la Familia A (deck AUREA). Para el render, leé `estetica-deck.md` + `estetica-deck-system.md`. La diferencia con una propuesta o un presupuesto: es **más largo, tiene índice navegable, y presenta la oferta completa como un ecosistema**, no un solo frente.

## Cuándo se hace

Cuando el prospecto necesita ver **toda la oferta integrada** (no un frente suelto): cómo se ordena la venta con Prometheo y cómo, sobre esa base, se activa y se mide el marketing. Es el documento "institucional-comercial" completo, el que muestra el círculo entero.

## El ángulo central (el hilo)

Un solo proceso: **vender mejor y saber qué funciona.** Primero ordenamos la venta con Prometheo; después activamos y medimos la demanda con marketing. Dos frentes, un mismo dato. El documento entero se cuelga de que **el círculo solo cierra si el dato vuelve**: la Inteligencia Comercial le dice a los canales de generación qué anuncio y qué lead valen la pena.

## Estructura (esqueleto; adaptar el contenido al caso)

**Header con índice navegable.** Barra superior con las dos ramas y sus anclas: VENTAS (Diagnóstico · Presupuesto · Plan) y MARKETING (Diagnóstico · Marketing 360 · Inteligencia · Contrato anual). El índice es parte de la estética de este género: se navega como una web.

**Portada / hero.** Marca + cliente. Una línea de estrategia ("Un solo proceso: vender mejor y saber qué funciona"). Bajada que separa los dos frentes y explica que se lee con el índice.

**Diagnóstico general · el círculo comercial.** Quién genera hoy (pauta, base), qué falta (convertir mejor y medir), y dónde entra AUREA (la capa que convierte y mide). El diagrama del ecosistema: Generan → Convertimos → Medimos, y la vuelta del dato. Los puntos a resolver para que el círculo cierre.

**Parte 1 · Ventas.** Ordenar la venta con Prometheo: CRM, agente IA y chat omnicanal. Es la base sobre la que se apoya el marketing. Sub-secciones típicas: Diagnóstico de la operación (canales dispersos, sin trazabilidad), el diseño de la solución, el presupuesto del frente de ventas, el plan.

**Parte 2 · Marketing.** Sobre la base ordenada: Marketing 360 (Email y WhatsApp sobre la base del cliente) e **Inteligencia Comercial** (medir cada canal, costo por comprador real, qué anuncio y qué lead valen). El modelo de contrato anual cuando aplique. Ver `nuevos-servicios.md`.

**Cierre · el círculo que cierra.** El párrafo que resuelve el hilo: el dato que vuelve hace que cada peso de generación rinda más la próxima vez. Cierre de marca.

## Reglas propias de este género

- **El orden es doctrina:** ventas primero, marketing después. Nunca al revés. Prometheo ordena y convierte demanda existente; el marketing la genera y la mide **sobre** esa base.
- **El índice tiene que funcionar:** anclas reales (`id` en cada sección, links en la barra). Es lo que distingue este género de un one-pager.
- **Separar los dos frentes visualmente:** "Parte 1 de 2 · Ventas" y "Parte 2 de 2 · Marketing" como marcadores claros. No se funden en un continuo indistinto.
- Cada número defendible y marcado como estimado cuando lo sea.
- Voseo, AUREA en mayúsculas, cero em-dashes.

## Checklist de inputs

| Necesitás | De dónde sale |
|---|---|
| Nombre del cliente y su situación (quién genera demanda hoy) | la reunión / auditoría |
| Los dolores de ventas (canales, trazabilidad, qué se cae) | la reunión |
| El alcance de marketing que aplica (Email, WhatsApp, medición) | lo acordado |
| Los canales de generación del cliente (pauta, base, redes) | la reunión |
| Presupuestos de cada frente (o "a definir" en rojo) | lo acordado |

## Tooling

Render con el sistema de la Familia A. Como es largo, cuidá especialmente el QA por chunks (cada sección) y que las anclas del índice resuelvan. HTML por defecto; PDF solo con aprobación. Presentá siempre el archivo.
