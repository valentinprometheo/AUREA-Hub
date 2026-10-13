---
name: aurea-data-action-driven
description: Define qué es un dato data-driven y qué es una acción action-driven en AUREA, cómo se pasa de uno a otra y cómo se muestran en los tableros de Inteligencia Comercial y en los documentos para clientes (cards de Posibles mejoras, Fugas y Qué hago ahora). Usala SIEMPRE que haya que escribir, auditar o corregir una card de acción, una recomendación o un hallazgo para el cliente. Activar ante "data-driven", "action-driven", "insight accionable", "posibles mejoras", "fugas", "qué hago ahora", "cards de acción", "recomendación", "y entonces qué".
---

# Data-driven y action-driven en AUREA

Un tablero de IC no termina en el número. Termina en una decisión que alguien ejecuta
y que el próximo período confirma o desmiente. Esta skill fija el idioma para pasar del
dato a la acción sin perder trazabilidad.

Se usa junto con `aurea-ic-curaduria-del-dato` (qué número se puede mostrar),
`aurea-ic-performance-report` (priorización por impacto y esfuerzo) y
`aurea-dashboard-design` (componentes y color). No las reemplaza.

## Las dos capas

**Data-driven (en AUREA).** El número curado: tiene base, denominador y fuente, y
responde "qué pasó y por qué". Cubre los niveles descriptivo y diagnóstico de la
escalera de Gartner. Sin base o sin fuente, no es data-driven: es una impresión.

**Action-driven (en AUREA).** [DEFINICIÓN AUREA] La decisión que sale de ese número.
Tiene cinco partes obligatorias: verbo, dueño, lugar donde se cambia, efecto esperado
medible y cómo se verifica. Cubre el nivel prescriptivo y el "Now what".

AUREA es data-informed en el sentido de Chen y Mosseri: el dato propone, el criterio
comercial decide. Por eso la card siempre muestra el dato y la decisión juntos.

## Regla de paso (obligatoria)

1. **Ninguna card action-driven existe sin su dato data-driven.** Si no hay número con
   base y fuente, la card no se publica; a lo sumo se convierte en una card de *Medir*.
2. **Ningún dato se muestra al cliente sin, al menos, una lectura de "y entonces qué".**
   Un KPI suelto es descriptivo; la lectura puede ser "no requiere acción este período",
   pero tiene que estar escrita.
3. **El efecto esperado usa la misma métrica que el dato.** Si el dato es mensajes por
   lead, el efecto se mide en mensajes por lead o en envíos, no en "mejor experiencia".
4. **Cada acción se cierra en el período siguiente** con el mismo cálculo, la misma base
   y la misma fuente (ciclo Build-Measure-Learn). Si se cambió la base, se dice.

## Del dato a la acción en cuatro preguntas

| Paso | Pregunta | Fuente | Lo que se escribe |
|---|---|---|---|
| What | ¿Qué pasó? | Borton; Gartner descriptiva | Dato principal con base |
| So what | ¿Por qué importa y por qué pasó? | Gartner diagnóstica | Causa probable y costo |
| Now what | ¿Qué hacemos? | Gartner prescriptiva | Verbo, dueño, dónde |
| Measure | ¿Cómo sabemos si funcionó? | Ries, OODA | Métrica, umbral, fecha |

## Sellos de verbo

Seis verbos, ni uno más: **Corregir, Proteger, Separar, Medir, Decidir, Activar**.
Dueños posibles: **AUREA, Ventas, Marketing, Dirección**. Detalle, colores y ejemplos en
`references/taxonomia-verbos.md`.

## Anatomía de la card (tablero de IC de EDFAN)

- Arriba: sello con verbo y dueño.
- Título: "Tema · dato principal".
- Contexto: Qué mide / Base / Dato (fuente).
- Al desplegar: Qué hacer / Dónde se cambia / Efecto esperado / Cómo lo medimos.

HTML y CSS de referencia en `references/anatomia-card.md`.

## Dónde se usa

- **Tablero IC**, sección "¿Qué hago ahora?": máximo tres cards en modo Básico,
  ordenadas por impacto. En Avanzado se agregan, no se reemplazan.
- **Posibles mejoras**: cards de Corregir, Activar o Medir sobre el período.
- **Fugas**: cards de Corregir, Proteger o Separar donde se pierde plata, leads o tokens.
- **Documentos para clientes**: misma anatomía en versión estática (todo desplegado).

## Cómo trabajar

1. Partí del número curado (`aurea-ic-curaduria-del-dato`). Anotá base y fuente.
2. Escribí la lectura "y entonces qué" en una frase.
3. Elegí el verbo con la tabla de taxonomía. Si dudás entre dos, la acción no está clara.
4. Completá las cuatro partes del despliegue.
5. Pasá el checklist de `references/checklist-validacion.md`. Si falla un chequeo
   obligatorio, la card no sale.
6. Compará con `references/ejemplos.md` antes de entregar.

## Límites que hay que decir en voz alta

- **Ley de Goodhart.** Si una card premia una métrica (por ejemplo, bajar tokens), sumá
  una métrica guardiana (tasa de calificación, respuesta del lead) para no ahorrar
  rompiendo la conversación.
- **Parálisis por dato.** Si el dato no alcanza, la acción es *Medir* con fecha, no
  esperar indefinidamente.
- **Data-informed, no data-dictated.** El dato no captura lo que todavía no se construyó.

## Referencias

- `references/definiciones-y-fuentes.md`: definiciones con autor, URL y fecha de acceso.
- `references/taxonomia-verbos.md`: los seis sellos.
- `references/anatomia-card.md`: estructura y HTML/CSS de referencia.
- `references/checklist-validacion.md`: diez chequeos.
- `references/ejemplos.md`: tres buenos y tres malos (tokens y Meta).
