---
name: aurea-ic-tablero
description: Conductor de punta a punta para crear, actualizar o auditar un tablero de Inteligencia Comercial de AUREA (HTML autocontenido sobre Prometheo, Meta, Tokko y canales) para cualquier cliente (EDFAN, DRAKON, PAVIR, TKVA o nuevos). Ordena el trabajo en pasos y carga en cada uno la skill que corresponde (aurea-metodologia, aurea-curaduria-dato, aurea-criterio-comercial, skills de canal, aurea-dashboard-design), y pide los insumos que falten antes de armar nada. Usala SIEMPRE que se pida "armá el tablero", "tablero de IC", "dashboard de inteligencia comercial", "actualizá el tablero de [cliente]", "nueva quincena / nuevo mes del tablero", "auditá el tablero", o se comparta un export de Prometheo para reportar.
---

# Tablero de Inteligencia Comercial · conductor

Esta skill no reemplaza a las demás: **las ordena**. Cada paso carga una skill
especializada y no se pasa al siguiente sin cerrar el anterior.

El tablero responde cinco preguntas, en este orden, y se organiza por pregunta, no por
canal (el canal es un filtro transversal):

1. ¿Cómo venimos? (panorama y evolución)
2. ¿Qué pide el mercado? (demanda y criterio comercial)
3. ¿Qué trajo resultado? (campañas y anuncios)
4. ¿Qué hago ahora? (decisiones con dueño)
5. ¿De dónde sale esto? (fuentes y última actualización)

Propuesta de valor que el tablero tiene que explicar adentro:
**Meta ve hasta el clic. Prometheo ve del clic a la venta. El cruce por ID de anuncio es el producto.**

---

## Paso 0 · Insumos (pedí lo que falte, no supongas)

| Insumo | Obligatorio | Si falta |
|---|---|---|
| Cliente y rubro | Sí | Preguntar |
| Período (quincena o mes) y período anterior para deltas | Sí | Preguntar |
| Export de Prometheo (contactos, tags, variables, conversación) | Sí | No se arma el tablero |
| Tablero anterior del cliente, si existe | Si es actualización | Se arma desde cero |
| Perfil de venta del cliente y capa variable elegida | Sí | Resolver en el paso 3 |
| Export de Meta (gasto, alcance, por anuncio y día) | No | Faltante de integración: sin CPL ni ROAS, se declara |
| Tokko (catálogo) | Solo real estate | Demanda sin cruce de producto |
| Campañas de email / WhatsApp masivo | Si las hubo | Se omite la sección de canales propios |
| Registro de cierre del equipo | No | Faltante de proceso: no hay ciclo cerrado, se declara |

Decí explícitamente si los datos son **reales o modelados**.

## Paso 1 · CRM aguas arriba → `aurea-metodologia`

Entender cómo está diseñado el CRM del cliente antes de leer el export: embudos (cada
etapa es una Smart Tag), una tag por dimensión, variables padre e hija condicional,
corte embudo del agente vs embudo humano. Lo que el CRM no registró no se puede reportar.

## Paso 2 · Curaduría del dato → `aurea-curaduria-dato`

Correr su procedimiento de auditoría completo antes de diseñar una sola card:
cobertura real por columna, escalera de evidencia, base curada, denominadores
declarados, etapa declarada vs etapa por evidencia, citas, faltantes por tipo.

Salida de este paso: una tabla variable → cobertura → origen → nivel → pestaña donde vive.

## Paso 3 · Criterio comercial → `aurea-criterio-comercial`

Elegir la capa variable según el perfil del cliente, medir los cinco campos del núcleo
(problema, impacto, causa raíz, disparador, resultado de contacto) y decidir qué puede
mostrarse según su nivel de evidencia.

## Paso 4 · Atribución, RevOps y canales

- Atribución por ID de anuncio y calidad por anuncio (respuesta, identificación,
  calificación, derivación) con la **misma definición de cohorte** en todo el tablero.
  Marco de referencia: skill `attribution` si está instalada.
- Ciclo de vida, etapas, handoff: skill `revops` si está instalada.
- Email: `aurea-email-prometheo` (CTOR, empalme, la apertura no titula).
- WhatsApp masivo: `aurea-whatsapp-prometheo` (titula la respuesta, no la lectura; tier
  y calidad del número).
- Si una de estas skills no está disponible, seguí con las reglas de
  `references/cuerpo-de-conocimiento.md` (capas 3 y 4) y avisá qué skill faltó.

## Paso 5 · Diseño y armado → `aurea-dashboard-design`

Doctrina Básico / Avanzada (un número, un nombre), KPI con delta obligatorio, embudo
como pasos y no a escala, color semántico separado del de marca, modo oscuro, estados
vacíos, fecha de actualización por fuente, chips de cobertura y tags de nivel de la
curaduría. HTML autocontenido, assets en WebP, objetivo de peso menor a 250 KB.

## Paso 6 · Control antes de entregar

- [ ] Checklist de `aurea-curaduria-dato` completo.
- [ ] Checklist de `aurea-criterio-comercial` completo.
- [ ] Cotejar cifra por cifra contra la fuente (evita dos criterios de cohorte en la misma pantalla).
- [ ] Ninguna cifra suma Meta + Prometheo.
- [ ] Las cinco preguntas tienen respuesta, o un estado vacío diseñado que dice por qué no.
- [ ] Faltantes de integración (Meta, cierre) declarados en "¿De dónde sale esto?".
- [ ] El switch Básico / Avanzada cambia algo en todas las vistas.
- [ ] Peso del HTML verificado; las últimas pestañas cargan.

## Referencias

- `references/cuerpo-de-conocimiento.md`: el producto completo, el caso EDFAN, el estado
  de la atribución, lo que se puede y no se puede medir, y el vocabulario común.
  Leelo cuando haya dudas de definición o se trabaje con alguien nuevo.
