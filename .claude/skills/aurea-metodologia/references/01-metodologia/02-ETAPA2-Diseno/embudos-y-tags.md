---
consultar-cuando: Etapa 2, diseño de CRM, modelo de datos, perfiles de lead
disparadores: "smart tags", "embudos", "variables", "modelo de tags", "tipo perfil", "hot lead"
fuente-única-de: el modelo de datos (embudos, tags, variables) y el patrón variable+hija
combina-con: 03-reglas-diseno-prometheo-by-aurea, restricciones-plataforma-prometheo, framework-seguimientos
---

# Embudos, Tags y Variables — el modelo de datos de Prometheo

> Cómo Prometheo modela el proceso comercial: qué es una Smart Tag, qué es una Variable,
> qué es un Embudo y cómo se decide qué dato va a cada cosa. Es el modelo base sobre el
> que operan las Reglas Diseño de Prometheo by AUREA
> (`03-reglas-diseno-prometheo-by-aurea.md`).

---

## Por qué este archivo

Durante varias versiones se arrastraron enredos sobre cómo guardar el estado del lead.
Quedaron resueltos al validar contra plataforma (implementación AUREA Hub) y al codificar
el caso G&D Developers (caso paradigmático del modelo de tags). La idea central:

> **Prometheo tiene dos entidades base — Smart Tags y Variables. El Embudo no es una
> tercera entidad: es una agrupación ordenada de Smart Tags que ya existen.**

Una etapa de embudo **es** una Smart Tag. No hay "la etapa" por un lado y "la tag" por
otro. Cuando entendés eso, las contradicciones históricas se caen solas.

---

## Las dos entidades base

### Smart Tags

Una **Smart Tag** es una etiqueta que se le asigna a una conversación.

- **Se ve en la lista de Chats** como etiqueta de color. Si una conversación tiene varias
  tags, al hacer hover se ven todas.
- Se crea con un **mini-prompt de asignación** (15-25 palabras) que la IA usa para
  asignarla sola. El prompt define cuándo corresponde.
- Puede **disparar ejecutables**: seguimientos, acciones (apagar/reactivar asistente),
  notificaciones, creación de leads en integraciones.
- Puede usarse para **categorizar visualmente**: un dato que el equipo necesita ver de un
  vistazo en Chats — el rubro/tipología, el estadío del lead. Una variable no se ve en el
  listado.

### Variables

Una **Variable** guarda contexto y estado del lead que **no necesita verse en la lista de
Chats**: prioridad, presupuesto, proyecto de interés, plazo, objetivo de búsqueda, etc.

- Son **consultables y filtrables** desde su propio panel, separado del de Chats.
- Son visualmente **"gratis"**: no ensucian la lista de Chats.
- Cada variable tiene un campo de **prompt opcional**: con prompt, la IA la completa sola;
  sin prompt, es de carga manual.
- Llevan **prefijo `var_`** para distinguirlas rápido en el Excel de carga y en Prometheo.
- Tipos disponibles: ver `restricciones-plataforma-prometheo.md` (restricción 4).

> El panel de filtros de Chats separa físicamente **Etiquetas**, **Variables** y
> **Moderadores** — la arquitectura confirma que son entidades distintas.

---

## El Embudo — agrupación ordenada de tags

El **Embudo** ordena el proceso comercial en **etapas**. No es una entidad nueva: cada
etapa de un embudo **es una Smart Tag** elegida entre las tags ya creadas.

- Al crear un embudo, Prometheo pide **elegir tags existentes** como etapas. Si la tag no
  existe, la etapa no existe.
- Las etapas son **mutuamente excluyentes**: un lead está en una sola etapa por embudo. Al
  avanzar, la tag de la etapa anterior **se reemplaza** por la nueva — no se acumulan.
- Como la etapa es una tag, una etapa **se ve en Chats** y **puede disparar ejecutables**.
  No hay diferencia entre "tag de etapa" y "tag operativa" — es la misma entidad cumpliendo
  un rol dentro del embudo.
- El embudo se crea con un **campo de descripción**. No es decorativo: la IA lo lee para
  decidir cuándo asignar las tags de ese embudo.
- Se pueden tener **varios embudos en paralelo** (típicamente ventas + post-venta).

### Cuándo un embudo se justifica

Un embudo separado se justifica solo cuando **cambia el actor** (el agente IA vs. el
equipo humano) o **cambia la naturaleza del proceso** (calificación vs. transacción vs.
gestión de relación). Si el recorrido es el mismo, es el mismo embudo.

### Qué NO es un embudo — corrección conceptual

Dos errores típicos en diseños iniciales:

- **FAQ no es un embudo.** Es interacción puntual sin estados que persistan. El lead
  pregunta, el agente responde, se cierra. No hay "estado actual de FAQ".
- **Excepciones no es un embudo.** Es un disparador de derivación que manda el lead al
  embudo correcto. No tiene recorrido propio.

Diseños iniciales listaban 4 embudos (Venta, Derivación, FAQ, Excepciones). **El modelo
correcto deja FAQ y Excepciones fuera de los embudos.** Se modelan con tags y variables,
no con embudos.

### Arrancar minimalista

Si un proceso se gestiona 100% manual y por fuera del sistema (típico en B2B), su embudo
arranca con pocas etapas y se expande cuando se valida la dinámica real. **No inventar
estados que el cliente no usa.**

---

## La regla AUREA: una tag por dimensión

> **Un lead puede llevar varias Smart Tags al mismo tiempo, pero solo una por cada
> dimensión.** Una dimensión es una pregunta que se le hace al lead. Cada dimensión
> admite **una sola respuesta a la vez**, así que cada dimensión genera **una sola tag
> visible** en el panel de Chats.

Esta es la regla central de diseño. Reemplaza el viejo "tope de 2 tags fijas" por un
criterio más honesto: la cantidad de tags depende de cuántas dimensiones se definan,
no de un número arbitrario. Lo que sí se mantiene firme: **dentro de una dimensión, las
tags son mutuamente excluyentes** — nunca dos tags del mismo cajón conviven.

### Dimensiones canónicas — el set base

| Dimensión | Pregunta que responde | Valores típicos (mutuamente excluyentes entre sí) |
|---|---|---|
| **Estadío** | ¿En qué etapa del proceso está? | Nuevo Lead, En Conversación, Calificado, Derivado, Cierre… |
| **Tipo de usuario** | ¿Qué clase de contacto es? | Inversor, Cliente final, Inmobiliaria *(o las equivalentes del rubro)* |
| **Prioridad** *(opcional)* | ¿Es prioritario? | Contacto VIP *(solo se asigna si aplica)* |

**Lectura típica de un lead en Chats:**
- Lead estándar: 2 tags visibles → `En Conversación` + `Inversor`
- Lead prioritario: 3 tags visibles → `En Conversación` + `Inversor` + `Contacto VIP`

La dimensión "Prioridad" es **opcional por lead**: si no aplica, simplemente no se asigna
y el lead muestra 2 tags. No es excepción a variable como decía la versión anterior — es
una dimensión legítima del modelo, solo que no todos los leads la tienen activa.

### Por qué este modelo funciona y no superpone

Lo que se quiere evitar es que dos tags compitan por el mismo cajón: un lead **no puede
ser** "Inversor" y "Cliente final" al mismo tiempo, o "Nuevo Lead" y "Calificado" a la
vez. Eso rompe la legibilidad del panel — ¿en qué columna lo cuenta el equipo?

El modelo de dimensiones resuelve esto por diseño: cada dimensión es un cajón, y dentro
del cajón las tags son excluyentes. Tags de **dimensiones distintas** pueden coexistir
sin problema porque no compiten por el mismo cajón.

### Cuándo agregar una dimensión nueva

Las dimensiones del set base (estadío, tipo de usuario, prioridad opcional) son las que
hoy aplican a los rubros activos. Una dimensión nueva se justifica solo si:

1. Responde una pregunta sobre el lead que el equipo necesita ver **sin abrir el chat**.
2. **No se superpone** con ninguna dimensión existente — sus valores no compiten con los
   de otra dimensión por el mismo cajón.
3. Sus valores son mutuamente excluyentes entre sí (si no lo son, el modelo se rompe).

Si la pregunta puede vivir en variable y no necesita verse de un vistazo, no es una
dimensión: es una variable. La regla "ante la duda, variable" sigue siendo el default.

### Sub-reglas operativas — extraídas del caso G&D

- **Las etapas de embudo SON Smart Tags.** Verificado en plataforma.
- **Las etapas de un mismo embudo son mutuamente excluyentes** y se reemplazan al
  avanzar. Esto es la dimensión "estadío" funcionando dentro del embudo.
- **La tag de tipo de usuario se deriva de una variable, no se pide dos veces.** La
  variable captura el dato (ej. `var_objetivo_busqueda`); la tag lo muestra. Misma
  información, dos representaciones.
- **No diseñar tags con alta similitud semántica.** Si dos tags se leen casi igual, el
  equipo las confunde en el panel. Caso real G&D: "Visita a Coordinar" vs "Visita
  Coordinada" se renombró a "Por Coordinar" vs "Visita Agendada".
- **Una tag se crea solo si genera una acción concreta o una distinción visual que el
  equipo necesita ver sin abrir el chat.** Si el detalle puede vivir en variable y nadie
  necesita verlo de un vistazo, va a variable.

---

## El criterio de diseño: tag, variable o etapa de embudo

```
¿Es la posición del lead dentro de un proceso comercial?
   → SÍ  → es una TAG de la dimensión ESTADÍO (= etapa del embudo)
   → NO  → seguir

¿Responde a otra dimensión definida del lead (tipo de usuario, prioridad)?
   → SÍ  → SMART TAG en esa dimensión
   → NO  → seguir

¿Necesita verse en la lista de Chats, o dispara un ejecutable?
   Si la respuesta es SÍ, probablemente conviene definir una dimensión nueva
   para ese dato — siempre que no se superponga con las dimensiones existentes.

¿Es contexto consultable / filtrable del lead?
   → SÍ  → VARIABLE
```

**Regla práctica ante la duda:** si el dato no responde a una dimensión clara del lead
y no necesita verse en Chats, va a variable.

### Por qué pocas tags por lead — el motivo real

Mantener pocas tags visibles **no es una restricción de plataforma** — es higiene visual.
Prometheo no deja elegir qué tags se muestran en Chats: si una conversación tiene varias,
al hacer hover se ven todas. Muchas tags ensucian el listado.

El modelo de dimensiones controla esto naturalmente: cada lead muestra una tag por
dimensión activa, así que el techo lo pone la cantidad de dimensiones definidas, no un
número arbitrario. Hoy son 2 a 3 tags visibles (estadío + tipo de usuario + a veces VIP).
Si en el futuro se justifica una dimensión nueva, el modelo lo soporta sin romperse.

Lo que rompe la legibilidad no es "tener varias tags" — es **tener varias tags del mismo
cajón** o tener tags que no responden a ninguna pregunta clara. El modelo de dimensiones
previene las dos cosas por diseño.

---

## Variables — reglas operativas

- **Prefijo `var_`** obligatorio.
- **El estadío NO va en variable.** Con el modelo "etapa = tag", las viejas variables de
  estado (`proceso_actual`, `estado_venta`, `estado_derivacion`) quedan redundantes y se
  eliminan. El estadío vive en la tag.
- **Variable vs tag — regla de decisión:** si el dato necesita verse de un vistazo en el
  panel para clasificar/agrupar → tag. Si es detalle puntual que se filtra o segmenta →
  variable.
- **Una variable puede gobernar a otras (router):** su valor habilita o bloquea preguntas
  posteriores. Caso real estate: `var_objetivo_busqueda = inversion` permite preguntar
  renta/m²; `uso_propio` no.
- **Variables de handoff:** se llenan solo al derivar (ej. `var_tipo_derivacion`).

---

## Reglas duras del modelo

> Sección extensible. Cada regla dura confirmada se agrega como ítem nuevo, con su
> evidencia.

1. **Una etapa de embudo es una Smart Tag.** No son entidades separadas. *Verificado en
   plataforma — implementación AUREA Hub y G&D Developers.*
2. **Una misma tag no puede ser etapa de dos embudos distintos.** Si un estado equivalente
   aplica a dos procesos, son dos tags con nombres distintos. *Bot oficial + plataforma.*
3. **Las etapas de un mismo embudo son excluyentes** y se reemplazan al avanzar.
4. **Una tag puede cumplir varios roles a la vez** — estadío, tipología, acción,
   visibilidad. Los roles no son excluyentes.
5. **Si la tag no está creada, la etapa no existe.** Las tags se crean antes que los
   embudos (ver `importacion-contactos.md`, orden de carga).
6. **Una tag por dimensión.** Un lead puede llevar varias Smart Tags al mismo tiempo,
   pero solo una por cada dimensión (cada dimensión = una pregunta sobre el lead, con
   valores mutuamente excluyentes entre sí). Dimensiones canónicas hoy: estadío, tipo de
   usuario, prioridad (opcional). Una dimensión nueva se justifica solo si no se
   superpone con las existentes.
7. **FAQ y Excepciones no son embudos.** Se modelan con tags y variables.

---

## Embudos en paralelo

Un cliente puede tener **varios embudos a la vez** (ventas + post-venta). Cada tag-etapa
pertenece a un solo embudo (regla dura 2). Si un estado equivalente se necesita en dos
procesos, son dos tags distintas, una en cada embudo.

> Cuando el agente maneja 2+ embudos, hace falta una **variable router** que defina cuál
> está activo en cada momento — ver Regla 8 en `03-reglas-diseno-prometheo-by-aurea.md`.

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| `03-reglas-diseno-prometheo-by-aurea.md` | Las Reglas Diseño operan sobre este modelo. Las reglas afectadas (1, 3, 6) están al día con este modelo a partir de v1.11. |
| `restricciones-plataforma-prometheo.md` | Las acciones de Smart Tag, los tipos de variable, el prompt opcional y el match de tags son restricciones de plataforma. |
| `importacion-contactos.md` | El orden de carga (variables → tags → embudos → contactos) sale de la regla dura 5. |
| `excel-carga-clientes.md` | El Excel de carga concreto de cada cliente se diseña a partir de este modelo. |
| `framework-seguimientos.md` | Los seguimientos se disparan por tag — incluyendo tags que son estadío. |
| `prometheo-etapa2-design` (skill) | Aplica este modelo en el diseño del CRM de cada cliente. La SECCIÓN 0 de su SKILL.md desarrolla las 3 capas. |

---

## Hallazgos de campo — confirmados en producción (v1.14)

> Comportamientos vistos con clientes reales, ya confirmados como regla dura porque se repitieron
> en más de un caso.

### Corrección de modelo — variable de perfil única + variable hija, reemplaza tags de tipo-usuario

**Lo que cambia:** la dimensión de tipología que en v1.12 vivía como Smart Tag con valores
Inversor/Cliente final/Inmobiliaria se resuelve mejor como **una variable única de selección
única** (mutuamente excluyente por diseño, sin necesidad de la regla de desambiguación de tags),
con el detalle fino en una **variable hija** que se completa solo cuando corresponde.

- **G&D Developers:** `Tipo Perfil` (Inmobiliaria / Vivienda / Inversión) reemplazó a las dos
  variables previas y redundantes `Tipo Contacto` + `Objetivo Búsqueda`. El detalle de la
  inversión vive en `Inversión Finalidad` (Renta / Reventa / Diversificación), hija: se completa
  SOLO si `Tipo Perfil` = Inversión; para Vivienda o Inmobiliaria queda vacía, N/A real. Esto
  evita que "Reventa" viva en dos variables distintas a la vez (la superposición que se corrigió).
- **BETROX:** confirma el patrón como generalizable, no un capricho de un cliente: `Tipo Cliente`
  (Consumidor Final / Profesional / Municipio / Instalador / Cliente Recurrente) + `Tipo
  Profesional` hija (Arquitecto / Decorador / Paisajista / Constructora), que se completa SOLO
  si `Tipo Cliente` = Profesional.

**La tag de tipología no desaparece:** sigue existiendo, pero pasa a ser **pura visibilidad que
espeja la variable** (el dato vive en la variable; la tag es para verlo de un vistazo en el panel),
no la fuente del dato. Esto es coherente con la regla dura de este archivo (una tag por
dimensión) pero afina el rol: cuando existe variable + hija, la tag de esa dimensión es un espejo,
no un dato primario.

**Regla generalizada:** ante un perfil de lead con subcategorías, diseñar variable única
mutuamente excluyente (padre) + variable hija condicional, y solo entonces la tag de tipología
como espejo visible. No usar tags para cargar el detalle fino.

### Contacto VIP — de tag binaria combinable a variable de 4 valores

En v1.11-v1.12, "Contacto VIP" vivía como Smart Tag de prioridad, combinable con la tipología.
BETROX lo llevó a variable de selección única con 4 valores (`Recomendación` / `Referido
directo` / `Cliente conocido` / `No VIP`), porque el registro de *por qué* alguien es VIP importa
para el trato y no cabe en un binario. La tag de prioridad sigue existiendo para visibilidad, pero
el detalle vive en la variable — mismo patrón que Tipo Perfil.

### "Hot Lead" reemplaza la dimensión "Prioridad" ambigua

La vieja dimensión "Prioridad" (combinable con tipología) se descartó por ambigua: no quedaba
claro qué la disparaba. BETROX la reemplaza por una sola tag **Hot Lead**, con criterio binario
explícito y estricto: alta intención de compra E inmediatez (quiere avanzar ya, define producto y
medida, pide cerrar, pone urgencia de tiempo). No se asigna por volumen de compra ni por tipo de
cliente, solo por temperatura. **Regla:** una tag de prioridad necesita un criterio de disparo
binario y verificable: si el criterio no se puede responder con sí/no en una lectura de la
conversación, la tag está mal diseñada (es la falla que tenía "Prioridad").


---

## Doctrina de diseño de CRM (probada en tres cuentas: EDFAN, G&D, BETROX)

> Esta sección junta las decisiones de fondo que hacen bien un diseño de embudos, tags y
> variables. Sale del cruce de los tres diseños reales y es lo que hay que tener a mano al
> arrancar una cuenta nueva. Los moldes concretos por rubro (cuántos embudos, qué tags) están
> en `arquitectura-crm-por-rubro.md`; acá está el criterio que los gobierna.

### La prueba embudo-vs-tag (la primera decisión)

Algo es **embudo** cuando sus estados son **mutuamente excluyentes, ordenados, y el paso de uno
al siguiente es progreso medible**: el lead está en UNO a la vez y avanza en orden. Si los
estados no son ordenados ni excluyentes entre sí, no es embudo: es una dimensión de tag (varias
pueden coexistir) o una variable (un dato que se guarda). Test rápido antes de crear un embudo:
"¿un lead está en exactamente uno de estos estados a la vez, y pasar de uno a otro es avanzar?".
Si no, no es embudo.

### El embudo marca DE QUIÉN es el trabajo, no qué compra el lead

Los tres diseños separan **Recepción/Calificación (la conduce el agente)** de **Venta/Cierre (la
conduce el equipo humano)**. El corte no es por tipo de producto ni por tipo de cliente: es por
quién acciona. Esto permite medir la autonomía real del agente (cuánto cierra solo vs cuánto
necesita humano) y evita que el agente "toque" estados que son de una persona. Un canal cuyo
ciclo de vida es estructuralmente distinto (B2B / profesionales, postventa) va a **embudo
propio**, no a una etapa dentro de otro: cuando el recorrido comercial es propio de punta a
punta, merece embudo.

### El estado del lead vive SOLO en el embudo, nunca duplicado en variable

No se crea una variable "estado" ni una variable router además del estadío del embudo: dos
fuentes del mismo dato se desincronizan. La etapa del embudo (vía su tag de estadío) es la única
fuente de verdad del estado.

### Notificar solo donde hay acción humana

Una tag lleva acción de Notificaciones **solo si, al entrar en ella, alguien del equipo tiene que
hacer algo**. Las tags puramente informativas no notifican. Poner notificación en todas las tags
satura al equipo y le quita señal a las que importan. (Recordatorio de plataforma: Notificaciones
requiere plan Enterprise; ver `restricciones-plataforma-prometheo.md`.)

### Eliminar el estadío que no tiene una acción propia que lo justifique

Si una etapa del embudo no dispara ninguna acción ni notificación propia y no aporta información
que la tag de estadío + el tiempo transcurrido ya no den, se elimina. (G&D sacó "En Seguimiento"
por esto.) Un embudo no es un diario de la conversación: es la secuencia de estados que ameritan
una acción o una medición.

### Test de redundancia entre dos etapas: "¿existe un caso real en A pero no en B?"

Cuando dos etapas parecen pisarse (ej. "Calificado" y "Derivado"), la prueba es: ¿puede un lead
estar en A y todavía no en B? Si hay un caso real en el limbo (calificado pero nadie lo tomó
aún), las dos etapas tienen sentido. Si no hay limbo, una sobra y se colapsa (a veces reemplazada
por una variable de estado, como "Reasignación Moderador"). No se asume: se responde con un caso
concreto.

### Variable por-conversación vs por-lead

Una variable puede vivir en la **conversación** (un mismo lead tiene valores distintos en chats
distintos) o en el **lead** (dato estable del contacto). "Reasignación Moderador" (¿ya entró un
humano a responder?) vive en la conversación, es un flag que solo sube (No→Sí) y no vuelve a
bajar dentro del mismo chat. Definir dónde vive la variable es parte del diseño, no un detalle.

### Selección múltiple solo cuando el dato tiene varios valores reales a la vez

Una variable va en selección múltiple **solo** si un lead legítimamente puede tener varios valores
simultáneos (líneas de producto que consulta, proyectos que menciona, obras en las que ya compró).
Si el dato es uno solo por lead, va en única. No perder información real por elegir un campo más
simple, ni inflar con múltiple lo que es único. (G&D corrigió "Obra Anterior Mencionada" de única
a múltiple por esto.)

### Producto/condición externa nunca como embudo

Una condición que vive en el catálogo (que un producto esté en Outlet, en oferta, sin stock) NO
es una etapa de un proceso: es un atributo de producto que se **consulta en la integración** en
runtime, más, si importa, una **variable de interés del lead** (Outlet Interes). Un lead que
quiere una pieza en oferta recorre el mismo embudo de siempre. (BETROX había modelado Outlet como
embudo: era un error.)

### Variables de fecha por modalidad cuando el mensaje cambia

Cuando una fecha dispara un recordatorio cuyo texto cambia radicalmente según la modalidad
(dirección física vs link de videollamada), conviene **una variable de fecha por modalidad**
(Reunión Física - Fecha/Hora, Reunión Virtual - Fecha/Hora) en vez de una fecha + una variable de
modalidad, para no tener que cruzar dos condiciones en el recordatorio. Y, sin integración de
calendario, el agente **no agenda: transcribe** a la variable lo que el vendedor humano ya acordó.

### La extracción vive en la plataforma; el prompt solo refuerza (dos niveles)

Cada variable tiene su prompt de extracción cargado en Prometheo, que la nutre sola. El prompt del
agente NO re-explica cómo se llena cada variable (duplicar lógica en dos lugares los
desincroniza): lleva un refuerzo de dos niveles: una línea paraguas ("registrás lo relevante que
surja") + una línea que prioriza solo las **señales blandas fáciles de perder** (objeción, dolor,
disparador, pedido fuera de catálogo, VIP, descarte). Las señales duras (zona, tipología,
presupuesto) se extraen solas y no se refuerzan. Regla: si el refuerzo nombra todo, no prioriza
nada.

### El tipo de variable tiene que representar el dato

Un dato abierto e infinito no entra en un enum cerrado por más refuerzo que tenga el prompt (caso
"Pedido Fuera de Catálogo" cargado como Opciones cuando pretende capturar el pedido literal: no
nutre). Antes de dar una variable por buena: ¿el tipo (Opciones / Texto / Texto largo) representa
de verdad el dato? Es config de plataforma, no se arregla desde el prompt.
