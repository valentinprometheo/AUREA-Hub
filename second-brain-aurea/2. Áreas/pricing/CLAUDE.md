# Pricing · cómo cotiza AUREA

Área permanente. Separa dos cosas que no se mezclan:
- **Costos de plataforma** (lo que el cliente le paga a Prometheo y a Meta): fuente única en la skill
  `ic-costos-y-rentabilidad-de-prometheo`. Enterprise USD 149 recomendado (no es piso), IA proyectada
  con USD 0,40 por conversación, Meta en pesos y aparte.
- **Precio de AUREA** (lo que cobra AUREA): este archivo.

## Vigente hoy
Los presupuestos de **EAF** (07/10) y **DRAKON** (01/09 y 17/09): fee de implementación, licencia,
IC por canal y Mejora Continua. Es lo que se usa con clientes hasta que el modelo nuevo esté cerrado
(costos de plataforma siempre desde `ic-costos-y-rentabilidad-de-prometheo`).

## En construcción (desde 23/10/2026): paquetes con el Estimador de presupuesto
Valen: "es muy nuevo, se está creando". No se usa con clientes todavía. Herramienta: **Estimador de presupuesto · AUREA Hub** (artifact
https://claude.ai/artifact/CZbWPxJoPKr3uUR9beq268, uso interno). Pieza para el cliente: **AUREA Hub ·
Growth V2** (sin precios). En la skill `aurea-ic-conocimiento` v1.3.0 (`02`) figura como [A VALIDAR].

| Valores por defecto (250 conv./mes) | Esencial | Crecimiento | Escala |
|---|---|---|---|
| Horas · setup (USD 50/h) | ~49 h · USD 2.450 | ~92 h · USD 4.600 | ~140 h · USD 7.000 |
| IC | no | USD 400/mes desde el mes 4 | USD 900/mes desde el mes 4 |
| Mejora Continua | Estabilización 12 h, después Start 6 h | Estabilización 16 h, después Start | Estabilización 24 h, después Pro 10 h |
| Meses 1 a 3 / desde el mes 12 | ~USD 1.000 / ~580 | ~USD 1.710 / ~980 | ~USD 2.510 / ~1.680 |
| Año 1 cliente · le queda a AUREA | ~USD 9.400 · 2.200 (35%) | ~USD 15.800 · 4.200 (33%) | ~USD 25.800 · 7.500 (33%) |
| Facturación mínima para no pasar el 4% | ~USD 14.500/mes | ~USD 24.500/mes | ~USD 42.000/mes |

La hora: el estimador usa **USD 50** y el documento del CTO, USD 45 (a cerrar).

### Lo que conviene mirar del estimador
- Con los valores por defecto, el margen de AUREA sobre fees queda en 33% a 35%, apenas arriba de la
  alerta del 30%: cualquier desvío de horas lo come. Por eso el setup "nunca se bonifica".
- Escala con una facturación de USD 25.000/mes da 6,7%: la alerta del 4% lo marca en rojo. Escala es
  para clientes de USD 42.000/mes o más (o con ticket alto).
- El precio de IC (400 y 900) lo pone Javi; sus horas de producción y su profit share siguen a definir.

## Historia: cómo se llegó (conviven en documentos viejos)

| | Modelo en las skills (vigente en documentos) | Modelo de paquetes (propuesta del CTO) |
|---|---|---|
| Fuente | `aurea-ic-conocimiento`, `aurea-estetica-documentacion`, propuesta DRAKON | "Modelo de pricing por cliente · Aurea" (Javier Sculli, oct-2026, documento de trabajo para los socios) |
| Implementación | Fee mensual durante 2 a 3 meses (DRAKON: USD 850/mes) | Setup por horas × USD 45, con piso. Esencial ~60 h (USD 2.700), Crecimiento ~100 h (USD 4.500), Escala ~150 h (USD 6.750). Financiable en cuotas, nunca bonificado |
| Operación | Mejora Continua Start USD 200 / Pro desde USD 450 | % de la facturación del cliente con licencia y consumo incluidos: ~1% / ~1,5% / ~2% (piso USD 400 a 500) |
| IC | USD 200/mes un canal + USD 50 por canal extra | Producto propio: no en Esencial, desde USD 500 en Crecimiento, desde USD 1.000 en Escala |
| Descuento | Bonificaciones por ítem | Solo por plazo (contrato de 12 meses) |
| Argumento | Ahorro ("cuesta menos que una persona") | Impacto: crecimiento de ventas y decisiones con datos |

**Ya se usó con un cliente:** en la reunión con PAVIR del 23/10 Magalí presentó los tres escenarios
(Esencial, Crecimiento y Escala) y un contrato de duración mínima anual (notas de Gemini, 23/10).
El documento del CTO dice "propuesta de trabajo para discutir con los socios".

## Lo que se fue decidiendo en reuniones (notas de Gemini)
- 14/09 (Follow up equipo): implementación con Prometheo desde USD 850, IC USD 200/mes + 50 por
  canal, contrato anual, implementación de 3 meses como máximo. Hora de trabajo: **USD 50**.
- 15/10: niveles cerrados, con IC dentro de la base y un nivel Pro para lo avanzado.
- 23/10 (PAVIR): se presentan Esencial, Crecimiento y Escala.
- El documento del CTO usa **USD 45** la hora: unificar con los USD 50 del 14/09.

## Decisión abierta
- [ ] ¿Cuándo pasa a vigente el modelo de paquetes? Hoy está en construcción (23/10). Si sí, hay que actualizar `aurea-ic-conocimiento`
  (precio de IC), `aurea-estetica-documentacion` (nuevos servicios y género presupuesto) y el
  ejemplo DRAKON, y rehacer la propuesta de EAF con los tres paquetes (lo pide el propio documento).
- [ ] Resuelve dos pendientes de `aurea-ic-conocimiento/hallazgos.md`: "el precio de IC se fijó sin
  cálculo" e "IC sola USD 200 vs Mejora Continua Pro USD 300".

## Reglas del modelo de paquetes (si se aprueba)
- El cliente elige un paquete, no arma un menú. Esencial queda corto a propósito; Crecimiento es el
  recomendado; Escala es el ancla.
- Facturación estimada en la primera reunión: (empleados × USD 600) ÷ 0,7 ≈ USD 850 por empleado por
  mes. En el discovery se reemplaza por el dato real (ventas × ticket).
- Target mínimo: Crecimiento no supera ~4% de la facturación → piso ~USD 25.000/mes (unos 30
  empleados). Debajo, solo Esencial.
- Ejemplo del documento, EAF (30 personas, ~USD 25.000/mes): hoy USD 2.100 de implementación y
  USD 200/mes; en Crecimiento, USD 4.500 y USD 900/mes (necesita +3,6% de ventas para cubrirse).
- Pendientes del propio documento: calibrar horas con 2 o 3 implementaciones reales, validar
  facturación por empleado, relevar métricas de impacto (leads por mes, tiempo de primera respuesta,
  % fuera de horario atendido, conversión, leads recuperados) y definir IC estándar vs avanzada.

## Reglas que valen con cualquier modelo
- Precio de lista con IVA 21% e Ingresos Brutos aunque hoy no se paguen; la diferencia se muestra
  como descuento (`aurea-ic-conocimiento`).
- No publicar precios de marketing en piezas comerciales.
- Números defendibles, rotulados como referencia.

## Log
- 2026-10-23: se detecta que el modelo de paquetes ya se presentó a PAVIR y no está en ninguna skill.
