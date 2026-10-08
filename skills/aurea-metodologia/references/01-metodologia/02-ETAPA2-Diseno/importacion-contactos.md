---
consultar-cuando: Etapa 2/3, carga de base de contactos, cliente con base previa
disparadores: "importar contactos", "carga de base", "migrar contactos", "base legacy"
fuente-única-de: el proceso y disciplina de importación de contactos a Prometheo
combina-con: embudos-y-tags, restricciones-plataforma-prometheo, excel-carga-clientes
---

# Importación de contactos a Prometheo

> Procedimiento para cargar contactos en masa a Prometheo mediante Excel, y el orden de
> carga de toda la configuración del cliente (variables, tags, embudos, contactos).
> Aprendizajes de la implementación de AUREA Hub como cliente de Prometheo.

---

## Para qué sirve este archivo

La importación de contactos por Excel parece trivial y no lo es: tiene una plantilla
obligatoria, un formato de columnas estricto y varios fallos silenciosos que dejan datos
incompletos sin avisar. Este archivo fija el procedimiento para que la carga de un cliente
nuevo salga bien a la primera.

---

## El orden de carga — obligatorio

La configuración de un cliente en Prometheo se carga **siempre en este orden**:

1. **Variables** — crear todas las variables, cada una con su tipo y su decisión de prompt
   (IA) o manual.
2. **Tags** — crear todas las Smart Tags: las que serán etapa de embudo y las de
   visibilidad. Escritas con sus tildes correctas.
3. **Embudos** — crear los embudos, eligiendo qué tags son sus etapas y redactando la
   descripción que la IA usa para enrutar.
4. **Contactos** — recién ahora, importar el Excel de contactos.

El motivo: la importación solo puede **mapear a cosas que ya existen**. Si se importa antes
de tener variables, tags y embudos creados, el mapeo no tiene a qué apuntar y los datos
entran incompletos. El orden no es una recomendación — es una dependencia técnica.

> Este orden se apoya en la regla dura 5 de `embudos-y-tags.md` ("si la tag no está
> creada, la etapa no existe") y en las restricciones 17 y 18 de
> `restricciones-plataforma-prometheo.md`.

---

## La plantilla de importación

- La importación masiva se hace con un **Excel**.
- Hay que usar la **plantilla oficial** que se descarga desde la propia pantalla de
  importación de Prometheo. No se arma un Excel propio.
- No se cambian el formato ni los nombres de los encabezados (la primera fila).
- Los datos se vuelcan dentro de esa plantilla, una sola hoja.

### Campos

- **Nombre** y **Teléfono** son **obligatorios**. Un contacto sin teléfono no se puede
  importar.
- Las columnas de **variable** llevan el prefijo `var_` (ej. `var_empresa`,
  `var_prioridad`). Solo se pueden mapear a variables que ya existan en Prometheo.
- La **columna Tags**: varias tags se separan con el carácter barra vertical `|` —
  no con coma. Ejemplo: `En Conversación | Construcción`.
- La **etapa de embudo no se mapea como columna propia**. El contacto entra a la etapa que
  corresponda según la tag-etapa que traiga en la columna Tags.

---

## Comportamientos a tener en cuenta

### Las tags desconocidas se ignoran en silencio

Si el Excel trae una tag que no existe ya creada en la organización, Prometheo **no la crea
ni da error**: no la asigna y el contacto entra sin esa tag. No hay aviso. Antes de
importar, verificar que **todas** las tags del archivo existan, escritas de forma idéntica.

> El match de tags no distingue mayúsculas pero **sí distingue tildes** (restricción 16).
> `construccion` sin tilde es otra tag que `Construcción`. Una tilde de diferencia y la tag
> se ignora.

### Deduplicación por teléfono

Prometheo deduplica por número de teléfono. Si un contacto del Excel ya existe con ese
número, no lo duplica: lo informa como "ya existe" y lo omite. El resto se importa normal.

### Sin límite de cantidad

No hay límite de cantidad de contactos por importación.

### El problema "__EMPTY"

Al mapear columnas, algunas pueden aparecer como `__EMPTY`, `__EMPTY_1`, etc., en vez de su
nombre real. Ocurre cuando Prometheo no logra leer la fila de encabezados, o lee una hoja
equivocada. Se evita trabajando siempre sobre la plantilla oficial descargada, con una sola
hoja, encabezados en la primera fila y sin alterar el formato. Si el `__EMPTY` persiste con
un archivo aparentemente correcto, es un tema de plataforma: consultar al bot oficial.

---

## Reglas para la metodología

1. **Respetar el orden de carga:** variables → tags → embudos → contactos. Nunca importar
   antes de tener las tres primeras creadas.

2. **Trabajar siempre sobre la plantilla oficial** descargada de Prometheo. No armar un
   Excel propio con encabezados a gusto: un archivo con formato distinto puede no leerse.

3. **Verificar antes de importar** que todas las tags del archivo existan ya creadas en
   Prometheo, escritas idénticas (con tildes).

4. **Separar tags múltiples con `|`** en la columna Tags, nunca con coma.

5. **Separar los contactos en dos listas desde el inicio:** los que tienen teléfono
   (importables) y los que no (lista de trabajo aparte, hasta conseguir el número).

### Trampas a evitar

- **Armar un Excel propio** con formato y nombres de columna a gusto. Prometheo necesita su
  plantilla exacta.
- **Poner teléfonos falsos** a contactos sin número para "meterlos igual". Rompe la
  deduplicación (varios contactos con el mismo número se fusionan) y llena el CRM de
  contactos incontactables.
- **Asumir que una tag escrita distinto va a matchear.** Una tilde de diferencia y la tag
  se ignora sin aviso: el contacto entra incompleto.

---

## Checklist — antes de cargar un cliente nuevo

- [ ] Variables creadas, cada una con su tipo y su decisión de prompt (IA) o manual.
- [ ] Tags creadas: las de cada etapa de embudo y las de visibilidad, con tildes correctas.
- [ ] Embudos creados, con sus etapas elegidas entre las tags y su descripción redactada
      para la IA.
- [ ] Contactos separados en lista con teléfono y lista sin teléfono.
- [ ] Excel armado sobre la plantilla oficial, con tags separadas por `|`.
- [ ] Importación hecha al final, después de variables, tags y embudos.

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| `embudos-y-tags.md` | El orden de carga sale del modelo de Tags/Variables/Embudos (regla dura 5). |
| `restricciones-plataforma-prometheo.md` | Restricciones 16, 17 y 18 — la base técnica de este procedimiento. |
| `prometheo-etapa2-design` (skill) | El diseño del CRM define las variables, tags y embudos que después se cargan con este procedimiento. |
| Etapa 3 — Implementación | La carga efectiva en Prometheo es parte del lanzamiento — ver `03-ETAPA3-Lanzamiento/`. |

---

## Hallazgos de campo — confirmados en producción (v1.14)

> Ranura de extensión. Comportamientos de la importación observados con clientes reales.

### Disciplina de carga de base legacy (cuando el cliente trae base previa)

Confirmado en dos casos (G&D: 6.057 contactos migrados; BETROX: checklist formalizado). Antes de
migrar una base previa a Prometheo:

1. **Auditar qué columnas están realmente pobladas antes de migrar, no asumir.** Una columna que
   existe en el Excel no significa que tenga datos usables en la mayoría de las filas.
2. **No promover defaults masivos.** Si un valor está en el 100% de la base, no es una señal real
   de ese dato — es la ausencia de dato disfrazada de default. Migrar cada variable **solo** a los
   contactos con dato real; el resto queda vacío y el agente lo completa cuando el lead reengancha.
   No fuerces un valor "por si acaso".
3. **Preservar verbatim.** Línea, producto, modelo y canal se cargan con su valor natural
   existente, no se recodifican al importar.
4. **Extraer los valores distintos por columna y configurarlos como opciones ANTES del import**
   (modelos históricos, líneas o canales que aparezcan en la base), y comunicarlos al cliente
   antes de cargar — evita que la restricción de plataforma "tags desconocidas se ignoran en
   silencio" (ver `restricciones-plataforma-prometheo.md`, restricción 17) rompa la migración sin
   aviso.
5. **Sanear teléfonos:** formato E.164, 13 dígitos para móvil argentino (549 + 10 dígitos).
   Autocorregir solo typos inequívocos (el 15 redundante, el 9 faltante). Flaggear los ambiguos en
   una hoja aparte — nunca borrar un contacto por duda.
6. **QA final:** comparar el output contra la fuente campo por campo hasta cero mismatches.
   Cargar teléfonos siempre como texto — si Excel los toma como número, la notación científica
   rompe la carga.

Este checklist es reutilizable tal cual para cualquier cliente que traiga base previa, sin
importar el rubro.
