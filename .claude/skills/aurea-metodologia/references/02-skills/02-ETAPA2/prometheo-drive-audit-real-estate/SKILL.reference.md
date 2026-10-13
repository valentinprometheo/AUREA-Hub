---
name: prometheo-drive-audit-real-estate
description: Auditoría sistemática del Drive de un cliente desarrollista inmobiliario y diseño del sistema de placeholders de assets. Se ejecuta entre el cierre del Doc 1 (Etapa 1) y la generación del prompt del agente (Etapa 2). Genera el documento interno AUREA "Matching y Difusión" que sirve como input contextual estructurado para la skill de generación de prompt. Cubre: auditoría de carpetas estándar de desarrollistas (Conversaciones Reales, Info General, Listas de Precios, Material Inmobiliarias, Obras/Proyectos, Videos), extracción de información de brochures, detección de discrepancias entre Doc 1 y Drive real, diseño de slugs y placeholders, decisión MVP simple vs lógica escalonada de difusión, lógica de oferta no mecánica para vendedor inmobiliario. Activar cuando Valentín diga "auditar Drive de [cliente]", "preparar Etapa 2", "armar matching y difusión", "auditoría de assets", "diseñar placeholders" para un cliente desarrollista inmobiliario.
---

# Skill: Pre-Etapa 2 para Desarrollistas Inmobiliarios — Auditoría de Drive y Diseño de Difusión

> Esta skill se ejecuta DESPUÉS de cerrar el Doc 1 de Discovery (Etapa 1) y ANTES de generar el prompt del agente con la skill `prometheo-etapa2-prompt`.
>
> Su output es un documento interno AUREA llamado **"Matching y Difusión v1"** que sirve como input contextual estructurado para la generación del prompt.
>
> Es el equivalente metodológico de lo que se hizo para EDFAN Real Estate (caso de referencia). G&D Developers es el primer cliente al que se le aplica como skill consolidada.

---

## 1. Cuándo activar esta skill

Activar inmediatamente cuando Valentín pida cualquiera de estos:

- "Auditar el Drive de [cliente]"
- "Preparar Etapa 2 para [cliente]"
- "Armar el documento de Matching y Difusión"
- "Diseñar placeholders para [cliente]"
- "Hacer la auditoría de assets de [cliente]"
- "Quiero pre-armar Etapa 2 antes de la primera reunión de diseño"

**Pre-requisitos para ejecutar:**
- Doc 1 de Síntesis cerrado y aprobado por el cliente.
- Acceso al Drive del cliente otorgado.
- Vertical confirmada como **desarrollista inmobiliario** (no agencia, no mobiliario).

**Qué NO es esta skill:**
- No es la skill de generación del prompt (eso es `prometheo-etapa2-prompt`).
- No es discovery de Etapa 1 (eso es `prometheo-discovery-transversal` + `prometheo-vertical-real-estate`).
- No es auditoría web previa a R1 (eso es `prometheo-auditoria-web`).

---

## 2. Carpetas estándar de un Drive de desarrollista

Todo desarrollista organizado tiene alguna versión de esta estructura. La skill busca estas carpetas (los nombres pueden variar, importa lo que contienen):

| Carpeta tipo | Qué contiene | Para qué sirve |
|---|---|---|
| **Conversaciones Reales** | Capturas de WhatsApp, exports de chats reales con leads | Tono real del equipo, FAQs no anticipadas, objeciones reales, frases de cierre que funcionan |
| **Info General (No por Obra)** | Documentos transversales: financiación general, manual de marca, guía de tono, presentación corporativa | Sección 2 del prompt (tono), sección 4 del prompt (contexto de marca) |
| **Listas de Precios + Financiación** | Excel/PDF con precios actualizados por unidad, esquemas de cuotas, anticipos | Lo que NO va al prompt (precio exacto va a Tokko) y lo que SÍ (esquema general de financiación por proyecto) |
| **Material Inmobiliarias** | Brochures con comisiones, fichas técnicas para brokers, lista B2B | Saber si el material para B2B es distinto del material para compradores finales — afecta el flujo de derivación |
| **Obras / Proyectos** | Una subcarpeta por proyecto: brochure, renders, planos, fichas | Inventario maestro para diseño de placeholders |
| **Videos de avances** | Drone shots, recorridos, timelapses, reels | Material vivo (cambia mensualmente) — placeholder dinámico vs derivación a humano |

**Si el cliente tiene una estructura distinta:** mapear cada carpeta del cliente a una de estas categorías antes de seguir. No imponer la estructura — entender la suya.

---

## 3. Procedimiento de auditoría — paso a paso

### Paso 1 — Inventario maestro de proyectos

**Input:** Doc 1 sección B2 (catálogo de proyectos relevado).

**Acción:**
1. Listar todos los proyectos declarados en Doc 1, en una tabla.
2. Para cada proyecto: dirección, barrio, estado de obra, fecha de entrega, tipologías declaradas, precio referencial declarado.
3. Marcar los proyectos prioritarios MVP si el cliente los identificó.

**Output parcial:** Matriz maestra v0 — solo lo declarado por el cliente.

### Paso 2 — Cruce con Drive

**Input:** Matriz maestra v0 + acceso al Drive.

**Acción:** Para cada proyecto declarado, verificar en `/Obras/Proyectos/[proyecto]/`:
- ¿Existe la carpeta? Sí / No.
- Si existe: ¿tiene brochure (PDF principal de venta)? ¿Renders? ¿Planos?
- Peso del brochure en MB (crítico — explico abajo).
- Nombre del archivo del brochure (puede revelar discrepancias).
- Fecha de modificación del material.

**Estados posibles por proyecto:**
- ✅ **Material completo** — brochure + renders presentes, peso < 25 MB.
- ⚠️ **Material parcial** — algo falta (ej: brochure ausente pero hay renders).
- ❌ **Sin carpeta** — proyecto declarado en Doc 1 pero sin presencia en Drive.
- 🔴 **Material pesado** — brochure existe pero supera 25 MB (no se puede enviar por WhatsApp).

**Por qué importa el peso:** WhatsApp tiene un límite operativo de **25 MB por archivo**. Brochures de 40, 60, 140 MB (sí, vi un brochure de 141 MB en EDFAN) no se pueden enviar por el canal principal del agente. Hay dos opciones: pedir al cliente que comprima, o derivar a humano para envío por correo.

### Paso 3 — Detección de discrepancias

Esto es lo más valioso del proceso. Las discrepancias entre lo que dice el Doc 1 y lo que está en el Drive son siempre fuentes de error en el prompt si no se validan antes.

**Discrepancias típicas a buscar:**

| Tipo de discrepancia | Cómo se detecta | Ejemplo real (EDFAN) |
|---|---|---|
| **Marca distinta del desarrollador en el brochure** | El brochure menciona otra desarrolladora | CHALETS Martín Coronado → brochure marca SPAZIOS, no EDFAN. Validar relación: ¿desarrolla o comercializa? |
| **Co-desarrollo no declarado** | El brochure menciona socios/desarrolladoras adicionales | CENTRAL Belgrano → brochure indica MARY&JOE / SIMMONS / Baigún |
| **Tipologías que no coinciden** | Doc 1 dice "X amb", brochure dice "X, Y, Z amb" | BOYACÁ → Doc 1: 2-3 amb. Brochure: 2, 3, 4 y 5 amb |
| **Amenities no declarados** | Brochure detalla amenities que el Doc 1 omite | BOYACÁ → Doc 1 sin amenities. Brochure: piscina, gym, spa, jacuzzi |
| **Archivo mal nombrado** | El nombre del PDF no coincide con el proyecto | EDEN Villa Urquiza → archivo se llama "CARPETA FINAL ZABAL.pdf" |
| **Proyectos confundibles** | Dos proyectos con nombres/direcciones similares y una sola carpeta | "Juan B Justo 3794" vs "Juan B Justo y Cucha Cucha" → carpeta única "JUAN B JUSTO" |
| **Brochure desactualizado** | El brochure está fechado y la información ya cambió | BOYACÁ → brochure de 2019 para proyecto entregado |

**Acción:** Documentar cada discrepancia con:
- Proyecto afectado
- Fuente A (Doc 1) vs Fuente B (Drive)
- Pregunta concreta a validar con el cliente
- Severidad (alta = bloquea hardcodeo / media = ajusta hardcodeo / baja = nota informativa)

### Paso 4 — Lectura de "Conversaciones Reales" (si existe)

Si el cliente comparte capturas o exports de WhatsApp reales — esto es oro puro y NO existe en todos los clientes. Cuando existe, leer con estos lentes:

**Qué extraer:**
1. **Tono real del equipo** — cómo escriben Tiago, Evelyn, Sebastián (en el caso de EDFAN). Voseo o usted, abreviaturas, emojis, longitud de mensajes, uso de audios. El Doc 1 declara un tono; las conversaciones lo confirman o lo contradicen.
2. **FAQs no relevadas** — preguntas que aparecen en chats reales y no fueron capturadas en Doc 1 B4.
3. **Objeciones reales** — cómo se manifiestan en chat (no son las 5 típicas del Doc 1, son frases concretas).
4. **Frases de cierre que funcionan** — copia textual de cómo el equipo cierra conversaciones que avanzan.
5. **Momentos de derivación** — en qué punto el humano toma la conversación. Patrones: ¿siempre cuando aparece "presupuesto X"? ¿Cuando piden visita? ¿Cuando preguntan algo técnico?
6. **Timing real de respuesta** — cuánto tarda el equipo. Si tardan 4 horas y el cliente dice que quiere "respuesta inmediata", hay un gap entre lo que dice y lo que hace.
7. **Vocabulario de marca** — palabras que repiten ("financiación a medida", "estamos para acompañarte", etc.). Esas frases entran al prompt.
8. **Lo que el equipo NUNCA hace** — silencios reveladores: si en 50 chats nadie negocia precios por WhatsApp, ese límite es real.

**Output:** Sección "Insights de Conversaciones Reales" en el documento de Matching y Difusión, con quotes textuales numerados y categorizados.

**Si el cliente NO comparte conversaciones reales:** dejarlo explícito en el documento. La calidad del prompt baja sin esto, y conviene pedirlo aunque sea post-lanzamiento como input para optimización.

### Paso 5 — Lectura de "Listas de Precios + Financiación"

**Qué extraer:**
- ¿Hay precios por unidad o solo rangos por proyecto? Los exactos van a Tokko, los rangos al prompt.
- Esquema de anticipo + cuotas por proyecto (porcentajes, plazos, ajuste CAC/IPC/UVA).
- Excepciones: descuentos por contado, refuerzos, escalas según anticipo.
- Plazos de actualización: ¿la lista cambia diaria, semanal, mensual?

**Regla de hardcodeo:**
- **Hardcodea en prompt:** estructura general de financiación por proyecto (ej: "30% anticipo + 60 cuotas en pesos ajustadas por CAC").
- **NO hardcodea en prompt:** valor exacto del anticipo, valor exacto de la cuota, precio total.
- **Marca con flag "Tokko":** todo lo que vive en Tokko y aún no está integrado.

### Paso 6 — Lectura de "Material Inmobiliarias"

**Pregunta clave:** ¿el material es distinto del que se le envía a compradores finales?

- **Si es el mismo:** simplifica todo. Un solo set de placeholders. Flujo B2B = mismo flujo + tag `#contacto_inmobiliaria` para routing.
- **Si es distinto:** se necesitan placeholders separados (`/BrochureB2B-SLUG`) o derivación automática a humano para el envío de material B2B.

En EDFAN era el mismo material, así que se simplificó. En G&D Developers, por la presencia de una carpeta dedicada "Material Inmobiliarias", probablemente sea distinto — hay que validar antes de avanzar.

### Paso 7 — Lectura de "Videos de Avances"

Los videos son material vivo: cambian con el avance de obra, son lo que más comparte el equipo en redes, generan engagement alto.

**Tres opciones de tratamiento:**

1. **Placeholder dinámico por proyecto** (`/VideoAvance-SLUG`): el equipo actualiza manualmente el archivo en Prometheo cada vez que sale un nuevo video. Simple pero requiere disciplina.
2. **Placeholder estático "Drive público"**: link a la carpeta de videos en Drive. El lead navega. Menos comercial pero auto-actualiza.
3. **Derivación a humano**: cuando el lead pide videos de avance, el agente deriva. Más fricción, más control.

Recomendación default: **opción 1** para los proyectos prioritarios MVP, **opción 3** para el resto.

### Paso 8 — Diseño del sistema de placeholders

Esta es la parte más operativa. Reglas:

**Convención de SLUG:**
- Mayúsculas + guion bajo si tiene espacios. Ej: `VERVE_VC`, `BLACK_DEVOTO`, `JBJ_3794`.
- Único por proyecto, corto pero identificable.
- Si dos proyectos comparten nombre, agregar diferenciador de barrio o número (`JBJ_3794` vs `JBJ_CUCHA`).

**Placeholders mínimos por proyecto (todos los desarrollistas):**
- `/Brochure-SLUG` — carpeta de venta completa (PDF).
- `/Render-SLUG` — render maestro (imagen).

**Placeholders adicionales según material disponible:**
- `/Plano-SLUG` — solo si los planos están separados del brochure y son material de venta independiente.
- `/VideoAvance-SLUG` — solo para los proyectos prioritarios MVP, si el equipo los actualiza con disciplina.
- `/Ubicacion-SLUG` — link a Google Maps. Útil si el lead acepta visita.
- `/ListaPrecios-SLUG` — solo si el cliente tiene una lista pública por proyecto que está bien tenerla mano (raro, normalmente va a Tokko).

**Cálculo de placeholders totales:**
- Mínimo: 2 × N proyectos = 2N placeholders.
- Con video: 3N para los prioritarios + 2N para el resto.
- En EDFAN fueron 32 (2 × 16). En G&D, dependerá del catálogo y del nivel de organización.

**⚠️ NOTA INTERNA AUREA — VALIDAR ANTES DEL LANZAMIENTO:**
La sintaxis exacta del placeholder en Prometheo (guion medio vs bajo, mayúscula vs minúscula, prefijo `/` o `@` o `#`) se valida con el bot oficial de Prometheo antes de cargarlos. Si la sintaxis difiere de lo asumido, hacer search/replace global en el prompt y en el documento de Matching.

### Paso 9 — Decisión MVP simple vs Escalonada

Para difusión de material, dos arquitecturas posibles:

**A) MVP simple (recomendado por default):**
> El lead pide brochure → el agente lo manda. Sin escalonamiento.

Ventajas: simple, rápido de implementar, fácil de explicar al cliente, sin nuevas variables ni tags.
Desventajas: el agente puede saturar al lead con un brochure pesado en el primer turno; no hay control sobre el momento del envío.

**B) Escalonada M1 → M2 → M3 → M4 (post-MVP):**
> M1 = render + texto. M2 = brochure tras pedido explícito. M3 = datos detallados (Tokko + financiación). M4 = pre-visita (re-envío + ubicación + asesor).

Ventajas: control fino, evita saturación, puntos de medición claros.
Desventajas: agrega una variable nueva (`momento_difusion`) + 5 Smart Tags + lógica condicional en el prompt. Mayor complejidad inicial.

**Criterio de decisión:**
- Arrancar siempre con A.
- Pasar a B después de los primeros 60 días de operación si las métricas muestran:
  - Tasa de avance brochure → visita por debajo del 30%.
  - O leads que reciben brochure en turno 1 y desaparecen.
  - O quejas del equipo de que el agente "tira material a cualquiera".

En EDFAN se eligió A (MVP simple) y se documentó B como Anexo v2. Mismo criterio para G&D salvo que aparezca una razón explícita para cambiarlo.

### Paso 10 — Generación del documento "Matching y Difusión v1"

**Ver sección 5 abajo para la estructura exacta del documento.**

---

## 4. Cómo procesar conversaciones reales — guía detallada

> Esta sección es nueva respecto a la metodología de EDFAN porque EDFAN no compartió conversaciones reales. G&D Developers sí, así que hay que saber qué hacer con ellas.

### 4.1 — Qué buscar (lentes de lectura)

**Lente 1 — Tono real**
- ¿Vosean o tutean? ¿Tratan de usted?
- ¿Usan emojis? Cuáles, cuántos, en qué contextos.
- ¿Mensajes cortos o largos? ¿Una idea por mensaje o varias?
- ¿Audios o solo texto? Si hay audios, ¿qué los dispara?
- ¿Abreviaturas? ("xq", "tmb", "bsos")

**Lente 2 — FAQs no anticipadas**
Cualquier pregunta del lead que se repite en 3+ chats y no aparece en Doc 1 B4 → FAQ nueva. Documentar pregunta + respuesta tipo del equipo.

**Lente 3 — Objeciones reales**
No las 5 típicas del libro. Las frases reales: "está re lejos", "se va de presupuesto", "necesito hablarlo con mi señora", "vi otra cosa más barata acá". Capturar literal.

**Lente 4 — Triggers de derivación**
Patrones de cuándo el humano interviene:
- Por palabra clave (ej: "boleto", "escritura", "abogado").
- Por pregunta no anticipada (ej: técnica específica).
- Por intención (ej: pide visita).
- Por tiempo (ej: después de X turnos sin avance).

**Lente 5 — Frases que funcionan**
Cierres exitosos (los que terminan en visita agendada o reserva). Copiar literal — entran al prompt como referencia.

**Lente 6 — Velocidad real de respuesta**
- ¿Cuánto tardan promedio?
- ¿Hay diferencia entre uso propio e inversor?
- ¿Hay franja horaria con respuesta más rápida?
- Cruzar contra el resultado declarado en Doc 1 B0 (objetivo y baseline, ej. "100% respuesta inmediata"). Si hay gap, marcarlo.

**Lente 7 — Vocabulario de marca**
Palabras o frases que repiten cruzados varios chats, distintos asesores. Eso es voz de marca real, no la del manual.

### 4.2 — Cómo presentarlo en el documento

Sección dedicada en el documento de Matching y Difusión, llamada **"Insights de Conversaciones Reales"**, con esta estructura:

```
1. TONO REAL OBSERVADO
   - Hallazgo: [qué se ve]
   - Quotes (3-5 ejemplos, anonimizando al lead)
   - Implicación para el prompt: [qué cambia o confirma]

2. FAQs NUEVAS DETECTADAS
   - Pregunta: [literal]
   - Frecuencia observada: [N chats sobre M revisados]
   - Respuesta tipo del equipo: [resumen + 1 quote]
   - Acción: incorporar a sección 5 del prompt (FAQs)

3. OBJECIONES REALES
   - Objeción literal: [quote]
   - Smart Tag asociado: [#objecion_X — existente o nueva]
   - Manejo del equipo: [resumen + quote]
   
4. TRIGGERS DE DERIVACIÓN OBSERVADOS
   - Patrón: [descripción]
   - Quote ejemplo: [si aplica]
   - Implicación para el prompt: [regla de derivación a sumar]

5. FRASES DE CIERRE QUE FUNCIONAN
   - Lista numerada de quotes textuales (10-15 si hay material)
   - Etiquetar contexto: cierre con visita agendada / cierre con reserva / cierre con derivación a Sebastián

6. GAP DECLARADO vs OBSERVADO
   - Lo que dice el Doc 1: [cita]
   - Lo que muestra el Drive: [evidencia]
   - Decisión: [cuál tomar como verdad — recomendación]
```

### 4.3 — Reglas de privacidad

- Anonimizar a los leads en el documento. Reemplazar nombres por "Lead 01", "Lead 02", etc.
- No copiar números de teléfono ni datos personales.
- Si el lead aparece con nombre y apellido en el chat, reemplazar por inicial.

---

## 5. Estructura del documento output: "Matching y Difusión v1"

El documento es interno AUREA. NO se entrega al cliente. Su único destinatario es la skill `prometheo-etapa2-prompt`.

**Convención de colores** (consistente con resto de docs AUREA):
- **Negro** — información cerrada de Etapa 1 o auditoría.
- **Azul** — pendiente de completar.
- **Naranja** — nota interna AUREA.
- **Rojo** — discrepancia detectada (requiere validación cliente).
- **Gris** — propuesta v2 / post-MVP.
- **Cyan** — placeholder de adjunto en Prometheo.

**Estructura de secciones obligatorias:**

```
1. PROPÓSITO Y USO DEL DOCUMENTO
   - Para qué sirve, quién lo lee, cuándo se usa.
   - Convención de colores.

2. PRINCIPIOS COMERCIALES DEL AGENTE
   - Principio 1: vende, no busca (3 partes en cada respuesta).
   - Principio 2: oferta no es match exacto (ejemplos del cliente).
   - Principio 3: filtrado interno estricto, conversación flexible.
   - Principio 4: tono [del Doc 1 B6] estricto.

3. INVENTARIO DE PROYECTOS — MATRIZ MAESTRA
   - Una tabla por proyecto con: slug, dirección, barrio, estado, entrega, tipologías, precio referencial, estado del material, placeholders.
   - Marcar prioritarios MVP si aplica.

4. ESTADO DEL MATERIAL POR PROYECTO
   - 4.1 — Inventario por estado (completo / parcial / sin carpeta / pesado).
   - 4.2 — Brochures que requieren compresión.
   - 4.3 — Discrepancias detectadas (tabla con proyecto / fuente A / fuente B / acción).
   - 4.4 — Lista para presentación al cliente (texto diplomático listo para incluir).

5. INSIGHTS DE CONVERSACIONES REALES
   - Las 6 secciones detalladas en sección 4.2 de esta skill.
   - Solo si el cliente compartió chats reales.

6. LÓGICA DE DIFUSIÓN — VERSIÓN 1 (LANZAMIENTO)
   - Lo relevado en Etapa 1 (B9 + Doc 2).
   - Regla operativa MVP simple.
   - Reglas duras de difusión.
   - Información Tokko vs hardcoded.

7. GLOSARIO DE PLACEHOLDERS
   - Tabla con todos los placeholders a configurar en Prometheo.
   - Nota de validación de sintaxis con bot oficial.

8. BLOQUE DE PROMPT V1 — LISTO PARA INSERTAR
   - 8.1 Catálogo embebido (sección 4 del prompt-tipo).
   - 8.2 Flujo conversacional (sección 6).
   - 8.3 Asignación de material (sección 11).

9. ANEXO — PROPUESTAS AUREA V2 (POST-MVP)
   - Sub-perfiles de inversor (si aplica).
   - Lógica escalonada M1→M4.
   - Variables nuevas propuestas.
   - KPIs específicos del esquema escalonado.
   - **NOTA AUREA OBLIGATORIA**: aclarar que es propuesta del consultor, NO relevamiento del cliente. NO se implementa en lanzamiento. Se evalúa post-60 días.
```

---

## 6. Cómo se conecta con la skill `prometheo-etapa2-prompt`

Cuando se ejecute la skill de generación del prompt, va a tomar este documento como input principal. Específicamente:

- **Sección 2** (Principios comerciales) → encabezado del prompt.
- **Sección 3** (Matriz maestra) → sección 4 del prompt-tipo (Catálogo).
- **Sección 6** (Lógica de difusión) → sección 11 del prompt-tipo (Asignación de Material).
- **Sección 7** (Glosario placeholders) → configuración paralela en Prometheo.
- **Sección 8** (Bloque de prompt v1) → insertar literalmente.
- **Insights de Sección 5** → enriquecen secciones 2 (tono), 5 (FAQs) y 6 (objeciones) del prompt-tipo.

---

## 7. Caso de referencia: EDFAN Real Estate

**EDFAN sirvió como prototipo de esta metodología.** Resultados que se obtuvieron:

- 16 proyectos auditados.
- 9 con material completo / 4 con carpeta sin brochure / 3 sin carpeta.
- 3 brochures pesados a comprimir (BLACK Devoto 141 MB, EDEN 66 MB, MAKER 43 MB).
- 6 discrepancias detectadas entre Doc 1 y Drive (CHALETS / SPAZIOS, CENTRAL / co-desarrollo, BOYACÁ / amenities, etc.).
- 32 placeholders diseñados (2 × 16 proyectos).
- Decisión MVP simple v1 + lógica escalonada M1→M4 documentada en anexo v2.

**Diferencia con G&D Developers:** G&D viene con material adicional que EDFAN no tuvo:
- Carpeta de Conversaciones Reales (no existía en EDFAN).
- Carpeta separada de Material Inmobiliarias (en EDFAN era el mismo material).
- Carpeta dedicada de Videos de Avances (en EDFAN no estaba sistematizada).

Eso significa que el documento de Matching y Difusión para G&D va a ser más rico en las secciones 5 (Insights de conversaciones), 6 (lógica de difusión, con tratamiento explícito de B2B) y 4 (estado del material, con placeholders de video).

---

## 8. Checklist de salida — antes de cerrar el documento

Antes de declarar el documento "Matching y Difusión v1" terminado y pasarlo a la skill de generación del prompt, verificar:

- [ ] Todos los proyectos del Doc 1 B2 tienen entrada en la matriz maestra.
- [ ] Cada proyecto tiene estado de material declarado (completo / parcial / sin carpeta / pesado).
- [ ] Cada discrepancia tiene pregunta concreta para el cliente.
- [ ] Si hay conversaciones reales, hay sección de insights con quotes anonimizados.
- [ ] El sistema de placeholders está completo (mínimo `/Brochure-SLUG` + `/Render-SLUG` por proyecto).
- [ ] La nota de validación de sintaxis con bot oficial Prometheo está presente.
- [ ] La decisión MVP simple vs escalonada está tomada y documentada.
- [ ] El bloque de prompt v1 (sección 8) está escrito en imperativo, en segunda persona, listo para pegar.
- [ ] El anexo v2 está claramente separado y marcado como "no se implementa ahora".
- [ ] Convención de colores aplicada consistentemente.

Si falta cualquiera de estos puntos, el documento no está listo y la skill de generación del prompt va a producir un output inferior.

---

## 9. Regla AUREA: validación con bot oficial Prometheo

Cualquier decisión de configuración que dependa del comportamiento exacto de Prometheo (sintaxis de placeholders, lógica AND entre Smart Tags, comportamiento de la actualización de variables, formato de variables tipo precio, etc.) se marca en el documento como NOTA INTERNA AUREA naranja. Valentín la valida con el bot oficial de Prometheo (vía WhatsApp) ANTES del lanzamiento.

No diseñar artefactos polémicos sin validar.

---

*Skill creada por AUREA Hub. Caso de referencia: EDFAN Real Estate. Aplicación: G&D Developers + futuros desarrollistas inmobiliarios.*
