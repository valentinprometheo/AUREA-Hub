# 05 · Documentación formal (legal, tipo NDA)

> Familia de output: NDAs, acuerdos de confidencialidad, contratos de servicios, anexos con cláusulas, cartas acuerdo, cualquier documento institucional con estructura jurídica. Formato `.docx`. Estética congelada en el template oficial: tipografía Calibri, violeta de marca, header con logo, barras de sección, tabla de Condiciones Comerciales, bloque FIRMAS. **No inventar otra estética: esta es la única para esta familia.**

Las reglas transversales (voseo, cero em-dashes, AUREA sin tilde) viven en el SKILL.md del conductor; acá están las reglas **propias de esta familia**, empezando por la fundamental.


Producí NDAs, acuerdos de confidencialidad, contratos y documentos legales
formales de marca AUREA partiendo del `.docx` oficial. La estética está
congelada en el template: no se reconstruye, se edita.

## La regla fundamental

**Nunca reconstruir el documento con docx-js, python-docx u otra librería que
escriba `.docx` desde cero.** Toda reconstrucción introduce desvíos en
tipografía (Calibri se renderiza distinto que Arial), pesos de fuente, colores
exactos, micro-tipografía y elementos no obvios (la firma de Magalí escaneada
y pegada en su tarjeta, los `<w:rsid>` que Google Docs respeta, los pPr
specíficos de cada párrafo). El template existe en
`assets/nda/NDA-AUREA-template-base.docx` y es la única fuente de verdad de la
estética. La skill edita ese XML quirúrgicamente.


## Flujo de trabajo obligatorio

```
1. Copiar el template a /home/claude/original.docx
   cp assets/nda/NDA-AUREA-template-base.docx /home/claude/original.docx

2. Unpack
   python /mnt/skills/public/docx/scripts/office/unpack.py original.docx unpacked/

3. Identificar zonas a modificar en unpacked/word/document.xml
   grep -n "MARKER UNICO" unpacked/word/document.xml

4. Editar con script Python o str_replace
   - Cambios chicos (fechas, nombres): str_replace directo
   - Cambios estructurales (tablas, cláusulas enteras): script Python con re

5. Pack preservando metadata original
   python /mnt/skills/public/docx/scripts/office/pack.py unpacked/ output.docx --original original.docx

6. QA visual OBLIGATORIO antes de entregar
   python /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf output.docx
   pdftoppm -jpeg -r 95 output.pdf page
   # Revisar cada página, especialmente: portada, cláusula modificada, firmas

7. Copiar a /mnt/user-data/outputs/ y present_files
```

## Tokens de diseño extraídos del template

Estos valores están en el XML real del template, NO inventarlos:

| Elemento | Fuente | Tamaño (half-points) | Color | Peso | Itálica |
|---|---|---|---|---|---|
| Cuerpo de cláusula | Calibri | 21 (10.5pt) | `#0d1f2d` | normal | no |
| Encabezado de cláusula ("CLÁUSULA X. TÍTULO") | Calibri | 22 (11pt) | `#9900ff` | bold | no |
| Letras de lista a) b) c) | Calibri | 21 | `#9900ff` | bold | no |
| Header de tabla | Calibri | 22 | `#FFFFFF` sobre fondo `#9966ff` | bold | no |
| Columna principal de tabla (Concepto / Descripción) | Calibri | 22 | `#000000` | bold | no |
| Columnas auxiliares (Cant., Forma, Fecha) | Calibri | 22 | `#555555` | normal | sí |
| Subtítulos en violeta ("Resumen de inversión") | Calibri | 22 | `#9900ff` | bold | no |
| Notas debajo de tabla (tipo de cambio, IVA) | Calibri | 20 | `#555555` | normal | sí |
| Cierre "se suscribe en DOS (2) ejemplares" | Calibri | 22 | `#555555` | normal | sí |
| FIRMAS (título centrado) | Calibri | 24 | `#0D1F2D` | bold | no |
| Texto de tarjeta de firma (nombre y cargo) | Calibri | 21 | `#0d1f2d` | mixto | no |

**Otros tokens estructurales:**
- Indent de incisos a/b/c: `<w:ind w:left="500" w:firstLine="0"/>`
- Spacing entre incisos: `<w:spacing w:after="100" w:line="260" w:lineRule="auto"/>`
- Spacing entre cláusulas: `<w:spacing w:after="100" w:before="300" w:lineRule="auto"/>`
- Justificación cuerpo: `<w:jc w:val="both"/>`
- Bordes de tabla: `single`, size `8`, color `#000000`
- Línea horizontal divisoria: color `#9999ff`, size `6`, single

Detalle completo en `references/documentacion-formal-tokens.md`.

## Anatomía del documento (orden fijo)

1. **Header**: tabla 2 columnas, logo wordmark izquierda + bloque título derecha (sin caja contenedora). Título "ACUERDO DE CONFIDENCIALIDAD" en violeta `#9900ff` bold, subtítulo "Non-Disclosure Agreement — Prometheo CRM" en itálica gris, fecha "Buenos Aires, X de Mes 20XX".
2. **Línea horizontal divisoria** (`#9999ff`).
3. **"Entre las partes que a continuación se identifican:"**
4. **Barra "PARTE DIVULGANTE..."** + **caja de detalle** con labels en violeta + valores en negro.
5. **Barra "PARTE RECEPTORA — CLIENTE"** + **caja de detalle** con lista numerada de empresas.
6. **Conjunción**: "AUREA HUB y el Cliente serán referidos conjuntamente como las 'Partes'..."
7. **Línea horizontal divisoria** (cierre de zona de partes).
8. **CONSIDERANDOS** (I, II, III, IV en violeta bold).
9. **Línea centrada**: "ACUERDO DE CONFIDENCIALIDAD Y NO DIVULGACIÓN" + línea horizontal abajo.
10. **Cláusulas Primera a Décima** (encabezado violeta bold + cuerpo justificado + incisos con letra en violeta cuando aplica).
11. **Cláusula Undécima: Condiciones Comerciales** (subtítulo "Resumen de inversión" + tabla(s) + notas en itálica gris).
12. **Línea horizontal divisoria** (separación con FIRMAS).
13. **FIRMAS** (título centrado + dos tarjetas: Parte Divulgante / Parte Receptora).
14. **Cierre en itálica gris centrado**: "El presente instrumento se suscribe en DOS (2) ejemplares..."
15. **Línea horizontal divisoria** final.

## Zonas editables más comunes

### Datos del cliente (Parte Receptora)
- Razones sociales, CUITs, domicilios, nombre del representante, DNI, email.
- Localizar la `<w:tbl>` que contiene "La Parte Receptora está integrada" y editar las filas correspondientes manteniendo el `<w:tcPr>` y `<w:pPr>` originales.

### Considerando II (objeto del Acuerdo)
- Si el cliente tiene varias unidades de negocio (caso EDFAN: real estate + mobiliario + productos + revestimientos), ampliar "proyectos inmobiliarios" a "distintas unidades de negocio" enumerando.

### Cláusula Quinta (Protección de Datos)
- Reemplazar el bloque entero por la versión Prometheo/ITESA/GDPR cuando el cliente lo pida.
- Ver `scripts/edit_clause_5_proteccion_datos.py` como referencia.

### Cláusula Undécima (Condiciones Comerciales)
- Lo que más cambia entre clientes. Cada uno tiene su estructura: pago único, abono mensual recurrente, varias sociedades facturantes, echeqs, etc.
- Marker único para localizar: la `<w:tbl>` que contiene "USD 149" (la única del documento).
- Reemplazar desde la apertura de esa `<w:tbl>` hasta el cierre del `<w:p>` que contiene "La suscripción mensual a Prometheo".
- Mantener el subtítulo "Resumen de inversión" intacto.
- Ver `scripts/edit_clause_11_condiciones_comerciales.py` como referencia.

### Fechas
- Aparecen en 3 lugares: título ("Buenos Aires, X de Mes 20XX"), pie de firma de la Parte Divulgante, pie de firma de la Parte Receptora. Unificar las tres con `str_replace` cuidadoso.

### Nombre del representante en la firma de la Parte Receptora
- Editar el `<w:p>` dentro de la tarjeta de la Parte Receptora con el nuevo nombre, DNI y carácter del firmante.

## Reglas no negociables AUREA

- **Voseo rioplatense** en cuerpo redactado por nosotros.
- **Cero em-dashes (—)** en texto nuevo que generemos. El template original tiene em-dashes en algunas barras ("ÁUREA HUB", "Non-Disclosure Agreement —"), no los corregimos en zonas que el cliente ya validó. Pero en cláusulas nuevas que escribamos: cero em-dashes.
- **AUREA sin tilde** en cuerpo nuevo. En las barras de sección heredadas del template original aparece "ÁUREA HUB" con tilde, decisión del cliente sobre su propio template, no tocar a menos que Valentín lo pida explícito.
- **Nombres correctos**: Magalí Domínguez (con tilde), Valentín Zas, Sebastián Mato.
- **Placeholders en rojo bold** (`<w:color w:val="C00000"/>` + `<w:b/>`, texto entre corchetes, ej. `[A COMPLETAR: fecha]`). NUNCA usar `highlight: "yellow"`, rompe la validación XML schema (`highlightCs` element error).
- **Montos**: confirmados reales tal cual, sugeridos con "(sugerido)", desconocidos en rojo. Jamás inventar.
- **No mencionar handoff de tarjeta de crédito** ni medios de pago internos de AUREA en el cuerpo del documento. La columna "A quién se paga" o la cláusula de Facturación habilitan el split sin texto explícito.

## QA visual obligatorio

Antes de entregar, validar visualmente. **El rendering de LibreOffice
(`soffice`) NO es idéntico al de Google Docs.** Si Valentín reporta "se ve
distinto", subir el `.docx` a Google Drive y abrirlo en Google Docs antes de
asumir que hay un bug. Google Docs es el rendering real de uso.

Checklist:

- [ ] Portada idéntica al template original (no reconstruida).
- [ ] Tipografía Calibri en todo el documento.
- [ ] Encabezados de cláusula en violeta `#9900ff` bold.
- [ ] Letras a) b) c) en violeta bold dentro de las listas.
- [ ] Tabla de Condiciones Comerciales con header violeta pleno y texto blanco.
- [ ] Columnas auxiliares de tabla en itálica gris `#555555`.
- [ ] Notas debajo de tabla (tipo de cambio, IVA) en itálica gris.
- [ ] Bloque FIRMAS intacto (tarjetas con header violeta, firma de Magalí pegada).
- [ ] Fechas consistentes en título y ambos pies de firma.
- [ ] Validación de esquema OK (`validate.py` reporta `All validations PASSED!`).
- [ ] Conteo de párrafos coherente (no debe explotar; chequear delta con `pack.py`).
- [ ] Renderizar a PDF y revisar cada página con `pdftoppm -jpeg -r 95`.
- [ ] Recordar la advertencia de soffice vs Google Docs si reporta diferencias.

## Archivos de esta familia (dentro de la skill consolidada)

```
assets/nda/NDA-AUREA-template-base.docx   (template oficial, fuente de verdad de la estética)
scripts/edit_clause_5_proteccion_datos.py
scripts/edit_clause_11_condiciones_comerciales.py
scripts/README.md
references/documentacion-formal-tokens.md   (tabla detallada de tokens)
references/documentacion-formal-qa.md        (checklist QA + casos vistos)
```

## Aprendido a la mala

En las primeras iteraciones para EDFAN, reconstruí el NDA desde cero con
`docx-js` y Arial intentando emular el look del template a partir de
screenshots. Resultado: tres versiones con diferencias estéticas notables que
fueron rechazadas por Valentín. La quinta iteración partió del `.docx` real,
editó solo lo necesario, y matcheó al 100%. La lección queda codificada arriba
en "La regla fundamental": no reconstruir, editar.

Otra lección: cuando el QA visual del lado de Claude (soffice → PDF → JPEG)
muestra diferencias contra el original que Valentín ve en Google Docs, eso no
necesariamente significa que el archivo esté mal. Verificar el diff a nivel
XML antes de tocar nada: si las líneas modificadas son solo las que tenían
que cambiar, el archivo está bien y la diferencia es de rendering. En ese
caso, subir a Drive y dejar que Valentín verifique en su entorno.
