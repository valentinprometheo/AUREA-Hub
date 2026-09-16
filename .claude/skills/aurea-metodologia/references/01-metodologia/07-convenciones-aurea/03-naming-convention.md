# 03 — Naming Convention

**Convención de nombres para archivos, variables, tags, embudos y todo lo demás.**

---

## Por qué importa una naming convention

En un sistema con múltiples clientes, múltiples archivos, múltiples consultores: si cada uno nombra como quiere, en 3 meses no encontrás nada.

Una buena convención de nombres:
- Acelera la búsqueda
- Permite identificar el tipo de archivo a primera vista
- Evita conflictos entre clientes
- Facilita la generación automática de outputs (scripts, plantillas)

---

## Naming para archivos del CRM (Prometheo)

### Variables

**Convención:** `snake_case`

✅ Correcto:
- `proceso_actual`
- `tipo_usuario`
- `estado_venta`
- `proyecto_interes`

❌ Incorrecto:
- `procesoActual` (camelCase)
- `proceso-actual` (kebab-case)
- `Proceso Actual` (con espacios)
- `proceso_Actual` (mixto)

**Regla adicional:** los nombres son **descriptivos y cortos**. Si la variable necesita más de 3 palabras, probablemente está mezclando 2 conceptos.

```
✅  estado_venta
❌  estado_actual_del_proceso_de_venta
```

### Valores de variables tipo Opciones

**Convención:** `snake_case` también.

✅ Correcto:
- `venta · soporte · faq · derivacion`
- `whatsapp · instagram · mail · web`
- `1_amb · 2_amb · 3_amb · 4_amb`

❌ Incorrecto:
- `Venta · Soporte · FAQ` (mayúsculas inconsistentes)
- `1 ambiente · 2 ambientes` (con espacios)
- `1amb · 2amb` (sin separador, ambiguo)

### Smart Tags

**Convención:** `#snake_case` con prefijo `#`.

✅ Correcto:
- `#seguimiento_activo`
- `#derivar_a_humano`

❌ Incorrecto:
- `#Seguimiento_Activo` (mayúsculas)
- `#derivar-a-humano` (kebab)
- `derivar_a_humano` (sin prefijo)
- `#seg_act` (abreviado, no descriptivo)

### Embudos / Etapas

**Convención:** `snake_case` con verbos descriptivos.

✅ Correcto:
- `calificando · info_enviada · visita_agendada · visita_realizada`
- `consulta_recibida · respuesta_enviada · cerrada`

❌ Incorrecto:
- `1_calificando · 2_info_enviada` (números al inicio innecesarios)
- `pendiente · trabajando · listo` (poco descriptivos)
- `estado_1 · estado_2` (sin significado)

---

## Naming para archivos del proyecto del cliente

### Documentos en Drive

**Convención:** `[Cliente] - [Tipo de documento] - [versión opcional].extensión`

✅ Correcto:
- `G&D Developers - Diseño de CRM.docx`
- `MIA App - Prompt - V5.md`
- `BETROX - Guía para Implementador.md`
- `EDFAN Productos - Doc 1 Síntesis.md`

❌ Incorrecto:
- `mia_prompt_v5.md` (sin contexto del cliente)
- `Diseño CRM Final.docx` (sin cliente ni versión)
- `2026-05-15-MIA-prompt.md` (fecha al inicio, no es necesario)

**Excepción:** archivos internos AUREA que no son cliente-facing pueden usar formato más libre.

### Carpetas en Drive

**Convención:** estructura estándar por cliente.

```
[Cliente]/
├── Documentación / Accesos/
│   ├── Doc 3 - Accesos.md
│   ├── Contratos firmados.pdf
│   └── ...
└── Etapa 1 – DISCOVERY // Consultoría por AUREA Hub/
    ├── Conversaciones Reales/
    ├── Info General/
    ├── Listas de Precios/
    ├── Material Inmobiliarias/
    ├── Obras/Proyectos/
    └── Videos/
```

**Regla:** la estructura macro es **estandard para todos los clientes**, las subcarpetas pueden variar según el rubro.

### Archivos del consultor (markdown / docs internos)

**Convención:** descriptiva, en kebab-case si es markdown.

✅ Correcto:
- `g-d-developers-matching-difusion-v1.md`
- `betrox-discovery-doc1-sintesis.md`
- `audit-doc1-edfan-real-estate.md`

### Versiones

**Convención:** sufijo `V[N]` con mayúscula y número entero.

✅ Correcto:
- `V1`, `V2`, `V3`...
- `Prompt V5` (espacio entre nombre y versión)

❌ Incorrecto:
- `v1.0.0` (versionado semántico no aplica)
- `Final`, `Final2`, `FinalFinal` (clásico anti-patrón)
- `Borrador`, `Aprobado` (estado en el nombre, mejor por carpeta)

---

## Naming para archivos de la metodología AUREA

### Documentos en `01-metodologia/`

**Convención:** prefijo numérico + descripción en kebab-case.

✅ Correcto:
- `00-INDEX.md`
- `01-operativa-y-decisiones.md`
- `03-reglas-diseno-prometheo-by-aurea.md`

**Razón del prefijo numérico:** permite ordenar los archivos en el explorador de archivos según el orden de lectura recomendado, no según alfabético.

### Skills en `02-skills/`

**Convención:** `[scope]-[concepto].md` en kebab-case.

✅ Correcto:
- `prometheo-etapa2-design.md`
- `prometheo-crm-graphics.md`
- `prometheo-vertical-real-estate.md`
- `prometheo-vertical-mobiliario.md`

**Razón:** el prefijo indica el scope (aurea = AUREA-wide, prometheo = específico de Prometheo). El concepto va después.

### Templates

**Convención:** sufijo `-template` en kebab-case.

✅ Correcto:
- `README-cliente-template.md`
- `documento-cero-template.md`
- `docx-diseno-crm-template.md`

### Casos de referencia

**Convención:** prefijo `PROTOTIPO-` o `PLACEHOLDER-` según estado.

✅ Correcto:
- `PROTOTIPO-mia-app.md` (referente activo)
- `PROTOTIPO-betrox.md`
- `PLACEHOLDER-referente-prompt-02.md` (vacío, esperando contenido)

---

## Naming para placeholders en documentos

Cuando un documento tiene marcadores que se reemplazan después (links, nombres, fechas):

**Convención:** `[CORCHETES_EN_MAYUSCULAS_CON_GUION_BAJO]`

✅ Correcto:
- `[PLACEHOLDER_LINK_DRIVE]`
- `[NOMBRE_CLIENTE]`
- `[FECHA_GO_LIVE]`
- `[NOMBRE_AGENTE]`

❌ Incorrecto:
- `<<PLACEHOLDER>>` (sintaxis confusa)
- `{{placeholder}}` (jerga de templating engines, confunde al cliente)
- `XXX_LINK_XXX` (poco identificable)

**Razón:** los corchetes con mayúsculas son visualmente evidentes y nunca se confunden con contenido real.

---

## Naming para variables del rubro

Cuando creás una variable nueva para un rubro:

### Regla 1 — Descriptiva del concepto, no del cliente

✅ `proyecto_interes` (concepto)
❌ `gd_proyecto_interes` (con prefijo del cliente)

Razón: la variable se va a generalizar a otros clientes del mismo rubro.

### Regla 2 — Substantivos, no verbos

✅ `tipo_unidad`, `estado_venta`, `forma_de_pago`
❌ `comprar_unidad`, `vender_estado`

### Regla 3 — Plural solo si el campo acepta múltiples valores

- Si la variable es Opciones con 1 valor → singular: `proyecto_interes`
- Si la variable es Lista de valores → plural: `proyectos_interes` (raro en Prometheo)

### Regla 4 — Sin acentos ni caracteres especiales

✅ `tipo_operacion`, `producto_de_interes`
❌ `tipo_operación`, `producto_de_interés` (aunque el acento sea correcto en español)

**Razón:** los sistemas como Prometheo, Tokko, PrestaShop pueden tener problemas con acentos en nombres de variables. Mantener ASCII puro.

**Excepción:** los valores de las variables sí pueden tener acentos si son cadenas que el agente usa en mensajes al usuario.

---

## Naming para Smart Tags por rubro

Aunque el modelo v7 dice "2 tags base", a veces aparecen tags adicionales rubro-específicas. Cuando aparecen:

### Convención

**Verbo de acción + objeto** en snake_case con `#`:

✅ Correcto:
- `#derivar_a_humano` (verbo + objeto)
- `#seguimiento_activo` (sustantivo + adjetivo de estado)

❌ Incorrecto:
- `#vip` (poco descriptivo de la acción)
- `#urgente` (descriptivo del caso, no de la acción)
- `#blanqueo` (descriptivo del tema, no de la acción)

**Regla:** si vas a crear una tag nueva, asegurate de que el nombre describa **qué acción dispara el sistema**, no el tema del caso.

---

## Naming para procesos / embudos

**Convención:** una palabra simple en snake_case que describa el proceso, no el output.

✅ Correcto:
- `venta`, `soporte`, `faq`, `postventa`, `derivacion`

❌ Incorrecto:
- `embudo_de_ventas` (redundante: ya está dentro del embudo)
- `nuevo_cliente_potencial` (descriptivo del lead, no del proceso)

---

## Naming para versiones de las Reglas Diseño de Prometheo by AUREA

**Convención:** `v[major].[minor]` en minúscula.

✅ Correcto:
- v7 (versión inicial mayor)
- v7.1 (mejora menor)
- v7.2 (otra mejora menor)
- v8 (cambio mayor — backward incompatible)

❌ Incorrecto:
- V7 (mayúscula inconsistente con el resto)
- v7.0.0 (semver no aplica)
- v7-final (sin estados en el nombre)

---

## Resumen visual de convenciones

| Tipo de elemento | Convención | Ejemplo |
|---|---|---|
| Variable Prometheo | `snake_case` | `tipo_usuario` |
| Valor de variable | `snake_case` | `consumidor_final` |
| Smart Tag | `#snake_case` | `#seguimiento_activo` |
| Embudo | `snake_case` (1 palabra) | `venta` |
| Etapa de embudo | `snake_case` (verbo + objeto) | `info_enviada` |
| Archivo cliente DOCX | `[Cliente] - [Tipo] - [V?].ext` | `MIA App - Diseño de CRM.docx` |
| Archivo metodología | `[NN]-descriptivo.md` | `03-reglas-diseno-prometheo-by-aurea.md` |
| Skill | `[scope]-[concepto].md` | `prometheo-crm-graphics.md` |
| Template | `[concepto]-template.md` | `documento-cero-template.md` |
| Caso de referencia | `PROTOTIPO-[cliente].md` | `PROTOTIPO-betrox.md` |
| Placeholder en documento | `[MAYUSCULAS_CON_GUION_BAJO]` | `[NOMBRE_CLIENTE]` |
| Versión de modelo | `v[N]` | `v7` |
| Versión de archivo | `V[N]` | `V5` |

---

## Errores frecuentes a evitar

| Error | Solución |
|---|---|
| Mezclar camelCase y snake_case en mismo proyecto | snake_case siempre para Prometheo |
| Variables muy largas (3+ palabras) | Acortar al concepto esencial |
| Nombrar archivos cliente sin contexto del cliente | Siempre [Cliente] - [Tipo] |
| Versionar con "_final" o "_aprobado" | Usar V1, V2, V3... |
| Crear tags con tema en vez de acción | El nombre describe qué acción dispara, no el tema |
| Olvidar el prefijo numérico en metodología | 00-INDEX, 01-, 02-... permite ordenar bien |
| Usar acentos en nombres internos de variables | ASCII puro para nombres, acentos solo en valores que se muestran al usuario |

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Paleta de colores | `01-paleta-y-colores.md` |
| Metodología de gráficos | `02-metodologia-graficos.md` |
| Reglas Diseño de Prometheo by AUREA | `../02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` |
| Convenciones DOCX | `../02-ETAPA2-Diseno/04-convenciones-docx-cliente.md` |
