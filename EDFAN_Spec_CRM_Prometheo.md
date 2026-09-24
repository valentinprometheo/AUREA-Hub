# EDFAN Real Estate · Spec de cambios del CRM Prometheo

Documento interno AUREA. Sale de auditar el export real de Prometheo
(1.017 contactos, julio a septiembre 2026) contra la metodología de diseño de CRM.

- **Rubro:** desarrollista inmobiliario · **Integración:** Tokko · **Estadío:** Etapa 4, mejora continua.
- **Doctrina aplicada:** `embudos-y-tags.md` (modelo de datos), `01-real-estate.md` (vertical),
  `aurea-curaduria-dato` (criterio de evidencia y denominadores).

---

## 1. Diagnóstico en una línea

> **El CRM está bien diseñado y a medio usar.** El embudo que conduce el agente funciona
> (64% de los contactos tiene tag de ese tramo). El embudo que conduce el equipo humano
> está diseñado completo hasta "Reservado" y "No Concretado", y lo usa el **2%**.

No hay que rediseñar el modelo. Hay que **cerrar el tramo de carga**.

### Evidencia

| Hallazgo | Dato real |
|---|---|
| Embudo del agente (recepción y calificación) | 653 contactos · **64%** |
| Embudo humano (venta y cierre) | 21 contactos · **2%** |
| Contactos sin ningún tag | 260 · **26%** |
| Leads con evidencia de calificado vs marcados con el tag | **386 vs 6** |
| Campo `Reuniones` | **0** en 1.017 |
| Tags que compiten por el mismo cajón | 22 contactos (1%) |

---

## 2. El modelo correcto (y por qué el actual está bien)

La doctrina dice que **el embudo marca de quién es el trabajo, no qué compra el lead**:
se separa Recepción/Calificación (la conduce el agente) de Venta/Cierre (la conduce el
equipo). EDFAN ya tiene esa separación modelada. El problema es de operación, no de diseño.

También está bien resuelto el patrón **variable padre + variable hija**:
`Tipo Perfil` (Vivienda / Inversión / Inmobiliaria) con `Inversión Finalidad` (Renta /
Diversificación) que se completa **solo** si el perfil es Inversión. Sobre su base correcta
(los 61 de perfil Inversión) está al **51%**, no al 3% del total. No tocar.

Y `Pedido Fuera de Catálogo` ya está partido en enum + `Detalle` en texto, que es
exactamente la corrección que la metodología pide cuando un dato abierto no entra en un
enum cerrado. No tocar.

---

## 3. Cambios propuestos

Ordenados por costo, de menor a mayor. Cada uno dice dónde se toca y quién lo hace.

### 3.1 Campos requeridos por etapa · config de Prometheo · AUREA

**Problema:** 386 leads tienen la evidencia de un lead calificado (proyecto, zona y perfil
cargados) y solo 6 llevan el tag. El embudo no está vacío, está subregistrado.

**Cambio:** que una etapa avanzada **no se pueda asignar sin su evidencia mínima**.

| Etapa | Evidencia mínima para entrar |
|---|---|
| Calificado | `Proyecto Interés` + `Zona Interés` + `Tipo Perfil` |
| Visita Agendada | lo anterior + fecha de reunión cargada |
| Reservado | lo anterior + `Forma de Pago` |

**Verificación:** después del cambio, el conteo del tag `Calificado` tiene que acercarse al
conteo por evidencia. Mientras la brecha siga en 380, el cambio no prendió.

### 3.2 Reforzar solo las señales blandas · prompt del agente · AUREA

**Problema:** las variables de señal blanda están bloqueadas: `Objeción Principal` 10%,
`Dolor Principal` 5%, `Contexto VIP` 0,5%. Las duras (zona 51%, proyecto 53%, unidad 38%)
se extraen razonablemente solas.

**Cambio:** aplicar el **refuerzo de dos niveles** de la metodología. El prompt no
re-explica cómo se llena cada variable (eso vive en la plataforma): lleva una línea paraguas
más una línea que prioriza **solo** objeción, dolor, disparador, pedido fuera de catálogo,
VIP y descarte.

> Regla que se respeta: *si el refuerzo nombra todo, no prioriza nada.* No agregar las duras.

**Verificación:** `Objeción Principal` debería pasar de Indicio (10%) a Señal (sobre 40%)
en el siguiente corte.

### 3.3 Activar el embudo de cierre · proceso del equipo · EDFAN

**Problema:** existen `Calificado`, `En Negociación`, `Visita Agendada`, `Reunión Realizada`,
`Reunión Virtual`, `Reservado`, `No Concretado`. Entre todos suman 21 contactos.

**Cambio:** el equipo marca la etapa al agendar y al cerrar. Dos caminos posibles:
disciplina de proceso, o disparar la tag desde una acción ya existente (cargar la fecha de
reunión asigna `Visita Agendada`).

**Verificación:** sin esto **no hay tasa de conversión posible**. Es el único cambio que
desbloquea medir lead → visita → reserva.

### 3.4 Higiene de dimensiones · config de Prometheo · AUREA

**Problema:** 22 contactos llevan dos tags del mismo cajón. El caso principal: **10 leads
marcados a la vez como `Inversor` y `Uso Propio`**, que son dos valores de la dimensión
"tipo de usuario" y deberían ser excluyentes. Otros 8 tienen dos estadíos simultáneos.

**Cambio:** hacer excluyentes los valores dentro de cada dimensión. Además, la tipología ya
vive en la variable `Tipo Perfil`: según la metodología, la tag de tipo de usuario debe ser
**espejo de la variable**, no fuente del dato.

**Nota menor:** 2 contactos tienen `Inversión Finalidad` cargada sin `Tipo Perfil = Inversión`.
La hija no debería completarse fuera de su condición.

### 3.5 Revisar `En Seguimiento` · config · AUREA

La metodología dice: *eliminar el estadío que no tiene una acción propia que lo justifique*
(G&D sacó exactamente este). En EDFAN tiene 96 usos, así que **no se elimina de entrada**:
primero se responde si dispara alguna acción propia o si el tag de estadío más el tiempo
transcurrido ya dan la misma información. Si no dispara nada, se colapsa.

### 3.6 Tags huérfanos del canal B2B

`Inmo x Contactar` (30) e `Inmo en Gestión` (8) son un recorrido B2B propio, no etapas del
embudo de consumidor final. Cuando un canal tiene ciclo de vida estructuralmente distinto,
la metodología pide **embudo propio**. Con 55 inmobiliarias en la base, conviene separarlo.

---

## 4. Inventario de tags y acción por cada uno

| Tag | Uso | Acción |
|---|---:|---|
| En Conversación | 436 | Mantener |
| Uso Propio | 124 | Mantener, pero como espejo de `Tipo Perfil` |
| En Seguimiento | 96 | Revisar (§3.5) |
| Derivado | 86 | Mantener |
| Forma de pago | 82 | Mantener |
| Inversor | 57 | Excluyente con Uso Propio (§3.4) |
| Financiación a preparar | 43 | Mantener |
| Proveedor / Inmobiliaria | 41 / 36 | Mantener, fuera de la base de demanda |
| Inmo x Contactar / en Gestión | 30 / 8 | Mover a embudo B2B propio (§3.6) |
| No Fit | 28 | Mantener |
| Seguir SEM | 12 | Definir criterio de disparo o eliminar |
| Nuevo Lead | 7 | Probablemente redundante con En Conversación |
| Calificado · En Negociación · Visita Agendada | 6 · 5 · 4 | **Activar** (§3.1 y §3.3) |
| Reunión Realizada · Reservado · No Concretado | 2 · 2 · 1 | **Activar** (§3.3) |
| Contacto VIP | 2 | Evaluar pasar a variable de 4 valores, como BETROX |

---

## 5. Orden de implementación

1. **Config** (§3.1, §3.4): no depende de nadie más y arregla la medición.
2. **Prompt** (§3.2): desbloquea las señales blandas.
3. **Proceso** (§3.3): es el que más valor da y el que más depende del equipo de EDFAN.
4. **Estructura** (§3.5, §3.6): se decide con el cliente, no urge.

---

## 6. Lo que falta para cerrar la auditoría

- **Catálogo de tags configurados en Prometheo.** El export solo muestra los tags que se
  usaron al menos una vez: un tag creado y nunca aplicado es invisible en este análisis.
  Sin ese catálogo no se puede afirmar qué tags están muertos por diseño y cuáles por falta
  de uso.
- **Definición de embudos vigente** (qué tags son etapa de qué embudo). Acá se infirió por
  el nombre y el comportamiento.
- **Gasto de Meta**, para cerrar costo por consulta calificada y ROI por anuncio.
