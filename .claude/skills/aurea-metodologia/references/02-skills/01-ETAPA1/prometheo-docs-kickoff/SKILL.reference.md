---
name: prometheo-docs-kickoff
description: >
  Skill que genera los 2 documentos cliente-facing del PASO 1 de Etapa 1 (Pre-Discovery),
  los que el cliente recibe ANTES de la primera reunión (R1): (1) el Doc de Bienvenida //
  Kickoff — DOCX personalizado que presenta AUREA, el sistema a diseñar y las 4 etapas del
  proyecto, y (2) la Guía Metodológica — DOCX pensado para subir a Drive y abrir como
  Google Doc, que le explica al cliente cómo va a funcionar el Discovery con sus 3
  documentos vivos. Toma como input principal el
  Doc 0 (auditoría web, output de prometheo-auditoria-web) más datos del proyecto que
  aporta el implementador. NO contiene la metodología de auditoría ni la de Discovery —
  solo produce el material cliente-facing intermedio entre el Doc 0 interno y los 4
  documentos del Paso 2. Activar cuando el implementador diga "generar el Doc de
  Bienvenida", "armar la Guía Metodológica", "material para enviar al cliente antes de
  R1", "documentos de kickoff", "material pre-discovery", o cuando termine la auditoría
  web y necesite preparar lo que el cliente recibe antes de la primera reunión.
---

# SKILL: MATERIAL CLIENTE-FACING PRE-DISCOVERY (PASO 1 DE ETAPA 1)

## QUÉ ES ESTA SKILL

Esta skill genera los **2 documentos que el cliente recibe antes de la primera reunión**:

1. **Doc de Bienvenida // Kickoff** — DOCX. La primera impresión profesional. Le muestra al cliente que llegamos a R1 con un panorama de su negocio, le explica qué vamos a diseñar y quién tiene que estar en la reunión.
2. **Guía Metodológica** — DOCX que el implementador sube a Drive y abre como Google Doc nativo. Le explica al cliente cómo va a funcionar el Discovery: los 3 documentos vivos, la modalidad de cada uno, qué es la "Biblia".

Ambos se envían **en secuencia**: primero la Bienvenida, después la Guía. Comparten la mayoría de los inputs, por eso son una sola skill.

**Dónde encaja en la metodología:** PASO 1 de Etapa 1, entre la auditoría web (que produce el Doc 0 interno) y el PASO 2 del Discovery (que produce los 4 documentos). La skill orquestadora `prometheo-etapa1` la invoca en sus pasos 1.2 y 1.3.

```
PASO 1 — PRE-DISCOVERY
├── 1.1 Auditoría web + IG     → skill prometheo-auditoria-web   → Doc 0 (interno)
├── 1.2 Doc de Bienvenida      → ESTA SKILL                      → DOCX (cliente-facing)
└── 1.3 Guía Metodológica      → ESTA SKILL                      → DOCX → Google Doc (cliente-facing)
```

---

## REGLA DE ORO

Esta skill **redacta y maqueta**, no inventa. Todo dato del negocio del cliente que aparezca
en el Doc de Bienvenida tiene que venir del Doc 0 (auditoría web). Si un dato no está en
el Doc 0, no se inventa: o se omite, o pasa a la sección "Qué nos queda por entender".

---

## INPUTS QUE NECESITA LA SKILL

Antes de generar nada, el implementador tiene que tener resueltos estos inputs. Si falta
alguno, **pedirlo antes de avanzar** — no completar con supuestos.

### Inputs obligatorios

| Input | Para qué se usa | Origen |
|---|---|---|
| Nombre del cliente | Título, encabezados, todo el cuerpo de ambos docs | Implementador |
| Rubro / vertical | Adapta ejemplos, dominios, tipología macro | Implementador |
| Doc 0 — Auditoría web | Sección 1 de la Bienvenida (datos verificados) | skill `prometheo-auditoria-web` |
| Consultor asignado | Sección 5 de la Bienvenida (nombre, perfil, rol) | Implementador |
| N estimado de reuniones | Sección 3 de Bienvenida + Doc 1 de la Guía | Implementador |

### Inputs opcionales

| Input | Efecto si está / si falta |
|---|---|
| Foto del consultor | Si está: se incrusta en la tarjeta de Sección 5. Si falta: se deja recuadro placeholder, el implementador la agrega después |
| Links a los 3 docs del Discovery | Si están: la Guía los enlaza. Si faltan: la Guía no los menciona (TKVA real no los tenía) |
| ID de la carpeta Drive del cliente | Si está: la skill sube el DOCX de la Guía a esa carpeta. Si falta: el implementador lo sube manualmente. En ambos casos el implementador lo abre como Google Doc |
| ¿El cliente ya tiene CRM? | Si sí: se ajusta la profundidad de la explicación del Documento 3 en la Guía |

---

## DECISIÓN DE FORMATO (FIJA)

| Documento | Formato generado | Por qué | Cómo se entrega / usa |
|---|---|---|---|
| Doc de Bienvenida | **DOCX** | Se envía, no se navega. Tablas e imágenes ricas que la librería `docx` maqueta perfecto | Archivo en `/mnt/user-data/outputs/`. El implementador lo exporta a PDF antes de mandarlo (como el `AUREA_Hub_-_Bienvenida_TKVA.pdf`) |
| Guía Metodológica | **DOCX** | Tiene tabla de 4 columnas e imagen que tienen que verse bien — DOCX las maqueta nativas. Después se vuelve Google Doc | Archivo en `/mnt/user-data/outputs/`. El implementador lo sube a la carpeta Drive del cliente y hace **"Abrir con Google Docs"** → queda Google Doc nativo, navegable, con la tabla intacta |

**Por qué los dos son DOCX y no Google Doc directo:** la integración de Drive disponible
**no convierte** archivos a Google Doc nativo (probado: `text/plain` y `text/html` quedan
como archivos sueltos, la tabla se pierde o no se forma). El camino confiable es generar
DOCX —donde la librería `docx` maqueta tablas e imágenes impecables— y dejar que Google
Docs haga la conversión al importar, que sí preserva todo. La Guía termina siendo un
Google Doc igual; solo que nace DOCX y se convierte con un clic del implementador.

Esta decisión es convención AUREA, no se cambia por cliente.

---

## ORDEN DE EJECUCIÓN

1. **Confirmar inputs.** Revisar la tabla de inputs obligatorios. Si falta alguno, pedirlo y frenar.
2. **Leer el Doc 0.** Es la fuente de los datos verificables del cliente. Marcar qué se sabe y qué queda abierto.
3. **Generar el Doc de Bienvenida** (DOCX) → ver módulo `doc-bienvenida.md`.
4. **Checkpoint con el implementador.** No avanzar a la Guía sin que el Doc de Bienvenida esté validado.
5. **Generar la Guía Metodológica** (DOCX) → ver módulo `guia-metodologica.md`.
6. **Entregar.** Ambos DOCX presentados al implementador. Indicarle que la Guía se sube a Drive y se abre como Google Doc.

---

## MÓDULOS DE LA SKILL

| Módulo | Qué contiene | Cuándo se lee |
|---|---|---|
| `doc-bienvenida.md` | Estructura completa del DOCX de Bienvenida — encabezado + 5 secciones, contenido fijo vs adaptable, maquetación, código de generación | Antes de generar la Bienvenida |
| `guia-metodologica.md` | Estructura completa de la Guía — apertura + 3 documentos + cierre, qué es fijo, cómo generar el DOCX y convertirlo a Google Doc | Antes de generar la Guía |

---

## CONVENCIONES VISUALES

Ambos documentos usan la paleta AUREA. Ver `01-metodologia/07-convenciones-aurea/01-paleta-y-colores.md`.

Resumen de lo aplicable acá:
- **Morado AUREA `#7C5CBF`** — eyebrow de marca, identidad
- **Azul AUREA `#5B8FD9`** — callouts, cajas destacadas, instrucciones
- **Oscuro AUREA `#2D2D3D`** — texto principal, títulos
- **Gris AUREA `#7A7A7A`** — texto secundario
- Logo AUREA Hub arriba a la izquierda en la Bienvenida
- Numeración de secciones formato "1 · Título" en la Bienvenida

---

## CASOS DE REFERENCIA

| Documento | Caso de referencia | Ubicación |
|---|---|---|
| Doc de Bienvenida | `AUREA_Hub_-_Bienvenida_TKVA` | `08-casos-referencia/TKVA-real-estate/` |
| Guía Metodológica | `Guia-Metodologica-TKVA` | `08-casos-referencia/TKVA-real-estate/` |

TKVA es un cliente desarrollista inmobiliario. Los documentos reales valen como referencia
de tono, nivel de detalle y estructura. Para clientes de otras verticales, la estructura
se mantiene; cambian los ejemplos y la tipología macro.

---

## ERRORES COMUNES A EVITAR

| Error | Por qué está mal |
|---|---|
| Inventar números en la Sección 1 de la Bienvenida | El cliente detecta el dato falso y se pierde la confianza. Solo datos del Doc 0 |
| Generar la Bienvenida sin Doc 0 | La Sección 1 queda vacía o inventada. El Doc 0 es input obligatorio |
| Explicarle al cliente qué es un Smart Tag o una Variable | El cliente no necesita la taxonomía CRM en este momento. Lenguaje de negocio |
| Entregar la Guía sin avisar que se abre como Google Doc | El implementador tiene que subirla a Drive y hacer "Abrir con Google Docs" — si no, queda un DOCX suelto y pierde navegabilidad |
| Saltear el checkpoint entre los 2 documentos | El implementador valida la Bienvenida antes de que se genere la Guía |
| Omitir "Qué nos queda por entender" en la Sección 1 | La honestidad sobre lo que falta es parte del valor del documento |

---

## RELACIÓN CON OTRAS SKILLS

| Skill | Relación |
|---|---|
| `prometheo-auditoria-web` | Produce el Doc 0, input obligatorio de esta skill. La auditoría dispara esta skill al cerrar el Paso 1.1 |
| `prometheo-etapa1` | Skill orquestadora — invoca esta skill en sus pasos 1.2 y 1.3 |
| `prometheo-discovery-transversal` | Toma el relevo en el Paso 2 (genera los 4 documentos del Discovery). No se solapa: esos son documentos distintos, de otro momento |
| Skill vertical del rubro | Aporta los ejemplos y la tipología macro que adaptan el contenido de ambos documentos |
