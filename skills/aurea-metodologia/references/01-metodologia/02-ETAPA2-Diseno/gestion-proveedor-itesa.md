---
consultar-cuando: el proveedor (Prometheo/ITESA) genera retrabajo, entrega una reescritura del prompt, o hay que elevar un incidente
disparadores: "reclamo a Prometheo", "retrabajo del proveedor", "reescritura de ITESA", "auditar versión del proveedor", "dossier de incidentes"
fuente-única-de: gestión del proveedor — incidentes, reescrituras y los tres actores
combina-con: metodologia-correccion-agente, pendientes-itesa, 10-patrones-correccion-agente
---

# Gestión del proveedor (Prometheo / ITESA)

> Capa de método para trabajar con el proveedor de la plataforma. Cubre tres cosas: cómo se
> auditan las reescrituras del prompt que entrega Prometheo, cómo se documenta el retrabajo
> imputable al proveedor, y cómo se separan los tres actores para no confundir un mensaje al
> cliente con una elevación al proveedor.

---

## Los tres actores — nunca se mezclan

En todo proyecto conviven tres actores con roles distintos:

1. **AUREA** — diseña la lógica comercial y conversacional, corrige el prompt, audita.
2. **Prometheo / ITESA (proveedor)** — la plataforma. Entrega reescrituras del prompt, resuelve
   integraciones, define qué permite el producto.
3. **El cliente** — el negocio (EDFAN, BETROX). Reporta bugs desde su operación real.

**Regla dura:** un mensaje al cliente NO es una elevación al proveedor, y viceversa. Un bug que
reporta el cliente puede ser responsabilidad de AUREA (prompt), de ITESA (plataforma o
integración) o del propio cliente (dato mal cargado). Antes de elevar algo a ITESA se clasifica
de quién es. Y **no se nombra el sistema al cliente:** PrestaShop, Tokko, la integración, el
catálogo interno son mecánica de AUREA, no información para el negocio ni para su lead.

---

## Auditar una reescritura del proveedor

Prometheo reescribe el prompt de un agente cada tanto (el de Catalina se reescribió varias
veces). Cada reescritura se audita antes de activarla, con el barrido de coherencia (ver
`metodologia-correccion-agente.md`, chequeo 8). El molde de auditoría, validado con la
V3.0-R3 de Catalina:

1. **Bloqueantes** — lo que impide activar (nombres de archivo rotos, identificadores que no
   coinciden entre secciones, placeholders cruzados). Se listan primero.
2. **Reglas nuestras que se perdieron** — la reescritura del proveedor suele llevarse puestas
   las reglas comerciales que AUREA agregó por feedback del cliente. Se listan una por una, con
   dónde estaban y qué pasó, para reponerlas.
3. **Contradicciones internas que metió** — dos reglas que aplican al mismo turno sin declarar
   cuál prevalece (ej. "2 o 3 opciones" en una sección y "2" en otra).
4. **Lo que aportó de nuevo (replicable)** — la parte más valiosa: reglas estructurales que
   AUREA no tenía y conviene replicar en otros clientes (jerarquía de reglas, mapeo estricto de
   campos, descripciones verificables, identificación por nombre no posición). Estas suben a la
   metodología como doctrina.
5. **Lo nuestro que sí conservó** — se verifica presente en el texto, para saber qué no hay que
   reponer.
6. **Apéndice sin sanear** — lo que el proveedor no tocó (correcto si la instrucción fue no
   tocarlo) pero sigue con entradas rotas.

### El hallazgo estable sobre las reescrituras del proveedor

**La reescritura del proveedor mejora la estructura y pierde la lógica comercial.** Aporta
orden, jerarquía y reglas anti-alucinación de primer nivel; se lleva puestas las reglas de
venta que se agregaron por feedback del cliente. La conclusión operativa: **no se elige entre
la versión del proveedor y la de AUREA, se combinan.** La estructura de ellos más la lógica
comercial nuestra, con barrido de coherencia obligatorio antes de entregar.

Consecuencia metodológica doble: cada reescritura del proveedor es a la vez un riesgo (perder
lógica comercial) y una fuente de doctrina nueva (las reglas estructurales que aporta). Por eso
se audita con los dos ojos: qué reponer y qué replicar.

---

## Dossier de incidentes — retrabajo imputable al proveedor

Cuando el proveedor genera retrabajo (una entrega incompleta, una regla fija que se
desestabiliza sola entre versiones, un caso que vuelve), se documenta con evidencia para poder
elevarlo. El registro tiene un **filtro de credibilidad**: no todo lo que molesta es imputable
al proveedor; se separa lo que es responsabilidad de ITESA de lo que es de AUREA o del cliente.

Estructura del registro (documento vivo por cliente, no método):
- Registro por cliente (incidente, fecha, evidencia, a quién es imputable).
- Casos con cronología propia (cuando un incidente tiene varias idas y vueltas).
- Entregas incompletas.
- Inestabilidad de reglas fijas (una regla que se pierde y reaparece entre versiones).
- Otros temas (patrón reactivo).
- **Descartados y por qué** — la columna que da credibilidad: lo que se evaluó y NO se eleva
  porque no es del proveedor.

**Cuándo se usa:** cuando hay que elevar retrabajo a ITESA con evidencia. El filtro de
credibilidad es lo que hace que la elevación sea tomada en serio: se eleva lo que está probado,
no la queja.

---

## Separación método vs entregable de cliente

Este archivo es **método** (reutilizable en cualquier cliente). Los documentos concretos que
se generan aplicándolo son **entregables de cliente** y se archivan por cliente:
- El registro de incidentes de un cliente puntual.
- La auditoría de una versión concreta que entregó el proveedor.
- La matriz de auditoría del prompt del cliente (documento vivo por cliente, se actualiza en
  cada ronda).

Ver el principio general de separación en `00-OUTPUTS-POR-ETAPA.md` y en el índice de
documentos maestros del proceso.
