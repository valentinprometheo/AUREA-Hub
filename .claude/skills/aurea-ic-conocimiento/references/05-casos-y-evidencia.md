# 05 · Casos y evidencia

Regla: cada caso dice qué es **real** y qué es **ilustrativo**. En piezas comerciales, los clientes van anónimos salvo permiso.

| Caso | Rubro y tipo de venta | Qué demuestra | Estado del dato |
|---|---|---|---|
| EDFAN Real Estate | Desarrollista inmobiliario, B2C con pauta | Atribución por anuncio y estrategia de entrada con informe de demanda | Real |
| BETROX | Mobiliario, B2C/B2B | Base de Prometheo con muchas variables; el cruce por ID de anuncio funciona | Real (base), resto en construcción |
| PAVIR | Fábrica con red de distribuidores, B2B | IC se adapta a cualquier lógica comercial | Real (tablero) |
| EAF | Escuela de fotografía, inscripción por curso | Tablero de referencia (V3) con pestañas por rubro | Real (tablero) |
| DRAKON Machines | Maquinaria industrial, B2B | Tablero y presupuesto modelo; estética canónica | Ilustrativo (datos ficticios) |

## EDFAN Real Estate
- El tablero ya atribuye a su anuncio el **64%** de las consultas; el **36%** queda sin atribuir hasta tener el export de Meta. [Real]
- Con el export de Meta se suma: costo por consulta real por anuncio, ROI por campaña, qué anuncio rinde y cuál no, costo por proyecto (por ejemplo, traer un interesado a un desarrollo frente a otro).
- Estrategia: el **informe de demanda** (con lo que ya hay en Prometheo) es el gancho para que pasen el export de Meta. Además da a AUREA un caso con datos curados de dos meses.
- Lección de calificación: con un criterio propio de AUREA el tablero mostró 350 calificados; con la regla del cliente eran 252 (176 en la lectura estricta). El criterio de calificación es **del cliente** (ver `aurea-hub-criterio-calificacion-leads`). [Real]

## PAVIR · B2B
Red de distribuidores. Las decisiones del tablero se traducen en "Qué hago ahora": **cobrar** lo vencido, **visitar** a quien le toca recomprar, **despertar** a los dormidos. Úsalo como ejemplo de que IC no impone una lógica: se adapta a la del negocio.

## Supuestos de dimensionamiento (siempre marcados como ilustrativos)
- **Lo que se quema a ciegas:** con USD 3.000 por mes de pauta, si un 40% va a campañas que traen clics pero no ventas, son USD 14.400 al año. [Supuesto ilustrativo]
- **Dos lecturas del mismo lead:** la campaña A trae los leads más baratos (parece la ganadora); el cruce muestra que ninguno compró y que la B, más cara por lead, vende. [Ilustrativo]

## Pendiente de evidencia
- Primer caso medido de punta a punta (pauta + venta) con resultado de negocio.
- Test de product-market fit con clientes que ya ven el tablero.
