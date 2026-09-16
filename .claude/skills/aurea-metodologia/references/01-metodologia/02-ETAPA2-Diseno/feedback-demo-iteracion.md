# Feedback de Demo — Iteración del Agente IA

> El documento que el cliente completa durante el testing del agente IA para reportar
> respuestas incorrectas. Es la herramienta de iteración de Etapa 2, fase de demo.
> Permite que AUREA refine el prompt en ciclos cortos a partir de criterios reales del
> cliente, sin perder el contexto de qué falló y cómo debería haber respondido.

---

## Para qué sirve

Cuando el agente entra en fase de demo, el cliente lo prueba con conversaciones reales (o
simuladas). Inevitablemente aparecen respuestas que están mal: el agente cae a fallback,
arma un instructivo cuando debería dar un link directo, contradice una regla de
autonomía, usa un tono que no corresponde.

Para que esas correcciones se procesen ordenadamente, se usa el **Documento de Feedback
de Demo**: una tabla con una fila por corrección, donde el cliente pega la captura del
error y AUREA registra qué está mal y cómo debería responder.

Sin este documento, las correcciones llegan dispersas en mensajes de WhatsApp y se
pierden. Con este documento, el ciclo iterar → corregir → testear funciona.

---

## Estructura del documento

### Encabezado

Datos del cliente, agente, versión del prompt en demo, fecha de última actualización,
preparado por.

### Cómo se completa este documento (instrucciones al cliente)

- Hay una fila por cada corrección detectada en la conversación.
- En la columna izquierda va la **captura de pantalla** de la respuesta del agente que
  está mal, con el sector criticado marcado (subrayado o recuadrado).
- En la columna derecha se explica **qué está mal** y **cómo debería haber respondido**.
- La fila 1 viene **precargada como ejemplo** — para que el cliente entienda el formato
  antes de completar.
- Las filas siguientes están vacías. Se sugiere arrancar con ~10 filas; se agregan más si
  hacen falta.

### Reglas para marcar la captura (críticas)

- **Marcá antes de capturar.** Subrayá o recuadrá el sector criticado en la conversación,
  y recién después sacá la captura. Así la imagen llega señalando sola el problema.
- **El marcado es aditivo, nunca destructivo.** Se permite subrayar, recuadrar, poner una
  flecha al costado. Está **prohibido** tachar palabras, poner líneas encima del texto, o
  recortar partes de la respuesta del agente.
- **Una corrección por fila.** Si una misma conversación tiene varios problemas, son
  varias filas.
- **Por qué importa:** AUREA necesita leer qué respondió mal el agente para corregirlo.
  Tapar el texto destruye la información.

### Dónde se guarda

> Carpeta Drive del cliente → Etapa 2 — Diseño del Agente Inteligente → Iteración cliente

### Tabla de correcciones

Dos columnas:
- **Captura de la conversación** — la imagen marcada.
- **Corrección** — texto en dos partes: **Qué está mal** y **Cómo tendría que responder**.

La fila 1 viene **siempre precargada** con un ejemplo real (o adaptado del caso del
cliente) que muestre los dos campos completos en un caso concreto. Sin ese ejemplo, los
clientes no completan bien la primera fila vacía.

---

## Cómo se trabaja con el cliente

- **La primera vez se completa juntos en reunión con pantalla compartida.** Esto
  transfiere el criterio: el cliente ve cómo AUREA piensa la corrección y aprende el
  formato. Después siguen completando filas por su cuenta.
- AUREA revisa el documento periódicamente, procesa las correcciones, ajusta el prompt y
  comunica al cliente qué cambió. La nueva versión del prompt entra en demo y el ciclo
  continúa.
- Cuando el documento llega a ~10 correcciones procesadas, conviene cerrarlo y abrir uno
  nuevo para la próxima vuelta. Mantenerlo siempre con pocas filas activas evita que se
  pierda el foco.

---

## Versión del prompt

El encabezado **siempre** indica qué versión del prompt está en demo (V1, V2, V3…). Si
durante la iteración se actualiza el prompt y empieza una nueva vuelta de testing, **se
abre un documento de feedback nuevo** con la nueva versión. No se mezclan correcciones
del prompt viejo y el nuevo en el mismo documento — son ciclos distintos.

---

## Plantilla base — qué llevar al cliente

El documento que se entrega al cliente tiene:

1. Encabezado con datos del cliente y del agente.
2. Sección "Cómo se completa este documento".
3. Sección "Reglas para marcar la captura".
4. Sección "Dónde se guarda".
5. Tabla con **fila 1 precargada** como ejemplo y filas 2-10 vacías con placeholders.

La plantilla concreta se genera en formato DOCX (para que el cliente pueda pegar capturas
y completar texto directamente).

> **Caso de referencia:** BETROX — Feedback DEMO 2. Es la plantilla canónica que se
> reutiliza adaptando solo el encabezado y la fila de ejemplo al cliente concreto.

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| `metodologia-correccion-agente.md` | **El método** de procesar lo que se recoge en este documento (clasificar por capa, detectar patrón, trazar corrección→regla). Este archivo es el documento; ese es el método. |
| `principios-transversales-agente.md` | Las correcciones que se repiten en dos o más rubros suben ahí como principio transversal probado. |
| `prometheo-etapa2-design` (skill) | Genera los 4 outputs principales de Etapa 2. Este documento se entrega cuando esos outputs entran a fase de demo. |
| `refactorizacion.md` (módulo skill) | Las correcciones que sean estructurales (no de redacción) pueden disparar entradas en el Doc de Refactorización del cliente. |
| Etapa 3 — Lanzamiento | El cierre del feedback marca el pase a Go-Live. |

---

## Hallazgos de campo (confirmados con dos rubros)

> Aprendizajes sobre cómo funciona el documento con clientes reales. Confirmados procesando
> feedback de G&D y EDFAN (desarrollista) y BETROX (mobiliario), en versión consultor y
> versión cliente autónomo.

- **El documento es transversal al rubro:** el mismo formato de dos columnas (captura
  marcada + corrección) funcionó igual en desarrollista y en mobiliario. La plantilla no
  cambia entre rubros; lo que cambia es el contenido de las correcciones.
- **Arco de autoría (consultor → cliente autónomo):** la primera ronda se completa en vivo
  con pantalla compartida (transferencia de criterio); las siguientes las hace el cliente
  solo. El documento autónomo del cliente es la evidencia de que el criterio se transfirió.
  Qué capa reporta el cliente depende de su perfil (vendedor → lógica comercial; operador →
  datos). Detalle en `metodologia-correccion-agente.md`.
- **La marca sobre la captura es la crítica:** la corrección muchas veces vive en lo que el
  cliente subrayó dentro de la imagen, no en el texto de la celda. Nota operativa: el lector
  de Drive trae el texto pero no las marcas; las capturas marcadas se revisan/transcriben
  aparte.
- **El prompt lleva su propia trazabilidad:** cada regla que nace de una corrección cita el
  caso real que la originó ("Caso real: ..."), lo que hace el prompt auditable contra el
  feedback. Patrón de diseño documentado en `metodologia-correccion-agente.md`.

### Pendiente

- **Plantilla DOCX canónica reutilizable:** crear una versión limpia de la plantilla
  (sin datos de cliente) para que cualquier consultor la copie y adapte al cliente nuevo.
  Por ahora se reutiliza el BETROX como base.
