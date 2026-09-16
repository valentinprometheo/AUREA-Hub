---
consultar-cuando: cliente desarrollista inmobiliario, diseño o iteración de su prompt/CRM
disparadores: "desarrollista", "real estate", "proyectos en pozo", "G&D", "EDFAN", "Tokko", "inmobiliaria que vende sus propios desarrollos"
fuente-única-de: lógica comercial del rubro desarrollista
combina-con: principios-transversales-agente, integracion (Sheets o Tokko), 00-sistema-fija-flexible
---

# 01 — Rubro Real Estate (Desarrollistas Inmobiliarios)

**Patrones consolidados del rubro para clientes desarrollistas inmobiliarios.**

---

## Definición del rubro

**Aplica a:** clientes que venden proyectos inmobiliarios propios (en pozo, en construcción, o terminados) directo al consumidor final, con o sin canal de inmobiliarias intermediarias.

**NO aplica a:** inmobiliarias tradicionales con cartera de propiedades de terceros (ver `04-inmobiliaria-tradicional.md` cuando exista).

**Clientes documentados:** G&D Developers (prototipo), EDFAN Real Estate (descartado por desactualización al modelo v7).

---

## Particularidades del rubro

### 1. La unidad central del CRM es el **proyecto**

A diferencia de otros rubros, en desarrollistas todo gira alrededor del proyecto inmobiliario. No es la propiedad individual ni la zona — es el desarrollo completo con su nombre propio, ubicación, etapa de obra, tipologías disponibles.

Esto define la variable `proyecto_interes` como una de las variables más cargadas del sistema.

### 2. Catálogo en Tokko (estándar de facto del rubro)

El 80%+ de los desarrollistas usan Tokko como CRM/catálogo. Esto define la modalidad de catálogo como **B (integración externa)** casi por default.

**Implicancia:**
- NO hardcodear info de unidades, precios o disponibilidad en el prompt
- El prompt conoce los proyectos (estructura macro) pero no las unidades específicas
- Tokko se consulta en runtime

### 3. Canal B2B con inmobiliarias

Los desarrollistas trabajan con inmobiliarias intermediarias que les llevan clientes. Esto es estructural:

- 30-60% del volumen viene por inmobiliarias
- Las inmobiliarias tienen comisión por venta
- El agente IA tiene que identificar a una inmobiliaria desde el primer mensaje y darle tratamiento diferenciado

### 4. Temas fiscales sensibles

El rubro está atravesado por temas legales que el agente NUNCA debe asesorar:

- Blanqueo de capitales (Ley 27.743 Argentina)
- Crédito hipotecario (varía por país, banco, política)
- Permutas con tasaciones
- Compra-venta entre familiares con razones fiscales

**Patrón:** identificar el tema → derivar inmediatamente con `tipo_derivacion` correspondiente.

### 5. Ciclo de venta largo (3-12 meses)

A diferencia de venta de productos, el ciclo desde primer contacto hasta cierre puede durar meses. Implica:

- Seguimientos espaciados (no agresivos)
- Variable `objetivo_busqueda` para distinguir inversor (decisión más rápida) vs usuario final (decisión más larga)
- Reactivación de leads a los 60-90 días

### 6. Variable router obligatoria

Por la cantidad de procesos paralelos (venta + B2B + FAQ + excepciones), `proceso_actual` es variable router obligatoria.

---

## Patrones macro confirmados

### Variables transversales típicas

Las variables que aparecen en TODOS los desarrollistas (validar en cada cliente, pero esperar que aparezcan):

| Variable | Tipo | Notas |
|---|---|---|
| `canal_origen` | Opciones | WhatsApp, Instagram, Mail, Zonaprop, Web, Referido |
| `tipo_contacto` | Opciones | comprador_final, inmobiliaria, profesional |
| `proyecto_interes` | Opciones | Set cerrado: catálogo del cliente |
| `zona_interes` | Opciones | Barrios donde el cliente tiene proyectos |
| `tipo_unidad` | Opciones | 1_amb, 2_amb, 3_amb, 4_amb, cochera, local |
| `presupuesto` | Precio | Monto USD |
| `finalidad` | Opciones | vivienda, inversion_renta, reventa, diversificacion |
| `objetivo_busqueda` | Opciones | inversion vs uso_personal — gobierna preguntas posteriores |
| `forma_de_pago` | Opciones | contado, financiado, pozo_cuotas, permuta |
| `tipo_derivacion` | Opciones | inmobiliaria, negociacion, tema_fiscal_blanqueo, credito, vip, postventa |
| `estado_venta` | Opciones | calificando, info_enviada, visita_agendada, visita_realizada, reservado, cerrado |

### Smart Tags

Modelo v7: 2 tags base.

- `#seguimiento_activo`
- `#derivar_a_humano`

Excepción: NO crear `#derivar_a_inmobiliaria`, `#derivar_a_blanqueo`, etc. Esos casos se distinguen con `tipo_derivacion`.

### Embudos típicos

4 embudos:

1. **Venta** (principal, 70-80% volumen)
   - Etapas: calificando → info_enviada → visita_agendada → visita_realizada → reservado → cerrado_ganado/perdido
2. **Derivación B2B (inmobiliarias)**
   - Etapas: inmobiliaria_detectada → variables_capturadas → asignado_a_humano → cerrado
3. **FAQ**
   - Etapas: pregunta_recibida → respuesta_enviada → vuelve_a_venta / cierra
4. **Excepciones**
   - Etapas: patron_detectado → derivado_a_humano

### Seguimientos típicos

- Follow-up 1: 24hs después de info enviada
- Follow-up 2: 72hs si no respondió al 1
- Follow-up 3: 7 días (reactivación leve)
- Follow-up 4: 30 días (reactivación profunda con tono distinto)
- Follow-up de visita: 1 día antes a las 17hs (recordatorio)
- Follow-up post-visita: 24hs después de la visita

---

## Reglas operativas específicas

### Regla 1 — Inmobiliarias se derivan automáticamente en MVP

Aunque conceptualmente sería interesante un flujo conversacional con inmobiliarias, en MVP se deriva siempre. Razones:

- Las inmobiliarias prefieren hablar con humano directo (relación comercial)
- Volumen B2B es importante (no se puede automatizar mal)
- El agente captura las variables clave y deriva con contexto

Fase 2 puede incluir flujo conversacional para B2B si el cliente lo necesita.

### Regla 2 — Reglas inquebrantables del B2B con inmobiliarias

1. **No pedir el número del cliente final de la inmobiliaria.** La inmobiliaria gestiona su contacto, no el desarrollista.
2. **No confirmar comisiones por chat.** Eso lo cierra el equipo comercial cuando hay operación concreta.
3. **No mandar material proactivo a la inmobiliaria** (catálogos, listas de precios). La inmobiliaria pide lo que necesita.
4. **Coordinar siempre por el número de la inmobiliaria, no del cliente final.** El cliente final habla con su inmobiliaria.
5. **La inmobiliaria mantiene el contacto con el cliente.** El agente del desarrollista solo coordina con la inmobiliaria.

### Regla 3 — Tema fiscal blanqueo siempre se deriva

Argentina tiene la Ley 27.743 de regularización. El agente NUNCA asesora sobre cómo regularizar, qué documentación se necesita, ni implicancias.

Patrón:
```
Lead menciona "blanqueo", "regularización", "Ley 27.743", "exteriorización"
→ identificar tipo_derivacion = tema_fiscal_blanqueo
→ disparar #derivar_a_humano
→ mensaje del agente: "Para el tema fiscal te pasa nuestro equipo legal,
   que es el indicado para asesorarte. Ya te ponen en contacto."
```

### Regla 4 — Crédito hipotecario suele derivar

Aunque no es prohibido por ley, suele NO ser el perfil del cliente ideal del desarrollista (compra más rápida = contado o cuotas del pozo). Si el lead solo puede comprar con crédito hipotecario, conviene derivar para que el equipo decida si avanzar o no.

### Regla 5 — Variable `objetivo_busqueda` gobierna preguntas

Si el agente identifica que `objetivo_busqueda = inversion`:
- Puede preguntar valor por m²
- Puede preguntar renta esperada
- Puede mostrar análisis de rentabilidad si tiene el dato

Si `objetivo_busqueda = uso_personal`:
- NO preguntar valor por m² (es jerga de inversor)
- Preguntar presupuesto total directo
- Foco en características del proyecto (amenities, ubicación, terminaciones)

### Regla 6 — Co-comercialización con otros desarrollistas

Algunos proyectos son co-comercializados entre 2 desarrollistas (G&D + Cesarprop en 9 de Julio Estudios 3, por ejemplo). El agente del desarrollista A:

- Vende también unidades de proyectos co-comercializados con B
- Coordina visitas a ambos
- Comisión / cierre lo arregla el equipo, no el agente

Documentar esta situación en el prompt si aplica.

### Regla 7 — Reactivación a 60-90 días

El ciclo largo justifica reactivar leads fríos con tono distinto al follow-up normal:

```
"Hola [nombre], hace un par de meses estuviste consultando por
[proyecto]. Tenemos novedades [novedad concreta: nueva etapa, descuento,
unidades disponibles]. ¿Te interesa retomar?"
```

---

## KPIs típicos del rubro

| KPI | Cómo se mide | Target inicial |
|---|---|---|
| % de leads calificados | Leads con variables transversales completas / Total leads | 80%+ |
| Tiempo a primera respuesta | Mediana | < 5 minutos |
| % visitas agendadas | Visitas / leads calificados | 25-40% |
| % visitas realizadas | Visitas realizadas / visitas agendadas | 60-75% |
| Tasa de cierre | Reservas / visitas realizadas | 15-30% según proyecto |
| % derivaciones correctas | Derivaciones donde el equipo confirmó que estaban bien clasificadas / Total derivaciones | 85%+ |

---

## Glosario rubro-específico

| Término | Definición |
|---|---|
| Pozo | Etapa pre-construcción, se vende sobre plano |
| Construcción | Obra en proceso |
| Posesión | Momento en que el propietario puede usar la unidad |
| Escritura | Acto formal de transferencia de propiedad |
| Anticipo | Monto inicial al firmar el boleto de compra |
| Cuotas del pozo | Pagos mensuales durante construcción |
| Reserva | Compromiso firme de compra previo al boleto |
| Boleto de compraventa | Contrato firme entre comprador y vendedor |
| Blanqueo | Regularización de capitales no declarados |
| Permuta | Intercambio de bien por bien (típicamente terreno por unidades) |
| Tasación | Valoración profesional de una propiedad |
| Co-comercialización | Dos desarrollistas comparten la venta de un proyecto |

---

## Errores frecuentes a evitar

| Error | Consecuencia | Solución |
|---|---|---|
| Hardcodear precios en el prompt | Cada cambio requiere editar prompt | Modalidad B con Tokko |
| Tratar a inmobiliaria como B2C | Saturación del embudo + mala experiencia para la inmobiliaria | Derivación automática con tipo_derivacion = inmobiliaria |
| Asesorar sobre blanqueo | Riesgo legal + mala info al lead | Derivación inmediata |
| Asumir que todos los leads son inversores | Preguntas inadecuadas para uso personal | Variable objetivo_busqueda + preguntas condicionales |
| No tener follow-up de reactivación | Leads fríos se pierden definitivamente | Follow-up a 60-90 días con tono distinto |
| Mensajes muy largos | Saturan al lead | Mensajes cortos + objetivo "visita al showroom" |
| Ignorar amenities en el prompt | Cliente pregunta y agente no sabe responder | Amenities macro hardcodeadas; detalles en brochures |

---

## Patrones que están en evaluación

Estas son hipótesis que aparecen en algún cliente pero no están confirmadas como patrón del rubro:

| Patrón | Cliente donde apareció | Estado |
|---|---|---|
| Programa "Invertí en m²" para inversores | G&D Developers (BLACK Devoto) | Específico del cliente, no patrón del rubro |
| Variable `estado_proyecto` (fase de obra) | Si el cliente tiene proyectos en múltiples fases | Flexible, no obligatorio |
| Variable `tipo_operacion` (primaria vs reventa) | EDFAN RE | Solo si el cliente trabaja con reventa |
| Renta hasta posesión | G&D (Feel Palermo) | Específico del cliente |
| Captura de DNI temprano | (ninguno aún) | En evaluación para B2B |

---

## Próximos clientes a sumar

Cuando aparezca un nuevo cliente desarrollista, documentar en este archivo:

- Patrones nuevos que aporta
- Variables idiosincráticas que NO se generalizan
- Decisiones operativas distintas a G&D

---

## Integración con catálogo digital (Tokko)

En real estate (desarrollistas inmobiliarios) la integración estándar es **Tokko CRM**. Tokko es la plataforma que aloja el catálogo de unidades/proyectos del desarrollista y devuelve info dinámica (disponibilidad, precio, plano, ubicación).

Las 6 reglas de integración con catálogo del Reglas Diseño de Prometheo by AUREA (Reglas 16-21) **aplican siempre** en este rubro. Ver `../02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` para el detalle completo.

**Cómo aplicar en real estate (desarrollista):**

| Regla | Aplicación específica al rubro |
|---|---|
| 16 — No bloquear consultas atómicas | El lead pregunta "¿tienen unidades en Caballito de 2 ambientes?" antes de identificarse. El agente responde con info de Tokko sin pedir calificación previa. |
| 17 — Búsqueda separada de consulta | Tools `[BUSCAR_PROYECTO]`, `[CONSULTA_UNIDADES]`, `[OBTENER_LINK_FICHA]`. Búsqueda por: zona, ambientes, precio, proyecto puntual. |
| 18 — Match tolerante | El lead nombra "Drago Select", "Drago", "el proyecto de Drago", "el de Drago 261" — todos resuelven al mismo proyecto. Cuando hay ambigüedad (ej: "el proyecto de Belgrano" si hay varios), el agente repregunta. |
| 19 — URLs Tokko son válidas | Las URLs devueltas por Tokko (link a ficha de la unidad, link al brochure del proyecto) son canónicas. Las URLs externas (videos institucionales, renderizados extra, planos PDF que no están en Tokko) NO van hardcoded — viven en una fuente externa de acceso compartido (Drive, YouTube, Vimeo, Notion, Dropbox, Sheets, etc.) que el cliente elige. **Paso obligatorio en Etapa 2:** preguntar al cliente "¿qué tenés en Tokko vs qué tenés en Drive?", "¿hay material externo (videos, renders) que el agente vaya a usar?" y "¿en qué fuente lo querés tener?" |
| 20 — Naming unificado | Cada proyecto tiene `clave_interna` (ej: `DRAGO_SELECT`). Cada unidad tiene su sub-clave (`DRAGO_SELECT_3A`). Tabla de 3 columnas: clave_interna + variantes técnicas del CRM (código Tokko, nombre comercial) + variantes del lead (jerga: "Drago", "el de Drago", "Drago 261"). |
| 21 — Prioridad de respuesta | Lógica de calificación inversor vs vivienda, FAQs del rubro, política de financiación: hardcoded. Disponibilidad de unidades, precios, link a ficha: integración Tokko. Cotización personalizada, reserva, visita: derivar. |

**Particularidad del rubro:** en real estate la **disponibilidad** es crítica. Tokko devuelve estados: `disponible`, `reservado`, `vendido`. El agente debe mostrar disponibilidad ANTES que precio (no tiene sentido decir el precio de algo que ya se vendió).

**Stock cambia rápido:** las unidades se reservan y venden en horas. Por eso la integración tiene que ser en tiempo real, no cacheada. Si el agente le dice al lead "disponible" y 2 minutos después se vendió, es un problema operativo.

**Productos típicos del rubro que SÍ se consultan en Tokko:**
- Unidades por proyecto (departamento, semipiso, cochera, baulera)
- Disponibilidad en tiempo real
- Precios por unidad
- Link a ficha completa
- Brochures y planos vinculados al proyecto

**Productos que NO se consultan (derivar a humano):**
- Cotizaciones personalizadas con financiación
- Reservas (requiere validación legal del comercial)
- Visitas a obra
- Negociación de descuentos por volumen (inversores)
- Unidades fuera del MVP (proyectos no cargados en Tokko)

**Caso de referencia:** G&D Developers (en proceso de finalización). EDFAN Real Estate y TKVA están en discovery.

---

## Smart Tags — doctrina del rubro (validada en G&D)

Apartado canónico del modelo de Smart Tags para desarrollistas inmobiliarios. Doctrina
nutrida desde la implementación de G&D Developers y validada en producción. Aplica el
modelo general de `embudos-y-tags.md` ("una tag por dimensión") al rubro, con sus
embudos típicos, sus tipos de usuario, sus colores y sus acciones.

### Las dimensiones aplicadas al rubro

| Dimensión | Valores en desarrollista | Cómo se asigna |
|---|---|---|
| **Estadío** | Etapas del embudo donde está el lead | Automático según embudo |
| **Tipo de usuario** | Inversor *o* Cliente final *o* Inmobiliaria *(una sola)* | Derivado de `var_objetivo_busqueda` o equivalente |
| **Prioridad** *(opcional)* | Contacto VIP *(se asigna o no)* | Manual o por regla del cliente |

Combinaciones válidas en el panel:
- `En Conversación + Inversor` (lead estándar)
- `En Conversación + Inversor + Contacto VIP` (lead estándar prioritario)
- `Visita Agendada + Cliente final`

Combinaciones inválidas (rompen el modelo):
- `Inversor + Cliente final` — ambas son de la dimensión "tipo de usuario", una sola.
- `Inversor + Inmobiliaria` — ídem.
- `Nuevo Lead + Calificado` — ambas son estadío del mismo embudo, una sola.

### Los tres embudos típicos

Un desarrollista inmobiliario tiene tres recorridos con dueños y lógicas distintas.
Meterlos en un solo embudo hace el pipeline ilegible.

| Embudo | Dueño | Qué cubre |
|---|---|---|
| Recepción y Calificación | Principalmente el agente IA | Desde que el lead escribe hasta que sale calificado o se descarta |
| Venta y Cierre | Equipo humano | La gestión comercial real, después de calificar |
| Inmobiliaria | Equipo (track B2B) | La relación con inmobiliarias intermediarias (no venta directa) |

El lead "sale" de un embudo y "entra" a otro: cruza, no acumula etapas de los dos.

### Inventario de tags — modelo G&D

#### Embudo "Recepción y Calificación" (6 etapas)

| Tag | Color | Significado | Acción recomendada |
|---|---|---|---|
| Nuevo Lead | Azul | Escribió por primera vez, sin calificar | Ninguna · asistente activo |
| No Fit | Rojo | No califica (fuera de rubro, presupuesto, alquiler, etc.) | Cierra seguimientos |
| En Conversación | Violeta | El agente está calificando activamente | Ninguna · asistente activo |
| En Seguimiento | Amarillo | Dejó de responder, en reactivación | Dispara seguimientos programados |
| Calificado | Verde | Reúne criterios, listo para el equipo | **Notificación** al equipo |
| Derivado | Naranja | Pasa a un humano | **Notificación + apagar asistente** |

#### Embudo "Venta y Cierre" (6 etapas)

| Tag | Color | Significado | Acción recomendada |
|---|---|---|---|
| Por Coordinar | Azul | Tomado por el equipo, hay que coordinar visita | **Notificación** al responsable |
| Visita Agendada | Violeta | Visita confirmada | Recordatorio programado |
| Visita Realizada | Naranja | Ya visitó | Seguimiento post-visita |
| En Negociación | Naranja | Negociando condiciones | Gestión humana · asistente apagado |
| Convertida | Verde | Cerró la operación | **Apagar asistente** · cierre |
| No Concretado | Rojo | No avanzó tras la visita/negociación | Cierra seguimientos |

#### Embudo "Inmobiliaria" (4 etapas, condicional)

Solo aplica si el cliente trabaja con inmobiliarias como canal B2B.

| Tag | Color | Significado | Acción recomendada |
|---|---|---|---|
| Inmobiliaria a Contactar | Azul | Inmobiliaria detectada, hay que contactarla | **Notificación** |
| Inmobiliaria Gestión | Violeta | En conversación con la inmobiliaria | Gestión humana |
| Inmobiliaria Activa | Verde | Relación activa, deriva clientes | Sin acción |
| Inmobiliaria Inactiva | Amarillo | Relación en pausa | Sin acción |

#### Tags de la dimensión "tipo de usuario" (3 — mutuamente excluyentes)

| Tag | Significado |
|---|---|
| Inversor | Compra para invertir/renta |
| Cliente final | Compra para uso propio (vivir o usar) |
| Inmobiliaria | El contacto es una inmobiliaria intermediaria — además rutea al embudo Inmobiliaria |

#### Tag de la dimensión "prioridad" (opcional, una sola)

| Tag | Significado | Acción |
|---|---|---|
| Contacto VIP | Referido o cliente prioritario | **Notificación prioritaria** |

### Lógica de color — transversal

El color codifica el tipo de momento, no es estético. Aplica igual a cualquier
desarrollista que use este modelo:

| Color | Significa | Ejemplos |
|---|---|---|
| Azul | Entrada / inicio | Nuevo Lead, Por Coordinar, Inmobiliaria a Contactar |
| Violeta | En proceso temprano | En Conversación, Visita Agendada, Inmobiliaria Gestión |
| Amarillo | Espera / pausa | En Seguimiento, Inmobiliaria Inactiva |
| Naranja | Proceso activo avanzado / handoff | Derivado, Visita Realizada, En Negociación |
| Verde | Éxito | Calificado, Convertida, Inmobiliaria Activa |
| Rojo | Cierre negativo / descarte | No Fit, No Concretado |

### Principio de asignación de acciones

- **Notificar** donde alguien tiene que actuar ya (Calificado, Derivado, Por Coordinar,
  Inmobiliaria a Contactar, Contacto VIP).
- **Apagar asistente** donde el humano toma la posta (Derivado, En Negociación, Convertida).
- **Reactivar asistente** cuando el lead vuelve al bot tras un handoff.
- Las etapas de puro tránsito (Nuevo Lead, En Conversación) no llevan acción.

Las notificaciones requieren plan **Pro o Enterprise** (ver `restricciones-plataforma-prometheo.md`, restricción 9).

### Qué es fijo y qué es flexible al replicar en otro desarrollista

**Fijo** — se replica en cualquier desarrollista, es la estructura del modelo:

- Las dimensiones del modelo: estadío + tipo de usuario + prioridad opcional.
- Los tres embudos y su lógica (Recepción y Calificación / Venta y Cierre / Inmobiliaria).
- El código de color por tipo de momento.
- El principio de asignación de acciones.

**Flexible** — se ajusta por cliente:

- Los nombres exactos de las etapas (un cliente puede llamar "Visita Agendada" distinto).
- La cantidad de etapas de cada embudo según su proceso.
- Si existe o no el embudo Inmobiliaria (depende del canal B2B del cliente).
- Qué acción concreta lleva cada etapa.

### Checklist del implementador

1. Mapear los recorridos del cliente a embudos (¿cuántos procesos paralelos tiene?).
2. Definir las etapas de cada embudo como Smart Tags, en orden.
3. Definir las tags de tipo de usuario (mutuamente excluyentes entre sí).
4. Definir si la dimensión "prioridad" aplica (VIP o equivalente).
5. Asignar color por tipo de momento, no por gusto.
6. Asignar acciones: notificar donde hay que actuar, apagar en el handoff.
7. Cargar en orden: Variables → Tags → Embudos → Contactos (ver `importacion-contactos.md`).
8. Validar con conversaciones reales (el módulo Testing no dispara tags).
9. Confirmar el plan: si necesita notificaciones, tiene que ser Pro o Enterprise.

---


---

## Para profundizar

| Tema | Archivo |
|---|---|
| Caso de referencia G&D | `../08-casos-referencia/PROTOTIPO-g-d-developers.md` |
| Skill vertical real-estate | `../../02-skills/00-TRANSVERSAL/prometheo-vertical-real-estate/SKILL.md` |
| Reglas Diseño de Prometheo by AUREA | `../02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` |
| Reglas de integración con catálogo (Tokko, Drive, externos) | `../02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` |
| Operativa Etapa 2 | `../02-ETAPA2-Diseno/01-operativa-y-decisiones.md` |
| Modelo de embudos, tags y variables (base general del modelo) | `../02-ETAPA2-Diseno/embudos-y-tags.md` |

---

## Lógicas comerciales del rubro (destiladas de feedback en producción)

> Estas lógicas salieron de procesar el feedback de corrección de G&D (Veronica) y EDFAN
> (Martina) sobre agentes en producción. Son específicas del desarrollista. Las que además
> se vieron en mobiliario subieron a `principios-transversales-agente.md` y no se repiten
> acá. Cada una indica cómo se tradujo a regla de prompt, para que sea reutilizable.

### Precisión de stock e inventario (el agente afirma de más cuando no tiene el dato)

El error de fondo más repetido del rubro: el agente inventa o afirma de más cuando no tiene
el dato vivo. Sub-reglas:

- **Sin stock = alternativa, nunca negación seca.** Si en la zona o proyecto que pide el
  lead no hay unidades, nunca "no tenemos" a secas: se ofrece la alternativa más cercana o
  se deriva por reventas. (G&D: ofrecía Distrito Colegiales como disponible cuando ya no
  tenía unidades; debía ofrecer Aguilar Point.)
- **No pluralizar stock ni afirmar superlativos sin respaldo.** Si una tipología tiene una
  sola unidad, se presenta como única ("el único 2 ambientes"), nunca en plural ni con
  "desde" (que sugiere varias). No afirmar "el más económico" si no surge confirmado de la
  fuente.
- **No inventar atributos ni restricciones por inferencia.** Los atributos de una unidad
  (parrilla, patio, orientación, piso) salen de la fuente; si no está, se deriva. No deducir
  restricciones no cargadas (G&D: afirmaba que la parrilla estaba solo en planta baja,
  erróneo).
- **m² totales vs cubiertos: el cliente define el default.** En G&D el default es m²
  totales; en EDFAN, cubiertos. Es una convención por cliente: se confirma en discovery y se
  fija en el prompt. Lo importante es no mezclar ni asumir.
- **Reventas siempre de contado.** Las reventas (unidades de entrega inmediata que se
  revenden) se ofrecen solo con pago total de contado, nunca con financiación. Si se presenta
  una reventa, no se menciona ningún esquema de financiación.
- **Escritura / estado legal no se afirma de memoria.** El estado de escritura no se afirma
  ni reconfirma sin respaldo de la fuente. Si el lead pregunta, se deriva. (G&D: afirmaba que
  Moca 2 tenía escritura, erróneo.)
- **Proceso B2B con inmobiliarias no se improvisa.** El agente no inventa cómo se trabaja con
  una inmobiliaria (quién contacta a quién, pasos de reserva). Deriva con la frase canónica.
  (G&D: improvisó todo un flujo que en la práctica no sucede.)

### Lógica de parámetros fijos vs flexibles (columna vertebral de la venta a inversores)

Ante criterios de búsqueda (zona + presupuesto + tipología), el agente identifica cuál es el
parámetro FIJO (lo que el lead no negocia) y cuál el FLEXIBLE (lo que puede mover), leyendo
el registro del lead. Jerarquía típica de rigidez: tipología (la más rígida) → zona
(media) → estado de obra (media) → presupuesto (el más rígido). Tres reglas de oro:

1. **Zona fija + no quiere mono:** se ofrece financiación para cubrir la diferencia de
   tipología.
2. **Presupuesto fijo + tipología fija:** se flexibiliza la zona, con la persuasión de zona
   sur — misma rentabilidad que zona premium con ~40% menos de inversión inicial. Persuadir
   con permiso, nunca empujando.
3. **Zona y presupuesto ambos fijos:** se deriva al comercial especializado.

Regla satélite — **prejuicio de zona sur como segunda opción:** si el lead venía pidiendo
zona premium y se le ofrece zona sur, se reconoce brevemente el prejuicio (seguridad, zona
en desarrollo) y se reorienta al diferencial real (rentabilidad + valorización), nunca se lo
ignora.

### Financiación: orientativa, en dos pasos, beneficio primero

Cuando el lead pregunta cómo se paga, la primera respuesta engancha con el beneficio (cuota
fija en dólares, sabe desde el día uno cuánto paga; tramo sin recargo) y cierra con una
pregunta que avanza. El detalle fino (anticipo y cuotas según entrega, tasa, refuerzos) se
reserva para cuando el lead lo pide. Si pide un ejemplo numérico, se va en dos pasos: paso 1
acuse breve + pregunta de enganche; paso 2 (solo si el lead acepta) el orientativo corto,
dejando clarísimo que el número fino lo cierra el comercial. Nunca se larga el esquema
completo de una.

### No asustar con precios

Nunca se hacen comparaciones que espanten ("muy por arriba de ese valor", "son bastante más
caros"). Si el lead pregunta por una tipología, se da el rango de esa tipología directo,
sin compararlo con una más barata.

### Comparar siempre con pro y contra para ambos

Si se comparan proyectos por rentabilidad, zona o lo que sea, nunca se dice que uno es
"menos" que otro sin decir también su pro. Cada proyecto de la comparación lleva su pro y su
contra de forma pareja; nunca queda uno solo con lo negativo.

### Inversor sin experiencia: tres pasos progresivos

Si el lead es inversor pero da señales de no tener experiencia (pregunta qué es el boleto,
cómo se compra en pozo), se va en tres pasos para no abrumar: (1) trayectoria + estructura
básica (SA/SRL, no fideicomiso, boleto de compraventa); (2) si quiere profundizar, informe
de dominio y estructura societaria; (3) si aún quiere más, derivación al comercial
especializado. No se vuelca todo de una.

### Cercanía como eje de la oración

Si el lead trae una referencia de cercanía (un subte, una avenida, "cerca de X"), la oración
ARRANCA ubicando el proyecto respecto de esa referencia; la cercanía es el eje, no un detalle
al final. Si pide la distancia exacta (cuántas cuadras), no se inventa el número: se deriva.

### Material y derivación

- **Generosidad con el material disponible:** si el material está cargado (renders,
  brochure, planos, video de avance), se manda directo, no se difiere al equipo. Lo que vive
  solo en la fuente o el equipo es el dato vivo (precio, stock, m² exacto).
- **Fidelidad léxica de material:** plano ≠ render ≠ brochure. Si el lead pide planos, no se
  sustituye por renders sin avisar. Cada cosa por su nombre.
- **Derivar sin auto-agendar (según cliente):** en G&D el agente no agenda solo (captura la
  preferencia y el equipo coordina); en EDFAN sí agenda en parámetros acotados. Es una
  decisión por cliente que se fija en discovery.
- **Videos de avance de obra:** se hardcodea/consulta el link por proyecto y se ofrece solo
  si existe para ese proyecto (no se ofrece para entrega inmediata, que no tiene video).

---

## Lógica comercial del rubro desarrollista (nivel 2 — probada en EDFAN y G&D)

> Estas lógicas están confirmadas en los DOS desarrollistas (EDFAN/Martina y G&D/Feli), pero no
> en un rubro distinto, así que son doctrina de rubro, no transversal (ver la regla de promoción
> en `logica-comercial-transversal.md`). A un desarrollista nuevo se le aplican directo; a un
> rubro distinto, no se asumen: se testean. Forma = doctrina; valores concretos = instancia del
> cliente.

- **Responder el eje que trajo el lead antes de calificar.** El lead marca el eje (precio, zona,
  tipología, entrega); se responde ese eje primero y recién después se pregunta para afinar. No
  devolver una pregunta que uno podría resolver.
- **Nombrar con autoridad apenas hay datos suficientes.** Apenas se puede recomendar, se nombran
  las opciones con un micro-argumento; hablar en abstracto cuando ya se puede ser concreto resta
  autoridad. Y se nombra el producto antes de dar su dato.
- **Recorte por perfil / consenso antes de un volcado grande.** Ante un pedido amplio, no volcar
  todo: recortar por perfil y, si pide "mandame todo", pedir consenso ("¿todo junto o por
  partes?").
- **Inferir en vez de preguntar cuando hay señal fuerte;** y no re-calificar lo que el lead ya
  cerró ("abierto a opciones" no se fuerza a definir).
- **Objeción de precio: reencuadrar por valor o referencia externa de mercado, nunca descuento.**
  La negociación se deriva. (G&D: Reporte Inmobiliario; EDFAN: alternativas en presupuesto.)
- **Objeción de confianza por trayectoria + estructura.** Ante desconfianza, trayectoria
  verificable y estructura jurídica/operativa, sin afirmar estados legales no verificados. La forma
  es candidata a transversal (falta confirmarla en un rubro no desarrollista); la estructura
  jurídica (S.A., fideicomiso, boleto) es instancia.
- **Preguntar la modalidad de pago antes de explicar esquemas.**
- **Financiación de a poco, con enganche; el número fino lo cierra un humano.** Comunicar pisos y
  rangos, nunca cerrar un número; cifras sensibles (cuota, comisión) no se calculan, se derivan.
- **No afirmar estados legales/administrativos sin respaldo de la fuente** (escritura, apto
  crédito, disponibilidad); si preguntan y no está, derivar.
- **Segmentos que no son lead comprador se detectan y derivan sin calificar** (intermediarios,
  socios, proveedores, referidos), cada uno con su frase y ruteo. El mapa de nombres es instancia.
- **Derivar cuando hay dinero concreto o se agota el margen conversacional;** temas de riesgo
  (fiscal, legal, crédito) se derivan sin asesorar.
- **Ante producto ajeno, reconducir al catálogo propio, no cortar.**
- **Material de venta como salida comercial, nunca adjunto suelto:** el brochure va con imágenes y
  fusionado en un CTA con el paso de mayor valor (video de obra, visita).
- **Canal B2B / intermediario con reglas de contacto propias:** el intermediario es el contacto
  único, no se salta al cliente final, las condiciones las cierra el equipo.
- **Reconocer al cliente recurrente y sacarlo del flujo estándar,** con trato preferencial.
- **Rentabilidad como rango, nunca garantía;** objeción macro (dólar/inflación) no abre debate;
  comparación con competencia sin denostar; cochera como complementario independiente; no sesgar
  el uso esperado por perfil (no "ideal Airbnb" a quien busca vivienda).

### Candidatos a transversal detectados en desarrollista (esperan confirmación en otro rubro)
- **Doble salida al cierre** (EDFAN): toda respuesta cierra ofreciendo dos caminos, uno es "ver
  más de lo mismo". Fuerte, pero visto en un solo cliente.
- **El CTA se amolda al contexto** (EDFAN): el paso siguiente puede ser encuentro, material o más
  opciones; no hay un CTA único obligatorio.
- **Palanca de financiación como acceso, no deuda** (G&D): la financiación se presenta como forma
  de acceder a un producto mayor, no como deuda.
- **Decir de frente lo que el negocio no ofrece** (EDFAN): si el modelo no ofrece un tipo de
  producto que el lead pide, se dice de frente y se reconduce.
