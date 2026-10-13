# Protocolo del Documento de Feedback de Demo

> **Etapa:** 2 — Diseño del Agente Inteligente
> **Paso:** 2 — Diseño del Agente IA, fase de iteración
> **Tipo:** Documento cliente-facing
> **Skill que lo genera:** `prometheo-diseno-agente-ia-feedback`

---

## Qué es

Un documento de dos columnas donde se registran, de forma ordenada, las correcciones al
agente detectadas al probar la demo dentro de Prometheo. **Izquierda:** la captura de
pantalla de la respuesta del agente que hay que corregir. **Derecha:** qué está mal y cómo
debería responder. Una fila por corrección.

Es la herramienta que canaliza el feedback de la demo durante la iteración del prompt
(V1 → V2 → VN).

---

## Por qué existe

El `protocolo-iteracion-prompt.md` establece dos cosas: que **siempre hay demo antes de
iteración**, y que **sin demo no hay feedback válido**. Pero el feedback de una demo —el
agente respondiendo en conversaciones reales— necesita un soporte propio: una corrección
casi siempre requiere mostrar *qué respondió el agente*, y eso es una captura de pantalla,
no un comentario de texto suelto sobre el documento de diseño.

Este documento cubre ese hueco. El comentario sobre el DOCX de diseño sirve para feedback
del diseño en abstracto; el Documento de Feedback de Demo sirve para feedback de la
conversación real del agente.

---

## El método: del consultor al cliente

El documento se usa en dos momentos, y esa secuencia es parte del método:

1. **Primero, en vivo (sincrónico).** El consultor completa el documento durante una
   reunión con el cliente, con pantalla compartida. El cliente ve **cómo se corrige**: qué
   se mira en una respuesta, cómo se marca la captura, cómo se redacta una corrección útil.
2. **Después, asincrónico.** El cliente y su equipo siguen completando el documento por su
   cuenta, replicando el criterio que vieron.

El valor está en esa transferencia de criterio: no se le entrega al cliente un documento
frío con instrucciones, se le enseña el método haciéndolo, y recién después se le delega.

---

## Estructura del documento

| Parte | Contenido |
|---|---|
| Encabezado | Título + momento de la etapa (Etapa 2, fase de iteración) |
| Instrucciones "Cómo se completa" | Bloque corto, en bullets — el documento no enseña, lo enseña el consultor en vivo |
| Dónde se guarda | Una línea apuntando a la carpeta de Drive |
| El cuadro | Tabla de 2 columnas: una fila EJEMPLO + filas en blanco |

El documento es **apaisado (horizontal)** — las capturas de conversación son grandes y
necesitan ancho de columna.

---

## Reglas de marcado de la captura

Estas reglas son el núcleo metodológico del documento y son **fijas**:

- La captura se marca **antes** de capturar: se subraya o recuadra el sector criticado, y
  recién después se saca la captura. La captura llega señalando sola el problema.
- El marcado es **aditivo, nunca destructivo**. Se permite subrayar, recuadrar, poner una
  flecha al costado. Está prohibido tachar palabras, poner líneas encima del texto, o
  recortar partes de la respuesta.
- La razón de la prohibición: el consultor necesita **leer qué respondió mal el agente**
  para poder corregirlo. Tapar el texto destruye la información que hace falta.
- Una corrección por fila. Si una conversación tiene varios problemas, son varias filas.

---

## Dónde se guarda

El documento vive en la carpeta de Drive del proyecto, dentro de **Etapa 2 — Diseño del
Agente Inteligente**, en la subcarpeta **"Iteración cliente"**. Cada ronda de correcciones
se trabaja sobre el mismo documento — es el registro acumulado de la iteración.

---

## Conexión con el resto de la metodología

- **`protocolo-iteracion-prompt.md`** (misma carpeta) — este documento es el soporte
  concreto del feedback de demo que ese protocolo exige. El feedback recogido acá se
  clasifica con la matriz de ese protocolo (crítico / mejora / cosmético / ambiguo /
  contradice plataforma / out of scope) antes de aplicarse al prompt.
- **`protocolo-entrega-cliente.md`** (misma carpeta) — la Ronda 1 entrega DOCX + Prompt +
  demo; este documento es lo que el cliente usa para devolver el feedback de esa demo.
- **Skill `prometheo-diseno-agente-ia-feedback`** — genera el documento personalizado por
  cliente.
