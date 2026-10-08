---
consultar-cuando: Etapa 2 iteración de prompt, procesar feedback de demo, corregir agente
disparadores: "documento de corrección", "feedback del agente", "iterar el prompt", "procesar correcciones", "ronda de feedback"
fuente-única-de: método de procesamiento de feedback y trazabilidad corrección→regla
combina-con: feedback-demo-iteracion, principios-transversales-agente, 03-reglas-diseno-prometheo-by-aurea
---

# Metodología de corrección del Agente IA

> Cómo se procesa el feedback de una demo y se convierte en mejoras del prompt, sin romper
> lo que ya funciona, dejando trazabilidad de qué corrección originó qué regla.

---

## Dónde encaja

Etapa 2, fase de iteración. Después de entregar el prompt V1 y la demo, el cliente prueba
el agente y marca correcciones en el Documento de Feedback (ver `feedback-demo-iteracion.md`
para el documento; este archivo es el **método** de procesarlas). El ciclo es:
demo → feedback → clasificación → corrección del prompt → nueva versión → nueva demo.

---

## El protocolo, en cinco pasos

**1. Leer todo el documento antes de tocar nada.** Una corrección puede contradecir o
matizar otra; se lee el conjunto primero. Si el feedback viene en capturas con marcas
(subrayado sobre la respuesta del agente), la crítica vive en el cruce captura↔marca: hay
que ver la marca, no solo el texto de la celda. (Nota operativa: el lector de Drive trae el
texto de las celdas pero NO las marcas sobre las imágenes; las capturas marcadas se revisan
aparte o se transcriben.)

**2. Clasificar cada corrección por capa.** Toda corrección cae en una de estas:
- **Dato / fuente** — el dato existe en la integración (Sheets/Tokko/PrestaShop) y el agente
  no lo tomó, o lo tomó mal. Se corrige en la fuente o en cómo el prompt instruye consultarla.
- **Terminología de rubro** — el agente usó una palabra incorrecta del oficio. Se corrige
  con vocabulario obligatorio/prohibido en el prompt.
- **Lógica conversacional / comercial** — el agente condujo mal la conversación (orden,
  ritmo, calificación, derivación). Se corrige con una regla de comportamiento.

**3. Detectar el patrón.** Varias correcciones suelen ser el mismo problema de fondo
(ej. ocho "reitera" distintos = un solo principio: no repetir, ampliar). Se corrige el
patrón una vez, no ocho veces.

**4. Extraer la lógica y decidir dónde va.**
- Si es específica del rubro → al archivo del rubro (`06-rubros/`).
- Si se vio en dos o más rubros → sube a `principios-transversales-agente.md`.
- Si es de la fuente → a `08-reglas-integracion-catalogo.md`.

**5. Aplicar al prompt de forma aditiva, aislada y no regresiva.** Las reglas de cómo tocar
el prompt sin romperlo están en `03-reglas-diseno-prometheo-by-aurea.md`. Cada corrección
se convierte en una regla que **cita el caso real que la originó** (ver Trazabilidad, abajo).

---

## Quién detecta qué — el arco de autoría (hallazgo de campo)

Cruzando feedback de cuatro documentos (G&D y EDFAN en desarrollista, BETROX en mobiliario,
con versión "consultor corrige" y versión "cliente corrige solo"), aparece un patrón
estable, **más fino que "cliente = datos, AUREA = lógica"**:

**Lo que el cliente puede aportar depende del PERFIL de quien corrige, no del rubro:**

- **Cliente operador / administrativo** (caso EDFAN autónomo): reporta capa de **dato y
  terminología**. "Esto está en Tokko y no lo tomó", "decí la calle Charcas, no Charcas",
  "es apto crédito". Muy poca lógica conversacional.
- **Cliente vendedor / del equipo comercial** (caso Celeste en G&D): reporta **también
  lógica comercial de rubro**. "Las reventas no van con financiación", "no afirmes escritura
  sin respaldo", "no inventes que la parrilla está solo en planta baja". Un vendedor ve la
  lógica de venta porque la vive.
- **AUREA, en los dos casos**, aporta la capa **transversal**: los principios de
  comportamiento del agente (no repetir, calificar antes de mostrar, no exponer la
  herramienta), que ningún cliente reporta espontáneamente porque no piensa en términos de
  diseño conversacional.

**Consecuencia para la consultoría:** el cliente tapa los agujeros de dato y terminología
(y, si es vendedor, también de lógica comercial); la doctrina conversacional transversal es
el valor agregado de AUREA. De cara a automatizar el procesamiento de feedback, la capa de
dato/terminología es la candidata a sistematizar primero; la conversacional queda como
criterio curado.

**Arco de enseñanza:** la primera ronda de corrección se hace en vivo, con pantalla
compartida, para transferir el criterio. Las siguientes las hace el cliente solo. El
documento autónomo del cliente (sin consultor al lado) es la evidencia de que el criterio
se transfirió. La calidad de ese documento autónomo mide qué tan bien enseñamos.

---

## Trazabilidad corrección → regla (el patrón de diseño clave)

El hallazgo más reutilizable de todo el procesamiento de feedback: **un prompt bien
diseñado lleva su propia trazabilidad adentro.** Cada regla que nace de una corrección cita
el caso real que la originó, con la cita verbatim del problema. Eso hace el prompt
auditable contra el feedback, y demuestra al cliente que su corrección se aplicó.

El formato canónico de una regla trazable, dentro del prompt:

```
REGLA [N] — [NOMBRE EN MAYÚSCULAS]. [enunciado de la regla].
(Caso real: [cita verbatim de lo que el agente respondió mal].)
```

### Casos reales documentados (de los tres prompts en producción)

Estos son ejemplos verificados de corrección → regla. Sirven de molde para el próximo cliente.

**G&D Developers (agente Veronica, fuente Google Sheets):**

| Corrección del cliente (verbatim) | Regla resultante en el prompt |
|---|---|
| "Menciona y reconfirma que Moca 2 tiene escritura, es erróneo" | Regla 56 — NO AFIRMAR ESCRITURA sin respaldo del Sheet |
| "Las reventas no son con financiación" | Regla 54 — REVENTAS SIEMPRE DE CONTADO |
| "Menciona solo m² cubiertos" | Regla 55 — SUPERFICIE: m² TOTALES POR DEFECTO |
| "2 ambientes exclusivos, da a entender que hay muchos, hay uno solo" | Regla 58 — NO PLURALIZAR STOCK |
| "Parrilla no necesariamente en planta baja, sigue dando esa respuesta" | Regla 59 — NO INVENTAR ATRIBUTOS POR INFERENCIA |
| "Ofrece Distrito Colegiales como disponible" | Regla 57 — SIN STOCK = ALTERNATIVA, nunca negación seca |
| "Habla de un proceso que nunca aclaramos, está inventando" | Regla 24 ampliada — no improvisar el proceso B2B inmobiliarias |

**EDFAN Real Estate (agente Martina, fuente Tokko):**

| Corrección (verbatim) | Regla resultante |
|---|---|
| "Dice en Charcas y debería decir en la calle Charcas / sobre Córdoba → Av. Córdoba" | Principio 22 — convención léxica de direcciones |
| "Dice en su sistema, el sistema es de la empresa" | Sección 7, Regla de Discreción (lista esa frase como ejemplo incorrecto) |
| "Le dije que es para que viva mi hija y me habla de inversión" | Principio 23 — framing según objetivo declarado |
| "Que diga que no tiene los planos, están cargados en Tokko" | Principio 20 + Regla Tokko — consultar la fuente, no negar de memoria |

**BETROX (agente Catalina, fuente PrestaShop):**

| Corrección (verbatim) | Regla resultante |
|---|---|
| "No quiero que mandes más de dos opciones, lo abrumás" | Sección 3.3 — máximo 2 opciones por turno |
| "El banco SIT 45 no es un PUFF, los PUFF son la línea TERRACE" | Sección 9 — taxonomía mobiliario urbano (PAROS/SIT/TERRACE) |
| "No utilizar unos milímetros, usar entre 1,5 y 2 cm" | Sección 7 — vocabulario de espesor |
| "Primero el precio, después la foto si la pide" | Sección 3 — de menos a más |
| "No te mandes al frente nombrando a Mariana, parecés un agente" | Sección 11 — Mariana solo en el handoff real |

---

## Tabla de registro de rondas (por cliente)

Se mantiene una bitácora por cliente para no perder el hilo entre versiones. Modelo:

| Ronda | Fecha | Autor (consultor / cliente, perfil) | Versión prompt antes → después | Nº correcciones | Capas tocadas |
|---|---|---|---|---|---|
| 1 | — | consultor (en vivo) | V1 → V2 | — | dato / terminología / lógica |
| 2 | — | cliente autónomo (vendedor/operador) | V2 → V3 | — | — |

Anotar el **perfil del autor** de cada ronda es parte del método: explica qué capa esperás
que reporte (ver arco de autoría) y dónde vas a tener que poner vos el criterio transversal.

---

## El barrido de coherencia — 8 chequeos antes de cada entrega

> Ninguna versión de un prompt se entrega sin correr antes este barrido. Es el corazón del
> método y la garantía operativa de la regla de oro: **una versión nueva no puede contradecir
> a sí misma ni romper lo que ya funcionaba.** Vive como hoja dentro del template de auditoría
> de entrega (ver `06-estructura-guia-implementador.md` y el template de auditoría). Si un
> chequeo falla, la versión no sale.

1. **Presencia.** Cada corrección de la ronda quedó efectivamente escrita en el prompt.
2. **Contradicción entre reglas.** No hay dos reglas que apliquen al mismo turno sin declarar
   cuál prevalece. Este es el chequeo que hace cumplir la regla de oro: si dos reglas chocan,
   o se resuelve la jerarquía (ver sección 0 del prompt) o no sale.
3. **Propagación de mecanismo.** Si se cambió un mecanismo (una forma de pago, un dato, una
   condición), el cambio se propagó a TODAS sus apariciones. Es el chequeo que ataca el
   patrón 9.
4. **Estructura huérfana.** No quedaron ejemplos, fichas o referencias que apunten a algo que
   ya no existe (un brochure retirado, un placeholder cruzado).
5. **Referencias cruzadas.** Los identificadores coinciden entre secciones (un archivo se
   nombra igual en el cuerpo y en el apéndice; una sección que remite a otra remite a la
   correcta).
6. **Ámbito de cada regla.** Cada regla dura declara cuándo NO aplica. Ataca el patrón 7.
7. **Reconciliación entre rondas.** La última corrección manda y no quedó residuo de la
   versión anterior conviviendo con la nueva. Ataca el patrón 10.
8. **Compatibilidad con la versión del proveedor.** Si Prometheo entregó una reescritura, se
   verificó qué reglas nuestras conservó, cuáles perdió y qué contradicciones metió, antes de
   activar (ver más abajo).

Chequeo 9 (cuando aplica) · **Verificación acumulada de feedback:** cada corrección reportada
por el cliente en rondas anteriores sigue verificada contra el texto vigente, con resultado
X/X por bloque. Incluye las que deben estar AUSENTES y siguen ausentes (un dato retirado, un
proyecto dado de baja).

### El template de auditoría de entrega (documento maestro, acompaña cada entrega)

Toda entrega de un prompt, parcial o completa, va acompañada de una planilla de auditoría que se
copia de un template en blanco y se completa. **Sin barrido completo volcado en la planilla, la
versión no se entrega.** El template tiene cinco hojas:

1. **Entrega** — qué sector se entregó, versión anterior → nueva, qué cambió, qué se eliminó
   (si algo se eliminó, es decisión explícita y documentada), qué no se tocó.
2. **Barrido de coherencia** — los 8 chequeos (más el 9 cuando aplica), cada uno con resultado
   OK / observación. Es la hoja que corre el barrido de arriba.
3. **Correcciones de la ronda** — cada corrección de esta ronda, con su síntoma verbatim, la
   regla resultante y la capa (dato / terminología / lógica).
4. **No regresión (lo sagrado)** — las reglas comerciales y de comportamiento que no se pueden
   perder, verificadas presentes en el texto nuevo. Es la lista de "lo que no se rompe".
5. **Pendientes** — lo que queda para la próxima ronda o depende de una definición del cliente
   o de ITESA.

El template en blanco es maestro (reutilizable en todo cliente). La planilla completada de cada
cliente es un **entregable de cliente**: documento vivo por cliente, se archiva por cliente, no
es método transversal. Ver la distinción método vs entregable abajo.

---

## El criterio de refuerzo completo de Prometheo

Una regla dura no se escribe solo en positivo. La forma completa, validada en los prompts
vivos, tiene cuatro partes:

1. **Regla positiva** — qué hacer.
2. **Prohibición explícita** — qué NO hacer, con la conducta incorrecta nombrada.
3. **Ámbito** — cuándo la regla NO aplica (evita el patrón 7).
4. **Autochequeo interno** — un control que el agente corre antes de enviar ("antes de
   responder, verificá que...").

**Por qué las cuatro partes:** la regla positiva sola se saltea; la prohibición sola no dice
qué hacer; sin ámbito produce conductas absurdas; sin autochequeo el agente no tiene cómo
atraparse el error. Cuando la corrección la formula el propio Prometheo, suele venir con la
regla positiva y la prohibición explícitas: **se conserva esa formulación tal cual**, no se
reescribe (ver Trazabilidad con las palabras del proveedor, abajo).

Ejemplo real, corrección de Prometheo sobre el primer mensaje de mobiliario urbano (BETROX),
citada como vino:
- Regla positiva: *"en el primer mensaje de cada conversación, saludá amablemente y respondé
  la consulta con contexto. Aunque envíes un video o archivo, nunca envíes únicamente la frase
  introductoria ni omitas la explicación del producto."*
- Prohibición: *"prohibido responder el primer mensaje sin saludo o solamente con un archivo o
  texto respondiendo únicamente lo que consulta."*

Así quedó en el prompt de Catalina, sección 2 ("PROHIBIDO EN EL PRIMER MENSAJE"), con el
ámbito (prevalece sobre las secciones específicas) y el autochequeo ("si lo único que estás
por mandar es un archivo, está mal: falta el saludo y la explicación"). Es el molde de cómo
una corrección del proveedor se integra sin perder su forma.

---

## Trazabilidad con las palabras del proveedor

Cuando la corrección viene formulada por Prometheo (no por el cliente ni por AUREA), su
**formulación se conserva**: es la forma en que el proveedor entiende su propia plataforma, y
reescribirla arriesga perder el matiz. Se cita textual en la matriz de auditoría del cliente,
con la regla positiva y la prohibición tal como las dio Prometheo, y se marca de qué versión
salió. Las **múltiples versiones del prompt de un agente** (Prometheo reescribió el de Catalina
varias veces) son parte de la trazabilidad: cada reescritura del proveedor se audita con el
barrido (chequeo 8) y se combina con la lógica comercial de AUREA, no se adopta ni se descarta
en bloque. El hallazgo estable: **la reescritura del proveedor mejora la estructura y pierde
lógica comercial; no se elige entre una y otra, se combinan** (detalle en
`gestion-proveedor-itesa.md`).
