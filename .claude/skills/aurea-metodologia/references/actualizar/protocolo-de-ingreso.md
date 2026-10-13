---
consultar-cuando: clasificar una mejora y decidir dónde va antes de editar la skill
disparadores: "dónde va esto", "es patrón o instancia", "archivo dueño", "derogar"
fuente-única-de: la clasificación y ubicación de mejoras (mapa de archivos dueños)
combina-con: actualizar/procedimiento, metodologia-correccion-agente
---

# Protocolo de ingreso de una mejora a la metodología

Este archivo dice, para cada aprendizaje nuevo, **qué es**, **dónde va** y **qué operación se
hace**. Es lo que evita que una mejora se superponga con algo que ya existe o rompa algo que
funciona.

## Contenido
1. Las cuatro preguntas de clasificación
2. Mapa de destinos (dónde vive cada cosa)
3. Las cinco operaciones
4. Cómo detectar si ya existe (antes de escribir)
5. Plantillas

---

## 1. Las cuatro preguntas de clasificación

Para cada aprendizaje, respondé en este orden:

**a) ¿Es patrón o instancia?**
- **Patrón:** la forma de la lógica, sin valores concretos. Sirve para otro cliente. Sube a la
  metodología.
- **Instancia:** el valor de hoy de un cliente (un precio, un nombre, una zona, una lista de
  productos). NO entra a la metodología: vive en el material del cliente. Si no se puede
  escribir sin nombrar un valor concreto, es instancia.

**b) ¿En cuántos rubros distintos se vio?**
- Un solo cliente → candidato, en el archivo de su rubro, marcado "candidato a subir".
- Dos clientes del mismo rubro → doctrina de ese rubro (no es transversal).
- Dos rubros distintos → transversal.
Que algo "suene universal" no alcanza: sube lo que efectivamente apareció en dos rubros.

**c) ¿De qué tipo es?** (define el archivo dueño, ver mapa abajo)
Comportamiento del agente · lógica de venta · modelo de datos (embudos, tags, variables) ·
calificación · integración · plataforma · patrón de corrección · testing · proveedor ·
entregable · producto (IC) · proceso por etapa.

**d) ¿Qué relación tiene con lo que ya existe?**
- No existe nada parecido → **agregar**.
- Existe y lo amplía → **complementar**.
- Existe y lo contradice porque cambió la práctica → **corregir** o **derogar**.
- Existe igual → **no hacer nada** (anotarlo como evidencia nueva si suma un rubro).

## 2. Mapa de destinos

Cada tema tiene **un solo archivo dueño** (su encabezado lo declara en `fuente-única-de`).
Los demás archivos apuntan a él; no copian su contenido.

| Tipo de aprendizaje | Archivo dueño (dentro de `references/01-metodologia/` salvo indicación) |
|---|---|
| Cómo conversa el agente (transversal) | `02-ETAPA2-Diseno/principios-transversales-agente.md` |
| Cómo vende el agente (transversal) | `02-ETAPA2-Diseno/logica-comercial-transversal.md` |
| Lógica de un rubro (venta, objeciones, variables típicas) | `06-rubros/<rubro>.md` |
| Embudos, tags, variables: el criterio | `02-ETAPA2-Diseno/embudos-y-tags.md` |
| Embudos, tags, variables: el molde por rubro | `02-ETAPA2-Diseno/arquitectura-crm-por-rubro.md` |
| Calificación de leads, hot lead, recalificación | `references/calificacion/00-criterio-calificacion.md` y `rubros/` |
| Regla oficial de diseño | `02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md` |
| Fuente de datos (Tokko, Sheets, PrestaShop) | `02-ETAPA2-Diseno/08-reglas-integracion-catalogo.md` |
| Límite o comportamiento confirmado de Prometheo | `02-ETAPA2-Diseno/restricciones-plataforma-prometheo.md` |
| Duda abierta con la plataforma | `02-ETAPA2-Diseno/pendientes-itesa.md` |
| Error recurrente de un agente | `02-ETAPA2-Diseno/10-patrones-correccion-agente.md` |
| Cómo se procesa feedback, barrido, términos derogados | `02-ETAPA2-Diseno/metodologia-correccion-agente.md` |
| Testing | `02-ETAPA2-Diseno/guion-testing.md` |
| Seguimientos y mensajería | `02-ETAPA2-Diseno/framework-seguimientos.md` |
| Proveedor (ITESA) | `02-ETAPA2-Diseno/gestion-proveedor-itesa.md` |
| Consumo de tokens (decisiones) | `02-ETAPA2-Diseno/ahorro-de-tokens.md` |
| Consumo de tokens (tarifas, medición) | `references/calificacion/ahorro-de-tokens-detalle.md` |
| Entregables por etapa | `00-OUTPUTS-POR-ETAPA.md` |
| Inteligencia Comercial | `02-ETAPA2-Diseno/inteligencia-comercial-producto.md` |

Si la tabla de arriba quedó desactualizada respecto del skill real, la verdad está en los
encabezados `fuente-única-de` de cada archivo: buscalos con
`grep -rn "fuente-única-de" references/`.

## 3. Las cinco operaciones

**Agregar** (no existe nada): se suma al archivo dueño como sección o ítem nuevo. Se crea un
archivo nuevo **solo** si no hay dueño posible. Archivo nuevo = encabezado de auto-ruteo
completo + una línea en `SKILL.md` (si cambia el ruteo) + una línea en `00-CONSULTA.md` y
`00-INDEX.md`.

**Complementar** (existe y lo amplía): se agrega debajo de lo que ya está, con la evidencia
nueva. No se reescribe lo existente. Si un candidato gana su segundo rubro, se lo promueve:
se mueve al archivo transversal y en el rubro queda un puntero.

**Corregir** (existe y estaba mal o cambió la práctica): se reemplaza el texto, y en el mismo
lugar queda una línea "Actualización vX: antes decía…, ahora…, por qué". Nunca se borra en
silencio.

**Derogar** (un concepto entero deja de valer): además de corregirlo donde nace, se suma una
fila a la tabla de **términos derogados** en `metodologia-correccion-agente.md`, y se
**propaga** a todos los archivos que lo nombran (incluidas las copias de otras skills en
`references/02-skills/`). La auditoría falla si queda uno vigente.

**Archivar** (algo que no es molde pero conviene conservar): se marca en sus primeras líneas
con "Registro histórico" o "CASO HISTÓRICO". La auditoría no lo revisa por términos
derogados. No se reescribe su contenido.

## 4. Cómo detectar si ya existe (antes de escribir)

1. Buscá las palabras clave del aprendizaje en todo el skill:
   `grep -rni "<palabra>" references/ SKILL.md`
2. Leé los encabezados `fuente-única-de` de los archivos candidatos.
3. Si encontrás algo parecido, leé ese párrafo completo antes de decidir entre complementar,
   corregir o no hacer nada.
4. Si dos archivos ya hablan del tema, el dueño es el que lo declara en `fuente-única-de`; el
   otro debe apuntar, no repetir.

## 5. Plantillas

**Encabezado de auto-ruteo (archivo nuevo de doctrina):**
```
---
consultar-cuando: <en qué tarea se lee este archivo>
disparadores: "<frase>", "<frase>"
fuente-única-de: <el tema del que este archivo es el único dueño>
combina-con: <archivos que se leen junto con este>
---
```

**Entrada de CHANGELOG (va arriba de todo en `references/CHANGELOG.md`):**
```
## vX.Y - <día> <mes> <año>

<una o dos líneas: qué cambió y por qué>

**Agregado** · **Complementado** · **Corregido** · **Derogado** (usá solo los que apliquen)
- `<archivo>`: <qué>

**Auditado con scripts/auditar.py**: <resultado en una línea>

**Pendiente:** <decisiones abiertas, si hay>
```

**Fila de término derogado:**
```
| `<término>` o "<frase>" | vX.Y | <qué lo reemplaza> |
```
