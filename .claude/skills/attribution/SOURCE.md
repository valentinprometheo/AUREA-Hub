# attribution (vendored)

Community skill by Corey Haines — MIT License.
Source: https://github.com/coreyhaines31/marketingskills (`skills/attribution`)

## Por qué está acá
Es la skill que ordena la parte de **"de qué anuncio vino cada consulta"** de
nuestros tableros de Inteligencia Comercial (EDFAN, DRAKON). Trata el problema
que ya nos apareció con datos reales: qué campaña causó cada lead, cómo leer los
que quedan **sin atribución**, y cómo cruzar lo cualitativo con lo cuantitativo.

## Cómo la usamos en el tablero IC
- **Sección "De qué anuncio vino"** (cards por anuncio): elegir el modelo
  (first-touch vs last-touch) y mostrar ambos cuando difieren; el gap es el insight.
- **Los "sin dato" no son ruido**: en EDFAN, 36% de las consultas entran sin
  anuncio identificado (direct / dark social / branded search). La skill los nombra
  como blind spots estructurales, no como error de carga.
- **Cualitativo + cuantitativo**: el "¿cómo nos conociste?" auto-reportado (texto
  libre + pick-list) es la triangulación contra lo que el tracking no ve. Se combina
  con el conteo por `Anuncio` / `ID Anuncio` de Prometheo.
- **Escribir el `source` al CRM** con nivel de confianza (journey-linked /
  auto-reportado / fallback): es lo que vuelve accionable la atribución por lead,
  no solo un gráfico.

## Depende de
Se apoya en Prometheo (captura `Anuncio` + `Canal Origen` por consulta). Se potencia
al conectar la cuenta de Meta (gasto), que hoy falta para cerrar costo por consulta
y ROI por campaña.
