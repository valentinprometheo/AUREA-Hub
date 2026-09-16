# Género · Presupuesto

> Género dentro de la **Familia A (deck)**. Es el deck que le presenta a un prospecto la **estimación de inversión** de su proyecto, como documento de referencia. Caso de referencia del formato: **PAVIR — Presupuesto AUREA Hub**.

Usa la estética de la Familia A (deck AUREA: base blanca, bandas de gradiente, esfera, Helvetica + itálica, HTML que pasa a PDF con aprobación). Para el render, leé `estetica-deck.md` + `estetica-deck-system.md`. Este módulo aporta la **estructura y la forma de presentar los números**, no una estética nueva.

## Qué es y qué no es

- **Es** el primer frente con fecha: presenta el alcance del proyecto y una estimación de magnitud de la inversión para que quede claro qué se contrata.
- El presupuesto es **una de las tres partes** de una propuesta AUREA típica. En PAVIR el hero lo dice: la propuesta se ordena en 01 Diagnóstico de la operación, 02 Presupuesto del CRM con IA (el frente con fecha), 03 Plan de acción (pautas y Marketing se suman después, cada uno en su momento).
- **No es** un contrato ni una factura. Los montos formales, la mecánica de facturación y las firmas viven en la **Documentación formal (Familia B)**. El presupuesto los anticipa como referencia, no los formaliza.

## La estructura narrativa (esqueleto fijo, contenido adaptado)

**Portada / hero.** Header de marca (logo + esfera) + dos eyebrows ("DISEÑO DE PROCESOS COMERCIALES CON IA" y "PRESUPUESTO · [CLIENTE] · [MES AÑO]") + h1 que nombra el proyecto ("Estructuramos tu proceso comercial con IA.") + lead que ordena las partes con bullets numerados (01 / 02 / 03). Cerrar el hero con la nota de encuadre: **"Propuesta comercial de referencia. Este documento presenta el alcance del proyecto y una estimación de magnitud de la inversión, para que quede claro de qué hablamos. Las condiciones comerciales y el detalle definitivo se emiten a mayor detalle y definidos los servicios, y es el documento que se firma."**

**01 · Diagnóstico de la operación.** Cómo entra la demanda hoy, con stats defendibles (consultas por día por canal, % que se cae, dato que se pierde). Es el "antes", el problema que el presupuesto resuelve. Cada número anclado en la realidad del cliente, marcado como estimación cuando lo sea.

**02 · Presupuesto del CRM con IA.** El corazón. Qué incluye el alcance (implementación del CRM, agente IA, chat omnicanal, seguimientos) y la **estimación de inversión**:
- Un bloque de **inversión** con el plan de plataforma (ej. Prometheo desde USD X/mes + tokens) y los honorarios de consultoría/implementación (setup único vs abono, según el caso), cada monto marcado como confirmado, sugerido o a definir.
- Cuando aplique, el **ejemplo de ahorro**: costo de hacerlo a mano hoy (tabla tarea · horas · valor hora · costo mensual/anual, marcada como estimada) vs con AUREA (24/7, desde USD X + tokens). Cerrar con qué produce en rentabilidad.
- Card(s) de precio con el número grande en la itálica de acento (regla del deck), label gemelo con la card vecina, y la nota de cierre como pie con divisor.

**03 · Plan de acción / próximos pasos.** Qué frentes se suman después (pautas, Marketing 360, Inteligencia Comercial) y en qué orden, cada uno en su momento. Deja claro que el presupuesto de hoy es el frente con fecha y los demás entran cuando corresponda. Ver `nuevos-servicios.md`.

**Cierre · En una línea.** Un párrafo de una línea que condensa el valor + el cierre de marca (Master Partner Oficial de Prometheo, [CLIENTE] · [mes año]).

## Checklist de inputs

| Necesitás | De dónde sale |
|---|---|
| Nombre del cliente, mes | dato |
| El diagnóstico (cómo entra la demanda, canales, volumen, qué se cae) | la reunión / auditoría |
| El **alcance** que se presupuesta (qué incluye el proyecto) | lo acordado |
| Plan de plataforma y honorarios (montos, o "a definir" en rojo) | la Guía de Consultoría / lo acordado |
| Datos para el cálculo de ahorro (horas diarias, valor hora, canales) | la reunión / estimación acordada |
| Qué frentes se suman después (pautas, Marketing) | la oferta AUREA |

Si falta el alcance o los montos, **pedilos antes de generar**. Lo no confirmado va marcado como estimado o en placeholder rojo, **nunca inventado**.

## Reglas de contenido

- Todo monto sin confirmar va **marcado**: "(estimado)", "(sugerido)" o placeholder en rojo. Jamás inventar cifras.
- El cálculo de ahorro va **marcado como estimado** y con el alcance aclarado (cobertura parcial, solo horario, no incluye calificar/seguir/agendar).
- La nota de encuadre del hero ("propuesta comercial de referencia... el documento que se firma") es **obligatoria**: separa el presupuesto de referencia del documento formal.
- No mezclar con la Documentación formal: acá no van cláusulas, ni facturación, ni firmas. Eso es Familia B.
- Voseo, AUREA en mayúsculas, cero em-dashes.

## Tooling

Render con el sistema de la Familia A (deck `aurea_kit.py`, HTML por defecto, PDF solo con aprobación vía `render_single_page_pdf()`). Presentá siempre el archivo.
