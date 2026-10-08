# 01 — Paleta y Colores AUREA

**Sistema de color para todos los outputs cliente-facing y materiales internos.**

---

## Paleta principal

| Color | Hex | Uso conceptual |
|---|---|---|
| Morado AUREA | `#7C5CBF` | Identidad de marca · seguridad · autonomía del agente |
| Naranja AUREA | `#E8943A` | **Soporte** · Smart Tags · acciones operativas |
| Azul AUREA | `#5B8FD9` | Variables · información · FAQ |
| Verde AUREA | `#4CAF80` | Venta · conversión · resultados positivos |
| Rojo AUREA | `#E84545` | **Urgencia / alerta** · bloqueos críticos · errores |
| Coral AUREA | `#F37D6E` | Estados intermedios · resultados de procesos |
| Teal AUREA | `#3FA89E` | Postventa · seguimiento · estados estables |
| Gris AUREA | `#7A7A7A` | Texto secundario · etiquetas técnicas · footers |
| Oscuro AUREA | `#2D2D3D` | Texto principal · headers · backgrounds densos |

---

## Paleta secundaria (tonos claros para fondos)

Cada color principal tiene una versión clara para usar como fondo de cards:

| Color principal | Versión clara hex | Uso |
|---|---|---|
| Morado claro | `#EDE7F8` | Fondo de cards de Roles / Autonomía |
| Naranja claro | `#FFE5C2` | Fondo de cards de proceso **Soporte** + notas AUREA |
| Azul claro | `#E3EEFC` | Fondo de cards de Variables · proceso FAQ |
| Verde claro | `#E1F5EA` | Fondo de cards de proceso Venta |
| Rojo claro | `#FBE3E3` | Fondo de cards de proceso **Urgencia / alerta** |
| Coral claro | `#FDE3DE` | Fondo de cards de procesos intermedios |
| Teal claro | `#DDEFEC` | Fondo de cards de Postventa |
| Gris claro | `#F0F0F0` | Fondo de cards desactivadas / no aplica |
| Amarillo feedback | `#FFF9D6` | Fondo de bloques de feedback del cliente |

---

## Asignación por categoría conceptual

### Por proceso del CRM

| Proceso | Color principal | Color claro fondo |
|---|---|---|
| Venta | Verde `#4CAF80` | `#E1F5EA` |
| **Soporte** | **Naranja `#E8943A`** | `#FFE5C2` |
| FAQ | Azul `#5B8FD9` | `#E3EEFC` |
| Seguridad | Morado `#7C5CBF` | `#EDE7F8` |
| Postventa | Gris `#7A7A7A` | `#F0F0F0` |
| **Urgencia / alerta** | **Rojo `#E84545`** | `#FBE3E3` |
| Otros (outlet, B2B) | Teal `#3FA89E` | `#DDEFEC` |
| Derivación general | Coral `#F37D6E` | `#FDE3DE` |

**Cambios importantes respecto a versiones anteriores:**

- El **soporte** ahora va en naranja (antes iba en rojo). Razón: soporte es un proceso normal del negocio, no una emergencia. El naranja es el color correcto.
- El **rojo** ahora se reserva para **urgencia/alerta** — bloqueos críticos, errores que el equipo humano debe atender de inmediato. Aparece poco en gráficos comunes, mucho en alertas operativas.
- La **postventa** pasó a gris (antes era teal). Razón: postventa es un proceso de "mantenimiento" del cliente activo, encaja mejor con neutralidad gris.
- El **teal** queda libre para procesos especiales (outlet, B2B, otros embudos del cliente).

### Por tipo de elemento del DOCX

| Elemento | Color principal |
|---|---|
| Banner sección Estrategia | Verde `#4CAF80` |
| Banner sección Variables | Azul `#5B8FD9` |
| Banner sección Smart Tags | Naranja `#E8943A` |
| Banner sección Roles / Autonomía | Morado `#7C5CBF` |
| Banner sección Seguimientos | Teal `#3FA89E` |
| Banner sección Reglas Distribución | Coral `#F37D6E` |
| Banner sección Pendientes / Próximos pasos | Gris `#7A7A7A` |

### Por tipo de anotación (markup interno)

| Tipo | Color principal | Cuándo aplicar |
|---|---|---|
| ⚫ Nota AUREA interna | Naranja `#E8943A` | Comentarios internos del consultor, NO van al cliente final |
| 🔵 Instrucción para cliente | Azul `#5B8FD9` | Tareas asíncronas que el cliente tiene que completar |
| 🟠 Hipótesis a validar | Coral `#F37D6E` | Cuando AUREA propone algo que el cliente tiene que confirmar |
| 🔴 Bloqueante | Rojo `#E84545` | Sin resolver esto, no se puede avanzar al Go-Live |
| ⚪ Funcionalidad futura | Gris `#7A7A7A` | Fase 2 / Post-MVP — visible pero no urgente |
| 🟢 Validado | Verde `#4CAF80` | Hipótesis confirmada por el cliente o por el bot oficial de Prometheo |
| 🟦 Decisión cerrada | Azul oscuro `#2D5FA8` | Decisión definitiva, no se vuelve a discutir |

---

## Reglas de aplicación

### Regla 1 — Consistencia entre el DOCX y los gráficos

Si en el DOCX usás verde para Venta, en TODOS los gráficos relacionados a Venta usás el mismo verde. No cambiar por sección.

### Regla 2 — Solo un color principal por elemento

Un mismo elemento (card, bullet, tag) usa un color principal + su versión clara para fondo. Mezclar colores rompe la jerarquía visual.

### Regla 3 — Contraste de texto

Sobre fondos claros (versiones claras) → texto en oscuro `#2D2D3D`.
Sobre fondos oscuros (versiones principales saturadas) → texto en blanco `#FFFFFF`.

### Regla 4 — Notas AUREA siempre en naranja claro

Las cajas "NOTA AUREA" que explican decisiones al cliente siempre van con fondo naranja claro `#FFE5C2`. Esto las hace identificables a primera vista.

### Regla 5 — Bloques de feedback siempre en amarillo

Las cajas donde el cliente deja feedback al final de cada sección siempre van con fondo amarillo `#FFF9D6`. Esto las hace inmediatamente identificables como "acá tengo que escribir".

### Regla 6 — Grises para info técnica entre paréntesis

Cuando se muestra sintaxis técnica entre paréntesis después de una frase comprensible:

```
"Cuando la conversación es de venta (proceso_actual = venta)"
                                      ↑
                                      en gris #7A7A7A, font reducido
```

---

## Cómo usar la paleta en gráficos

Ver `02-metodologia-graficos.md` para detalles de cómo aplicar los colores en cada uno de los 8 gráficos del DOCX.

Regla maestra para gráficos:
- **Cajas de proceso** → color del proceso correspondiente
- **Flechas y conexiones** → gris medio `#7A7A7A`
- **Trigger principal** → verde si es positivo, rojo si es de cancelación
- **Resultado final** → coral si es transitorio, verde si es positivo final, gris si es archivado

---

## Errores frecuentes a evitar

| Error | Cómo evitarlo |
|---|---|
| Usar colores aleatorios para banners | Usar la tabla por sección |
| Mezclar paletas (verde Material + verde Bootstrap) | Siempre usar los hex exactos de esta paleta |
| Texto oscuro sobre fondo oscuro saturado | Verificar contraste con la Regla 3 |
| Usar amarillo para algo que no sea feedback | El amarillo es exclusivamente para bloques de feedback |
| Usar el morado en exceso | El morado es de marca, no decorativo. Usar en banners de Roles/Autonomía y poco más |
| Crear nuevos colores sin documentarlos acá | Si necesitás un color nuevo, primero sumarlo a esta paleta con justificación |

---

## Versionado de la paleta

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | Mayo 2026 | Paleta inicial. 9 colores principales + 9 versiones claras + 7 colores de anotación. |

---

## Para profundizar

| Tema | Archivo |
|---|---|
| Metodología de gráficos | `02-metodologia-graficos.md` |
| Naming convention | `03-naming-convention.md` |
| Convenciones DOCX cliente-facing | `../02-ETAPA2-Diseno/04-convenciones-docx-cliente.md` |
| Skill de gráficos | `../../02-skills/02-ETAPA2/prometheo-crm-graphics/SKILL.md` |
