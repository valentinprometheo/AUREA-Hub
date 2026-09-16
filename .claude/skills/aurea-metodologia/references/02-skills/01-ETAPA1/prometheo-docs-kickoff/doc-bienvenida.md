# MÓDULO: DOC DE BIENVENIDA // KICKOFF

> Módulo de la skill `prometheo-docs-kickoff`. Especifica cómo generar el **DOCX
> de Bienvenida**. Leer este módulo después del `SKILL.md` y antes de generar el documento.

---

## QUÉ ES ESTE DOCUMENTO

El primer documento que el cliente recibe del proyecto, **antes de la R1**. Es la primera
impresión profesional de AUREA. Cumple 4 funciones a la vez:

1. Mostrar que llegamos a R1 con un **panorama del negocio** (no en frío).
2. Explicar **qué se va a diseñar** (los 3 pilares conceptuales).
3. Presentar **las 4 etapas** del proyecto.
4. Definir **quién tiene que estar en R1** del lado del cliente.

**Formato:** DOCX. El implementador lo exporta a PDF antes de enviarlo al cliente.
**Personalización:** alta — Secciones 1 y 5 cambian por cliente; 2, 3 y 4 son casi fijas.

---

## ESTRUCTURA — ENCABEZADO + 5 SECCIONES

El orden y los títulos de las secciones son **fijos**. El encabezado de portada también.
Solo cambia el contenido.

### ENCABEZADO DE PORTADA (fijo en estructura)

Tres líneas, antes de la Sección 1. Tomado del documento real de TKVA:

```
[eyebrow]  AUREA Hub — PROPUESTA DE TRABAJO
[título]   [CLIENTE] — Implementación de CRM y Agente de Ventas con IA
[subtítulo] Documento de bienvenida y hoja de ruta
```

Debajo, el **párrafo de apertura** (fijo, solo cambia el nombre del cliente):

> "Hola equipo [CLIENTE], antes de nuestra primera reunión queríamos compartirles este
> documento. Lo armamos después de revisar su web y redes para llegar a la conversación
> con un primer panorama del negocio. La idea no es que respondan nada todavía: solo
> queríamos mostrarles desde dónde arrancamos, qué entendemos de [CLIENTE] hasta acá, y
> qué viene en las próximas semanas de trabajo conjunto."

Logo AUREA Hub arriba a la izquierda.

---

### SECCIÓN 1 · "Lo que ya sabemos de [CLIENTE]"

**Es la sección que más personalización requiere. Todo el contenido sale del Doc 0.**

Estructura interna — subtítulos en negrita, contenido en bullets:

| Sub-bloque | Qué incluye | Origen |
|---|---|---|
| Trayectoria y volumen | Años en el mercado, números de escala (m², unidades, clientes, etc.) | Doc 0 |
| Cartera comercial activa | Proyectos / productos / líneas activas, con nombres reales | Doc 0 |
| Posicionamiento y comunicación | Tono de marca, canales activos (WhatsApp, IG, web, etc.) | Doc 0 |
| **Qué nos queda por entender (lo vemos en la R1)** | **Cierre obligatorio** — párrafo que lista 3-5 temas que la auditoría NO pudo inferir | Doc 0 (gaps) |

**Reglas de esta sección:**
- **Nunca inventar números.** Si el Doc 0 no tiene un dato, no va. Un número falso destruye la confianza en la primera página.
- Los nombres de proyectos/productos van **literales**, como aparecen en la web del cliente.
- El cierre "Qué nos queda por entender" **es obligatorio** — la honestidad sobre lo que falta es parte del valor. Se redacta en prosa, no en bullets, listando los temas abiertos en una sola frase fluida.
- Tono: profesional, sobrio, basado en datos verificables.

**Ejemplo de cierre (TKVA real), como referencia de tono:**
> "Cómo se reparte hoy el trabajo comercial entre ustedes, qué herramientas usan para
> gestionar consultas, cómo califican un comprador inversor versus uno de vivienda, qué
> financiación ofrecen... De esto y otros puntos hablamos en la primera reunión."

---

### SECCIÓN 2 · "Qué vamos a diseñar juntos"

**Contenido casi fijo.** Solo se adaptan los ejemplos del rubro. Explica los 3 pilares
conceptuales del sistema, sin jerga técnica.

**Frase de apertura (fija):**
> "El trabajo consiste en implementar un sistema que combine un agente automático con su
> equipo humano. El agente atiende cada consulta entrante, conversa de manera natural,
> califica al interesado y, según el caso, lo deriva al vendedor correcto con toda la
> información ya organizada."

**Pilar A · El embudo y los roles del equipo**

Explica el funnel comercial (etapas: lead nuevo → calificado → oportunidad → visita/demo →
reserva → venta — adaptar nombres de etapa al rubro) y los **3 roles** que tienen que
existir del lado del cliente:
- **Quien atiende primero** — el agente automático como filtro inicial 24/7.
- **Quien toma la conversación humana** — vendedor que recibe el lead ya calificado con la ficha armada, no empieza de cero.
- **Quien lidera la operación** — alguien que mira el embudo completo en un panel y toma decisiones con datos.

**Pilar B · Los momentos clave de cada conversación**

Los 2 momentos base de toda implementación:
- **Seguimiento activo** — cuando el lead deja de responder, el sistema retoma con un mensaje calibrado al punto exacto donde quedó.
- **Derivación a humano** — cuando el lead está calificado o pide explícitamente una persona, se entrega al vendedor con la ficha completa.

Más los **momentos específicos del rubro** (adaptar): para real estate → consulta de financiación, interés en proyecto puntual, objeción de precio, pedido de visita a obra. Para otros rubros, los momentos equivalentes.

**Pilar C · La ficha del interesado que se arma sola**

El agente completa automáticamente una ficha mientras conversa (nombre, qué consultó,
perfil, presupuesto si lo declaró, canal de origen, urgencia, objeciones). Cuando el lead
llega al vendedor, la ficha ya está.

**Regla de esta sección:** lenguaje de negocio. **Nunca** usar las palabras "Variable",
"Smart Tag", "embudo de 3 niveles" ni ninguna taxonomía CRM. El cliente no la necesita acá.

---

### SECCIÓN 3 · "Cómo vamos a trabajar"

**Contenido fijo.** Presenta las 4 etapas del proyecto.

**Frase de apertura (fija):**
> "El proyecto se organiza en cuatro etapas. La primera es donde nos enfocamos ahora; las
> siguientes están listadas para que tengan el panorama completo."

**Etapa 1 — Discovery** — se explica con detalle, 3 sub-puntos obligatorios:
- **Qué hacemos:** entender a fondo cómo funciona el negocio hoy.
- **Cómo lo hacemos:** una R1 de ~90 min para mapear el negocio en bloques + reuniones siguientes más cortas para cerrar lo abierto + documento asincrónico liviano entre reuniones. **Acá va el N estimado de reuniones** (input del implementador — TKVA: 3-6; clientes chicos: 2-3).
- **Qué entregamos al cierre:** un documento maestro con el negocio sintetizado — la materia prima de las etapas siguientes.

**Etapas 2, 3 y 4** — se listan, un párrafo cada una:
- **Etapa 2 — Diseño del CRM y del agente:** se traduce el Discovery en el sistema concreto.
- **Etapa 3 — Implementación y lanzamiento:** se configura todo en Prometheo, se conectan canales, se capacita al equipo, se sale en vivo con un MVP acotado.
- **Etapa 4 — Monitoreo y mejora continua:** ya en producción, se mide con datos reales y se afina.

**Cierre obligatorio (fijo):**
> "No necesitan preparar material previo: las preguntas las traemos nosotros. La
> conversación tendrá una estructura clara para que el tiempo rinda y salgamos con la
> mayor parte del negocio mapeada."

---

### SECCIÓN 4 · "Con quién necesitamos conversar de [CLIENTE]"

**Contenido fijo.** Define los **5 dominios de conocimiento** del Discovery y quién los cubre.

**Frase de apertura (fija):**
> "Para que la primera reunión rinda al máximo, necesitamos que del lado de [CLIENTE]
> participen las personas que conocen el día a día comercial. No hace falta que sea una
> sola persona ni un cargo específico: lo importante es que entre quienes nos acompañen
> cubran los cinco dominios de conocimiento que vamos a recorrer juntos."

**Los 5 dominios** (fijos — solo se adapta el ejemplo de tipología macro):
1. **Equipo y operación comercial** — cómo está armado el equipo, cómo se reparten los leads, qué herramientas usan, por qué canales entran las consultas.
2. **Objetivo del proyecto y métricas actuales** — dolores actuales, volumen de consultas por semana, cuántas avanzan, tasa de conversión actual.
3. **Cartera de [proyectos/productos/líneas] y calificación** — qué se vende, cómo se diferencia un buen lead, cómo se trabaja con terceros (inmobiliarias/arquitectos/etc.). *Adaptar "proyectos/productos/líneas" a la tipología macro del rubro.*
4. **Conversación con el cliente: preguntas frecuentes, objeciones, flujo y tono** — FAQs que se repiten, objeciones frecuentes, recorrido típico, tono de marca.
5. **Autonomía del agente, derivación a humano y excepciones** — qué decide el agente solo (precios, financiación, plazos), qué escala siempre, casos especiales, reglas para referidos.

**Cierre obligatorio (fijo):**
> "En la práctica, esto suele resolverse con la persona que coordina el área comercial
> más, idealmente, quien toma decisiones sobre precios y financiación. Si las dos personas
> son la misma, mejor todavía."

**Elemento opcional adaptable:** si el rubro lo amerita, agregar la frase de TKVA sobre
Marketing: *"También vamos a invitar en algún momento a la persona encargada de Marketing
según avance la consultoría."* Incluir solo si el implementador lo indica.

---

### SECCIÓN 5 · "Quién va a estar acompañándolos del lado de AUREA"

Presentación formal del consultor asignado.

**Frase de apertura (fija):**
> "Queremos darles la bienvenida formal al inicio de este trabajo y presentarles a la
> persona de nuestro equipo que llevará adelante la consultoría e implementación de la
> cuenta [CLIENTE]."

**Tarjeta del consultor** — recuadro visual: foto circular + texto al lado, sobre fondo
suave. Contiene:
- Nombre del consultor (destacado, tipografía grande).
- Perfil profesional + rol: "[Nombre] es [perfil]. Estará a cargo de la cuenta de
  [CLIENTE] como Consultor e Implementador, en el marco de la metodología de AUREA Hub.
  Los acompañará durante todo el proceso, desde el discovery inicial hasta el lanzamiento
  del agente y el monitoreo posterior."
- Una frase sobre su trabajo concreto en el proyecto.

**Manejo de la foto:**
- Si el implementador la aportó → se incrusta en el recuadro circular.
- Si falta → se deja un recuadro placeholder con la nota interna "[Insertar foto del consultor]". El implementador la agrega antes de enviar.

Si hay **más de un consultor** asignado, presentar a los dos, una tarjeta cada uno.

**Cierre del documento (fijo):**
> "Bienvenidos al proyecto. Estamos entusiasmados de empezar. Cualquier duda antes de la
> reunión, escribinos sin problema. Nos vemos pronto.
>
> Equipo AUREA Hub"

---

## CONVENCIONES VISUALES

Paleta completa en `01-metodologia/07-convenciones-aurea/01-paleta-y-colores.md`.

| Elemento | Especificación |
|---|---|
| Logo AUREA Hub | Arriba a la izquierda, en la portada |
| Eyebrow de marca | Morado AUREA `#7C5CBF`, mayúsculas, tamaño chico |
| Títulos de sección | Formato "1 · Título", oscuro AUREA `#2D2D3D`, con línea de color debajo |
| Callouts / cajas destacadas | Borde azul AUREA `#5B8FD9`, fondo azul muy claro — para frases clave (el cierre de Sección 4, el "Bienvenidos al proyecto") |
| Texto principal | Oscuro AUREA `#2D2D3D` |
| Texto secundario | Gris AUREA `#7A7A7A` |
| Tarjeta del consultor | Recuadro con esquinas redondeadas, foto circular + texto al lado |

---

## PATRÓN TÉCNICO DE GENERACIÓN

El DOCX se genera con la librería `docx` de Node (mismo patrón que `prometheo-etapa2-design`).

1. `npm install docx` si no está instalada.
2. Construir el documento sección por sección con `Paragraph`, `TextRun`, `Table`, `ImageRun`.
3. El encabezado de portada y los títulos "N · Título" como `Paragraph` con estilo propio.
4. Los callouts como `Table` de 1 celda con `borders` y `shading` azul claro.
5. La tarjeta del consultor como `Table` de 1 fila × 2 celdas (foto | texto).
6. Empacar con `Packer.toBuffer` → escribir en `/mnt/user-data/outputs/`.
7. **Validar** con `python /mnt/skills/public/docx/scripts/office/validate.py`. Si falla: despaquetar, corregir XML, repaquetar.

**Nombre del archivo de salida:** `AUREA Hub - Bienvenida [CLIENTE].docx`

---

## CHECKLIST ANTES DE ENTREGAR

- [ ] Encabezado de portada con el nombre del cliente correcto
- [ ] Sección 1 con datos VERIFICADOS del Doc 0 — cero números inventados
- [ ] Sección 1 con cierre "Qué nos queda por entender" honesto (3-5 temas)
- [ ] Sección 2 con ejemplos del rubro del cliente, sin jerga CRM
- [ ] Sección 3 con el N de reuniones estimado correcto
- [ ] Sección 4 con la tipología macro adaptada al rubro en el dominio 3
- [ ] Sección 5 con el consultor correcto, perfil y foto (o placeholder)
- [ ] DOCX validado con el script de OOXML
- [ ] Archivo nombrado `AUREA Hub - Bienvenida [CLIENTE].docx`

---

## CASO DE REFERENCIA

`AUREA Hub - Bienvenida TKVA` — `08-casos-referencia/TKVA-real-estate/`.

TKVA es desarrollista inmobiliario. Vale como referencia de tono, nivel de detalle y
estructura. Lo que hizo especialmente bien: Sección 1 con datos verificables y específicos
(45.000 m², 700 unidades, nombres reales de proyectos), honestidad sobre lo que falta,
Sección 5 con presentación visual fuerte del consultor.

Lo que se adapta por cliente: cantidad de reuniones (TKVA 3-6, clientes chicos 2-3),
profundidad de la Sección 1 (depende de qué tan pública es la información del cliente),
cantidad de consultores presentados.
