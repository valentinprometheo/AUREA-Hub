# Diagramas — AUREA Hub × Prometheo

Vista visual de la metodología en 4 ETAPAS. Complementa el `README.md` (manual de instrucciones).

---

## 1. La metodología en 4 Etapas

```mermaid
flowchart LR
    A["<b>ETAPA 1</b><br/>Discovery<br/>━━━━━━<br/><br/>PASO 1 · Pre-Discovery<br/>• Auditamos web e Instagram<br/>• Doc de Bienvenida al cliente<br/>• Guía Metodológica al cliente<br/><br/>PASO 2 · Discovery<br/>• Biblia del negocio<br/>• Asincrónico<br/>• Accesos y material"]:::e1

    B["<b>ETAPA 2</b><br/>Diseño<br/>━━━━━━<br/><br/>PASO 1 · Diseño del CRM<br/>PASO 2 · Diseño Agente IA<br/>(iteración V1→V2→V3)<br/>PASO 3 · Implementación<br/>del CRM en Prometheo"]:::e2

    C["<b>ETAPA 3</b><br/>Lanzamiento<br/>━━━━━━<br/><br/>• Cargamos en Prometheo<br/>• Probamos internamente<br/>• Activación con tráfico<br/>  limitado → en vivo MVP"]:::e3

    D["<b>ETAPA 4</b><br/>Mejora Continua<br/>━━━━━━<br/><br/>• Monitoreo de KPIs<br/>• Iteración con datos<br/>  reales<br/>• Mejoras al prompt"]:::e4

    A --> B --> C --> D

    classDef e1 fill:#7C5CBF,color:#fff
    classDef e2 fill:#E8943A,color:#fff
    classDef e3 fill:#3FA89E,color:#fff
    classDef e4 fill:#4CAF80,color:#fff
```

Cada Etapa tiene **iteración y validación con el cliente**. No hay entregables cerrados de una sola pasada.

---

## 2. Flujo cronológico de un proyecto típico

```mermaid
flowchart LR
    Start([🤝 Firma]):::start

    P1["<b>ETAPA 1</b><br/>Discovery<br/>━━━━━━<br/>duración media-larga<br/><br/>• Auditamos cliente<br/>• Doc de Bienvenida<br/>• Reuniones con cliente<br/>• Biblia validada"]:::e1

    P2["<b>ETAPA 2</b><br/>Diseño<br/>━━━━━━<br/>duración corta-media<br/><br/>• Diseño CRM<br/>• Diseño Agente IA<br/>  (iteración V1→V2→V3)<br/>• Implementación CRM"]:::e2

    P3["<b>ETAPA 3</b><br/>Lanzamiento<br/>━━━━━━<br/>duración media<br/><br/>• Cargamos en Prometheo<br/>• Probamos internamente<br/>• Salida en vivo gradual"]:::e3

    P4["<b>ETAPA 4</b><br/>Mejora Continua<br/>━━━━━━<br/>continuo<br/><br/>• Monitoreo<br/>• Iteraciones con datos<br/>  reales del agente"]:::e4

    End([✨ Mejora continua]):::endd

    Start --> P1 --> P2 --> P3 --> P4 --> End

    classDef start fill:#2D2D3D,color:#fff
    classDef e1 fill:#7C5CBF,color:#fff
    classDef e2 fill:#E8943A,color:#fff
    classDef e3 fill:#3FA89E,color:#fff
    classDef e4 fill:#4CAF80,color:#fff
    classDef endd fill:#2D2D3D,color:#fff
```

**Duración total típica:** entre la firma del contrato y el lanzamiento del agente en vivo, un proyecto promedio para cliente de escala media (tipo TKVA o EDFAN) lleva un período largo. Lo importante es el ritmo de iteración, no la velocidad.

---

## 3. Skills por rubro

```mermaid
flowchart TB
    Universal["<b>Project Instructions</b><br/>━━━ universales ━━━<br/>SIEMPRE cargado<br/>en cualquier cliente"]:::base

    Principal["<b>Skill maestra</b><br/>━━━ Diseño Etapa 2 ━━━<br/>Orquesta todo el diseño<br/>del agente del cliente"]:::principal

    Graphics["<b>Skill de Gráficos</b><br/>━━━ prometheo-crm-graphics ━━━<br/>Genera los SVGs visuales<br/>del Documento cliente"]:::graphics

    RE["<b>Real Estate</b><br/>━━━ desarrollistas ━━━<br/>Clientes: TKVA,<br/>G&D, EDFAN RE"]:::p2

    MOB["<b>Mobiliario</b><br/>━━━━━━<br/>Cliente: BETROX"]:::p4

    INS["<b>Insumos para<br/>construcción</b><br/>━━━━━━<br/>Clientes: EDFAN<br/>Productos, ZATOH"]:::p5

    INM["<b>Inmobiliaria<br/>tradicional</b><br/>━━━━━━<br/>Referencia: Paganini"]:::p6

    Universal --> Principal
    Principal --> Graphics
    Principal --> RE
    Principal --> MOB
    Principal --> INS
    Principal --> INM

    classDef base fill:#2D2D3D,color:#fff
    classDef principal fill:#7C5CBF,color:#fff
    classDef graphics fill:#E8943A,color:#fff
    classDef p2 fill:#5B8FD9,color:#fff
    classDef p4 fill:#4CAF80,color:#fff
    classDef p5 fill:#3FA89E,color:#fff
    classDef p6 fill:#F37D6E,color:#fff
```

**Regla:** siempre se cargan las Project Instructions universales + la Skill maestra de Diseño Etapa 2 + la Skill vertical del rubro del cliente.

---

## 4. Relaciones entre archivos clave

```mermaid
flowchart LR
    Inputs["<b>Lo que aporta el cliente</b><br/>━━━━━━<br/><br/>• Biblia del negocio<br/>• Asincrónico<br/>• Accesos y material"]:::inputs

    Metodologia["<b>Reglas y método AUREA</b><br/>━━━━━━<br/><br/>• Reglas Diseño Prometheo<br/>  by AUREA (24 reglas)<br/>• Trazabilidad<br/>  Discovery → Diseño<br/>• Operativa de Etapa 2"]:::metodologia

    Convenciones["<b>Convenciones de entregables</b><br/>━━━━━━<br/><br/>• Convenciones del Documento<br/>• Estructura del Prompt<br/>• Estructura de la Guía técnica<br/>• Patrones del rubro"]:::convenciones

    Skills["<b>Skills que orquestan</b><br/>━━━━━━<br/><br/>• Skill maestra Diseño Etapa 2<br/>• Skill de Gráficos<br/>• Skill vertical del rubro"]:::skills

    Outputs["<b>Lo que entregamos al cliente</b><br/>━━━━━━<br/><br/>• Documento de diseño en Word<br/>• Prompt del agente<br/>  versionado V1+<br/>• Guía para implementador"]:::outputs

    Inputs --> Skills
    Metodologia --> Skills
    Convenciones --> Skills
    Skills --> Outputs

    classDef inputs fill:#5B8FD9,color:#fff
    classDef metodologia fill:#7C5CBF,color:#fff
    classDef convenciones fill:#E8943A,color:#fff
    classDef skills fill:#4CAF80,color:#fff
    classDef outputs fill:#3FA89E,color:#fff
```

---

**Para el manual de instrucciones detallado de cada archivo, ver `README.md`.**
