# 01 · El producto: qué es Inteligencia Comercial

## Definición corta (para cualquier pieza)
Inteligencia Comercial es un **tablero omnicanal** que cruza el dato de ventas con el de marketing y suma **criterio comercial**, para que el cliente tome **decisiones con más información y más rápidas**. Producto estrella, diseñado por AUREA Hub.

## Las tres promesas (cards principales aprobadas)
1. **Métricas operativas, al instante.** Ventas y cada canal de marketing, actualizados en un solo tablero.
2. **Decisiones con más información y más rápidas.** El dato de la venta cruzado con el de la pauta, con la acción que conviene tomar.
3. **Tu tablero, donde estés.** Desde el celular o la computadora, y en las reuniones con todas las áreas del equipo.

## El tablero omnicanal (el concepto central)
Así como Prometheo tiene **chat omnicanal** (todas las conversaciones en una bandeja), IC es el **tablero omnicanal**: todo el dato comercial en una pantalla. En las piezas se dice directo, sin la analogía: *"Ventas y marketing en una sola pantalla: todo tu dato comercial, centralizado y actualizado."*

Estructura narrativa aprobada:
- **Ventas · Insights de tu CRM:** quién consulta, quién califica y quién compra. Fuente: Prometheo (la plataforma que gestiona AUREA Hub) o el CRM del cliente.
- **Marketing · Performance y marketing directo:** la pauta y las campañas, canal por canal (Meta Ads, Google Ads, LinkedIn, Email, WhatsApp).
- **= Inteligencia Comercial · El dato completo, de punta a punta:** decisiones data-driven, saber qué estrategia trae compradores y dónde invertir, **ser dueño de tu dato y de tus decisiones**.
- **Sumá tu canal:** el tablero crece con el negocio; cada canal nuevo se integra como un módulo (espejo de la pestaña Integraciones).

### Terminología de marketing (usar así)
- **Performance marketing:** pauta paga medible (Meta Ads, Google Ads, LinkedIn Ads).
- **Marketing directo** (también CRM marketing): Email y WhatsApp sobre la base propia del cliente.
- **Estrategia de marketing:** el paraguas (objetivos, mensajes, creativos, calendario).
- En piezas: "performance y marketing directo" cubre ambos sin mezclarlos.

## La capa de criterio comercial (el diferencial)
**Narrativa externa aprobada:** *"Métricas, y le sumamos criterio comercial."* Tus métricas vienen con la lógica de venta que mejor funciona en tu negocio: el agente la aplica en cada conversación y el tablero la mide.

Cadena de tres pasos (cards aprobadas):
1. **Métodos de venta probados:** elegidos para tu rubro y tu tipo de cliente.
2. **Tu agente vende con ese método:** lo aplica en cada conversación, igual que tu equipo.
3. **Lo ves medido en tu tablero:** sabés qué funciona y qué ajustar, con datos.

Teaser aprobado (misterio): *"Evaluamos siete metodologías de venta. Solo entran las que se vuelven dato."*

**Interno (no va a piezas comerciales):** el criterio usa un núcleo fijo de campos (Gap Selling, Jobs to be Done, SPIN) y una capa variable por rubro (JTBD, Hormozi, Solution Selling). Filtro de entrada: si una metodología no produce un dato que el agente pueda extraer de una conversación, no entra. El detalle técnico vive en `aurea-ic-criterio-comercial`.

Ligado a la consultoría de Ventas: si el cliente ya tiene lógica comercial, la potenciamos; si no, se la prestamos ("Desarrollamos una lógica comercial para tu negocio").

## El tablero: pestañas y beneficios
Cada pestaña responde una pregunta del cliente (estructura de referencia: tablero EAF V3, ver `aurea-ic-dashboard`):

| Pregunta | Pestañas | Beneficio que se comunica |
|---|---|---|
| ¿Cómo venimos? | Panorama, Evolución | La foto del mes en una pantalla; cómo rinde cada ronda frente a la anterior |
| ¿Qué pide el mercado? | Venta · CRM, pestañas del rubro, Criterio comercial, Insights | A quién venderle primero; tu lógica de venta medida; las decisiones del mes listas |
| ¿Qué trajo resultado? | Meta Ads, Google Ads, Email, WhatsApp, Meta en Prometheo | Qué canal, campaña y creativo trae compradores |
| ¿Qué hago ahora? | Audiencias, recomendaciones con dueño | Tus compradores como semilla de pauta; acciones con responsable |
| ¿Qué falta conectar? | Integraciones | Sumá tu canal |
| (transversal) | Consumo y costos | Cuánto cuesta cada conversación y cada mensaje, y cómo bajarlo |

- **Dos modos de lectura:** Simple (dirección, lenguaje literal, sin siglas) y Avanzada (marketing, métricas técnicas).
- **Por rubro o a medida.** Ejemplo de personalización: seguir a 15 comerciales con la performance de cada uno.
- **Cadencia:** quincenal de base; a la agencia, si hace falta, semanal.

### Qué se muestra y qué no (FOMO)
Mostrar: Panorama, Venta · CRM, Insights con su beneficio. Insinuar (desenfocado o con candado): Criterio comercial, Audiencias, Evolución, pestañas de canal. Cierre: *"El resto, en la demo. Cada tablero se diseña para tu rubro."*

## Del dato a la decisión (las acciones)
Las "decisiones, no métricas" se entregan como **cards de acción**: cada una dice qué hacer, quién
lo hace, qué efecto esperamos y **cuán basada en datos está** (score de 0 a 100%). Una acción con
poca evidencia no se esconde: se declara como prueba acotada y se mide. Detalle técnico en
`aurea-data-action-driven`; cómo se muestra en `aurea-ic-dashboard`.
Narrativa externa: ver hallazgo del 13/10/2026 (frase a validar).

## Cómo funciona por dentro (interno y para pitch técnico)
- **Fuentes:** export de Prometheo (calidad y perfil del lead, con ID de anuncio) + reporte de Meta a nivel anuncio (performance) + estructura de Meta (nombres). Se suman Google, Email y WhatsApp como canales.
- **La llave del cruce:** `ID Anuncio` (Prometheo) = `Ad ID` (Meta). Jerarquía: campaña, conjunto de anuncios, anuncio (con nombre individual para poder medir cada creativo).
- **Lo que trae Prometheo no es solo calificación:** tipo de comprador, industria o aplicación, zona, empresa, producto de interés, etapa, objeción, escala, dolor, repuestos y servicio. Cada variable es filtrable y cruzable con la pauta.
- **Lectura vs escritura:** la capa de lectura (el tablero) es viable hoy con exports y concentra la mayor parte del valor. La capa de escritura (devolver eventos a Meta por CAPI, audiencias Lookalike de compradores) requiere plan Enterprise y WhatsApp API oficial.
- **Integraciones Meta que se comunican:** Lead Forms (cada lead con su origen), Ads · CAPI (el evento vuelve y la pauta aprende), Audiencias · Lookalike (compradores reales como semilla).

## Preguntas que responde (de la presentación oficial de IC)
- ¿Quién compra de verdad, y no solo consulta? (semilla de Lookalike)
- ¿Qué inversión de marketing se paga sola? (priorización de pauta)
- ¿En qué punto se te cae la venta? (eventos de conversión)
- ¿Qué te piden y todavía no ofrecés? (inteligencia de producto)
