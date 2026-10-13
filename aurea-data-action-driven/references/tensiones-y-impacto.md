# Tensiones entre fuentes y su impacto hoy en AUREA

No son errores de las fuentes: tiran para lados distintos según el contexto. Para cada
una, AUREA toma una postura y la ata a algo concreto que hacemos hoy. Si el contexto
cambia, se revisa la postura, no la fuente.

| # | Tensión | Lado A | Lado B | Postura AUREA hoy | Dónde impacta hoy |
|---|---|---|---|---|---|
| T1 | Data-driven o data-informed | Provost y Fawcett, Brynjolfsson: decidir con datos rinde más | Chen, Mosseri: delegar en lo medible te encierra en lo que ya existe | Data-informed con score: el dato propone, el criterio decide y se declara | Toda card lleva score; discovery y prompt v1 arrancan con score bajo sin culpa |
| T2 | Cuánto rinde ser data-driven | Paper 2011: 5 a 6% más productividad en 179 firmas | Nota HBR 2012: 330 empresas, 5% y 6% | No se promete un porcentaje al cliente; se cita como correlación en grandes empresas | Pitch y decks de IC (`aurea-ic-conocimiento`) |
| T3 | La escalera de Gartner | Más valor cuanto más prescriptivo | Críticos: la madurez no es lineal | Se premia el diagnóstico contrastado; predictivo solo con volumen | Componente 4 del score; clientes chicos no necesitan predicción |
| T4 | Autoría de What / So what / Now what | Borton 1970, Driscoll 1994 | Rolfe et al. 2001 | Citar "Borton (1970), adaptado por Driscoll y Rolfe" | Solo en documentos que citan la fuente |
| T5 | Para qué sirve un tablero | Few: monitorear de un vistazo, no es análisis | Senturus y Tableau: un insight accionable | Secciones 1, 2, 3 y 5 monitorean; "¿Qué hago ahora?" acciona | Arquitectura de `aurea-dashboard-design` |
| T6 | Qué hace accionable a un insight | Dykes: seis atributos, sin dueño ni métrica | Otras listas: dueño y resultado medible | Dueño y métrica obligatorios en la card | Sello con dueño; componente 6 del score |
| T7 | Medir para mejorar o deformar | Medir y fijar metas mejora el foco | Goodhart y Strathern: la meta deforma la medida | Guardiana obligatoria en toda card que premia una métrica | Ahorro de tokens (que no baje calificación); % de calificados (que no se afloje el criterio para subirlo) |
| T8 | Color en el tablero | Identidad de marca violeta, azul y rosa | Color solo como semántica | Sellos y bandas con paleta semántica propia | `anatomia-card.md` |
| T9 | Velocidad o rigor | Boyd y Ries: ciclos cortos, actuar y aprender | Estadística: esperar n suficiente | Con n chico se actúa igual, como prueba acotada y con fecha | Quincenas de IC, rondas de feedback de prompts, campañas con poco gasto |

## Cómo usar esta tabla

- Cuando una card choca con una regla, buscá la tensión: casi siempre la card está en un
  contexto distinto al que supuso la regla. Escribilo en el "por qué este score".
- Cuando una postura deja de servir (por ejemplo, un cliente con volumen para tests
  formales en T9), actualizá la columna "Postura AUREA hoy" con fecha.
