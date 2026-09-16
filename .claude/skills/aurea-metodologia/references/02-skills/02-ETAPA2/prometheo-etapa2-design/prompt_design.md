# MÓDULO: PROMPT DEL AGENTE — DISEÑO Y ESTRUCTURA

Output 2 de Etapa 2. Es el archivo .md que se copia y pega directamente en Prometheo.
**No es un documento de presentación — es el código del agente.**

---

## REGLAS DE FORMATO (NO NEGOCIABLES)

### El prompt SE LEE COMO TEXTO LITERAL por el agente
Esto cambia todo. Reglas que se derivan:

1. **Sin tablas markdown.** El agente las ve como `| header | header |` y las
   incorpora literalmente en sus respuestas. Catastrófico.
2. **Sin cuadros visuales, sin diagramas ASCII, sin emojis decorativos.**
3. **Sin headers markdown** (`# H1`, `## H2`). Usar separadores `===` entre
   secciones.
4. **Prosa redactada corrida.** El agente debe leer instrucciones como si fueran
   párrafos de un manual, no listas tipo bullet point fragmentadas.
5. **Listas SOLO cuando son enumeraciones operativas reales** (ej: lista de
   variables, lista de mensajes literales). Si es una explicación, va en prosa.

### Código y referencias técnicas
- Variables en sintaxis exacta: `proceso_actual`, `tipo_usuario`, `estado_venta`
- Smart Tags con hashtag: `#seguimiento_activo`, `#derivar_a_humano`
- Valores de variables sin comillas en prosa pero con comillas si están dentro
  de instrucciones de comparación: "si proceso_actual = 'venta'"
- Mensajes literales con emojis REALES (👋, ✅, ⚠️) — no placeholders

---

## ESTRUCTURA CANÓNICA (15 secciones + 3 anexos)

Cada sección separada por línea con `===` arriba y abajo del título.

### 1. IDENTIDAD Y MISIÓN
Quién es el agente, qué empresa representa, cuál es su misión principal y la
prioridad de objetivos cuando entran en conflicto. Ejemplo:
"Sos [Nombre], el asistente IA de [Cliente]. Tu misión principal es [verbo
principal — ej: maximizar descargas]. Si dudás entre [opción A] y [opción B],
siempre elegí [B]."

### 2. TONO Y ESTILO
Cómo habla el agente. Reglas concretas:
- Tuteo o usted (especificar cuál)
- Argentino con voseo (típico) o neutro
- Cercano vs formal
- Uso de emojis (cuándo sí, cuándo no)
- Largo de respuesta (típico: corto, 2-3 párrafos máximo)
- Qué NUNCA decir (palabras prohibidas, jerga técnica, etc.)

### 3. BIENVENIDA POR CANAL
El agente saluda distinto según el canal de entrada (whatsapp, instagram, mail,
tiktok, x). Para cada canal: ejemplo de bienvenida que reconoce el contexto.
**Nunca repetir bienvenida si ya hubo intercambio.**

### 4. MENÚ DE NAVEGACIÓN
Si el usuario pregunta de forma genérica, el agente puede ofrecer un menú con
las opciones principales. Lista las opciones (ej: "Quiero info de la app",
"Tengo un problema técnico", "Quiero hablar con alguien").

**Regla de hilo (crítica):** si el usuario YA declaró su intención (ej:
"quiero descargar la app"), el agente NO interrumpe el tema para mostrar el
menú. Sigue ese hilo. El menú es solo para casos donde no hay intención clara.

### 5. INFO DEL PRODUCTO
Toda la información del producto que el agente debe conocer:
- Qué es el producto (1-2 párrafos)
- Diferenciales (5-10 puntos)
- Funcionalidades específicas (si aplica)
- Casos de uso típicos
- Lo que NO hace el producto (importante para evitar promesas falsas)

### 6. LINKS OFICIALES
Lista de URLs que el agente puede compartir, con el contexto de cuándo usar cada
uno. Ejemplo:
- Link de descarga Android: [URL] — solo si sistema_operativo = android
- Link de descarga iOS: [URL] — solo si sistema_operativo = ios
- Link al sitio web: [URL] — para info general
- Mail de soporte humano: [email] — solo cuando deriva caso técnico

### 7. CONVERSIÓN / OBJETIVO PRINCIPAL
Detalla CÓMO el agente debe perseguir el objetivo principal. Ejemplo para venta:
"Tu objetivo final es que el usuario haga click en el link de descarga. Antes
de mandar el link, siempre preguntá Android o iPhone para mandar el correcto.
No mandes ambos."

### 8. VARIABLES DEL CRM (instrucciones de captura)
Para cada variable: nombre, qué representa, valores posibles, cómo el agente la
debe inferir de la conversación. Ejemplo:

"**proceso_actual**: identifica el motivo principal de la conversación. Valores:
venta, soporte, faq, seguridad, postventa. Default al inicio: venta. Cambiá si
el usuario explícitamente menciona un problema técnico (→ soporte), una pregunta
sobre cómo usar la app (→ faq), o un tema de seguridad/estafa (→ seguridad)."

Repetir para cada una de las N variables.

### 9. OBJECIONES TÍPICAS Y RESPUESTAS
Lista de las 5-10 objeciones más frecuentes que va a recibir el agente, con la
respuesta canónica para cada una. Ejemplo:

"**Objeción: 'Es realmente gratis?'**
Respuesta: Sí, descargar y publicar en MIA es 100% gratis. No tenemos planes
pagos por ahora. Si más adelante lanzamos servicios premium, te avisamos. Querés
que te pase el link de descarga?"

### 10. DERIVACIÓN A HUMANO
Cuándo y cómo el agente deriva. Reglas operativas:
- Antes de derivar, SIEMPRE recopilar info mínima (tipo_derivacion + severidad +
  resumen del caso en 1 frase)
- Cuando dispara `#derivar_a_humano`, explicar al usuario que el caso pasa al
  equipo humano y dar tiempo estimado de respuesta
- Listar los 6 valores de `tipo_derivacion` y cuándo aplica cada uno

### 11. CONDICIONES GENERALES (qué SÍ, qué NO)
Síntesis de la sección Autonomía del DOCX en formato prompt. Ejemplo:
"PUEDE: mandar links de descarga, explicar el producto, capturar variables,
asignar Smart Tags. NUNCA: mandar listados completos de productos por chat,
inventar funcionalidades, dar precios de planes pagos sin tenerlos confirmados."

### 12. EXCEPCIONES Y CASOS BORDE
Casos específicos que merecen instrucciones puntuales. Ejemplo:
- Si el usuario es menor de edad → derivación inmediata sin avanzar
- Si el usuario habla en otro idioma → responder en español pidiendo confirmación
- Si el usuario insiste con la misma pregunta 3 veces → derivar
- Si el usuario amenaza o agrede → cerrar conversación amigablemente y derivar a Trust & Safety

### 13. CIERRE Y SEGUIMIENTOS
Cuándo y cómo el agente activa `#seguimiento_activo`. Lista los 5 follow-ups
con: condición de disparo (proceso + estado + tiempo), tag macro requerida, y
texto literal o contextual del mensaje.

Para los seguimientos LITERALES, copiar el texto exacto con emoji real.
Para los seguimientos CONTEXTUALES, dar la instrucción de cómo armar el mensaje.

### 14. RESPUESTAS A FOLLOW-UPS
Cuando el usuario responde a un seguimiento automático, el agente NO debe tratar
esa respuesta como mensaje nuevo. Debe reconocer que es una respuesta al
seguimiento y avanzar la conversación desde donde quedó. Instrucción explícita.

### 15. LIMPIEZA MANUAL DE TAGS
Después de un handoff a humano, el equipo debe limpiar manualmente las tags
para que el agente pueda volver a tomar la conversación si corresponde. Esta
sección documenta esa responsabilidad operativa para que el agente la mencione
cuando el caso vuelve.

---

## ANEXOS (al final del prompt)

### Anexo A — CTAs por canal
Lista de calls-to-action por canal, con el wording exacto. Ejemplo:
- WhatsApp: "Querés que te pase el link?" / "Te ayudo a descargar?"
- Instagram: "Te dejo el link en el próximo mensaje 👇"
- Mail: "Te dejo el link de descarga abajo. Si tenés dudas, respondé este mail."

### Anexo B — Navegación dentro del producto
Si el agente necesita guiar al usuario a una funcionalidad específica de la app,
lista paso a paso de cómo llegar. Ejemplo:
"Para crear tu primera publicación: abrí MIA → tocá el botón + en la barra
inferior → seleccioná 'Vender' o 'Alquilar' → completá los datos → tocá
'Publicar'."

### Anexo C — Checklist de coherencia
Reglas finales que el agente debe respetar siempre:
- Solo 1 Smart Tag activa por conversación (regla v7 inviolable)
- Nunca repetir beneficios mencionados en los últimos 2 mensajes
- Nunca inventar zonas, productos, fechas o funcionalidades
- Nunca dar consejos legales o fiscales
- Si severidad = alta, push 24/7 + nunca prometer tiempo de respuesta exacto

---

## REGLA TOKKO (vertical real estate)

Para clientes desarrollistas inmobiliarios:
- **Lo que está en Tokko (CRM externo) NO se hardcodea en el prompt**.
  El prompt instruye al agente a "consultar Tokko" o "el equipo te va a pasar
  los detalles del proyecto", pero NO incluye listados de propiedades, precios,
  metrajes, etc.
- **Lo que NO está en Tokko SÍ va al prompt**: financiación, condiciones
  comerciales especiales, info del desarrollador, FAQs.

Esta regla aplica también a otros CRM externos (PrestaShop para e-commerce,
ficha.info para inmobiliarias, etc.).

---

## CHECKLIST FINAL DEL PROMPT

- [ ] 15 secciones canónicas + 3 anexos
- [ ] Sin tablas markdown (verificar grep de `|`)
- [ ] Sin headers markdown `#` (usar `===` entre secciones)
- [ ] Variables y Smart Tags en sintaxis exacta
- [ ] Mensajes literales con emojis reales
- [ ] Regla de hilo explícita en sección 4
- [ ] Regla "1 Smart Tag activa" en Anexo C
- [ ] Si vertical real estate: regla Tokko aplicada
- [ ] Listas solo en enumeraciones operativas (variables, mensajes), no en
      explicaciones
- [ ] Prosa redactada en el resto

---

## ANTES DE PEGAR EN PROMETHEO

1. Validar que el archivo .md no tenga código LaTeX, MathML u otros formatos
   exóticos (Prometheo no los renderiza)
2. Verificar largo total: típico 8-15 páginas. Si es más, recortar redundancia.
3. Hacer 3 simulaciones mentales: "qué pasa si el usuario dice X" — el prompt
   debe tener respuesta clara
4. Confirmar con el cliente las 3 preguntas críticas:
   - El emoji de saludo final para los seguimientos literales
   - Los responsables por tipo de derivación
   - El plan contratado con Prometheo (Pro/Enterprise para 24/7)
