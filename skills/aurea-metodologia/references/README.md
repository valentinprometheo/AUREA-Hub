# AUREA Hub × Prometheo — Manual de instrucciones del ZIP

> **Versión:** 1.12
> **Fecha:** 11 junio 2026
> **Mantenedor:** Valentín Zas — AUREA Hub

---

## Para qué sirve este archivo

Es el **manual de uso del ZIP**. Cada archivo de la metodología está acá descripto con 5 bullets:

- **Qué hace** — función principal del archivo en 1 frase
- **Cuándo se usa** — momento operativo donde lo consultás
- **Al abrirlo encontrás** — qué estructura interna tiene
- **Relacionado con** — otros archivos del ZIP conectados
- **Status** — estable, prototipo, en construcción, etc.

**Para una vista visual de la metodología**, abrí `DIAGRAMAS.md` (4 diagramas Mermaid).

**Para empezar de cero con un cliente nuevo**, saltá a la sección "Cómo empezar" al final de este README.

---

## Estructura del ZIP

```
AUREA-Hub/
├── README.md                    ← este archivo
├── CHANGELOG.md                 ← registro de cambios por versión
├── DIAGRAMAS.md                 ← 4 diagramas Mermaid
├── Fondo_Transparente.png       ← assets de marca
├── LOGO_fondo_transparente.png  ← assets de marca
│
├── 01-metodologia/              ← la metodología completa
│   ├── 00-INDEX.md
│   ├── protocolo-extension-metodologia.md  ← cómo extender la metodología sin rehacerla
│   ├── roadmap.md                          ← estado y pendientes de la metodología
│   │
│   ├── 01-ETAPA1-Discovery/
│   │   ├── 01-PASO1-Pre-Discovery/
│   │   └── 02-PASO2-Discovery/
│   │
│   ├── 02-ETAPA2-Diseno/
│   │   ├── (contenido teórico transversal: reglas de diseño Prometheo, convenciones, etc.)
│   │   ├── 01-PASO1-Diseno-CRM/
│   │   ├── 02-PASO2-Diseno-Agente-IA/
│   │   └── 03-PASO3-Implementacion-CRM/
│   │
│   ├── 03-ETAPA3-Lanzamiento/   ← sin sub-Pasos definidos todavía
│   │
│   ├── 04-ETAPA4-Mejora-Continua/   ← sin sub-Pasos definidos todavía
│   │
│   ├── 06-rubros/               ← transversal (aplica a todas las Etapas)
│   ├── 07-convenciones-aurea/   ← transversal
│   └── 08-casos-referencia/     ← transversal (clientes prototipo y referentes)
│
└── 02-skills/                   ← skills para Claude.ai (formato carpeta/SKILL.md)
    │                               organizadas por etapa
    ├── 00-TRANSVERSAL/         ← skills que aplican a más de una etapa
    │   ├── project-instructions-universal.md
    │   ├── prometheo-vertical-real-estate/
    │   └── prometheo-vertical-mobiliario/
    ├── 01-ETAPA1/              ← skills de la Etapa 1 (Discovery)
    │   ├── prometheo-etapa1/ (orquestadora Etapa 1)
    │   ├── prometheo-auditoria-web/ (Paso 1.1 — Pre-Discovery)
    │   ├── prometheo-docs-kickoff/ (Pasos 1.2-1.3 — material cliente-facing, modular: 3 archivos)
    │   ├── prometheo-discovery-transversal/ (Paso 2 — los 4 docs)
    │   ├── prometheo-audit-doc1/ (Paso 2.4 — auditor de Etapa 1)
    │   ├── prometheo-formulario-real-estate/
    │   └── prometheo-formulario-mobiliario/
    ├── 02-ETAPA2/              ← skills de la Etapa 2 (Diseño del Agente)
    │   ├── prometheo-etapa2-design/ (orquestadora Etapa 2, modular: 6 archivos)
    │   ├── prometheo-drive-audit-real-estate/ (Pre-Etapa 2 — auditoría Drive)
    │   ├── prometheo-crm-graphics/ (gráficos del DOCX de diseño)
    │   └── prometheo-diseno-agente-ia-feedback/ (iteración — Documento de Feedback de demo)
    ├── 03-ETAPA3/              ← skills de la Etapa 3 (Lanzamiento) — pendientes de crear
    ├── 04-ETAPA4/              ← skills de la Etapa 4 (Mejora Continua) — pendientes de crear
    └── 05-templates/           ← templates de entregables
```

---

# RAÍZ DEL ZIP

### `README.md` (este archivo)

- **Qué hace:** manual de uso del ZIP completo. Describe cada archivo con 5 bullets.
- **Cuándo se usa:** primera lectura al abrir el ZIP. Después como referencia rápida cuando no sabés dónde buscar algo.
- **Al abrirlo encontrás:** descripción de todos los archivos organizada por carpeta (raíz → metodología → skills) y una sección "Cómo empezar" al final.
- **Relacionado con:** `DIAGRAMAS.md` (complemento visual), `01-metodologia/00-INDEX.md` (índice más conciso).
- **Status:** estable. Actualizar cada vez que se agregue/elimine un archivo del ZIP.

### `DIAGRAMAS.md`

- **Qué hace:** 4 diagramas Mermaid que muestran la metodología visualmente.
- **Cuándo se usa:** al onboardear un nuevo consultor o al explicar la metodología a un cliente.
- **Al abrirlo encontrás:** (1) las 4 Etapas en flujo, (2) cronograma típico de un proyecto, (3) skills por rubro, (4) relaciones entre archivos clave.
- **Relacionado con:** `README.md` (manual textual complementario).
- **Status:** estable. Actualizar si se modifica la estructura de las 4 Etapas o se agregan rubros.

### `CHANGELOG.md`

- **Qué hace:** registra qué se agregó, cambió o sacó en cada versión del ZIP.
- **Cuándo se usa:** al abrir una versión nueva del ZIP para ver qué cambió respecto a la anterior; al incorporar un cambio, para anotarlo.
- **Al abrirlo encontrás:** una entrada por versión (v1.3 en adelante) con secciones "Agregado" y "Cambiado".
- **Relacionado con:** `01-metodologia/protocolo-extension-metodologia.md` (todo cambio que se registra acá se hace siguiendo ese protocolo).
- **Status:** estable. Actualizar en cada cambio del ZIP.

### `Fondo_Transparente.png` y `LOGO_fondo_transparente.png`

- **Qué hace:** activos visuales de la marca AUREA Hub.
- **Cuándo se usa:** al generar DOCX cliente-facing, presentaciones, o cualquier entregable con identidad visual.
- **Al abrirlo encontrás:** archivos PNG con transparencia.
- **Relacionado con:** `01-metodologia/07-convenciones-aurea/01-paleta-y-colores.md`.
- **Status:** estable. Pendiente: subir logo final 2D cuando esté listo.

---

# 01-METODOLOGIA — La metodología completa

### `00-CONSULTA.md` ⭐ PUNTO DE ENTRADA OPERATIVO

- **Qué hace:** es el router de la metodología. No tiene contenido de doctrina: dice qué cargar según cuatro ejes (proceso / rubro / integración / transversal) y según si la conversación es nueva o con trayectoria. La metodología se consulta por la intersección de ejes, no entera.
- **Cuándo se usa:** PRIMERO, en cualquier conversación de trabajo. Antes de generar nada, se resuelven los cuatro ejes y se carga el set mínimo de esa tarea.
- **Al abrirlo encontrás:** las tablas de despacho por estadío y por integración, la lógica de los modos nueva/trayectoria, dos ejemplos completos de consulta, y el mapa de los cuatro ejes.
- **Relacionado con:** todos los archivos (los rutea). Los archivos clave llevan encabezado de auto-ruteo (`consultar-cuando` / `disparadores` / `combina-con`) que el router usa.
- **Status:** estable. Nuevo en v1.13.

### `00-INDEX.md`

- **Qué hace:** índice maestro de la metodología en 4 Etapas. Versión condensada del README.
- **Cuándo se usa:** consulta rápida cuando ya conocés el ZIP y solo necesitás ubicar una Etapa o protocolo.
- **Al abrirlo encontrás:** las 4 Etapas con sus Pasos internos, validaciones, archivos principales y principios transversales.
- **Relacionado con:** `README.md` (manual completo), `DIAGRAMAS.md` (vista visual).
- **Status:** estable.

### `00-planes-aurea.md`

- **Qué hace:** documenta los 2 planes operativos de acompañamiento mensual de AUREA — Plan Start (USD 150/mes) y Plan Pro (USD 250/mes).
- **Cuándo se usa:** al cerrar la propuesta con un cliente y al arrancar la Etapa 4 (Mejora Continua).
- **Al abrirlo encontrás:** comparación de los 2 planes, qué incluye cada uno, cuándo arranca el plan, relación con el protocolo de monitoreo.
- **Relacionado con:** `04-ETAPA4-Mejora-Continua/protocolo-monitoreo.md`, `metricas-core-prometheo.md`.
- **Status:** estable.

### `protocolo-extension-metodologia.md`

- **Qué hace:** define cómo agregar o modificar contenido de la metodología sin tener que rehacerla. Establece el principio de fuente única (cada dato vive en un archivo, el resto referencia).
- **Cuándo se usa:** SIEMPRE antes de incorporar un cambio al ZIP — categoría nueva, regla nueva, skill nueva, rubro nuevo.
- **Al abrirlo encontrás:** el principio de fuente única y cómo se ve un puntero, la distinción estable vs extensible, una tabla de tipos de cambio comunes con su archivo-fuente y punteros a verificar, un checklist de incorporación, y un caso resuelto de ejemplo.
- **Relacionado con:** `../CHANGELOG.md` (donde se registra cada cambio), todos los archivos de metodología (define cómo se editan).
- **Status:** estable.

### `roadmap.md`

- **Qué hace:** muestra el estado de la metodología (qué está hecho, parcial, pendiente) y la lista de pendientes ordenada por prioridad, con sus dependencias.
- **Cuándo se usa:** para decidir qué construir a continuación, o para ver en qué estado está cada etapa.
- **Al abrirlo encontrás:** estado por etapa, pendientes en 3 niveles de prioridad, dependencias entre pendientes, y un orden de trabajo sugerido.
- **Relacionado con:** `../CHANGELOG.md` (se actualizan juntos).
- **Status:** estable. Actualizar cuando se complete un pendiente o aparezca uno nuevo.

---

## ETAPA 1 — Pre-Discovery (PASO 1)

📁 `01-metodologia/01-ETAPA1-Discovery/01-PASO1-Pre-Discovery/`

### `auditoria-web-instagram.md`

- **Qué hace:** protocolo interno AUREA para auditar la web e Instagram del cliente antes de la primera reunión.
- **Cuándo se usa:** apenas el cliente firma contrato, antes de R1.
- **Al abrirlo encontrás:** checklist de qué buscar en cada plataforma, qué inferir, qué hipótesis cerrar, qué preguntas dejar abiertas para Discovery.
- **Relacionado con:** `doc-bienvenida-kickoff-template.md` (output cliente-facing que se nutre de la auditoría), `introduccion-etapa1-guia-metodologica-template.md`.
- **Status:** estable.

### `doc-bienvenida-kickoff-template.md`

- **Qué hace:** plantilla del Doc de Bienvenida // Kickoff que se envía al cliente antes de R1.
- **Cuándo se usa:** después de hacer la auditoría web, antes de la primera reunión con el cliente.
- **Al abrirlo encontrás:** estructura de 5 secciones (lo que sabemos del cliente, qué vamos a diseñar, las 4 etapas, quién tiene que estar en R1, presentación del consultor) + caso de referencia TKVA.
- **Relacionado con:** `auditoria-web-instagram.md` (input), `introduccion-etapa1-guia-metodologica-template.md` (segundo doc cliente-facing).
- **Status:** estable.

### `introduccion-etapa1-guia-metodologica-template.md`

- **Qué hace:** plantilla del segundo doc cliente-facing que explica cómo funciona la Etapa 1 (los 3 docs vivos).
- **Cuándo se usa:** después del Doc de Bienvenida, antes o durante el inicio de Etapa 1.
- **Al abrirlo encontrás:** explicación de los 3 docs (Biblia sincrónica, Asincrónico, Accesos) con su modalidad, función y conexión.
- **Relacionado con:** `doc-bienvenida-kickoff-template.md` (precede), los 3 templates de Discovery (los que el cliente va a usar).
- **Status:** estable.

---

## ETAPA 1 — Discovery (PASO 2)

📁 `01-metodologia/01-ETAPA1-Discovery/02-PASO2-Discovery/`

### `doc1-discovery-biblia-template.md`

- **Qué hace:** plantilla del Doc 1 — la "Biblia" del cliente. Se llena en vivo durante las reuniones de Discovery.
- **Cuándo se usa:** durante todas las reuniones sincrónicas de Etapa 1 (3-6 reuniones típicas).
- **Al abrirlo encontrás:** los bloques del Discovery (ver estructura-discovery.md), estructura de 4 partes por pregunta (por qué te preguntamos, pregunta, lo que ya sabemos, lo que nos cuentan), convenciones de anotación.
- **Relacionado con:** `protocolo-validacion-biblia.md` (cómo se cierra), los 4 archivos de `06-rubros/` (cada uno tiene preguntas específicas).
- **Status:** estable.

### `doc2-asincronico-template.md`

- **Qué hace:** plantilla del Doc 2 — preguntas que el cliente completa con tiempo, fuera de las reuniones sincrónicas.
- **Cuándo se usa:** en paralelo a las reuniones de Etapa 1. Crece a medida que avanza Discovery.
- **Al abrirlo encontrás:** categorías típicas de preguntas asincrónicas (métricas, listas detalladas, decisiones internas), cómo se gestiona el crecimiento del doc.
- **Relacionado con:** `doc1-discovery-biblia-template.md` (la info que se completa acá se integra a la Biblia).
- **Status:** estable.

### `doc3-accesos-documentacion-template.md`

- **Qué hace:** plantilla del Doc 3 — inventario operativo del material que el agente va a necesitar (brochures, fichas, accesos a sistemas).
- **Cuándo se usa:** en paralelo a las reuniones de Etapa 1. El cliente carga material en Drive a medida que puede.
- **Al abrirlo encontrás:** categorías de material por rubro, estructura sugerida de carpeta Drive del cliente, criterios de material crítico mínimo para arrancar Etapa 2.
- **Relacionado con:** `04-convenciones-docx-cliente.md` (los assets cargados se usan en el DOCX).
- **Status:** estable.

### `protocolo-validacion-biblia.md`

- **Qué hace:** define cómo se cierra formalmente la Etapa 1 con la Biblia validada como fuente oficial.
- **Cuándo se usa:** al cierre de Discovery, antes de arrancar Etapa 2 (Diseño).
- **Al abrirlo encontrás:** criterios de readiness, ciclo de iteración con el cliente, formato del callout de validación, qué hacer si la Biblia cambia después de aprobada.
- **Relacionado con:** `doc1-discovery-biblia-template.md`, `02-ETAPA2-Diseno/01-operativa-y-decisiones.md` (próxima Etapa).
- **Status:** estable.

### `metricas-core-prometheo.md`

- **Qué hace:** documenta las 5 métricas core de Prometheo (velocidad de respuesta, leads calificados, capacidad, satisfacción, ventas) con sus benchmarks. Se relevan como baseline en el Discovery.
- **Cuándo se usa:** en el bloque B10 del Discovery, para capturar el "antes" de cada métrica.
- **Al abrirlo encontrás:** las 5 métricas con benchmark y pregunta de relevamiento, métricas adicionales por rubro, conexión con el reporte mensual de Etapa 4.
- **Relacionado con:** `prometheo-discovery-transversal` (skill, bloque B10), `04-ETAPA4-Mejora-Continua/protocolo-monitoreo.md`, `00-planes-aurea.md`.
- **Status:** estable.

---

## ETAPA 2 — Contenido teórico transversal

📁 `01-metodologia/02-ETAPA2-Diseno/`

Estos archivos viven directamente en `02-ETAPA2-Diseno/` (no dentro de un PASO específico) porque son **transversales a los 3 Pasos de la Etapa 2** (Diseño del CRM, Diseño del Agente IA, Implementación del CRM).

### `01-operativa-y-decisiones.md`

- **Qué hace:** manual operativo de la Etapa 2 completa. Define qué se diseña primero, qué después, qué decisiones se cierran antes de avanzar.
- **Cuándo se usa:** al arrancar la Etapa 2 de cualquier cliente.
- **Al abrirlo encontrás:** secuencia de sub-pasos (Embudos → Variables → Tags → Seguimientos → Reglas Distribución), criterios de cierre, decisiones típicas por sub-paso.
- **Relacionado con:** `02-trazabilidad-etapa1-etapa2.md` (de dónde sale la info), `03-reglas-diseno-prometheo-by-aurea.md` (qué reglas respetar).
- **Status:** estable.

### `02-trazabilidad-etapa1-etapa2.md`

- **Qué hace:** muestra cómo cada bloque del Discovery alimenta cada componente del diseño conceptual.
- **Cuándo se usa:** cuando dudás de dónde sale una decisión del diseño, o al auditar coherencia entre Discovery y Etapa 2.
- **Al abrirlo encontrás:** tabla cruzada Discovery × Componentes de diseño (Embudos, Variables, Tags, Seguimientos, Reglas).
- **Relacionado con:** `01-operativa-y-decisiones.md`, los bloques del Discovery.
- **Status:** estable.

### `03-reglas-diseno-prometheo-by-aurea.md` ⭐ DOCUMENTO CENTRAL

- **Qué hace:** define las 24 reglas inviolables del diseño AUREA × Prometheo. Aplica a TODOS los clientes sin excepción.
- **Cuándo se usa:** SIEMPRE — antes de proponer cualquier regla nueva, antes de aprobar un Prompt V1, al auditar prompts existentes.
- **Al abrirlo encontrás:** vista resumen al inicio con 4 bloques (Smart Tags/Variables, Comunicación, Operativa, Integración catálogo) con definición de 1-2 líneas por regla. Después, detalle completo de cada regla con ejemplos y razones.
- **Relacionado con:** `08-reglas-integracion-catalogo.md` (profundiza reglas 16-21), todos los archivos de `06-rubros/` (aplican las 24 reglas con matices del rubro).
- **Status:** documento maestro estable. Actualizar si Prometheo libera features nuevas o el bot oficial valida comportamiento nuevo.

### `04-convenciones-docx-cliente.md`

- **Qué hace:** define las 10 convenciones del DOCX cliente-facing que se entrega en Ronda 1 del Paso 2 de Etapa 2.
- **Cuándo se usa:** al diseñar el DOCX para cualquier cliente.
- **Al abrirlo encontrás:** convenciones de naming, paleta de colores asignada a procesos, estructura de secciones obligatorias, formato de tablas, KPIs.
- **Relacionado con:** `03-reglas-diseno-prometheo-by-aurea.md` (regla 13: color por proceso), `07-convenciones-aurea/01-paleta-y-colores.md`, `02-skills/05-templates/docx-diseno-crm-template.md`.
- **Status:** estable.

### `05-estructura-prompt-agente.md`

- **Qué hace:** define las 14 secciones + 3 anexos que tiene todo prompt de agente diseñado por AUREA.
- **Cuándo se usa:** al diseñar el Prompt V1 para cualquier cliente.
- **Al abrirlo encontrás:** las 14 secciones con su función (Identidad, Tono, Bienvenida, Árbol de decisión, etc.) y los 3 anexos canónicos.
- **Relacionado con:** `03-reglas-diseno-prometheo-by-aurea.md` (las reglas aplican al prompt), `02-skills/05-templates/prompt-template.md`.
- **Status:** estable.

### `06-estructura-guia-implementador.md` ⭐ FAMILIA 7 DE OUTPUTS

- **Qué hace:** define los bloques de la Guía Implementador (Familia 7) que se entrega en el
  pasaje Etapa 2 → Etapa 3, más las reglas duras de formato del generador (vertical/angosto,
  bloques de código, naming sin guion bajo), las reglas de diseño de variables (única/múltiple,
  padre/hija, producto-externo vs interés-del-lead, patrón dual de IC en 6 variables), y la
  decisión de diseño de cuándo un B2B necesita embudo propio.
- **Cuándo se usa:** al diseñar la Guía Implementador para cualquier cliente nuevo, o al validar
  el diseño de variables/tags antes de generarla.
- **Al abrirlo encontrás:** los bloques de la guía con contenido típico, las reglas duras de
  formato, las reglas de diseño de variables, y una **tabla comparativa de los tres casos reales
  de referencia** (EDFAN/Tokko, G&D/Sheet-First, BETROX/PrestaShop) con integración, agendamiento,
  modelo de perfil, distribución, B2B y conteo de variables/testing de cada uno.
- **Relacionado con:** `embudos-y-tags.md`, `framework-seguimientos.md`,
  `08-reglas-integracion-catalogo.md`, `protocolo-implementacion.md` (Etapa 3 — Lanzamiento).
- **Status:** estable. Ampliado en v1.14 con reglas de diseño y los 3 casos reales.


### `arquitectura-crm-por-rubro.md` ⭐ MOLDES DE DISEÑO

- **Qué hace:** los moldes de arquitectura de CRM que ya funcionaron, para calcar la estructura al arrancar una cuenta nueva en vez de reinventarla. Es la respuesta al problema de que el modelo se equivocaba diseñando embudos, tags y variables de cuentas nuevas: acá tiene la experiencia cargada.
- **Cuándo se usa:** al arrancar el diseño de CRM de una cuenta nueva; se combina con `embudos-y-tags.md` (el criterio) y el archivo del rubro.
- **Al abrirlo encontrás:** el molde desarrollista (3 embudos) y el molde mobiliario (4 embudos), con sus dimensiones de tags y variables típicas, marcado patrón (sube) vs instancia (queda en la cuenta), y qué se mantiene y qué cambia entre rubros.
- **Relacionado con:** `embudos-y-tags.md`, `06-estructura-guia-implementador.md`, los archivos de `06-rubros/`.
- **Status:** estable. Nuevo en v1.18. Validado en EDFAN, G&D y BETROX.

### `inteligencia-comercial-producto.md` ⭐ PRODUCTO IC

- **Qué hace:** documenta Inteligencia Comercial como producto: qué es (dashboard sobre el export de Prometheo), qué no es (no es Mejora Continua, no es obligatorio, es producto aparte), sobre qué corre y qué requiere.
- **Cuándo se usa:** cuando el cliente pregunta por IC, o se ofrece/diseña el producto; para no confundirlo con Mejora Continua ni con la carta de venta.
- **Al abrilo encontrás:** el encuadre (producto independiente), el export de Prometheo como fuente (Tags + Variables), los 6 paneles del dashboard, los requisitos (WhatsApp API + Enterprise), y la viabilidad validada por el desarrollista con DRAKON como caso de referencia (probado contra el export real de TKVA).
- **Relacionado con:** `logica-comercial-transversal.md` y `embudos-y-tags.md` (las 6 variables de IC que alimentan los paneles), `restricciones-plataforma-prometheo.md` (requisitos de plan), el deck oficial de AUREA (venta).
- **Status:** estable. Nuevo en v1.18. Producto en desarrollo, viabilidad confirmada.

### `08-reglas-integracion-catalogo.md` ⭐ EJE INTEGRACIÓN

- **Qué hace:** las reglas de consulta a fuentes de datos. Tres partes: las 6 reglas genéricas a cualquier catálogo, la doctrina por fuente concreta (Sheets / Tokko / PrestaShop, incluidos los bloqueantes ITESA recurrentes de PrestaShop), y la distinción ERP interno no integrado vs ERP integrado a medida por Connect/Atlas. Insight central: las reglas de consulta dependen de la fuente, no del rubro, así que esto cruza rubros y acelera el próximo prompt.
- **Cuándo se usa:** al diseñar un agente con integración a una fuente de datos externa. Se carga por el eje INTEGRACIÓN del router según qué fuente usa el cliente.
- **Al abrirlo encontrás:** las 6 reglas genéricas; la doctrina por fuente (Sheets: verificación del lote, búsqueda fresca, columnas sobre notas, precio siempre; Tokko: tipología-proyecto vs unidades-hoy, anti-memoria, discreción; PrestaShop: modelo como clave, búsqueda escalonada de 4 intentos, bloqueantes ITESA); el sistema de placeholders **de archivo** con su estado (distinto de los placeholders de mensaje, ver `framework-seguimientos.md`); y el criterio ERP interno vs integrado.
- **Relacionado con:** `03-reglas-diseno-prometheo-by-aurea.md`, los archivos de rubros, `05-estructura-prompt-agente.md`, `framework-seguimientos.md` (los otros 2 sistemas de placeholder). Casos de referencia: G&D (Sheets), EDFAN (Tokko), BETROX (PrestaShop).
- **Status:** estable. Doctrina por fuente y placeholders en v1.13; bloqueantes ITESA y criterio ERP en v1.14.

### `restricciones-plataforma-prometheo.md`

- **Qué hace:** documenta las restricciones técnicas de la plataforma Prometheo que condicionan el diseño. Las 1-8 son el marco base; 9-15 se sumaron en v1.8; 19-21 se confirmaron en v1.14 con los tres casos de producción (colores de Smart Tags, acciones de tag y plan requerido, patrón Descripción de Embudo para la IA).
- **Cuándo se usa:** durante toda la Etapa 2 — el diseño tiene que respetar estas restricciones.
- **Al abrirlo encontrás:** las 21 restricciones explicadas + su relación con las Reglas Diseño + ranura de hallazgos de campo.
- **Relacionado con:** `embudos-y-tags.md`, `03-reglas-diseno-prometheo-by-aurea.md`, `framework-seguimientos.md`.
- **Status:** estable.

### `framework-seguimientos.md` ⭐ SISTEMA COMPLETO DE MENSAJERÍA (5 MECANISMOS)

- **Qué hace:** ya no es solo sobre seguimientos — es el hub de los **5 mecanismos de mensajería
  automatizada** de Prometheo: Seguimientos, Recordatorios conversacionales, Recordatorios
  programados, Campañas masivas, y Plantillas de WhatsApp (Meta). Corrige una afirmación previa
  (la lógica AND de tags no era "Fase 2": el modelo real de segmento con inclusión/exclusión ya
  está disponible, confirmado en BETROX).
- **Cuándo se usa:** al diseñar cualquier mensajería automática de un cliente en Etapa 2.
- **Al abrirlo encontrás:** el cuadro resumen de los 5 mecanismos; el detalle completo de
  Seguimientos (6 criterios de redacción, convención de nombre, 3 packs horarios, variable
  `Reasignación Moderador`, caso G&D completo con mensajes y alternativas A/B); los otros 4
  mecanismos con su mecánica, ventajas y límites; la sintaxis de placeholder de cada mecanismo; y
  la tabla comparativa de los **tres sistemas de placeholder** (archivo, seguimiento,
  recordatorio) para no confundirlos.
- **Relacionado con:** `03-reglas-diseno-prometheo-by-aurea.md` (Reglas 1 y 6), `restricciones-plataforma-prometheo.md`, `08-reglas-integracion-catalogo.md` (placeholders de archivo), `06-rubros/01-real-estate.md` (caso G&D), el bloque B5 del Discovery.
- **Status:** estable. Reescrito de fondo en v1.14 — antes cubría 1 de 5 mecanismos.

### `embudos-y-tags.md` ⭐ MODELO DE DATOS

- **Qué hace:** fija el modelo de datos de Prometheo — Smart Tags y Variables como dos entidades base, y el Embudo como agrupación ordenada de tags. Define la **regla AUREA de "una tag por dimensión"**, y su refinamiento confirmado en v1.14: cuando el perfil tiene subcategorías, se diseña **variable única + variable hija condicional**, y la tag de esa dimensión pasa a ser espejo de visibilidad, no la fuente del dato (casos G&D `Tipo Perfil`+`Inversión Finalidad`, BETROX `Tipo Cliente`+`Tipo Profesional`). También documenta el reemplazo de la vieja tag "Prioridad" ambigua por `Hot Lead` con criterio binario estricto.
- **Cuándo se usa:** en todo el diseño del CRM en Etapa 2; es la base conceptual de las Reglas Diseño.
- **Al abrirlo encontrás:** las dos entidades base, el Embudo, las reglas de cuándo justificar un embudo y qué NO es embudo, la regla de una tag por dimensión con sus dimensiones canónicas, el árbol de decisión, reglas duras (7), y los hallazgos confirmados de v1.14 (variable+hija, Contacto VIP de 4 valores, Hot Lead).
- **Relacionado con:** `03-reglas-diseno-prometheo-by-aurea.md`, `restricciones-plataforma-prometheo.md`, `excel-carga-clientes.md`, `importacion-contactos.md`, `framework-seguimientos.md`, y los archivos de `06-rubros/` que aplican el modelo a cada vertical.
- **Status:** estable — modelo validado con G&D Developers y confirmado/refinado con BETROX en v1.14 (la doctrina aplicada a cada rubro vive en `06-rubros/`).

### `integraciones-por-rubro.md`

- **Qué hace:** mapea las integraciones y canales de Prometheo contra las 4 verticales de AUREA, para decidir en Etapa 2 qué integraciones proponer a cada cliente.
- **Cuándo se usa:** al diseñar el CRM, cuando hay que elegir integraciones.
- **Al abrirlo encontrás:** catálogo de integraciones y canales con nivel de confianza por ficha, mapa por las 4 verticales (núcleo vs según caso), ranura de hallazgos de campo.
- **Relacionado con:** `restricciones-plataforma-prometheo.md`, los archivos de `06-rubros/`.
- **Status:** estable — varias integraciones con detalle pendiente de lectura del GitBook.

### `pendientes-itesa.md`

- **Qué hace:** buzón único de dudas sobre la plataforma Prometheo sin confirmar, que requieren respuesta de ITESA.
- **Cuándo se usa:** cuando surge una duda de comportamiento de plataforma que no se puede confirmar con el bot oficial; y antes de una reunión con ITESA.
- **Al abrirlo encontrás:** tabla de dudas abiertas, registro de dudas ya resueltas, cómo se agrega un pendiente.
- **Relacionado con:** `restricciones-plataforma-prometheo.md`, `integraciones-por-rubro.md`.
- **Status:** documento vivo.

### `reglas-revisadas-v1.11.md`

- **Qué hace:** historial de los cambios al archivo oficial de reglas. Lista las 4 propuestas que el modelo de Embudos/Tags/Variables introdujo y que se aplicaron en v1.11, con texto viejo / texto nuevo / motivo.
- **Cuándo se usa:** para trazabilidad. Si en el futuro aparecen nuevas propuestas de cambio a reglas, este archivo es el modelo (formato y proceso).
- **Al abrirlo encontrás:** tabla resumen de qué se aplicó, y por cada propuesta: texto viejo, motivo, texto nuevo aplicado.
- **Relacionado con:** `03-reglas-diseno-prometheo-by-aurea.md`, `embudos-y-tags.md`.
- **Status:** cerrado — propuestas v1.11 aplicadas. Se reutiliza el formato si surgen nuevas propuestas.

### `importacion-contactos.md`

- **Qué hace:** procedimiento para cargar contactos en masa a Prometheo por Excel, y el orden de carga obligatorio de toda la configuración del cliente (variables → tags → embudos → contactos).
- **Cuándo se usa:** al cargar un cliente nuevo en Prometheo — final de Etapa 2 / Etapa 3.
- **Al abrirlo encontrás:** el orden de carga obligatorio, la plantilla oficial y su formato (columna Tags con `|`, prefijo `var_`), comportamientos a tener en cuenta (tags ignoradas en silencio, dedup por teléfono, problema `__EMPTY`), reglas y trampas, checklist para cliente nuevo.
- **Relacionado con:** `embudos-y-tags.md`, `restricciones-plataforma-prometheo.md` (restricciones 16-18), `excel-carga-clientes.md`.
- **Status:** estable.

### `excel-carga-clientes.md`

- **Qué hace:** define qué es el Excel/Sheets de Carga del cliente — el 4º output de Etapa 2. Estructura, conflicto Excel-de-trabajo vs Sheets-plano, cuándo se genera.
- **Cuándo se usa:** al final del diseño de Etapa 2, después de aprobar DOCX y Prompt, para preparar la carga al Go-Live.
- **Al abrirlo encontrás:** la pieza dentro de los 4 outputs, estructura del Excel (2 hojas), validaciones, formato de teléfono y montos, orden de generación.
- **Relacionado con:** `embudos-y-tags.md`, `importacion-contactos.md`, `prometheo-etapa2-design` (módulo `excel_carga_contactos.md`).
- **Status:** estable.

### `feedback-demo-iteracion.md`

- **Qué hace:** define el Documento de Feedback de Demo — la tabla que el cliente completa durante el testing del agente para reportar correcciones. Herramienta de iteración de la fase de demo.
- **Cuándo se usa:** cuando el agente entra en fase de demo y empieza el ciclo iterar → corregir → testear.
- **Al abrilo encontrás:** estructura, reglas para marcar capturas (aditivo nunca destructivo, una corrección por fila), cómo se trabaja con el cliente, versión del prompt en encabezado, plantilla base, y los hallazgos de campo confirmados con dos rubros (transversalidad, arco de autoría, la marca es la crítica).
- **Relacionado con:** `metodologia-correccion-agente.md` (el método de procesarlo), `principios-transversales-agente.md` (donde suben las correcciones que se repiten en 2 rubros), `prometheo-etapa2-design` (skill).
- **Status:** estable — casos de referencia: G&D, EDFAN, BETROX. Plantilla DOCX canónica reutilizable, pendiente.

### `metodologia-correccion-agente.md` ⭐ MÉTODO DE ITERACIÓN

- **Qué hace:** define cómo se procesa el feedback de una demo y se convierte en mejoras del prompt sin romper lo que funciona, con trazabilidad de qué corrección originó qué regla. Mientras `feedback-demo-iteracion.md` es el documento, este es el método.
- **Cuándo se usa:** al procesar cualquier ronda de correcciones de un agente en demo/producción.
- **Al abrirlo encontrás:** el protocolo de cinco pasos (leer todo → clasificar por capa → detectar patrón → extraer y decidir destino → aplicar aditivo), el arco de autoría (qué capa reporta el cliente según su perfil), la sección de trazabilidad corrección→regla con casos verbatim de los tres prompts, el barrido de coherencia 8+1, el template de auditoría de entrega (5 hojas), el criterio de refuerzo completo de Prometheo, y la trazabilidad con las palabras del proveedor.
- **Relacionado con:** `feedback-demo-iteracion.md`, `principios-transversales-agente.md`, `10-patrones-correccion-agente.md`, `gestion-proveedor-itesa.md`, `03-reglas-diseno-prometheo-by-aurea.md`.
- **Status:** estable. Ampliado en v1.15 (barrido 8+1, template, refuerzo completo).

### `10-patrones-correccion-agente.md` ⭐ DOCUMENTO MAESTRO DE AUDITORÍA

- **Qué hace:** los 13 errores recurrentes de cualquier agente de Prometheo, con síntoma, causa, regla que lo corrige, traducción por vertical y estado (cubierto/parcial/hueco/hueco por diseño). Es la referencia para auditar un prompt nuevo o ubicar un bug dentro de un patrón conocido.
- **Cuándo se usa:** al arrancar con un cliente nuevo, o cuando aparece un bug. Se lee, se marca qué patrones aplican, se busca en el prompt si están cubiertos.
- **Al abrilo encontrás:** los 13 patrones (los 10 originales + 11 contradicción de jerarquía, 12 CTA que no vende, 13 regla condicionada a evaluación ambigua), cómo se usa el documento, la regla de oro (un patrón describe un error y su corrección tal como quedó en un prompt que HOY funciona; no se inventan reglas que rompan lo que anda), y los marcados transversales.
- **Relacionado con:** `contradicciones-jerarquia.md` (desarrollo de los patrones 11-13), `metodologia-correccion-agente.md`, `logica-comercial-transversal.md` (cara positiva del patrón 12), `guion-testing.md`.
- **Status:** estable. Ampliado a 13 en v1.16. Validado con Martina (EDFAN) y Catalina (BETROX).

### `contradicciones-jerarquia.md` ⭐ TERCER TIPO DE ERROR

- **Qué hace:** desarrolla el tipo de error "contradicción de jerarquía" (dos reglas propias correctas que compiten en el mismo turno; una pisa a la otra), además de sus dos hermanos: CTA que existe pero no vende, y regla condicionada a una evaluación ambigua del contexto.
- **Cuándo se usa:** cuando un bug puntual "seguro pasa también en otros casos", cuando una regla muy reforzada pisa otra, o cuando una acción obligatoria falla al entrar por un anuncio.
- **Al abrilo encontrás:** el caso PAROS, las tres señales para reconocerlo, cómo se corrige (nombrar los dos casos, generalizar, declarar prevalencia, nunca reforzar), los dos hermanos, y el enganche con los chequeos 2 y 5 del barrido.
- **Relacionado con:** `10-patrones-correccion-agente.md` (patrones 11-13), `metodologia-correccion-agente.md` (barrido), `logica-comercial-transversal.md`.
- **Status:** estable. Nuevo en v1.16. Confirmado por soporte de Prometheo sobre el caso PAROS.

### `logica-comercial-transversal.md` ⭐ CÓMO VENDE EL AGENTE

- **Qué hace:** la doctrina de lógica comercial transversal, distinta de la de comportamiento. Cómo VENDE un buen agente. Contiene solo los **13 patrones transversales reales** (probados en desarrollista Y mobiliario); la lógica de un solo rubro vive en su archivo de `06-rubros/`.
- **Cuándo se usa:** al diseñar o corregir cómo vende un agente, y al integrar los hallazgos de lógica comercial de un cliente nuevo.
- **Al abrilo encontrás:** la regla de promoción (rubro → transversal solo si aparece en dos rubros DISTINTOS, no dos clientes del mismo rubro), la regla patrón vs instancia (la forma sube, el valor de hoy queda en el cliente), los 13 transversales con su evidencia de cada rubro, y el puntero a dónde vive lo que no es transversal (rubro desarrollista y candidatos).
- **Relacionado con:** `principios-transversales-agente.md` (comportamiento, no venta), `06-rubros/01-real-estate.md` (nivel 2 desarrollista) y `06-rubros/02-mobiliario.md` (candidatos), `10-patrones-correccion-agente.md` (patrón 12).
- **Status:** estable. Rebalanceado en v1.17 (de ~30 a 13 reales; el resto bajó a rubro). Destilado de EDFAN, G&D y BETROX.

### `gestion-proveedor-itesa.md` ⭐ CAPA DE PROVEEDOR

- **Qué hace:** cómo se trabaja con Prometheo/ITESA como proveedor: auditar las reescrituras del prompt que entrega, documentar el retrabajo imputable con evidencia, y separar los tres actores (AUREA / proveedor / cliente).
- **Cuándo se usa:** cuando el proveedor entrega una reescritura del prompt, o hay que elevar un incidente con evidencia.
- **Al abrirlo encontrás:** los tres actores y la regla de que un mensaje al cliente no es una elevación al proveedor; el molde de auditoría de una reescritura (bloqueantes, reglas perdidas, contradicciones, lo replicable, lo conservado); el hallazgo "la reescritura mejora estructura y pierde lógica comercial, no se elige, se combina"; y el dossier de incidentes con filtro de credibilidad.
- **Relacionado con:** `metodologia-correccion-agente.md`, `pendientes-itesa.md`, `10-patrones-correccion-agente.md`.
- **Status:** estable. Nuevo en v1.15. Molde validado con la V3.0-R3 de Catalina.

### `guion-testing.md` ⭐ DOCTRINA DE TESTING

- **Qué hace:** cómo se arma y se corre el guión que valida un agente antes de un Go-Live y después de cada corrección. El formato no depende del rubro.
- **Cuándo se usa:** al armar o correr el testing de un agente, o al validar una ronda de correcciones.
- **Al abrilo encontrás:** el principio de los "primos" (testear la regla general, no el caso; si pasa solo el caso reportado, quedó parche), el formato de test, la marca [PLATAFORMA], el bloque de regresión, los patrones reutilizables (reconocer por atributo, tabla de sinónimos) y la distinción guión interno vs client-facing.
- **Relacionado con:** `10-patrones-correccion-agente.md`, `metodologia-correccion-agente.md`, `08-reglas-integracion-catalogo.md`, `00-OUTPUTS-POR-ETAPA.md` (familia 3).
- **Status:** estable. Nuevo en v1.15. Destilado de los guiones de Martina y Catalina.

### `principios-transversales-agente.md` ⭐ DIECISIETE PRINCIPIOS

- **Qué hace:** reúne los diecisiete principios de comportamiento que aplican a cualquier agente de Prometheo sin importar el rubro. Cada uno está PROBADO en dos o más rubros independientes, con evidencia citada. Es la capa base de cualquier prompt. El 17 (un archivo nunca reemplaza la respuesta) se sumó en v1.17.
- **Cuándo se usa:** siempre que se diseña o itera un prompt, en cualquier rubro.
- **Al abrirlo encontrás:** los diecisiete principios con su evidencia por rubro, el criterio de promoción (rubro → transversal solo si se ve en 2 rubros DISTINTOS, no dos clientes del mismo rubro), el patrón de fondo (agente conducido por el lead), el hallazgo de autoría, y la ranura de candidatos.
- **Relacionado con:** todos los archivos de `06-rubros/`, `08-reglas-integracion-catalogo.md`, `metodologia-correccion-agente.md`, y la skill de incubación de corrección de prompt.
- **Status:** estable. Nuevo en v1.13.

---

## ETAPA 2 — Diseño del Agente IA (PASO 2)

📁 `01-metodologia/02-ETAPA2-Diseno/02-PASO2-Diseno-Agente-IA/`

Acá viven los protocolos de la entrega del agente al cliente: rondas de entrega, iteración del prompt V1 → V2 → V3, demo aplicada en vivo dentro de Prometheo.

> **Nota:** los otros 2 Pasos de Etapa 2 (`01-PASO1-Diseno-CRM/` y `03-PASO3-Implementacion-CRM/`) todavía no tienen protocolos escritos — quedan pendientes de documentar.

### `protocolo-entrega-cliente.md`

- **Qué hace:** define cómo se ejecutan las 2 rondas de entrega al cliente (DOCX+Prompt → aprobación → Guía Implementador).
- **Cuándo se usa:** al pasar de la Etapa 2 (Diseño) a la entrega visible al cliente.
- **Al abrirlo encontrás:** estructura de cada ronda, qué se entrega, cómo se itera, criterios de aprobación, tabla de progreso típica (~3 semanas), errores comunes.
- **Relacionado con:** `protocolo-iteracion-prompt.md` (detalle de iteración), `02-skills/05-templates/` (templates de los deliverables).
- **Status:** estable.

### `protocolo-iteracion-prompt.md`

- **Qué hace:** define cómo se gestionan los rediseños del prompt cuando el cliente pide ajustes.
- **Cuándo se usa:** después de cada demo, cuando el cliente marca cambios al Prompt V1, V2, V3, etc.
- **Al abrirlo encontrás:** convención de versionado, formato de changelog, clasificación del feedback (crítico/mejora/cosmético/ambiguo/out-of-scope), cuándo bloquear el prompt como final.
- **Relacionado con:** `protocolo-entrega-cliente.md`, `02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` (las reglas que no se pueden romper en iteración).
- **Status:** estable.

---

## ETAPA 3 — Lanzamiento

📁 `01-metodologia/03-ETAPA3-Lanzamiento/`

Esta Etapa no tiene Pasos definidos todavía — los archivos viven sueltos en la raíz de la carpeta.

### `protocolo-implementacion.md`

- **Qué hace:** define las fases de carga en Prometheo después de que el cliente aprueba la Guía Implementador.
- **Cuándo se usa:** cuando arranca la fase técnica de configuración del agente en la plataforma.
- **Al abrirlo encontrás:** orden de carga (estructura base → variables → tags → seguimientos → prompt → integraciones), checklist de cierre, errores comunes, cuándo escalar a ITESA.
- **Relacionado con:** `protocolo-go-live.md` (siguiente fase), `02-ETAPA2-Diseno/06-estructura-guia-implementador.md` (input del implementador).
- **Status:** estable.

### `protocolo-go-live.md`

- **Qué hace:** define las 3 sub-fases del Go-Live (Testing interno → activación con tráfico limitado → salida en vivo MVP).
- **Cuándo se usa:** después de cargar todo en Prometheo, antes de exponer al agente a tráfico real.
- **Al abrirlo encontrás:** criterios de cada sub-fase, 3 opciones de activación limitada (por canal/horario/proyecto), métricas mínimas, checklist completo, plan de rollback.
- **Relacionado con:** `protocolo-implementacion.md` (fase previa), `04-ETAPA4-Mejora-Continua/protocolo-monitoreo.md` (Etapa siguiente).
- **Status:** estable.

---

## ETAPA 4 — Mejora Continua

📁 `01-metodologia/04-ETAPA4-Mejora-Continua/`

Esta Etapa no tiene Pasos definidos todavía — los archivos viven sueltos en la raíz de la carpeta.

### `protocolo-monitoreo.md`

- **Qué hace:** define cómo se monitorea el agente post Go-Live durante las primeras 2 semanas y después en régimen continuo.
- **Cuándo se usa:** desde el día 1 del Go-Live en adelante.
- **Al abrirlo encontrás:** las 4 dimensiones de monitoreo (volumen, calidad, funnel, equipo), ritmo de revisión, tipos de ajuste post-launch, formato de reporte, métricas de éxito.
- **Relacionado con:** `../03-ETAPA3-Lanzamiento/protocolo-go-live.md` (fase previa), `../02-ETAPA2-Diseno/02-PASO2-Diseno-Agente-IA/protocolo-iteracion-prompt.md` (ajustes estructurales requieren rediseño).
- **Status:** estable.

---

## 06-RUBROS

📁 `01-metodologia/06-rubros/`

Skills verticales con patrones FIJOS y FLEXIBLES por rubro. Cada uno tiene tabla de aplicación de las 24 reglas de las Reglas Diseño de Prometheo by AUREA.

### `00-sistema-fija-flexible.md`

- **Qué hace:** explica el sistema de marcado [FIJA] / [FLEXIBLE] que usan todas las skills verticales. Una regla [FIJA] no cambia entre clientes del rubro; una [FLEXIBLE] varía y tiene una pregunta de discovery asociada.
- **Cuándo se usa:** al leer cualquier skill vertical y al verificar si un Discovery está completo.
- **Al abrirlo encontrás:** definición de [FIJA] y [FLEXIBLE] con ejemplos, cómo se usa al diseñar un cliente, el check de cierre de Etapa 1.
- **Relacionado con:** las 4 skills `prometheo-vertical-*`, `prometheo-discovery-transversal` (gate de cierre).
- **Status:** estable.

### `01-real-estate.md`

- **Qué hace:** documenta los patrones específicos del rubro desarrollista inmobiliario.
- **Cuándo se usa:** al diseñar agentes para clientes desarrollistas (G&D, EDFAN RE, TKVA, futuros).
- **Al abrirlo encontrás:** tipología macro (proyecto/desarrollo), variables específicas, Smart Tags, calificación inversor vs vivienda, canal B2B inmobiliarias, integración Tokko, sección sobre integración con catálogo digital.
- **Relacionado con:** `PROTOTIPO-g-d-developers.md`, `02-skills/00-TRANSVERSAL/prometheo-vertical-real-estate/SKILL.md`.
- **Status:** estable.

### `02-mobiliario.md`

- **Qué hace:** documenta los patrones específicos del rubro mobiliario.
- **Cuándo se usa:** al diseñar agentes para clientes de mobiliario (BETROX, futuros).
- **Al abrirlo encontrás:** tipología macro (línea de producto), variables de personalización, estándar vs configurable vs a medida, showroom como punto de conversión, B2B con arquitectos/diseñadores, sección sobre integración con catálogo digital.
- **Relacionado con:** `PROTOTIPO-betrox.md`, `02-skills/00-TRANSVERSAL/prometheo-vertical-mobiliario/SKILL.md`.
- **Status:** estable.

### `03-insumos-construccion.md`

- **Qué hace:** documenta los patrones específicos del rubro insumos para construcción.
- **Cuándo se usa:** al diseñar agentes para clientes de insumos (EDFAN Productos, ZATOH, futuros).
- **Al abrirlo encontrás:** tipología macro (categoría + tipo de cliente), variables, jerga ambigua del rubro ("alisado" → microcemento o hormigón alisado), múltiples comerciales por tipo de obra, sección sobre integración con catálogo digital.
- **Relacionado con:** `PROTOTIPO-edfan-productos.md`.
- **Status:** [VALIDADO PARCIAL]. Algunos patrones pendientes de confirmar con más casos.

### `04-inmobiliaria-tradicional.md`

- **Qué hace:** documenta los patrones específicos del rubro inmobiliaria tradicional (stock externo de propietarios terceros).
- **Cuándo se usa:** al diseñar agentes para inmobiliarias con catálogo de propiedades de terceros.
- **Al abrirlo encontrás:** tipología macro (propiedad), integración ficha.info/Tokko, multi-portal (Zonaprop, MercadoLibre, etc.), stock super dinámico, sección sobre integración con catálogo digital.
- **Relacionado con:** caso Paganini (referencia parcial, no cliente activo).
- **Status:** estable.

---

## 07-CONVENCIONES-AUREA

📁 `01-metodologia/07-convenciones-aurea/`

### `01-paleta-y-colores.md`

- **Qué hace:** define la paleta hex oficial de AUREA + asignación de colores por proceso del CRM.
- **Cuándo se usa:** al generar cualquier entregable visual (DOCX, gráficos, presentaciones).
- **Al abrirlo encontrás:** paleta completa con códigos hex, asignación por proceso (verde=venta, naranja=soporte, azul=FAQ, morado=seguridad, gris=postventa, rojo=urgencia/alerta).
- **Relacionado con:** `04-convenciones-docx-cliente.md`, `02-metodologia-graficos.md`, `02-skills/02-ETAPA2/prometheo-crm-graphics/SKILL.md`.
- **Status:** estable.

### `02-metodologia-graficos.md`

- **Qué hace:** define el sistema visual de los SVGs que aparecen en el DOCX cliente-facing.
- **Cuándo se usa:** al generar gráficos para el DOCX (los 8 gráficos típicos).
- **Al abrirlo encontrás:** estilo visual de cada tipo de gráfico (embudo, ficha de variable, card de tag, cronograma, etc.), reglas de composición, casos de uso.
- **Relacionado con:** `01-paleta-y-colores.md`, `02-skills/02-ETAPA2/prometheo-crm-graphics/SKILL.md`.
- **Status:** estable.

### `03-naming-convention.md`

- **Qué hace:** define cómo se nombran los archivos entregables y los conceptos internos.
- **Cuándo se usa:** al guardar cualquier archivo entregable o al nombrar variables/tags en un prompt.
- **Al abrirlo encontrás:** convenciones por tipo de archivo (`[Cliente] - Diseño de CRM.docx`, `[Cliente] - Prompt - V[N].md`, etc.) y convención snake_case para nombres internos.
- **Relacionado con:** `02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` (Regla 12).
- **Status:** estable.

---

## 08-CASOS-REFERENCIA

📁 `01-metodologia/08-casos-referencia/`

**Sección transversal.** Casos de clientes prototipo o referentes firmes. Sirven como inspiración al diseñar clientes nuevos. **Información menos fija** que la de Rubros — refleja decisiones customizadas para casos puntuales.

### `00-INDEX-referentes.md`

- **Qué hace:** índice de los casos de referencia disponibles.
- **Cuándo se usa:** cuando buscás inspiración para diseñar un cliente nuevo.
- **Al abrirlo encontrás:** lista de los 4 prototipos + status de cada uno.
- **Relacionado con:** los 4 archivos PROTOTIPO de la misma carpeta.
- **Status:** estable.

### `00-protocolo-incorporar-nuevo-referente.md`

- **Qué hace:** protocolo para promover un cliente prototipo a referente firme cuando se cierra como caso real productivo.
- **Cuándo se usa:** cuando un cliente AUREA llega a Go-Live exitoso y querés capitalizarlo como referente.
- **Al abrirlo encontrás:** checklist para validar el caso, formato esperado del archivo final, criterios de promoción.
- **Relacionado con:** los archivos PROTOTIPO y PLACEHOLDER.
- **Status:** estable.

### Carpetas de ejemplos reales (templates)

Cuatro carpetas contienen **outputs reales de clientes** que sirven como templates de referencia — muestran cómo se ven los entregables bien hechos:

- **`TKVA-real-estate/`** — los 2 documentos cliente-facing del Paso 1 de Etapa 1 de un desarrollista (Doc de Bienvenida en PDF, Guía Metodológica en `.md`). Referencia de la skill `prometheo-docs-kickoff` — muestra el estándar del material que el cliente recibe antes de R1.
- **`MIA-App-marketplace/`** — caso paradigmático de Etapa 2. Contiene el Prompt V6 del agente y el HTML del DOCX "Diseño de CRM". Referencia del formato V6 del prompt y del estándar visual del DOCX.
- **`G-D-Developers-real-estate/`** — los 3 documentos de Etapa 1 de un desarrollista (Doc 1 Síntesis, Doc 2 Asincrónico, Doc 3 Accesos). Referencia de los entregables de Discovery en real estate.
- **`BETROX-mobiliario/`** — el ciclo completo de Etapa 1 de un cliente de mobiliario (Formulario completado, Doc 0 Análisis interno, Doc 1 Síntesis). Referencia de cómo se pasa de la reunión al documento aprobable.

Estos archivos conservan el nombre real del cliente y el rubro, y se usan como modelo de calidad al diseñar clientes nuevos del mismo rubro.

### `PROTOTIPO-mia-app.md`

- **Qué hace:** caso de referencia de MIA App (marketplace inmobiliario). Es el referente del modelo v7 puro.
- **Cuándo se usa:** al diseñar agentes con lógica de marketplace, multi-embudo, o muy alta cantidad de variables.
- **Al abrirlo encontrás:** reglas de diseño Prometheo de MIA, sus Smart Tags, variables, seguimientos, decisiones de diseño relevantes.
- **Relacionado con:** `02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` (MIA validó las reglas), `02-skills/00-TRANSVERSAL/`.
- **Status:** PROTOTIPO. Cerrar versión final ~26 mayo 2026.

### `PROTOTIPO-betrox.md`

- **Qué hace:** caso de referencia de BETROX (mobiliario de hormigón liviano).
- **Cuándo se usa:** al diseñar clientes de mobiliario con catálogo digital + integración PrestaShop.
- **Al abrirlo encontrás:** reglas de diseño Prometheo de BETROX, sus Smart Tags, variables, decisiones de diseño relevantes.
- **Relacionado con:** `06-rubros/02-mobiliario.md`, `02-skills/00-TRANSVERSAL/prometheo-vertical-mobiliario/SKILL.md`.
- **Status:** PROTOTIPO. Cerrar versión final ~26 mayo 2026.

### `PROTOTIPO-g-d-developers.md`

- **Qué hace:** caso de referencia de G&D Developers (desarrollista inmobiliario).
- **Cuándo se usa:** al diseñar clientes desarrollistas con Tokko como CRM, Drive completo y múltiples proyectos.
- **Al abrirlo encontrás:** reglas de diseño Prometheo de G&D, criterios de calificación inversor vs vivienda, decisiones relevantes.
- **Relacionado con:** `06-rubros/01-real-estate.md`, `02-skills/00-TRANSVERSAL/prometheo-vertical-real-estate/SKILL.md`.
- **Status:** PROTOTIPO. Cerrar versión final ~26 mayo 2026.

### `PROTOTIPO-edfan-productos.md`

- **Qué hace:** caso de referencia de EDFAN Productos (insumos para construcción).
- **Cuándo se usa:** al diseñar clientes de insumos con catálogo PrestaShop, jerga técnica ambigua, y múltiples comerciales.
- **Al abrirlo encontrás:** árbol de decisión de Paula (agente EDFAN), 9 tipos de derivación, regla "una subvariable por turno".
- **Relacionado con:** `06-rubros/03-insumos-construccion.md`.
- **Status:** PROTOTIPO. Cerrar versión final ~26 mayo 2026.

### `PLACEHOLDER-referente-prompt-01.md` y `PLACEHOLDER-referente-crm-01.md`

- **Qué hace:** placeholders reservados para el primer prompt y el primer CRM de referencia firme.
- **Cuándo se usa:** se llenan cuando el primer cliente productivo califica como referente.
- **Al abrirlo encontrás:** estructura esperada del archivo final + instrucciones de cómo llenarlo.
- **Relacionado con:** `00-protocolo-incorporar-nuevo-referente.md`.
- **Status:** placeholder vacío. A llenar cuando aparezca el caso.

### `PLACEHOLDER-referente-prompt-02.md` y `PLACEHOLDER-referente-crm-02.md`

- **Qué hace:** placeholders reservados para futuros referentes (segundo prompt y segundo CRM de referencia).
- **Cuándo se usa:** se llenan cuando un cliente productivo califica como referente firme.
- **Al abrirlo encontrás:** estructura esperada del archivo final + instrucciones de cómo llenarlo.
- **Relacionado con:** `00-protocolo-incorporar-nuevo-referente.md`.
- **Status:** placeholder vacío. A llenar cuando aparezca el caso.

---

# 02-SKILLS — Skills para Claude.ai

📁 `02-skills/`

> **Organización:** desde la v1.6, las skills están organizadas **por etapa** en
> `02-skills/`: `00-TRANSVERSAL/`, `01-ETAPA1/`, `02-ETAPA2/`, `03-ETAPA3/`, `04-ETAPA4/`,
> `05-templates/`. Cada carpeta de etapa tiene su propio README. Las descripciones de abajo
> están agrupadas por esa misma estructura.

## 00-TRANSVERSAL/ — skills que aplican a más de una etapa

### `project-instructions-universal.md` ⭐

- **Qué hace:** instrucciones de proyecto para Claude.ai que se cargan SIEMPRE al iniciar un proyecto AUREA con un cliente nuevo.
- **Cuándo se usa:** se pegan en la sección "Project Instructions" de cualquier proyecto Claude.ai dedicado a un cliente.
- **Al abrirlo encontrás:** workflow estándar de las 4 Etapas, principios transversales, reglas de comportamiento, naming, qué memoria mantener, qué tools usar.
- **Relacionado con:** la skill orquestadora `prometheo-etapa2-design/`, las skills verticales, las Reglas Diseño de Prometheo by AUREA.
- **Status:** estable. Vive en `02-skills/00-TRANSVERSAL/` porque aplica a todas las etapas.

---

### `prometheo-vertical-real-estate/`

- **Qué hace:** skill vertical para clientes desarrollistas inmobiliarios. Define slots verticales: tipología macro (proyecto/desarrollo), variables por proyecto, calificación inversor vs vivienda, B2B inmobiliarias, integración Tokko, reventa, financiación, routing por zona. Cada regla marcada [FIJA] o [FLEXIBLE]. Caso de referencia: G&D Developers.
- **Cuándo se usa:** SIEMPRE junto con `prometheo-discovery-transversal/` cuando el cliente sea desarrollista, constructora con proyectos propios, emprendimientos.
- **Al abrirlo encontrás:** los slots verticales que llenan los bloques del discovery transversal con la lógica de real estate.
- **Relacionado con:** `prometheo-formulario-real-estate/`, `01-metodologia/06-rubros/01-real-estate.md`, `08-casos-referencia/PROTOTIPO-g-d-developers.md`.
- **Status:** estable.

### `prometheo-vertical-mobiliario/`

- **Qué hace:** skill vertical para clientes de mobiliario (muebles, equipamiento, decoración, mobiliario urbano). Define slots verticales: tipología macro (línea de producto), variables de personalización, estándar vs configurable vs a medida, showroom, B2B arquitectos/diseñadores, ciclo de personalización. Caso de referencia: BETROX.
- **Cuándo se usa:** SIEMPRE junto con `prometheo-discovery-transversal/` cuando el cliente sea de muebles, mobiliario, equipamiento.
- **Al abrirlo encontrás:** los slots verticales que llenan los bloques del discovery con la lógica de mobiliario.
- **Relacionado con:** `prometheo-formulario-mobiliario/`, `01-metodologia/06-rubros/02-mobiliario.md`, `08-casos-referencia/PROTOTIPO-betrox.md`.
- **Status:** estable.


## 01-ETAPA1/ — skills de la Etapa 1 (Discovery)

### `prometheo-etapa1/` ⭐ ORQUESTADORA

- **Qué hace:** skill orquestadora de toda la Etapa 1. Es el **punto de entrada único** para un implementador que arranca el Discovery de un cliente. No contiene metodología propia: coordina las skills especializadas en el orden correcto y le dice al implementador qué hacer en cada paso.
- **Cuándo se usa:** al arrancar un cliente nuevo, o cuando el implementador no sabe por dónde empezar en Etapa 1.
- **Al abrirlo encontrás:** el mapa de ruta completo de Etapa 1 (PASO 1 Pre-Discovery + PASO 2 Discovery), qué skill activar en cada sub-paso, el checklist de cierre, los errores comunes a evitar.
- **Relacionado con:** todas las skills de Etapa 1 (las coordina), `prometheo-etapa2-design/` (toma el relevo al cerrar).
- **Status:** estable.

### `prometheo-auditoria-web/` ⭐

- **Qué hace:** skill del Paso 1.1 de Etapa 1. Analiza web + Instagram del cliente ANTES de la primera reunión. Genera Doc 0 (interno AUREA) con inventario pre-armado, hipótesis de tipología macro, preguntas cerradas para R1.
- **Cuándo se usa:** al recibir URL/IG de un cliente nuevo, ANTES de R1. Se ejecuta antes de la skill `prometheo-docs-kickoff`.
- **Al abrirlo encontrás:** qué analizar (arquitectura web, catálogo, canales, IG), formato del Doc 0, conexión con la plantilla del formulario del rubro.
- **Relacionado con:** `prometheo-docs-kickoff/` (la dispara con el Doc 0 como input), `prometheo-discovery-transversal/`, las skills `prometheo-formulario-[rubro].md`.
- **Status:** estable.

### `prometheo-docs-kickoff/` ⭐ (skill modular — carpeta con 3 archivos)

- **Qué hace:** genera los 2 documentos cliente-facing del Paso 1 de Etapa 1, los que el cliente recibe antes de R1: (1) el Doc de Bienvenida // Kickoff (DOCX) y (2) la Guía Metodológica (DOCX que se sube a Drive y se abre como Google Doc). Toma como input el Doc 0 de la auditoría web más datos del proyecto (cliente, rubro, consultor asignado, N de reuniones).
- **Cuándo se usa:** después de la auditoría web, antes de R1. "Generar el Doc de Bienvenida", "armar la Guía Metodológica", "material pre-discovery".
- **Al abrirlo encontrás 3 archivos:**
  - `SKILL.md` — orquestador: inputs obligatorios/opcionales, decisión de formato, orden de ejecución con checkpoint entre los 2 docs
  - `doc-bienvenida.md` — estructura del DOCX de Bienvenida: encabezado + 5 secciones, contenido fijo vs adaptable, patrón técnico de generación
  - `guia-metodologica.md` — estructura de la Guía: apertura + 3 documentos vivos + cierre, generación DOCX, conversión a Google Doc
- **Relacionado con:** `prometheo-auditoria-web/` (produce el Doc 0, su input), `prometheo-etapa1/` (la invoca en Pasos 1.2 y 1.3), `01-metodologia/01-ETAPA1-Discovery/01-PASO1-Pre-Discovery/` (los 2 templates de base), `08-casos-referencia/TKVA-real-estate/` (caso de referencia).
- **Status:** estable.

### `prometheo-discovery-transversal/` ⭐

- **Qué hace:** skill metodológica base de toda la Etapa 1 (Discovery). Define los bloques del Discovery (estructura-discovery.md), los 4 docs output (Doc 1 Síntesis, Doc 2 Asincrónico, Doc 3 Accesos, Doc 4 Preguntas Clave), las convenciones UX/UI de colores, el framework de seguimientos, las 5 métricas core Prometheo.
- **Cuándo se usa:** SIEMPRE que se trabaje con un Discovery. Se acopla con la skill vertical del rubro y después de la auditoría web.
- **Al abrirlo encontrás:** sistema completo del Discovery, bloques con slots verticales, framework de seguimientos, transición a Etapa 2.
- **Relacionado con:** `prometheo-etapa1/` (la orquesta), `prometheo-auditoria-web/` (Paso 0), las skills verticales, `prometheo-etapa2-design/` (siguiente Etapa).
- **Status:** estable.

### `prometheo-audit-doc1/`

- **Qué hace:** skill de control de calidad para auditar si la información del formulario de reunión fue transferida correcta y completamente al Doc 1 de Síntesis. Genera reporte de auditoría con estado por dato.
- **Cuándo se usa:** SIEMPRE después de generar un Doc 1. "Auditar", "control de calidad", "cotejar", "verificar doc 1".
- **Al abrirlo encontrás:** comparación dato por dato entre formulario fuente y Doc 1 output, formato de reporte con estado por dato (✅ transferido / ⚠️ parcial / ❌ faltante).
- **Relacionado con:** `prometheo-discovery-transversal/`, las skills `prometheo-formulario-[rubro]/`.
- **Rol:** auditor de calidad de la Etapa 1.
- **Status:** estable.

### `prometheo-formulario-real-estate/`

- **Qué hace:** skill que genera la plantilla del formulario de reunión sincrónico (R1) para clientes de real estate. 16 secciones con 3 capas por pregunta: rosa (pre-llenado de auditoría web), naranja (traducción CRM AUREA), azul (respuesta en reunión).
- **Cuándo se usa:** después de ejecutar la skill de auditoría web (Paso 0), antes de R1.
- **Al abrirlo encontrás:** las 16 secciones del formulario (objetivo, proyectos, equipo, calificación, FAQs, objeciones, flujo, autonomía, etc.) con las 3 capas por pregunta.
- **Relacionado con:** `prometheo-auditoria-web/`, `prometheo-vertical-real-estate/`, `prometheo-discovery-transversal/`.
- **Status:** estable.

### `prometheo-formulario-mobiliario/`

- **Qué hace:** skill que genera la plantilla del formulario de reunión sincrónico para clientes de mobiliario. Misma estructura de 3 capas que real estate, adaptada al rubro.
- **Cuándo se usa:** después de la auditoría web, antes de R1 con un cliente de mobiliario.
- **Al abrirlo encontrás:** 16 secciones adaptadas al rubro mobiliario (líneas producto, personalización, showroom, envío, métodos de pago).
- **Relacionado con:** `prometheo-auditoria-web/`, `prometheo-vertical-mobiliario/`, `prometheo-discovery-transversal/`.
- **Status:** estable.

> **Verticales [PENDIENTE DE CREAR]:** `prometheo-vertical-insumos-construccion/` + `prometheo-formulario-insumos-construccion/` (caso EDFAN Productos), `prometheo-vertical-inmobiliaria-tradicional/` + `prometheo-formulario-inmobiliaria-tradicional/` (caso Paganini).


## 02-ETAPA2/ — skills de la Etapa 2 (Diseño del Agente)

### `prometheo-etapa2-design/` ⭐ (skill modular — carpeta con 6 archivos)

- **Qué hace:** skill maestra que orquesta toda la Etapa 2 (Diseño). Genera los 3 outputs finales: (1) DOCX cliente-facing "Diseño de CRM" con metodología visual AUREA, (2) Prompt del agente en prosa formato V6 listo para pegar en Prometheo, (3) Doc de Refactorización con inconsistencias e info pendiente.
- **Cuándo se usa:** al iniciar el diseño de cualquier cliente. Se puede arrancar antes de cerrar todos los inputs de Etapa 1.
- **Al abrirlo encontrás 6 archivos:**
  - `SKILL.md` — orquestador: inputs, flexibilidad de arranque, secuencia de los 3 outputs
  - `docx_diseno_crm.md` — las secciones del DOCX cliente-facing con metodología visual
  - `prompt_design.md` — formato V6 del prompt (prosa redactada, separadores `===`, sin tablas markdown)
  - `cuadros_explicados.md` — patrón de cuadros "Explicado:" heredado de MIA App
  - `docx_xml_fixes.md` — fixes técnicos para que el DOCX renderice bien
  - `refactorizacion.md` — cómo armar el Doc de Refactorización (3er entregable)
- **Acopla con:** `prometheo-discovery-transversal/` (produce los inputs), `prometheo-crm-graphics/` (gráficos SVG), la skill vertical del rubro.
- **Relacionado con:** `01-metodologia/02-ETAPA2-Diseno/` (metodología que orquesta), `08-casos-referencia/MIA-App-marketplace/` (caso paradigmático).
- **Status:** estable.


### `prometheo-drive-audit-real-estate/`

- **Qué hace:** skill de auditoría sistemática del Drive de un cliente desarrollista inmobiliario. Se ejecuta entre cierre del Doc 1 (Etapa 1) y generación del prompt (Etapa 2). Genera el documento "Matching y Difusión".
- **Cuándo se usa:** al pasar de Etapa 1 a Etapa 2 en clientes desarrollistas. "Auditar Drive de [cliente]", "preparar Etapa 2".
- **Al abrirlo encontrás:** auditoría de carpetas estándar de desarrollistas, extracción de info de brochures, detección de discrepancias entre Doc 1 y Drive real, diseño de slugs y placeholders.
- **Relacionado con:** `prometheo-vertical-real-estate/`, `prometheo-etapa2-design/`.
- **Carpeta:** `02-skills/02-ETAPA2/`.
- **Status:** estable.

### `prometheo-crm-graphics/`

- **Qué hace:** skill para generar SVGs visuales del DOCX cliente-facing de Etapa 2. Versión completa (785 líneas) con estándar visual AUREA, paleta de colores, tipos de gráficos transversales, patrones "Explicado:".
- **Cuándo se usa:** al armar el DOCX en Ronda 1 del Paso 2 de Etapa 2.
- **Al abrirlo encontrás:** principios visuales AUREA, gráficos transversales (mapa embudos, overview variables, arquitectura router, smart tags, escenarios, seguimientos, derivación), cuadros "Explicado:".
- **Relacionado con:** `prometheo-etapa2-design/` (orquesta), `01-metodologia/07-convenciones-aurea/02-metodologia-graficos.md`.
- **Carpeta:** `02-skills/02-ETAPA2/`.
- **Status:** estable.

### `prometheo-diseno-agente-ia-feedback/`

- **Qué hace:** genera el Documento de Feedback de Demo — un DOCX apaisado, cliente-facing, de dos columnas, donde se registran las correcciones al agente detectadas al probar la demo en Prometheo. Izquierda: la captura de la respuesta a corregir. Derecha: qué está mal y cómo debería responder.
- **Cuándo se usa:** en la fase de iteración del prompt (Etapa 2, Paso 2). El consultor lo completa primero en vivo con el cliente y después el cliente lo completa de forma asincrónica.
- **Al abrirlo encontrás:** `SKILL.md` (orquestador), `generar_documento.js` (script de generación del DOCX) y `ejemplo-output.docx` (documento de muestra).
- **Relacionado con:** `01-metodologia/02-ETAPA2-Diseno/02-PASO2-Diseno-Agente-IA/protocolo-feedback-demo.md` (su fuente de verdad), `protocolo-iteracion-prompt.md` (el feedback se clasifica con esa matriz), `prometheo-docs-kickoff/` (skill hermana, documentos cliente-facing de Etapa 1).
- **Carpeta:** `02-skills/02-ETAPA2/`.
- **Status:** estable.


## 03-ETAPA3/ y 04-ETAPA4/ — skills de Lanzamiento y Mejora Continua

Sin skills creadas todavía. Cada carpeta tiene un README con los pendientes (orquestadora de etapa + auditor de etapa). La metodología de ambas etapas ya está documentada en `01-metodologia/`.

## 05-templates/ (templates de entregables)

### `README-cliente-template.md`

- **Qué hace:** plantilla del README que se entrega al cliente en la carpeta Drive del proyecto.
- **Cuándo se usa:** al armar la carpeta de Drive del cliente al inicio de Etapa 1.
- **Status:** estable.

### `docx-diseno-crm-template.md`

- **Qué hace:** plantilla del DOCX cliente-facing que se entrega en Ronda 1 del Paso 2 de Etapa 2.
- **Cuándo se usa:** al generar el DOCX para cualquier cliente.
- **Status:** estable.

### `prompt-template.md`

- **Qué hace:** plantilla del Prompt V1 con las secciones + anexos.
- **Cuándo se usa:** al generar el prompt V1 para cualquier cliente.
- **Status:** estable.

### `guia-implementador-template.md`

- **Qué hace:** plantilla de la Guía Implementador que se entrega en Ronda 2 del Paso 2 de Etapa 2.
- **Cuándo se usa:** al generar la Guía para cualquier cliente después de aprobar Ronda 1.
- **Status:** estable.

# Cómo empezar (3 escenarios)

### Escenario A — Cliente nuevo, arrancando de cero

1. Cargar en Claude.ai la skill orquestadora `prometheo-etapa1/` — te guía por todo el Discovery
2. Ejecutar la auditoría web con `prometheo-auditoria-web/` → genera el Doc 0
3. Generar los 2 documentos cliente-facing con `prometheo-docs-kickoff/` → Doc de Bienvenida + Guía Metodológica
4. Enviar ambos al cliente antes de R1

### Escenario B — Cliente en Discovery, hay que diseñar Etapa 2

1. Confirmar que la Biblia está validada (Etapa 1 cerrada con `protocolo-validacion-biblia.md`)
2. Abrir `01-metodologia/02-ETAPA2-Diseno/01-operativa-y-decisiones.md`
3. Cargar en Claude.ai: `project-instructions-universal.md` + `prometheo-etapa2-design/` + skill vertical del rubro
4. Generar Prompt V1 + DOCX siguiendo Ronda 1 del `protocolo-entrega-cliente.md`

### Escenario C — Cliente con Etapa 2 aprobada, hay que implementar

1. Abrir `01-metodologia/03-ETAPA3-Lanzamiento/protocolo-implementacion.md`
2. Cargar config en Prometheo según la Guía Implementador
3. Ejecutar las 3 sub-fases de `protocolo-go-live.md` (Testing → activación con tráfico limitado → salida en vivo MVP)
4. Activar `protocolo-monitoreo.md` desde el día 1

---

# Principios transversales

Aplican a todas las Etapas:

1. **Iteración esperada.** Ningún entregable se cierra de una pasada.
2. **El cliente no aprende jerga técnica.** Variables, Smart Tags, embudos se traducen a lenguaje de negocio.
3. **Lo que está en Tokko/PrestaShop no se hardcodea.** Toda info de catálogo viene de la integración.
4. **Una sola Smart Tag activa por conversación.** Regla inviolable v7.
5. **MVP primero.** Mejor poco bien hecho que mucho a medias.
6. **Cada rubro tiene su tipología macro.** No se intercambia.
7. **El discovery es conversacional.** Al cliente nunca se le pregunta sobre taxonomía CRM.
8. **Color por proceso, no por capricho.** Verde=venta, naranja=soporte, azul=FAQ, morado=seguridad, gris=postventa, rojo=urgencia/alerta.

---

# Mantenimiento de este manual

**Antes de incorporar cualquier cambio**, leer `01-metodologia/protocolo-extension-metodologia.md` —
define cómo extender la metodología sin romperla (fuente única + punteros).

**Cuándo actualizar este README:**
- Cuando se agregue un archivo nuevo al ZIP
- Cuando se elimine un archivo del ZIP
- Cuando cambie el status de un archivo (de prototipo a estable, por ejemplo)
- Cuando se incorpore un nuevo rubro

**Versionado:**
- Cambios menores: actualizar fecha al inicio del archivo
- Cambios estructurales (carpetas nuevas, reorganización): bump de versión del ZIP
- Todo cambio se registra en `CHANGELOG.md`

**Responsable:** Valentín Zas, con apoyo de Magalí Domínguez y consultores asignados (Rodrigo Buono).

---

**Equipo AUREA Hub** · *Master Partner Prometheo*
