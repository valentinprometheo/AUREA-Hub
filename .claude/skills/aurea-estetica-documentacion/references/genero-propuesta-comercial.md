# 04b · Propuesta Comercial y Proyectual

> Género específico dentro de la **familia 4 (presentación estética)**. Es el deck que se le arma a un prospecto para presentarle el plan de acción concreto, adaptado a lo que contó en la reunión. Caso de referencia del formato y la narrativa: **MAMUT — Propuesta Comercial y Proyectual**.

Usa la estética de la familia 4 (deck AUREA: gradiente, esfera, Helvetica + itálica, HTML que pasa a PDF con aprobación). Para el render, leé `estetica-deck.md` + `estetica-deck-system.md`. Este módulo aporta la **estructura narrativa y el timing**, no una estética nueva.

## Cuándo se hace (el timing)

El recorrido es: **feria o referencia → reunión con el prospecto → sacar notas → armar esta propuesta.** No se arma a ciegas: se arma DESPUÉS de escucharlos, y el documento entero está adaptado a los insights que dieron en la reunión. Por eso abre con "venimos de escucharlos, después de la reunión armamos esto".

Su función es que el prospecto **entienda la parte práctica del proyecto**, vista para su caso puntual: qué le pasa hoy, cómo se resuelve, qué cambia en su día a día y por qué conviene avanzar.

## El par: Propuesta + Guía

Esta propuesta es **el porqué** (la estrategia y la razón para avanzar). Va acompañada de la **Guía de Consultoría e Implementación**, que es **el cómo y el cuánto** (modalidad, roles, tiempos, metodología de 4 fases, honorarios). La propuesta no incluye precios ni mecánica de trabajo: los deriva a la guía. Siempre se entregan juntas.

## La estructura narrativa (replicar, adaptando el contenido a los insights)

El esqueleto es fijo; el contenido de cada sección se adapta a lo que el prospecto contó. El **hilo conductor** (el ángulo central) sale del insight principal de la reunión. En MAMUT ese ángulo fue "ordenar y exprimir el outbound antes de construir inbound"; en otro cliente será otro. Todo el documento se cuelga de ese ángulo.

**Portada / intro.** Header de marca + una línea de estrategia ("Diseñamos una estrategia para que [CLIENTE] venda más"). Bajada que aclara que es una estrategia, no una herramienta suelta, y que sale de escucharlos. Línea de credibilidad (ya implementamos con [rubro]: clientes reales del rubro). Aclaración de que el porqué está acá y el cómo/cuánto en la guía adjunta.

**1 · El punto de partida.** El diagnóstico de la situación actual, **punto por punto**. Cada item: la situación de hoy (un dolor real que mencionaron) → cómo lo resuelve la propuesta. Sumar etiquetas de cambio donde aplique (ej. RESPUESTA INMEDIATA, CAMBIAMOS EL ORDEN, EL PRESUPUESTO SE CUIDA). Esta sección es la más adaptada a la reunión: los dolores son los de ellos.

**2 · Un ejemplo de ahorro.** El costo de hacerlo a mano hoy vs hacerlo con IA. Tabla de inversión estimada (tarea · horas diarias · horas mensuales · valor hora · costo mensual · costo anual) marcada como **estimada**. Comparación "hoy a mano" (cobertura parcial, con horario) vs "con AUREA" (24/7, más capacidad, desde USD X + tokens). Cerrar con qué produce en rentabilidad (recupera conversaciones que se caen, escala sin sumar gente, libera horas para cerrar).

**3 · Cómo cambia la operación.** Los frentes concretos que cambian el día a día (Frente A / B / C), cada uno con su bajada y bullets. Típicamente: una sola interfaz para todos los canales, un agente que califica solo, seguimientos que no se caen. Adaptar los frentes al caso.

**4 · El equipo, enfocado en cerrar.** El embudo en tiempo real (los estadíos: Consulta → Calificado → Propuesta → Negociación → Cierre) y el reparto: el humano hace lo que cierra, la IA se queda con la parte de arriba del embudo. Opcional: qué hacer con el tiempo liberado.

**5 · Capacidades extra de la plataforma.** Lo que la misma cuenta habilita además de recibir y responder (ej. WhatsApp Marketing sobre la base del cliente, automatizaciones de seguimiento), aclarando que entra en el mismo plan y solo se suman los tokens.

**6 · Marketing y ventas integrados** (si aplica al caso). El modelo hub: ordenar la venta primero, generar datos e insights, y recién con eso construir la capa de marketing. Las capas (ventas sobre Prometheo / marketing con foco) y, si corresponde, la agencia recomendada del portfolio. Esta sección se incluye solo si el insight del cliente lo pide (en MAMUT sí, por el tema outbound/inbound).

**7 · El documento que te enviamos.** El puente a la Guía de Consultoría: un resumen de lo que van a ver en la guía (clientes del rubro, metodología de 4 fases, roles y alcance, impacto/números de Prometheo, modalidad y soporte, honorarios). Cierre del puente: "este documento te dice por qué conviene; la guía te dice cómo trabajamos y cuánto cuesta".

**Cierre · En una línea.** Un párrafo de una línea que condensa la estrategia para ese cliente, + el cierre de marca (Master Partner Oficial de Prometheo, estrategia diseñada para [CLIENTE] · [mes año]).

## Checklist de inputs

| Necesitás | De dónde sale |
|---|---|
| El **ángulo central** (el hilo conductor) | el insight principal de la reunión |
| Los **dolores actuales** punto por punto | notas de la reunión |
| Datos para el cálculo de ahorro (horas diarias en lo repetitivo, valor hora, canales) | la reunión / estimación acordada |
| Canales que usan hoy | la reunión |
| Rubro y clientes de referencia para la credibilidad | base AUREA |
| Plan y precio para el puente a la guía | la Guía de Consultoría |
| Nombre del cliente, mes | dato |

Si falta el ángulo central o los dolores concretos, **pedilos antes de generar**: sin los insights de la reunión esto se vuelve genérico y pierde el sentido (que esté hecho para ellos).

## Reglas de contenido

- El documento es **el porqué**: nunca mete honorarios ni mecánica de trabajo, los deriva a la guía.
- El cálculo de ahorro va **marcado como estimado** y con el alcance aclarado (cobertura parcial, solo horario, no incluye calificar/seguir/agendar).
- No prometer lo que no es: las capacidades son las reales de Prometheo + AUREA.
- Cerrar siempre con "en una línea" y el puente a la guía.
- Voseo, AUREA en mayúsculas, cero em-dashes (las reglas transversales del conductor).

## Tooling

Render con el sistema de la familia 4 (deck `aurea_kit.py`, HTML por defecto, PDF solo con aprobación vía `render_single_page_pdf()`). `present_files` siempre.
