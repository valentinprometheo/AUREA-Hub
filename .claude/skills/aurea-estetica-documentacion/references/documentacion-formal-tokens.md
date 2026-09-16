# Design Tokens, NDA AUREA

Valores extraídos directamente del XML del template oficial
(`template/NDA-AUREA-template-base.docx`). Usar estos valores tal cual cuando
se genere XML nuevo. No improvisar ni redondear.

## Paleta de colores

| Token | Hex | Uso |
|---|---|---|
| `--purple-deep` | `#9900ff` | Encabezados de cláusula, letras de incisos, subtítulos en violeta, borde inferior de header |
| `--purple-fill` | `#9966ff` | Fondo de header de tabla y barras de sección |
| `--ink-body` | `#0d1f2d` | Texto del cuerpo de cláusulas y párrafos, título FIRMAS |
| `--ink-default` | `#000000` | Columna principal de tablas (Concepto/Descripción), texto de cierre, contenido de placeholder |
| `--grey-italic` | `#555555` | Columnas auxiliares de tabla, notas en itálica debajo de tablas, frase de cierre "se suscribe en DOS (2)..." |
| `--white` | `#FFFFFF` | Texto sobre header de tabla y barras de sección violeta |
| `--shell-light` | `#ECE3F8` aprox | Fondo de cajas de detalle (Parte Divulgante / Receptora) |
| `--card-grey` | `#F4F4F6` aprox | Fondo de cuerpo de tarjetas de firma |
| `--hr-line` | `#9999ff` | Líneas horizontales divisorias |
| `--placeholder-red` | `#C00000` | Placeholders pendientes de completar (`[A COMPLETAR: ...]`) |

Nota sobre `--purple-deep` vs `--purple-fill`: el template usa `#9900ff` para
texto sobre fondo blanco (encabezados, subtítulos) y `#9966ff` para fondos de
elementos rellenos (barras y headers de tabla). Si se confunden los dos, el
contraste se rompe.

## Tipografía

**Fuente única**: Calibri (con `<w:rFonts w:ascii="Calibri" w:cs="Calibri" w:eastAsia="Calibri" w:hAnsi="Calibri"/>`).

| Elemento | `<w:sz>` half-points | Equivalente pt | Estilo |
|---|---|---|---|
| Cuerpo de cláusula | 21 | 10.5pt | Regular |
| Encabezado de cláusula | 22 | 11pt | Bold, color `#9900ff` |
| Subtítulo violeta ("Resumen de inversión") | 22 | 11pt | Bold, color `#9900ff` |
| Header de tabla | 22 | 11pt | Bold, color `#FFFFFF` |
| Columna principal de tabla | 22 | 11pt | Bold |
| Columnas auxiliares de tabla | 22 | 11pt | Italic, color `#555555` |
| Notas debajo de tabla | 20 | 10pt | Italic, color `#555555` |
| Cierre del documento | 22 | 11pt | Italic, color `#555555` |
| FIRMAS (título) | 24 | 12pt | Bold, color `#0D1F2D` |
| Nombre en tarjeta de firma | 21 | 10.5pt | Bold |
| Cargo/lugar en tarjeta de firma | 21 | 10.5pt | Regular |
| Encabezado "Buenos Aires, X de Mes" | 20 | 10pt | Italic, gris |

## Spacing y layout

```xml
<!-- Encabezado de cláusula: separa de cláusula anterior -->
<w:spacing w:after="100" w:before="300" w:lineRule="auto"/>

<!-- Párrafo introductorio de cláusula: justificado -->
<w:spacing w:after="140" w:line="280" w:lineRule="auto"/>
<w:jc w:val="both"/>

<!-- Inciso a/b/c con sangría izquierda -->
<w:spacing w:after="100" w:line="260" w:lineRule="auto"/>
<w:ind w:left="500" w:firstLine="0"/>
<w:jc w:val="both"/>

<!-- Línea horizontal divisoria (en pPr) -->
<w:pBdr>
  <w:bottom w:color="9999ff" w:space="1" w:sz="6" w:val="single"/>
</w:pBdr>
```

## Tabla de Condiciones Comerciales

Estructura del template original (5 columnas):

| Columna | Ancho DXA | Alineación | Estilo |
|---|---|---|---|
| Concepto | 2760 | Left | Calibri 22, bold, color `#000000` |
| Monto | 1740 | Center | Calibri 22, regular |
| Forma de pago | 1575 | Center | Calibri 22, italic, color `#555555` |
| Fecha para pagar | 2385 | Center | Calibri 22, italic, color `#555555` |
| A quién se paga | 1485 | Center | Calibri 22, italic, color `#555555` |

Total: 9945 DXA.

Header:
- Fondo: `#9966ff`
- Texto: `#FFFFFF`, Calibri 22, bold, centrado
- Borde: single, sz 8, color `#000000`

Filas de datos:
- Fondo: blanco
- Borde: single, sz 8, color `#000000`

**Variante 4 columnas** (usada en EDFAN para reflejar la estructura real de
imagen 2 del cliente): Descripción / Cant. / Precio Unit. / Subtotal, anchos
`[4500, 1200, 1900, 2360]`, mismos estilos.

**Variante "Total general"** (1 fila, 2 columnas): ambas celdas con fondo
`#9966ff`, texto blanco bold, izquierda alineada a la izquierda, derecha
alineada a la derecha.

## Cajas de detalle (Parte Divulgante / Parte Receptora)

Tabla de 1 celda full-width:
- Fondo: `#ECE3F8` (aprox)
- Borde: ninguno visible (puede tener borde nulo o transparente)
- Padding interno: top/bottom 200 DXA, left/right 240 DXA
- Labels (Denominación:, Representantes:, Domicilio:, etc.): Calibri 21, bold, color `#9900ff`
- Valores: Calibri 21, regular, color `#0d1f2d`

## Bloque FIRMAS

Tabla de 2 columnas con padding entre cajas. Cada caja es a su vez:
- Header: 1 celda con fondo `#9966ff`, texto blanco bold Calibri 22, centrado ("PARTE DIVULGANTE" / "PARTE RECEPTORA — CLIENTE").
- Cuerpo: 1 celda con fondo `#F4F4F6` (aprox), conteniendo:
  - Imagen de firma escaneada (en la tarjeta de la Parte Divulgante: firma de Magalí ya pegada).
  - Línea para firma (caracteres `_____`).
  - Nombre en bold.
  - Cargo y empresa.
  - Lugar y fecha.

## Sobre la diferencia LibreOffice vs Google Docs

LibreOffice (`soffice`) renderiza Calibri con métricas ligeramente distintas
a Google Docs. Diferencias observadas:

- Logo aparenta tamaño relativo distinto (ocupar más o menos espacio relativo en la columna).
- Espaciado entre logo y bloque de título.
- Posición vertical del subtítulo en itálica respecto al título principal.

**No son bugs del archivo**. Son diferencias de rendering motor. Para
validar el output real, abrir el `.docx` en Google Docs o Word.
