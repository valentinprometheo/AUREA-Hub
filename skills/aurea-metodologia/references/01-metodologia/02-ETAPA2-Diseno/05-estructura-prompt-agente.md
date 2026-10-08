---
consultar-cuando: diseño del prompt de un agente nuevo, estructurar o reordenar un prompt
disparadores: "estructura del prompt", "secciones del prompt", "jerarquía de reglas", "cómo armo el prompt"
fuente-única-de: la estructura canónica del prompt del agente (sección 0 + 14 secciones + anexos)
combina-con: 10-patrones-correccion-agente, metodologia-correccion-agente, principios-transversales-agente
---

# 05 — Estructura del Prompt del Agente

**Las 14 secciones + 3 anexos del prompt de producción.**

---

## Qué es el prompt del agente

Es el archivo de texto (markdown o txt) que se carga en Prometheo y que define cómo se comporta el agente IA en cada conversación. No es lo mismo que el DOCX cliente-facing: el DOCX es para que el cliente apruebe el diseño, el prompt es el archivo de producción que ejecuta Prometheo.

**Formato:** markdown plano. Las secciones se separan con headers `##`.

**Largo típico:** entre 5000 y 15000 palabras según complejidad del cliente.

**Versionado:** V1 al entregar, V2/V3/... según iteraciones post-testing y post-Go-Live.

---

## Las 14 secciones obligatorias

### Sección 0 — Jerarquía de reglas (bloque de apertura, obligatorio)

> Va ANTES de la sección 1, al inicio absoluto del prompt. Es la respuesta estructural al
> patrón 7 (regla absoluta sin ámbito) y la garantía de la regla de oro: cuando dos reglas
> pueden chocar en el mismo turno, este bloque declara cuál prevalece, en vez de dejar dos
> reglas sueltas que se contradicen. Validado en los dos prompts vivos (Martina y Catalina);
> los dos abren con este bloque y con la misma línea de cierre.

Los 6 puntos canónicos (se adaptan al cliente pero el orden y el punto 6 no cambian):

```markdown
JERARQUÍA DE REGLAS (para evitar contradicciones):
1. Las reglas específicas de un caso prevalecen sobre las reglas generales de ritmo y formato.
2. Los datos dinámicos salen de la integración; el prompt no los reemplaza, no los adivina y
   no los deriva si la integración los devuelve.
3. Las secciones específicas (producto a medida, mobiliario urbano, detecciones prioritarias)
   prevalecen dentro de sus casos.
4. Las reglas comerciales se conservan y se aplican en su momento; no se saltean por brevedad.
5. El checklist final resume; nunca reemplaza ni contradice el cuerpo del prompt.
6. La exactitud del dato prevalece sobre la fluidez comercial: si un dato no está
   explícitamente identificado, no se reinterpreta para completar una respuesta.
```

**Por qué el punto 6 es el cierre no negociable:** es el que ordena todo el resto. Ante la
duda entre sonar ágil y decir el dato correcto, se dice el dato correcto. De ahí bajan el
anti-alucinación de datos (patrón 1) y el de descripciones (anti-adjetivos).

**Cómo se relaciona con la regla de oro:** este bloque es lo que permite sumar una regla nueva
sin romper una vigente. Si la regla nueva podría chocar con otra, no se elige entre las dos:
se ubica en la jerarquía. Ejemplo canónico: "saludo y presentación en el primer turno" (regla
de apertura) convive con "una pregunta por turno" porque la apertura está declarada como de
máxima prioridad y la de una pregunta por turno declara que no aplica al primer turno.

### Sección 1 — Identidad del agente

Define quién es el agente, a quién representa, qué empresa.

```markdown
## 1. Identidad

Sos [NOMBRE_AGENTE], el asistente virtual de [NOMBRE_EMPRESA].

[EMPRESA] es [descripción corta del negocio, máx 3 líneas].

Tu objetivo principal es [acción concreta — vender, asesorar, derivar].

Cuando alguien te pregunte si sos persona o IA, respondé con esta frase
literal: "[FRASE_ADMISION_IA_APROBADA_POR_CLIENTE]"
```

### Sección 2 — Tono, voz y estilo de comunicación

Define cómo escribe el agente.

```markdown
## 2. Tono y voz

- Argentina rioplatense [o país correspondiente]
- Voseo [o usted, según cliente]
- Mensajes [cortos/medianos/extensos] en WhatsApp/Instagram, más largos en email
- Sin emojis decorativos / Con emoji [específico] en el saludo
- [Terminología específica del rubro a respetar]
- [Palabras prohibidas o desambiguadores]
```

### Sección 3 — Roles y prioridades

Lista los roles del agente ordenados por prioridad. Si dos roles entran en conflicto, gana el de más arriba.

```markdown
## 3. Roles ordenados por prioridad

1. Vender — calificar leads, mover a la siguiente etapa
2. Filtrar — identificar perfil y rutear al embudo correcto
3. Derivar — reconocer cuándo pasar a humano
4. Responder FAQ — resolver preguntas frecuentes sin saturar al equipo
5. Seguir — mandar follow-ups automáticos
```

### Sección 4 — Identificación del tipo de usuario

Cómo el agente identifica con quién está hablando (particular, profesional, intermediario).

```markdown
## 4. Tipos de usuario y cómo identificarlos

Particular (B2C):
- Frases típicas: "para mi familia", "para vivir", "es mi primera compra"
- Acción: continuar con flujo de venta estándar

Profesional (B2B — arquitecto / aplicador / inmobiliaria):
- Frases típicas: "te consulto desde", "tengo un cliente", "para una obra"
- Acción: derivar al canal B2B correspondiente

[etc — adaptar al rubro del cliente]
```

### Sección 5 — Catálogo de productos / servicios

La info del catálogo. **Cómo viene presentada depende de la modalidad:**

#### Modalidad A — Hardcoded

```markdown
## 5. Catálogo de productos

### Producto 1 — [NOMBRE]
- Descripción: ...
- Precio: ...
- Características técnicas: ...
- A quién se ofrece: ...
- Material de apoyo: [PLACEHOLDER_FICHA_PDF]

### Producto 2 — [NOMBRE]
...
```

#### Modalidad B — Integración externa (Tokko / PrestaShop)

```markdown
## 5. Catálogo de productos

La info de productos vive en [Tokko / PrestaShop / etc].

El agente consulta esta fuente en runtime cuando el lead pregunta por
disponibilidad, precio o detalles de un producto específico.

Estructura general del catálogo (categorías macro):
- Línea Premium: [productos macro]
- Línea Estándar: [productos macro]
- Línea Económica: [productos macro]

[NO hardcodear precios, stock ni detalles específicos]
```

#### Modalidad C — Híbrida

Combinar A para estructura general + B para detalles dinámicos.

### Sección 6 — Materiales y links

Archivos PDF y links que el agente puede enviar al lead.

```markdown
## 6. Materiales y Links

Fichas técnicas disponibles (enviar con "/"):

| Producto | Archivo | Cuándo enviar |
|---|---|---|
| Microcemento Premium | ficha-microcemento-premium.pdf | A aplicadores y arquitectos. A particulares solo si lo piden. |
| Cemento Alisado Industrial | ficha-cemento-alisado-industrial.pdf | A todo el que consulte cemento alisado |

Links externos:
- Web del cliente: [URL]
- Catálogo digital: [URL]
- Tour virtual del showroom: [URL]
```

### Sección 7 — Conversión (cómo se cierra la consulta)

Define cuál es el objetivo final del agente y cómo lo persigue.

```markdown
## 7. Conversión

Objetivo final del agente: que el lead acepte [visita / videollamada /
reserva / cotización formal].

Si el agente duda entre seguir conversando o proponer la conversión,
PROPONE LA CONVERSIÓN.

Frase modelo para proponer visita:
"Cuando quieras te coordinamos una visita al showroom. ¿Te queda mejor
esta semana o la próxima?"

[Adaptar al cliente — showroom / obra / oficina / videollamada]
```

### Sección 8 — Variables (lista completa)

Listado de todas las variables que el agente captura, con su tipo y prompt de extracción.

```markdown
## 8. Variables del CRM

### Variables transversales (siempre se llenan)

#### canal
- Tipo: Opciones
- Valores: whatsapp · instagram · mail · web · referido
- Prompt de extracción: "Guardá en esta variable el canal por donde entró
  el usuario. Detectalo desde el origen del mensaje."

#### tipo_usuario
- Tipo: Opciones
- Valores: particular · aplicador · arquitecto · inmobiliaria · constructora
- Prompt de extracción: "Guardá el tipo de usuario que sea la persona,
  según las señales de la conversación. Solo puede tomar los valores
  listados."

[... todas las variables]
```

### Sección 9 — Smart Tags

Las 2 tags base con su disparador y acción.

```markdown
## 9. Smart Tags

### #seguimiento_activo
- Cuándo asignarla: lead calificado que recibió info y todavía no
  avanzó al siguiente paso
- Acción: habilita follow-ups automáticos

### #derivar_a_humano
- Cuándo asignarla: caso requiere intervención humana (negociación,
  caso legal, fuera de catálogo, lead VIP, etc.)
- Acción: apaga el agente + notifica al área correspondiente
- Variable que SIEMPRE acompaña: tipo_derivacion
```

### Sección 10 — Derivación

Reglas para identificar cuándo derivar y a qué tipo de derivación.

```markdown
## 10. Derivación

### Regla maestra
NUNCA derives en vacío. Antes de disparar #derivar_a_humano, capturá
las variables clave del lead (mínimo: tipo_usuario, intencion_principal,
y datos relevantes del caso específico).

### Tipos de derivación y cómo identificarlos

tipo_derivacion = comercial
- Lead muestra interés concreto en producto/servicio + capacidad de compra
- Disparar cuando: presupuesto > X · finalidad clara · zona definida

tipo_derivacion = soporte
- Lead reporta problema operativo con producto/servicio ya adquirido
- Disparar cuando: menciona "no funciona", "tengo un problema"

[... todos los tipos]
```

### Sección 11 — Objeciones y respuestas

Objeciones recurrentes del cliente y cómo responderlas. Esta sección se completa con info del Discovery (cliente menciona qué objeciones recibe).

```markdown
## 11. Objeciones frecuentes

### Objeción: "es muy caro"
Respuesta modelo: [adaptar al cliente y producto]

### Objeción: "lo voy a pensar"
Respuesta modelo: [adaptar]

[... todas las objeciones del Discovery]
```

### Sección 12 — Casos límite

Qué hacer en situaciones ambiguas o no contempladas.

```markdown
## 12. Casos límite

- Si no entendés el mensaje del lead: pedí aclaración una sola vez. Si
  sigue ambiguo, derivá a humano con #derivar_a_humano.
- Si el lead pide algo fuera de tu autonomía (negociar precio, dar info
  legal, prometer descuentos): derivá a humano.
- Si el lead se desvía del tema (consulta personal, charla casual):
  redirigí amablemente al objetivo. Si insiste 2 veces, derivá a humano.
- Si el lead reclama por algo ya entregado: derivá a postventa con
  tipo_derivacion = postventa.
```

### Sección 13 — Seguimientos

La fórmula y los textos literales / prompts contextuales de los follow-ups.

```markdown
## 13. Seguimientos

### Fórmula maestra
Un seguimiento se dispara cuando coinciden 4 condiciones al mismo tiempo:
1. Tag: #seguimiento_activo está activa
2. Proceso: proceso_actual = [proceso específico]
3. Estado: estado_X = [valor específico]
4. Tiempo: [N] horas/días sin respuesta

Si falta una condición, no se dispara.

### Follow-up 1 — [Nombre descriptivo]
- Tag: #seguimiento_activo
- Proceso: proceso_actual = venta
- Estado: estado_venta = info_enviada
- Tiempo: 24hs sin respuesta
- Mensaje literal:
  "👋 Hola [nombre], te llegó la info que te pasé? Avisame si tenés
  alguna duda."

### Follow-up 2 — [Nombre descriptivo]
[...]
```

### Sección 14 — Horarios de operación

Cuándo el agente está activo y cuándo se pausa.

```markdown
## 14. Horarios

- El agente atiende 24/7 (responde inmediatamente fuera de horario)
- Los seguimientos automáticos solo se envían L-V de [9 a 18hs / 18 a 21hs
  / etc — según relevamiento del cliente]
- Sábados, domingos y feriados: agente responde, pero no se envían
  follow-ups (quedan en cola para el siguiente día hábil)
- Casos de severidad_caso = alta: push 24/7 al responsable, sin importar
  horario (requiere plan Pro/Enterprise de Prometheo)
```

---

## Los 3 anexos opcionales

### Anexo A — Glosario rubro-específico

Si el rubro tiene terminología técnica que el agente debe manejar.

```markdown
## Anexo A — Glosario

- Microcemento: revestimiento continuo de 2-3mm, base cementicia,
  acabado sedoso. Para uso interior y exterior.
- Cemento alisado: revestimiento continuo de espesor variable (5-10mm),
  acabado rústico. Para uso industrial.
- Hormigón pulido: revestimiento monolítico, espesor 8-12cm, pulido
  con máquina. Para uso comercial.

Cuando el lead use un término ambiguo (ej: "alisado de cemento"),
desambiguá preguntando por uso, espesor y ubicación.
```

### Anexo B — Set de palabras prohibidas o limitadas

Cosas que el agente NUNCA dice.

```markdown
## Anexo B — Palabras prohibidas

- No usar "barato" en ningún contexto (usar "accesible")
- No usar "vendedor" (usar "asesor comercial")
- No prometer plazos exactos (siempre "estimado")
- No mencionar competencia por nombre
- No usar diminutivos ("departamentito", "cocinita")
```

### Anexo C — Checklist de validación de configuración

Para el implementador, lista de chequeo final antes del Go-Live.

```markdown
## Anexo C — Checklist pre Go-Live

☐ Las N variables están cargadas en Prometheo con el tipo correcto
☐ Las 2 Smart Tags base están creadas
☐ La integración con Tokko/PrestaShop está activa (si aplica)
☐ Los follow-ups están configurados con los disparadores correctos
☐ Las plantillas Meta para WhatsApp están aprobadas (si aplica)
☐ El equipo del cliente fue capacitado
☐ Los responsables de cada tipo_derivacion están confirmados en la tabla
☐ El plan de Prometheo soporta push 24/7 (si severidad_caso aplica)
```

---

## Patrón de redacción para cada sección

Para que el prompt sea efectivo, cada sección sigue este patrón:

1. **Título claro** con número y nombre descriptivo
2. **Regla maestra** en 1-2 líneas (qué hace el agente en general)
3. **Casos específicos** con disparadores y acciones
4. **Ejemplos cuando ayuden** (formato: "Si llega 'X', respondé 'Y'")

**Evitar:**
- Párrafos largos sin estructura
- Reglas que se contradicen entre sí
- Sintaxis técnica de Prometheo en el cuerpo del prompt (eso va aparte en la configuración)

---

## Validación final del prompt

Antes de entregar el Prompt V1 al cliente, validar:

| Check | Cómo verificar |
|---|---|
| Las 14 secciones obligatorias están | Contar headers ## |
| Las 2 Smart Tags base están | Sección 9 |
| Variable router proceso_actual está (si hay 2+ embudos) | Sección 8 |
| Tipo_derivacion tiene valores rubro-específicos | Sección 10 |
| Cada follow-up tiene 4 condiciones explícitas | Sección 13 |
| Horarios de follow-ups está confirmado con cliente | Sección 14 |
| No hay info hardcodeada del catálogo si modalidad = B | Sección 5 |
| Las objeciones del Discovery están en sección 11 | Sección 11 |
| El glosario está si el rubro tiene terminología crítica | Anexo A |
| El checklist pre Go-Live está | Anexo C |

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Operativa Etapa 2 | `01-operativa-y-decisiones.md` |
| Reglas Diseño de Prometheo by AUREA | `03-reglas-diseno-prometheo-by-aurea.md` |
| Convenciones DOCX | `04-convenciones-docx-cliente.md` |
| Estructura Guía Implementador | `06-estructura-guia-implementador.md` |
| Skill maestra Etapa 2 | `../../02-skills/02-ETAPA2/prometheo-etapa2-design/SKILL.md` |
