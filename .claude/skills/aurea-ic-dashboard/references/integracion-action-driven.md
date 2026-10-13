# Integración de `aurea-data-action-driven` (v2) al proceso de IC

Trazabilidad: qué toma cada skill de la familia de `aurea-data-action-driven`, qué le entrega,
y qué reglas propias de IC se suman. La skill de origen se invoca con la herramienta Skill;
acá solo está lo que cambia al usarla en un tablero.

## 1. Qué es y qué no es

- **Data-driven** es el número curado (base, denominador, fuente). **Action-driven** es la
  decisión con verbo, dueño, lugar, efecto y forma de verificarlo. El **score** (0 a 100%) dice
  cuánto de la *acción* se apoya en datos. Se calcula con la rúbrica de 6 componentes de la
  skill (base 20, fuente 15, cobertura 15, profundidad 20, evidencia previa 15, cierre medible 15).
- El score es de **acciones**, no de KPIs. Un número del tablero no lleva score: lleva base,
  cobertura, origen y nivel de la escalera de evidencia (`aurea-ic-curaduria-del-dato`).
- La rúbrica es propia de AUREA, **versión 1, sin calibrar**: los pesos se ajustan cuando hay
  20 cards cerradas. El tablero lo dice (ver regla R4).

## 2. Cuánto se integra

| Nivel | Qué | Decisión |
|---|---|---|
| Núcleo | Cards de acción en "¿Qué hago ahora?" (recomendaciones, posibles mejoras, fugas), con sello, dueño y score | **Integrar ya** |
| Núcleo | Lectura "y entonces qué" en cada pestaña, aunque sea "no requiere acción este período" | **Integrar ya** |
| Núcleo | Guardiana en toda card que premia una métrica | **Integrar ya** |
| Con adaptación | El score se limita según el nivel de evidencia del dato central (R1) y los datos modelados (R2) | **Integrar con la regla propia de IC** |
| Con adaptación | Registro de calibración por card | **Empezar a registrar ya**, ajustar pesos con 20 cards cerradas |
| Fuera del tablero | Citas académicas y tensiones T2 (rendimiento de ser data-driven) | Solo en pitch y decks (`aurea-ic-conocimiento`), nunca como promesa al cliente |
| Fuera de IC | Score en corrección de prompts, discovery, calificación y tokens | Lo aplican esas skills; IC solo lo recibe como card |

## 3. Reglas propias de IC (se suman a las de la skill)

**R1 · Techo por evidencia del dato central.** La rúbrica por sí sola permite que una card con
cobertura 0 llegue a 85% ("basada en datos"), porque cobertura vale 15 de 100. En IC eso
contradice la escalera de evidencia. El score de una card no puede superar el techo del nivel
del dato central que la sostiene:

| Nivel del dato central (curaduría) | Techo del score | Banda máxima | Verbos permitidos |
|---|---|---|---|
| Hecho (80% o más) | 100 | Basada en datos | Los seis |
| Señal (40 a 79%) | 79 | Informada por datos | Los seis |
| Indicio (10 a 39%) | 54 | Hipótesis con indicio | Prueba acotada con fecha; Medir; Decidir |
| No reportable (menos de 10%) | 29 | Criterio experto | Solo Medir o Decidir |

Esto reemplaza la regla anterior "no usar datos por debajo de Señal": ahora la card puede
existir, pero declara su techo y su verbo cambia.

**R2 · Datos modelados.** Si el dato central es modelado o ilustrativo (por ejemplo PAVIR):
Fuente = 0, el techo es 54 y la card lo dice en el sello. Nunca se presenta como basada en datos.

**R3 · Score solo en acciones.** KPIs, series y tablas no llevan score. Cada pestaña lleva su
lectura "y entonces qué". Monitorean las pestañas; acciona "¿Qué hago ahora?" (tensión T5).

**R4 · Rúbrica v1 sin calibrar.** Mientras no haya 20 cards cerradas, "Integraciones" o "Calidad
de datos" muestra la leyenda "Rúbrica de score versión 1, sin calibrar" y la fecha. El score se
lee junto a la etiqueta de banda; la banda manda sobre el número exacto.

**R5 · Guardianas típicas de IC.**

| Card que premia… | Guardiana |
|---|---|
| Menos mensajes por lead o menos tokens | % de calificación con la definición del cliente |
| Subir el % de calificados | Que la definición del cliente no cambie (ni se afloje) |
| Más respuestas a una difusión de WhatsApp | Respuestas calificadas y hot leads, y calidad del número |
| Más clics o empalme en email | Consultas calificadas generadas |
| Menor CPL | CPL por lead calificado, no por consulta |
| Más hot leads recontactados | Tiempo de derivación y ruteo registrado |

**R6 · Cantidad.** En modo Básico, tres cards por impacto esperado. Las de score menor a 55
llevan la etiqueta de banda visible sin desplegar. En Avanzada, todas.

**R7 · Registro de calibración.** Al cerrar cada período se registra por card: score, banda,
techo aplicado y resultado (cumplió, parcial, no cumplió). Lo carga AUREA y vive en la
pestaña Integraciones (o en un anexo del reporte).

**R8 · Impacto primero.** El orden entre cards es por impacto esperado (como en
`aurea-ic-performance-report`); el score desempata y define la etiqueta. Una card de alto
impacto y score bajo se convierte en prueba acotada con fecha, no se descarta.

## 4. Trazabilidad por skill

| Skill | Qué entrega a las cards | Qué toma de la skill nueva | Estado |
|---|---|---|---|
| `aurea-ic-curaduria-del-dato` | Base, cobertura y origen: alimentan los componentes 1 a 3 del score. El nivel de la escalera fija el techo (R1) | Distinguir escalera (decide si un *número* titula) de banda (decide cuánto pesa una *acción*) | Hecho en este repo |
| `aurea-hub-criterio-calificacion-leads` | Materia de cards: hot leads sin seguimiento (*Activar*), no-demanda (*Separar*), recalificar la base (*Corregir*), ahorro de tokens (*Corregir*) | Score y guardiana en cambios de criterio y de tokens | **Pendiente en la cuenta** (no editable desde acá) |
| `aurea-ic-criterio-comercial` | Cola por impacto × disparador (*Activar*), objeción ↔ Disparador Compra (*Decidir* o *Activar*) | Card como formato de salida; el cruce con datos modelados sigue R2 | Hecho en este repo |
| `aurea-ic-email-marketing`, `aurea-ic-whatsapp-marketing` | Métricas de canal y su guardiana (R5) | Card para "pausar, subir, corregir" una campaña | Cubierto por R5; sin cambios en el archivo |
| `aurea-ic-performance-report` | El formato de la lectura: cada recomendación es una card | Sellos, score, "por qué este score" | Hecho en este repo |
| `aurea-ic-dashboard` (conductor) | Orquesta: curaduría → card → control | Paso nuevo de acciones y checklist | Hecho en este repo |
| `aurea-dashboard-design` | Cómo se ve la card | Componente `act-card`, colores semánticos de sellos y bandas, regla de tres cards en Básico | **Pendiente en la cuenta** |
| `aurea-metodologia` | Contexto de implementación y mejora continua | Curva de score que sube a medida que entra dato real; registro de calibración en Etapa 4 | **Pendiente en la cuenta** |
| `prometheo-correccion-prompts` | Filas de Feedback del Agente | Score por fila: una captura suelta no pesa como 40 conversaciones | **Pendiente en la cuenta** |
| `aurea-ic-conocimiento` | Narrativa comercial de IC | T2: no prometer un porcentaje de rendimiento al cliente | Sin revisar en esta conversación |

## 5. Pendientes en la cuenta (texto sugerido)

- **`aurea-dashboard-design`:** sumar el componente card de acción (referencia
  `anatomia-card.md` de la skill nueva), con tokens semánticos de sellos y bandas que no usan
  el violeta, azul ni rosa de marca; en Básico, tres cards, y las de menos de 55 con la
  banda visible.
- **`aurea-metodologia`:** en Etapa 4 (mejora continua), registrar score y resultado de cada
  card; en discovery y prompt v1, aclarar que arrancan con score bajo y está bien.
- **`aurea-hub-criterio-calificacion-leads`:** en `ahorro-de-tokens` y en cambios de criterio,
  exigir score y guardiana (R5).
- **`prometheo-correccion-prompts`:** score por fila del Feedback.
