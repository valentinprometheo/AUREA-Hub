---
name: prometheo-diseno-agente-ia-feedback
description: >
  Skill de la Etapa 2 (Diseño del Agente Inteligente), fase de iteración. Genera el
  Documento de Feedback de Demo: un DOCX apaisado, cliente-facing, de dos columnas, donde
  se registran las correcciones al agente detectadas al probar la demo dentro de Prometheo.
  Izquierda: la captura de pantalla de la respuesta del agente a corregir. Derecha: qué
  está mal y cómo debería responder. El consultor lo completa primero en vivo con el
  cliente (para transferir el criterio de corrección) y después el cliente lo completa de
  forma asincrónica. Activar cuando Valentín diga "documento de feedback", "feedback de la
  demo", "documento de correcciones del agente", "iteración del prompt", "documento para
  que el cliente marque correcciones", o cuando esté en la fase de iteración de Etapa 2 y
  necesite el soporte para recoger el feedback de una demo.
---

# SKILL: DOCUMENTO DE FEEDBACK DE DEMO (ETAPA 2 — ITERACIÓN)

## QUÉ HACE ESTA SKILL

Genera el **Documento de Feedback de Demo** — un DOCX que se usa en la fase de iteración
del agente (Etapa 2). El documento tiene un cuadro de dos columnas: el cliente pega la
captura de una respuesta del agente que hay que corregir, y al lado escribe qué está mal y
cómo debería responder.

**Fuente de verdad de la metodología:** el protocolo
`01-metodologia/02-ETAPA2-Diseno/02-PASO2-Diseno-Agente-IA/protocolo-feedback-demo.md`.
Esta skill **genera el documento**; el protocolo define **qué es y cómo se usa**. Ante
cualquier duda metodológica, el protocolo manda.

---

## DÓNDE ENCAJA

```
ETAPA 2 — DISEÑO DEL AGENTE INTELIGENTE
└── PASO 2 — Diseño del Agente IA
    ├── Se entrega DOCX + Prompt V1 + demo        (protocolo-entrega-cliente)
    ├── El cliente prueba la demo en Prometheo
    ├── Registra correcciones → DOCUMENTO DE FEEDBACK   ← ESTA SKILL
    ├── El feedback se clasifica y se aplica      (protocolo-iteracion-prompt)
    └── Prompt V2 → nueva demo → … hasta versión final
```

---

## EL MÉTODO — IMPORTANTE

El documento se usa en dos momentos y la secuencia es parte del método:

1. **Primero el consultor lo completa en vivo** con el cliente (pantalla compartida),
   durante una reunión. El cliente ve cómo se corrige.
2. **Después el cliente lo completa solo**, de forma asincrónica, replicando ese criterio.

Por eso el documento es deliberadamente **sintético**: no tiene que enseñar el método —lo
enseña el consultor en vivo—, solo tiene que ser un soporte claro y dar espacio a las
capturas.

---

## INPUTS

| Input | Obligatorio | Para qué |
|---|---|---|
| Nombre del cliente | No | Si se pasa, se puede personalizar el encabezado. Si no, el documento es genérico (sirve igual — su contenido es transversal) |

El documento es **transversal a los rubros**: el cuadro de feedback no cambia entre un
cliente desarrollista, de mobiliario o de insumos. La skill no necesita la vertical.

---

## CARACTERÍSTICAS FIJAS DEL DOCUMENTO

Estas no cambian — son la definición del documento:

- **Formato:** DOCX. El implementador lo sube a Drive y lo abre como Google Doc. Al
  convertir, verificar que se mantenga la orientación apaisada.
- **Orientación:** apaisada (horizontal). Las capturas de conversación son grandes y
  necesitan ancho de columna.
- **Encabezado:** eyebrow "AUREA HUB × PROMETHEO" + título "Documento de Feedback —
  Iteración del Agente IA" + línea de momento de etapa.
- **Bloque "Cómo se completa":** callout naranja, 4 bullets secos. Una fila por corrección;
  marcar antes de capturar; no tachar ni tapar texto; cómo agregar filas.
- **Línea "Dónde se guarda":** apunta a Drive → Etapa 2 — Diseño del Agente Inteligente →
  carpeta "Iteración cliente".
- **El cuadro:** tabla de 2 columnas — "LA IMAGEN CRÍTICA / SITUACIÓN CRÍTICA" y
  "LA CORRECCIÓN". Una fila EJEMPLO (en naranja claro, genérica) + filas en blanco altas.
- **Reglas de marcado de captura:** marcado aditivo (subrayar, recuadrar, flecha), nunca
  destructivo (tachar, tapar, recortar). Ver el protocolo para el detalle del porqué.

---

## CÓMO SE GENERA

El DOCX se genera con el script `generar_documento.js` (en esta misma carpeta), que usa la
librería `docx` de Node.

1. `npm install docx` si no está instalada.
2. Ejecutar `node generar_documento.js`. El script produce el DOCX en
   `/mnt/user-data/outputs/`.
3. **Validar** con `python /mnt/skills/public/docx/scripts/office/validate.py`.
4. Convertir a PDF/imagen para revisar que se vea bien antes de entregar.
5. Entregar al implementador con la instrucción: subir a Drive y abrir como Google Doc,
   verificando la orientación apaisada.

**Nombre del archivo de salida:** `Documento de Feedback - Iteracion del Agente IA.docx`
(o con el nombre del cliente, si se personalizó).

El script `generar_documento.js` ya tiene embebida la paleta AUREA, la estructura completa
y la fila EJEMPLO. Para personalizar por cliente, ajustar el encabezado en el script.

---

## EJEMPLO DE OUTPUT

En esta carpeta está `ejemplo-output.docx` — el documento ya generado, como referencia de
cómo tiene que verse el resultado.

---

## RELACIÓN CON OTRAS SKILLS Y DOCUMENTOS

| Elemento | Relación |
|---|---|
| `protocolo-feedback-demo.md` | Fuente de verdad de la metodología — esta skill la ejecuta |
| `protocolo-iteracion-prompt.md` | El feedback recogido con este documento se clasifica con la matriz de ese protocolo |
| `prometheo-etapa2-design` | Skill orquestadora de Etapa 2 — la fase de iteración usa esta skill |
| `prometheo-docs-kickoff` | Skill hermana: genera documentos cliente-facing, pero de Etapa 1 |
