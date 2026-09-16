# Pendientes con ITESA

> Buzón único de dudas sobre la plataforma Prometheo que están **sin confirmar** y que
> requieren respuesta del equipo de ITESA (desarrolladores de Prometheo). Ninguna de estas
> bloquea el trabajo — son precisiones a cerrar cuando haya contacto con ITESA.
>
> Cuando una duda se resuelve: se quita de esta lista, se incorpora al archivo que
> corresponda (restricciones, embudos-y-tags, integraciones, reglas) y se registra en
> `CHANGELOG.md`.

---

## Dudas abiertas

| # | Duda | Por qué importa | Dónde impacta al resolverse |
|---|---|---|---|
| 1 | ¿El uso de **Prometheo Connect** consume el cupo de "integración de marketplace" del plan (Pro = 1, Enterprise = 2), o es independiente? | Define qué se le puede prometer a un cliente de plan Pro: si ya usa Connect, ¿le queda cupo para una integración nativa de marketplace o no? | `restricciones-plataforma-prometheo.md` (restricción 7 y 14) |
| 2 | **PrestaShop** — alcance de la sincronización nativa: ¿sincroniza catálogo, precios y stock? ¿con qué frecuencia? | Caso EDFAN Productos. Define qué datos puede leer el agente y qué hay que resolver por otra vía. | `integraciones-por-rubro.md` (ficha PrestaShop + fila insumos) |

---

## Resueltas — registro

> Dudas que estuvieron en esta lista y ya se confirmaron. Se dejan registradas para
> trazabilidad.

| Duda | Resolución | Confirmado por |
|---|---|---|
| ¿La etapa de embudo es internamente un tag? | Sí, internamente es un tag. Por eso un tag no puede estar en dos embudos. | ITESA |
| ¿En qué planes está Prometheo Connect? | Desde el plan Pro. | ITESA (captura de planes) |
| ¿Hay límite de cantidad de embudos por plan? | Sin límite conocido. | ITESA |
| ¿PrestaShop tiene integración nativa? | Sí, es integración nativa. | ITESA |
| ¿La creación de leads en Tokko se dispara por etapa o por tag? | La plataforma permite ambas. La metodología AUREA lo hace por Smart Tag — depende de cómo se configure la tag. | ITESA |

---

## Dudas abiertas agregadas en v1.15

**Inconsistencia y parcialidad de resultados de búsqueda** (detectado con Tokko, agente
Martina; aplica a cualquier integración de catálogo):
- ¿Hay un límite de resultados por consulta? Si lo hay, ¿cuál es y el agente puede saber que
  la respuesta quedó truncada?
- ¿Por qué cambia el conjunto de resultados entre consultas equivalentes? ¿Ranking,
  aleatoriedad, paginación?
- ¿El agente puede conocer el total de resultados, para decir "le muestro tres de catorce" en
  vez de dar a entender que eso es todo?
- ¿Cómo se consulta a nivel entidad (panorama de proyectos/categorías) vs a nivel unidad?

Impacto: mientras no haya respuesta, el agente no puede declarar parcial lo que la integración
no marca como parcial. La mitigación (panorama desde catálogo embebido, nunca afirmar "no hay"
desde un resultado parcial) está en `08-reglas-integracion-catalogo.md`.

---

## Cómo se agrega un pendiente

Cualquier duda de comportamiento de plataforma que surja trabajando (en discovery, diseño
o implementación) y que no se pueda confirmar con el bot oficial, se anota acá como fila
nueva en "Dudas abiertas". Es la aplicación de la regla de oro: no se asume — se anota y se
pregunta.
