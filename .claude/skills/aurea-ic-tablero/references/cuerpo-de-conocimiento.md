# Inteligencia Comercial de AUREA · Cuerpo de conocimiento

Documento de traspaso. Sirve para dos cosas:

1. **Que alguien de afuera entienda el producto sin leer el código ni las conversaciones previas.**
2. **Mapear qué conocimiento necesita tener integrado el equipo** para seguir evolucionando el producto y el servicio.

Está escrito pensando en que lo lea una **especialista en performance marketing** que va a corregir y evolucionar el producto. Por eso separa de forma explícita lo que ya sabemos hacer de lo que no, y termina con preguntas concretas para ella.

**Fecha:** septiembre 2026 · **Caso de referencia con datos reales:** EDFAN Real Estate (1.017 contactos, julio a septiembre 2026).

---

## 1. Qué es el producto

Un **tablero de Inteligencia Comercial**: un HTML autocontenido, con la marca de AUREA, que se le entrega al cliente cada quincena o mes y responde cinco preguntas en este orden.

1. ¿Cómo venimos? (panorama y evolución)
2. ¿Qué pide el mercado? (demanda)
3. ¿Qué trajo resultado? (campañas y anuncios)
4. ¿Qué hago ahora? (decisiones con dueño)
5. ¿De dónde sale esto? (fuentes y última actualización)

La arquitectura se ordena **por pregunta, no por canal**. Una pestaña por plataforma obliga a agregar una pestaña cada vez que entra un canal nuevo, y el cliente termina navegando el organigrama de las herramientas en vez de su negocio. El canal es un filtro transversal, no una sección.

### La propuesta de valor, en una línea

> **Meta ve hasta el clic. Prometheo ve del clic a la venta. El cruce por ID de anuncio es el producto.**

Esa frase hay que explicarla dentro del tablero, no darla por supuesta. Es lo único que una agencia de medios no puede replicar con el Ads Manager.

### De dónde sale el dato

| Fuente | Manda en | No manda en | Estado |
|---|---|---|---|
| **Prometheo** (CRM con agente de IA sobre WhatsApp e Instagram) | Conteo de consultas, tags, calificación, texto de la conversación | Gasto, alcance | Activa |
| **Meta** | Gasto, alcance, impresiones, clics | Cuántas consultas reales hubo | Prevista, **falta conectar** |
| **Tokko** (catálogo inmobiliario) | Producto: proyectos, unidades, precios, estado de obra | Intención del lead | Activa en real estate |
| **Cálculo** | Ratios y costos derivados | Nada primario | - |

Previstas: Google Ads, LinkedIn. Verticales donde ya corre: desarrollista inmobiliario, mobiliario, insumos de construcción, inmobiliaria tradicional.

---

## 2. El activo diferencial: dato conversacional de primera mano

Esto es lo que conviene entender antes que nada, porque cambia qué tipo de análisis es posible.

**Cada lead tiene una conversación completa de WhatsApp, y un agente de IA la convierte en variables estructuradas.** No es un formulario de tres campos: es una charla de 8 mensajes promedio de la que salen zona de interés, tipo de unidad, perfil (vivienda o inversión), forma de pago, objeción declarada, horizonte de compra y el texto literal.

Consecuencia práctica para performance: **podemos medir la calidad de un anuncio, no solo su volumen.** Un anuncio puede traer 320 consultas y otro 75, pero también podemos decir que el primero califica al 49% y el segundo al 25%, con la misma definición de "calificado" para los dos. Las plataformas de medios no ven eso, porque su conversión termina en el clic o en el mensaje iniciado.

Contracara honesta: **es dato declarado en una conversación, con cobertura desigual.** Zona al 51%, perfil al 26%, objeción al 10%. Por eso existe la capa de curaduría que viene abajo. Sin ella, ese activo se convierte en porcentajes sobre bases a medio llenar, que es peor que no tener nada.

---

## 3. Las cinco capas de conocimiento

El producto se apoya en cinco cuerpos de saber distintos. Están escritos como skills en el repositorio (`.claude/skills/`) y en la metodología de consultoría. Esta sección es el resumen de cada uno y **dónde está el gap**.

| Capa | Qué resuelve | Dónde vive | Cómo estamos |
|---|---|---|---|
| 1. Modelo de datos | Cómo se diseña el CRM para que después se pueda medir | `aurea-metodologia` | Fuerte |
| 2. Curaduría del dato | Qué número se muestra, sobre qué base, con qué confianza | `aurea-curaduria-dato` | Fuerte, es nuestro aporte original |
| 3. Atribución y medición | Qué causó cada venta; reconciliar fuentes que se contradicen | `attribution` (vendorizada) | **Débil en la práctica** |
| 4. RevOps | Ciclo de vida del lead, etapas, scoring, handoff, higiene | `revops` (vendorizada) | Media |
| 5. Diseño de tablero | Cómo se ve y cómo se opera | `aurea-dashboard-design` + `interface-design` | Fuerte |

---

### Capa 1 · Modelo de datos: el CRM es la base de datos

Nadie puede reportar lo que el CRM no registró. Esta capa es aguas arriba de todo lo demás.

**Los principios que usamos:**

- **Una etapa de embudo ES una Smart Tag.** No son dos conceptos distintos.
- **Una tag por dimensión.** Los valores dentro de una dimensión son excluyentes. "Inversor" y "Uso Propio" son dos valores de "tipo de usuario": un contacto no puede tener los dos.
- **El embudo marca de quién es el trabajo, no qué compra el lead.** Se separa el tramo que conduce el agente (recepción, conversación, calificación) del tramo que conduce el equipo humano (visita, negociación, reserva). Es el corte más útil que tenemos para diagnosticar.
- **Variable padre + variable hija condicional.** `Inversión Finalidad` solo se llena si `Tipo Perfil = Inversión`. Leerla sobre el total es un error de lectura, no un faltante de carga.
- **La tag de tipología es espejo de la variable, no fuente del dato.**
- **La extracción vive en la plataforma; el prompt del agente solo refuerza.** Dos niveles. Y si el refuerzo nombra todo, no prioriza nada.
- **Eliminar el estadío que no tiene una acción propia que lo justifique.**
- **Un canal con ciclo de vida estructuralmente distinto necesita embudo propio** (por ejemplo, el B2B con inmobiliarias no es el embudo del consumidor final).

**Por qué le importa a performance:** si el equipo del cliente no marca la reserva, no hay tasa de conversión posible, no importa cuánto presupuesto de medios haya. En EDFAN, el embudo del agente funciona al 64% y el humano al 2%. Eso no se arregla con pauta.

---

### Capa 2 · Curaduría del dato: qué se puede afirmar

Es la capa que cruzamos y reescribimos nosotros a partir de `attribution` y `revops`. Es lo más original que tenemos y lo que hay que defender en cualquier evolución del producto.

**La regla de oro: ningún número sin procedencia.** Todo número carga cuatro cosas, y si no se pueden responder, no se muestra.

| | Qué es | Ejemplo real |
|---|---|---|
| **Base** | El denominador real | 518 que declaran zona, no 1.017 |
| **Cobertura** | % del total con esa variable cargada | Zona 51%, perfil 26%, reuniones 0% |
| **Origen** | Declarado por el lead / inferido por el agente / calculado / de plataforma | - |
| **Confianza** | Alta, media o baja, según cobertura + origen | Anuncio: 64% y de plataforma, media-alta |

El **origen** importa tanto como la cobertura. Un campo al 90% inferido por el agente es más frágil que uno al 60% declarado por el lead con sus palabras.

#### La escalera de evidencia

Es nuestro aporte propio: portar la regla de RevOps "un deal no avanza de etapa sin los campos requeridos" al reporte, como "**un dato no asciende a titular sin cobertura**".

| Nivel | Cobertura | Qué puede hacer | Qué no puede hacer |
|---|---|---|---|
| **Hecho** | ≥ 80% | Titular, KPI grande, encabezar un insight | - |
| **Señal** | 40 a 79% | Card con denominador explícito | Titular sin decir la base |
| **Indicio** | 10 a 39% | Bullet, tabla o modo Avanzada | Card propia, porcentaje protagonista |
| **No reportable** | < 10% | Va a "Calidad de datos" como hallazgo | Aparecer como dato de demanda o venta |

Tres reglas que la acompañan:

- **Un Indicio nunca titula.** Si la variable está al 10%, el hallazgo real no es el ranking de valores: es que está al 10%.
- **Un dato sube de nivel cambiando la base, no maquillando el número.** Objeción al 10% del total es Indicio; sobre "los que declararon objeción" es una Señal legítima, siempre que se diga.
- **No reportable no es invisible.** Cambia de pestaña: deja de ser dato y pasa a ser hallazgo de calidad, con el insight que desbloquearía si se completara.

#### Denominador honesto (doble lectura)

Siempre que la cobertura sea menor al 80%, se reportan dos lecturas:

> Villa Crespo: **283 consultas**, 28% del total, **55% de las 518 que declaran zona**.

La primera dimensiona, la segunda lee el mercado. Nunca una sola. Y nunca normalizar un multi-select a 100%: si un lead puede declarar dos zonas, se dice, no se fuerza la suma.

#### El faltante es un hallazgo

"Direct" no es un canal, es un problema de medición. Igual acá. Se nombra, se dimensiona, se dibuja, y se clasifica en tres tipos porque se arreglan distinto:

1. **Estructural** (el dato no existe de origen: boca a boca, dark social) → se resuelve preguntando.
2. **De proceso** (nadie lo completó) → se resuelve con prompt y con campos requeridos por etapa.
3. **De integración** (la fuente no está conectada: gasto de Meta) → se resuelve conectando.

#### Etapa declarada vs etapa por evidencia

La curaduría que más valor generó. Se define cada etapa con su evidencia requerida y se cuenta **dos veces**: cuántos tienen el tag y cuántos cumplen la evidencia. La brecha es el hallazgo.

| EDFAN | Tag declarado | Cumple evidencia |
|---|---:|---:|
| Calificado | 6 | 386 |

No hay 6 calificados: hay **381 leads calificados de hecho que nadie marcó**. El embudo no está vacío, está subregistrado.

#### Base curada

Antes de cualquier porcentaje, definir sobre quién se habla. El export trae todo junto y un proveedor que ofrece premarcos no es demanda de compra.

```
1.017  contactos en el export
 -117  no-demanda (inmobiliarias 55, proveedores 41, no fit 28, desarrolladores 4)
=  900  demanda de compra
 -187  nunca respondieron
=  713  demanda real que conversó
```

Efecto medible: el ratio de calificación pasa de 38% a **41%**. Cada pestaña declara sobre qué base corre.

#### Lo cualitativo audita a lo cuantitativo

El texto libre es el chequeo fuera de modelo, no es relleno.

- **La cita textual vale más que la paráfrasis.** "Por el momento no estaría dentro de mi presupuesto" es evidencia; "objeción de precio" es una categoría.
- **No codificar a porcentaje con n chico.** Cuatro citas no son un 4%.
- **Buscar la contradicción.** Si "Ubicación" figura 9 veces como objeción pero 20 conversaciones dicen "es muy lejos", la variable está subcargada, no el problema.

#### Reglas de fuentes

- **Nunca sumar entre fuentes.** Si Meta reclama 50 y Prometheo registra 40, hay 40 consultas con dos relatos, no 90.
- **Un solo conteo maestro.** Prometheo define cuántas consultas hubo; el resto explica de dónde vinieron.
- **Leer acuerdo direccional**, no coincidencia exacta.

#### Los anti-patrones que ya nos pasaron

- **El porcentaje huérfano.** "28%" sin decir de qué.
- **El promedio sobre relleno.** Promediar un campo donde el vacío se guardó como `0`.
- **El embudo optimista.** Reportar conversión con la etapa subregistrada.
- **La cita disfrazada de dato.** Tres frases convertidas en categoría con barra.
- **El faltante borrado.** Sacar del gráfico lo que no tiene dato y dejar que el resto sume 100%.
- **Dos criterios de cohorte en la misma pantalla.** Nos pasó: las cards de anuncios contaban por coincidencia parcial (329 / 147 / 92 / 80) y la barra de reparto por coincidencia exacta (320 / 142 / 88 / 75). Se detecta cotejando cifra por cifra contra la fuente.

---

### Capa 3 · Atribución y medición: acá está el gap principal

Esta es la capa donde más necesitamos a alguien de performance. El marco teórico lo tenemos vendorizado; la práctica está sin construir.

**Lo que el marco dice y ya aplicamos:**

- **La atribución es direccional, no verdad.** Es un modelo de causalidad sobre datos incompletos. Es una pista fuerte, nunca un veredicto.
- **Todo modelo es una opinión.** First-touch dice que el primer aviso se lleva el crédito; last-touch, que lo hace el último clic. Los dos están mal en direcciones opuestas.
- **La brecha de atribución es normal.** La suma de lo que reclaman los canales casi siempre supera las conversiones reales, porque cada plataforma se adjudica la misma venta. El trabajo es achicar y explicar la brecha, no hacer que cierre.
- **Cuando "directo" y "búsqueda de marca" dominan, el tope del embudo está funcionando y la atribución lo está escondiendo.** Es el error de lectura más común del rubro.

**Los seis modelos y cómo miente cada uno** (resumen, el detalle está en la skill): first-touch sobre-acredita awareness; last-touch sobre-acredita el fondo del embudo y la marca; last non-direct solo mueve el punto ciego; linear trata una visita suelta igual que una demo; time-decay subestima el tope; position-based usa un 40/40/20 arbitrario; data-driven es una caja negra que necesita volumen.

**Los tres paradigmas de medición:** MTA (stitchear toques a nivel usuario), MMM (regresión top-down de inversión contra resultados, necesita 2 a 3 años de datos semanales y variación real de presupuesto) e incrementalidad (experimento controlado con grupo retenido, el estándar de oro y el desempate cuando dos canales reclaman la misma conversión).

#### Dónde estamos parados de verdad

| Práctica | Estado | Nota |
|---|---|---|
| Atribución por ID de anuncio desde Prometheo | **Hecho** | 64% de cobertura en EDFAN |
| Calidad por anuncio (respuesta, identificación, calificación, derivación) | **Hecho** | Es nuestra ventaja |
| Los "sin dato" nombrados como punto ciego estructural | **Hecho** | 366 consultas, 36% |
| First-touch vs last-touch en paralelo | **No** | Hoy hay un solo toque registrado, el del anuncio de entrada |
| Atribución self-reported ("¿cómo nos conociste?") | **No** | El agente no lo pregunta. Es la corrección más barata que tenemos disponible |
| Gasto conectado, CPL, CPA, ROAS | **No** | Bloqueado por el export de Meta |
| Métricas de plataforma (CTR, CPC, CPM, frecuencia, alcance) | **No** | Mismo bloqueo |
| Cruce por UTM propio | **No** | No tenemos capa de tracking propia |
| Reconciliación entre plataformas | **No** | Con una sola plataforma conectada todavía no aplica |
| Incrementalidad, geo-holdout, MMM | **No** | Fuera de alcance por ahora, pero define el techo del producto |
| Ciclo cerrado hasta la venta | **No** | Bloqueado por el registro del cliente, no por nosotros |

#### Las métricas que hoy podemos calcular y las que no

**Se pueden, con lo que ya tenemos:**

- Consultas totales y por anuncio
- % con anuncio identificado
- Tasa de respuesta por anuncio
- Tasa de identificación (dejó zona o tipología)
- Tasa de calificación por anuncio, con definición consistente
- Mensajes promedio por contacto
- Tasa de derivación y motivo
- Distribución de demanda por zona, tipología, perfil, forma de pago
- Objeción declarada y su base
- Brecha entre etapa declarada y etapa por evidencia

**No se pueden, y por qué:**

| Métrica | Bloqueada por |
|---|---|
| CPL, costo por consulta calificada, CAC | Falta el gasto de Meta |
| ROAS, LTV:CAC | Falta gasto **y** falta valor de operación cerrada |
| CTR, CPC, CPM, frecuencia, alcance | Falta el export de plataforma |
| Conversión lead → visita → reserva | El equipo del cliente no marca esas etapas (2% de uso) |
| Tiempo a conversión por canal | Depende de lo anterior |
| Win rate por anuncio | Depende de lo anterior |
| Cohortes por mes de entrada | Se puede construir, no está hecho |

**Lo que esto implica:** hoy el tablero mide **calidad** de cada anuncio muy bien y **eficiencia** nada. Cerrar eso es el salto de producto más grande disponible, y depende de dos inputs que no controlamos: el export de Meta y el registro del cierre.

---

### Capa 4 · RevOps: el ciclo de vida del lead

El marco viene de B2B SaaS y hay que traducirlo, pero la estructura se reusa entera.

- **Definir antes de automatizar.** Cada etapa lleva criterio de entrada, criterio de salida y dueño.
- **Un lead calificado necesita fit y engagement.** Ninguno de los dos alcanza solo. Una empresa perfecta que nunca interactúa no es un MQL; un estudiante que baja todos los ebooks tampoco.
- **Tiene que existir señal negativa,** o pasa cualquiera.
- **Bloquear el avance de etapa si faltan los campos requeridos.** Es la regla que portamos al reporte como escalera de evidencia.
- **Medir cada handoff.** Speed-to-lead, tasa de aceptación, motivo de rechazo.
- **La higiene es un ritual, no un arreglo único.** Auditoría trimestral: duplicados, contactos sin actividad en 12 meses, distribución de etapas buscando cuellos de botella.

**Traducción al rubro:** el fit de un SaaS (tamaño de empresa, cargo, stack) se reemplaza por proyecto, zona, tipología, perfil inversor vs vivienda, forma de pago y horizonte. El engagement se lee como respuesta, profundidad de conversación y visita agendada.

**Gap:** no tenemos scoring de leads implementado en ningún cliente. Hoy la calificación es binaria por tag. Un score de 0 a 100 con fit y engagement separados es evolución natural y no está hecho.

---

### Capa 5 · Diseño del tablero

**Lo que es fijo (branding, no se negocia):** paleta violeta `#7C5CBF`, azul `#5B8FD9`, rosa `#C77AA8`; tipografías Arimo para texto y datos, Newsreader itálica como acento; logo y esfera iridiscente. Todo lo demás está abierto.

**La doctrina Básico / Avanzado.** Son dos profundidades, no dos vocabularios.

1. **Un número, un nombre.** Nunca renombrar una métrica entre modos. Si un término no se entiende, se explica en tooltip, no se traduce. Renombrar rompe el idioma común con el cliente en la reunión.
2. **El glosario vive en los dos modos.** Quien menos sabe es quien más lo necesita.
3. **Avanzado agrega, nunca reemplaza.**
4. **El switch actúa en todas las vistas.** Si una sección se ve igual en los dos modos, el control enseña que es decorativo y el cliente deja de usarlo.

**Especificaciones que ya son ley:**

- **KPI**: superficie neutra, cifra en `tabular-nums`, **delta obligatorio** contra el período anterior. El color aparece solo en el delta y solo como semántica. Cuatro KPI con cuatro colores distintos es decoración, no información.
- **Embudo**: nunca a escala lineal. Un embudo comercial va de cientos de miles de impresiones a unidades de venta, cinco órdenes de magnitud, y una barra proporcional deja los últimos pasos invisibles. Se dibuja como pasos, con **la tasa de conversión entre pasos como cifra protagonista** y el absoluto en segundo plano.
- **Series**: toda línea lleva escala, mínimo y máximo rotulados, punto final marcado y delta explícito. Una línea que sube sin referencia puede ser +3% o +300%.
- **Tablas**: `tabular-nums`, scroll horizontal propio, y **la fuente del dato en el encabezado** cuando hay cruce de plataformas.
- **Color semántico** (bueno / atención / crítico) definido aparte del acento de marca. El violeta-azul-rosa es identidad, no estado.
- **Obligatorios**: modo oscuro con tokens, estados vacíos diseñados ("sin datos suficientes en este período" es una vista, no un hueco), y fecha de última actualización por fuente.

**Cómo se renderiza la curaduría:** chip de cobertura en el encabezado de cada card (`base declarada: 518`), barra de faltante explícita en ámbar cuando supera el 15%, tag de nivel cuando no es Hecho (`Señal`, `Indicio`), doble lectura en el valor, y citas en tarjetas de texto sin barra ni porcentaje.

**Restricción técnica aprendida a los golpes:** el archivo se entrega como HTML autocontenido y **el peso importa**. Los visores truncan archivos grandes y las últimas pestañas quedan en blanco sin avisar. Los assets van en WebP al tamaño real de uso. Referencia: los tableros pasaron de 1,1 MB a menos de 250 KB sin perder nitidez.

---

## 4. El caso de referencia: qué encontró el método en EDFAN

Sirve como prueba de que el marco produce hallazgos, no solo prolijidad. Todo esto salió de un export real, sin gasto de medios.

- **El embudo está subregistrado, no vacío.** Tag "Calificado": 6. Cumplen la evidencia: 386. Hay 381 leads calientes que nadie marcó.
- **Hay dos embudos y solo uno funciona.** El del agente al 64% (653 contactos), el humano al 2% (21). El diagnóstico no es "falta pauta", es "falta carga en el tramo de cierre".
- **La fuga más cara está después de calificar, no antes.** De 386 calificados, 96 tienen seguimiento. Se enfrían 290 leads que ya dijeron qué querían. No requiere dato nuevo ni pauta nueva para recuperarlos.
- **La atribución predice calidad, no solo volumen.** Las cohortes con anuncio responden entre 90% y 95% y califican entre 44% y 49%. La cohorte sin anuncio identificado responde 61% y califica 26%. Atribuir bien mejora la calidad promedio, no solo el reporte.
- **El 36% sin atribución tapa el ROI.** 366 consultas que no se pueden asignar a ninguna campaña.
- **Dos errores de lectura propios los encontró el método, no el ojo.** Un criterio de cohorte inconsistente entre dos secciones, y una variable hija leída sobre el total (3%) en vez de sobre su base condicional (51%).

---

## 5. Qué necesitamos de una especialista en performance marketing

Ordenado por lo que más mueve la aguja.

### 5.1 Cerrar la capa de eficiencia

Hoy medimos calidad y no medimos plata. Necesitamos definir, con criterio profesional:

- Qué export de Meta pedimos exactamente y con qué desglose (campaña, conjunto, anuncio, día).
- Cómo se cruza el gasto contra las consultas de Prometheo sin caer en sumar fuentes.
- Qué ventana de atribución adoptamos como estándar de la casa y por qué.
- Cómo se reporta la brecha entre lo que reclama Meta y lo que registra Prometheo, sin falsa reconciliación.
- Qué métricas de plataforma entran al tablero y en qué modo (Básico o Avanzada).

### 5.2 Diseñar la pregunta de atribución auto-reportada

Es la corrección más barata disponible y hoy no existe. El agente de IA ya conversa con todos los leads: puede preguntar "¿cómo nos conociste?" con una lista de opciones más un campo libre.

Decisiones que necesitamos de alguien con criterio: en qué momento de la charla preguntar sin romper la conversión, cómo redactarla para capturar dark social sin sesgar, y cómo se usa después como desempate contra el tracking.

### 5.3 Definir el estándar de medición por tamaño de cuenta

Nuestros clientes son PyMEs con presupuestos chicos. Necesitamos una regla de la casa sobre qué corresponde a cada escala: cuándo alcanza con buenas UTM más last non-direct más encuesta auto-reportada, cuándo tiene sentido un test de incrementalidad, y a partir de qué volumen el tablero puede mostrar tendencias sin que sean ruido.

### 5.4 Auditar los tableros existentes con ojo de performance

Hay cuatro construidos: EDFAN, DRAKON, PAVIR, TKVA. Las preguntas que queremos que nos haga:

- ¿Qué métrica falta que una especialista buscaría primero y no encuentra?
- ¿Qué está mostrado de una forma que induce a una decisión equivocada?
- ¿Qué benchmark del rubro deberíamos poder poner al lado de cada número?

### 5.5 Definir el scoring de leads

Fit y engagement separados, con señal negativa, adaptado a real estate primero. Hoy la calificación es binaria por tag.

### 5.6 El caso de negocio del ciclo cerrado

El bloqueo más grande no es técnico, es de proceso: el cliente no marca la reserva. Necesitamos el argumento comercial afilado de por qué registrar el cierre le conviene **a él**, no a nosotros. Una especialista que haya peleado esa conversación en agencias lo va a decir mejor.

---

## 6. Vocabulario común

Para que una reunión no se trabe en definiciones.

| Término | En AUREA significa |
|---|---|
| **Consulta** | Un contacto que escribió por WhatsApp o Instagram y quedó registrado en Prometheo. Es el conteo maestro. |
| **Base curada** | El subconjunto sobre el que corre un porcentaje, después de sacar la no-demanda. |
| **Base declarada** | Cuántos contactos tienen cargada la variable de la que se está hablando. |
| **Cobertura** | Base declarada sobre base total. |
| **Escalera de evidencia** | Hecho ≥80%, Señal 40-79%, Indicio 10-39%, No reportable <10%. Decide qué puede hacer cada dato. |
| **Etapa por evidencia** | Contar los que cumplen los campos requeridos de una etapa, tengan o no el tag. |
| **Embudo del agente** | Tramo que conduce la IA: recepción, conversación, calificación, derivación. |
| **Embudo humano** | Tramo que conduce el equipo del cliente: visita, negociación, reserva, cierre. |
| **Doble lectura** | Reportar un número sobre el total y sobre la base declarada, siempre los dos. |
| **Faltante estructural / de proceso / de integración** | Los tres tipos de dato ausente, que se arreglan distinto. |
| **Variable hija** | Variable condicional que solo se llena si la padre tiene cierto valor. Se lee sobre su base condicional. |
| **Modo Básico / Avanzada** | Dos profundidades del mismo tablero, nunca dos vocabularios. |

---

## 7. Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Curaduría del dato (nuestra) | `.claude/skills/aurea-curaduria-dato/SKILL.md` |
| Atribución (marco de origen) | `.claude/skills/attribution/SKILL.md` |
| RevOps (marco de origen) | `.claude/skills/revops/SKILL.md` |
| Diseño de tablero | skill `aurea-dashboard-design` |
| Metodología de CRM | skill `aurea-metodologia` (router por estadío, rubro, integración y transversales) |
| Spec de cambios de CRM, caso EDFAN | `EDFAN_Spec_CRM_Prometheo.md` |
| Tableros construidos | `EDFAN`, `DRAKON`, `PAVIR`, `TKVA` `_Inteligencia_Comercial.html` |

**Créditos:** las capas de atribución y RevOps derivan de dos skills comunitarias de Corey Haines (licencia MIT), vendorizadas sin modificar en `.claude/skills/`. La capa de curaduría es cruce y reescritura propia de AUREA: la escalera de evidencia, el denominador honesto, la base curada y el cruce etapa vs evidencia son aporte nuestro.

---

## 8. La síntesis para la especialista

- **Lo que tenemos y casi nadie tiene:** una conversación completa por lead, estructurada en variables, que permite medir la **calidad** de cada anuncio y no solo su volumen.
- **Lo que no tenemos:** el gasto. Sin él no hay CPL, ni CAC, ni ROAS, ni decisión de presupuesto.
- **Lo que nos bloquea de verdad:** que el cliente no registra el cierre. Sin eso no hay ciclo cerrado, y sin ciclo cerrado la atribución nunca llega hasta la plata.
- **La disciplina que no queremos perder al crecer:** ningún número sin base, sin cobertura, sin origen y sin confianza. Es lo que hace que el tablero se pueda defender en una reunión.

