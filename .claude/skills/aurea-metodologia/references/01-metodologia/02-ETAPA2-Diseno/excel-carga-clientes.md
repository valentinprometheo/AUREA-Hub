# Excel de Carga de Clientes — el 4º output de Etapa 2

> El Excel/Sheets que el cliente recibe para volcar sus contactos antes del Go-Live.
> Es el 4º output de Etapa 2, junto con el DOCX de Diseño de CRM, el Prompt del agente y
> el Doc de Refactorización. Este archivo explica qué es, para qué sirve y cómo se conecta
> con el resto de la metodología. La ejecución técnica vive en la skill
> `prometheo-etapa2-design`, módulo `excel_carga_contactos.md`.

---

## Para qué sirve

Una vez aprobado el diseño del CRM, hay que cargar los contactos del cliente en Prometheo
antes del Go-Live. Cargarlos sin un Excel preparado lleva a leads incompletos, tags mal
escritas y dedups fallidos. El Excel de Carga resuelve esto con un formato único que el
cliente completa y que después se vuelca a Prometheo siguiendo el procedimiento de
`importacion-contactos.md`.

---

## Qué pieza es dentro de Etapa 2

| Output | Para quién | Formato | Qué contiene |
|---|---|---|---|
| DOCX de Diseño de CRM | Cliente | Word | El diseño del agente IA, visual y narrativo |
| Prompt del agente | Implementación | Markdown | El prompt redactado para Prometheo |
| Doc de Refactorización | Interno AUREA | DOCX/MD | Pendientes, inconsistencias, decisiones diferidas |
| **Excel de Carga** | **Cliente → AUREA** | **Excel + Sheets** | **La base de contactos del cliente lista para importar** |

---

## El conflicto Excel-de-trabajo vs Sheets-plano

El Excel y el Sheets cumplen funciones distintas y no deben confundirse:

- **Excel de trabajo (cliente):** el archivo que el cliente edita. Tiene 2 hojas:
  *INSTRUCCIONES* (cómo completar) y *LEADS* (la planilla con sus columnas). Tiene
  validaciones, dropdowns, formato.
- **Sheets plano (Prometheo):** la hoja de cálculo que Prometheo lee si la integración es
  Sheets en lugar de importación por Excel. **Plano: sin formatos, sin dropdowns, sin
  hojas auxiliares.** Solo datos crudos.

Estos dos artefactos pueden coexistir: el cliente trabaja sobre el Excel de trabajo, y
AUREA copia los datos al Sheets plano (o exporta el Excel y lo importa, según el cliente).

---

## Estructura del Excel de trabajo

### Hoja 1 — INSTRUCCIONES

Una sola hoja con explicación breve, sobria, redactada para el cliente:
- Para qué es este Excel.
- Qué columnas son obligatorias (Nombre, Teléfono).
- Cómo se separan las tags múltiples (`|`, no coma — ver `importacion-contactos.md`).
- Qué tags y variables existen creadas en Prometheo (con tildes correctas).
- Cómo entregar el archivo a AUREA.

### Hoja 2 — LEADS

Las columnas, en este orden:

| Columna | Notas |
|---|---|
| Nombre | Obligatorio |
| Teléfono | Obligatorio. Sin formato — número plano |
| Email | Opcional |
| Tags | Tags separadas por `\|`. Solo tags ya creadas en Prometheo |
| `var_*` (n columnas) | Una columna por variable. Prefijo `var_` obligatorio |

Validaciones a aplicar en la planilla del cliente:
- Teléfono como **número plano** (sin paréntesis, sin guiones, sin formato moneda ni
  miles). Esto es crítico: montos formateados o teléfonos con separadores no se importan
  bien.
- Dropdowns para las variables de tipo "Opciones" donde apliquen.
- Columna de Tags como texto libre (no dropdown — el cliente puede combinar varias).

### Hoja oculta o auxiliar — solo en el Excel de trabajo

Si el cliente necesita una hoja de referencia con las tags disponibles, las variables y
sus tipos, va como hoja auxiliar **solo en el Excel de trabajo**. **No** se exporta al
Sheets plano.

---

## El orden con el resto de Etapa 2

El Excel de Carga se genera **después** del DOCX de Diseño de CRM y del Prompt, porque
hereda de ambos:

1. El DOCX define qué tags y variables tendrá el cliente.
2. El Prompt confirma cómo se las usa.
3. El Excel se arma con esas tags y variables como columnas — no se inventan acá.

Si el diseño cambia (se agrega una variable, se renombra una tag), el Excel se regenera o
se actualiza puntualmente. Nunca el Excel introduce tags/variables nuevas que no estén en
el DOCX.

---

## Cómo se ejecuta

La generación concreta del Excel la hace la skill `prometheo-etapa2-design`, módulo
`excel_carga_contactos.md`. Ese módulo cubre el detalle técnico: estructura XLSX, cómo
generar el Sheets plano paralelo, validaciones, dropdowns, formato de teléfono y montos.

Este archivo (`excel-carga-clientes.md`) es el contexto metodológico: qué pieza es,
cuándo se genera, cómo se conecta con los otros outputs. El módulo de la skill es el
"cómo se hace".

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| `embudos-y-tags.md` | Las columnas del Excel reflejan las tags y variables del modelo de 3 capas. |
| `importacion-contactos.md` | El procedimiento de carga efectiva en Prometheo. Este archivo es el paso previo. |
| `prometheo-etapa2-design` (skill) | El módulo `excel_carga_contactos.md` ejecuta la generación. |
| Etapa 3 — Lanzamiento | El Excel se vuelca a Prometheo en Etapa 3, antes del Go-Live. |

---

## Hallazgos de campo — pendientes de incorporar

_(Sin hallazgos pendientes al cierre de v1.11.)_
