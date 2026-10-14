# Tablero de Inteligencia Comercial · TKVA

`IC_Dashboard_TKVA.html` es el tablero autocontenido (abrir en el navegador). Estructura y diseño
replicados del tablero de EDFAN Real Estate, con los datos reales de TKVA.

- **Fuentes:** export de Prometheo al 14/10/2026 (1.470 contactos), panel de consumo de IA
  (agosto a octubre al 14), resumen técnico TKVA × LT, reporte semanal de Vanesa, contrato.
- **Calificación:** criterio de EDFAN aplicado a TKVA, rotulado "propuesta a validar". Rango 55 a 118.
- **14 pestañas:** Panorama, Reporte comercial (formato del reporte de Vanesa), Evolución,
  Venta · CRM, Vanesa y el agente, Proyectos, Inmobiliarias y proveedores, Demanda,
  Criterio comercial, Insights y accionables, Meta, Consumo variable CRM (Tokens IA | META),
  Audiencias, Integraciones.
- **MC · Start / MC · Pro:** quién ejecuta cada mejora (plan de Mejora Continua vs desarrollo).

## Regenerar

`generador/` tiene el pipeline: `load.py` → `curate.py` → `master.py` (cifras en `D.json`)
→ `build.py` (usa `tabs1.py`, `tabs2.py`, `R.json` y la plantilla HTML de EDFAN).
Las rutas a los archivos fuente apuntan a la carpeta de uploads de la sesión: ajustarlas
para correrlo con un export nuevo.
