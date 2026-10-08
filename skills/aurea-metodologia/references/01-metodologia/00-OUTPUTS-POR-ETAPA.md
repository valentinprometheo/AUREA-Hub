---
consultar-cuando: hay que entregar un documento o presentación al cliente, saber qué output corresponde a cada etapa
disparadores: "qué documento entrego acá", "output de esta etapa", "presentación cliente", "diseño de CRM", "carga de contactos", "guión de testing", "NDA", "deck"
fuente-única-de: índice de qué outputs cliente-facing existen y en qué etapa se usan
combina-con: el router 00-CONSULTA, la etapa correspondiente
---

# Índice de outputs client-facing por etapa

> Este archivo NO contiene los templates. Solo registra **qué documentos existen, de qué
> familia son, y en qué etapa/estadío se entregan.** Es un mapa de inventario.
>
> **La fuente viva de los templates es la skill `documentos-client-facing`** (paquete
> `documentos-client-facing.skill`), que vive en la zona de incubación de skills en Drive,
> fuera de este ZIP de metodología. Esa skill es conductor + repositorio + generador: cuando
> se pide un output, clasifica la familia, chequea dependencias, pide lo que falta y lo genera
> respetando la estética exacta de esa familia. Este índice solo apunta a ella.
>
> Por qué los templates no se internalizan acá: pesan, cambian, y tienen su propia estética
> y scripts. La metodología (este ZIP) es doctrina curada y liviana; los templates son
> ejecución y viven en la skill. Acá queda el puntero, no el contenido.

---

## Las ocho familias de output (con sus componentes reales)

> Tabla de inventario: qué familia es, su formato, y qué piezas concretas la componen dentro
> de la skill. Son los nombres de los archivos, no su contenido. Sirve para saber qué existe
> y pedir la pieza exacta, sin tener que abrir la skill.

| # | Familia | Formato | Componentes en la skill |
|---|---|---|---|
| 1 | **Diseño de CRM** | DOCX cliente-facing | reference `01-diseno-crm.md` |
| 2 | **Carga de Contactos** | XLSX (3 hojas) + prompt | reference `02-carga-contactos.md` · asset `plantilla-contactos.xlsx` |
| 3 | **Guión de Testing** | DOCX | reference `03-guion-testing.md` |
| 4 | **Presentación estética** | HTML → PDF | references `04-presentacion-estetica.md` + `...-system.md` (sistema de diseño) · assets deck: `aurea_kit.py` (motor), `logo.txt`, `sphere.txt` (base64) |
| 5 | **Documentación formal** | DOCX (edita template oficial) | references `05-documentacion-formal.md` + `...-tokens.md` + `...-qa.md` · asset `NDA-AUREA-template-base.docx` · scripts `edit_clause_5_proteccion_datos.py`, `edit_clause_11_condiciones_comerciales.py` |
| 6 | **Correcciones / Feedback de Demo** | DOCX | reference `06-correcciones-feedback-demo.md` · asset `feedback-demo-template-base.docx` |
| 7 | **Guía de Implementador** | Markdown vertical copy-paste | Metodología completa (no skill): `06-estructura-guia-implementador.md`. Tres casos de referencia validados: EDFAN (Tokko), G&D (Sheet-First), BETROX (PrestaShop) |
| 8 | **Acuerdo de Alcance y Objetivos** | DOCX branded AUREA (editable en Google Docs) | Generador propio (no skill todavía): catálogo de 8 bloques de servicio con estados por emoji, integraciones a medida (ERP), lista abierta de deseables, bloque de firmas. Componente reutilizable: carta banda Inteligencia Comercial (navy) |

**Estructura interna de la skill** (para ubicar las piezas de las familias 1 a 6):
`documentos-client-facing/` → `SKILL.md` (conductor) · `references/` (una por familia, definen estética y reglas) · `assets/` (`correcciones/`, `deck/`, `nda/`, `plantilla-contactos.xlsx`) · `scripts/` (editores de cláusula del NDA).

**Familias 7 y 8 viven fuera de la skill** (todavía no empaquetadas ahí): la Guía de Implementador
es metodología pura en `02-ETAPA2-Diseno/06-estructura-guia-implementador.md`; el Acuerdo de
Alcance tiene su propio generador DOCX (no skill), documentado como output pero sin reference
propio todavía — candidato a sumarse a la skill de outputs en una vuelta futura.

> Recordatorio de frontera: lo de arriba es el **inventario** (nombres de las piezas). El
> **contenido** de cada pieza (el texto del NDA, el código de los scripts, la estética de
> cada reference) NO se copia acá: vive en la skill o en el archivo de metodología referenciado.

---

## Mapa por etapa / estadío

```
ETAPA 1 — DISCOVERY
└── (outputs de discovery: biblia, asincrónico, accesos — son otra familia,
     generados por las skills de discovery, no por la de outputs client-facing)

ETAPA 2 — DISEÑO
├── Diseño del CRM presentado al cliente   → Familia 1 (Diseño de CRM, DOCX)
├── Carga de contactos del cliente          → Familia 2 (Carga de Contactos, XLSX + prompt)
├── Demo del agente → cliente reporta        → Familia 6 (Correcciones / Feedback de Demo, DOCX)
│     (el MÉTODO de procesar esas correcciones vive en
│      02-ETAPA2-Diseno/metodologia-correccion-agente.md; el DOCUMENTO, en la skill)
└── Testing del agente                       → Familia 3 (Guión de Testing, DOCX)

ETAPA 2 → ETAPA 3 (pasaje, diseño cerrado → configurar Prometheo)
└── Guía de Implementador                    → Familia 7 (Markdown, 3 casos de referencia)

CIERRE ETAPA 3 (lanzamiento validado, arranca Mejora Continua)
└── Acuerdo de Alcance y Objetivos           → Familia 8 (DOCX branded, con firmas)

TRANSVERSALES (cualquier etapa)
├── Propuestas, guías, one-pagers de marca   → Familia 4 (Presentación estética, HTML→PDF)
└── NDA / contratos / cláusulas              → Familia 5 (Documentación formal, DOCX legal)
```

Familias 1, 2, 3, 6 y 7 son el recorrido de Etapa 2/3. Familia 8 marca el cierre de Etapa 3.
Familias 4 y 5 son transversales (se
usan en cualquier momento del proyecto).

---

## Relación con la metodología (qué referencia a qué)

- **Familia 6 (Feedback de Demo)** es el documento que se llena en
  `02-ETAPA2-Diseno/feedback-demo-iteracion.md`; el método de procesarlo es
  `metodologia-correccion-agente.md`. La skill genera el documento; la metodología define
  el método. No se duplican.
- **Familia 4 (Presentación estética)** usa el sistema de diseño AUREA (la
  `aurea-deck-design.skill`, que esta skill de outputs absorbe).
- **Familia 7 (Guía de Implementador)** es metodología pura, no skill: vive completa en
  `02-ETAPA2-Diseno/06-estructura-guia-implementador.md`, con sus reglas de formato, reglas de
  diseño de variables, y los tres casos reales de referencia (EDFAN, G&D, BETROX).
- **Familia 8 (Acuerdo de Alcance)** referencia el catálogo completo de servicios de AUREA
  (Bloques 1 a 8 del documento), que a su vez espeja la estructura de esta misma metodología
  (config base del asistente, diseño de CRM, canales, integraciones, lanzamiento, inteligencia
  comercial). Cuando el catálogo de servicios de la metodología crece, el Acuerdo se actualiza
  en paralelo para no quedar desalineado.
- **La metodología comercial general** (lógicas de prompt, calificación, integraciones)
  vive en este ZIP; la skill de outputs es la **capa de ejecución** que la referencia, no
  la duplica.

---

## Estado y pendientes

- La skill `documentos-client-facing` está en **incubación** (Drive, fuera del ZIP) y cubre las
  familias 1 a 6. Cuando madure con los proyectos vivos, se evalúa si su índice se estabiliza acá.
- **Familias 7 y 8 ya están validadas y en uso**, pero viven fuera de la skill (metodología pura y
  generador propio, respectivamente). Candidatas a empaquetarse como módulos de la skill en una
  vuelta futura, sin urgencia — hoy funcionan bien como están.
- Cuando se agregue una familia nueva de output, se actualiza este índice (solo el puntero y
  el mapa por etapa, nunca el template en sí).

---

## Inteligencia Comercial NO es un output de estos, es un producto aparte

Ojo con no meter Inteligencia Comercial en esta lista de familias. No es un documento
client-facing ni un entregable de la implementación: es un **producto independiente** (un
dashboard sobre el export de Prometheo), que se contrata aparte y no se implementa por defecto en
todas las cuentas. Su documentación vive en
`02-ETAPA2-Diseno/inteligencia-comercial-producto.md`. No confundir con Mejora Continua (que
afina el agente) ni con la carta de venta de IC (que sí es material client-facing, familia 4).

## Principio general — documento maestro vs entregable de cliente

La distinción más importante para no ensuciar la metodología con material de un cliente puntual:

- **Documento maestro (método):** reutilizable en cualquier cliente, no depende de ninguno.
  Define CÓMO trabajamos. Viven en la metodología (este ZIP). Ejemplos: los 10 patrones de
  corrección, el barrido de coherencia y el template de auditoría en blanco, la doctrina de
  guión de testing, la gestión de proveedor, los principios transversales, la doctrina de
  integración por fuente.
- **Entregable de cliente:** el resultado de aplicar el método a un cliente concreto. Se archiva
  por cliente, no sube a la metodología. Ejemplos: la matriz de auditoría del prompt de un
  cliente (documento vivo por cliente, se actualiza cada ronda), el registro de incidentes de
  un cliente, la auditoría de una versión concreta del proveedor, los guiones de testing con
  datos reales de un cliente, las secciones corregidas de un prompt.

**Regla:** cada vez que un cliente marca un error nuevo, además de corregirlo se evalúa si es un
patrón nuevo (se agrega a los 10 patrones), si revela un hueco del método (se agrega un chequeo
al barrido), o si es una regla de método nueva (se graba en la metodología). Los documentos
maestros crecen; los entregables de cliente quedan archivados por cliente. La matriz de
auditoría de un cliente NO es método transversal, por más viva que sea.
