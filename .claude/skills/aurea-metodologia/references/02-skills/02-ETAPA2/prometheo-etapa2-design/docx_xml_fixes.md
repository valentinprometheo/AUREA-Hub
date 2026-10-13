# MÓDULO: FIXES XML DEL DOCX

Conocimiento técnico crítico aprendido durante la implementación del DOCX de MIA.
Sin estos fixes, el preview de Claude.ai falla con "Failed to load document".

---

## PROBLEMA RAÍZ

`python-docx` genera DOCX que abren bien en Word/LibreOffice pero el preview
server de Claude.ai NO los soporta. La causa raíz tiene 3 componentes:

### 1. `styles.xml` inflado (CAUSA PRINCIPAL)
- python-docx mete una librería gigante de estilos legacy default
- Tamaño típico: **341 KB**
- DOCX que sí renderizan: `styles.xml = 4-10 KB` (de Google Docs o Word minimalista)

### 2. `stylesWithEffects.xml` (legacy de Office 2010)
- Tamaño típico: **428 KB**
- Es archivo legacy que no se necesita
- Hay que eliminarlo y limpiar referencias en `Content_Types.xml` y `rels`

### 3. Tablas anidadas
- `<w:tbl>` dentro de otro `<w:tbl>` rompe el renderer
- `max_depth = 1` es la regla
- Si necesitás 2 columnas, usá UNA tabla 1×2 con celdas grandes

---

## SOLUCIÓN: FIXER POST-PROCESO

El fixer toma el DOCX que `python-docx` generó y lo procesa para hacerlo
compatible con el preview de Claude.

### Pasos del fixer

1. **Reemplazar `word/styles.xml`** por uno minimal (4-10 KB)
2. **Eliminar `word/stylesWithEffects.xml`** completo
3. **Limpiar `[Content_Types].xml`** quitando el Override de stylesWithEffects
4. **Limpiar `word/_rels/document.xml.rels`** quitando la Relationship a stylesWithEffects
5. **Fix zoom** en `word/settings.xml`: agregar `w:percent="100"` al elemento `w:zoom`
6. **Reordenar children** de `tcPr` y `tblPr` según OOXML strict order (algunos
   parsers son estrictos con el orden)

### Código del fixer (Python con lxml + zipfile)

```python
import zipfile, shutil, os, re
from lxml import etree

NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

TCPR_ORDER = [
    'cnfStyle', 'tcW', 'gridSpan', 'hMerge', 'vMerge',
    'tcBorders', 'shd', 'noWrap', 'tcMar', 'textDirection',
    'tcFitText', 'vAlign', 'hideMark', 'headers', 'cellIns',
    'cellDel', 'cellMerge', 'tcPrChange',
]
TBLPR_ORDER = [
    'tblStyle', 'tblpPr', 'tblOverlap', 'bidiVisual',
    'tblStyleRowBandSize', 'tblStyleColBandSize', 'tblW', 'jc',
    'tblCellSpacing', 'tblInd', 'tblBorders', 'shd', 'tblLayout',
    'tblCellMar', 'tblLook', 'tblCaption', 'tblDescription', 'tblPrChange',
]


def fix_zoom(xml_str):
    return xml_str.replace(
        '<w:zoom w:val="bestFit"/>',
        '<w:zoom w:val="bestFit" w:percent="100"/>'
    )


def reorder_children(parent, order_list):
    children = list(parent)
    if not children: return
    def sort_key(child):
        tag = child.tag.replace(W, '')
        return order_list.index(tag) if tag in order_list else 9999
    sorted_children = sorted(children, key=sort_key)
    if [c.tag for c in children] == [c.tag for c in sorted_children]:
        return
    for c in children: parent.remove(c)
    for c in sorted_children: parent.append(c)


def fix_document_xml(xml_bytes):
    parser = etree.XMLParser(remove_blank_text=False)
    tree = etree.fromstring(xml_bytes, parser)
    for tcPr in tree.iter(W + 'tcPr'):
        reorder_children(tcPr, TCPR_ORDER)
    for tblPr in tree.iter(W + 'tblPr'):
        reorder_children(tblPr, TBLPR_ORDER)
    return etree.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone=True)


def fix_docx(input_path, minimal_styles_bytes):
    """
    minimal_styles_bytes: bytes del styles.xml minimal (típicamente 4-10 KB).
    Extraer del DOCX referencia que sí renderiza, o usar el incluido en la skill.
    """
    tmp_path = input_path + '.tmp'

    with zipfile.ZipFile(input_path, 'r') as zin:
        with zipfile.ZipFile(tmp_path, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.namelist():
                # Eliminar stylesWithEffects.xml
                if item == 'word/stylesWithEffects.xml':
                    continue

                data = zin.read(item)

                # Reemplazar styles.xml
                if item == 'word/styles.xml':
                    data = minimal_styles_bytes
                # Fix zoom en settings
                elif item == 'word/settings.xml':
                    data = fix_zoom(data.decode('utf-8')).encode('utf-8')
                # Reordenar elementos en document.xml
                elif item == 'word/document.xml':
                    data = fix_document_xml(data)
                # Limpiar Content_Types
                elif item == '[Content_Types].xml':
                    text = data.decode('utf-8')
                    text = text.replace(
                        '<Override PartName="/word/stylesWithEffects.xml" '
                        'ContentType="application/vnd.ms-word.stylesWithEffects+xml"/>',
                        ''
                    )
                    data = text.encode('utf-8')
                # Limpiar rels
                elif item == 'word/_rels/document.xml.rels':
                    text = data.decode('utf-8')
                    text = re.sub(
                        r'<Relationship\s+[^>]*Target="stylesWithEffects\.xml"[^>]*/>',
                        '', text
                    )
                    data = text.encode('utf-8')

                zout.writestr(item, data)

    shutil.move(tmp_path, input_path)
    size = os.path.getsize(input_path) / 1024
    print(f"✓ Optimizado: {input_path} ({size:.0f} KB)")
```

---

## STYLES.XML MINIMAL DE REFERENCIA

El styles.xml minimal que sabemos que funciona se puede obtener de cualquier DOCX
de Google Docs (descargar como .docx y extraer styles.xml del zip). Tiene típicamente
estos estilos:

- `Normal` (default)
- `Title`, `Heading1` a `Heading6`
- `Strong`, `Emphasis`
- `ListParagraph`
- `Hyperlink`
- `FootnoteReference`, `FootnoteText`
- `EndnoteReference`, `EndnoteText`
- `CommentReference`, `CommentText`
- `TableNormal`, `TableGrid`

Tamaño total: **4.7 KB** aproximadamente.

**Estrategia recomendada para la skill:**
- Tener el archivo `styles_minimal.xml` incluido en la skill como recurso
- O bien, generar uno mínimo programáticamente (más frágil)
- O bien, extraerlo de un DOCX referencia siempre disponible en el proyecto

---

## VALIDACIÓN ANTES DE ENTREGAR

Después del fixer, verificar:

### 1. OOXML válido
```bash
python3 /mnt/skills/public/docx/scripts/office/validate.py archivo.docx
# Debe imprimir "All validations PASSED!"
```

### 2. No hay tablas anidadas
```python
import zipfile, re
with zipfile.ZipFile('archivo.docx') as z:
    content = z.read('word/document.xml').decode('utf-8')
depth = max_depth = nested = 0
for m in re.finditer(r'(<w:tbl(?:\s|>))|(</w:tbl>)', content):
    if m.group(1):
        depth += 1
        if depth > 1: nested += 1
        if depth > max_depth: max_depth = depth
    else:
        depth -= 1
assert max_depth == 1, f"Tablas anidadas detectadas: max_depth={max_depth}"
```

### 3. styles.xml no está inflado
```python
import zipfile
with zipfile.ZipFile('archivo.docx') as z:
    info = z.getinfo('word/styles.xml')
    assert info.file_size < 50_000, f"styles.xml inflado: {info.file_size} bytes"
```

### 4. Peso total razonable
```python
import os
size = os.path.getsize('archivo.docx') / 1024
assert size < 1500, f"DOCX muy pesado: {size:.0f} KB"
# Ideal: < 800 KB. Aceptable: < 1500 KB.
```

---

## TROUBLESHOOTING — CASOS QUE VIMOS

### Caso 1: Preview falla pero Word abre bien
Causa típica: styles.xml inflado o stylesWithEffects.xml presente.
Solución: aplicar el fixer.

### Caso 2: Validación OOXML pasa pero preview falla
Causa típica: tablas anidadas (max_depth > 1).
Solución: rediseñar como tabla única con celdas merged.

### Caso 3: Preview falla con DOCX < 100 KB
Causa típica: encoding XML mal formado, caracteres especiales sin escapar.
Solución: validar con `xmllint --noout document.xml` y arreglar.

### Caso 4: Preview funciona pero abre vacío
Causa típica: zoom mal configurado.
Solución: agregar `w:percent="100"` al elemento `w:zoom` en settings.xml.

---

## ALTERNATIVA: ENTREGAR PARA DESCARGA, NO PREVIEW

Si después de aplicar todos los fixes el preview sigue fallando, la decisión
estratégica es entregar el DOCX para que el cliente lo **descargue y abra en
Word/Google Docs**. El preview de Claude.ai es un renderer limitado, no es el
destino real del documento.

En ese caso:
- Confirmar que el DOCX abre bien en Word/Google Docs
- Documentar al cliente que descargue el archivo en lugar de previsualizar
- Considerar entregar también una versión PDF como respaldo

---

## GENERACIÓN CON LIBRERÍA `docx` DE NODE.JS (alternativa a python-docx)

Hallazgo de G&D: la librería `docx` de Node mantiene `styles.xml` chico (~4 KB)
de entrada, sin necesidad del fixer de styles. Es una alternativa válida a
python-docx.

Reglas si se usa Node `docx`:
- **`ImageRun` requiere `type: "png"`** en docx v9.x. Sin ese parámetro, la
  imagen no se embebe (falla silenciosa: el archivo se genera pero sin la imagen).
- **`ImageRun` debe venir del MISMO módulo `docx`** que `Document`/`Packer`. Si
  se importa de una instancia de require distinta, la imagen se pierde aunque el
  código sea correcto. Reexportar todo desde un único helper.

---

## BUG CRÍTICO: TEXTO EN VERTICAL EN GOOGLE DOCS

Hallazgo de G&D, vale para CUALQUIER DOCX que vaya a abrirse en Google Docs.

**Síntoma:** las tablas con ancho en porcentaje pero **sin ancho de columna
absoluto** se renderizan bien en Word y en el preview, pero **Google Docs
colapsa la columna y apila el texto carácter por carácter en vertical.**

**Solución — toda tabla necesita los tres atributos:**
1. `layout = fixed`
2. `tblGrid` con el ancho de cada columna en twips
3. ancho de celda (`tcW`) en DXA (twips absolutos), NO en porcentaje

**Regla permanente:** anchos de columna en DXA + layout fixed siempre, nunca
solo porcentaje, si el documento va a abrirse en Google Docs.

Referencia de ancho: **ancho útil A4 con márgenes de 2 cm ≈ 9026 twips.**
Repartir ese total entre las columnas según proporción deseada.

En python-docx esto se traduce a:
- Setear `table.allow_autofit = False`
- Setear `table.alignment` y anchos absolutos por celda con `cell.width = Cm(x)`
- Verificar que el `tblGrid` tenga los anchos en el XML final

---

## VERIFICAR SIEMPRE: 0 TABLAS ANIDADAS

Regla repetida por su importancia. Las tablas anidadas rompen el renderer del
preview. Verificar con el script de la sección de validación (max_depth == 1).
