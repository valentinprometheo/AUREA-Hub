---
name: aurea-ic-criterio-comercial
description: Criterio comercial de AUREA para los tableros de Inteligencia Comercial sobre Prometheo. Define qué dato se agrega dentro de cada consulta (núcleo fijo de cinco campos de Gap Selling, Jobs to be Done y SPIN, más una capa variable por rubro con JTBD, Hormozi o Solution Selling), cómo lo extrae el agente, cómo se audita su cobertura y cómo se muestra en el tablero. Usala SIEMPRE que haya que elegir la metodología de venta de un cliente, diseñar o auditar los campos de problema, impacto, causa raíz, evento disparador o resultado de contacto, reforzar el prompt del agente para cargarlos, armar la pestaña de criterio comercial, cruzar impacto con disparador, o preparar la Consultoría 02 (capacitación comercial aplicada al agente). Activar ante "criterio comercial", "Gap Selling", "Jobs to be Done", "JTBD", "SPIN", "Hormozi", "evento disparador", "impacto", "causa raíz", "resultado de contacto", "capa variable", "qué metodología le corresponde".
---

# Criterio comercial (AUREA · Inteligencia Comercial)

El tablero base cuenta cuántas consultas entran y de qué anuncio vienen. El criterio
comercial lee lo que pasa **dentro** de cada consulta: qué problema trae el cliente y
por qué consulta hoy. Es la lógica de venta que le prestamos al cliente que no la tiene.

Esta skill decide **qué dato se agrega**. `aurea-hub-criterio-calificacion-leads` decide
**quién es un lead calificado y quién es hot**. `aurea-ic-curaduria-del-dato` decide **si se puede
mostrar**. `aurea-dashboard-design` decide **cómo se ve**. `aurea-metodologia` decide
**cómo se carga en el CRM**.

Filtro de entrada para cualquier metodología: **si la aplicamos, ¿qué dato nuevo queda
registrado en Prometheo?** Si no produce un campo que el agente pueda extraer de una
conversación de WhatsApp, no entra al tablero.

---

## 1. Núcleo fijo: cinco campos

Se extraen de la misma conversación, sin preguntar de más.

| Campo | Qué registra | Viene de | Lo carga | Tipo de señal |
|---|---|---|---|---|
| Problema declarado | Lo que el cliente dice, en sus palabras | Gap Selling | Agente | Dura (cita literal) |
| Impacto | Qué le cuesta no resolverlo | Gap Selling | Agente | Blanda |
| Causa raíz | Qué produce el problema de fondo | Gap Selling | Agente | Blanda |
| Evento disparador | Qué pasó para que consulte hoy | Jobs to be Done | Agente | Media |
| Resultado de contacto | Orden, avance, continuación o no venta | SPIN | Equipo | Dura (si se carga) |

### Definiciones operativas

Completá las marcadas como `[A DEFINIR]` con el cliente o en el discovery. No inventes
umbrales: si falta la definición, el campo no se puede auditar y no titula.

- **Problema declarado.** Texto libre, cita textual del lead. Nunca parafrasear al cargar.
- **Impacto.** Escala `alto / medio / bajo / sin dato`.
  - Alto: hay un costo concreto y presente por no resolverlo (ej.: obra frenada,
    mudanza con fecha, pérdida de venta propia). `[A DEFINIR por rubro]`
  - Medio: costo declarado pero sin urgencia ni cifra. `[A DEFINIR por rubro]`
  - Bajo: exploración o comparación sin costo declarado ("estoy mirando precios").
- **Causa raíz.** Lista cerrada por rubro `[A DEFINIR por rubro]` más "otra" con texto.
  Si el agente la infiere en vez de que el lead la declare, se marca origen = inferido.
- **Evento disparador.** Dos variables: el evento (lista cerrada por rubro
  `[A DEFINIR]`) y su antigüedad en días o en tramo (`< 30 días`, `30 a 90`, `> 90`,
  `sin dato`). El corte de 30 días es el que se usó en el ejemplo de PAVIR.
- **Resultado de contacto.** Lo marca el equipo después de cada contacto humano:
  - `Orden`: compró o reservó.
  - `Avance`: **hay una acción acordada con fecha**. Sin fecha, no es avance.
  - `Continuación`: la charla sigue sin compromiso con fecha.
  - `No venta`: se cierra sin compra, con motivo.

Los dos campos que más valor dan:

- **Impacto** ordena la cola por tamaño de problema y no por fecha de entrada.
- **Evento disparador** es el puente con marketing: explica el "por qué ahora" y es
  criterio para escribir el creativo de la pauta.

## 2. Capa variable: según cómo vende el cliente

Decidila en el discovery (la Value Pyramid es el guion de esa reunión; se usa para
elegir la capa, no va al tablero del cliente).

| Perfil del cliente | Capa que se suma |
|---|---|
| B2C de ticket alto, ciclo largo | Jobs to be Done completo (las cuatro fuerzas: empuje, atracción, ansiedad, hábito) |
| B2B de canal, recompra, visita de corredor | Gap Selling y resultado de contacto |
| B2C de consideración media | Gap Selling y Hormozi |
| Transaccional de volumen, ticket bajo | Solo Hormozi (el discovery no se paga) |
| B2B con comité de compra | Solution Selling |

Reglas:
- Un cliente tiene **una** capa variable. Si dudás entre dos, elegí la de ciclo más corto.
- Hormozi entra como heurístico de cuatro palancas, **no como ecuación**. No cites el
  ratio 3 a 1 con valores más altos que no estén verificados.
- The Unsold Mindset no produce dato: es tono de redacción del prompt del agente.

## 3. Cómo se carga (liga con `aurea-metodologia`)

**Reusar las variables de IC que ya existen en el CRM, no crear nuevas.** La metodología
ya define una familia de 6 variables de inteligencia comercial (patrón dual: Opciones para
contar + Texto largo para la frase literal):

| Campo del criterio comercial | Variable que ya existe en Prometheo | Nota |
|---|---|---|
| Problema declarado | Dolor Principal (Texto largo) | Mismo concepto: el problema de fondo, en palabras del lead |
| Impacto | — (nueva, Opciones: alto / medio / bajo) | Solo si el cliente tiene la capa de Gap Selling |
| Causa raíz | — (nueva, Opciones por rubro) | Solo si el cliente tiene la capa de Gap Selling |
| Evento disparador | Disparador Compra (Texto largo) | **Definición en conflicto**, ver abajo |
| Resultado de contacto | — (tag manual del equipo, sin prompt) | Las etapas humanas no llevan prompt de IA |
| (insumo de Insights) | Objeción Principal + Frase Literal · Pedido Fuera de Catálogo + Detalle | Taxonomía de objeciones idéntica entre clientes del mismo rubro |

> Conflicto abierto `[A DEFINIR]`: para la metodología, *Disparador Compra*
> es "qué destrabaría la decisión"; para esta skill, el evento disparador es "qué pasó
> para que consulte hoy". Hasta resolverlo, no se crea una variable nueva: se lee
> *Disparador Compra* y se declara cuál de las dos definiciones usa su prompt.

Cada variable nueva tiene costo: se evalúa en cada conversación (en EDFAN la extracción
fue el 16% del gasto de IA). Antes de sumar impacto o causa raíz, confirmar que el cliente
las va a usar.

- La extracción vive en la plataforma (variables de Prometheo); el prompt del agente
  solo refuerza. Nombrá cada campo como variable con el mismo nombre en todos los
  clientes para que el tablero sea comparable. Los nombres de base están en la tabla de
  arriba (familia de 6 variables de IC de la metodología).
- Impacto y causa raíz son **señales blandas**. En EDFAN las blandas se cargaron al 5 y
  10% mientras las duras llegaban al 50%. Si no se refuerzan en el prompt, nacen como
  Indicio y no titulan nada. El refuerzo debe:
  1. Pedir que el agente registre impacto y disparador apenas el lead los menciona,
     sin hacer preguntas extra si la conversación no da pie.
  2. Priorizar estos dos campos por sobre el resto. Si el refuerzo nombra todo, no
     prioriza nada.
- Resultado de contacto lo carga el equipo: es un campo requerido al cerrar cada
  contacto humano (regla de `revops`: no avanza de etapa sin sus campos).

## 4. Cómo se audita (liga con `aurea-ic-curaduria-del-dato`)

Cada campo pasa por la escalera de evidencia antes de aparecer:

| Nivel | Cobertura | Uso del campo |
|---|---|---|
| Hecho | ≥ 80% | Puede titular una card |
| Señal | 40 a 79% | Card con denominador explícito |
| Indicio | 10 a 39% | Bullet o modo Avanzada |
| No reportable | < 10% | Calidad de datos, como hallazgo de proceso |

- Medí la cobertura real de los cinco campos **a los 30 días** del primer cliente.
- Declarar origen: problema = declarado; impacto y causa raíz = casi siempre inferido
  por el agente (más frágil); resultado de contacto = equipo.
- Si un campo no llega a Señal, el hallazgo es la cobertura, no la distribución.

## 5. Cómo se muestra (liga con `aurea-dashboard-design`)

**Relación con la calificación:** el criterio comercial no reemplaza la definición de
calificado del cliente ni la de hot lead. Se lee **dentro** de esa clasificación:
- Impacto × disparador ordena a quién llamar primero entre los calificados y los hot leads.
- Un hot lead con impacto alto y sin seguimiento es la acción más urgente de "¿Qué hago ahora?".
- Resultado de contacto "Avance" (acción acordada con fecha) es la evidencia de la
  etapa humana: se cruza con los tags de visita o reunión.

- Pestaña o sección **Criterio comercial**, dentro de la pregunta "¿Qué pide el mercado?"
  (problema, impacto, causa, disparador) y "¿Qué hago ahora?" (cola priorizada).
- **Cola priorizada por impacto**, no por fecha de entrada.
- **Cruce impacto alto × disparador < 30 días**: el corte que identifica a quién llamar
  primero. Ninguno de los dos campos lo produce por separado. Mostralo solo si ambos
  campos llegan a Señal; si no, va a Calidad de datos con el insight que desbloquearía.
- Disparadores más frecuentes como insumo para creativos (modo Avanzada).
- Resultado de contacto: avance vs continuación, que es el cruce de etapa declarada vs
  etapa por evidencia aplicado a la reunión.
- Citas de problema declarado en tarjetas de texto, sin barra ni porcentaje.
- Si los datos son modelados (como PAVIR), decirlo en el mismo bloque.

## 6. Procedimiento

1. Clasificá al cliente en uno de los cinco perfiles y elegí la capa variable.
2. Completá las definiciones `[A DEFINIR]` para el rubro.
3. Verificá con `aurea-metodologia` que las variables existan en Prometheo y que el
   prompt del agente tenga el refuerzo.
4. Con el export, medí cobertura y origen de cada campo (`aurea-ic-curaduria-del-dato`).
5. Armá la sección según el nivel de evidencia de cada campo.
6. Corré el checklist.

## 7. Checklist

- [ ] El cliente tiene una sola capa variable, elegida por perfil.
- [ ] Los cinco campos tienen definición operativa para el rubro (sin `[A DEFINIR]`).
- [ ] Impacto y disparador están reforzados en el prompt del agente.
- [ ] "Avance" exige acción acordada con fecha.
- [ ] Ningún campo titula sin llegar a Hecho; impacto y causa raíz declaran origen.
- [ ] El cruce impacto × disparador solo aparece si ambos llegan a Señal.
- [ ] Si los datos son modelados, lo dice.

## Pendientes conocidos

- Este criterio todavía no se corrió sobre datos reales (EDFAN, 1.017 contactos). Las
  cifras de PAVIR (66% contra 31%) son modeladas.
- Sin gasto de Meta no hay capa de eficiencia: el criterio mejora la calidad de la
  lectura, no reemplaza el costo por consulta calificada.

## Referencias

- `references/informe-criterio-comercial.md`: el informe completo con el puntaje de las
  siete metodologías, el mapa de skills y las fuentes.
