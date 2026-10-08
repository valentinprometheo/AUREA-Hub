# MÓDULO: DOCX DISEÑO DE CRM — DETALLE POR SECCIÓN

Estructura obligatoria de las 11 secciones del DOCX cliente-facing. Cada sección
sigue la fórmula visual AUREA: **banner → card explicativa → gráfico overview →
tabla técnica → gráfico arquitectura/detalle (si aplica) → card "EJEMPLO PARA
QUE SE ENTIENDA" → bloque de feedback amarillo**.

---

## SETUP DEL DOCUMENTO

### Márgenes y tipografía
- Márgenes: 2 cm en todos los lados
- Tipografía base: Calibri 11pt
- Tipografía banner: Calibri 13pt blanco bold
- Tipografía título card: Calibri 11-12pt bold color del tema

### Paleta AUREA (RGB hex)
- Morado: `7C5CBF` — Variables, conceptos transversales
- Naranja: `E8943A` — Smart Tags, seguimientos, énfasis
- Azul: `5B8FD9` — FAQ, ejemplos, info
- Verde: `4CAF80` — Venta, condiciones positivas, aprobaciones
- Rojo: `D9534F` — Cancelaciones, errores críticos
- Morado claro: `9D7FD4` — Seguridad
- Gris claro: `F1EFE8` — Pies, contenedores neutros
- Coral: `F37D6E` — Acciones del agente
- Teal: `3FA89E` — Áreas humanas, destinos finales
- Cyan cliente: `00B0F0` — Subbanners de tablas que el cliente debe completar
- Amarillo pálido: `FFF9D6` — Bloques de feedback

### Color por proceso (consistencia entre gráficos y secciones)
- Venta = Verde
- Soporte = Rojo
- FAQ = Azul
- Seguridad = Morado claro
- Postventa = Gris

---

## SECCIÓN 1 — PORTADA + "QUÉ ES ESTE DOCUMENTO"

### Composición
1. 3 párrafos vacíos (espacio superior)
2. Eyebrow centrado: "AUREA Hub × Prometheo" (morado, 14pt, bold)
3. Título principal centrado: "[NOMBRE CLIENTE]" (oscuro, 42pt, bold)
4. Subtítulo centrado: descripción corta del cliente (gris, 14pt, italic)
5. Subtítulo del entregable: "Diseño del Agente IA + CRM" (oscuro, 22pt, bold)
6. Versión: "Versión final · Modelo conceptual v[N]" (naranja, 12pt, bold)
7. Card explicativa "QUÉ ES ESTE DOCUMENTO" con 3 bullets:
   - Es la presentación del diseño del CRM y del agente IA que [cliente] va a tener funcionando en Prometheo.
   - Cada sección muestra una pieza del sistema, con un gráfico que la explica de un golpe de vista, una tabla con los valores concretos, y un ejemplo aplicado.
   - Al final de cada sección hay un bloque amarillo donde pueden escribir su feedback directamente.
8. Pie centrado: "Consultoría por Valentín Zas — AUREA Hub" + "Plataforma de implementación: Prometheo (ITESA)"
9. Page break

---

## SECCIÓN 2 — ROLES DEL AGENTE

### Composición
1. Banner morado: "1. ROLES DEL AGENTE"
2. Párrafo introductorio (1-2 líneas) explicando que el agente tiene N roles ordenados por prioridad
3. Tabla 3 columnas: Rol | Qué hace | Estado MVP
   - Columna "Rol": nombre corto (Vender, Onboarding, Soporte, FAQ y consultas, Seguridad, etc.)
   - Columna "Qué hace": descripción 1-2 líneas
   - Columna "Estado MVP": "Activo", "Fase 2", "No incluido"
4. Bloque feedback amarillo
5. Page break

### Reglas
- Mínimo 4 roles, máximo 7
- Si un rol no entra al MVP, marcarlo como "Fase 2" pero documentarlo
- Header background: oscuro (`2D2A3E`)
- Anchos de columna: 3.5cm | 9.5cm | 3cm

---

## SECCIÓN 3 — ESTRATEGIA + KPIs

### Composición
1. Banner verde: "2. ESTRATEGIA + KPIs"
2. Card explicativa "OBJETIVO PRINCIPAL Y SECUNDARIOS" con 3 bullets:
   - Objetivo principal: [una frase clara]. Si el agente duda entre [opción A] y [opción B], hace [opción ganadora].
   - Objetivos secundarios: [3-4 secundarios separados por comas].
   - Cada KPI tiene una columna 'Por qué lo medimos' en lenguaje claro: para que sepan qué decisión se toma con cada métrica, no solo cómo se calcula.
3. Subbanner verde: "KPIs principales del MVP"
4. Tabla 4 columnas: KPI | Qué mide | Cómo se mide | Por qué lo medimos
5. Bloque feedback
6. Page break

### Reglas
- Mínimo 5 KPIs, máximo 8
- La columna "Por qué lo medimos" es OBLIGATORIA y va en lenguaje cliente-facing
  (no técnico). Ejemplos: "Es el objetivo #1 del agente. Si baja, hay que revisar
  pitch o copys." NO: "Métrica primaria del modelo."
- Anchos: 3.2 | 3.8 | 4.0 | 5.0 cm

---

## SECCIÓN 4 — AUTONOMÍA DEL AGENTE

### Composición
1. Banner oscuro: "3. AUTONOMÍA DEL AGENTE"
2. Párrafo introductorio (1 línea): "Qué cosas puede hacer el agente solo, y qué cosas NUNCA hace sin un humano."
3. Tabla 1×2 (UNA tabla con 2 celdas grandes — NO usar tablas anidadas):
   - Celda izquierda: fondo verde pálido, borde izquierdo verde grueso
     - Título: "✅  PUEDE HACER" (verde, 13pt, bold)
     - Bullets con palabra clave en bold + resto en peso normal
   - Celda derecha: fondo rojo pálido, borde izquierdo rojo grueso
     - Título: "❌  NUNCA HACE SOLO"
     - Bullets con misma estructura
4. Bloque feedback
5. Page break

### Reglas
- Mínimo 8 ítems en cada columna, máximo 15
- Las palabras clave (primeras 2-4 palabras del bullet) van en BOLD
- Ancho de cada celda: 8.5 cm

---

## SECCIÓN 5 — EMBUDOS

### Composición
1. Banner morado: "4. EMBUDOS — los N procesos del agente"
2. Card explicativa "EL PORQUÉ DE LOS N EMBUDOS" con 3 bullets:
   - El agente atiende N procesos paralelos. Una misma persona puede pasar por más de uno.
   - La variable proceso_actual identifica cuál está activo en cada momento.
   - Cada embudo tiene su propio recorrido de etapas, su propio color, y su propia lógica de seguimiento.
3. **Gráfico 1: Mapa de Embudos** (PNG, ancho 16cm, centrado)
4. Subbanner morado: "Etapas detalladas por embudo"
5. Para cada embudo, un párrafo: nombre del embudo en bold con color del proceso, seguido de la cadena de etapas separadas por flechas `→`
6. Bloque feedback
7. Page break

### Reglas
- Cantidad de embudos: depende del cliente (típico 3-5)
- Cada embudo tiene SU color del proceso (Venta=verde, Soporte=rojo, FAQ=azul, etc.)
- Las etapas se muestran como cadena: `etapa1 → etapa2 → etapa3 → etapa_final`

---

## SECCIÓN 6 — VARIABLES

### Composición
1. Banner azul: "5. VARIABLES — los datos que captura el agente"
2. Card explicativa "QUÉ HACE EL AGENTE CON LAS VARIABLES" con 3 bullets:
   - Las variables son los 'casilleros' que el agente completa automáticamente durante la conversación.
   - Permiten que el equipo [cliente] filtre, segmente y entienda a cada lead sin tener que leer el chat completo.
   - Hay N variables en total: M transversales (siempre se llenan), K de handoff (cuando hay que derivar), L de estado (solo se llena la del proceso activo).
3. **Gráfico 2: Overview Variables** (PNG, 16cm)
4. Subbanner azul: "Variables transversales (N) — se llenan siempre"
5. Tabla 3 columnas: Variable | Para qué sirve | Valores posibles
6. Subbanner morado: "Variables de handoff y priorización (N) — se llenan al derivar"
7. Tabla 3 columnas igual estructura (tipo_derivacion, severidad_caso típicamente)
8. Subbanner verde: "La regla de oro de variables de estado"
9. Párrafo italic gris explicando: "Cada variable estado_X solo se completa cuando proceso_actual=X..."
10. **Gráfico 3: Arquitectura Variables (router)** (PNG, 16cm)
11. **Card EJEMPLO PARA QUE SE ENTIENDA** con storytelling:
    - Título bold: "Imaginate que llega [Nombre ficticio] por [canal]:"
    - Frase italic con ejemplo de mensaje del usuario
    - "El agente, sin que se entere, llena estos casilleros:"
    - 5 bullets con `variable = valor`
    - Frase final con "Resultado:" en bold verde explicando qué información tiene ahora el equipo
12. Bloque feedback
13. Page break

### Reglas
- Persona ficticia con nombre concreto (Juan, María, etc.) — no genérico
- El ejemplo debe disparar al menos 5 variables (cubrir transversales)
- La columna "Valores posibles" lista los valores separados por `·` (punto medio)

---

## SECCIÓN 7 — SMART TAGS

### Modelo vigente: una tag por dimensión: estadío + tipo de usuario + prioridad opcional
Ver SECCIÓN 0 del SKILL.md. Cada lead muestra 2 Smart Tags de un vistazo:
ESTADÍO (etapa del embudo) + TIPOLOGÍA (categoría más fuerte). Opcional 3ª de
PRIORIDAD combinable. Las etapas de embudo SON tags.

### Composición
1. Banner naranja: "6. SMART TAGS — lo que se ve de cada lead en el panel"
2. Card explicativa "EL PORQUÉ DE LAS SMART TAGS" con 3 bullets:
   - Cada lead muestra dos Smart Tags de un golpe de vista: su estadío (en qué
     etapa del embudo está) y su tipología (qué clase de lead es). Así el equipo
     sabe, sin abrir el chat, dónde está parado y de qué tipo es.
   - El estadío lo maneja el embudo (las etapas de la sección 4). La tipología
     es la categoría más fuerte que diferencia al lead.
   - Sumamos [#tag_prioridad] como marca de prioridad, que se combina con
     cualquier tipología (un lead puede ser X Y prioritario a la vez).
3. **Gráfico 4: Overview Smart Tags** (PNG, 16cm)
4. Subbanner naranja: "Smart Tags de tipología — visibles siempre"
5. Tabla 3 columnas: Smart Tag | Cuándo se asigna | Acción que dispara
   - Cada tipología (ej: #inversor, #uso_propio, #inmobiliaria). Marcar cuáles
     son "solo visibilidad" y cuáles disparan acción (ej: #inmobiliaria apaga el
     asistente y deriva).
6. Subbanner naranja: "Smart Tag de prioridad — se combina con la tipología"
7. Tabla 3 columnas igual estructura para la tag de prioridad
8. **Cuadro "Explicado:" de cómo se leen las 2 tags juntas** (obligatorio — un
   lead "En Conversación + #inversor + #contacto_vip" le dice todo al equipo sin
   abrir el chat). Ver `cuadros_explicados.md`.
9. Bloque feedback
10. Page break

### Reglas
- El estadío NO se lista como tabla aparte acá — vive en la sección 4 (Embudos).
  Acá se listan las tipologías y la prioridad.
- No diseñar tags con alta similitud semántica (regla anti-confusión)
- Una tag se crea solo si se ve de un vistazo o dispara una acción concreta
- El cuadro "Explicado: cómo se leen las 2 tags juntas" es OBLIGATORIO

---

## SECCIÓN 8 — 3 ESCENARIOS DE EJEMPLO

### Composición
1. Banner verde: "7. 3 ESCENARIOS DE EJEMPLO — el agente en acción"
2. Card explicativa "POR QUÉ MOSTRAMOS 3 ESCENARIOS" con 3 bullets:
   - Para que se entienda cómo funciona todo junto (embudos + variables + smart tags + acciones), armamos 3 escenarios concretos.
   - Cada uno cubre un proceso distinto: [Escenario 1 nombre], [Escenario 2 nombre], [Escenario 3 nombre].
   - Los 3 muestran el mismo patrón: mensaje del usuario → proceso identificado → variables capturadas → smart tag → 3 acciones del agente.
3. Subbanner verde: "Escenario 1 — [título caso típico de venta]"
4. **Gráfico 5a** (PNG, 15cm), page break
5. Subbanner rojo: "Escenario 2 — [título caso de soporte/error]"
6. **Gráfico 5b** (PNG, 15cm), page break
7. Subbanner morado: "Escenario 3 — [título caso B2B / partnership / fuera de perfil]"
8. **Gráfico 5c** (PNG, 15cm)
9. Bloque feedback (al final de los 3)
10. Page break

### Reglas
- Los 3 escenarios DEBEN cubrir 3 procesos DISTINTOS para mostrar el espectro
- Recomendado: 1 caso típico de venta + 1 caso de error/soporte (que dispare push 24/7) + 1 caso B2B/partnership
- Mismo template visual para los 3 (ver skill aurea-crm-graphics)

---

## SECCIÓN 9 — SEGUIMIENTOS

### Composición
1. Banner naranja: "8. SEGUIMIENTOS — los N follow-ups del MVP"
2. Card explicativa "CÓMO FUNCIONAN LOS SEGUIMIENTOS" con 3 bullets:
   - El agente puede mandar mensajes automáticos al lead días después si la conversación quedó abierta.
   - Para que un seguimiento se dispare, tienen que coincidir 4 condiciones al mismo tiempo. Si falta una, no se manda.
   - N follow-ups en total: [breakdown por tipo].
3. Subbanner naranja: "Las 4 condiciones que tienen que coincidir"
4. **Gráfico 6: Fórmula Seguimiento** (PNG, 15cm), page break
5. Subbanner naranja: "Distribución de los N seguimientos por proceso"
6. **Gráfico 7: Overview Seguimientos (con ramas a 24h y 72h)** (PNG, 16cm)
7. Subbanner verde: "Texto literal de los N seguimientos de [proceso principal]"
8. Párrafo italic gris explicando que el placeholder `(emoji de saludo)` es para que el cliente decida el emoji final
9. Tabla 3 columnas: Seguimiento | Disparador | Mensaje literal
10. Subbanner naranja: "Los N seguimientos contextuales"
11. Tabla 3 columnas igual estructura, con ejemplos de mensajes (no literales)
12. Bloque feedback
13. Page break

### Reglas
- Cantidad de seguimientos: típico 3-7 en MVP
- Distinguir CLARAMENTE seguimientos literales (texto fijo) vs contextuales (el agente arma el mensaje)
- En DOCX cliente-facing: usar `(emoji de saludo)` como placeholder
- En el prompt: usar el emoji real (👋, ✅)

---

## SECCIÓN 10 — REGLAS DE DISTRIBUCIÓN

### Composición
1. Banner morado: "9. REGLAS DE DISTRIBUCIÓN — quién recibe qué caso"
2. Card explicativa "EL AGENTE NUNCA DERIVA EN VACÍO" con 3 bullets:
   - Antes de pasar el chat a un humano, el agente califica el caso: identifica qué tipo de derivación corresponde y qué severidad tiene.
   - Eso es lo más importante de todo este sector: el equipo humano recibe el caso ya con contexto.
   - Hay N tipos de derivación posibles, cada uno va a un área distinta del equipo [cliente].
3. **Gráfico 8: Derivación** (PNG, 15cm), page break
4. Subbanner rojo: "Casos críticos que generan notificación 24/7"
5. Párrafo italic gris explicando que requiere plan Pro/Enterprise
6. **Gráfico 9: Notificaciones Urgentes 24/7** (PNG, 15cm)
7. Subbanner cyan cliente: "Tabla para que [cliente] complete los responsables por área"
8. Párrafo italic gris pidiendo que completen las columnas vacías
9. Tabla 5 columnas: Cuándo se dispara | tipo_derivacion | severidad | Prometheo o WhatsApp | Responsable
   - Filas pre-llenadas con los casos típicos
   - Columnas "Prometheo o WhatsApp" y "Responsable" en BLANCO con checkboxes y líneas
10. Bloque feedback
11. Page break

### Reglas
- La columna "Cuándo se dispara" en lenguaje cliente-facing
  ("Usuario quiere descargar pero pide humano"), NO sintaxis técnica
  ("intencion_principal=informarse + tipo_derivacion=comercial")
- Las columnas vacías para que cliente complete son OBLIGATORIAS
- Mínimo 6 casos pre-llenados, máximo 12

---

## SECCIÓN 11 — PENDIENTES DEL EQUIPO + PRÓXIMOS PASOS

### Composición de "Pendientes"
1. Banner naranja: "10. PENDIENTES DEL EQUIPO [CLIENTE]"
2. Párrafo introductorio (1-2 líneas)
3. Subbanner rojo: "Críticos — sin esto no podemos avanzar"
4. Lista con checkbox `☐` rojo para cada item crítico
5. Subbanner naranja: "Normales — pueden cerrarse en paralelo"
6. Lista con checkbox `☐` naranja para cada item normal
7. Bloque feedback
8. Page break

### Composición de "Próximos Pasos"
1. Banner morado: "11. PRÓXIMOS PASOS"
2. Párrafo: "Una vez aprobado este documento, así avanzamos:"
3. 6 cards horizontales (uno por paso):
   - Borde izquierdo grueso color del paso (rotando entre verde, naranja, azul, morado)
   - Título bold con color del paso
   - Descripción
   - "Responsable: [equipo o consultor]" en italic gris
4. Pie centrado: "— FIN DEL DOCUMENTO —" + "AUREA Hub × Prometheo · [cliente] · Versión final · Modelo conceptual v[N]"

### Reglas
- Paso 1 SIEMPRE incluye `[PLACEHOLDER_LINK_DRIVE]` para que se reemplace
- Pasos típicos: Completar pendientes en Drive → Implementación en Prometheo → Testing inhouse → Capacitación al equipo → Go-Live → Monitoreo 15 días post-Go-Live

---

## CHECKLIST FINAL DEL DOCX

Antes de entregar, verificar:

- [ ] 11 secciones en el orden correcto
- [ ] Cada sección tiene banner + card explicativa + gráfico + tabla + ejemplo (cuando aplica) + feedback
- [ ] Los 9 gráficos transversales están embebidos
- [ ] El cuadro "Explicado: #seguimiento_activo" está en sección 7
- [ ] La tabla de Reglas de Distribución tiene columnas vacías
- [ ] Próximos Pasos tiene placeholder del Drive
- [ ] OOXML pasa validación
- [ ] No hay tablas anidadas (max_depth = 1)
- [ ] styles.xml fue reemplazado por minimal
- [ ] Peso < 800 KB
