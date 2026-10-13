# Mapa del ecosistema de skills de Inteligencia Comercial

Esta es la referencia transversal: qué skills intervienen en un tablero de IC, en qué paso
entra cada una, qué recibe, qué entrega y qué reglas suyas no se pueden romper. Se lee
**antes de arrancar un tablero nuevo** y cada vez que una skill cambia.

Versión del mapa: 13/10/2026. Cuando una skill del mapa sube de versión, se revisa su fila.

---

## 1. La cadena en una línea

```
Insumos → Metodología → Curaduría → Calificación → Criterio comercial
        → Canales + Costos → Lectura y acciones (score) → Diseño → Control
```

Cada flecha es un **entregable**: el paso siguiente no arranca sin el anterior.

| Paso | Skill | Recibe | Entrega |
|---|---|---|---|
| 0 | (este conductor) | Pedido del usuario | Lista de insumos completa, o lista de faltantes declarados |
| 1 | `aurea-metodologia` | Rubro, integración, CRM del cliente | Cómo está diseñado el CRM: embudos, tags, variables, qué se captura |
| 2 | `aurea-ic-curaduria-del-dato` | Export de Prometheo | Tabla variable → cobertura → origen → nivel de evidencia → pestaña; base curada |
| 3 | `aurea-hub-criterio-calificacion-leads` | Definición del cliente (B3) + base curada | Calificados en rango, hot leads, por qué no califican, malas prácticas detectadas |
| 4 | `aurea-ic-criterio-comercial` | Calificados y hot leads + variables de IC | Cola por impacto × disparador, objeción ↔ Disparador Compra, cobertura de los 5 campos |
| 5a | `aurea-ic-email-marketing`, `aurea-ic-whatsapp-marketing` | Exports de campañas (si hubo) | Métricas de canal con su base y su guardiana |
| 5b | `aurea-hub-costos-rentabilidad` | Panel de consumo, factura o conteo de Meta | Pestaña de consumo y costos, catálogo de acciones de costo |
| 6 | `aurea-ic-performance-report` + `aurea-data-action-driven` | Todo lo anterior, ya curado | Lectura "y entonces qué" por pestaña y cards de acción con score |
| 7 | `aurea-dashboard-design` | Contenido y cards | HTML del tablero |
| 8 | (este conductor) | Tablero armado | Checklist completo y registro de calibración |

Fuera de la cadena, pero conectadas: `aurea-ic-conocimiento` (cómo se cuenta y se vende IC;
se usa si el tablero va acompañado de una presentación) y `prometheo-correccion-prompts`
(cuando una card de acción termina en una corrección del prompt del agente).

---

## 2. Quién manda en cada tema (fuente única)

Si dos skills dicen cosas distintas sobre el mismo tema, manda la de esta tabla y la otra se
corrige. Nunca se resuelve "promediando".

| Tema | Fuente única | Las demás… |
|---|---|---|
| Qué número se puede mostrar y sobre qué base | `aurea-ic-curaduria-del-dato` | Aplican la escalera de evidencia |
| Qué es un lead calificado y un hot lead | `aurea-hub-criterio-calificacion-leads` (definición del cliente) | Nunca usan un criterio propio de AUREA. La copia dentro de la metodología, si difiere, pierde |
| Qué se extrae de cada consulta (problema, impacto, disparador) | `aurea-ic-criterio-comercial` | Reusan las variables de IC del CRM |
| Diseño del CRM, embudos, tags, variables | `aurea-metodologia` | Leen el CRM tal como está |
| Tarifas, consumo de IA, costo de Meta, rentabilidad | `aurea-hub-costos-rentabilidad` | No copian tarifas: apuntan a esa skill |
| Formato de la acción, score y guardiana | `aurea-data-action-driven` | Escriben sus recomendaciones como cards |
| Cómo se ve el tablero | `aurea-dashboard-design` | No definen colores ni componentes |
| Cómo se cuenta y se vende IC | `aurea-ic-conocimiento` | Mandan en lo técnico; esa manda en lo narrativo |
| Métricas de email y WhatsApp masivo | `aurea-ic-email-marketing`, `aurea-ic-whatsapp-marketing` | Usan sus definiciones de titular y guardiana |

---

## 3. Lo que no se negocia de cada skill (resumen operativo)

Resumen para tener todo a mano en un solo lugar. El detalle vive en cada skill: si hay
duda, se invoca la skill, no se trabaja de memoria con este resumen.

### `aurea-metodologia`
- Una etapa del embudo **es** una Smart Tag; una tag por dimensión; el estado del lead vive
  solo en el embudo, nunca en una variable.
- El embudo marca de quién es el trabajo: tramo del agente (recepción, calificación) y tramo
  humano (visita, cierre). Las etapas humanas no llevan prompt de IA y no se apagan: se miden.
- Variable padre e hija condicional: la hija se lee sobre su base, no sobre el total.
- La extracción vive en la plataforma; el prompt del agente solo refuerza las señales blandas.
- Familia de variables de IC: Objeción Principal + Frase Literal, Pedido Fuera de Catálogo +
  Detalle, Dolor Principal, Disparador Compra.
- Métricas core y línea base B10: velocidad, calificados, capacidad, satisfacción, ventas.

### `aurea-ic-curaduria-del-dato`
- Ningún número sin base, cobertura, origen y confianza.
- Escalera de evidencia: Hecho ≥ 80% · Señal 40 a 79% · Indicio 10 a 39% · No reportable < 10%.
- Doble lectura con cobertura menor a 80%. El faltante se dibuja, no se borra.
- Base curada: tipo de contacto excluyente; solo el comprador entra a calificación.
- Nunca sumar fuentes: Prometheo define cuántas consultas hubo.
- Con cortes de saldo, el costo por charla va sobre charlas procesadas.

### `aurea-hub-criterio-calificacion-leads`
- Paso 0: rubro + documento del discovery con la definición del cliente. Sin definición, el
  molde del rubro va rotulado "propuesta a validar" y no titula.
- Calificado = todos los obligatorios + al menos k de n sumas, con No Fit y motivo.
- Hot lead = una señal alcanza; es tag de prioridad, no etapa; "corto plazo" en días.
- Rango estricto y amplio cuando hay aproximaciones; cambio de criterio declarado.
- Sin benchmark de % de calificados: la meta sale de la línea base del cliente.
- Cada cambio (criterio, recalificación, ahorro) es card con score y guardiana.
- Caso EDFAN: 252 calificados (176 estricto) sobre 874 consultas de compra.

### `aurea-ic-criterio-comercial`
- Núcleo de cinco campos: problema, impacto, causa raíz, evento disparador, resultado de contacto.
- Evento Disparador (qué pasó para que consulte hoy) ≠ Disparador Compra (qué destrabaría la
  decisión). No se fusionan.
- Se lee dentro de los calificados y hot leads. Impacto y causa raíz son señales blandas: sin
  refuerzo en el prompt nacen en Indicio.
- "Avance" exige acción acordada con fecha.

### `aurea-ic-email-marketing` y `aurea-ic-whatsapp-marketing`
- Email: titula el empalme (clic que termina en conversación) y la calificación de lo que generó;
  la apertura nunca titula.
- WhatsApp: titula la respuesta, no la lectura; doble lectura sobre entregados y leídos; tier
  y calidad del número son métricas del tablero.
- Costo de una difusión: enviados × tarifa de su categoría (marketing ARS 89,56).

### `aurea-hub-costos-rentabilidad`
- Tres costos separados: suscripción (Enterprise USD 149 recomendado), saldo de IA (proyectar
  con USD 0,40 por conversación) y Meta (ARS 37,68 servicio y utilidad, ARS 89,56 marketing,
  1.000 respuestas gratis por mes por número).
- Ventana de 72 h de Click to WhatsApp: desde la respuesta, respondiendo en 24 h, contacto
  desde el celular.
- Consumo = saldo inicial − saldo final + recargas. Cortes de saldo = faltante de datos.
- Rentabilidad en rangos (67% a 77% de ahorro), nunca promesas.
- Tabla de derogados: no se usa ninguno.

### `aurea-ic-performance-report`
- Trabaja sobre números ya curados; no cita benchmarks genéricos ni metas sin fuente.
- Cada recomendación es una card; cada sección cierra con "y entonces qué".

### `aurea-data-action-driven`
- Toda card: sello (Corregir, Proteger, Separar, Medir, Decidir, Activar) + dueño (AUREA,
  Ventas, Marketing, Dirección) + título "Tema · dato" + score con su "por qué" + qué hacer,
  dónde, efecto, cómo se mide y guardiana.
- Bandas: 80 a 100 basada en datos · 55 a 79 informada · 30 a 54 hipótesis · 0 a 29 criterio.
- Una card, un verbo, un dueño. Rúbrica v1 sin calibrar hasta 20 cards cerradas.
- Regla propia de IC: techo del score según el nivel del dato central (Hecho 100, Señal 79,
  Indicio 54, No reportable 29; modelado 54). Ver `integracion-action-driven.md`.

### `aurea-dashboard-design`
- Branding fijo: violeta, azul, rosa; Arimo + Newsreader itálica; esfera una sola vez.
- Básico y Avanzado son dos profundidades, no dos vocabularios; el switch actúa en todo.
- KPI con delta obligatorio; embudo como pasos; color semántico aparte de la marca.
- Cards de acción con paleta semántica propia; tres en Básico.
- Modo oscuro, estados vacíos, fecha de actualización por fuente.

### `aurea-ic-conocimiento` (si hay presentación)
- Tono afirmativo, sin ganchos negativos ni jerga interna; misterio controlado (FOMO).
- Cada número con estado; costos desde `aurea-hub-costos-rentabilidad`; sin promesas de rendimiento.

---

## 4. Cómo se mantiene este mapa

1. Cuando una skill del ecosistema cambia de versión, se revisa su fila en las secciones 1 a 3.
2. Si aparece una skill nueva, se suma a la cadena (sección 1), a la tabla de fuente única
   (sección 2) y a la cadena del `SKILL.md` del conductor.
3. Si dos skills se contradicen, se resuelve con la sección 2 y se corrige la que pierde.
4. Cada cambio se anota en `references/CHANGELOG.md` de este conductor.
