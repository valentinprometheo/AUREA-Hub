# Mejora continua · cómo esta skill aprende mientras funciona

Esta es la capa que hace que la skill **no se quede quieta**: cada documento que generamos deja un aprendizaje, y cada documento nuevo arranca revisando lo aprendido. Así la estética y la metodología se afinan solas con el uso, en vez de repetir los mismos errores.

## El problema que resuelve

Claude no recuerda entre sesiones. Pero **un archivo versionado en el repo sí persiste.** Entonces la memoria de la skill no vive en la cabeza del modelo: vive en `references/aprendizajes.md` (el log) y en las referencias canónicas (la doctrina estable). Este módulo es el protocolo para leerlas, escribirlas y ascender lo aprendido.

## El ciclo (cerrá el loop en cada entrega)

```
   ┌─────────────────────────────────────────────────────────┐
   │  1. LEER    → antes de generar, revisar aprendizajes.md  │
   │  2. APLICAR → usar lo aprendido en este documento        │
   │  3. OFRECER → proponer mejoras concretas al usuario      │
   │  4. CAPTURAR→ al cerrar, anotar el aprendizaje nuevo      │
   │  5. ASCENDER→ lo que se repite, subirlo a la doctrina     │
   └─────────────────────────────────────────────────────────┘
```

### 1 · LEER (Paso 1 del flujo del conductor)

Antes de generar cualquier documento, leé `references/aprendizajes.md`. Filtrá por lo que aplica: mismo **género** (presupuesto, propuesta, NDA...), mismo **cliente**, o misma **clase de problema** (una alineación, un número, una cláusula). Si hay algo, tenelo presente desde el arranque.

### 2 · APLICAR

Aplicá el aprendizaje sin que el usuario tenga que pedirlo. Ejemplo: si `aprendizajes.md` dice "en cards de precio hermanas, el label gemelo evita el escalonado", ya lo armás así de entrada. El aprendizaje aplicado en silencio es la mitad del valor.

### 3 · OFRECER (proactivo, sin imponer)

Cuando un aprendizaje sugiere una mejora que **cambia una decisión del usuario**, no la apliques sola: ofrecela en una línea, con el porqué y el costo. Formato:

> "Sobre el presupuesto: la última vez descubrimos que separar honorarios de plan de plataforma en dos cards leía más claro que una tabla junta. ¿Lo armo así o preferís la tabla?"

Reglas del ofrecimiento:
- **Máximo dos mejoras por documento**, las de mayor impacto. No abrumes.
- Cada una: qué mejora, por qué (el aprendizaje que la respalda), y qué implica elegirla.
- Si el usuario dice que no, respetalo y **anotá la preferencia** en el log (así no se vuelve a ofrecer lo mismo).

### 4 · CAPTURAR (Paso 7 del flujo del conductor)

Al cerrar la entrega, anotá el aprendizaje en `references/aprendizajes.md` **cuando pase alguna de estas cosas**:
- El usuario **corrigió** algo (lo más valioso: una corrección es un aprendizaje puro).
- Descubrimos una **receta** que funcionó mejor que la anterior.
- Detectamos una **preferencia** del usuario (un número, un tono, un orden que prefiere).
- Un dato de negocio se **confirmó o cambió** (un monto, un plan, un servicio nuevo).
- Algo **salió mal** y hay que no repetirlo.

Si la entrega fue de rutina y no pasó nada de eso, **no inventes un aprendizaje**. El log vale por su señal, no por su volumen.

### 5 · ASCENDER (mantener la doctrina viva)

El log es memoria de trabajo; las referencias canónicas son la doctrina. Cuando un aprendizaje **se repite dos o tres veces** o queda claramente confirmado, ascendelo: movelo del log a la referencia que corresponde (`estetica-deck.md`, `documentacion-formal.md`, `nuevos-servicios.md`, el género...) como regla estable, y en el log dejá la línea marcada como `[ascendido → <archivo>]`. Así la doctrina crece y el log no se infla con cosas ya resueltas.

**Cuándo asciende algo:** proponéselo al usuario cuando lo detectes ("esto ya lo corregimos tres veces, ¿lo dejo fijo en la estética?"). No reescribas la doctrina sin su OK; las referencias canónicas son la fuente de verdad y se tocan con criterio.

## Formato de una entrada en `aprendizajes.md`

Cada entrada es una fila corta y accionable. No un diario: una regla que la próxima vez se pueda aplicar.

```
### [AAAA-MM-DD] · <género o área> · <cliente si aplica>
- **Qué pasó:** (una línea: la corrección, el descubrimiento, la preferencia)
- **Aprendizaje:** (la regla accionable para la próxima vez)
- **Aplica a:** (género / familia / cliente / transversal)
- **Estado:** activo | ascendido → <archivo> | descartado por el usuario
```

## Reglas de la mejora continua

- **Aditivo, no regresivo.** Un aprendizaje nuevo no borra ni debilita la doctrina existente sin que el usuario lo apruebe. Si contradice una regla canónica, se ofrece el cambio, no se impone.
- **La corrección del usuario es la señal más fuerte.** Priorizá capturar correcciones sobre cualquier otra cosa.
- **El usuario manda.** La skill ofrece mejoras; decide el usuario. Una preferencia declarada se respeta y se registra.
- **Señal sobre volumen.** Mejor cinco aprendizajes que se usan que cincuenta que nadie mira.
- **Trazable.** Cada aprendizaje dice de dónde salió (fecha, cliente, género), para poder revisarlo.
- **Versionado.** El log vive en el repo y viaja con la skill; commitealo junto con el documento cuando cierres una entrega relevante.
