# 02 — Metodología de Gráficos

**Cómo se diseñan los gráficos visuales del DOCX cliente-facing.**

Esta es la versión documentada de la skill `prometheo-crm-graphics` para que cualquier consultor entienda el sistema visual sin tener que abrir la skill operativa.

---

## Filosofía del diseño visual

Los gráficos NO son decoración. Son **información estructurada visualmente** para que el cliente entienda el sistema sin tener que leer 30 páginas.

Principios:
1. **Cada gráfico responde a 1 pregunta concreta del cliente** (ej: "¿qué hace el agente cuando llega un mensaje?")
2. **La información sigue una dirección de lectura clara** (arriba → abajo, izquierda → derecha)
3. **El color comunica categoría** (ver `01-paleta-y-colores.md`)
4. **Los textos son cortos** (máximo 1-2 líneas por caja)
5. **Las flechas indican causalidad o secuencia**, no decoración

---

## Los 8 gráficos del DOCX

### Gráfico 1 — Overview de Variables

**Pregunta que responde:** ¿qué datos del lead captura el agente?

**Estructura:**
- Caja central: "Datos del lead"
- Cajas laterales agrupadas por categoría (Datos básicos · Calificación · Estado · Operativos)
- Cada categoría con 3-6 variables como sub-cajas

**Colores:**
- Caja central: morado AUREA
- Categoría "Básicos": gris claro
- Categoría "Calificación": azul
- Categoría "Estado": teal
- Categoría "Operativos": coral

**Cuándo usarlo:** Sección 5 del DOCX (Variables), al inicio antes de la tabla completa.

---

### Gráfico 2 — Arquitectura de Variables (router + estados)

**Pregunta que responde:** ¿cómo se relaciona la variable router con las variables de estado?

**Estructura:**
- Arriba: `proceso_actual` como diamond (decisión)
- Abajo: ramificaciones a cada `estado_X` correspondiente
- Cada rama con su color de proceso

**Colores:**
- proceso_actual (diamond): azul `#5B8FD9`
- estado_venta: verde
- estado_soporte: rojo
- estado_faq: azul
- estado_postventa: teal
- estado_seguridad: morado

**Cuándo usarlo:** Sección 5 del DOCX (Variables), después de la tabla.

---

### Gráfico 3 — Overview de Smart Tags

**Pregunta que responde:** ¿qué tags hay y qué hacen?

**Estructura:**
- 2 cards horizontales, una por tag
- Cada card con: nombre de tag (header) + subtitle (qué hace) + bullet de acciones

**Colores:**
- Card `#seguimiento_activo`: naranja
- Card `#derivar_a_humano`: rojo

**Cuándo usarlo:** Sección 6 del DOCX (Smart Tags), reemplazando una tabla.

---

### Gráficos 4-6 — Los 3 Escenarios de Ejemplo

**Pregunta que responde:** ¿cómo se ve el sistema funcionando con un caso concreto?

**Estructura de cada escenario (vertical, top-down):**

```
┌─────────────────────────────────┐
│  📨 SITUACIÓN                    │
│  "Mensaje del usuario entre       │
│  comillas"                        │
└─────────────────────────────────┘
              ↓
┌─────────────────────────────────┐
│  🔄 PROCESO IDENTIFICADO         │
│  Embudo: [nombre]                 │
│  Variable router: proceso_actual  │
│  = valor                          │
└─────────────────────────────────┘
              ↓
┌─────────────────────────────────┐
│  💾 VARIABLES QUE LLENA           │
│  • var_1 = valor                  │
│  • var_2 = valor                  │
│  • var_3 = valor                  │
└─────────────────────────────────┘
              ↓
┌─────────────────────────────────┐
│  🏷️ SMART TAGS QUE SE DISPARAN   │
│  Tag activa: #nombre              │
└─────────────────────────────────┘
              ↓
┌─────────────────────────────────┐
│  ⚡ QUÉ HACE EL AGENTE            │
│  - Respuesta inmediata: ...       │
│  - Notificación al equipo: ...    │
│  - Seguimiento programado: ...    │
└─────────────────────────────────┘
```

**Colores:**
- Cada escenario usa el color del proceso que representa:
  - Escenario de Venta → verde
  - Escenario de Soporte → rojo
  - Escenario de FAQ → azul
  - Etcétera

**Reglas:**
- Los 3 escenarios deben mostrar **3 procesos distintos**
- Si el cliente tiene menos de 3 procesos, mostrar 3 casos del mismo proceso con resultados distintos
- Cada escenario es un gráfico independiente, no se combinan

**Cuándo usarlos:** Sección 7 del DOCX (3 Escenarios), una página por escenario.

---

### Gráfico 7 — Fórmula de Seguimiento

**Pregunta que responde:** ¿cómo se decide cuándo el agente manda un follow-up?

**Estructura (vertical apilada):**

```
   REQUISITO 1 — TAG
   ┌────────────────────┐
   │  #seguimiento_     │   ← Verde (trigger inicial)
   │   activo activa    │
   └────────────────────┘
            +
   REQUISITO 2 — PROCESO
   ┌────────────────────┐
   │  proceso_actual    │   ← Color del proceso
   │  = [valor]         │
   └────────────────────┘
            +
   REQUISITO 3 — ESTADO
   ┌────────────────────┐
   │  estado_X          │   ← Color del proceso, más claro
   │  = [valor]         │
   └────────────────────┘
            +
   REQUISITO 4 — TIEMPO
   ┌────────────────────┐
   │  [N] horas/días    │   ← Coral o naranja
   │  sin respuesta     │
   └────────────────────┘
            ↓
   ┌────────────────────┐
   │  → EL AGENTE       │   ← Coral fuerte (resultado)
   │    ENVÍA MENSAJE   │
   └────────────────────┘
```

**Reglas adicionales:**
- Si alguno de los 4 requisitos falla, el seguimiento NO se dispara → mostrar caja de cancelación en rojo al lado
- Las regla de cancelación (si responde el usuario, si aparece #derivar_a_humano) van como nota al pie del gráfico, en gris

**Cuándo usarlo:** Sección 8 del DOCX (Seguimientos), antes de listar los follow-ups específicos.

---

### Gráfico 8 — Distribución de Seguimientos por proceso

**Pregunta que responde:** ¿cuántos follow-ups hay y a qué proceso pertenece cada uno?

**Estructura:**
- Cajas verticales agrupadas por proceso
- Cada caja con: número de FU + nombre descriptivo + tiempo de espera

**Ejemplo visual:**

```
┌─── EMBUDO VENTA ───────────────────────┐
│  FU#1   Recordatorio info        24hs   │
│  FU#2   Reactivación            72hs    │
│  FU#3   Última oportunidad      7 días  │
│  FU#4   Reactivación profunda   30 días │
└─────────────────────────────────────────┘

┌─── EMBUDO SOPORTE ──────────────────────┐
│  FU#5   Check de resolución     48hs    │
└─────────────────────────────────────────┘

┌─── EMBUDO POSTVENTA ────────────────────┐
│  FU#6   Satisfacción            7 días  │
└─────────────────────────────────────────┘
```

**Colores:**
- Cada grupo con el color de su proceso

**Cuándo usarlo:** Sección 8 del DOCX, después de la Fórmula de Seguimiento.

---

## Gráficos adicionales (según cliente)

### Gráfico extra A — Mapa de Embudos

Si el cliente tiene 3+ embudos, sumar al inicio del DOCX (Sección 4) un mapa visual de los embudos con sus etapas internas.

### Gráfico extra B — Flujo de Derivación

Si el cliente tiene `tipo_derivacion` con 4+ valores, sumar en Sección 9 (Reglas de Distribución) un flujo top-down que muestre:
- Trigger: `#derivar_a_humano` activa
- Diamond: valor de `tipo_derivacion`
- Ramificaciones: cada tipo va a un responsable distinto

### Gráfico extra C — Notificaciones Urgentes 24/7

Si el cliente tiene `severidad_caso = alta`, sumar un gráfico específico mostrando:
- Trigger: severidad_caso = alta detectada
- Acción: push 24/7 al responsable + activación de #derivar_a_humano
- Diferencia con flujo normal (que respeta horario laboral)

---

## Reglas de diseño común a todos los gráficos

### Regla 1 — Dirección de lectura
- Vertical: arriba → abajo
- Horizontal: izquierda → derecha
- NO mezclar direcciones en un mismo gráfico

### Regla 2 — Conexiones
- Flechas: `→` o `↓` simples, en gris `#7A7A7A`
- NO usar flechas curvas o estilos elaborados
- Texto sobre la flecha solo si es indispensable

### Regla 3 — Cajas
- Bordes redondeados sutiles (radius 4-8px)
- Padding interno generoso (texto no pegado al borde)
- Sombra muy sutil o ninguna

### Regla 4 — Tipografía
- Texto principal en caja: bold, 11-13pt
- Texto secundario en caja: regular, 9-11pt, color secundario
- Labels de flechas: 9pt, gris medio

### Regla 5 — Tamaño del gráfico
- Cada gráfico debe entrar en máximo media página del DOCX
- Si requiere más, dividir en 2 gráficos relacionados

### Regla 6 — Iconos
- Usar emojis simbólicos (📨, 💾, 🏷️, ⚡, 🔄) solo en los escenarios de ejemplo
- En los demás gráficos: sin iconos decorativos, solo texto + color

### Regla 7 — Footer técnico
- Si el gráfico tiene información técnica subyacente (sintaxis Prometheo, nombres exactos de variables), poner como footer en gris pequeño

---

## "Explicado:" — Gráficos pedagógicos adicionales

Para conceptos especialmente difíciles de explicar (ej: por qué `proceso_actual` gobierna las variables de estado, o cómo se cancela un follow-up cuando aparece #derivar_a_humano), AUREA crea gráficos "Explicado:" como complemento.

**Patrón visual estándar de los "Explicado:"**

```
   GRÁFICO PRINCIPAL    →    "Explicado:"
   (técnico)                  (pedagógico)
```

El gráfico "Explicado:" usa:
- Verde para el trigger principal
- Amber / amarillo para condiciones intermedias
- Coral para resultado
- Rojo para cancelaciones
- Gris claro para footer con regla operativa textual

Estos son opcionales pero suman mucho cuando el cliente tiene resistencia a entender un concepto.

---

## Cómo se generan los gráficos en el DOCX

Los gráficos se generan con SVG inline o como imágenes PNG embebidas en el DOCX usando `python-docx`. La skill `prometheo-crm-graphics` tiene los templates específicos.

**Reglas de implementación técnica:**

- SVG preferido si el gráfico es simple (cajas + flechas)
- PNG si el gráfico requiere efectos visuales que SVG no soporta bien
- Resolución mínima 300 DPI para PNG
- Tamaño máximo de archivo: 200KB por gráfico

---

## Validación de los gráficos antes de entregar

| Check | Cómo verificar |
|---|---|
| Cada gráfico responde a 1 pregunta del cliente | Leer el gráfico y preguntarse: "¿qué duda resuelve esto?" |
| Direcciones de lectura consistentes | No hay flechas zigzagueando |
| Paleta de colores aplicada según `01-paleta-y-colores.md` | Verificar hex exactos |
| Texto legible a 100% de zoom | Mínimo 9pt para labels |
| Cada gráfico entra en media página | Verificar tamaño en el DOCX final |
| Iconos solo en los 3 escenarios de ejemplo | Resto sin emojis decorativos |
| Los 8 gráficos obligatorios están presentes | Contar en el DOCX final |

---

## Errores frecuentes a evitar

| Error | Solución |
|---|---|
| Gráficos demasiado densos (muchas cajas pequeñas) | Dividir en 2 gráficos relacionados |
| Mezclar paletas (un gris en un gráfico, otro gris en otro) | Usar hex exactos de la paleta |
| Texto largo dentro de cajas | Máximo 1-2 líneas; si necesita más, va como nota al pie |
| Conexiones con flechas estilizadas | Flechas simples siempre |
| Olvidar el color de proceso en gráficos de escenarios | Cada escenario hereda el color de su proceso |
| Gráficos sin trigger inicial claro | Siempre hay una caja "trigger" arriba |

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Paleta de colores | `01-paleta-y-colores.md` |
| Convenciones DOCX cliente-facing | `../02-ETAPA2-Diseno/04-convenciones-docx-cliente.md` |
| Skill de gráficos | `../../02-skills/02-ETAPA2/prometheo-crm-graphics/SKILL.md` |
