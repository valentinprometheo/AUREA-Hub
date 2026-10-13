# Protocolo de Extensión de la Metodología

> Cómo agregar o modificar contenido de la metodología AUREA × Prometheo **sin tener que
> rehacerla**. Leer antes de incorporar cualquier cambio al ZIP.

---

## El principio: una sola fuente de verdad

Cada pieza de información de la metodología vive en **un solo archivo** — su *fuente*.
Todos los demás archivos que necesiten esa información la **referencian** (apuntan a la
fuente), no la **copian**.

Cuando un dato está copiado en varios lados, cada cambio obliga a sincronizar todas las
copias, y si una se olvida, el ZIP se contradice. Cuando hay una sola fuente y el resto son
punteros, cambiar la fuente actualiza todo de una.

**Regla práctica:** antes de escribir algo, preguntarse "¿esto ya está dicho en otro
archivo?". Si sí, no lo copies — apuntá a ese archivo.

---

## Cómo se ve un puntero

Un archivo que referencia en vez de copiar dice algo como:

> "El Doc 3 se arma según el template `doc3-accesos-documentacion-template.md` — esa es la
> fuente de verdad de qué categorías lo componen. No re-listar acá su contenido."

Y se queda **solo con lo que es propio de ese archivo** (en el ejemplo: quién genera el
Doc 3, la regla anti-duplicación). Lo que pertenece a la fuente, no se repite.

---

## Distinguir lo estable de lo que cambia seguido

Dentro de un mismo archivo conviven cosas de dos tipos:

- **Estable** — casi nunca cambia. Ej: "el Discovery tiene 3 documentos vivos", "una sola
  Smart Tag activa por conversación".
- **Extensible** — cambia seguido. Ej: las categorías de material del Doc 3, la lista de
  reglas de diseño, los bloques del Discovery.

Lo extensible se mantiene en una **sección propia, claramente delimitada**, de modo que
agregar un ítem sea agregar a una lista — sin tocar el resto del archivo. Si lo estable y
lo extensible están mezclados, cada cambio chico obliga a releer todo.

**Ejemplo de la distinción aplicada:** en el módulo `guia-metodologica.md`, el texto del
Documento 3 separa la *afirmación canónica* ("Es el inventario de todo el material que el
agente va a necesitar") — fija — de la *enumeración de ejemplos* ("brochures, fichas,
planos...") — adaptable. La afirmación no se toca nunca; la enumeración se actualiza desde
el template del Doc 3.

---

## Tabla de cambios comunes — fuente y punteros a verificar

Para cada tipo de cambio: cuál es el archivo-fuente que se edita, y qué punteros hay que
verificar que sigan alineados.

| Tipo de cambio | Archivo-fuente (se edita) | Punteros a verificar |
|---|---|---|
| Agregar / cambiar una **categoría de material del Doc 3** | `01-ETAPA1-Discovery/02-PASO2-Discovery/doc3-accesos-documentacion-template.md` | Archivo `estructura-discovery.md` (fuente única) (debe decir "según el template", no re-listar) · módulo `guia-metodologica.md` de `prometheo-docs-kickoff` (la enumeración de ejemplos del Documento 3) |
| Agregar / cambiar un **bloque del Discovery** | Archivo `estructura-discovery.md` (fuente única) | Skills verticales (slots del bloque) · `02-ETAPA2-Diseno/02-trazabilidad-etapa1-etapa2.md` · skills de formulario por rubro |
| Agregar / cambiar una **regla de diseño Prometheo** | `02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` | `08-reglas-integracion-catalogo.md` (si es regla de catálogo) · skills verticales (tabla de aplicación de reglas) · skill `prometheo-etapa2-design` |
| Agregar / cambiar una **restricción de plataforma** | `02-ETAPA2-Diseno/restricciones-plataforma-prometheo.md` | `03-reglas-diseno-prometheo-by-aurea.md` · `framework-seguimientos.md` |
| Agregar una **skill nueva** | La carpeta de la skill (`SKILL.md` + módulos), dentro de la carpeta de etapa que corresponda (`02-skills/01-ETAPA1/`, `02-ETAPA2/`, etc., o `00-TRANSVERSAL/` si aplica a varias) | `README.md` (descripción de 5 bullets + árbol de skills) · `CHANGELOG.md` · README de la carpeta de etapa · skill orquestadora de la etapa (`prometheo-etapa1`, etc.) |
| Agregar un **rubro / vertical nuevo** | `06-rubros/0X-[rubro].md` + skills `prometheo-vertical-[rubro]` y `prometheo-formulario-[rubro]` | `README.md` · `00-INDEX.md` · `prometheo-etapa1` (lista de rubros) · `00-INDEX-referentes.md` |
| Agregar una **convención visual / de naming** | `07-convenciones-aurea/` (el archivo que corresponda) | `04-convenciones-docx-cliente.md` · skill `prometheo-crm-graphics` · skill `prometheo-etapa2-design` |
| Agregar un **caso de referencia** | `08-casos-referencia/` (carpeta o archivo del caso) | `README.md` · `00-INDEX-referentes.md` (solo si es referente de diseño de CRM, no si es de documentos) |

> Esta tabla no es exhaustiva. Si un cambio no encaja en ninguna fila, el criterio es el
> mismo: identificar la fuente, dejar el resto como punteros, registrar el cambio en el
> `CHANGELOG.md`.

---

## Checklist para incorporar un cambio

1. **Identificar la fuente.** ¿En qué único archivo vive (o debería vivir) esta información?
2. **Editar solo la fuente.**
3. **Verificar los punteros.** Buscar dónde más se menciona el tema (`grep` por palabras
   clave). Donde haya una *copia*, convertirla en *puntero* a la fuente.
4. **Migración oportunista.** Si al verificar punteros encontrás un archivo con una copia
   vieja y lo estás tocando igual, dejalo como puntero — no hace falta un refactor aparte.
5. **Registrar en el `CHANGELOG.md`.** Toda extensión queda anotada con su versión.
6. **Bump de versión** si el cambio es estructural (skill nueva, rubro nuevo, carpeta nueva).

---

## Caso resuelto — primer ejemplo (v1.5)

**Cambio:** agregar la categoría "Conversaciones de referencia" (Ideales / NO Ideales) al
Doc 3 del Discovery.

Cómo se ejecutó siguiendo este protocolo:

1. **Fuente identificada:** `doc3-accesos-documentacion-template.md` — es el archivo que
   define qué hay en el Doc 3.
2. **Se editó solo la fuente:** se agregó la categoría 5 (Conversaciones de referencia, con
   sub-bloques Ideales y NO Ideales, formatos `.txt` y `.jpg/.png`), la carpeta
   correspondiente en la estructura Drive, y una línea en "material recomendado".
3. **Punteros verificados y convertidos:**
   - Archivo `estructura-discovery.md` (fuente única) tenía una **copia** de la estructura del Doc 3
     (lista de 5 secciones). Se reemplazó por un puntero: "el Doc 3 se arma según el
     template". La skill quedó solo con lo propio (quién genera, regla anti-duplicación).
   - Módulo `guia-metodologica.md`: el texto del Documento 3 se separó en afirmación
     canónica (fija) + enumeración de ejemplos (adaptable, que ahora incluye conversaciones
     y se deriva del template).
4. **Resultado:** la próxima vez que se sume una categoría al Doc 3, se toca **un solo
   archivo** (el template) y se verifica que los 2 punteros sigan diciendo "según el
   template" — sin reescribir nada.

---

## Caso resuelto — segundo ejemplo (v1.6)

**Cambio:** reorganizar `02-skills/` por etapa + agregar la skill `prometheo-diseno-agente-ia-feedback`.

Cómo se ejecutó:

1. **Reorganización:** las carpetas de `02-skills/` pasaron de agruparse por tipo
   (`00-skill-principal/`, etc.) a agruparse por etapa (`00-TRANSVERSAL/`, `01-ETAPA1/`,
   `02-ETAPA2/`, `03-ETAPA3/`, `04-ETAPA4/`, `05-templates/`).
2. **Punteros verificados:** un `grep` por las rutas viejas detectó todos los archivos que
   las referenciaban (archivos de metodología + README + `project-instructions-universal`).
   Cada ruta se actualizó a la nueva ubicación.
3. **Skill nueva:** `prometheo-diseno-agente-ia-feedback` se creó directamente en
   `02-ETAPA2/`. Su fuente de verdad metodológica es `protocolo-feedback-demo.md`.
4. **Registro:** README, `00-INDEX.md` y `CHANGELOG.md` actualizados; READMEs nuevos en
   cada carpeta de etapa.

**Lección:** una reorganización de carpetas rompe rutas. El paso clave es el `grep` por las
rutas viejas — sin eso, quedan punteros rotos. Toda mención de ruta es un puntero a
verificar.
