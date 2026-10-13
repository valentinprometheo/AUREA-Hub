---
consultar-cuando: antes de entregar cualquier versión de un prompt, cerrar una ronda de correcciones
disparadores: "barrido", "verificar el prompt", "está listo para entregar", "sacar la v13", "chequeo de coherencia"
fuente-única-de: paso de verificación obligatorio antes de entregar una versión de prompt
combina-con: 01-entrega-por-sector-completo, 03-matriz-auditoria
---

# 02 · Barrido de coherencia

> Paso **OBLIGATORIO** que se ejecuta ANTES de entregar cualquier versión de un prompt, sea
> parcial o completa. Su resultado se vuelca en la **matriz de auditoría del cliente**.
> **Sin barrido, la versión no se entrega.**

---

## El punto ciego que este paso cierra

El método de correcciones aditivas verifica que una regla **esté** en el texto. No verifica
que sea **coherente** con el resto del prompt.

Esa diferencia no es teórica. Cuando dos reglas propias compiten por el mismo turno de
conversación, el agente falla de forma intermitente, y el síntoma se parece muchísimo a un
problema de plataforma o de modelo. Se pierden rondas enteras buscando afuera una causa que
está adentro del prompt, y peor: se "refuerza" la regla que ya estaba, que es exactamente lo
que no hay que hacer cuando el problema es competencia interna.

**Hasta acá el proceso validaba presencia. A partir de ahora valida presencia Y coherencia.**

---

## Los siete chequeos

### 1 · Chequeo de presencia

El que ya hacíamos. Verificar **por script** que cada regla corregida esté **literalmente** en
el texto de la versión a entregar.

- Se corre sobre el texto final, no sobre el borrador.
- Se busca por cadena literal (nombre de regla, número, frase clave del enunciado), no por
  "me acuerdo de haberla escrito".
- Ayuda mecánica: `scripts/barrido.py --reglas`.

**Es el piso, no el techo.** Una regla presente puede estar en conflicto con otras cinco. Los
chequeos 2 a 7 existen porque este solo no alcanza.

---

### 2 · Chequeo de contradicción entre reglas

Por cada regla **nueva o modificada**, buscar en **TODO** el prompt otras reglas que hablen
del **mismo comportamiento**, y verificar que no compitan.

Criterio operativo: si dos reglas pueden aplicar **al mismo turno de conversación**, una de
las dos tiene que declarar **prevalencia explícita** sobre la otra, o **acotar su ámbito**.
No alcanza con que "se entienda cuál gana".

Fórmula de prevalencia, para pegar dentro de la regla:

```
Esta regla prevalece sobre [regla / sección X] cuando [condición].
```

Cómo se busca, en concreto:

- Extraé el **comportamiento** que la regla nueva gobierna (abrir la conversación, mostrar
  opciones, enviar un archivo, pedir un dato, derivar, priorizar una fuente).
- Buscá ese comportamiento por sus palabras, en todo el prompt, no solo en el sector que
  tocaste.
- Leé cada coincidencia preguntando: si el lead escribe X, ¿cuál de las dos reglas se aplica?
  Si la respuesta no es inmediata, hay conflicto.

> **Caso real (saludo).** La Sección 2 decía que el primer mensaje abre SIEMPRE con saludo,
> sin excepción, y la Sección 3 decía saludo en un mensaje e información en otro. Dos reglas
> propias compitiendo por el mismo turno. El agente falló semanas y se atribuyó a la
> plataforma. La causa era nuestra.

> **Caso real (material de base).** La regla 1.1 mandaba leer el dato desde la integración y
> la 1.8 (prioridad de respuesta) no lo listaba entre los datos dinámicos. Misma competencia
> interna, mismas rondas de refuerzo perdidas.

**Señal de alarma:** si venís "reforzando" la misma regla ronda tras ronda y el agente sigue
fallando igual, dejá de reforzar y corré este chequeo. Un refuerzo que no mueve la aguja casi
siempre significa que hay otra regla ganándole el turno.

---

### 3 · Chequeo de propagación de mecanismo

Distinguir entre cambiar una **frase** y cambiar un **mecanismo**.

- **Frase:** cambia cómo se dice algo. Impacto local.
- **Mecanismo:** cambia **de dónde sale un dato**, **cómo se envía algo**, o **qué fuente
  manda**. Impacto en todo el prompt.

**Si cambió un mecanismo, hay que barrer TODAS las secciones que lo mencionan, no solo la que
lo define.** El error típico es reescribir la sección que DEFINE el mecanismo y dejar intactas
las que lo MENCIONAN.

Procedimiento:

1. Nombrá el mecanismo en una frase ("las fotos ahora salen de la integración nativa del
   catálogo, no del apéndice").
2. Elegí las **palabras clave** del mecanismo viejo y del nuevo (nombre del apéndice, nombre
   de la integración, verbo de envío, nombre del archivo).
3. Buscá cada una en el prompt **completo**.
4. Verificá que **todas** las apariciones digan lo mismo. Las que quedaron con el mecanismo
   viejo se corrigen en la **misma ronda**, no en la siguiente.
5. No pares en el primer foco. Los mecanismos suelen estar mencionados en tres, cuatro o cinco
   lugares distintos.

> **Caso real (fotos a PrestaShop).** Al migrar el envío de fotos a la integración nativa de
> PrestaShop se reescribió la Sección 6, que define el mecanismo, pero la Sección 4 siguió
> diciendo "enviás la foto del Apéndice". Después aparecieron tres focos más en otras
> secciones. Se cambió la sección que DEFINE y no las que MENCIONAN.

Ayuda mecánica: `scripts/barrido.py --mecanismo "palabra clave"` lista todas las apariciones
con su sector.

---

### 4 · Chequeo de estructura huérfana

Un cambio de mecanismo no solo desactualiza texto: **deja estructura sin función**.

Si al cambiar la fuente de un dato queda un **bloque, índice, tabla o apéndice** que servía a
la fuente vieja y ya no sirve a nadie, **se elimina**. No se conserva "por las dudas", no se
deja comentado, no se deja "para la fase 2".

Por qué se elimina y no se archiva adentro del prompt:

- Un bloque huérfano **consume tokens en cada mensaje**, para siempre.
- Es **fuente de contradicciones futuras**: la próxima ronda lo lee como si estuviera vigente
  y arma reglas encima.
- Rompe el chequeo 2 de forma silenciosa: sigue siendo una regla del prompt que puede ganar un
  turno.

Procedimiento:

1. Con el mecanismo nuevo ya escrito, preguntá por cada bloque que tocaba el mecanismo viejo:
   ¿alguien lo invoca todavía? ¿alguna regla vigente lo necesita?
2. Si la respuesta es no en las dos, es huérfano.
3. Eliminalo **en el mismo sector completo que estás entregando**, así el borrado viaja con la
   corrección y queda trazado.
4. Registralo en la matriz: qué bloque se eliminó y por qué quedó sin función. El registro es
   lo que evita que alguien lo "restaure" tres rondas después pensando que se borró por error.

> **Caso real (fotos a PrestaShop).** Cuando las fotos pasaron a venir de PrestaShop, el bloque
> que servía a la fuente vieja quedó en el prompt sin función, ocupando tokens y generando
> contradicciones. Había que detectarlo y eliminarlo, no solo actualizarlo.

**Ojo con los placeholders:** un inventario de placeholders no es huérfano solo porque cambió
la fuente de un dato distinto. Antes de eliminar un bloque de placeholders, verificá contra el
inventario real (ver `01-entrega-por-sector-completo.md`). Borrar un placeholder vivo rompe el
adjunto en silencio.

---

### 5 · Chequeo de referencias cruzadas

Extraer del prompt **todas** las menciones del tipo `ver Sección X`, `(Sección X)`,
`según la regla N`, y verificar que:

- esa sección o regla **exista** en el prompt, y
- **contenga lo que se invoca**.

Mismo chequeo para **placeholders** y **nombres de archivo** citados en el cuerpo del prompt:
que el placeholder exista en el inventario y que el nombre coincida verbatim, con sus tildes,
mayúsculas, espacios y extensión.

Una referencia rota no da error: el agente simplemente no encuentra la lógica invocada y
resuelve por su cuenta. Es el fallo más silencioso de los siete.

> **Caso real (Sección 5B).** La Sección 9 invocaba la lógica de cross-sell "de la Sección 5B"
> y esa sección no existía en el prompt. La lógica comercial se invocaba y nunca se definía.

Este chequeo tiene doble sentido: se verifica que lo invocado exista (referencia rota) y, del
lado del chequeo 4, que lo que existe siga siendo invocado por alguien (estructura huérfana).

Ayuda mecánica: `scripts/barrido.py` extrae las referencias y las contrasta contra los
encabezados reales, y marca placeholders casi duplicados.

---

### 6 · Chequeo de ámbito de cada regla

**Toda regla nueva debe declarar a qué caso aplica y a cuál no.** Una regla sin ámbito se
vuelve absoluta y produce conducta absurda fuera de su contexto.

Fórmula, para pegar dentro de la regla:

```
Aplica a: [casos]. No aplica a: [casos].
```

Disparador de alerta: si la regla usa **SIEMPRE**, **NUNCA**, **MÍNIMO**, **TODOS** o
**CUALQUIER**, el ámbito tiene que estar acotado de forma explícita. Un absoluto sin ámbito es
un bug esperando el turno correcto para aparecer.

> **Caso real (mínimo 2 opciones).** La regla de "mínimo 2 opciones" quedó como regla
> absoluta, sin acotarse a las recomendaciones. El agente mostraba dos modelos incluso cuando
> el cliente pedía uno solo.

---

### 7 · Chequeo de reconciliación entre rondas

Si dos correcciones de **rondas distintas** tocan el mismo punto, **gana la más reciente**
(regla ya vigente en el método). Lo que agrega este chequeo es que **la resolución tiene que
quedar DOCUMENTADA en la matriz**, para que el conflicto no se reabra en la ronda siguiente.

Procedimiento:

1. Antes de aplicar una fila, buscá en la matriz filas anteriores que toquen el mismo
   comportamiento o el mismo sector.
2. Si hay choque, resolvé por recencia.
3. Escribí la resolución en la matriz, en la fila nueva **y** en la vieja: qué manda ahora, qué
   queda derogado, por qué.

Sin ese registro, la ronda siguiente vuelve a discutir lo mismo y la corrección derogada puede
volver a entrar de contrabando.

> **Caso real (video en el primer mensaje).** Una fila pedía no adjuntar el video en la primera
> respuesta, y una fila posterior definió una secuencia que lo incluye al final del primer
> mensaje. Sin reconciliación explícita queda ambiguo para quien edite el prompt después, y se
> reabre.

---

## Cuándo se corre y qué pasa si falla

- Se corre **sobre el texto final**, después de escribir la corrección y **antes** de armar los
  bloques de entrega.
- Aplica a **cualquier** versión que salga de AUREA: completa o parcial. Una entrega parcial por
  excepción de placeholders también pasa por el barrido.
- Si algún chequeo falla: se corrige y **se vuelve a correr el barrido completo**, no solo el
  chequeo que falló. Una corrección puede romper otro chequeo.
- Recién con 7 de 7 en OK se arma la entrega y se completa el campo `Barrido de coherencia:
  OK (7/7)` en la cabecera de cada bloque.
- El resultado se vuelca en la **matriz de auditoría del cliente** (ver `03-matriz-auditoria.md`).

**No hay entrega "provisoria sin barrido".** Una versión sin barrido no es una versión: es un
borrador, y como tal no se manda al cliente ni se carga en Prometheo.
