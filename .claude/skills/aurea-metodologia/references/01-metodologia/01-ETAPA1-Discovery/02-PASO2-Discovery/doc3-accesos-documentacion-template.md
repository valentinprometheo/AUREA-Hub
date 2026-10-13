# Doc 3 — Accesos y Documentación — Template

> **Tipo:** Cliente-facing
> **Modalidad:** Asincrónica — el cliente lo va completando
> **Plataforma:** Google Doc con links a carpetas de Drive del cliente
> **Característica:** Es el inventario operativo del proyecto

---

## Propósito

Inventario de **todo el material que el agente IA va a necesitar** para responder con precisión. La calidad del agente depende directamente de la calidad de este inventario.

**Regla:** si el material no está disponible o no está actualizado, el agente no puede usarlo. Esto se traduce en respuestas pobres o derivaciones innecesarias a humanos.

---

## Estructura

### Categorías de material a inventariar

#### 1. Material visual de cada [proyecto/producto/línea]

Adaptar a la tipología macro del rubro:

- **Desarrollista inmobiliario:**
  - Brochures por proyecto
  - Renders y planos
  - Fichas técnicas
  - Listas de precios actualizadas
  - Imágenes de obra en distintas etapas
  - Videos de drone / recorridos virtuales

- **Mobiliario:**
  - Catálogos por línea
  - Fichas técnicas de cada producto
  - Imágenes de productos en distintos contextos
  - Listas de precios y opciones de personalización

- **Insumos / materiales:**
  - Catálogos por categoría
  - Fichas técnicas y certificaciones
  - Listas de precios por tipo de cliente (mayorista, retail)

- **Inmobiliaria tradicional:**
  - Material por propiedad (depende de qué tan dinámico es el stock)
  - Catálogo de Tokko o equivalente

#### 2. Información operativa

- Lista del equipo comercial (nombres, mails, WhatsApp, roles)
- Horarios de atención
- Política de visitas / showroom (cómo se agendan)
- Política de financiación (condiciones, cuotas, requisitos)
- Política de descuentos (autorizaciones, % máximos)

#### 3. Accesos a sistemas

- Tokko (usuario / password / link de API si aplica)
- WhatsApp Business API
- Cuenta Prometheo del cliente
- Otros CRMs o herramientas activas

#### 4. Comunicación pública del cliente

- Links a redes sociales activas
- Links a la web oficial
- Material de marketing actual (folletos digitales, campañas vigentes)

#### 5. Conversaciones de referencia

Conversaciones reales del cliente que sirven para **calibrar el tono y la forma de responder del agente**. El cliente las exporta y las entrega en dos sub-bloques:

**5.a · Conversaciones Ideales** — interacciones que el cliente considera modelo, ejemplo de cómo querría que el agente se comunique.

- En formato **`.txt`**: conversaciones completas, de punta a punta, que sirven como referencia de una interacción ideal entera.
- En formato **`.jpg` / `.png`** (capturas): un ejemplo de cada **tipo de interlocutor distinto** que el cliente atiende, y capturas de momentos donde expusieron especialmente bien la información (por ejemplo, cómo presentaron un producto o servicio).

**5.b · Conversaciones NO Ideales** — interacciones que el cliente **no** quiere repetir: respuestas que no le gustaron, formas de comunicar que considera un mal ejemplo.

- En los mismos dos formatos: `.txt` para conversaciones completas, `.jpg` / `.png` para momentos puntuales.

> **Por qué se piden:** son material de calibración directo para el diseño del agente. Las Ideales le marcan el estándar a imitar; las NO Ideales, el patrón a evitar. Alimentan sobre todo el tono del agente y el tratamiento de FAQs y objeciones. Una sola conversación ideal bien elegida vale más que una descripción abstracta del tono deseado.

---

## Cómo se completa

### Modalidad

**Asincrónica** — el cliente sube material a su tiempo, en la carpeta compartida de Drive.

### Durante las reuniones

El consultor:
1. Abre el Documento 3 en pantalla compartida
2. Muestra qué partes corresponden al tema que están conversando
3. Explica cómo se carga cada cosa (estructura de carpetas, naming, etc.)

### Acompañamiento

- AUREA crea la **estructura de carpetas inicial** en el Drive del cliente
- El cliente sube material en cada carpeta correspondiente
- El consultor revisa al final de cada semana y avisa al cliente si falta algo crítico

---

## Estructura sugerida de carpeta Drive del cliente

```
[CLIENTE] — AUREA Hub /
├── 00 - Documentos del Discovery /
│   ├── Doc 1 - Discovery (Biblia).gdoc
│   ├── Doc 2 - Asincrónico.gdoc
│   └── Doc 3 - Accesos y Documentación.gdoc
├── 01 - Material por [proyecto/producto/línea] /
│   ├── [Proyecto A] /
│   │   ├── Brochure.pdf
│   │   ├── Lista de precios.xlsx
│   │   ├── Renders /
│   │   └── Planos /
│   └── [Proyecto B] /
├── 02 - Operativo /
│   ├── Equipo comercial.gdoc
│   ├── Horarios y políticas.gdoc
│   └── FAQs internas.gdoc
├── 03 - Accesos /
│   └── Credenciales.gdoc (cifrado o link a 1Password)
├── 04 - Comunicación pública /
│   └── Material vigente /
└── 05 - Conversaciones de referencia /
    ├── Ideales /
    │   ├── Completas (.txt) /
    │   └── Capturas (.jpg / .png) /
    └── NO Ideales /
        ├── Completas (.txt) /
        └── Capturas (.jpg / .png) /
```

---

## Convención visual del documento

- **Tabla de inventario** con columnas: Material | Ubicación en Drive | Estado | Última actualización
- **Estados:**
  - 🟢 Disponible y actualizado
  - 🟠 Disponible pero desactualizado
  - 🔴 Falta cargar
  - ⚪ No aplica al cliente

---

## Validación

No hay validación formal del Documento 3 — es **operativo y vivo**.

Su completitud se mide en el **cierre de Etapa 1**: si los materiales críticos no están, no se puede pasar a Etapa 2 (Diseño de las Reglas Diseño de Prometheo by AUREA) o se diseña con placeholders.

**Material crítico mínimo para arrancar Etapa 2:**
- 1 brochure / catálogo / ficha completa por cada tipología macro
- Lista del equipo comercial
- Acceso a Tokko (si aplica)
- Lista de precios mínima

**Material fuertemente recomendado (no bloqueante):**
- Al menos 1-2 Conversaciones Ideales y 1 NO Ideal. No frenan el inicio de Etapa 2, pero su ausencia obliga a calibrar el tono del agente solo con lo relevado en el Discovery. Cuanto antes lleguen, mejor calibrado sale el agente.

---

## Caso de referencia

La carpeta de Drive de G&D Developers (folder ID `13KXLWrLQXawE_K9OUDtLu0lO174zj39-`) es el caso de referencia de estructura completa.

**Lo que funcionó bien:**
- Subcarpeta por proyecto con todo el material organizado
- Naming consistente (`[Proyecto] - Brochure.pdf`)
- Inventario en Google Doc con links activos a cada material

**Lo que se detectó como problema:**
- Carpetas vacías o desactualizadas que el cliente no avisó
- Discrepancias entre lo declarado en la Biblia y lo encontrado en Drive
- Material no clasificado en raíz (sin asignar a proyecto)

**Por eso este documento es importante:** detectar gaps antes de Etapa 2, no durante.
