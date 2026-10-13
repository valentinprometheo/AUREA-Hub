---
consultar-cuando: entregar una corrección de prompt, armar la versión nueva, pasar el bloque corregido
disparadores: "pasame la sección corregida", "mandame el bloque", "cómo lo entrego", "sector completo"
fuente-única-de: formato de entrega de una corrección de prompt
combina-con: 02-barrido-de-coherencia, 03-matriz-auditoria
---

# 01 · Entrega por sector completo

> Cómo se entrega una corrección para que se pueda aplicar de una sola pegada, sin edición
> quirúrgica dentro del editor de Prometheo.

---

## La regla

**Toda corrección se entrega como uno o más sectores completos del prompt, reescritos de punta
a punta, listos para reemplazar.**

El destinatario tiene que poder: abrir el prompt, seleccionar el sector viejo entero, borrar,
pegar el nuevo. Nada más. Si para aplicar la corrección hay que buscar una línea, ubicar un
párrafo, insertar en el medio o comparar dos textos parecidos, la entrega está mal hecha.

### Lo que está prohibido entregar

- Diffs, "antes / después" de una línea suelta.
- Instrucciones de edición: "cambiá X por Y", "agregá esto después del párrafo que empieza
  con…", "borrá la última oración de la sección 4".
- Fragmentos sin límite declarado: un párrafo suelto sin decir dónde arranca y dónde termina el
  sector al que pertenece.
- El prompt entero cuando cambió un sector. Entregar todo obliga a releer todo y esconde qué se
  tocó. **Sector completo no es prompt completo.**

### Por qué

Reemplazar cosas chicas dentro de un prompt largo es lento y propenso a error. Un sector
completo es una operación atómica: o se pegó o no se pegó, no hay estados intermedios. Además
deja el sector en un estado conocido, que es exactamente lo que el barrido de coherencia
necesita para poder verificarse.

---

## Qué es un "sector"

Un sector es una **sección numerada del prompt tal como existe en la versión vigente**: **de
encabezado numerado a encabezado numerado**, es decir desde su encabezado o separador `===`
hasta el carácter anterior al encabezado del sector siguiente. Los apéndices y anexos cuentan
como sectores propios.

Reglas de límite:

- El sector se define por el **texto vigente**, no por el índice teórico del prompt tipo. Si el
  prompt del cliente numera distinto, manda el prompt del cliente.
- El bloque entregado **incluye** el encabezado y el separador del sector. Si el sector vigente
  arranca con `=== SECCIÓN 6 · …`, el bloque entregado arranca igual, verbatim.
- Nunca se renumeran sectores en una corrección. Renumerar es cambio estructural: versión nueva
  y changelog.

---

## Sectores contiguos: se fusionan

Si las correcciones de la ronda tocan sectores **consecutivos**, se entregan como **un solo
bloque continuo**, no como bloques separados.

- Tocan 13 y 14 → un bloque `SECCIONES 13 y 14`.
- Tocan 8 y 9 → un bloque `SECCIONES 8 y 9`.
- Tocan 8, 9 y 10 → un bloque `SECCIONES 8 a 10`.
- Tocan 4 y 9 → **dos** bloques separados, uno por sector.
- Tocan 4, 5 y 9 → **dos** bloques: `SECCIONES 4 y 5` y `SECCIÓN 9`.

Cómo se opera:

1. Listá los sectores tocados por la ronda entera (viene del paso 4 del flujo).
2. Ordenalos y agrupalos en **corridas contiguas**.
3. Cada corrida es un bloque de entrega. Los sectores intermedios de una corrida se reproducen
   **completos, aunque no hayan cambiado**: forman parte del bloque continuo.
4. **La detección es automática.** No se pregunta "¿los querés juntos?": se detecta y se
   fusiona.

**Cuidado con el paso 3:** dentro de un bloque fusionado, los sectores que no cambian se copian
verbatim del vigente. No se reescriben "mejorados", no se reordenan, no se les corrige la
redacción de paso. Un cambio de conveniencia adentro de un bloque fusionado es una regresión
silenciosa: entra sin haber sido pedido y sin quedar registrado.

---

## Cabecera obligatoria de cada bloque

Cada bloque entregado va precedido por una cabecera fuera del prompt, para que quede claro qué
se reemplaza:

```
REEMPLAZO · [CLIENTE] · v[N] ← v[N-1]
Bloque: SECCIONES 13 y 14 (contiguas, bloque único)
Reemplaza: desde "=== SECCIÓN 13 · …" hasta el carácter anterior a "=== SECCIÓN 15 · …"
Cambia: reglas 61 y 62 (nuevas), regla 47 (ámbito acotado)
Se eliminó: bloque de índice del Apéndice A (huérfano, chequeo 4)
No se tocó: el resto de la sección 14, reproducida verbatim
Barrido de coherencia: OK (7/7) · ver matriz filas 88-91
```

Los seis campos son obligatorios (`Se eliminó` va con "nada" si no hubo borrado). El último es
el que hace de gate: si dice otra cosa que OK (7/7), el bloque no se entrega.

---

## La única excepción: sectores con placeholders

### Qué es un placeholder

Una referencia interna a un archivo que Prometheo adjunta y envía al lead: brochure, render,
plano, foto, video, carta de colores. El lead nunca ve el texto del placeholder, ve el archivo.
Ejemplos de forma: `/Brochure-SLUG`, `/Render-SLUG`, `[VIDEO_X]`, y las tablas de apéndice que
mapean producto o proyecto contra archivo.

**Regla de exactitud:** el nombre del placeholder es el nombre EXACTO del archivo cargado,
verbatim, con sus espacios, tildes, mayúsculas y extensión. Un carácter distinto rompe el
adjunto, y rompe **en silencio**: el agente responde igual, sin el archivo.

### Cuándo se activa la excepción

Cuando el sector a reemplazar **contiene un inventario o mapeo de placeholders** (una lista, una
tabla, un apéndice de assets) y la corrección **no lo modifica**.

Ahí, y solo ahí, la entrega puede ser parcial. El riesgo de reescribir treinta nombres de
archivo para cambiar dos oraciones es mayor que el beneficio de la pegada única.

### Cómo se entrega en ese caso

- Se entregan **solo los sub-bloques que cambian**, cada uno con su **ancla verbatim**: la línea
  inmediatamente anterior tal como está en el vigente, para que no haya duda de dónde va.
- Se declara explícitamente qué NO se toca: `El inventario de placeholders de la sección 11 no
  se toca. Dejarlo tal cual está.`
- La cabecera del bloque agrega un campo: `Excepción de placeholders: SÍ · motivo: la sección 11
  contiene el mapeo de 32 assets y la corrección no lo modifica.`
- **La entrega parcial también pasa por el barrido.** La excepción es al formato de entrega, no
  al gate de verificación.

### Si la corrección SÍ toca el inventario

Entonces el cambio se entrega **placeholder por placeholder**, línea vieja verbatim contra línea
nueva verbatim. Nunca se reemite el inventario entero.

```
En la sección 11, reemplazar exactamente esta línea:
  /Brochure-Torre-Sur  →  Torre Sur - Brochure 2025.pdf
por esta:
  /Brochure-Torre-Sur  →  Torre Sur - Brochure 2026 v2.pdf
El resto del inventario no se toca.
```

### Lo que nunca se hace con un placeholder

- Regenerarlo de memoria o "deducir" el nombre.
- Normalizarlo: sacarle tildes, cambiar mayúsculas, unificar espacios por guiones, agregar o
  sacar extensión.
- Reordenar el inventario "para que quede prolijo".
- Eliminarlo como estructura huérfana sin verificar antes contra el inventario real. Un
  placeholder vivo borrado rompe el adjunto en silencio.
- Inventar un placeholder para un archivo que todavía no está cargado. Si falta, se deja el
  hueco con su estado (pendiente de subir, a comprimir) y se suma a la lista de lo que hay que
  pedirle al cliente.

---

## Qué NO habilita una entrega parcial

Ninguna de estas razones alcanza. La excepción de placeholders es la única.

- "Es un cambio chico, una sola frase."
- "El sector es muy largo."
- "Ya te lo pasé la vez pasada, solo cambió esto."
- "Para ahorrar tokens."
- "Es obvio dónde va."

Si el sector es tan largo que reescribirlo completo se vuelve inmanejable, el problema no es la
regla de entrega: el sector está mal cortado, y eso se resuelve con una versión nueva que lo
parta, con changelog, no con una entrega parcial.

---

## Checklist de la entrega

- [ ] Tengo a la vista el texto literal de la versión vigente.
- [ ] Cada regla de la ronda está mapeada a su sector.
- [ ] Los sectores tocados están agrupados en corridas contiguas.
- [ ] Cada corrida se entrega como un bloque continuo, con los sectores intermedios verbatim.
- [ ] Cada bloque arranca con el encabezado y separador reales del sector vigente.
- [ ] Cada bloque tiene su cabecera con los seis campos obligatorios.
- [ ] Si hubo entrega parcial, está declarada la excepción de placeholders y su motivo.
- [ ] Ningún placeholder fue reescrito, normalizado, reordenado ni borrado sin verificar.
- [ ] Las estructuras huérfanas detectadas se eliminaron dentro del mismo bloque entregado.
- [ ] No entró ningún cambio de conveniencia no pedido.
- [ ] El campo "Barrido de coherencia" dice OK (7/7).
