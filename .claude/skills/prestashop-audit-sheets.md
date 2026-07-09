# PrestaShop Audit to Google Sheets

Skill para auditar el catálogo de una tienda PrestaShop y volcar toda la información a una hoja de cálculo de Google Sheets organizada por pestañas.

## Cuándo usar

Cuando el usuario pida auditar, capturar, relevar o documentar los productos de una tienda PrestaShop para crear una base de datos en Google Sheets. Funciona con cualquier tienda PrestaShop accesible públicamente.

## Instrucciones

### Paso 1: Recopilar datos del usuario

Preguntar al usuario:
1. **URL de la tienda PrestaShop** (obligatorio)
2. **Nombre del cliente / empresa** (para titular el Sheet)
3. **Filtros de marca o categoría** (si hay que excluir alguna marca o sección)
4. **Carpeta de Google Drive** (opcional, si quiere guardar el Sheet en una carpeta específica)

### Paso 2: Explorar la estructura de la tienda

Usar `WebFetch` para:
1. Navegar la página principal y extraer el menú de navegación completo
2. Identificar todas las categorías y subcategorías con sus URLs
3. Detectar la separación de marcas si hay varias en la misma instalación
4. Anotar información general: idioma, moneda, datos de contacto, redes sociales

### Paso 3: Rastrear el catálogo completo

Para cada categoría (respetando los filtros del usuario):
1. Navegar cada página de categoría con `WebFetch`
2. Extraer de cada producto visible:
   - Nombre del producto
   - SKU / Referencia
   - Precio (moneda)
   - URL del producto
   - Descripción corta
   - Categoría y subcategoría a la que pertenece
   - Colores / variantes disponibles (si son visibles)
   - Rendimiento / cobertura (si aplica)
3. Seguir la paginación hasta cubrir todos los productos
4. Si se necesita más detalle, entrar a la ficha individual del producto

### Paso 4: Organizar los datos

Estructurar la información en las siguientes pestañas (tabs) para el Google Sheet:

**Tab 1 — "Resumen"**
| Campo | Valor |
|-------|-------|
| Nombre del cliente | ... |
| URL de la tienda | ... |
| Plataforma | PrestaShop |
| Fecha de auditoría | ... |
| Total de productos | ... |
| Total de categorías | ... |
| Moneda | ... |
| Idioma | ... |
| Contacto | ... |
| Redes sociales | ... |

**Tab 2 — "Categorías"**
| ID | Categoría | Subcategoría | URL | Cantidad de productos |
|----|-----------|--------------|-----|-----------------------|

**Tab 3 — "Productos"**
| # | SKU | Nombre | Categoría | Subcategoría | Precio | Moneda | Descripción | URL | Variantes/Colores | Rendimiento | Notas |
|---|-----|--------|-----------|--------------|--------|--------|-------------|-----|-------------------|-------------|-------|

**Tab 4 — "Observaciones"**
| # | Tipo | Descripción | Impacto | Recomendación |
|---|------|-------------|---------|---------------|

Tipos de observación: Precio sospechoso, Producto sin SKU, Categoría vacía, Producto sin descripción, Imagen faltante, etc.

### Paso 5: Crear el Google Sheet

1. Usar `mcp__Google_Drive__create_file` para crear un archivo CSV con los datos tabulados
2. El título del archivo debe ser: `[Nombre Cliente] - Auditoría Catálogo PrestaShop - [Fecha]`
3. Subir el contenido como CSV con `contentMimeType: "text/csv"` para que Google lo convierta a Sheets automáticamente
4. Para múltiples pestañas: crear un Sheet por tab y nombrar cada uno

### Paso 6: Reportar al usuario

Presentar un resumen con:
- Enlace al Google Sheet creado
- Total de productos capturados
- Total de categorías mapeadas
- Observaciones encontradas (precios raros, productos sin datos, etc.)
- Productos o categorías que fueron excluidos por los filtros

## Herramientas necesarias

- `WebFetch` — para navegar la tienda y extraer datos
- `WebSearch` — para buscar información adicional del cliente si es necesario
- `mcp__Google_Drive__create_file` — para crear el Sheet en Google Drive
- `mcp__Google_Drive__read_file_content` — para verificar el contenido creado

## Notas importantes

- Siempre respetar los filtros de exclusión de marca/categoría del usuario
- Los precios que aparezcan como $1,760,470.70 o valores extremadamente altos suelen ser placeholders de "Consultar precio" en PrestaShop — marcarlos como "A consultar" en la observación
- Seguir TODA la paginación, no quedarse solo con la primera página
- Si un producto aparece en múltiples categorías, listarlo una sola vez con la categoría principal
- Moneda siempre en formato local (ARS, USD, EUR, etc.)
