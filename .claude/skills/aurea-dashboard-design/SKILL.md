---
name: aurea-dashboard-design
description: "Diseño de dashboards web de Inteligencia Comercial de ÁUREA (Prometheo + Meta + canales). Usar al crear, rediseñar o auditar un dashboard, panel o tablero de métricas para un cliente."
---

# Dashboards de Inteligencia Comercial — ÁUREA

## Cuándo usar

Activar ante: "dashboard", "tablero", "panel de métricas", "Inteligencia Comercial", "reporte quincenal", o cuando se pida crear, rediseñar o auditar una vista de métricas para un cliente.

**No confundir con `aurea-deck-design`.** Esa skill es para documentos de una página: propuestas, guías, one-pagers, PDFs institucionales. Su estética — bandas full-bleed con gradiente al 15%, esfera iridiscente como decoro, secciones tipo landing — **no se hereda acá**. Un dashboard se escanea y se opera; un deck se lee de arriba a abajo. Ver "Qué NO se hereda del deck".

## Lo que es fijo: branding

No se negocia:

- **Paleta**: violeta `#7C5CBF`, azul `#5B8FD9`, rosa `#C77AA8`
- **Tipografías**: Arimo (texto, UI y datos) + Newsreader itálica (acento en títulos)
- **Logo ÁUREA** y esfera iridiscente

Todo lo demás — cards, bordes, radios, grillas, densidad, navegación, tipos de gráfico — está abierto.

**Advertencia a decir en voz alta al presentar:** en los dashboards viejos la identidad ÁUREA la cargaban las tarjetas pastel. Al sacarlas, el branding se apoya en tipografía, el acento itálico y la esfera usada con moderación. El resultado es **más sobrio**, no más vistoso. Anticiparlo evita que el primer render sorprenda.

## Qué NO se hereda del deck

| Del deck | En dashboard |
|---|---|
| Gradiente como superficie de sección | Gradiente solo como hairline, subrayado o estado activo |
| Esfera iridiscente repetida | Una sola aparición, en el encabezado |
| Tarjeta teida de color por bloque | Superficie neutra; el color se reserva para semántica |
| Un radio y una sombra en todo | Borde/relleno/sombra gastados por rol, no por defecto |

## Doctrina Básico / Avanzado

Los dashboards de ÁUREA tienen dos niveles. **Son dos profundidades, no dos vocabularios.**

- **Básico — "¿funcionó?"**: 4 KPI con delta contra el período anterior, el embudo completo, las 3 cards de acción de mayor impacto (con dueño y score), y una curva de tendencia.
- **Avanzado — "¿por qué?"**: todo lo del básico sin reemplazar nada, más KPI técnicos (CTR, CPC, cotizaciones, % calificación), tablas cruzadas campaña › conjunto › anuncio, variables de demanda, histórico largo y listas de audiencia con su tag de origen.

### Reglas del modo

1. **Un número, un nombre.** Nunca renombrar una métrica entre modos. Si un término no se entiende, se explica en tooltip — no se traduce. Renombrar rompe el idioma común con el cliente en la reunión.
2. **El glosario vive en los dos modos.** Quien menos sabe es quien más lo necesita. Jamás esconder definiciones detrás del modo experto.
3. **Avanzado agrega, nunca reemplaza.** Subir de nivel no puede hacer desaparecer nada visible abajo.
4. **El switch actúa en todas las vistas.** Si una sección se ve igual en ambos modos, el control enseña que es decorativo y el cliente deja de usarlo.

## Especificaciones de componentes

### KPI tile
Superficie neutra, sin teñir. Etiqueta en mayúsculas con letter-spacing, cifra grande en Arimo con `font-variant-numeric: tabular-nums`, y **delta obligatorio** contra el período anterior. El color aparece solo en el delta y solo como semántica (mejor / peor / neutro). Cuatro KPI con cuatro colores distintos es decoración, no información.

### Embudo
No dibujar a escala lineal. Un embudo comercial típico va de cientos de miles de impresiones a unidades de venta — cinco órdenes de magnitud — y una barra proporcional deja los últimos pasos invisibles. Dibujar como **pasos con la tasa de conversión entre pasos como cifra protagonista**, y el valor absoluto secundario.

### Sparkline y series
Toda línea lleva escala: mínimo y máximo rótulados, punto final marcado y delta explícito. Una línea que sube sin referencia puede ser +3% o +300%: no informa. Para "menos es mejor" (costo por comprador), rotularlo en el eje.

### Tablas
`tabular-nums`, contenedor con `overflow-x: auto` propio, encabezado con la **fuente del dato** cuando hay cruce de plataformas (Meta / Prometheo / cálculo). Nunca mostrar nombres técnicos de creativos sin traducción o tooltip.

### Color semántico
Bueno / atención / crítico, definidos aparte del acento de marca. No usar violeta-azul-rosa para codificar estado: son identidad, no semántica.

### Obligatorios
- **Modo oscuro** con tokens en `:root` y redefinición en `prefers-color-scheme` y `[data-theme]`.
- **Estados vacíos**: con exports periódicos reales siempre hay períodos sin dato suficiente. "Sin datos suficientes en este período" es una vista diseñada, no un hueco.
- **Fecha de última actualización por fuente**, visible.

## Cards de acción (skill `aurea-data-action-driven`)

"¿Qué hago ahora?" se arma con **cards de acción**, no con bullets. Anatomía y CSS de referencia
en `anatomia-card.md` de esa skill:

- **Sello** con uno de seis verbos (Corregir, Proteger, Separar, Medir, Decidir, Activar) y un
  dueño (AUREA, Ventas, Marketing, Dirección).
- **Título** "Tema · dato principal", con el número en el título.
- **Score data-driven** grande, pegado al título: "85% basada en datos", barra y etiqueta de banda.
- **Contexto** visible plegada (qué mide, base, dato y fuente) y **despliegue** con qué hacer,
  dónde se cambia, efecto esperado, cómo lo medimos (con guardiana) y por qué este score.

Reglas de diseño:
- **Superficie neutra.** El color aparece solo en el sello (verbo) y en la barra del score (banda).
  Los sellos y las bandas tienen **paleta semántica propia**: nunca violeta, azul ni rosa de marca.
- **Básico:** tres cards, ordenadas por impacto; las de score menor a 55 muestran la etiqueta de
  banda sin desplegar. **Avanzado:** todas.
- **Los números del tablero no llevan score**: llevan base, cobertura y origen. El score es de
  las acciones.
- En documentos estáticos, la card va toda desplegada.
- Modo oscuro: los tokens de sellos y bandas se redefinen igual que el resto.

## Arquitectura: por pregunta, no por canal

Nombrar secciones por plataforma ("Meta", "Google") obliga a sumar una pestaña por canal nuevo, y el cliente termina navegando el organigrama de las herramientas en vez de su negocio.

Ordenar por pregunta, con el canal como **filtro transversal**:

1. ¿Cómo venimos? — panorama + evolución
2. ¿Qué pide el mercado? — demanda (viene de Prometheo, es independiente del canal)
3. ¿Qué trajo resultado? — campañas, filtrable por canal
4. ¿Qué hago ahora? — cards de acción con score y audiencias, con dueño
5. ¿De dónde sale esto? — fuentes, cruce y última actualización

Estructura de pestañas vigente: la del tablero EAF V3, agrupada por estas cinco preguntas (ver
`aurea-ic-dashboard`). Se suma una pestaña de **consumo y costos** (IA y Meta) con el criterio de
`aurea-hub-costos-rentabilidad`. Cada pestaña cierra con su lectura "y entonces qué", aunque sea
"no requiere acción este período".

## Fuentes de datos

Activas: **Prometheo** (perfil y calificación del lead), **Meta** (performance de pauta), **WhatsApp Marketing**. Previstas: Google, LinkedIn Marketing.

El cruce Prometheo × Meta se hace por ID de anuncio: Meta ve hasta el clic, Prometheo ve del clic a la venta. Ese cruce es la propuesta de valor del dashboard y debe estar explicado en el producto, no asumido.

## Antipatrones verificados

Detectados auditando dashboards reales. Chequear que ninguno se repita:

- Switch de modo que no actúa en la mayoría de las vistas.
- Modo "simple" que solo renombra métricas en vez de reducir profundidad.
- Glosario de columnas disponible únicamente en modo avanzado.
- Modo simple mostrando nombres crudos de creativos sin explicación.
- KPI con un color distinto cada uno, sin que el color signifique nada.
- Sparklines sin escala ni delta.
- Embudo de varios órdenes de magnitud dibujado con cajas de igual tamaño.
- Gris claro sobre fondo teido: revisar contraste contra WCAG AA.

## Antes de entregar

1. ¿El switch cambia algo en **todas** las vistas?
2. ¿Alguna métrica cambia de nombre entre modos? (debe ser no)
3. ¿Cada cifra tiene su definición accesible desde los dos modos?
4. ¿Cada color que usé significa algo?
5. ¿Cada serie tiene escala y delta?
6. ¿Funciona en oscuro y a 400px de ancho?
7. ¿Hay estado vacío diseñado?
8. ¿Se ve la fecha de actualización por fuente?
9. Contra el inventario del dashboard anterior: ¿se perdió algún dato? (debe ser no)
10. ¿Cada recomendación es una card con sello, dueño y score, y su color es semántico, no de marca?
11. ¿Cada pestaña tiene su lectura "y entonces qué"?