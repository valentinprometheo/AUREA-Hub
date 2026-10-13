# 00 — INDEX de la Metodología AUREA Hub × Prometheo

> Índice maestro condensado. Para el manual de instrucciones completo de cada archivo, ver `../README.md`.

> **Punto de entrada operativo: `00-CONSULTA.md`** (el router). La metodología se consulta
> por ejes (proceso / rubro / integración / transversal) y se ensambla según la tarea, en
> modo conversación nueva o con trayectoria. Empezá por ahí; este INDEX es el mapa de qué
> archivo es cada cosa.

---

## Las 4 ETAPAS

```
ETAPA 1 — DISCOVERY
├── PASO 1 · Pre-Discovery
│   ├── Auditoría web e Instagram
│   ├── Doc de Bienvenida (cliente-facing)
│   └── Guía Metodológica (cliente-facing)
│
└── PASO 2 · Discovery
    ├── Biblia del negocio (sincrónico, en reuniones)
    ├── Asincrónico (cliente completa con tiempo)
    ├── Accesos y material (Drive compartido)
    ├── Protocolo de validación de la Biblia
    └── Métricas core Prometheo (5 métricas, baseline)

ETAPA 2 — DISEÑO
├── (Contenido teórico transversal)
│   ├── Operativa y decisiones de Etapa 2
│   ├── Trazabilidad Etapa 1 → Etapa 2
│   ├── Reglas Diseño de Prometheo by AUREA
│   ├── Convenciones del DOCX cliente
│   ├── Estructura del Prompt del agente
│   ├── Estructura de la Guía Implementador
│   ├── Reglas de integración con catálogo digital
│   │     (genéricas + doctrina por fuente + 3 sistemas de placeholder)
│   ├── Principios transversales de diseño de agente (10, probados en 2 rubros)
│   ├── Metodología de corrección del agente (trazabilidad corrección→regla + barrido 8+1 + template auditoría)
│   ├── Los 13 patrones de corrección de agentes IA (documento maestro, auditoría de prompt)
│   ├── Contradicciones de jerarquía (tercer tipo de error: reglas propias que compiten)
│   ├── Lógica comercial transversal (cómo VENDE el agente; patrón vs instancia)
│   ├── Gestión del proveedor Prometheo/ITESA (3 actores, auditar reescrituras, dossier de incidentes)
│   ├── Guión de testing (primos, marca PLATAFORMA, regresión)
│   ├── Estructura de la Guía de Implementador (familia 7, 3 casos reales de referencia)
│   ├── Arquitectura de CRM por rubro (moldes de embudos/tags/variables para calcar)
│   ├── Inteligencia Comercial — el producto (dashboard sobre export de Prometheo)
│   ├── Restricciones de la plataforma Prometheo
│   └── Sistema de mensajería automatizada — 5 mecanismos (antes "Framework de seguimientos")
│
├── PASO 1 · Diseño del CRM
│   └── (orquestado por skill prometheo-etapa2-design)
│
├── PASO 2 · Diseño del Agente IA
│   ├── Protocolo de entrega al cliente (2 rondas)
│   └── Protocolo de iteración del prompt (V1→V2→V3)
│
└── PASO 3 · Implementación del CRM en Prometheo
    └── (pendiente de documentar)

ETAPA 3 — LANZAMIENTO
├── Protocolo de implementación
└── Protocolo de Go-Live
    (Testing interno → tráfico limitado → salida en vivo MVP)

ETAPA 4 — MEJORA CONTINUA
└── Protocolo de monitoreo
    (Primeras 2 semanas + régimen continuo)
```

> **Raíz de metodología:** `00-INDEX.md` (este archivo) + `00-planes-aurea.md` (Plan Start / Pro) + `protocolo-extension-metodologia.md` (cómo extender la metodología sin rehacerla).

---

## Secciones transversales (aplican a todas las Etapas)

```
06-rubros/
├── 00-sistema-fija-flexible.md (cómo se marcan las reglas verticales)
├── 01-real-estate.md (desarrollistas inmobiliarios)
├── 02-mobiliario.md
├── 03-insumos-construccion.md
└── 04-inmobiliaria-tradicional.md

07-convenciones-aurea/
├── 01-paleta-y-colores.md
├── 02-metodologia-graficos.md
└── 03-naming-convention.md

08-casos-referencia/
├── PROTOTIPO-mia-app.md / betrox / g-d-developers / edfan-productos
├── PLACEHOLDERs para futuros referentes
├── TKVA-real-estate/ (Doc Bienvenida + Guía Metodológica — ejemplos Paso 1)
├── MIA-App-marketplace/ (Prompt V6 + DOCX CRM — ejemplos Etapa 2)
├── G-D-Developers-real-estate/ (Doc 1 + 2 + 3 — ejemplos Etapa 1)
└── BETROX-mobiliario/ (Formulario + Doc 0 + Doc 1 — ejemplos Etapa 1)
```

---

## Validaciones de cierre por Etapa

| Etapa | Cómo se cierra |
|---|---|
| Etapa 1 — Pre-Discovery (Paso 1) | Doc de Bienvenida + Guía Metodológica enviados al cliente |
| Etapa 1 — Discovery (Paso 2) | Biblia del negocio validada formalmente por cliente |
| Etapa 2 — Paso 1 (Diseño CRM) | Cliente recibe Documento de diseño CRM (típicamente sin objeciones) |
| Etapa 2 — Paso 2 (Diseño Agente IA) | Cliente aprueba prompt final tras iteraciones V1→V2→V3 + demo |
| Etapa 2 — Paso 3 (Implementación CRM) | CRM cargado en Prometheo según Guía Implementador |
| Etapa 3 — Lanzamiento | Agente en vivo con MVP funcionando |
| Etapa 4 — Mejora Continua | Sin cierre formal — proceso continuo |

---

## Principios transversales

Aplican a todas las Etapas:

1. **Iteración esperada.** Ningún entregable se cierra de una pasada.
2. **El cliente no aprende jerga técnica.** Variables, Smart Tags, embudos se traducen a lenguaje de negocio.
3. **Lo que está en Tokko/PrestaShop no se hardcodea.** Toda info de catálogo viene de la integración.
4. **Una sola Smart Tag activa por conversación.** Regla inviolable de las Reglas Diseño de Prometheo by AUREA.
5. **MVP primero.** Mejor poco bien hecho que mucho a medias.
6. **Cada rubro tiene su tipología macro.** No se intercambia.
7. **El discovery es conversacional.** Al cliente nunca se le pregunta sobre taxonomía CRM.
8. **Color por proceso, no por capricho.** Verde=venta, naranja=soporte, azul=FAQ, morado=seguridad, gris=postventa, rojo=urgencia/alerta.

---

## Cómo navegar este índice

- **Soy consultor nuevo y arranco mi primer cliente:** abrí `../README.md` y leé la sección "Cómo empezar".
- **Arranco la Etapa 2 con un cliente que ya cerró Discovery:** abrí `02-ETAPA2-Diseno/01-operativa-y-decisiones.md`.
- **Necesito entender cómo modelar el estado del lead (embudo, tags, variables):** abrí `02-ETAPA2-Diseno/embudos-y-tags.md`.
- **Tengo que elegir integraciones para un cliente:** abrí `02-ETAPA2-Diseno/integraciones-por-rubro.md`.
- **Voy a cargar contactos / configuración de un cliente en Prometheo:** abrí `02-ETAPA2-Diseno/importacion-contactos.md`.
- **Necesito preparar el Excel de carga del cliente:** abrí `02-ETAPA2-Diseno/excel-carga-clientes.md`.
- **El agente está en demo y el cliente reporta correcciones:** abrí `02-ETAPA2-Diseno/feedback-demo-iteracion.md` (el documento) y `02-ETAPA2-Diseno/metodologia-correccion-agente.md` (el método de procesarlo y trazar corrección→regla).
- **Voy a diseñar el prompt de un agente:** cargá `02-ETAPA2-Diseno/principios-transversales-agente.md` (siempre) + el rubro + la doctrina de la integración del cliente en `02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md`.
- **No sé qué archivos cargar para esta tarea:** abrí `00-CONSULTA.md` (el router) y resolvé los cuatro ejes.
- **Tengo que entregar un documento o presentación al cliente y no sé cuál corresponde:** abrí `00-OUTPUTS-POR-ETAPA.md` (índice de outputs por etapa; los templates viven en la skill `documentos-client-facing`).
- **Necesito auditar un prompt existente:** abrí `02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` y pasá la checklist de las reglas.
- **Estoy diseñando un cliente con catálogo digital:** abrí `02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` para profundizar las Reglas 16-21.
- **Mi cliente es de un rubro específico:** abrí el archivo correspondiente en `06-rubros/`.
- **Necesito un caso de referencia para inspirarme:** abrí `08-casos-referencia/00-INDEX-referentes.md`.

---

**Para el manual de instrucciones detallado de todos los archivos del ZIP, ver `../README.md`.**
