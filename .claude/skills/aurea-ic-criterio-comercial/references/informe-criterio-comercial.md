# Criterio comercial · qué es, qué dato agrega y con qué skills se mide

Documento exportable de AUREA Hub. Explica la capa de criterio comercial del tablero
de Inteligencia Comercial y el conjunto de skills de diseño de métricas sobre las que
está construido.

---

## 1. Qué es el criterio comercial

El tablero base de Inteligencia Comercial cuenta cuántas consultas entran y de qué
anuncio vienen. El **criterio comercial** es la capa que agrega AUREA para leer lo que
pasa **dentro** de cada consulta: qué problema trae el cliente y por qué consulta hoy.

Es la lógica de venta que le prestamos al cliente que no la tiene. Hasta ahora esa
lógica era nuestra, implícita y distinta en cada cuenta. Esta capa la vuelve:

- **Explícita:** tiene nombre, fuente y campos concretos.
- **Elegible por rubro:** no hay una metodología única, hay un núcleo fijo y una capa
  variable según cómo vende el cliente.
- **Medible:** cada campo tiene su cobertura y su nivel de evidencia en el tablero.

Es también el contenido de la **Consultoría 02** del presupuesto (capacitación comercial
aplicada al agente), que hasta hoy no tenía método propio.

## 2. De dónde sale

Evaluamos siete metodologías con un solo filtro: **si la aplicamos, ¿qué dato nuevo
queda registrado en Prometheo?** Una metodología que no produce un campo que el agente
pueda extraer de una conversación de WhatsApp no entra al tablero.

| Metodología | Puntaje | Dónde va |
|---|---:|---|
| Gap Selling | 27 / 30 | Núcleo del tablero |
| Jobs to be Done | 27 / 30 | Núcleo del tablero |
| Hormozi ($100M Offers y Leads) | 25 / 30 | Capa de marketing |
| SPIN Selling | 22 / 30 | Un solo campo, al núcleo |
| Value Pyramid | 19 / 30 | Nuestro discovery, no el tablero del cliente |
| Solution Selling | 16 / 30 | Reservada para clientes con comité de compra |
| The Unsold Mindset | 16 / 30 | Tono del prompt del agente |

El puntaje no decide solo. Unsold Mindset saca 16 y igual entra, porque compite en otra
categoría: no produce dato de cliente, produce criterio de redacción. Value Pyramid saca
19 y es muy valiosa, pero para nosotros: es el guion de la reunión de discovery que
decide qué capa variable le corresponde a cada cliente.

Gap Selling y Jobs to be Done no compiten, se complementan. Gap responde **qué le pasa**
al cliente; JTBD responde **por qué se mueve ahora y qué lo frena**.

## 3. La información que se agrega: el núcleo fijo

Cinco campos, que el agente extrae de la misma conversación sin preguntar de más:

| Campo | Qué registra | Viene de | Lo carga |
|---|---|---|---|
| Problema declarado | Lo que el cliente dice, en sus palabras | Gap Selling | Agente |
| Impacto | Qué le cuesta no resolverlo | Gap Selling | Agente |
| Causa raíz | Qué produce el problema de fondo | Gap Selling | Agente |
| Evento disparador | Qué pasó para que consulte hoy | Jobs to be Done | Agente |
| Resultado de contacto | Orden, avance, continuación o no venta | SPIN | Equipo |

Dos de ellos mueven más que el resto:

- **Impacto** ordena la cola por tamaño de problema y no por fecha de entrada. Dos
  personas que piden lo mismo no valen lo mismo si una tiene la obra frenada y la otra
  está comparando.
- **Evento disparador** es el puente entre venta y marketing: explica el "por qué ahora"
  y sirve de criterio para escribir el creativo de la pauta.

**Resultado de contacto** es el único que no carga el agente sino el equipo. Distingue
una charla de un avance real: **avance exige una acción acordada con fecha**; sin eso es
continuación. Es el cruce de "etapa declarada contra etapa por evidencia", aplicado a la
reunión.

### La capa variable, según cómo vende el cliente

| Perfil | Capa que se suma |
|---|---|
| B2C de ticket alto, ciclo largo | Jobs to be Done completo (las cuatro fuerzas) |
| B2B de canal, recompra, visita de corredor | Gap Selling y resultado de contacto |
| B2C de consideración media | Gap Selling y Hormozi |
| Transaccional de volumen, ticket bajo | Solo Hormozi (el discovery no se paga) |
| B2B con comité de compra | Solution Selling |

## 4. Qué métricas hay en el tablero

Todo número pasa por la skill de curaduría, cuya regla es que **ningún número se
muestra sin base, cobertura, origen y confianza**. La **escalera de evidencia** decide
qué puede hacer cada dato según su cobertura:

| Nivel | Cobertura | Qué puede hacer |
|---|---|---|
| Hecho | 80% o más | Titular una card |
| Señal | 40 a 79% | Card con su denominador explícito |
| Indicio | 10 a 39% | Bullet o modo Avanzada, nunca titula |
| No reportable | menos de 10% | Va a Calidad de datos como hallazgo |

Esto aplica al criterio comercial mismo: impacto y causa raíz son **señales blandas**, y
en el caso real de EDFAN las señales blandas se cargaron al 5 y al 10 por ciento mientras
las duras llegaban al 50. Si no se refuerzan en el prompt del agente, este núcleo nace con
cobertura de indicio y no puede titular nada. Hay que medirla a los 30 días del primer
cliente.

**Qué mide hoy el tablero con rigor:**

- Calidad de cada anuncio: respuesta, identificación, calificación y derivación, con la
  misma definición para todos.
- Distribución de la demanda: zona, producto, perfil, forma de pago, objeción, siempre
  sobre su base declarada y con doble lectura cuando la cobertura es menor al 80%.
- Etapa declarada contra etapa por evidencia: en EDFAN, 6 contactos con el tag
  "Calificado" contra 386 que cumplen la evidencia.
- Canales propios: email (con tasa de empalme y CTOR) y WhatsApp masivo (respuesta sobre
  lectura, tier, calidad del número).

**Qué todavía no mide:** la **eficiencia**. Costo por consulta calificada, CAC y retorno
por anuncio dependen de dos inputs que hoy faltan: el gasto de Meta y que el cliente
registre el cierre.

## 5. Un ejemplo de lo que habilita

El cruce de **impacto alto con disparador de menos de 30 días** identifica contactos que
cierran al 66% contra 31% de la media. Ninguno de los dos campos produce ese corte por
separado: impacto sin disparador da problemas sin urgencia; disparador sin impacto da
urgencia sin tamaño. Hoy esos contactos esperan en la misma cola que quien compara precios
por curiosidad.

> Aclaración de honestidad: las cifras de PAVIR son **modeladas**, para mostrar la forma
> del insight. Los datos reales están en EDFAN (1.017 contactos) y el criterio comercial
> todavía no se corrió sobre ellos.

## 6. Skills de diseño de métricas integradas

El criterio comercial define **qué dato se agrega**. Estas skills definen **cómo se mide,
se audita y se muestra**.

### Propias de AUREA

| Skill | Qué resuelve | Aporte propio |
|---|---|---|
| `aurea-curaduria-dato` | Qué número se puede mostrar y con qué base | La escalera de evidencia, el denominador honesto de doble lectura, la base curada y el cruce de etapa declarada contra etapa por evidencia |
| `aurea-email-prometheo` | Métricas de campañas de email que terminan en una conversación | El clic deja de ser el final y pasa a ser el empalme. CTOR además de CTR. La apertura es señal inflada y nunca titula |
| `aurea-whatsapp-prometheo` | Métricas de campañas masivas desde el propio CRM | En WhatsApp no existe el clic: titula la respuesta, no la lectura. Tier y calidad de número tratados como métricas de tablero |
| `aurea-dashboard-design` | Cómo se ve y cómo se opera el tablero | Doctrina Básico y Avanzada, el embudo como pasos y no a escala, delta obligatorio, color semántico separado del de marca |
| `aurea-metodologia` | Diseño del CRM aguas arriba (embudos, tags, variables) | Es lo que la curaduría audita: una etapa de embudo es una Smart Tag, el embudo marca de quién es el trabajo |

### De terceros, licencia MIT

| Skill | Qué aporta | Límite que tuvimos que cubrir |
|---|---|---|
| `attribution` | Epistemología del número: todo modelo es una opinión, el gap entre dos lecturas es el insight, los faltantes son estructurales | Está pensada para marketing digital general, no para atribución con conversación |
| `revops` | Disciplina del registro: etapas con criterio de entrada y dueño, campos requeridos, higiene como ritual | Nace en B2B SaaS y hay que traducir fit y engagement al rubro |
| `emails` | Diseño de secuencia y plantilla de reactivación | No trae métricas, y sus benchmarks son de prospección fría, que no sirven para base propia |

`interface-design` y `frontend-design` también están integradas, pero son de diseño visual,
no de métricas.

### Cómo se cruzan

- `attribution` y `revops` resuelven mitades distintas del mismo problema: una disciplina
  **números**, la otra disciplina **registros**. La curaduría es el cruce de las dos: la
  regla de `revops` de que una etapa no avanza sin sus campos se portó al reporte como "un
  dato no asciende a titular sin cobertura".
- `aurea-email-prometheo` y `aurea-whatsapp-prometheo` heredan de la curaduría las reglas
  de base, cobertura y fuentes, y le suman lo específico de cada canal.
- `aurea-metodologia` es aguas arriba de todo: lo que la curaduría audita, esa skill lo
  diseña.

## 7. Lo que falta

1. **El criterio comercial todavía no es una skill.** Vive como informe y como pestaña de
   PAVIR, así que no se activa solo. Empaquetarlo es el próximo paso.
2. **Los benchmarks de email y WhatsApp no existen todavía**, porque las campañas están
   modeladas y no corridas. El criterio de medición es sólido; las referencias hay que
   construirlas con datos reales.
3. **La capa de eficiencia.** Sin gasto de medios no hay costo por consulta calificada ni
   retorno por campaña. Es el bloqueo más grande del producto.
4. **El criterio comercial sobre datos reales.** Hay que correrlo sobre EDFAN y medir la
   cobertura real de los cinco campos antes de afirmar que funciona.

## 8. Fuentes y créditos

Las cifras de las metodologías de venta y de Hormozi salen de una investigación con fuente,
cuyo nivel de verificación se declaró afirmación por afirmación. Tres cosas que conviene no
repetir sin chequear: la ecuación de valor de Hormozi **no es una ecuación**, es un
heurístico de cuatro palancas; su ratio de 3 a 1 entre ganancia bruta y costo de
adquisición está confirmado, pero los valores más altos que circulan atribuidos a él no se
pudieron verificar; y la Value Pyramid **no tiene una atribución publicada**, la versión
pública más cercana es la de seis niveles de MEDDICC.

`attribution`, `revops` y `emails` son de Corey Haines (MIT). Las skills propias de AUREA y
este documento son material de AUREA Hub.
