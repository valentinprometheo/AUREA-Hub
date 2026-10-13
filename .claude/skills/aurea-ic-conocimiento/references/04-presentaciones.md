# 04 · Presentaciones: estructura, estética, frases y checklist

## Catálogo de piezas existentes (para reusar, no rehacer)
| Pieza | Público | Qué tiene |
|---|---|---|
| Presentación Principal · Ecosistema Comercial 360 con IA | Prospectos y clientes | Hero, Beneficios, círculo 360, consultoría, Marketing, Ventas, IC, CTA demo |
| Inteligencia Comercial · Deck Oficial (presentación al consultor) | Consultor de producto, partners | Rentabilidad, después del clic, dos lecturas, recorrido, loop, por qué el insight es nuestro, integraciones Meta, precio por canal, comisión de agencias |
| Panorama de Mercado y Objeciones | Uso interno y comercial | Tres fuerzas, postura, Lean Startup medido, tendencias a ofertas, objeciones |
| Sé Partner | Agencias de marketing | Las dos capas, integraciones Meta, seis lecturas, tablero compartido, comisiones |
| Presupuestos por cliente (DRAKON, PAVIR, EAF) | Cliente puntual | Referencia estética canónica; precios por cliente |
| Tableros de IC (EAF V3, PAVIR, DRAKON) | Cliente | Producto real; ver `aurea-ic-dashboard` |
| Plan de acción IC (pitch CTO, GTM, mercado y proyección) | Interno, CTO | Ver `hallazgos.md` |

## Estructura canónica de la sección IC dentro de un deck
1. Banda de apertura: *"Inteligencia Comercial · Nuestro producto estrella, diseñado por AUREA Hub."*
2. Para qué sirve: título *"Tus insights, en métricas operativas al instante"* + las tres promesas.
3. Tablero omnicanal: Ventas + Marketing = el dato completo, y "Sumá tu canal".
4. Capa de criterio comercial: *"Métricas, y le sumamos criterio comercial"* + cadena de tres pasos + teaser con candado.
5. Diseñado por rubro o a tu medida: ventana del tablero con pestañas, tres visibles, el resto desenfocado, *"El resto, en la demo"*, y el ejemplo de los 15 comerciales.
6. Precio compacto y chico.
7. Al cierre del documento: sector intermedio con el CTA.

## Estructura del deck principal 360
Hero → Beneficios (bloque azul) → Círculo 360 (diferencial: servicios integrales con un solo equipo, AUREA 360 primero) → Consultoría (*"Investigamos cómo vende tu negocio, para escalarlo"*) → divisor "Cómo lo hacemos" → 01 Marketing → 02 Ventas (beneficios primero, consultoría, implementación, rentabilidad, inversión chica, Mejora Continua Start vs Pro) → 03 IC → cierre → sector CTA → contactos → footer.

## Banco de frases aprobadas
- *Cada vez más valor.* (cabecera)
- *Generamos, convertimos y medimos.*
- *Meta ve hasta el clic. Prometheo ve del clic a la venta.*
- *Tus insights, en métricas operativas al instante.*
- *Métricas, y le sumamos criterio comercial.*
- *Sos dueño de tu dato y de tus decisiones.*
- *Ventas y marketing en una sola pantalla.*
- *Sumá tu canal.*
- *Investigamos cómo vende tu negocio, para escalarlo.* / *Lo que descubrimos hoy es lo que escala mañana.*
- *Desarrollamos una lógica comercial para tu negocio.* / *Llevamos tu forma de vender a la IA.*
- *Ninguna consulta se pierde. Cada una, más cerca de la venta.*
- *Diseñamos la trazabilidad entre la tecnología, tu negocio y tu equipo, para acelerar procesos humanos, no para reemplazarlos.*
- *La gestión ya no vale. El criterio y el dato, sí.*
- Hook CTA: *¿Venís pensando en tomar decisiones data-driven?*

## Frases y patrones prohibidos
- Cualquier gancho negativo: "no solo clics", "no te damos solo números", "no vendemos herramientas".
- Jerga interna hacia el cliente: "agentificable", "capa variable", nombres de metodologías de venta.
- "La IA sin estrategia no vende" como frase propia (no es la de AUREA).
- Precios de Marketing.
- Nombres de competidores o de clientes sin permiso (los ejemplos B2B o B2C van anónimos).
- Prometer un porcentaje de rendimiento por ser data-driven (los estudios que lo miden son correlaciones en grandes empresas; ver tensión T2 de `aurea-data-action-driven`).
- Costos derogados: "desde USD 149" como piso de plataforma, "USD 20 cada 2.000 chats", "~80% de ahorro", "Meta solo cobra campañas". Los vigentes están en `aurea-hub-costos-rentabilidad`.

## Estética (familia A, deck HTML)
- **Referencia exacta:** el presupuesto de DRAKON (CSS y componentes: topnav, bandas numeradas, divisores de color, hsteps, cards, callouts, priced, cc + ejemplo). Reusar su `<head>` y armar el cuerpo con sus clases.
- **Entrega:** solo HTML, nunca PDF salvo pedido explícito. Siempre responsive y verificado a 390 px sin desborde.
- **Tipografía:** sans moderna (Arimo/Helvetica); cursiva serif liviana **solo** en el acento de títulos principales y del hook del CTA.
- **Color:** intensidad baja. Más o menos 1 de cada 5 cards con fondo (degradé suave AUREA); nunca dos degradés juntos; sin azul ni oscuro dentro de grillas de beneficios. Sin marrón: paleta violeta, azul, rosa, cian, coral.
- **Jerarquía:** íconos en vez de bullets; títulos de sector grandes con divisor; precios chicos y secundarios pero claros.
- **Logo:** sin círculo blanco ni sombra detrás.
- **Círculo 360:** anillo degradé con logo al centro, "Cada vez / más valor" en dos renglones con brillo suave, nodos 01 Marketing, 02 Ventas, 03 Inteligencia / Comercial (dos renglones).
- **CTA:** botón "Agendá tu demo" con ícono de calendario → `https://calendar.app.google/jSWne7nP9ZKJZ3Lg7` (pestaña nueva).
- **Contacto:** info@aureahub.com.ar (al hacer click se copia al portapapeles) y aureahub.com.ar, con íconos.

## Checklist antes de entregar
- [ ] Ningún gancho negativo; tono afirmativo y de valor agregado.
- [ ] Cada número con su estado (real, referencia, ilustrativo, supuesto).
- [ ] Sin precios de Marketing; precios de Ventas e IC chicos.
- [ ] Costos de plataforma, IA y Meta contra `aurea-hub-costos-rentabilidad` (ningún derogado).
- [ ] FOMO: IC no se divulga completo; metodologías sin nombre.
- [ ] CTA de demo con el link correcto; mail info@.
- [ ] Sin guiones largos, "AUREA" sin tilde, voseo, tildes y eñes completas.
- [ ] Responsive verificado a 390 px.
- [ ] Solo HTML.
