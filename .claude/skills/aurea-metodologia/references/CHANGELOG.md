# CHANGELOG — Metodología AUREA Hub × Prometheo

> Registro de cambios del ZIP de metodología. Cada versión anota qué se agregó, cambió o
> sacó. Para cómo incorporar cambios, ver `01-metodologia/protocolo-extension-metodologia.md`.

---

## v1.19 - 16 septiembre 2026

Conversión de la metodología a Skill nativo de Claude, sin tocar la doctrina. Es reenvase,
no reescritura: el contenido de los archivos queda exactamente igual, cambia solo el
empaque para que la metodología se dispare y se consulte como un skill en vez de leerse
como un ZIP.

**Nuevo - empaque como Skill (`.claude/skills/aurea-metodologia/`)**
- `SKILL.md` nuevo, que hace de router: reproduce la lógica de los cuatro ejes de
  `01-metodologia/00-CONSULTA.md` (proceso / rubro / integración / transversal), los modos
  nueva vs trayectoria, y las tablas de despacho, apuntando a cada recurso bajo demanda. No
  duplica doctrina: solo rutea. Su `description` hace que el skill se dispare en las tareas
  típicas (diseñar CRM, corregir o auditar prompt, guión de testing, seguimientos,
  integración Tokko/Sheets/PrestaShop, entregable de cliente).
- Todos los `.md` de la metodología quedan como recursos de referencia bajo `references/`,
  sin modificar, con su estructura de carpetas intacta para que los enlaces internos entre
  archivos sigan resolviendo. Se leen bajo demanda; no se cargan todos de entrada.

**Sin cambios de doctrina**
- Ningún archivo de metodología se editó. `00-CONSULTA.md`, `00-INDEX.md`, `README.md` y
  todo el contenido siguen siendo la fuente de verdad; el `SKILL.md` es una capa de acceso
  por encima, no un reemplazo.

**Cómo se mantiene de acá en adelante**
- La mejora continua se hace editando el recurso que corresponde bajo `references/` y
  versionando el skill (nueva entrada en este CHANGELOG), no reempacando un ZIP. El criterio
  de promoción no cambia: una lógica sube a transversal solo cuando la confirma un segundo
  rubro distinto (ver `logica-comercial-transversal.md` y `principios-transversales-agente.md`).

## v1.18 — 8 septiembre 2026

Integra la experiencia de diseño de CRM de tres cuentas (EDFAN, G&D, BETROX) como doctrina, para
resolver el problema de que el modelo se equivocaba al construir embudos, variables y tags de
cuentas nuevas: le faltaba la experiencia real cargada. Y documenta Inteligencia Comercial como
producto. Todo aditivo; nada obliga a romper lo vigente.

**Diseño de CRM como doctrina (`embudos-y-tags.md`)**
- Sección nueva con las decisiones de fondo probadas en las tres cuentas: la prueba embudo-vs-tag
  (estados excluyentes+ordenados+progreso medible), el embudo marca de quién es el trabajo (agente
  vs equipo) no qué compra el lead, el estado vive solo en el embudo, notificar solo donde hay
  acción humana, eliminar estadío sin acción propia, el test de redundancia "¿existe un caso en A
  pero no en B?", variable por-conversación vs por-lead, selección múltiple solo con varios valores
  reales, producto/condición externa nunca como embudo, variables de fecha por modalidad, refuerzo
  de dos niveles, y el tipo de variable tiene que representar el dato.

**Moldes de arquitectura por rubro (`arquitectura-crm-por-rubro.md`, nuevo)**
- El esqueleto reutilizable: desarrollista (3 embudos: IA / venta / B2B inmobiliarias) y
  mobiliario (4 embudos: Recepción / Venta / B2B / Postventa), con sus dimensiones de tags y
  variables típicas. Marcado patrón (sube) vs instancia (queda en la cuenta), y qué se mantiene y
  qué cambia entre rubros. Es el molde para calcar al arrancar una cuenta nueva.

**Guía de Implementador formalizada (`06-estructura-guia-implementador.md`)**
- Estructura canónica de 8 secciones (setup, variables, tags, embudos, mensajería/import,
  distribución, testing, pendientes ITESA), tomada de las tres guías reales. Es la familia 7 de
  outputs; la estructura sube a la metodología, el contenido de cada cuenta queda en su material.

**Inteligencia Comercial como producto (`inteligencia-comercial-producto.md`, nuevo)**
- Qué es (dashboard sobre el export de Prometheo, el puente entre campañas y ventas), qué NO es
  (no es Mejora Continua, no es obligatorio, es producto aparte de los servicios). Corre sobre el
  export (Tags + Variables pobladas) de cualquier cuenta; dashboard de 6 paneles (Panorama,
  Campañas, Meta, Audiencias, Señales, Tendencia); requiere WhatsApp API + Enterprise. Viabilidad
  validada por el desarrollista contra export real (TKVA); caso de referencia DRAKON. Engancha con
  las 6 variables de IC (captura). Nota en `00-OUTPUTS-POR-ETAPA.md` para no confundirlo con las
  familias de output ni con Mejora Continua.

## v1.17 — 8 septiembre 2026

Rebalanceo de la lógica comercial con el criterio de promoción corregido, integración de la
doctrina PrestaShop, y un principio transversal nuevo. El cambio conceptual de fondo: **una lógica
sube a transversal solo cuando un SEGUNDO RUBRO la confirma, no un segundo cliente del mismo
rubro.** EDFAN + G&D son los dos desarrollistas: prueban robustez de rubro, no transversalidad.

**Rebalanceo — lógica comercial a tres niveles**
- `logica-comercial-transversal.md` se reduce de ~30 a **13 transversales reales** (probados en
  desarrollista Y mobiliario), con la regla de promoción escrita al inicio.
- `06-rubros/01-real-estate.md` gana una sección de **lógica comercial del rubro desarrollista**
  (nivel 2, probada en EDFAN y G&D pero no en otro rubro): responder el eje antes de calificar,
  financiación con enganche, objeción de precio por valor, objeción de confianza por
  trayectoria+estructura, material como salida comercial, canal B2B, reconocer recurrente, etc.
  Más los candidatos de un solo cliente (doble salida, CTA que se amolda, palanca de financiación,
  decir de frente lo que no se ofrece).
- `06-rubros/02-mobiliario.md` gana los candidatos de BETROX (presentar producto en 4 partes,
  cross-sell por correspondencia, línea con reglas propias, público/privado, a medida como
  diferencial), marcados "candidato a subir".

**Nuevo — principio transversal 17 (de 16 a 17)**
- `principios-transversales-agente.md`: un archivo nunca reemplaza la respuesta; el primer mensaje
  va completo (saludo + contexto + explicación) aunque lleve adjunto. Bisagra entre el Patrón 4
  (apertura que se saltea) y la regla de oro de PrestaShop (el archivo complementa, nunca
  reemplaza). Probado en los dos rubros.

**Ampliado — doctrina PrestaShop y método de integración (`08-reglas-integracion-catalogo.md`)**
- PrestaShop: qué devuelve, destacados no consultables en vivo, orden de imágenes no controlable,
  y el caso del adjunto que pisaba el texto (resuelto por Prometheo, con la mitigación revertida
  al resolverse). Checklist para el próximo cliente PrestaShop.
- Método transferible de integración (doctrina general): la regla de las tres veces, separar
  mitigación de solución, el prompt define el resultado no el mecanismo (regla de oro), y escalar
  con hipótesis y evidencia. Engancha con el principio 17 y con `gestion-proveedor-itesa.md`.



La versión que suma la capa de **lógica comercial** como doctrina propia, separada de la lógica
de comportamiento. Integra las tres extracciones de lógica comercial (EDFAN 31 hallazgos, G&D 32,
BETROX 17) con el criterio patrón/instancia, y sube los patrones de corrección de 10 a 13. Regla
de oro de esta versión, que resuelve la mejora continua: **solo los PATRONES entran a la
metodología; las INSTANCIAS (valores concretos de hoy) viven en el material del cliente, fuera del
ZIP.** Así la mejora continua muta instancias sin obligar a tocar la doctrina.

**Nuevo — doctrina de lógica comercial (`logica-comercial-transversal.md`)**
- Capa nueva: cómo VENDE un agente (calificar, presentar, objetar, cerrar, derivar), distinta de
  cómo CONVERSA (`principios-transversales-agente.md`). ~30 patrones comerciales probados en 2 o
  3 rubros, agrupados en calificación, presentación, objeciones, cierre que vende, condiciones de
  negocio, derivación, posicionamiento, cross-sell y segmentación. Cada patrón separa forma
  (sube) de valor concreto (queda en el cliente). Los "candidatos" esperan confirmación en un
  segundo rubro.
- Transversales fuertes confirmados en los tres rubros: subconjunto con condición de pago propia,
  reencuadrar la carencia como oferta, palabra vetada por posicionamiento, no verbalizar la
  operativa interna, señal de compra se aprovecha en el mismo mensaje, guion por tipo de comprador.

**Ampliado — patrones de corrección de 10 a 13 (`10-patrones-correccion-agente.md`)**
- Patrón 11 (contradicción de jerarquía: dos reglas propias que compiten, una pisa a la otra),
  patrón 12 (CTA que existe pero no vende), patrón 13 (regla condicionada a una evaluación
  ambigua del contexto). Los tres transversales, confirmados por el soporte de Prometheo sobre el
  caso PAROS.

**Nuevo — documento de método (`contradicciones-jerarquia.md`)**
- Desarrollo del tercer tipo de error (además de prompt y plataforma): la contradicción de
  jerarquía, con sus dos hermanos (CTA administrativo, condición ambigua). Cómo se reconoce, cómo
  se corrige (nombrar los dos casos, generalizar, declarar prevalencia, nunca reforzar), y su
  enganche con los chequeos 2 y 5 del barrido de coherencia.

**Principio confirmado — patrón vs instancia**
- La separación patrón/instancia, que ya vivía como "documento maestro vs entregable de cliente",
  se vuelve el criterio operativo de toda extracción de lógica comercial: al integrar un hallazgo
  de cliente, la forma sube a la metodología y el valor concreto queda en el prompt y la matriz de
  ese cliente. La metodología solo cambia ante un patrón nuevo.

**Pendiente registrado**
- BETROX tiene un pendiente de arreglo que el equipo suma más adelante; no bloquea esta versión.



La versión que consolida el método de corrección como doctrina madura, con los tres rubros
probando qué es transversal (EDFAN/desarrollista, BETROX/mobiliario, G&D/desarrollista
Sheet-First). Integra los documentos maestros del proceso, la doctrina de diseño de base en
Google Sheets verificada contra la planilla real, y la gestión del proveedor. Todo aditivo, con
una regla de oro explícita en cada archivo: **la metodología describe patrones y criterios para
auditar y decidir, no dicta reglas que obliguen a romper un prompt que hoy funciona.**

**Nuevo — los 10 patrones de corrección (`10-patrones-correccion-agente.md`)**
- Documento maestro: los 10 errores recurrentes de cualquier agente (dato que la fuente
  devuelve y el agente evade, regla fija en pregunta combinada, prioridad comercial al ofrecer,
  apertura que se saltea, variante asumida, mismo nombre en entidades distintas, regla absoluta
  sin ámbito, cierre que no vende, cambio de mecanismo sin propagar, rondas que se pisan). Cada
  uno con síntoma, regla, traducción por vertical y estado (cubierto/parcial/hueco/hueco por
  diseño). Validados en Martina y Catalina; los vistos en dos rubros, marcados transversales.

**Nuevo — gestión del proveedor (`gestion-proveedor-itesa.md`)**
- Los tres actores (AUREA / Prometheo-ITESA / cliente) y la regla de que un mensaje al cliente
  no es una elevación al proveedor. El molde para auditar una reescritura del prompt que entrega
  Prometheo (bloqueantes, reglas perdidas, contradicciones, lo replicable, lo conservado). El
  hallazgo estable: **la reescritura del proveedor mejora la estructura y pierde la lógica
  comercial; no se elige entre versiones, se combinan.** El dossier de incidentes con filtro de
  credibilidad (columna de descartados).

**Nuevo — doctrina de guión de testing (`guion-testing.md`)**
- El principio de los "primos" (testear la regla general, no el caso: si pasa solo el caso
  reportado, quedó parche), el formato de test, la marca [PLATAFORMA] (si falla, revisar la
  integración antes que el prompt), el bloque de regresión, y la distinción guión interno vs
  client-facing.

**Ampliado — doctrina de diseño de base en Google Sheets (`08-reglas-integracion-catalogo.md`)**
- Sección nueva verificada contra la planilla real de G&D (6 hojas): arquitectura por grano,
  criterio de diseño (fuente única, IDs jerárquicos, hoja derivada con la de detalle como fuente
  de verdad, precio vacío no 0), 9 buenas prácticas reutilizables, y los problemas reales
  detectados (hoja derivada desincronizada apuntando a IDs inexistentes, un concepto en dos
  formatos, columnas huérfanas, desnormalización pesada, dominios inconsistentes). Trazabilidad
  columna ↔ regla del prompt, y ruteo por grano como primera decisión de búsqueda. Más el límite
  de parcialidad de búsqueda como pregunta abierta a ITESA (el agente no puede declarar parcial
  lo que la integración no marca como parcial).

**Ampliado — método de corrección (`metodologia-correccion-agente.md`)**
- El template de auditoría de entrega (5 hojas: Entrega, Barrido, Correcciones, No regresión,
  Pendientes) y el criterio de refuerzo completo de Prometheo (regla positiva + prohibición +
  ámbito + autochequeo), con la corrección de mobiliario urbano citada textual como la formuló
  el proveedor. Trazabilidad con las palabras del proveedor: cuando la corrección la formula
  Prometheo, se conserva su formulación.

**Ampliado — principios transversales (`principios-transversales-agente.md`)**
- De 14 a 16 principios. Se sumaron: dato vivo siempre desde la fuente nunca de memoria, y no
  inventar datos fácticos ni contexto conversacional. Ambos probados en los tres rubros. Nota de
  campo: la migración cruzada ya ocurrió en los prompts vivos (una regla de BETROX está en el de
  EDFAN, redactada casi igual) = la doctrina ya viaja entre agentes.

**Ampliado — restricciones de plataforma (`restricciones-plataforma-prometheo.md`)**
- 4 restricciones nuevas confirmadas en G&D: refresco de integración destructivo (alta de
  columna obliga a reconfigurar todo), filtrado por estado no siempre confiable (hubo que borrar
  filas), límite de elementos por búsqueda no documentado, método de consulta multi-hoja no
  documentado.

**Nuevo principio de organización (`00-OUTPUTS-POR-ETAPA.md`)**
- Documento maestro (método reutilizable) vs entregable de cliente (se archiva por cliente). La
  matriz de auditoría de un cliente es viva pero no es método transversal. Cómo evoluciona el
  proceso: error nuevo → patrón nuevo, o chequeo nuevo del barrido, o regla de método nueva.



La integración más grande hasta ahora: tres Guías de Implementador completas (EDFAN/Tokko,
G&D/Sheet-First, BETROX/PrestaShop), el sistema completo de mensajería automatizada de Prometheo
(5 mecanismos, no solo seguimientos), la corrección del modelo de perfil de lead (variable +
hija reemplaza tags de tipo-usuario), y la indexación del Acuerdo de Alcance y Objetivos como
familia de output. Todo integrado de forma aditiva: nada se sustituyó sin dejar explícita la
corrección y su motivo.

**Agregado — Familia 7 de outputs: Guía de Implementador**
- `06-estructura-guia-implementador.md` ampliado con las reglas duras de formato del generador
  (vertical y angosto, opciones en bloque de código, nombres sin guion bajo, valores en lenguaje
  natural idénticos entre prompt y CRM), las reglas de diseño de variables (no solo de formato:
  única vs múltiple, padre/hija, producto-externo vs interés-del-lead, patrón dual de
  inteligencia comercial ahora en 6 variables), y una tabla comparativa de los tres casos reales
  de referencia (EDFAN, G&D, BETROX) con sus diferencias de integración, agendamiento,
  distribución y modelo de perfil.
- Nuevo principio de diseño: cuándo un B2B necesita Embudo propio (real estate: intermediación
  real hacia un tercero) vs cuándo alcanza con variables + tags (mobiliario: co-diseño como modo
  de trabajo, mismo embudo).

**Corregido — modelo de perfil de lead (variable única + variable hija reemplaza tags de tipo-usuario)**
- `embudos-y-tags.md`: documentada la corrección confirmada en dos casos (G&D: `Tipo Perfil` +
  `Inversión Finalidad` hija; BETROX: `Tipo Cliente` + `Tipo Profesional` hija). La tag de
  tipología pasa a ser espejo de visibilidad, no fuente del dato. Se corrige también `Contacto
  VIP` (de tag binaria combinable a variable de 4 valores) y se documenta el reemplazo de la
  vieja dimensión "Prioridad" ambigua por la tag `Hot Lead` con criterio binario estricto.

**Reescrito — sistema de mensajería automatizada (framework-seguimientos.md, ahora hub de 5 mecanismos)**
- Antes cubría solo Seguimientos y afirmaba que la lógica AND de tags era "Fase 2"; **esa
  afirmación queda corregida explícitamente**: el modelo real de segmento (tags/variables TODAS
  o AL MENOS UNA + exclusiones "No tiene") ya está disponible y confirmado en BETROX.
- Sumados los otros 4 mecanismos, antes inexistentes en la metodología: Recordatorios
  conversacionales (gratis, detecta fecha en la charla), Recordatorios programados (Pro, variable
  Fecha y hora, con checklist de troubleshooting), Campañas masivas (segmento puntual, requiere
  API oficial), Plantillas de WhatsApp Meta (formato, categorías Marketing/Utility/Authentication
  con regla de decisión).
- Sumados los 6 criterios de redacción invariables de seguimientos, la convención de nombre
  `[Estadío] - post [tiempo]`, los 3 packs de ventana horaria (12/7, 12/5, 8/5), la variable
  `Reasignación Moderador` como patrón cross-rubro, y el caso G&D completo con mensajes y
  alternativas A/B.
- Documentados los **tres sistemas de placeholder** (archivo, seguimiento, recordatorio) como no
  intercambiables, con tabla comparativa. Referenciado también desde `08-reglas-integracion-catalogo.md`.

**Ampliado — restricciones de plataforma (3 nuevas, confirmadas en producción)**
- `restricciones-plataforma-prometheo.md`: colores de Smart Tags (solo 6, se repiten entre
  dimensiones, la dimensión se distingue por nombre), acciones de tag (solo 3, Notificaciones
  requiere plan Enterprise), y el patrón "Descripción de Embudo" como instrucción que la IA lee
  para decidir asignación de tags.

**Ampliado — doctrina de integración PrestaShop y ERP**
- `08-reglas-integracion-catalogo.md`: bloqueantes ITESA confirmados y recurrentes (precio real
  por medida, cuadro "Detalles de producto" no expuesto). Nueva distinción ERP interno no
  integrado (caso Bejerman/BETROX) vs ERP integrado a medida por Prometheo Connect/Atlas, con
  criterio de decisión (¿el agente necesita leer o escribir del ERP para conversar?).

**Ampliado — rubros con casos reales nuevos**
- `06-rubros/02-mobiliario.md`: segundo cliente real del rubro (BETROX). Distribución de destino
  único (alcanza con Notificaciones, no hace falta reparto equitativo), B2B/co-diseño sin embudo
  propio, KPI de Tasa de cierre con framing propio del rubro (showroom como activo comercial
  número 1), y el patrón producto-externo vs interés-del-lead aplicado a Outlet.

**Ampliado — import de contactos**
- `importacion-contactos.md`: disciplina formal de carga de base legacy (auditar columnas
  pobladas, no promover defaults masivos, preservar verbatim, extraer valores distintos antes del
  import, sanear teléfonos E.164, QA campo por campo), confirmada en dos casos (G&D, BETROX).

**Indexado — Familia 8 de outputs: Acuerdo de Alcance y Objetivos**
- `00-OUTPUTS-POR-ETAPA.md` ampliado a ocho familias. El Acuerdo de Alcance (DOCX branded,
  editable en Google Docs, con catálogo de 8 bloques de servicio marcable por emoji, cuadro de
  integraciones a medida ERP, lista abierta de deseables, y bloque de firmas) se dispara al
  cierre de Etapa 3. Se nota que las familias 7 y 8 viven fuera de la skill de outputs
  (metodología pura / generador propio), candidatas a empaquetarse ahí en una vuelta futura sin
  urgencia.

**Router actualizado**
- `00-CONSULTA.md`: nueva fila de despacho para el pasaje Etapa 2 → Etapa 3 (Guía de
  Implementador), apuntando a integración + rubro + los 5 mecanismos de mensajería.

**Encabezados de auto-ruteo agregados** a `embudos-y-tags.md`, `restricciones-plataforma-prometheo.md`
e `importacion-contactos.md`, que no los tenían.



La versión más grande hasta ahora. Procesa el feedback de corrección de agentes en
producción de tres clientes (G&D, EDFAN, BETROX) sobre dos rubros, e introduce un cambio
de arquitectura: la metodología deja de ser un manual para leer de corrido y pasa a ser un
**sistema de consulta por ejes** que se ensambla según la tarea. Suma la doctrina de
integraciones por fuente, la trazabilidad corrección→regla, y los principios transversales
de diseño de agente probados en dos rubros.

**Agregado — arquitectura de consulta (4 ejes + router)**
- `00-CONSULTA.md` (nuevo, raíz de `01-metodologia/`): router de despacho. Lo primero que se
  lee en cualquier conversación. No tiene contenido de metodología: dice qué cargar según
  cuatro ejes ortogonales (PROCESO / RUBRO / INTEGRACIÓN / TRANSVERSAL) y según si la
  conversación es nueva o con trayectoria. La metodología se consulta por la intersección,
  no entera.
- Encabezados de auto-ruteo (estilo `description` de skill: `consultar-cuando`,
  `disparadores`, `fuente-única-de`, `combina-con`) agregados a los archivos clave de diseño
  y rubros, para que cada archivo declare cuándo entra y con qué se combina.

**Agregado — principios transversales de diseño de agente**
- `principios-transversales-agente.md` (nuevo): **diez principios** de comportamiento del
  agente, cada uno PROBADO en dos rubros independientes (desarrollista + mobiliario), con
  evidencia citada de ambos lados. No repetir/ampliar, no exponer la herramienta, de menos a
  más, una variable por turno, calificar antes de mostrar, no revelar que es agente, validar
  nunca invalidar, responder en orden lo pedido, mensajes cortos, y "el cliente marca el
  camino". Incluye criterio de promoción (rubro → transversal solo si se ve en 2+ rubros) y
  el hallazgo de autoría refinado por perfil del corrector.

**Agregado — metodología de corrección y trazabilidad**
- `metodologia-correccion-agente.md` (nuevo): el método de procesar feedback (clasificar por
  capa dato/terminología/lógica, detectar patrón, decidir destino). Incluye el arco de
  autoría (consultor → cliente autónomo; vendedor reporta lógica comercial, operador reporta
  datos) y la **sección de trazabilidad corrección→regla** con casos verbatim de los tres
  prompts (ej. "Moca 2 escritura" → Regla 56 NO AFIRMAR ESCRITURA). Patrón de diseño: el
  prompt lleva su propia trazabilidad adentro, citando el caso real que originó cada regla.

**Ampliado — doctrina de integraciones por fuente**
- `08-reglas-integracion-catalogo.md`: además de las 6 reglas genéricas que ya tenía, suma la
  **doctrina por fuente** (Google Sheets / Tokko / PrestaShop), destilada de los tres prompts
  en producción. Insight central: las reglas de consulta dependen de la fuente, no del rubro.
  Sheets (verificación del lote, búsqueda fresca, columnas sobre notas, precio siempre),
  Tokko (tipología-proyecto vs unidades-hoy, anti-memoria, discreción), PrestaShop (modelo
  como clave, búsqueda escalonada de 4 intentos, hoy sin consulta por categorías → destacados
  hardcodeados provisorios). Suma el **sistema de placeholders provisorios** (hueco marcado
  con su estado cargado/pendiente/comprimir, reemplazo por asset real, trazable).

**Ampliado — lógicas comerciales por rubro (de feedback real)**
- `06-rubros/01-real-estate.md`: lógicas desarrollista destiladas del feedback de G&D y
  EDFAN (precisión de stock, parámetros fijos vs flexibles, prejuicio de zona sur,
  financiación orientativa en dos pasos, no asustar con precios, comparar con pro/contra,
  inversor sin experiencia en tres pasos, cercanía como eje, derivación según cliente).
- `06-rubros/02-mobiliario.md`: lógicas mobiliario de BETROX (cascada de recomendación
  ambiente→uso→forma→materiales→medidas→colores, foto como interfaz inicial, similares
  linkeados, estándar cotiza/personalizado deriva, cross-sell por combos, showroom semilla
  vs cierre, plazo como dato de venta).
- `06-rubros/03-insumos-construccion.md`: **primera evidencia real** del rubro (EDFAN
  Productos / Paula, reunión 2). Deja de ser hipotético: dos flujos (asesoramiento vs
  material), tres tipos de usuario, m² antes que zona, el cliente asesora pero no ejecuta,
  densidad de repregunta por perfil, terminología del oficio.

**Actualizado — documento de feedback de demo**
- `feedback-demo-iteracion.md`: hallazgos confirmados con dos rubros (transversalidad del
  documento, arco de autoría, la marca sobre la captura es la crítica, el prompt lleva su
  trazabilidad). Conexión explícita a `metodologia-correccion-agente.md` y
  `principios-transversales-agente.md`.

**Agregado — índice de outputs por etapa**
- `00-OUTPUTS-POR-ETAPA.md` (nuevo): índice de qué documento cliente-facing se entrega en
  cada etapa/estadío (seis familias: Diseño de CRM, Carga de Contactos, Guión de Testing,
  Presentación estética, Documentación formal, Feedback de Demo). NO internaliza los
  templates: la fuente viva es la skill `documentos-client-facing` (en incubación, fuera del
  ZIP). Este archivo es solo el puntero y el mapa por etapa.

**Decisiones de alcance**
- Los PDF/capturas crudos de feedback NO van al ZIP (son materia prima: pesan, cambian). Va
  solo la destilación (lógicas + método + plantilla). El ZIP se mantiene como doctrina curada
  y liviana.
- Diseñar los templates de cada estadío (no solo alojarlos) queda para v1.14: requiere mapear
  cada template por etapa, su criterio de diseño y su contexto de uso. Se registra como el
  frente principal de la próxima versión.



Refinamiento del modelo de Smart Tags con la doctrina validada en G&D Developers.
Reemplaza el "tope de 2 tags fijas" de v1.11 por el modelo de **"una tag por dimensión"**,
que es más honesto con la realidad y resuelve la ambigüedad de cuántas tags puede tener
un lead. Integra la doctrina del rubro desarrollista como apartado canónico en
`06-rubros/01-real-estate.md`.

**Cambiado — modelo de tags**
- `embudos-y-tags.md`: la regla central pasa de "2 Smart Tags visibles (estadío +
  tipología)" a "**una tag por dimensión**". Una dimensión es una pregunta sobre el lead
  con valores mutuamente excluyentes entre sí. Tags de dimensiones distintas conviven sin
  problema; tags de la misma dimensión nunca conviven.
- Dimensiones canónicas hoy: **estadío** (etapa del embudo), **tipo de usuario** (Inversor
  / Cliente final / Inmobiliaria — mutuamente excluyentes), **prioridad** opcional (VIP).
  Resultado típico: 2 a 3 tags visibles por lead. Sin tope arbitrario.
- La "prioridad" deja de ser "excepción justificada a la regla de 2 tags" y pasa a ser
  una dimensión legítima del modelo. Si aplica, se asigna; si no, no.
- Regla 1 del archivo oficial actualizada al modelo de dimensiones.
- Regla dura 6 de `embudos-y-tags.md` reescrita.
- Árbol de decisión tag/variable/embudo y sección "Por qué pocas tags" reescritos.

**Agregado — doctrina del rubro desarrollista**
- `06-rubros/01-real-estate.md`: nuevo apartado **"Smart Tags — doctrina del rubro
  (validada en G&D)"**. Incluye el inventario completo de los 3 embudos típicos del rubro
  (Recepción y Calificación, Venta y Cierre, Inmobiliaria), las 3 tags de tipo de usuario
  (mutuamente excluyentes), la dimensión prioridad opcional, la lógica de color
  transversal y el principio de asignación de acciones. Cierra con qué es fijo y qué es
  flexible al replicar en otros desarrollistas, y un checklist del implementador.

**Corregido respecto del documento G&D original**
- El documento de G&D que sirvió de fuente listaba "Inversor + Inmobiliaria + Contacto
  VIP" como ejemplo de combinación válida. Eso era incorrecto: Inversor e Inmobiliaria
  son de la misma dimensión (tipo de usuario), no pueden coexistir. La doctrina integrada
  refleja la corrección: `En Conversación + Inversor + Contacto VIP` es válida;
  `Inversor + Inmobiliaria` no.

---

## v1.11 — 30 mayo 2026

Actualización integral con los aprendizajes del caso G&D Developers y la base BETROX. Es
la actualización más grande desde v1.9 — formaliza el modelo de tags, cierra el camino B
(las 4 propuestas se aplican al archivo oficial de reglas), incorpora la skill
`prometheo-etapa2-design` v2, y agrega dos archivos de metodología nuevos: el Excel de
Carga y el Documento de Feedback de Demo.

**Cambiado — modelo de Smart Tags (formalización)**
- `embudos-y-tags.md` reescrito con el modelo **estadío + tipología** (las 2 Smart Tags
  visibles por lead) extraído del caso G&D. Sub-reglas operativas integradas: la tipología
  se deriva de variable; no diseñar tags con alta similitud semántica; "FAQ y Excepciones
  NO son embudos" como corrección conceptual. La **prioridad va a variable por default**
  (la tag de prioridad es excepción documentada, no regla).
- El "tope de 2 tags como criterio en prueba" de v1.10 se promueve a **regla validada**.

**Camino B — cerrado, aplicado al archivo oficial**
Las 4 propuestas que estaban pendientes se aplicaron a
`03-reglas-diseno-prometheo-by-aurea.md`:
- Regla 1 reescrita al modelo estadío + tipología.
- Regla 2 reescrita: deja de fijar tags universales (`#seguimiento_activo` +
  `#derivar_a_humano` del modelo MIA temprano); ahora pide solo el mínimo funcional de
  estadío.
- Regla 3 actualizada: las acciones se cuelgan de tags, y como la etapa es tag, una etapa
  puede ejecutar.
- Regla 6 invertida: los follow-ups SÍ soportan placeholders vía plantilla con variables
  mapeadas.
- Reglas 8/9/10: vocabulario "embudo" alineado al modelo formal; Regla 9 aclara que el
  estadío principal va en tag, no en variable (variables de estadío como `proceso_actual`
  quedan obsoletas).

**Agregado — archivos nuevos en `02-ETAPA2-Diseno/`**
- `excel-carga-clientes.md` — el 4º output de Etapa 2. Explica qué es el Excel/Sheets de
  carga, su estructura (2 hojas, prefijo `var_`, separador `|`, teléfono plano), el
  conflicto Excel-de-trabajo vs Sheets-plano. La ejecución técnica vive en el módulo de la
  skill (`excel_carga_contactos.md`).
- `feedback-demo-iteracion.md` — el documento de feedback que el cliente completa durante
  el testing del agente. Reglas para marcar capturas (aditivo, nunca destructivo), una
  corrección por fila, versión del prompt en encabezado. Caso de referencia: BETROX.

**Cambiado — skill `prometheo-etapa2-design`**
- Reemplazada por la v2 (más madura). Incluye SECCIÓN 0 explícita con la arquitectura de
  3 capas (embudos / tags / variables), el módulo `excel_carga_contactos.md` (4º output),
  y `docx_xml_fixes.md` (bug texto vertical en Google Docs).

**Renombrado**
- `reglas-a-revisar-v1.8.md` → `reglas-revisadas-v1.11.md`. Las 4 propuestas pasan de
  `PENDIENTE DE APROBACIÓN` a `APROBADA Y APLICADA`. El archivo se conserva como historial
  para trazabilidad.

**Lo que sigue**
- 2 pendientes de ITESA siguen abiertos (cupo de Connect, sync de PrestaShop).
- Plantilla DOCX canónica de feedback de demo (sin datos de cliente) — por ahora se
  reutiliza el BETROX como base.

---

## v1.10 — 22 mayo 2026

Unificación de la estructura de bloques del Discovery — corrige el desajuste detectado en
v1.9 entre el Doc 1 y las skills.

**Resuelto — el desajuste de numeración de bloques**
El ZIP tenía dos estructuras de Discovery incompatibles conviviendo: el Doc 1 usaba 12
bloques (B0=Objetivo, FAQs y Objeciones separados, sin Logística) y las skills usaban 13
(B0=Equipo, FAQs+Objeciones juntos, con B12 Logística). Se adoptó como oficial una
estructura unificada de **14 bloques (B0-B13)** más los condicionales B13 Logística y B2B,
con **Derivación a humano como bloque propio (B12)** — antes era un subpunto de Autonomía.

**Agregado**
- `01-ETAPA1-Discovery/02-PASO2-Discovery/estructura-discovery.md` — **fuente única** de la
  estructura de bloques. Define los 14 bloques + condicionales. Todos los demás archivos
  referencian este; ninguno vuelve a listar los bloques por su cuenta. Resuelve de raíz la
  causa del desajuste (la estructura estaba copiada en varios archivos).

**Cambiado**
- `doc1-discovery-biblia-template.md`: ya no lista los bloques — apunta a
  `estructura-discovery.md`.
- `protocolo-validacion-biblia.md`, `protocolo-extension-metodologia.md`,
  `refactorizacion.md` (skill etapa2-design): referencias actualizadas al archivo único.
- Skill `prometheo-discovery-transversal`: el resumen de bloques se actualizó a la
  estructura oficial de 14 bloques (antes tenía la numeración vieja).
- Skills `prometheo-audit-doc1` y `prometheo-drive-audit-real-estate`: referencias de
  bloque corregidas a la numeración nueva.

---

## v1.9 — 22 mayo 2026

Incorporación de los aprendizajes de plataforma de la implementación de AUREA Hub como
cliente de Prometheo (documento "AUREA — Aprendizajes Plataforma Prometheo").

**Cambiado — corrección de fondo**
- `embudos-y-tags.md`: reescrito. El modelo de v1.8 ("tres entidades separadas: Embudo,
  Variables, Smart Tags") era incorrecto. Modelo correcto, verificado en plataforma: hay
  **dos entidades base** (Smart Tags y Variables); el **Embudo no es una entidad aparte**,
  es una agrupación ordenada de Smart Tags — cada etapa de embudo ES una tag. En
  consecuencia: una etapa de embudo se ve en Chats y puede disparar ejecutables; cayeron
  la regla dura 2 ("ejecutables nunca en etapas" — era un mito) y la regla dura 3 ("no
  espejar etapas" — sin sentido si la etapa es una tag). La intención válida de la vieja
  regla 3 (no inflar la lista de Chats) se reubicó en el criterio de diseño. Se integró el
  tope de 2 tags visibles (1 operativa + 1 de rubro opcional) como criterio en prueba.

**Cambiado**
- `restricciones-plataforma-prometheo.md`: restricción 4 ampliada (prompt opcional de
  variable: con prompt la completa la IA, sin prompt es manual). Agregadas restricciones
  16-18: match de tags distingue tildes pero no mayúsculas; las tags desconocidas se
  ignoran en silencio en la importación; las variables deben existir antes de importar
  (prefijo `var_`).

**Agregado**
- `01-metodologia/02-ETAPA2-Diseno/importacion-contactos.md` — procedimiento de importación
  de contactos por Excel y orden de carga obligatorio (variables → tags → embudos →
  contactos): plantilla oficial, columna Tags con separador `|`, deduplicación por
  teléfono, problema `__EMPTY`, checklist para cliente nuevo.

**Pendiente (no aplicado — espera aprobación)**
- Las propuestas de `reglas-revisadas-v1.11.md` para las Reglas 1, 3, 6 y 8/9/10 siguen sin
  aplicar al archivo oficial de reglas.
- Desajuste de numeración de bloques de discovery (B0-B11) entre el Doc 1 oficial y las
  skills — detectado, pendiente de resolver.

---

## v1.8 — 21 mayo 2026

Integración de la investigación del GitBook oficial de Prometheo y la validación con el bot
oficial e ITESA. Cierra el modelo de Embudos/Tags/Variables.

**Agregado**
- `01-metodologia/02-ETAPA2-Diseno/embudos-y-tags.md` — modelo de las tres entidades de
  Prometheo (Embudo, Variables, Smart Tags): qué hace cada una, las dos funciones del Smart
  Tag, las reglas duras del modelo y el criterio de diseño tag-vs-variable-vs-embudo que
  reemplaza el viejo sesgo "menos tags = mejor".
- `01-metodologia/02-ETAPA2-Diseno/integraciones-por-rubro.md` — mapa de las integraciones
  y canales de Prometheo ordenados por las 4 verticales, con nivel de confianza por ficha.
- `01-metodologia/02-ETAPA2-Diseno/pendientes-itesa.md` — buzón único de dudas de
  plataforma sin confirmar con ITESA, con registro de las ya resueltas.
- `01-metodologia/02-ETAPA2-Diseno/reglas-revisadas-v1.11.md` — documento de trabajo
  (camino B): propuestas de cambio a las reglas afectadas por el modelo nuevo. No aplica
  nada al archivo oficial hasta aprobación regla por regla.

**Cambiado**
- `restricciones-plataforma-prometheo.md`: corregida la restricción 5 (seguimientos —
  estaba contradictoria; ahora describe bien 1 tag / varias con AND nativo / sin tag).
  Agregadas 7 restricciones nuevas del GitBook (9-15): 3 acciones de Smart Tag, repetición
  nativa de seguimientos, franja horaria, placeholders vía plantilla, adjuntos, Prometheo
  Connect, dos conexiones de WhatsApp. Tabla de planes (restricción 7) reescrita con la
  info real: Basic/Pro/Enterprise, Connect desde Pro.

**Pendiente (no aplicado — espera aprobación)**
- Las propuestas de `reglas-revisadas-v1.11.md` para las Reglas 1, 3, 6 y 8/9/10. El archivo
  oficial `03-reglas-diseno-prometheo-by-aurea.md` no se tocó.

**Detectado — no corregido en esta versión**
- `00-INDEX.md` (línea ~118) menciona "checklist de las 24 reglas"; el archivo de reglas
  tiene 20 reglas numeradas. Desfasaje de conteo a corregir en una próxima auditoría.

---

## v1.7 — 21 mayo 2026

**Agregado**
- `01-metodologia/roadmap.md` — roadmap completo de la metodología: estado por etapa,
  pendientes ordenados por prioridad, dependencias, orden de trabajo sugerido.

**Cambiado**
- README: la sección "02-SKILLS" se reordenó **por etapa** (TRANSVERSAL → ETAPA1 → ETAPA2
  → ETAPA3/4 → templates), coherente con la estructura de carpetas de la v1.6. Las
  descripciones de skills se agruparon por carpeta.
- README: los placeholders `PLACEHOLDER-referente-*-01` estaban descriptos en la sección de
  skills por error; se movieron a la sección de casos de referencia, junto a los `-02`.
- Rutas de skills normalizadas a formato carpeta (`prometheo-X/`) en todo el README.

**Corregido — auditoría de consistencia del ZIP**
- Conteo de reglas: `01-operativa-y-decisiones.md` y `project-instructions-universal.md`
  decían "15 reglas"; el documento fuente tiene 24. Corregido a 24.
- Gramática rota por un reemplazo de naming anterior ("al reglas de diseño Prometheo
  vigente") en `00-protocolo-incorporar-nuevo-referente.md` y `00-INDEX-referentes.md`.
- Referencias a las skills `prometheo-etapa2-design` y `prometheo-crm-graphics` como
  archivo `.md` corregidas a formato carpeta en `01-operativa-y-decisiones.md` y
  `docx-diseno-crm-template.md`.

**Detectado, pendiente de resolver (ver `roadmap.md`)**
- Punteros rotos: `references/plantilla.md` (referenciado por las 2 skills de formulario,
  no existe) y `documento-cero-template.md` (referenciado por la auditoría web, no existe).
- Menciones residuales a "modelo v7" en archivos de metodología activa — decisión de
  naming editorial pendiente.

---

## v1.6 — 21 mayo 2026

**Cambiado — reorganización estructural de `02-skills/`**
- Las skills se reorganizaron **por etapa** en lugar de por tipo. Estructura nueva:
  `00-TRANSVERSAL/`, `01-ETAPA1/`, `02-ETAPA2/`, `03-ETAPA3/`, `04-ETAPA4/`, `05-templates/`.
- Carpetas viejas eliminadas: `00-skill-principal/`, `01-diseno-prompt-y-crm/`,
  `02-skills-verticales/`. La carpeta `03-templates/` se renombró a `05-templates/`.
- Reubicación de las 12 skills existentes:
  - **Etapa 1:** `prometheo-etapa1`, `prometheo-auditoria-web`, `prometheo-docs-kickoff`,
    `prometheo-discovery-transversal`, `prometheo-audit-doc1`, `prometheo-formulario-real-estate`,
    `prometheo-formulario-mobiliario`.
  - **Etapa 2:** `prometheo-etapa2-design`, `prometheo-drive-audit-real-estate`,
    `prometheo-crm-graphics`.
  - **Transversal:** `project-instructions-universal`, `prometheo-vertical-real-estate`,
    `prometheo-vertical-mobiliario` (se usan en Etapa 1 y Etapa 2, no se duplican).
- Todas las rutas internas que referenciaban las ubicaciones viejas fueron actualizadas.

**Agregado**
- Skill `prometheo-diseno-agente-ia-feedback` (en `02-skills/02-ETAPA2/`) — genera el
  Documento de Feedback de Demo, el DOCX apaisado de dos columnas que recoge las
  correcciones al agente durante la iteración del prompt. Incluye el script de generación
  y un documento de ejemplo.
- `01-metodologia/02-ETAPA2-Diseno/02-PASO2-Diseno-Agente-IA/protocolo-feedback-demo.md` —
  protocolo de metodología del Documento de Feedback de Demo (su fuente de verdad).
- README en cada carpeta de etapa de `02-skills/`. Las carpetas de Etapa 3 y 4 quedan con
  un slot reservado para el "auditor de etapa" pendiente de crear.

---

## v1.5 — 21 mayo 2026

**Agregado**
- Categoría **"Conversaciones de referencia"** al Doc 3 del Discovery (template
  `doc3-accesos-documentacion-template.md`): sub-bloques Conversaciones Ideales y NO
  Ideales, en formatos `.txt` (conversaciones completas) y `.jpg/.png` (capturas por tipo
  de interlocutor y momentos puntuales). Incluye carpeta en la estructura Drive y entrada
  en "material recomendado, no bloqueante".
- `01-metodologia/protocolo-extension-metodologia.md` — protocolo de cómo extender la
  metodología sin rehacerla (principio de fuente única, tabla de cambios comunes con sus
  punteros, checklist).
- `CHANGELOG.md` (este archivo).

**Cambiado**
- Skill `prometheo-discovery-transversal`: la sección del Doc 3 dejó de copiar la
  estructura del documento — ahora apunta al template como fuente de verdad (primer puntero
  bajo el principio de fuente única).
- Módulo `guia-metodologica.md` de `prometheo-docs-kickoff`: el texto del Documento 3 se
  separó en afirmación canónica (fija) + enumeración de ejemplos (adaptable, derivada del
  template e incluyendo conversaciones de referencia).

---

## v1.4 — 20 mayo 2026

**Agregado**
- Skill `prometheo-docs-kickoff` (en `02-skills/00-skill-principal/`, modular: `SKILL.md` +
  `doc-bienvenida.md` + `guia-metodologica.md`) — genera los 2 documentos cliente-facing
  del Paso 1 de Etapa 1: el Doc de Bienvenida y la Guía Metodológica. Las skills
  principales pasaron de 4 a 5.
- Carpeta de caso de referencia `08-casos-referencia/TKVA-real-estate/` — Doc de Bienvenida
  (PDF) y Guía Metodológica (`.md`) reales de TKVA, más README de carpeta.

**Cambiado**
- Skill `prometheo-auditoria-web`: nomenclatura alineada de "Paso 0 / Etapa 0" a "Paso 1.1
  de Etapa 1". Se agregó la sección de cierre con handoff explícito a `prometheo-docs-kickoff`.
- Skill `prometheo-etapa1`: pasos 1.2 y 1.3 dejaron de estar marcados como "pendiente de
  crear" — ahora apuntan a `prometheo-docs-kickoff`.
- `README.md` y `00-INDEX.md`: actualizados con la skill nueva; se quitó el conteo fijo de
  archivos (estaba desactualizado).

---

## v1.3 — base

Estado inicial registrado al abrir este changelog. Estructura de 4 ETAPAS con PASOS
internos, 24 reglas de diseño, 11 skills, casos de referencia (4 PROTOTIPO + 3 carpetas de
ejemplos reales), archivos de metodología (planes, métricas, restricciones, framework de
seguimientos, sistema FIJA/FLEXIBLE).

> Las versiones previas a v1.3 no tienen registro detallado en este changelog —
> v1.3 es el punto de partida del versionado documentado.
