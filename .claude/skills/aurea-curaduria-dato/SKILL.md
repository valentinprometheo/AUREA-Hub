---
name: aurea-curaduria-dato
description: Curaduría, trazabilidad y auditoría del dato comercial para los tableros de Inteligencia Comercial de AUREA (Prometheo + Tokko + canales). Usala SIEMPRE que haya que decidir qué número se muestra y cómo, curar un export de Prometheo, definir denominadores, auditar cobertura de variables, cruzar datos cualitativos con cuantitativos, separar demanda real de no-demanda, definir etapas del embudo por evidencia, o marcar faltantes en una pestaña de Demanda, Venta CRM o Calidad de datos. Activar ante "curar", "auditar el dato", "qué tan confiable es", "sobre qué base", "denominador", "cobertura", "faltantes", "sin dato", "atribución de anuncio", "etapa vs evidencia", "esto se puede mostrar al cliente".
---

# Curaduría del dato comercial (AUREA · Inteligencia Comercial)

El tablero IC se le muestra a un cliente. Cada número que aparece es una **afirmación
con consecuencias**: alguien va a mover presupuesto, priorizar un proyecto o salir a
recontactar por lo que diga esta pantalla. Esta skill define **qué se puede afirmar,
con qué base, y cómo se marca lo que no se puede**.

No es una skill de diseño (eso es `aurea-dashboard-design`) ni de metodología de CRM
(eso es `aurea-metodologia`). Es la capa de **criterio sobre el dato**: la que decide
si un número entra al tablero, como titular, como bullet, o como faltante.

## De dónde viene este criterio (trazabilidad)

Se cruzan dos disciplinas que resuelven mitades distintas del mismo problema:

**De `attribution` (epistemología del número).** Su aporte: un número nunca es la
verdad, es un modelo con supuestos. Declará el modelo. Mostrá dos lecturas cuando
difieren, porque *el gap es el insight*. Nunca sumes fuentes que reclaman el mismo
hecho. Los faltantes son estructurales, no errores de carga. Lo auto-reportado
(cualitativo) es el chequeo fuera de modelo que mantiene honesto al tracking. La
salida lleva **confianza y base**, no una reconciliación falsa al decimal.

**De `revops` (disciplina del registro).** Su aporte: definí antes de automatizar.
Cada etapa tiene criterio de entrada, evidencia requerida y dueño. Fit y engagement,
ninguno solo alcanza. **Bloqueá el avance de etapa si faltan los campos requeridos.**
Tiene que existir señal negativa o pasa cualquiera. La higiene es un ritual, no un
arreglo único.

**El cruce (lo nuestro).** Attribution disciplina *números*, revops disciplina
*registros*. El tablero es donde se encuentran. La jugada que sale de cruzarlos:

> **Portamos la regla de revops "no avanza de etapa sin campos" al reporting:
> un dato no asciende a titular sin cobertura.** Y portamos la regla de attribution
> "todo dato lleva confianza y base" al CRM: cada variable declara cómo se obtuvo.

Eso es la escalera de evidencia, abajo. Todo lo demás se desprende de ahí.

---

## 1. Regla de oro: ningún número sin procedencia

Todo número del tablero carga cuatro cosas. Si no podés responderlas, no lo muestres.

| | Qué es | Ejemplo EDFAN |
|---|---|---|
| **Base** | El denominador real sobre el que se calcula | 518 que declaran zona (no 1.017) |
| **Cobertura** | % de la base total con esa variable cargada | Zona 51%, Perfil 26%, Reuniones 0% |
| **Origen** | Cómo se obtuvo | declarado por el lead / inferido por el agente / calculado / de plataforma |
| **Confianza** | Alta, media o baja, derivada de cobertura + origen | Anuncio 64% + plataforma = media-alta |

El **origen** importa tanto como la cobertura. Un campo al 90% inferido por el agente
es más frágil que uno al 60% declarado por el lead en su propio mensaje.

## 2. La escalera de evidencia (el corazón de la skill)

Define **qué le está permitido hacer a cada dato** según su cobertura sobre la base
relevante. Es la regla de revops ("no avanza sin campos") aplicada al reporte.

| Nivel | Cobertura | Qué puede hacer | Qué NO puede hacer |
|---|---|---|---|
| **Hecho** | ≥ 80% | Titular de card, KPI grande, encabezar un insight | — |
| **Señal** | 40 a 79% | Card con denominador explícito y chip de cobertura | Titular sin decir la base |
| **Indicio** | 10 a 39% | Bullet, tabla, o modo Avanzada | Card propia, porcentaje protagonista |
| **No reportable** | < 10% o campo sin uso | Va a Calidad de datos como faltante | Aparecer como dato en Demanda o Venta |

**Reglas de la escalera:**
- Un Indicio nunca titula. Si la variable está al 10%, el hallazgo real no es el
  ranking de valores: es que está al 10%.
- Un dato puede subir de nivel **cambiando la base**, no maquillando el número.
  Objeción al 10% del total es Indicio; sobre "los que declararon objeción" es una
  Señal legítima, siempre que se diga.
- **No reportable no significa invisible.** Significa que cambia de pestaña: deja de
  ser un dato de demanda y pasa a ser un hallazgo de calidad, con el insight que
  desbloquearía si se completara.

## 3. Denominador honesto (doble lectura)

El error más común y más caro: mostrar "% del total" con la variable a medio llenar.

Siempre que la cobertura sea menor a 80%, se reportan **dos lecturas**:

> Villa Crespo: **283 consultas**, 28% del total, **55% de las 518 que declaran zona**.

La segunda es la que manda para leer el mercado; la primera es la que manda para
dimensionar. Nunca una sola. En el tablero, la base declarada va en el `.r` del
encabezado de la card: `base declarada: 518`.

**Nunca** normalices un multi-select a 100%. Si un lead puede declarar dos zonas,
decilo ("los leads suelen declarar más de una") en vez de forzar la suma.

## 4. El faltante es un hallazgo, no un hueco

Heredado de attribution: "direct" no es un canal, es un problema de medición. Igual acá.

- **Nombralo y dimensionalo.** "Sin anuncio identificado: 366 (36%)" es una barra, no
  una ausencia de barra.
- **Decí qué esconde.** El 36% sin atribución no es ruido: tapa el ROI por campaña.
  El 74% sin perfil no es pereza: impide segmentar por intención.
- **Distinguí tres faltantes distintos**, porque se arreglan distinto:
  1. **Estructural** (el dato no existe de origen: dark social, boca a boca) → se
     resuelve preguntando, no cargando.
  2. **De proceso** (el agente o el equipo no lo completó) → se resuelve con prompt
     y con campos requeridos por etapa.
  3. **De integración** (la fuente no está conectada: gasto de Meta) → se resuelve
     conectando.

## 5. Lo cualitativo audita a lo cuantitativo

El texto libre (dolor, objeción literal, contexto VIP, resumen por IA) no es adorno ni
relleno: es el **chequeo fuera de modelo**. Reglas de curaduría:

- **La cita textual vale más que la paráfrasis.** "Por el momento no estaría dentro de
  mi presupuesto" es evidencia; "objeción de precio" es una categoría.
- **No codifiques a porcentaje con n chico.** Cuatro citas no son un 4%. Si el n no
  llega a Señal, se muestran como citas, sin barra.
- **Buscá la contradicción.** Cuando la categoría cuantitativa y las citas no coinciden,
  ahí está el insight. Si "Ubicación" figura 9 veces pero las frases dicen "es muy
  lejos" en otras 20 conversaciones, la variable está subcargada, no el problema.
- **Una cita es de una persona.** No la presentes como patrón; presentala como color
  que explica un número que ya tenés.

## 6. Etapa declarada vs etapa por evidencia

Aporte directo de revops, y la curaduría que más valor genera en Venta · CRM.

Definí cada etapa con **evidencia requerida**, y después contá **dos veces**: cuántos
tienen el tag y cuántos cumplen la evidencia. La brecha es el hallazgo.

Ejemplo real EDFAN (evidencia = proyecto, zona, perfil, tipo de unidad):

| | Tag declarado | Cumple evidencia (3 de 4 campos) |
|---|---|---|
| Calificado | 6 | 386 |

No es que haya 6 calificados: hay **381 leads calificados de hecho que nadie marcó**.
El embudo no está vacío, está subregistrado. Ese es el número que hay que mostrar.

**Regla operativa:** el agente no debería poder marcar una etapa avanzada sin la
evidencia mínima; y el tablero no debería reportar conversión de etapa mientras la
evidencia y el tag no converjan. Mientras tanto, se muestran las dos columnas.

## 7. Base curada: separar demanda de no-demanda

Antes de cualquier porcentaje, definí **sobre quién estás hablando**. El export trae
todo junto. Un proveedor que ofrece premarcos no es demanda de compra.

Secuencia estándar (EDFAN como ejemplo):

```
1.017  contactos en el export
  -117  no-demanda (proveedores 41, inmobiliarias 55, no fit 28, desarrolladores 4)
=  900  demanda de compra
  -187  nunca respondieron
=  713  demanda real que conversó
```

Cada pestaña declara sobre qué base corre. Demanda puede correr sobre 900; el volumen
del canal corre sobre 1.017. Lo que no se puede es mezclarlas sin avisar.

## 8. Reglas de fuentes (nunca votan sobre lo mismo)

Cada fuente tiene **un rol** y no opina fuera de él:

| Fuente | Manda en | No manda en |
|---|---|---|
| **Prometheo** | Conteo de consultas, tags, calificación, texto de la conversación | Gasto, alcance |
| **Meta / canales** | Gasto, alcance, impresiones, clics | Cuántas consultas reales hubo |
| **Tokko** | Producto: proyectos, unidades, precios, estado de obra | Intención del lead |
| **Cálculo** | Ratios y costos derivados | Nada primario |

- **Nunca sumes entre fuentes.** Si Meta reclama 50 y Prometheo registra 40, hay 40
  consultas con dos relatos, no 90.
- **Un solo conteo maestro.** Prometheo define cuántas consultas hubo; el resto explica
  de dónde vinieron.
- **Leé acuerdo direccional**, no coincidencia exacta.

## 9. Procedimiento de auditoría (el que se corre antes de armar el tablero)

1. **Perfilá cobertura real** de cada columna, tratando `-`, vacío y `0` de relleno
   como ausentes (no como valor).
2. **Clasificá cada variable** en la escalera de evidencia. Esa clasificación decide
   la pestaña donde vive.
3. **Definí la base curada** (paso 7) y anotá sobre qué base corre cada sección.
4. **Calculá los denominadores declarados** por variable y guardalos: son los que van
   en el encabezado de cada card.
5. **Cruzá etapa declarada vs evidencia** (paso 6).
6. **Levantá las citas** que auditan las categorías (paso 5).
7. **Listá los faltantes** clasificados por tipo (paso 4) con el insight que desbloquean.
8. **Recién ahí** armá las cards.

## 10. Cómo se renderiza (liga con `aurea-dashboard-design`)

- **Chip de cobertura** en el `.r` del `ghdr`: `base declarada: 518` o `51% sin dato`.
- **Barra de faltante explícita** dentro de la card, en ámbar, cuando supera el 15%.
- **Tag de nivel** cuando no es Hecho: `Señal`, `Indicio`, `Proyección`, `Estimado`.
- **Doble lectura** en el valor: `283` con subtexto `55% de los que declaran`.
- **Citas** en tarjetas de texto, sin barra ni porcentaje, en modo Avanzada.
- Los faltantes viven en **Calidad de datos**, agrupados por nivel, con el insight que
  desbloquean.

## 11. Checklist antes de publicar

- [ ] Cada card dice sobre qué base corre.
- [ ] Ningún Indicio está titulando.
- [ ] Los faltantes mayores al 15% están dibujados, no omitidos.
- [ ] Ninguna cita se presentó como porcentaje.
- [ ] Ninguna cifra suma dos fuentes.
- [ ] Las etapas muestran declarado y evidencia cuando difieren.
- [ ] Todo lo no reportable está en Calidad de datos con su insight desbloqueable.
- [ ] Si es data real, dice que es real; si es proyección, lo dice en el mismo bloque.

## 12. Anti-patrones

- **El porcentaje huérfano.** "28%" sin decir de qué. Casi siempre esconde una base a medio llenar.
- **El promedio sobre relleno.** Promediar un campo donde el vacío se guardó como `0`.
- **El embudo optimista.** Reportar conversión de etapa con la etapa subregistrada.
- **La cita disfrazada de dato.** Tres frases convertidas en categoría con barra.
- **El faltante borrado.** Sacar del gráfico lo que no tiene dato y dejar que el resto sume 100%.
- **La suma de plataformas.** Meta + Prometheo como si fueran consultas distintas.

---

## Derivación y créditos

Cruce y reescritura propia de AUREA sobre dos skills comunitarias de Corey Haines
(MIT): `attribution` (modelo, confianza, blind spots, triangulación cualitativa) y
`revops` (definiciones, campos requeridos por etapa, higiene y auditoría). Ambas
vendoreadas en `.claude/skills/`. Lo aportado acá: la escalera de evidencia, el
denominador honesto, la base curada, el cruce etapa vs evidencia y el renderizado
en el tablero IC de AUREA sobre Prometheo, Tokko y canales.

## Skills relacionadas

- `aurea-dashboard-design` — cómo se ve el tablero. Esta skill decide **qué entra**.
- `aurea-metodologia` — diseño del CRM, tags y variables en Prometheo. Es aguas arriba:
  lo que esta skill audita, esa skill lo define.
- `attribution` / `revops` — las fuentes de origen, para consultar el detalle completo.
