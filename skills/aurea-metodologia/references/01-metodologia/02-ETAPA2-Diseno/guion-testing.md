---
consultar-cuando: armar o correr el guión de testing de un agente, validar correcciones antes o después del Go-Live
disparadores: "guión de testing", "testear el agente", "regresión", "primos", "escenarios de prueba"
fuente-única-de: doctrina de diseño del guión de testing (formato, primos, marca de plataforma)
combina-con: 10-patrones-correccion-agente, metodologia-correccion-agente, 08-reglas-integracion-catalogo
---

# Guión de testing del agente IA

> Cómo se arma y se corre el guión que valida un agente, antes de un Go-Live y después de cada
> ronda de corrección. Doctrina destilada de los guiones reales de Martina (EDFAN) y Catalina
> (BETROX). Es un documento maestro reutilizable: el formato no depende del rubro.

---

## Para qué sirve

El guión traduce cada bug reportado y cada regla nueva en una secuencia de turnos concreta que
un tester pega al agente para verificar si el comportamiento quedó bien. Es la contracara del
barrido de coherencia: el barrido audita el texto del prompt; el guión audita la conducta real.

---

## El principio de los "primos" (lo más importante del formato)

Cada bloque del guión no testea un caso: testea **una regla general**, con el caso reportado más
sus **primos** (variantes del mismo problema que no se vieron en el reporte original).

- Si la regla está bien escrita, el caso reportado **y sus primos** pasan.
- Si pasa solo el caso original pero falla un primo, **la regla quedó como parche**: se escribió
  para el ejemplo puntual, no para el patrón. Hay que reescribirla con ámbito general.

Esto es lo que separa una corrección real de un parche. Ejemplo (EDFAN): el caso reportado era
"presenta San Telmo dentro de 'Palermo o cercanías'". El primo es "presenta cualquier zona como
cercana a otra sin que el cliente lo haya definido". Si el agente arregla San Telmo pero sigue
infiriendo otras equivalencias geográficas por su cuenta, la regla era un parche.

**Regla de armado:** por cada corrección, escribí el caso reportado y al menos un primo. Si no
se te ocurre un primo, probablemente no entendiste el patrón todavía.

---

## Formato de cada test

- **Título** corto + categoría en itálica + cantidad de turnos.
- **Secuencia mínima de turnos** para llegar al punto donde se evidencia el comportamiento. El
  primer turno da el contexto real necesario para que la pregunta siguiente tenga sentido:
  nunca se arranca con un "Hola" pelado si el test necesita contexto.
- Cada turno en **bloque de código separado**, listo para copiar y pegar, sin comillas.
- **✅ Lo esperado** (qué tiene que hacer el agente).
- **❌ Lo que hacía mal** (el comportamiento viejo, para que el tester lo reconozca si reaparece).
- Máximo 3 turnos por test. Si el comportamiento se observa en el hilo de otro test, se marca
  "sigue el hilo del test X" en vez de repetir la secuencia.

Encabezado del guión: título, blockquote con alcance + versión del prompt en testeo + fecha, y
una línea sobre el método (copiar cada turno, cotejar la respuesta final contra lo esperado).
Los tests se agrupan por ronda de feedback (Bloque A, B, C…) o por regla general.

---

## La marca [PLATAFORMA]

Los tests cuyo resultado depende de la integración (no del prompt) se marcan `[PLATAFORMA]`. Si
uno de esos falla, la primera acción es **verificar que el dato esté cargado y la integración
responda**, no tocar el prompt. Distingue un bug de prompt de un bug de datos o de plataforma, y
evita "corregir" el prompt por un problema que no era suyo.

Ejemplos de test [PLATAFORMA]: el agente da el piso de una unidad (está en Tokko), ofrece el más
barato real (depende del orden que devuelve la integración), lee todas las características de la
unidad. Si fallan, se revisa la carga antes que la redacción.

---

## Regresión: lo que una corrección no puede romper

Todo guión incluye un bloque de **regresión**: los comportamientos que ya funcionaban y que la
ronda nueva no puede haber roto. Es la contraparte viva de la regla "aditiva, aislada y no
regresiva": no alcanza con que el bug nuevo esté corregido, hay que confirmar que lo que andaba
sigue andando. En clientes con reglas comerciales sensibles (BETROX funcionando bien), este
bloque es obligatorio antes de dar por buena una versión.

---

## Dos patrones de contenido reutilizables

- **Reconocer una entidad por un atributo distinto del nombre.** El lead nombra una unidad por
  su precio ("¿y el de 251.100?") o por una característica, no por su ID. El agente tiene que
  reconocerla igual. Se testea explícitamente.
- **Tabla de sinónimos del lead.** El guión incluye cómo el lead puede nombrar cada cosa
  ("mono" → monoambiente, "depto" → 2 ambientes; "amplio/patio/terraza" para exteriores) para
  testear que el agente traduzca. El vocabulario es del rubro; el patrón "tabla de sinónimos"
  es transversal.

---

## Guión client-facing vs guión interno

Hay dos usos y no se mezclan:
- **Interno (tester de AUREA):** puede mencionar la mecánica, marca [PLATAFORMA], nombra las
  reglas por su número.
- **Client-facing (lo ve el cliente):** cero jerga de CRM. Nada de Smart Tags, variables ni
  taxonomía. Estructura por caso: *pregunta del cliente → cómo responde el agente → qué
  mejoramos*, agrupado por áreas de mejora. El cliente lee comportamiento, no configuración.

---

## Decisión abierta — datos reales vs guión atemporal

Un guión con datos reales embebidos (precios, unidades) es más concreto pero envejece: hay que
reescribirlo cuando cambia el stock. Uno atemporal (con placeholders) se reusa mes a mes pero es
menos literal. Es un trade-off de todo material de testing, a definir por cliente. Queda como
decisión abierta, no como regla cerrada.

---

## Relación con la metodología

| Conecta con | Cómo |
|---|---|
| `10-patrones-correccion-agente.md` | cada patrón auditado se valida con un test (caso + primos) |
| `metodologia-correccion-agente.md` | el guión es el paso de verificación del ciclo de corrección |
| `08-reglas-integracion-catalogo.md` | los tests [PLATAFORMA] dependen de la fuente, no del prompt |
| `00-OUTPUTS-POR-ETAPA.md` | el guión client-facing es la familia 3 de outputs |
