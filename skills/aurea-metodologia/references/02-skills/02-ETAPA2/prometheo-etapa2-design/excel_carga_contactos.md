# MÓDULO: EXCEL / SHEETS DE CARGA DE CONTACTOS

Output 4 de Etapa 2. Es la planilla donde el cliente vuelca su base histórica de
leads para que el agente la tenga desde el día 1. Su estructura refleja las 3
capas (embudos, tags, variables) definidas en la SECCIÓN 0 del SKILL.md.

Caso de referencia: **G&D Developers — "Base de Leads", agente Veronica.**

---

## CUÁNDO SE GENERA

- Cuando el cliente tiene una **base histórica de leads** que quiere cargar al
  CRM desde el arranque.
- Si el cliente NO tiene base previa (arranca de cero), este output no es
  necesario — pero igual conviene entregar la plantilla vacía para que cargue
  leads nuevos de forma ordenada.

---

## ESTRUCTURA DEL ARCHIVO — DOS HOJAS

### Hoja 1 — INSTRUCCIONES (enseña al cliente a usar la planilla)
Contiene, en lenguaje del cliente (sin jerga de CRM):
1. **Para qué sirve el Excel** (1 párrafo).
2. **Cómo está organizado el CRM** — explicación de que el lead se mueve por N
   embudos y que cada lead muestra una tag por dimensión: estadío + tipo de usuario + prioridad opcional (VIP).
3. **Los embudos y sus etapas**, con responsable de cada uno.
4. **Las Smart Tags** de tipología + prioridad, qué significa cada una.
5. **Las variables**, cada una con "qué guarda" en lenguaje claro.
6. **Cómo completar la hoja LEADS** (pasos numerados).
7. **La regla de oro:** "No inventar datos. Mejor celda vacía que dato falso."

### Hoja 2 — LEADS (donde el cliente carga)
Una fila por lead. Columnas en este orden:
1. **Datos de contacto:** Nombre, Apellido, Teléfono, Email (mínimo Nombre + Teléfono)
2. **Estadío** — la etapa del embudo donde está hoy el lead
3. **Tipología** — `#inversor` / `#uso_propio` / `#inmobiliaria` (o las del rubro)
4. **VIP** — sí / no
5. **Columnas `var_`** — una por cada variable

---

## DECISIONES DE DISEÑO QUE FUNCIONARON

- **Fila de ejemplo en la hoja LEADS**, en gris itálico, que el cliente borra
  después. Muestra cómo se ve un lead bien cargado. Va en la fila 2; el cliente
  empieza a cargar en la fila 3.
- **Dropdowns (validación de datos)** en las columnas de valores cerrados:
  estadío (TODAS las etapas de todos los embudos), tipología, VIP, variables
  router. Evita que el cliente cargue valores fuera de norma.
- **Encabezados congelados** (freeze panes) para que no se pierdan al scrollear.
- **Barra de título** en la fila 1 con instrucción de una línea que remite a la
  hoja INSTRUCCIONES.
- **Regla de oro de carga** explícita en INSTRUCCIONES: "No inventar datos.
  Mejor celda vacía que dato falso."
- **Separar lo conectable de lo interno:** datos de uso interno del equipo
  (responsables, notas internas) pueden ir en columnas marcadas o en hoja aparte
  "NO conectar", para no exponerlos al agente si la hoja se conecta a Prometheo.

---

## EL CONFLICTO EXCEL-DE-CARGA vs SHEETS-DE-LECTURA (hallazgo crítico)

Hay **dos archivos distintos** que no hay que confundir:

### 1. Excel/Sheets de TRABAJO (para el cliente)
Con dropdowns, colores, formato condicional, fila de ejemplo. El cliente lo usa
para cargar y mantener cómodo. Es el que tiene las 2 hojas descritas arriba.

### 2. Sheets de LECTURA (para Prometheo) — PLANO
Solo datos crudos. **Sin dropdowns, sin formato condicional, sin filtros, sin
fórmulas.**

**Por qué:** cuando Prometheo lee un Sheets de forma programática, lee los
**valores**, no el formato. Los dropdowns y colores no le aportan y pueden
generar ruido. Prometheo necesita: fila 1 con encabezados limpios, una columna
por dato, cada dato en su formato correcto (número como número, texto como
texto, sí/no como texto plano), cero fórmulas/filtros/validaciones.

**Recomendación validada:** un solo Sheets plano para Prometheo. La disciplina
de carga se sostiene con la hoja INSTRUCCIONES (que lista los valores válidos),
no con dropdowns. Tener dos fuentes de verdad que se sincronizan con fórmulas
choca con el requisito de "sin fórmulas" y crea riesgo de desincronización.

---

## REGLAS TÉCNICAS DE GENERACIÓN (openpyxl)

- **Precios/montos: solo número, sin símbolo ni separador.** Cargar `75500`, no
  "USD $75.500". El símbolo de moneda va implícito en el nombre de la columna.
  Si Prometheo lee texto donde espera número, falla el filtrado.
- **Decimales con punto, no con coma.** `m²` como `59.9`, no `'59,9'` (string).
  Detectar y convertir texto-con-coma a número real.
- **Celdas no-aplica: vacías, no en 0.** Si una financiación es "contado", las
  columnas de cuotas/TNA van **vacías**, no en 0. El 0 se lee como dato válido
  y confunde.
- **Nombres de proyecto/categoría EXACTOS y consistentes entre hojas.** "MOCA 2"
  siempre igual, nunca "MOCA II" ni "Moca 2". El match es literal.
- **Dropdowns visibles:** usar `showDropDown=False` en openpyxl (el parámetro
  está invertido — False muestra el dropdown).
- **Validar el archivo final** con `/mnt/skills/public/xlsx/scripts/recalc.py`
  antes de entregar. Debe dar 0 errores.
- **Separar lo conectable de lo interno en hojas distintas** cuando haya datos
  internos sensibles.

---

## PROMPT OPERATIVO (para arrancar el Excel de una cuenta nueva)

Reemplazar `[corchetes]` con datos del cliente:

> Vamos a diseñar el **Excel de carga de contactos** del cliente **[NOMBRE]**,
> rubro **[RUBRO]**, agente **[NOMBRE AGENTE]**.
>
> Antes de generar nada, respetá la arquitectura de 3 capas y confirmá cada una:
>
> **1. Embudos.** Proponé los embudos del cliente. Cada uno con responsable claro
> (agente IA o humano) y etapas excluyentes que se reemplazan al avanzar. FAQ y
> Excepciones NO son embudos. Un embudo separado se justifica solo si cambia el
> actor o la naturaleza del proceso. Si la gestión es manual y por fuera del
> sistema, ese embudo arranca minimalista.
>
> **2. Smart Tags.** Todo lead muestra 2 tags de un vistazo: ESTADÍO (etapa del
> embudo) + TIPOLOGÍA (categoría más fuerte en este rubro). Sumá PRIORIDAD
> combinable solo si el cliente la necesita. Las etapas SON tags. No diseñes tags
> con nombres casi idénticos. Una tag se crea solo si se ve de un vistazo o
> dispara una acción.
>
> **3. Variables.** Detalle puntual que se filtra, prefijo `var_`. El estadío NO
> va en variable. Identificá variables router (gobiernan preguntas posteriores) y
> de handoff (se llenan al derivar).
>
> Con las 3 capas confirmadas, generá el Excel con DOS hojas:
> - **INSTRUCCIONES:** para qué sirve, cómo está organizado el CRM, los embudos
>   con responsable, las tags, las variables con "qué guarda", cómo completar
>   (pasos numerados), regla de oro.
> - **LEADS:** datos de contacto (mín. Nombre + Teléfono), Estadío, Tipología,
>   VIP, una columna por `var_`. Fila de ejemplo en gris itálico (fila 2),
>   dropdowns en columnas de valor cerrado (con TODAS las etapas), encabezados
>   congelados.
>
> Reglas técnicas: montos como número plano; decimales con punto; celdas
> no-aplica vacías (no 0); nombres consistentes entre hojas; validá con recalc.py
> (0 errores). Si generás Sheets de lectura para Prometheo, que sea plano: sin
> dropdowns, formato condicional, filtros ni fórmulas.
>
> Si una decisión es controvertida (lógica de tag, variable condicional,
> comportamiento de follow-up), pará y pedí validar con el bot oficial de
> Prometheo antes de seguir. No avances de capa sin confirmación. Una salida a
> la vez.

---

## CHECKLIST FINAL DEL EXCEL

- [ ] 2 hojas: INSTRUCCIONES + LEADS
- [ ] INSTRUCCIONES explica embudos, tags, variables en lenguaje del cliente
- [ ] LEADS tiene datos de contacto + Estadío + Tipología + VIP + columnas var_
- [ ] Fila de ejemplo en gris itálico (fila 2)
- [ ] Dropdowns en columnas de valor cerrado (todas las etapas en Estadío)
- [ ] Encabezados congelados
- [ ] Montos como número plano, decimales con punto
- [ ] Celdas no-aplica vacías (no 0)
- [ ] Nombres consistentes entre hojas
- [ ] Regla de oro "no inventar datos" en INSTRUCCIONES
- [ ] Validado con recalc.py (0 errores)
- [ ] Si va a Prometheo: versión Sheets de lectura plana (sin formato)
