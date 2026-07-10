# PrestaShop → Fichas de Producto por Venta Consultiva (Google Sheets)

Skill para relevar el catálogo de un cliente con tienda PrestaShop y volcar cada producto en una **ficha de producto profunda**, organizada según la **lógica de venta consultiva** del cliente, en Google Sheets.

## Cuándo usar

Cuando el usuario pida auditar, capturar, relevar o documentar los productos de un cliente para crear una base de conocimiento comercial en Google Sheets. Especialmente cuando el entregable esperado NO es una lista de precios, sino una ficha por producto que sirva como guion de venta consultiva.

## Principio rector

El objetivo no es volcar características sueltas, sino **categorizar la información según la lógica con la que el cliente ofrece y vende**. Una buena ficha equivale a una conversación de venta consultiva: acompaña al comprador desde "¿qué es?" hasta "¿cómo lo compro y lo mantengo?".

## Fuentes de datos (dos capas que se integran)

1. **Sitio corporativo / catálogo** (ej. WordPress) → contiene la información PROFUNDA: descripción, usos, aplicaciones, ventajas, datos técnicos, FAQ, colores. Es la fuente principal de la ficha.
2. **Tienda PrestaShop (shop)** → contiene SKUs, presentaciones y precios. Se integra dentro de la ficha como **presentaciones y SKUs asociados**, NO como entregable aparte.

Una ficha vive a nivel **producto/familia** (ej. "MicroCemento"). Los SKUs del shop (kits, muestras, presentaciones) son variantes que se listan dentro de la ficha de su familia.

## Instrucciones

### Paso 1: Recopilar datos del usuario
1. URL de la tienda PrestaShop y del sitio corporativo (si existe)
2. Nombre del cliente / empresa
3. Marcas o categorías a excluir
4. Confirmar particularidades del negocio (ej. sin stock / a pedido, moneda, etc.)

### Paso 2: Mapear el universo de productos
1. Con `WebFetch`, listar todas las fichas de producto del sitio corporativo (nivel familia)
2. Con `WebFetch`, listar todas las categorías/SKUs del shop PrestaShop
3. Cruzar ambas: cada familia del corporativo ← sus SKUs del shop

### Paso 3: Relevar cada ficha en profundidad
Para cada producto, scrapear del sitio corporativo TODO el texto y clasificarlo en las 10 secciones de venta consultiva (ver Paso 4). Transcribir textual, no resumir de más.

### Paso 4: Estructura de la ficha (lógica de venta consultiva)
Cada ficha es una hoja vertical (Campo | Valor) con estas 10 secciones:

1. **IDENTIFICACIÓN (¿Qué es?)** — nombre, categoría, qué es en una frase, marca, diferenciación clave
2. **DESCUBRIMIENTO DE NECESIDAD (¿Para qué lo necesitás?)** — ambientes, tránsito, usos, aplicaciones
3. **PROPUESTA DE VALOR (¿Por qué este?)** — ventajas y diferenciadores
4. **CRITERIOS DE ELECCIÓN (¿Cuál variante?)** — tipos, familia relacionada, cuándo elegir cada uno
5. **AJUSTE TÉCNICO (¿Sirve para mi caso?)** — composición del sistema, espesor, soporte, proporción de mezcla, rendimiento
6. **PRESENTACIÓN Y COMPRA (¿Cómo se compra?)** — modalidad (a pedido/sin stock), presentaciones, SKUs asociados, almacenamiento, vida útil
7. **PERSONALIZACIÓN / ESTÉTICA (¿De qué color?)** — gama de colores, terminaciones
8. **MANEJO DE OBJECIONES (Preguntas frecuentes)** — FAQ, cada objeción real del comprador con su respuesta
9. **POSTVENTA / MANTENIMIENTO Y SOPORTE** — limpieza y mantenimiento, servicios (colocación, presupuesto)
10. **EMPRESA Y CONTACTO** — sobre el cliente, showroom, contacto, URLs (ficha y shop)

Usar encabezados de sección visibles (ej. `▐ 1. IDENTIFICACIÓN`) para separar bloques.

### Paso 5: Crear los Google Sheets
1. Una ficha = un archivo CSV con formato vertical (Campo, Valor)
2. Subir con `mcp__Google_Drive__create_file` y `contentMimeType: "text/csv"` (Google lo convierte a Sheet)
3. Título: `[Cliente] - FICHA - [Producto]`
4. Opcional: un Sheet índice con links a todas las fichas

### Paso 6: Reportar al usuario
- Links a las fichas creadas
- Cobertura (fichas completas / totales)
- Vacíos de información detectados en la fuente (campos que el cliente debería completar)

## Notas importantes

- **Sin stock**: si el cliente produce a pedido, no incluir columna de inventario; marcar modalidad "a pedido / a cargo"
- **Precio**: no es el eje. Si aparecen placeholders (ej. $1.760.470,70 en PrestaShop) marcarlos como "a consultar", nunca como precio real
- **Respetar exclusiones de marca** del usuario (ej. excluir una segunda marca que comparte la misma instalación PrestaShop)
- **Nivel familia, no SKU**: una ficha por producto/familia; los SKUs son presentaciones dentro de la ficha
- Transcribir el lenguaje del propio cliente: la ficha debe sonar a cómo ellos venden

## Herramientas necesarias
- `WebFetch` — scrapear tienda y sitio corporativo
- `mcp__Google_Drive__create_file` — crear las fichas como Google Sheets
- `mcp__Google_Drive__read_file_content` — verificar contenido
