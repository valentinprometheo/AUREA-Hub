# MÓDULO: GUÍA METODOLÓGICA

> Módulo de la skill `prometheo-docs-kickoff`. Especifica cómo generar la **Guía
> Metodológica** como DOCX que el implementador convierte a Google Doc. Leer este módulo
> después del `SKILL.md`, y después de haber generado y validado el Doc de Bienvenida
> (checkpoint).

---

## QUÉ ES ESTE DOCUMENTO

El segundo documento que el cliente recibe, **después del Doc de Bienvenida**. Le explica
**cómo va a funcionar el Discovery**:

1. Que el Discovery se organiza alrededor de **3 documentos vivos** que conviven durante toda la Etapa 1.
2. La **modalidad de cada uno** (sincrónico / asincrónico, dónde se completa).
3. Qué es la **"Biblia"** y por qué se llama así.
4. **Dónde vive todo** (carpeta de Google Drive compartida).

El cliente lo termina de leer y entiende que va a participar de forma activa pero
estructurada, con tiempo para responder con calma lo que necesite chequear internamente.

**Formato:** se genera como **DOCX**. El implementador lo sube a la carpeta de Drive del
cliente y lo abre como Google Doc nativo (un clic: "Abrir con Google Docs"). El documento
**vive como Google Doc** — navegable, enlazable — pero **nace DOCX** porque así la tabla de
4 columnas y la imagen quedan maquetadas perfecto.
**Personalización:** media — cambian el nombre del cliente, el N de reuniones, y si la
tipología macro del rubro no es "proyectos", los ejemplos del Documento 3.

---

## POR QUÉ DOCX QUE SE VUELVE GOOGLE DOC

| Razón | Detalle |
|---|---|
| Tiene que vivir como Google Doc | Navegable, el cliente vuelve a él durante toda la Etapa 1; enlazable a los 3 docs del Discovery |
| Pero se genera como DOCX | La integración de Drive **no convierte** archivos a Google Doc nativo. El camino confiable es DOCX → "Abrir con Google Docs", que preserva tabla e imagen |
| La librería `docx` maqueta bien | La tabla de 4 columnas y la imagen de los 3 documentos quedan nativas y prolijas — Google Docs las conserva al importar el DOCX |

El Doc de Bienvenida también es DOCX, pero ese se exporta a PDF y se envía. La Guía es
DOCX que se convierte a Google Doc y se usa. Misma generación, destino distinto.

---

## ESTRUCTURA — ENCABEZADO + APERTURA + 3 DOCUMENTOS + CIERRE

Títulos y orden **fijos**. El contenido de los 3 bloques de Documento es casi 100% texto
canónico — ver más abajo.

### ENCABEZADO

```
GUÍA METODOLÓGICA
Cómo vamos a trabajar el Discovery con [CLIENTE]
Los tres documentos del proceso · AUREA Hub × Prometheo
```

### APERTURA (texto canónico, solo cambia el nombre del cliente)

> "Antes de arrancar a trabajar el Discovery, queríamos compartirles cómo está organizado
> todo el proceso. Esto les permite tener el panorama claro de qué viene en las próximas
> semanas, cuándo van a participar de manera activa y cuándo van a tener tiempo para
> responder con calma.
>
> El Discovery se construye sobre tres documentos que conviven durante toda la Etapa 1.
> Cada uno tiene un ritmo y un propósito específico. A continuación los presentamos en una
> imagen y después los explicamos uno por uno."

### IMAGEN DE LOS 3 DOCUMENTOS

Diagrama único que muestra los 3 documentos del Discovery en una sola vista (1 sincrónico
+ 2 asincrónicos). Estilo visual: ver `01-metodologia/07-convenciones-aurea/02-metodologia-graficos.md`.

**Manejo de la imagen:** como la Guía se genera en DOCX, la imagen se **incrusta nativa**
en el documento (a diferencia de lo que pasaría con una creación vía API de texto plano).
Si la skill `prometheo-crm-graphics` puede generar el SVG del diagrama, se genera, se
convierte a PNG y se incrusta con `ImageRun`. Si no está disponible, se deja un recuadro
placeholder con la nota interna "[Insertar diagrama de los 3 documentos]" y el implementador
lo agrega. La Guía es válida y enviable aunque la imagen se agregue en un segundo paso.

---

### DOCUMENTO 1 · Discovery (la "Biblia")

**Modalidad** (texto canónico — el N de reuniones es input del implementador):
> "Sincrónico, a lo largo de todas las reuniones de la Etapa 1 (estimamos [N] reuniones para [CLIENTE])."

**Cuerpo (texto canónico):**
> "Es el documento central del proceso. Lo llenamos juntos durante cada reunión con
> pantalla compartida: vamos abriendo bloque por bloque, conversando sobre cada uno, y
> tipeando en vivo lo que ustedes nos cuentan. Cada bloque cubre un aspecto del negocio
> comercial: cómo está armado el equipo, cómo entran y se reparten las consultas, qué
> define a un comprador calificado, qué objeciones aparecen seguido, qué puede responder
> el agente solo y qué necesita derivar a una persona."

**Por qué le decimos Biblia (texto canónico):**
> "Cuando terminamos la Etapa 1, este documento se les envía para que lo revisen, corrijan
> y validen dentro de Google Docs. Una vez aprobado por ustedes, queda como la fuente
> oficial de verdad sobre el negocio de [CLIENTE]. Todo lo que viene después (el diseño
> del agente, la configuración del CRM, las campañas) se construye a partir de lo que diga
> la Biblia."

**Estructura de cada pregunta del Discovery** — se muestra en una **tabla de 4 columnas**:

| Por qué te preguntamos esto | La pregunta concreta | Lo que ya sabemos | Lo que nos cuentan |
|---|---|---|---|
| Explicación breve de para qué nos sirve esa información — cómo va a alimentar al agente, al CRM o a las campañas | La pregunta tal como aparece en la conversación. Después la repreguntamos según lo que vayan respondiendo | Lo que nuestro equipo ya pudo inferir del análisis previo a la reunión (web, redes, materiales públicos) | El espacio en blanco donde tipeamos en vivo lo que ustedes responden. Es lo que después se convierte en la fuente oficial de información |

---

### DOCUMENTO 2 · Asincrónico

**Modalidad (texto canónico):**
> "Asincrónico, en paralelo al Discovery. Lo van completando ustedes con su equipo, en el
> momento que prefieran, durante toda la Etapa 1."

**Cuerpo (texto canónico):**
> "Algunas preguntas requieren chequear datos puntuales (cuántas consultas reciben por
> semana exactamente, cuál fue la última tasa de conversión, cuáles son las cinco
> objeciones más comunes) o conversar internamente entre socios y equipo comercial. Esas
> preguntas no las forzamos en las reuniones sincrónicas: las dejamos planteadas acá y
> ustedes las responden con tiempo.
>
> Tiene la misma estética que el Discovery, con la misma explicación de para qué nos sirve
> cada respuesta. La única diferencia es que se completa por escrito, en los momentos que
> ustedes definan."

**Aclaración obligatoria (texto canónico):**
> "Una aclaración: es probable que este documento crezca a lo largo del proceso. A medida
> que vayamos avanzando con el Discovery sincrónico, vamos a detectar preguntas que tiene
> más sentido que ustedes respondan con tiempo en vez de en vivo. Esas preguntas las vamos
> sumando al asincrónico. Es esperable y forma parte de la metodología."

---

### DOCUMENTO 3 · Accesos y Documentación

**Modalidad (texto canónico):**
> "Asincrónico, lo completan ustedes. Durante las reuniones les vamos mostrando el
> documento y explicando cómo cargarlo."

**Cuerpo — afirmación canónica (fija) + enumeración de ejemplos (adaptable):**

La afirmación de qué es el Doc 3 es texto canónico y no cambia:
> "Es el inventario de todo el material que el agente va a necesitar para responder con
> precisión: [ENUMERACIÓN DE EJEMPLOS]. Ustedes lo van completando con tiempo, y nosotros
> en cada reunión les explicamos qué partes corresponden al tema que estamos conversando y
> cómo se carga cada cosa."

La `[ENUMERACIÓN DE EJEMPLOS]` **no es canónica** — es una lista ilustrativa que la skill
adapta al rubro. Su contenido se deriva de las categorías del Doc 3 real (ver template
`doc3-accesos-documentacion-template.md`, que es la fuente de verdad de qué hay en el Doc 3).

Ejemplos por rubro:
- **Real estate** (es lo que usó TKVA): "brochures de cada proyecto, fichas técnicas, listas de precios actualizadas, imágenes de obra, planos, accesos a Tokko, números de WhatsApp, links de redes, y conversaciones de ejemplo de cómo se comunican con sus clientes".
- **Mobiliario:** catálogos de línea, fichas de producto, accesos a la tienda, conversaciones de ejemplo, etc.
- **Insumos:** listas de precios mayoristas, fichas técnicas, conversaciones de ejemplo, etc.

> **Regla:** la enumeración siempre cierra mencionando las **conversaciones de referencia**
> ("conversaciones de ejemplo de cómo se comunican con sus clientes") — es una categoría
> del Doc 3 en todos los rubros. El resto de la enumeración se adapta. Si el template del
> Doc 3 incorpora una categoría nueva, esta enumeración se actualiza desde ahí, no se
> reinventa.

**Clave del documento (texto canónico):**
> "Este documento es clave porque la calidad del agente depende directamente de la calidad
> del material que tenga disponible. Cuanto más completo esté al cierre de la Etapa 1, más
> rápido podemos pasar al diseño del agente."

> **Ajuste opcional:** si el cliente ya tiene un CRM, se puede acortar la explicación de
> qué es un acceso y enfocar más en qué material específico falta. Aplicar solo si el
> implementador lo indica.

---

### CIERRE · "Dónde vive todo esto"

**Texto canónico:**
> "Los tres documentos se guardan en una carpeta compartida de Google Drive a la que
> ustedes tienen acceso permanente. Esto les permite revisar lo que conversamos, agregar
> información cuando lo necesiten, y mantener una única fuente de verdad sobre el negocio
> de [CLIENTE].
>
> Toda la información que se construye en el Discovery es la materia prima de las etapas
> siguientes (diseño del agente, configuración del CRM, lanzamiento). Por eso lo hacemos
> con esta estructura: una vez bien hecho, no se rehace."

**Cierre emocional** — en caja centrada:
> *"Estamos felices de empezar. Ahora abrimos el Documento 1 y arrancamos."*

**Firma:** Equipo AUREA Hub

---

## LINKS A LOS 3 DOCUMENTOS — ELEMENTO CONDICIONAL

El template del ZIP pide "links activos a los 3 documentos". **El Google Doc real de TKVA
no los tiene** — porque cuando se le envió la Guía, esos 3 documentos todavía no existían.

Regla: los links son **condicionales**, no obligatorios.

| Situación | Qué hace la skill |
|---|---|
| Los 3 docs del Discovery ya existen en el Drive del cliente (el implementador pasa los links) | Cada bloque de Documento enlaza al doc real con un link activo |
| Los 3 docs todavía no existen | La Guía **no menciona links** — se describe cada documento sin enlazarlo. Es válida así (es el caso TKVA) |

Nunca dejar un placeholder de link roto visible para el cliente. O hay link real, o no hay
mención de link.

---

## PATRÓN TÉCNICO DE GENERACIÓN — DOCX QUE SE VUELVE GOOGLE DOC

La Guía se genera como **DOCX** con la librería `docx` de Node (mismo stack que el Doc de
Bienvenida y que `prometheo-etapa2-design`).

1. `npm install docx` si no está instalada.
2. Construir el documento sección por sección con `Paragraph`, `TextRun`, `Table`, `ImageRun`:
   - Encabezado y apertura como `Paragraph` con estilos AUREA.
   - Los 3 bloques de Documento con el texto canónico (ver arriba), subtítulos en negrita.
   - **La tabla de 4 columnas** del Documento 1 como `Table` nativa de 4 columnas — se ve perfecta en el DOCX y Google Docs la conserva al importar. Este es el motivo por el que la Guía se genera en DOCX y no por API.
   - La imagen de los 3 documentos con `ImageRun` (ver sección de imagen arriba).
   - El cierre emocional como `Table` de 1 celda centrada con `shading` suave.
3. Empacar con `Packer.toBuffer` → escribir en `/mnt/user-data/outputs/`.
4. **Validar** con `python /mnt/skills/public/docx/scripts/office/validate.py`. Si falla: despaquetar, corregir XML, repaquetar.
5. **Subir a Drive (opcional, si el implementador pasó el ID de carpeta):** usar la
   herramienta de Drive `create_file` para subir el DOCX a la carpeta del cliente. El
   archivo queda como DOCX en Drive.
6. **Entregar al implementador** con esta instrucción explícita:
   > "La Guía está en DOCX. Subila a la carpeta de Drive del cliente (o ya está, si pasaste
   > el ID de carpeta) y abrila con **'Abrir con Google Docs'**. Google la convierte a Doc
   > nativo conservando la tabla y la imagen. Recién ahí compartís el link con el cliente."

**Nombre del archivo de salida:** `Guía Metodológica - [CLIENTE].docx`

> **Por qué este camino y no creación directa de Google Doc:** se probó crear el Doc vía
> la integración de Drive (`text/plain` y `text/html`) — en ambos casos el archivo queda
> como tipo suelto, sin convertirse a Google Doc nativo, y la tabla se pierde. El camino
> DOCX → "Abrir con Google Docs" es el único confiable: Google Docs importa DOCX
> preservando tablas, imágenes y estilos. El paso manual es un solo clic.

---

## CHECKLIST ANTES DE ENTREGAR

- [ ] Nombre del cliente correcto en título y a lo largo del doc
- [ ] N de reuniones estimado correcto en la modalidad del Documento 1
- [ ] Documento 3 con la enumeración de ejemplos adaptada al rubro, cerrando con las conversaciones de referencia
- [ ] Links a los 3 docs: incluidos solo si los docs ya existen; si no, sin mención de links
- [ ] Tabla de 4 columnas como `Table` nativa de 4 columnas en el DOCX
- [ ] Cierre emocional en caja centrada
- [ ] DOCX validado con el script de OOXML
- [ ] Archivo nombrado `Guía Metodológica - [CLIENTE].docx`
- [ ] Subido a la carpeta de Drive del cliente, si el implementador pasó el ID
- [ ] Entregado con la instrucción de "Abrir con Google Docs"

---

## CASO DE REFERENCIA

"GUÍA METODOLÓGICA — Cómo vamos a trabajar el Discovery con TKVA" — `08-casos-referencia/TKVA-real-estate/`.

TKVA es desarrollista inmobiliario. Lo que hizo especialmente bien: apertura empática y
clara, distinción nítida entre los 3 documentos, honestidad sobre que el asincrónico va a
crecer, cierre emocional fuerte. Notar que el Doc real de TKVA **no tiene links** a los 3
documentos — es el caso "los docs todavía no existían", y es perfectamente válido.

Lo que se adapta por cliente: cantidad de reuniones (TKVA 3-6, clientes chicos 2-3),
profundidad de la explicación del Documento 3 si el cliente ya tiene CRM, inventario de
assets del Documento 3 según la vertical.
