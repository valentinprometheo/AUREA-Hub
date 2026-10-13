# 07 · Mejora continua de esta skill

Esta skill está viva: IC cambia cada semana (precios, pestañas, casos, correcciones de presentaciones). La arquitectura evita dos riesgos: que el conocimiento quede viejo y que se contradiga con las skills operativas.

## Las tres capas
1. **Bandeja de entrada · `hallazgos.md`.** Todo lo nuevo entra acá primero, con fecha, fuente y estado. Nada se integra directo a las referencias sin pasar por la bandeja, salvo una orden explícita de Valen.
2. **Conocimiento consolidado · `references/`.** Solo lo confirmado. Cada dato sensible lleva estado: [VIGENTE], [A VALIDAR], [REFERENCIA], [ILUSTRATIVO], [DEROGADO].
3. **Historial · `CHANGELOG.md`.** Qué cambió, cuándo y por qué. Lo derogado se registra acá antes de sacarlo de las referencias.

## Disparadores de actualización
- Valen corrige una presentación de IC (tono, estética, contenido): la regla de fondo se registra, no solo el cambio puntual.
- Cambia un precio, un canal, una comisión o una decisión de producto.
- Aparece un caso nuevo, un número real o una prueba de product-market fit.
- Llega una nota, un estudio o una tendencia de mercado.
- Una skill operativa del grupo cambia algo que afecta la narrativa.
- Valen dice "actualizá el conocimiento de IC", "integrá esto", "derogá tal cosa" o "sacá una versión nueva".

## Protocolo paso a paso
1. **Registrar.** Agregar en `hallazgos.md`: fecha, fuente (conversación, documento, reunión), qué dice, dónde impacta, estado.
2. **Clasificar.** ¿Es tesis, modelo de negocio, producto, narrativa, estética, caso o mercado? Eso define la referencia destino.
3. **Confirmar.** Si es una regla nueva o contradice algo vigente, confirmarlo con Valen antes de integrar. Si fue una corrección explícita suya, ya está confirmado.
4. **Integrar.** Editar la referencia destino. Si reemplaza algo, marcar lo viejo como [DEROGADO] con fecha o moverlo al CHANGELOG.
5. **Versionar.** Actualizar `CHANGELOG.md`:
   - **Mayor (2.0.0):** cambia la tesis, el modelo de negocio o el posicionamiento.
   - **Menor (1.1.0):** se suma contenido (caso, sección, objeción, pestaña).
   - **Parche (1.0.1):** corrección de un dato, frase o regla puntual.
6. **Barrido de coherencia.** Revisar:
   - que el precio sea el mismo en `02`, `03` (objeciones) y `04` (catálogo);
   - que las frases aprobadas no choquen con las prohibidas;
   - que lo técnico no contradiga a `aurea-ic-dashboard`, `aurea-ic-criterio-comercial` o `aurea-ic-curaduria-del-dato`;
   - que `SKILL.md` (tesis y mapa) siga siendo cierto.
7. **Empaquetar.** Regenerar el `.skill` y reemplazar el anterior (no duplicar versiones instaladas).
8. **Vaciar la bandeja.** Pasar lo integrado de `hallazgos.md` a la sección "Integrado" con la versión en que entró.

## Reglas de higiene
- Nunca convertir un supuesto en dato: si no hay fuente, queda [A VALIDAR] o [SUPUESTO].
- No duplicar contenido que ya vive en una skill operativa: referenciarla.
- `SKILL.md` se mantiene corto (tesis, mapa, reglas, ruteo); el detalle va a `references/`.
- Si una referencia supera ~300 líneas, partirla y agregar índice.
