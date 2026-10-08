---
consultar-cuando: cierre de Etapa 2, pasaje a Etapa 3, cargar Prometheo de un cliente nuevo
disparadores: "guía de implementador", "cargar Prometheo", "configurar el CRM", "pasar a Etapa 3"
fuente-única-de: estructura y reglas de la Guía de Implementador (familia 7 de outputs)
combina-con: embudos-y-tags, framework-seguimientos, 08-reglas-integracion-catalogo, el rubro correspondiente
---

# 06 — Estructura de la Guía de Implementador

**Los 10 bloques de la guía operativa para configurar Prometheo.**

---

## Qué es la Guía de Implementador

Es el documento que recibe el implementador (vos o un consultor jr) para configurar Prometheo paso a paso después de que el cliente aprueba el DOCX y el Prompt en Etapa 2.

**Audiencia:** consultor AUREA que ejecuta la configuración. **Es técnica**, asume que conoce Prometheo.

**Diferencia con el DOCX cliente-facing:**

| Aspecto | DOCX cliente-facing | Guía de Implementador |
|---|---|---|
| Audiencia | Cliente final (no técnico) | Consultor AUREA (técnico) |
| Tono | Visual, narrativo, gráficos | Operativo, checklists, comandos |
| Lenguaje | Cliente-friendly | Sintaxis Prometheo |
| Formato | DOCX con feedback inline | Markdown plano |
| Cuándo se entrega | Ronda 1 (antes de aprobación) | Ronda 2 (después de aprobación) |

**Razón de separar en 2 documentos:** el cliente no entiende la jerga técnica y se confunde. El implementador no necesita los gráficos visuales y los considera ruido.

---

## Los 10 bloques de la guía

### Bloque 1 — Información del cliente

Datos generales del proyecto para que el implementador tenga contexto al abrir la guía.

```markdown
## 1. Información del cliente

- Nombre: [CLIENTE]
- Rubro: [Rubro]
- Plan Prometheo contratado: [Basic / Pro / Enterprise]
- Fecha de Go-Live planificada: [fecha]
- Responsable AUREA: Valentín Zas
- Responsable cliente: [Nombre · Mail · Tel]
- Drive con materiales del cliente: [link]
- URL del CRM Prometheo: [URL específica del cliente]
```

### Bloque 2 — Setup inicial de la cuenta Prometheo

Cosas a configurar antes de cargar variables, tags y follow-ups.

```markdown
## 2. Setup inicial

### 2.1. Acceso a la cuenta
- Credenciales: [referencia al Doc 3 — Accesos]
- Verificar que el plan contratado sea: [Pro / Enterprise]

### 2.2. Conexión del canal principal
- WhatsApp Business API: número [+54 9 ...]
- Status: ☐ Pendiente · ☐ Conectado · ☐ Verificado

### 2.3. Conexión de canales secundarios (si aplica)
- Instagram: ☐ Pendiente · ☐ Conectado
- Mail: ☐ Pendiente · ☐ Conectado
- Portales (Zonaprop, etc): ☐ Pendiente · ☐ Conectado

### 2.4. Integraciones externas
- Tokko: ☐ Pendiente · ☐ Conectado
- PrestaShop: ☐ Pendiente · ☐ Conectado
- Google Calendar: ☐ Pendiente · ☐ Conectado
```

### Bloque 3 — Configuración de variables

Listado de todas las variables a crear en Prometheo con su tipo y prompt de extracción.

```markdown
## 3. Variables

### Orden de creación
Crear las variables en este orden para evitar dependencias rotas:
1. Variable router: proceso_actual
2. Variables transversales (canal, tipo_usuario, etc.)
3. Variables de estado por proceso (estado_venta, estado_soporte, etc.)
4. Variables operativas (severidad_caso, tipo_derivacion)
5. Variables del rubro específico

### Tabla de variables

| # | Nombre | Tipo | Valores | Prompt de extracción |
|---|---|---|---|---|
| 1 | proceso_actual | Opciones | venta · soporte · faq · derivacion | "Guardá el proceso que corresponda según el tema principal de la conversación. Solo puede tomar los valores listados." |
| 2 | canal | Opciones | whatsapp · instagram · mail · web · referido | "Guardá el canal por donde entró el usuario." |
| ... | ... | ... | ... | ... |

### Checklist por variable
Para cada variable, verificar:
☐ Nombre exactamente igual al definido (case-sensitive)
☐ Tipo correcto
☐ Valores cerrados (si es Opciones) sin tipos
☐ Prompt de extracción cargado y testeado
```

### Bloque 4 — Configuración de Smart Tags

Las 2 tags base con su disparador y acción.

```markdown
## 4. Smart Tags

### Tag 1: #seguimiento_activo

- Disparador (prompt en Prometheo):
  "Asigná esta tag cuando [condiciones específicas del cliente]:
  - El lead recibió toda la info disponible
  - Todavía no aceptó la conversión final
  - La conversación sigue activa"
- Acción configurada: habilitar follow-ups asociados

### Tag 2: #derivar_a_humano

- Disparador (prompt en Prometheo):
  "Asigná esta tag cuando detectes alguno de estos casos:
  - El lead pide hablar con humano explícitamente
  - El caso requiere [casos rubro-específicos]
  - [...]"
- Acción configurada: apagar agente + notificar al área correspondiente
- Variable que SIEMPRE acompaña: tipo_derivacion
```

### Bloque 5 — Configuración de embudos / etapas

Cómo configurar las etapas dentro de Prometheo para cada embudo.

```markdown
## 5. Embudos y etapas

### Embudo 1: Venta
Etapas (en orden):
1. Consulta recibida
2. Calificando
3. Info enviada
4. Visita agendada
5. Visita realizada
6. Reserva
7. Cerrado (ganado / perdido)

### Embudo 2: Soporte
[...]

### Reglas de movimiento entre etapas
- Etapa 1 → 2: cuando se identifica `proceso_actual = venta`
- Etapa 2 → 3: cuando el agente envía el material
- Etapa 3 → 4: cuando el equipo humano marca manualmente "visita_agendada"
- [...]
```

### Bloque 6 — Configuración de seguimientos

Cómo cargar cada follow-up con sus 4 condiciones.

```markdown
## 6. Seguimientos

### Follow-up 1 — [Nombre]

Configuración en Prometheo:
- Tag activadora: #seguimiento_activo
- Condición 1 (variable router): proceso_actual = venta
- Condición 2 (variable estado): estado_venta = info_enviada
- Condición 3 (tiempo): 24 horas sin respuesta del usuario
- Horario de envío: L-V de [9 a 18hs / etc]
- Mensaje:
  "[Texto literal copiado del prompt sección 13]"

- Cancelación automática:
  - Si el usuario responde
  - Si aparece #derivar_a_humano

### Follow-up 2 — [Nombre]
[...]
```

### Bloque 7 — Configuración de Reglas de Distribución

La tabla de routing por `tipo_derivacion` con responsables ya confirmados por el cliente.

```markdown
## 7. Reglas de Distribución

### Tabla de routing por tipo_derivacion

| tipo_derivacion | Canal de notificación | Responsable | Contacto |
|---|---|---|---|
| comercial | Prometheo | Sebastián Mato | seba@empresa.com · +54 9 11 ... |
| soporte | Prometheo + WhatsApp | María García | maria@empresa.com · +54 9 11 ... |
| ... | ... | ... | ... |

### Notificaciones urgentes (severidad_caso = alta)
- Plan Prometheo requerido: Pro o Enterprise
- Casos que disparan push 24/7: [lista específica]
- Responsable de notificación 24/7: [Nombre · WhatsApp]
```

### Bloque 8 — Carga del prompt del agente

Pasos para cargar el prompt en Prometheo.

```markdown
## 8. Carga del prompt

### 8.1. Archivo de origen
- Path: [PROMPT_V1.md del Drive de Trabajo Interno AUREA]
- Versión a cargar: V1 (la más reciente aprobada)

### 8.2. Pasos en Prometheo
1. Acceder a Configuración del agente
2. Pegar el prompt completo (las 14 secciones + 3 anexos)
3. Configurar el nombre del agente: [NOMBRE]
4. Configurar el modelo: GPT-4 / Claude / [el que use Prometheo por default]
5. Guardar y testear con 1 mensaje de prueba

### 8.3. Adjuntos al asistente
Archivos PDF a cargar como adjuntos del asistente (se envían con "/"):

| Archivo | Producto / categoría |
|---|---|
| ficha-microcemento-premium.pdf | Microcemento Premium |
| ficha-cemento-alisado.pdf | Cemento Alisado Industrial |
| brochure-general.pdf | General de la marca |
```

### Bloque 9 — Testing inhouse

Casos de prueba a correr antes del Go-Live.

```markdown
## 9. Testing inhouse

### Escenarios obligatorios a probar (mínimo 15 conversaciones)

#### Escenario 1: lead nuevo del proceso principal
- Simular: mensaje inicial con poca info
- Verificar: agente identifica proceso_actual correctamente
- Verificar: agente captura variables transversales
- Verificar: agente pide info faltante sin sonar a formulario

#### Escenario 2: lead fuera de horario
- Simular: mensaje a las 22hs un viernes
- Verificar: agente responde inmediatamente
- Verificar: no se dispara follow-up hasta el lunes 9hs

#### Escenario 3: lead B2B
- Simular: mensaje "te consulto desde una empresa"
- Verificar: agente identifica tipo_usuario = b2b
- Verificar: se dispara #derivar_a_humano con tipo_derivacion correcto

#### Escenario 4: caso crítico (si aplica)
- Simular: mensaje con palabras clave de severidad alta
- Verificar: severidad_caso = alta
- Verificar: push 24/7 al responsable
- Verificar: notificación correcta en el WhatsApp/casillero correspondiente

[... mínimo 11 escenarios más adaptados al cliente]

### Reporte de testing
Documentar en hoja de cálculo:
- # de escenario · descripción · resultado esperado · resultado obtenido
  · status (OK / FALLA / AJUSTE) · acción si falla
```

### Bloque 10 — Capacitación al equipo del cliente

Plan de capacitación post-testing y pre-Go-Live.

```markdown
## 10. Capacitación

### Duración recomendada
- 90 minutos en 1 sesión única (síncrona, videollamada)

### Audiencia
- Responsables de recibir leads derivados (típicamente 2-5 personas)
- Equipo comercial completo si aplica

### Agenda de la sesión

#### Minuto 0-15: Qué es Prometheo
- Concepto de agente IA + CRM integrado
- Diferencia con un chatbot tradicional
- Por qué hay variables y tags

#### Minuto 15-45: Cómo leer un lead en Prometheo
- Dónde se ven las variables capturadas
- Cómo interpretar las Smart Tags
- Cómo saber en qué etapa del embudo está el lead

#### Minuto 45-70: Workflow operativo del equipo humano
- Qué hacer cuando llega una notificación de derivación
- Cómo retirar la Smart Tag #seguimiento_activo cuando se toma el caso
- Cómo cerrar un caso en el embudo

#### Minuto 70-90: Preguntas y casos reales
- Mostrar conversaciones reales de testing
- Resolver dudas del equipo
- Acordar canal de soporte post-Go-Live (typically WhatsApp directo a Valentín)

### Materiales para la capacitación
- Presentación corta (5-7 slides)
- Acceso a la cuenta Prometheo del cliente
- 3-5 conversaciones de testing como ejemplo
```

---

## Anexo — Plan de monitoreo post Go-Live

Bloque adicional para los primeros 15 días después del lanzamiento.

```markdown
## Anexo — Monitoreo 15 días post Go-Live

### Días 1-3: monitoreo intensivo
- Revisar el 100% de las conversaciones
- Identificar regresiones del prompt
- Ajustes finos del prompt (V2) si aparecen patrones erróneos

### Días 4-7: monitoreo selectivo
- Revisar 30-50% de las conversaciones
- Foco en casos derivados y casos de severidad alta
- Reporte semanal de KPIs al cliente

### Días 8-15: monitoreo de calidad
- Revisar sample aleatorio (10-20%)
- Validar que los KPIs se mantienen en target
- Reporte semanal de KPIs

### Día 15 — Evaluación conjunta
- Revisión del prompt V2 (si se modificó)
- Decisión sobre Fase 2: qué funcionalidades sumar
- Cierre formal de Etapa 3
```

---

## Validación final de la Guía

Antes de entregar la Guía al implementador, verificar:

| Check | Cómo verificar |
|---|---|
| Información del cliente completa | Bloque 1 con todos los datos |
| Plan Prometheo del cliente identificado | Bloque 1 y 2 coinciden |
| Variables tienen prompt de extracción cargado | Bloque 3 |
| Smart Tags tienen disparador específico al rubro | Bloque 4 |
| Embudos tienen etapas claras | Bloque 5 |
| Follow-ups tienen las 4 condiciones explícitas | Bloque 6 |
| Tabla de Reglas de Distribución completa por cliente | Bloque 7 |
| Prompt y adjuntos identificados con path exacto | Bloque 8 |
| Mínimo 15 escenarios de testing | Bloque 9 |
| Agenda de capacitación con horarios | Bloque 10 |
| Plan de monitoreo 15 días | Anexo |

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Operativa Etapa 2 | `01-operativa-y-decisiones.md` |
| Reglas Diseño de Prometheo by AUREA | `03-reglas-diseno-prometheo-by-aurea.md` |
| Estructura Prompt | `05-estructura-prompt-agente.md` |
| Convenciones DOCX | `04-convenciones-docx-cliente.md` |
| Skill maestra | `../../02-skills/02-ETAPA2/prometheo-etapa2-design/SKILL.md` |

---

## Reglas duras de formato (del generador, no negociables)

> Validado en tres casos reales de producción (EDFAN, G&D, BETROX). El generador que produce la
> Guía a partir del diseño de CRM (Doc 1/DDV) sigue estas reglas de formato SIEMPRE:

1. **Vertical y angosto.** Nada de tablas anchas. Cada ítem es un bloque que entra en pantalla,
   pensado para copiar y pegar directo a Prometheo.
2. **Opciones en bloque de código**, una debajo de la otra, sin viñetas ni puntitos.
3. **El prompt de extracción de cada variable va pegado a sus opciones**, en la misma unidad
   visual. Nunca en una sección aparte.
4. **Nombres de variables y tags en formato natural**, mayúscula por palabra, SIN guion bajo ni
   numeral (`Tipo Perfil`, no `tipo_perfil`). El guion bajo con prefijo `var_` es solo encabezado
   de columna del Sheet de importación de contactos — nunca el nombre que se carga en Prometheo.
5. **Valores en lenguaje natural**, no en código: genéricos con mayúscula solo en la inicial
   (`Entrega inmediata`, no `entrega_inmediata`); nombres propios con su grafía real
   (`San Telmo`, `VERVÉ CHACARITA`). **Regla de oro:** el prompt del agente y el CRM tienen que
   hablar el mismo idioma de valores — los strings que escribe el agente son idénticos a las
   opciones cargadas en la variable y a los de la base importada.
6. Voseo rioplatense. AUREA siempre en mayúsculas. Cero em-dash. Sin emojis en el cuerpo técnico.
7. **Orden de carga fijo:** Variables → Smart Tags → Embudos → Import de contactos → Prompt →
   Testing → Go-Live. (BETROX suma Seguimientos y Plantillas entre Embudos y Distribución, según
   la complejidad del cliente; el orden relativo Variables-antes-que-Tags-antes-que-Embudos nunca
   cambia.)

## Reglas de diseño de variables (aplicar al generar, no solo al formatear)

Estas reglas se aplican mientras se PIENSA el diseño, no solo al momento de escribirlo:

- **Variable vs Smart Tag:** si el valor reemplaza al anterior es Variable; si se acumula es
  Smart Tag. Nunca mezclar.
- **Selección única = valores mutuamente excluyentes.** Test rápido: ¿un mismo lead puede ser dos
  de estos valores a la vez? Si sí, no van en el mismo eje. El arreglo suele ser reemplazar la
  etiqueta de rol por su sentido, no partir en dos variables (ver Frente B en
  `embudos-y-tags.md`: `Tipo Perfil` reemplazó a `Tipo Contacto` + `Objetivo Búsqueda`).
- **Selección múltiple** solo cuando el lead legítimamente tiene varios valores a la vez (ej.
  `Linea Producto`, `Producto Interes` en BETROX). Se importan separados por pipe, igual que las
  Tags multi-valor.
- **Derivable no se almacena:** si un dato sale de otro, su función va al comportamiento del
  prompt, no a un campo aparte.
- **Padre / hijo:** una variable puede gobernar si otra se llena. El vacío de la hija es N/A
  legítimo, no dato faltante; no se fuerza. (Patrón confirmado en tres casos: G&D `Inversión
  Finalidad` solo si `Tipo Perfil`=Inversión; BETROX `Tipo Profesional` solo si `Tipo
  Cliente`=Profesional.)
- **Naming:** la primera palabra fija el dominio (`inversion_finalidad`, no
  `finalidad_inversion`). Respetar prefijos de familia.
- **Producto/condición externa vs interés del lead — separar siempre.** Un atributo que vive en
  el catálogo (ej. que un producto esté en Outlet) NO es lo mismo que el interés del lead por esa
  categoría. Van en dos lugares distintos: la condición del producto se consulta en runtime a la
  integración; el interés del lead se guarda en una variable propia (`Outlet Interes`). No
  mezclar nunca los dos.
- **Inteligencia comercial — patrón dual, familia de 6 variables (ampliada en BETROX):** por cada
  insight, una variable Opciones (para contar y rankear) más una Texto largo (frase literal o
  detalle). La familia base es Objeción Principal + Frase Literal y Pedido Fuera de Catálogo +
  Detalle; BETROX agregó **Dolor Principal** (el problema de fondo detrás de la compra) y
  **Disparador Compra** (qué destrabaría la decisión), ambas Texto largo sin par Opciones porque
  son demasiado variables para categorizar. La familia completa de IC queda en 6 variables.
  Taxonomía de Objeción Principal idéntica entre clientes del mismo vertical para poder cruzar
  datos; el cliente puede tener variables extra propias sin romper esa paridad.
- **Numeración temática, no técnica:** variables numeradas por cercanía de tema (3b, 3c, 3d) no
  implican subordinación técnica en Prometheo — es solo convención de lectura de la Guía.

## Casos reales de referencia (validados en producción)

Tres implementaciones completas documentan cómo la Guía se adapta a cada integración y a cada
modelo de equipo. Usarlas como molde antes de diseñar una nueva:

| | EDFAN Real Estate | G&D Developers | BETROX |
|---|---|---|---|
| **Agente** | Martina | Veronica / Maia | Catalina |
| **Integración** | Tokko | Google Sheets + Tokko | PrestaShop |
| **Agendamiento** | Autónomo (Google Calendar) | NO autónomo (equipo confirma slot) | Autónomo (Google Calendar) |
| **Modelo de perfil** | Tipo Contacto + Objetivo Búsqueda (previo a la corrección) | `Tipo Perfil` único + `Inversión Finalidad` hija | `Tipo Cliente` (5 valores) + `Tipo Profesional` hija |
| **Distribución** | Multi-persona por especialidad (Sebastián/Thiago/Evelyn) | Multi-persona por zona (Celeste/Kevin/Fernanda) | **Destino único** (todo a Mariana) |
| **B2B / co-diseño** | Embudo 3 propio (Gestión Inmobiliarias) | Embudo 3 propio (Gestión Inmobiliarias) | **Sin embudo propio** — variables `Modo Trabajo` + `Referencias Recibidas`, mismo Embudo 1 |
| **Variables** | 18 | 16 | 23 (13 transversales + handoff + 6 de IC) |
| **Testing** | 17 escenarios | 18 escenarios | 16 escenarios |

**Por qué B2B a veces necesita embudo propio y a veces no** (decisión de diseño, no regla fija):
en real estate el lead B2B es una inmobiliaria intermediaria que representa a un tercero — el
modo de trabajo con ella es estructuralmente distinto (nunca se le pide el contacto del cliente
final, nunca se le vende directo) y eso amerita un embudo con sus propias etapas. En mobiliario,
un profesional o un municipio que trae un proyecto propio (co-diseño) sigue siendo un lead directo
que recorre el mismo embudo de siempre — lo único que cambia es que trae material propio y el
modo de trabajo es distinto, y eso se captura con una variable (`Modo Trabajo`: Catálogo /
Co-diseño) más la tag de tipología que ya notifica. **Regla de decisión:** si el B2B implica una
intermediación real hacia un tercero, embudo propio; si es un lead directo con un modo de trabajo
distinto, variables + tags alcanza. Esto se define en discovery, no se asume por rubro.

## Para profundizar (ampliado)

| Tema | Archivo |
|---|---|
| Operativa Etapa 2 | `01-operativa-y-decisiones.md` |
| Reglas Diseño de Prometheo by AUREA | `03-reglas-diseno-prometheo-by-aurea.md` |
| Estructura Prompt | `05-estructura-prompt-agente.md` |
| Convenciones DOCX | `04-convenciones-docx-cliente.md` |
| Modelo de tags y variables de perfil (Tipo Perfil + hija) | `embudos-y-tags.md` |
| Sistema completo de mensajería (5 mecanismos) | `framework-seguimientos.md` |
| Doctrina por integración (Sheets/Tokko/PrestaShop) + 3 sistemas de placeholder | `08-reglas-integracion-catalogo.md` |
| Restricciones de plataforma (colores, acciones, planes) | `restricciones-plataforma-prometheo.md` |
| Skill maestra | `../../02-skills/02-ETAPA2/prometheo-etapa2-design/SKILL.md` |

---

## Estructura canónica de la Guía de Implementador (8 secciones)

> Validada en las tres guías reales (EDFAN, G&D, BETROX). Es el molde: toda Guía de Implementador
> tiene estas secciones, en este orden, respetando el orden de carga de Prometheo. Cada cuenta la
> llena con sus datos; la estructura no cambia entre cuentas ni entre rubros.

1. **Datos de la cuenta y setup.** Plan de Prometheo (con qué acciones requieren Enterprise),
   canales conectados, integración de datos vivos (Tokko / Sheets / PrestaShop), agendamiento
   (Calendar o no), y los pendientes de plataforma con ITESA para el arranque.
2. **Variables (en orden de carga).** Cada una con: Nombre (formato natural, mayúscula por
   palabra, sin guion bajo), Tipo (Opciones única/múltiple, Texto, Texto largo, Precio, Fecha),
   Opciones en bloque, y el criterio del prompt de extracción. Las de inteligencia comercial
   marcadas aparte. Regla de captura al pie: pasiva, vacío es válido, registrar no es decir.
3. **Smart Tags.** Por dimensión (estadío / tipología / prioridad): valores, color, acción
   (Notificar / Apagar / Reactivar), y el mini-prompt de descripción de cada tag.
4. **Embudos.** Cada embudo con sus etapas en orden y su "Descripción para la IA". Los saltos
   entre embudos.
5. **Mensajería / Import de contactos** (según qué tenga la cuenta). Seguimientos, recordatorios,
   plantillas de Meta; y/o el import de base histórica con qué se saneó y qué defaults NO se
   promovieron.
6. **Distribución / derivación.** Destino único o multi-persona; a quién y con qué criterio
   (roles, no solo nombres); los procedimientos de handoff con sus prohibiciones (B2B, VIP).
7. **Testing.** Los escenarios críticos a correr antes de conectar canales, derivados de las
   reglas de esa cuenta (ver `guion-testing.md` para el método: primos, [PLATAFORMA], regresión).
8. **Pendientes y notas para ITESA.** Lo del prompt, lo de plataforma (donde está el ahorro de
   tokens y las config que dependen del proveedor), y los datos de negocio a confirmar con el
   cliente.

**Formato:** vertical y angosto, copy-paste, según las reglas duras de formato de arriba. La Guía
es un **entregable de cuenta** (instancia): esta estructura sube a la metodología, el contenido de
cada cuenta vive en su material, no en el ZIP. Ver la familia 7 en `00-OUTPUTS-POR-ETAPA.md`.
