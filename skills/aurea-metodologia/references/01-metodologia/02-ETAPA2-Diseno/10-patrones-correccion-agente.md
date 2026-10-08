---
consultar-cuando: iniciar corrección de un agente, auditar un prompt vivo, ubicar un bug dentro de un patrón conocido
disparadores: "patrones de corrección", "auditar el prompt", "trazabilidad", "por qué falla el agente", "13 patrones"
fuente-única-de: los 13 patrones de error recurrentes en cualquier agente de Prometheo
combina-con: metodologia-correccion-agente, principios-transversales-agente, 05-estructura-prompt-agente
---

# Los 13 patrones de corrección de agentes IA

> Documento maestro, reutilizable en cualquier cliente. Los 13 errores que se repiten en
> cualquier agente de Prometheo, sin importar el rubro. Es la referencia para hacer
> trazabilidad en un cliente nuevo: se lee, se marca qué patrones aplican, y se busca en su
> prompt si están cubiertos, parciales o en hueco.
>
> Validados en producción con dos agentes de rubros distintos: **Martina** (EDFAN,
> desarrollista inmobiliario, Tokko) y **Catalina** (BETROX, mobiliario, PrestaShop). Los que
> aparecen en los dos de forma independiente están marcados **[transversal probado]**.
>
> **Regla de oro de este documento (no negociable):** un patrón describe un error observado y
> la regla que lo corrige, tal como quedó en un prompt que HOY funciona. No se inventan reglas
> que obliguen a romper lo que anda. Cuando dos reglas pueden chocar, el patrón remite a la
> jerarquía de reglas (ver `05-estructura-prompt-agente.md`), que resuelve el conflicto por
> diseño en vez de dejar dos reglas sueltas.

---

## Cómo se usa este documento

1. Al arrancar con un cliente nuevo, o cuando aparece un bug, se lee la lista y se marca qué
   patrones aplican a ese agente.
2. Se busca en su prompt si cada patrón aplicable está **cubierto**, **parcial** o en **hueco**.
3. El resultado se vuelca en la matriz de auditoría del cliente (ver
   `metodologia-correccion-agente.md`, barrido de coherencia).
4. Si aparece un error que no encaja en ningún patrón, es un **patrón nuevo**: se agrega acá.

Estados posibles de un patrón en un prompt auditado: CUBIERTO (regla presente y con ámbito),
PARCIAL (la regla existe pero una vía de escape genérica la puede saltear), HUECO (no hay regla),
HUECO POR DISEÑO (el cliente decidió deliberadamente no cubrirlo).

---

## Los 10 patrones

### Patrón 1 · Dato que la integración devuelve y el agente dice no tener  [transversal probado]
- **Síntoma:** el lead pide un dato que la fuente (Tokko/PrestaShop/Sheet) sí devuelve, y el
  agente lo evade, lo deriva o dice que no lo tiene.
- **Causa real:** conviven una regla específica ("estado de obra y entrega salen de la fuente,
  se comunican") con vías de escape genéricas ("si el dato no está disponible, derivá") que no
  declaran que esos datos quedan fuera de su alcance. La genérica habilita la evasión.
- **Regla a escribir:** enumerar explícitamente qué datos devuelve la integración y que esos
  NO se derivan; prohibir la frase de escape; acotar el ámbito de la vía de derivación genérica
  para que no pise a la específica.
- **Evidencia:** Martina, patrón activo en la auditoría de EDFAN (secciones 2.11 y 12.10
  reabren la evasión de estado y entrega). Catalina 1.1: "NUNCA afirmás que el catálogo no
  especifica un atributo sin haberlo buscado".

### Patrón 2 · Regla fija que se pierde cuando la pregunta viene combinada  [transversal probado]
- **Síntoma:** el lead pregunta dos cosas en un mensaje (ej. precio + forma de pago), y el
  agente responde una y trunca la regla fija de la otra.
- **Causa real:** la regla fija (ej. "DONADO solo contado", "las sillas se ofrecen con la
  alternativa del banco") no declara que se aplica entera aunque venga mezclada con otro pedido.
- **Regla a escribir:** cuando un pedido combinado toca una regla fija del negocio, esa regla
  se enuncia completa, igual que si la pregunta hubiera venido sola.
- **Evidencia:** Martina 2.6. Catalina 5B (sillas: "se aplica ENTERA sin importar cómo venga
  formulada la pregunta... vale igual cuando el pedido viene combinado").

### Patrón 3 · Prioridad comercial que no se respeta al ofrecer
- **Síntoma:** ante varias opciones que matchean, el agente elige el orden por su cuenta, no
  por la prioridad comercial del cliente.
- **Causa real:** no hay regla de priorización; lo más cercano es el matcheo por criterio del
  lead, que no es lo mismo que la prioridad de colocación del negocio.
- **Regla a escribir:** definir con el cliente qué se ofrece primero y con qué criterio; los
  destacados van siempre primero dentro de su categoría.
- **Estado típico:** en BETROX está CUBIERTO (lista de destacados con "van siempre primero,
  nunca MÉXICO como destacado"). En EDFAN es HUECO **bloqueado por el cliente**: no se puede
  escribir sin que EDFAN defina qué proyectos colocar primero. **Nota de método:** un hueco
  bloqueado por el cliente no se rellena por criterio propio; se documenta como pendiente de
  definición.

### Patrón 4 · Apertura que se saltea  [transversal probado]
- **Síntoma:** el primer mensaje no saluda, o saluda pero omite pedir el nombre, o responde
  solo con un archivo sin explicación.
- **Causa real:** la regla de apertura no declara prevalencia sobre las reglas de formato
  posteriores (típicamente "una pregunta por turno", que compite con un primer turno que lleva
  saludo + nombre + respuesta + pregunta).
- **Regla a escribir:** la apertura es regla de máxima prioridad y prevalece sobre todas las
  secciones, incluidas las específicas; el primer turno lleva saludo + presentación + (nombre)
  + respuesta con contexto, y la regla de una pregunta por turno no aplica al primer turno.
- **Evidencia:** Catalina S2 ("APERTURA — REGLA DE MÁXIMA PRIORIDAD... ESTA REGLA PREVALECE
  SOBRE TODAS LAS SECCIONES"). Martina 3.5 (la apertura prevalece sobre la 2.2). **Es el
  ejemplo canónico de por qué el prompt necesita jerarquía de reglas (Frente jerarquía).**

### Patrón 5 · Se asume una variante que el cliente no pidió  [transversal probado]
- **Síntoma:** el lead nombra un proyecto o una familia y el agente muestra una unidad o
  variante concreta sin preguntar cuál.
- **Causa real:** la desambiguación cubre el nivel de arriba (proyecto) pero no el de abajo
  (tipología/variante); y hay una regla ("mostrá el más económico de cada tipología") que sin
  ámbito empuja a mostrar unidades antes de saber qué busca el lead.
- **Regla a escribir:** no asumir tipología/variante antes de mostrar una unidad concreta;
  ante una familia con varias variantes, dar info general y preguntar forma/medida antes de
  mostrar.
- **Evidencia:** Martina 8.2 ("No asumas la tipología"). Catalina 5 y 1.3 bis (familia:
  SPRING, RAW Pastilla, MOSCÚ; "acotar el tipo no siempre alcanza").

### Patrón 6 · Mismo nombre en entidades distintas  [transversal probado]
- **Síntoma:** un nombre corresponde a más de una entidad y el agente responde por la
  equivocada.
- **Causa real:** la regla de desambiguación nombra solo algunos casos; quedan homónimos sin
  cubrir. Falta declarar la identidad completa de la entidad.
- **Regla a escribir:** declarar la identidad completa (en real-estate: proyecto + tipología +
  UF; en mobiliario: categoría + modelo + variante) y desambiguar todo homónimo antes de dar
  datos.
- **Evidencia:** Martina 4 ("VERVÉ" = Villa Crespo o Chacarita; "el de Villa Urquiza" = EDEN o
  BLANCO ENCALADA). Catalina 5 y 9 (MOSCÚ existe en 4 categorías; SINUOSE en 3; "Mesa RAW
  Pastilla" ≠ "Mesa baja RAW Pastilla").

### Patrón 7 · Regla absoluta sin ámbito  [transversal probado]
- **Síntoma:** una regla escrita como absoluta produce una conducta absurda en un caso que no
  contempló (el ejemplo canónico: "una pregunta por turno" rompe el primer turno).
- **Causa real:** la regla no declara su ámbito (cuándo NO aplica).
- **Regla a escribir:** toda regla dura lleva su ámbito. La forma completa de una regla de
  Prometheo es **regla positiva + prohibición explícita + ámbito + autochequeo interno** (ver
  criterio de refuerzo completo en `metodologia-correccion-agente.md`).
- **Evidencia:** Martina 2.2 (ámbito declarado: "aplica a partir del segundo mensaje").
  Catalina, criterio aplicado de forma consistente (casi cada regla dura tiene su "PROHIBIDO"
  y su "control interno antes de enviar"). **Nota de campo:** en Martina el criterio está en
  varias reglas pero no en todas; la aplicación despareja entre prompts es en sí un hallazgo
  a emparejar por cliente (no en la metodología).

### Patrón 8 · Cierre que no vende
- **Síntoma:** ante una señal de compra, el agente responde el dato y cierra neutro, sin
  avanzar.
- **Causa real:** el cierre neutro no distingue una consulta informativa de una señal de compra.
- **Regla a escribir:** definir qué es señal de compra (pedir precio, medidas, forma de pago
  sobre una unidad concreta) y que ante ella el agente responde el dato Y ofrece el paso
  siguiente en el mismo mensaje.
- **Estado típico:** en BETROX y EDFAN está CUBIERTO (CTA de encuentro / señales de compra).
  **Nota:** en EDFAN fue durante un tiempo HUECO POR DISEÑO (el cliente no quería que el
  agente empujara reuniones); activarlo fue decisión del cliente, no criterio propio. Un hueco
  por diseño solo se cubre cuando el cliente lo habilita.

### Patrón 9 · Cambio de mecanismo que no se propaga  [transversal probado]
- **Síntoma:** se cambia una regla o un dato y queda un residuo del mecanismo viejo en otra
  parte del prompt (un ejemplo con la forma anterior, una ficha que promete material que ya no
  existe, un placeholder cruzado).
- **Causa real:** la corrección se aplicó en un lugar y no se propagó a todas sus apariciones.
- **Regla a escribir:** no es una regla del agente, es un chequeo del método: el barrido de
  coherencia (chequeo de propagación de mecanismo y de referencias cruzadas) tiene que correr
  antes de cada entrega.
- **Evidencia:** Martina, auditoría EDFAN (ejemplo de financiación con mecanismo viejo en 9.5
  vs 9.1; fichas que prometían brochure inexistente). Catalina, auditoría V3.0-R3 (nombres de
  archivo rotos, "2 o 3" vs "2" en distintas secciones). **Este patrón es la razón de ser del
  barrido de 8 chequeos.**

### Patrón 10 · Correcciones de rondas distintas que se pisan  [transversal probado]
- **Síntoma:** una corrección de una ronda reabre o contradice una de una ronda anterior.
- **Causa real:** no se reconcilian las rondas; queda rastro de la versión anterior conviviendo
  con la nueva.
- **Regla a escribir:** la última corrección manda, pero el conflicto entre rondas se documenta
  para que no se reabra; el barrido incluye el chequeo de reconciliación entre rondas.
- **Evidencia:** Martina, patrón CUBIERTO en el punto caliente (la orden vieja de informar
  estado en toda mención fue reemplazada por el criterio de primera presentación, sin residuos).
  Catalina, auditoría V3.0-R3 (5 reglas comerciales que la reescritura del proveedor había
  perdido, repuestas).

### Patrón 11 · Contradicción de jerarquía entre dos reglas propias  [transversal probado]
- **Síntoma:** un bug puntual sobre un producto o caso ("con PAROS muestra solo 2"), que en
  realidad se repite en cualquier familia o categoría.
- **Causa real:** dos reglas nuestras, correctas por separado, compiten en el mismo turno. Una
  está muy reforzada ("2 por turno") y la otra nunca se escribió ("si pide todo, dale todo"). La
  reforzada gana y pisa el caso no contemplado. NO es un hueco: es competencia entre reglas.
- **Regla a escribir:** no reforzar la que falla. Nombrar los dos casos, declarar cuál prevalece
  o acotar el ámbito de cada una, y hacerlo GENERAL (cualquier familia o categoría), nunca puntual
  del producto que disparó el bug. Ver el desarrollo completo en `contradicciones-jerarquia.md`.
- **Evidencia:** Catalina, caso PAROS, confirmado por soporte de Prometheo ("el problema no está
  en PAROS sino en una contradicción de jerarquía del prompt"). Traducción real-estate: "mostrame
  todas las unidades del proyecto" vs recomendación abierta.

### Patrón 12 · CTA que existe pero no vende  [transversal probado]
- **Síntoma:** el agente cierra con una pregunta, así que "tiene CTA", pero el cierre es
  administrativo y no acerca la venta.
- **Causa real:** el prompt exige que haya CTA pero no distingue un CTA comercial de uno de
  trámite. El agente cumple la forma (hay pregunta) sin cumplir el fondo (vender).
- **Regla a escribir:** el CTA no solo tiene que existir, tiene que usar una lógica comercial
  (avanzar con el modelo que le interese, pasar precios, invitar al showroom, preguntar para
  asesorar). Un pendiente con el equipo nunca es el cierre.
- **Detección:** NO se caza con chequeo de presencia (el CTA figura). Solo leyendo si el cierre
  usa una lógica comercial o es puro trámite. **Es el puente con la doctrina de lógica comercial**
  (ver `logica-comercial-transversal.md`): el patrón describe el error; la lógica comercial dice
  qué hace que un cierre venda.
- **Evidencia:** Catalina ("te confirmo las medidas con el equipo, ¿sigo con los precios?" vs
  "¿cuál te interesa para pasarte precio y verlo en tu espacio?"). Traducción real-estate: "te
  confirmo disponibilidad con el equipo" vs "¿coordinamos una visita a la obra?".

### Patrón 13 · Regla condicionada a una evaluación ambigua del contexto  [transversal probado]
- **Síntoma:** una acción obligatoria (saludar, presentarse) no ocurre en ciertos escenarios de
  entrada, sobre todo cuando la conversación llega por un anuncio o con metadatos previos.
- **Causa real:** la regla depende de una condición que obliga al agente a interpretar el contexto
  ("¿es el primer mensaje de la conversación?"). Ante un anuncio, una etiqueta o un origen de
  contacto, el agente interpreta mal y cae en la rama equivocada.
- **Regla a escribir:** no reforzar la acción. Cambiar la condición por una **binaria sobre un
  hecho verificable** ("¿ya hice yo esta acción?") y nombrar qué NO cuenta (anuncio, etiqueta,
  metadato). Detección: buscar toda regla que arranque con "si es el primer / el último / el
  único / si ya pasó X".
- **Evidencia:** Catalina, saludo de mobiliario urbano que fallaba al entrar por anuncio de Meta.
  Corrección: "¿ya saludaste vos? Un anuncio o una etiqueta del sistema no cuentan". Traducción
  real-estate: "presentate si es el primer contacto" falla igual al entrar por un anuncio de un
  proyecto.

---

## Relación con las 9 lógicas previas de real-estate

En `06-rubros/01-real-estate.md` viven las lógicas comerciales del rubro desarrollista
(precisión de stock, reventas de contado, no inferir atributos, etc.). Esas son **específicas
del rubro**: qué dato es correcto en una inmobiliaria. Los 10 patrones de acá son **el nivel de
arriba**: la forma del error (una regla sin ámbito, un homónimo sin desambiguar) que se repite
en cualquier rubro. Una lógica de real-estate suele ser una instancia de un patrón (ej.
"sin stock nunca 'no tenemos'" es una instancia del patrón 1). No se duplican: el rubro dice
qué es correcto; el patrón dice qué forma tiene el error y cómo se escribe la regla que lo cierra.

## Cómo evoluciona esta lista

Cada error nuevo que marca un cliente: (1) se ve si encaja en un patrón existente; (2) si es un
patrón nuevo, se agrega acá con su evidencia; (3) si revela un hueco del método (no del prompt),
se agrega un chequeo al barrido de coherencia. Así nacieron los chequeos de estructura huérfana
y de compatibilidad con la versión del proveedor.
