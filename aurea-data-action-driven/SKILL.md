---
name: aurea-data-action-driven
description: Cómo AUREA pasa del dato a la acción y cuán basada en datos está cada acción. Toda card action-driven lleva un score data-driven (0 a 100%) calculado con una rúbrica trazable a fuentes, y cada regla declara la tensión de la que sale y en qué impacta hoy. Sirve para los tableros de Inteligencia Comercial, los documentos para clientes (Posibles mejoras, Fugas, Qué hago ahora) y el resto de la metodología e implementación de AUREA (corrección de prompts, calificación, consumo de tokens, discovery, testing). Activar ante "data-driven", "action-driven", "insight accionable", "score", "cuán basado en datos", "posibles mejoras", "fugas", "qué hago ahora", "cards de acción", "recomendación", "y entonces qué".
---

# Data-driven y action-driven en AUREA

## La idea central: dos ejes, no dos categorías

Toda card de acción es **action-driven**: propone algo que alguien ejecuta. Lo que
cambia entre una card y otra es **cuán data-driven es**, y eso se dice con un número.
No hay cards "verdaderas" y cards "falsas": hay acciones con mucha evidencia y apuestas
con poca, y el cliente tiene derecho a saber cuál es cuál.

- **Data-driven (en AUREA).** El número curado: tiene base, denominador y fuente, y
  responde "qué pasó y por qué" (Gartner descriptiva y diagnóstica).
- **Action-driven (en AUREA).** [DEFINICIÓN AUREA] La decisión con verbo, dueño, lugar
  donde se cambia, efecto esperado y forma de verificarlo (Gartner prescriptiva, "Now what").
- **Score data-driven.** [DEFINICIÓN AUREA] De 0 a 100%, cuánto de la acción se apoya
  en datos verificables y cuánto en criterio. Se calcula con la rúbrica de
  `references/score-data-driven.md` y siempre se justifica componente por componente.

AUREA es **data-informed** (Chen, Mosseri): el dato propone y el criterio decide. Un
score bajo no invalida la card; obliga a decir que es una apuesta y a medirla.

## Cómo se ve: título grande y score

```
[ CORREGIR · AUREA ]
Mensajes por lead · 406 leads de una consulta recibieron 4,8 mensajes
85% basada en datos  ████████▌░
Qué mide / Base / Dato (fuente)
▸ Qué hacer / Dónde se cambia / Efecto esperado / Cómo lo medimos / Por qué este score
```

| Banda | Etiqueta en la card | Qué implica |
|---|---|---|
| 80 a 100 | Basada en datos | Se ejecuta y se mide |
| 55 a 79 | Informada por datos | Se ejecuta; decí qué parte es criterio |
| 30 a 54 | Hipótesis con indicio | Se ejecuta como prueba acotada, con fecha de revisión |
| 0 a 29 | Criterio experto | Solo como *Medir* o *Decidir*, o con aval explícito del dueño |

Un 100% no es certeza: es la mejor evidencia disponible hoy. Lo dice Goodhart y lo dice
Chen: la métrica no ve lo que todavía no se construyó.

## Reglas (con su tensión de origen)

1. **Toda card declara su score y su "por qué".** Reemplaza al "sin dato no hay card":
   ahora la card existe, pero muestra cuánto se apoya en datos (tensión T1).
2. **Todo dato que ve el cliente tiene una lectura "y entonces qué"**, aunque sea
   "no requiere acción este período" (Few frente a dashboards accionables, T5).
3. **El efecto se mide con la misma métrica que el dato**, en el período siguiente y
   con la misma base (Build-Measure-Learn).
4. **Toda card que premia una métrica nombra una guardiana** (Goodhart, T7).
5. **Score bajo no frena, acota.** Con poco volumen se actúa con prueba chica y fecha,
   no se espera a tener n "suficiente" (OODA y Ries frente a rigor, T9).

Cada tensión, qué dicen las fuentes, qué postura toma AUREA y dónde impacta hoy:
`references/tensiones-y-impacto.md`.

## Dónde se usa

- **Tablero IC.** "¿Qué hago ahora?", "Posibles mejoras" y "Fugas". En Básico, tres cards
  por impacto; las de menos de 55% llevan la etiqueta de banda bien visible.
- **Documentos para clientes.** Misma card, todo desplegado, score incluido.
- **Corrección de prompts** (`prometheo-correccion-prompts`). Cada fila del Feedback del
  Agente lleva score: una captura suelta no pesa lo mismo que 40 conversaciones.
- **Calificación y tokens** (`aurea-hub-criterio-calificacion-leads`). Cambios de criterio
  o de prompt para ahorrar tokens llevan score y guardiana.
- **Discovery e implementación.** Antes del lanzamiento casi todo es criterio (score
  bajo, y está bien); el score sube a medida que entra dato real. Mostrar esa curva es
  parte del relato de mejora continua.

## Cómo trabajar

1. Partí del número curado (`aurea-ic-curaduria-del-dato`). Anotá base, cobertura y fuente.
2. Escribí la lectura "y entonces qué" en una frase.
3. Elegí el verbo (`references/taxonomia-verbos.md`) y el dueño.
4. Completá Qué hacer / Dónde / Efecto / Cómo lo medimos.
5. Calculá el score con la rúbrica y escribí el "por qué" en una línea por componente.
6. Pasá `references/checklist-validacion.md` y compará con `references/ejemplos.md`.
7. Al cierre del período, registrá si el efecto se cumplió: eso calibra la rúbrica.

## Referencias

- `references/score-data-driven.md`: rúbrica, bandas, justificación y calibración.
- `references/tensiones-y-impacto.md`: puntos donde las fuentes tiran para lados distintos.
- `references/definiciones-y-fuentes.md`: definiciones con autor, URL y fecha de acceso.
- `references/taxonomia-verbos.md`: los seis sellos y los dueños.
- `references/anatomia-card.md`: estructura y HTML/CSS de referencia.
- `references/checklist-validacion.md` y `references/ejemplos.md`.
