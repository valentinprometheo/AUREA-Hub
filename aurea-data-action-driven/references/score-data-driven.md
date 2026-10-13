# Score data-driven

[DEFINICIÓN AUREA] Porcentaje de 0 a 100 que dice cuánto de una acción se apoya en datos
verificables. No existe un estándar externo para esto: la rúbrica es propia, sus pesos
son una versión 1 y se calibran con resultados reales (ver al final).

## Rúbrica (suma 100)

| # | Componente | Pts | Niveles | De dónde sale |
|---|---|---|---|---|
| 1 | Base y denominador | 20 | 0 sin n · 8 n menor a 30 o denominador ambiguo · 14 n de 30 a 99 con denominador explícito · 20 n de 100 o más con denominador explícito | Provost y Fawcett; curaduría del dato |
| 2 | Fuente y trazabilidad | 15 | 0 "lo dijo alguien" · 5 captura o caso suelto · 10 export con fecha de corte · 15 export reproducible y cruce verificado (ej. Meta × Prometheo por ID) | Curaduría del dato |
| 3 | Cobertura de la variable | 15 | 0 menos de 50% o desconocida · 7 de 50 a 79% · 11 de 80 a 94% · 15 de 95% o más | Curaduría del dato |
| 4 | Profundidad del análisis | 20 | 5 solo descriptivo · 10 diagnóstico con causa probable · 15 causa contrastada (segmento, período o grupo comparable) · 20 lo anterior más efecto estimado con cálculo visible | Escalera de Gartner |
| 5 | Evidencia previa de la acción | 15 | 0 nunca probada ni referida · 5 buena práctica externa o criterio experto · 10 funcionó en otro cliente AUREA con métrica · 15 verificada en este cliente en un período anterior | Ries (aprendizaje validado) |
| 6 | Cierre medible | 15 | 0 sin métrica · 5 métrica distinta del dato · 10 misma métrica sin fecha o sin guardiana · 15 misma métrica, base, fecha y guardiana | Build-Measure-Learn; Goodhart |

El umbral de n = 30 es una heurística de AUREA para volúmenes chicos, no un test de
significancia. Si el cliente tiene volumen para un test formal, usalo y anotalo en "por qué".

## Bandas

| Score | Etiqueta | Tratamiento |
|---|---|---|
| 80 a 100 | Basada en datos | Se ejecuta y se mide |
| 55 a 79 | Informada por datos | Se ejecuta; el "por qué" dice qué parte es criterio |
| 30 a 54 | Hipótesis con indicio | Prueba acotada (un conjunto, una sección, una quincena) |
| 0 a 29 | Criterio experto | Solo *Medir* o *Decidir*, o con aval explícito del dueño |

## Cómo se escribe el "por qué este score"

Una línea por componente con los puntos, en el despliegue de la card:

> Base 20 (n=406) · Fuente 10 (export Prometheo 15/10, sin cruce) · Cobertura 15 (conteo
> del sistema) · Profundidad 20 (comparado contra leads de varias consultas, ahorro
> calculado) · Evidencia 5 (criterio, no probado antes) · Cierre 15 = **85%**

Si un componente no aplica, no se reparte su peso: vale 0 y se explica. Así el score
nunca se infla por omisión.

## Prioridad entre cards

Primero impacto esperado (como en `aurea-ic-performance-report`); el score desempata y
define la etiqueta. Una card de alto impacto y score bajo se convierte en prueba acotada,
no se descarta.

## Calibración

Al cerrar cada período, registrá por card: score, banda y resultado (cumplió / parcial /
no cumplió). Con 20 cards cerradas, mirá la tasa de acierto por banda. Si "Basada en
datos" acierta menos de 70% o "Hipótesis" acierta más que "Informada", los pesos están
mal: ajustalos y subí la versión de la rúbrica en este archivo.
