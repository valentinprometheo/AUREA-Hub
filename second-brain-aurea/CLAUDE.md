# CLAUDE.md · AUREA Hub

> Lo primero que lee Claude (Cowork o Claude Code) al abrir esta carpeta. Es un mapa, no un manual:
> ubica y apunta. La doctrina de AUREA vive en las skills de la cuenta (tabla "Mis skills");
> acá vive el **estado**: clientes, decisiones, partners y lo que está abierto.
> Para crecer el sistema: `/brain-coach`.

## Reglas de arranque (siempre)
1. Leé este archivo y después `ESTADO.md`. Si el estado ya responde, no escanees el árbol.
2. Pedido de un cliente: leé **solo** `1. Proyectos/<cliente>/CLAUDE.md` (y su `log.md` si hace falta).
3. Pedido de método (CRM, prompt, calificación, discovery, testing): la skill `aurea-metodologia`
   manda. El estado del cliente sale de acá, la doctrina de la skill. Nunca al revés.
4. Costos y precios: **solo** `ic-costos-y-rentabilidad-de-prometheo` (costos de plataforma) y
   `2. Áreas/pricing/` (cómo cotiza AUREA). Nunca copies una cifra de un documento viejo.
5. Documento para un cliente: `aurea-estetica-documentacion` (deck HTML) o el template legal. Antes
   de mandar, `/brain-verify` (números, fechas y nombres contra la fuente).
6. Lo turbio va a `0. Inbox/`. Al cerrar la sesión, `/brain-doc`: deja la decisión en el log del
   cliente y actualiza `ESTADO.md` ("última vez" y "próximo paso").
7. Datos de clientes bajo NDA: nunca se publican ni salen de esta carpeta sin pedido explícito.

## Quiénes somos
- **AUREA Hub:** consultora y hub comercial. Master Partner Oficial de Prometheo CRM. Un solo
  proceso: vender mejor y saber qué funciona. Ventas primero, marketing después, el dato vuelve.
- **Equipo:** Valen (metodología, producto y venta), Maga (CEO, ventas y alianzas), Rodri
  (implementación y consultoría, modelo de datos), Rama (implementación y ventas), Javier Sculli
  (CTO, arquitectura, costos de construir IC y modelo de pricing).
- Voz: rioplatense con voseo, colega senior, números defendibles. Detalle en `2. Áreas/aurea/`.

## Mapa (PARA)
- **0. Inbox/**: captura sin decidir.
- **1. Proyectos/**: un cliente o lead por carpeta. Tienen fin (cierre, renovación o baja).
  - Activos: `EDFAN Productos`, `EDFAN Real Estate`, `ZATOH`, `BETROX`, `MIA App`, `TKVA`.
  - Hot leads (propuesta enviada, esperando respuesta): `DRAKON`, `PAVIR`, `EAF`, `MAMUT`.
  - A recuperar: `G&D Developers` (suspendió él).
  - Internos: `AUREA Growth` (adquisición propia), `Deck oficial`.
- **2. Áreas/**: lo que no termina. `aurea/` (identidad, equipo, voz), `partners/`, `pricing/`,
  `inteligencia-comercial/`, `marketing-growth/`, `marca-y-documentos/`, `skills-y-metodologia/`.
- **3. Recursos/**: referencias reusables (config de rutinas, plantillas).
- **4. Archivo/**: clientes cerrados o dados de baja, propuestas que no prosperaron.

## Atajos (frase → dónde ir)
| Si digo… | Andá a… |
|---|---|
| "cómo viene [cliente]", "retomemos [cliente]" | `1. Proyectos/<cliente>/CLAUDE.md` |
| "qué leads están esperando", "pipeline" | `ESTADO.md` § Pipeline |
| "partners", "agencias", "Bardo", "Growth Larriera", "Kiri" | `2. Áreas/partners/` |
| "cuánto cobramos", "paquetes", "Esencial / Crecimiento / Escala" | `2. Áreas/pricing/` |
| "tablero", "IC", "inteligencia comercial" | `2. Áreas/inteligencia-comercial/` |
| "growth", "conseguir clientes", "piloto pago" | `1. Proyectos/AUREA Growth/` y `2. Áreas/marketing-growth/` |
| "deck oficial", "presentación final" | `1. Proyectos/Deck oficial/` |
| "estado de las skills", "versión de la metodología" | `2. Áreas/skills-y-metodologia/` |

## Mis skills (frase → skill de la cuenta)
Las skills de AUREA están instaladas en la cuenta de claude.ai; no se copian acá.
| Si digo… | Skill |
|---|---|
| cliente nuevo, "paso 1.1", auditoría web, preparar R1 | `prometheo-auditoria-web` |
| discovery, formulario, Doc 1 a Doc 4 | `prometheo-discovery-transversal` + vertical del rubro |
| "se pasó todo al Doc 1?" | `prometheo-audit-doc1` |
| diseñar o auditar el CRM, calificación, seguimientos, testing | `aurea-metodologia` |
| "corregí el prompt", "sacá la vN", feedback del agente | `aurea-prometheo-corrección-prompts` |
| tablero de IC, nueva quincena, export de Prometheo | `aurea-ic-dashboard` (conductor) |
| vender o explicar IC, objeciones, pitch | `aurea-ic-conocimiento` |
| costos, tokens, Meta, rentabilidad | `ic-costos-y-rentabilidad-de-prometheo` |
| propuesta, presupuesto, deck, guía, one-pager | `aurea-estetica-documentacion` |
| NDA, contrato, cláusula | `aurea-estetica-documentacion` (Familia B) |
| Diseño de CRM, carga de contactos, guión de testing (cliente) | `documentos-client-facing` |
| "qué hago ahora", posibles mejoras, fugas | `aurea-data-action-driven` |
| brief del día | `/brain-triage` |
| qué pasó ayer, ciclo nocturno | `/brain-dreaming` (reuniones desde Drive: `3. Recursos/dreaming-reuniones-gemini.md`) |
| decisiones pendientes en tarjetas | `/brain-decide` |
| revisar antes de mandar | `/brain-verify` y, si pesa, `/brain-panel` |

## Rutinas
| Rutina | Cuándo | Qué hace |
|---|---|---|
| `/brain-dreaming` | todos los días, 05:00 | lee mail, calendario y notas de Gemini en Drive; escribe en el log de cada cliente; marca lo que pide decisión |
| `/brain-triage` | días hábiles, 08:30 | brief: qué cliente espera respuesta, qué reunión viene, qué vence |
| Auditoría de skills | cada versión nueva y los sábados | `python3 herramientas/auditar_ecosistema.py <skills>` + `auditar.py` de la metodología |
| `/brain-audit` | sábados | salud del brain: estados viejos, proyectos sin próximo paso |
