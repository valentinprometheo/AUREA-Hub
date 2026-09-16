---
consultar-cuando: un bug puntual que se repite en varios casos, una regla muy reforzada que pisa otra, un CTA que no vende, una acción obligatoria que falla al entrar por anuncio
disparadores: "contradicción de jerarquía", "regla que pisa a otra", "PAROS", "muestra solo 2", "no saluda", "CTA que no vende"
fuente-única-de: el tipo de error "contradicción de jerarquía" y sus dos hermanos (CTA administrativo, condición ambigua)
combina-con: 10-patrones-correccion-agente (patrones 11, 12, 13), metodologia-correccion-agente (barrido chequeos 2 y 5)
---

# Contradicciones de jerarquía en prompts de agentes IA

> Documento de método. Un tercer tipo de error, más difícil de ver que "prompt" o "plataforma".
> Nace del caso PAROS (BETROX) pero aplica a cualquier cliente. Los patrones 11, 12 y 13 de
> `10-patrones-correccion-agente.md` son la versión corta; este archivo es el desarrollo.

---

## El tercer tipo de error

Veníamos clasificando los errores del agente en dos causas: **prompt** (algo mal escrito o de
menos) y **plataforma** (algo que la integración no puede hacer). Falta un tercero, estructural:
la **contradicción de jerarquía**. No es que falte una regla: hay **dos reglas nuestras, las dos
correctas por separado, que compiten** en el mismo turno, y el agente resuelve la competencia de
la peor manera. El síntoma parece un bug puntual de un producto; la causa afecta a toda una
familia de casos. Lo confirmó el soporte de Prometheo sobre PAROS: el problema no estaba en
PAROS, sino en una contradicción de jerarquía del prompt.

## El caso que lo disparó

El cliente pidió "info de toda la línea PAROS" y "ver medidas de todos". El agente mostró 2
modelos y cortó. Convivían dos reglas: A (escrita y reforzada) "mostrá 2 modelos por turno"; B
(nunca escrita) "si el cliente pide todo, dale todo". El agente aplicó la única que tenía. **La
regla fuerte se comió al caso que nadie contempló.**

## Cómo se reconoce (tres señales)

1. **El síntoma es puntual pero se repite.** "Con PAROS muestra 2" también pasaría con SIT, con
   las mesas, con cualquier familia. Si al ver el bug pensás "esto seguro pasa también en...", es
   candidato.
2. **La regla que falla está, y está bien escrita.** No la olvidamos: otra más fuerte la anula en
   ese contexto.
3. **Reforzarla lo empeora.** La solución no es reforzar, es **declarar la jerarquía**.

## Cómo se corrige (tres partes, ninguna es "reforzar")

1. **Nombrar los dos casos y separarlos.** Recomendación abierta → 2 por turno. Pedido de
   totalidad → todos. La regla nueva no reemplaza a la vieja: declara su límite.
2. **Hacerla general, no puntual.** "Excepción para PAROS" está mal: corrige un producto y deja
   el resto roto. La regla correcta habla de "cualquier línea, familia o categoría" y de una
   lista de disparadores ("todos", "toda la línea", "todas las medidas", "todas las variantes").
3. **Declarar la prevalencia y propagarla.** La regla vive en un lugar (cantidad) pero otras
   secciones hablan del mismo comportamiento (embudo, sección de la línea). Las tres remiten al
   mismo criterio, o la contradicción vuelve por otro lado. Es el chequeo de propagación.

## Dónde entra en el barrido de coherencia

- **Chequeo 2 (contradicción entre reglas):** por cada regla nueva o reforzada, ¿hay otra que
  aplique al mismo turno? Una regla muy reforzada es sospechosa: cuanto más fuerte, más casos
  legítimos puede estar pisando sin que se vea.
- **Chequeo 5 (ámbito de cada regla):** toda regla con SIEMPRE, NUNCA, MÍNIMO o un número fijo
  tiene que declarar a qué caso aplica y a cuál no. Un absoluto sin ámbito es una contradicción
  esperando a pasar.
- **Regla de método:** cuando una regla tiene un número o un absoluto, preguntarse "¿qué pasa si
  el cliente pide justo lo contrario de lo que esta regla asume?". En "2 por turno", lo contrario
  es "quiero todos". Ese contraejemplo es el que hay que contemplar.

---

## Hermano 1 — CTA que existe pero no vende

Un CTA puede ser gramaticalmente correcto y aun así no ser comercial. El agente cerró con "te
confirmo las medidas con el equipo, ¿querés que siga con los precios?". Eso es un CTA (hay
pregunta que invita a seguir) pero **administrativo, no comercial**: no acerca la venta, suena a
trámite. La lógica que faltaba: **el cierre no solo tiene que existir, tiene que vender.** Un
pendiente con el equipo nunca es el cierre; va aparte, en una línea, y el CTA comercial va igual.
Se caza leyendo si el CTA usa una lógica comercial, no con un chequeo de presencia. Es el patrón
12, y su cara positiva (qué hace que un cierre venda) vive en `logica-comercial-transversal.md`.

## Hermano 2 — Regla condicionada a una evaluación ambigua

El saludo de mobiliario urbano fallaba al entrar por un anuncio de Meta. La regla decía "saludá
solo si es el primer mensaje de toda la conversación"; ante un anuncio o una etiqueta del sistema
previos, el agente concluía que "ya había algo" y no saludaba. El problema no era la regla, era
**la evaluación que le pedía**. Criterio: cuando una regla depende de una evaluación que el
agente puede interpretar mal, no se refuerza la regla, **se cambia la condición por una binaria
sobre un hecho verificable** ("¿ya saludaste vos?" en vez de "¿es el primer mensaje?"), y se
nombra qué NO cuenta (anuncio, etiqueta, metadato). Generalización: cualquier regla que arranque
con "si es el primer / el último / el único / si ya pasó X" depende de interpretar contexto y es
candidata a fallar. Es el patrón 13.

---

## Resumen operativo

- **Contradicción de jerarquía:** dos reglas correctas que compiten; una pisa a la otra. Se
  corrige nombrando los dos casos, generalizando y declarando prevalencia, nunca reforzando.
- **Señal de alarma:** una regla muy reforzada con un número o un absoluto, y un bug que "seguro
  pasa también en otros casos".
- **CTA que no vende:** un cierre correcto pero de trámite. Tiene que usar lógica comercial.
- **Condición ambigua:** preferir hechos verificables ("¿ya hice esta acción?") sobre
  interpretación de contexto ("¿en qué punto de la conversación estamos?").
- Los tres se cazan leyendo coherencia y comercialidad, no presencia.
