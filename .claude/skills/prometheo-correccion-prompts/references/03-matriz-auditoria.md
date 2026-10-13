---
consultar-cuando: cerrar una ronda de correcciones, documentar el barrido, armar la matriz del cliente
disparadores: "matriz de auditoría", "documentar el barrido", "cerrar la ronda", "checklist de corrección"
fuente-única-de: formato de la matriz de auditoría y checklist de cierre de corrección
combina-con: 01-entrega-por-sector-completo, 02-barrido-de-coherencia
---

# 03 · Matriz de auditoría y checklist de cierre

> Dónde queda registrado que el barrido se corrió, qué encontró y cómo se resolvió. Es el
> documento interno de AUREA que hace auditable la corrección de un prompt a lo largo de las
> rondas.

---

## Para qué existe

Tres funciones, en orden de importancia:

1. **Gate de entrega.** Una corrección sin barrido completo no se entrega. La matriz es donde
   consta que se corrió.
2. **Memoria entre rondas.** Es lo que impide que un conflicto ya resuelto se reabra tres rondas
   después (chequeo 7), y lo que impide que un bloque eliminado por huérfano se "restaure" por
   error (chequeo 4).
3. **Trazabilidad.** Permite responder qué corrección originó qué regla, y demostrarle al
   cliente que su feedback entró.

Vive del lado de AUREA, una por cliente, y acompaña al documento de Feedback del Agente IA
(que es el insumo) sin mezclarse con él.

---

## Estructura de la matriz

Una fila por **corrección aplicada**. Las columnas:

| Columna | Qué lleva |
|---|---|
| **Fila** | número de la fila del documento de feedback que la originó, o "captura suelta" con fecha |
| **Ronda / versión** | ronda de feedback y versión del prompt sobre la que se corrigió (ej. R3 · v12 → v13) |
| **Evidencia** | cita verbatim de lo que el agente respondió mal, o el título de la situación |
| **Capa** | dato / fuente · terminología · lógica conversacional |
| **Tipo de cambio** | **frase** o **mecanismo** (define si disparan los chequeos 3 y 4) |
| **Sector(es)** | los sectores tocados, y si se entregaron fusionados |
| **Regla resultante** | número y nombre de la regla que quedó en el prompt |
| **Ámbito declarado** | "aplica a / no aplica a", tal como quedó escrito |
| **Estructura eliminada** | qué bloque, índice o apéndice quedó huérfano y se borró, y por qué (o "nada") |
| **Barrido 1-7** | siete casilleros: OK / corregido / N/A, uno por chequeo |
| **Conflictos** | con qué regla o fila chocó y cómo se resolvió (o "sin conflicto") |
| **Entrega** | sector completo, bloque fusionado, o parcial por excepción de placeholders (con motivo) |
| **Score** | score data-driven de la corrección (0 a 100%) con su banda y una línea de "por qué" por componente (rúbrica de `aurea-data-action-driven`). Base = cantidad de conversaciones donde aparece el error |
| **Guardiana** | la métrica que no puede empeorar con la corrección (obligatoria si la corrección se motiva en costos o premia una métrica) |

Reglas de la matriz:

- **Nada se marca OK sin haberlo mirado.** Un chequeo que no aplica se marca N/A con motivo, no
  se deja en blanco ni se marca OK por defecto.
- **La columna Conflictos nunca queda vacía.** O dice con qué chocó y cómo se resolvió, o dice
  "sin conflicto". El vacío no distingue "no había" de "no miré".
- **La columna Estructura eliminada nunca queda vacía.** Dice qué se borró o dice "nada". Un
  borrado sin registro es indistinguible de un borrado por error.
- **Una fila derogada no se borra.** Se marca como derogada, con la fila que la reemplaza. Es
  justamente el registro que evita que vuelva.
- La matriz se actualiza **en el momento de la corrección**, no al final de la ronda.
- **El score se escribe, no se estima.** Una captura suelta del cliente suele quedar en la banda
  "criterio experto" (0 a 29) o "hipótesis con indicio" (30 a 54); el mismo error en decenas de
  conversaciones del export, en "informada" o "basada en datos". Con score bajo la corrección
  igual entra, pero en el Guión de Testing se marca para verificar en la ronda siguiente.
- **Al cerrar la ronda siguiente** se anota si la corrección resolvió el patrón (cumplió,
  parcial, no cumplió). Eso calibra la rúbrica.

---

## Checklist de cierre de corrección

Bloque corto para correr y pegar al final de **cada** corrección entregada. Los siete chequeos
en formato verificable, más el gate de entrega.

```
BARRIDO DE COHERENCIA · [CLIENTE] · v[N] ← v[N-1] · filas [__]

[ ] 1 · PRESENCIA
      Cada regla corregida está literalmente en el texto final.
      Verificado por: script / búsqueda literal.  Reglas chequeadas: ____

[ ] 2 · CONTRADICCIÓN ENTRE REGLAS
      Por cada regla nueva o modificada busqué en TODO el prompt otras reglas
      sobre el mismo comportamiento.
      Reglas que podían aplicar al mismo turno: ____
      Resolución: prevalencia explícita declarada / ámbito acotado / no había competencia.

[ ] 3 · PROPAGACIÓN DE MECANISMO
      ¿Cambió un mecanismo (de dónde sale un dato, cómo se envía algo, qué fuente manda)?
      SÍ → palabras clave barridas en el prompt completo: ____
           TODAS las secciones que lo MENCIONAN, alineadas: ____
      NO → solo cambió una frase. Impacto local verificado.

[ ] 4 · ESTRUCTURA HUÉRFANA
      ¿El cambio dejó algún bloque, índice o apéndice sin función?
      SÍ → eliminado dentro del mismo sector entregado: ____  (registrado en la matriz)
      NO → ningún bloque quedó sin invocación.
      Placeholders: verificados contra el inventario real antes de borrar nada.

[ ] 5 · REFERENCIAS CRUZADAS
      Extraje todas las menciones "ver Sección X" / "(Sección X)" / "regla N".
      Todas existen y contienen lo que se invoca: ____
      Placeholders y nombres de archivo citados: existen en el inventario, verbatim.

[ ] 6 · ÁMBITO DE CADA REGLA
      Cada regla nueva declara a qué caso aplica y a cuál no.
      Reglas con SIEMPRE / NUNCA / MÍNIMO / TODOS / CUALQUIER: ____
      Todas con ámbito acotado explícito.

[ ] 7 · RECONCILIACIÓN ENTRE RONDAS
      ¿Alguna corrección de ronda anterior toca el mismo punto?
      SÍ → gana la más reciente. Resolución documentada en la matriz, filas ____ (nueva y vieja).
      NO → sin antecedentes sobre este punto.

SCORE DATA-DRIVEN: __%  (Base __ · Fuente __ · Cobertura __ · Profundidad __ · Evidencia __ · Cierre __)
GUARDIANA (si aplica): ____

RESULTADO: __/7
ENTREGA: sector completo / bloque fusionado (secciones ____) / parcial por excepción
         de placeholders (motivo: ____)

Con menos de 7/7 la versión NO se entrega. Aplica también a entregas parciales.
```

---

## Cómo se conecta con el resto

- El **documento de Feedback del Agente IA** aporta la evidencia y el número de fila. Es el
  insumo, y es cliente-facing.
- Esta **matriz** es interna de AUREA y agrega la capa de verificación.
- El **Guión de Testing de regresión** se arma desde las reglas de la matriz: cada regla
  resultante se vuelve un bloque Tema / Pregunta / Respuesta correcta esperada, y es lo que le
  demuestra al cliente que la corrección entró.
