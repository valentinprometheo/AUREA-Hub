# EMPEZÁ ACÁ — Metodología AUREA × Prometheo

> **Si sos Claude y estás leyendo esto:** este es el punto de entrada de la metodología.
> Leé este archivo completo antes de hacer nada. Te dice qué es esto, cómo está organizado
> y, sobre todo, cómo ubicarte para arrancar a trabajar con un cliente desde la etapa en
> que esté. No empieces a generar entregables sin antes hacer el diagnóstico de abajo.

---

## Qué es esto

Esta es la metodología de consultoría de **AUREA Hub** para implementar **Prometheo**
(CRM con IA) en clientes. Cubre todo el proceso, de la primera reunión al monitoreo
post-lanzamiento. Está pensada para que un consultor —con Claude de copiloto— pueda tomar
cualquier cliente, de cualquier rubro, en cualquier punto del proceso, y avanzar.

---

## Cómo arrancar — diagnóstico en 3 preguntas

> **Para la consulta operativa detallada, el router es `01-metodologia/00-CONSULTA.md`.**
> Ese archivo amplía este diagnóstico a cuatro ejes (proceso, rubro, integración,
> transversal) y resuelve los dos modos (conversación nueva vs con trayectoria). Este
> bloque es la versión corta para ubicarse; el router es la herramienta para ensamblar
> exactamente qué cargar.

Antes de trabajar, Claude le pregunta al consultor (si no surge del contexto):

1. **¿Qué cliente y de qué rubro?** Los rubros con vertical propia son: desarrollista
   inmobiliario, mobiliario, insumos para construcción, inmobiliaria. Un cliente que no
   encaje en esos cuatro se trabaja con la metodología transversal sola.
2. **¿En qué etapa está?** Etapa 1 Discovery / Etapa 2 Diseño / Etapa 3 Lanzamiento /
   Etapa 4 Mejora continua.
3. **¿Qué hay hecho ya?** Qué entregables existen, qué se validó con el cliente. (Si el
   cliente tiene trayectoria, esto define el modo trayectoria del router: traer solo el
   delta y el estado del cliente, no recargar la metodología entera.)

Con esas tres respuestas, Claude va al router `00-CONSULTA.md`, arma la intersección de
ejes, y carga solo lo que esa tarea necesita.
No hace falta empezar de cero: la metodología está hecha para entrar en cualquier punto.

---

## Mapa de etapas — dónde está cada cosa

### ETAPA 1 — Discovery
Relevar el negocio del cliente y dejarlo documentado en la Biblia (Doc 1).

- **Antes de la primera reunión:** `01-metodologia/01-ETAPA1-Discovery/01-PASO1-Pre-Discovery/` — auditoría web, doc de bienvenida, guía metodológica.
- **El relevamiento:** `01-metodologia/01-ETAPA1-Discovery/02-PASO2-Discovery/` — la Biblia (Doc 1), el asincrónico (Doc 2), accesos (Doc 3), validación.
- **La estructura de bloques del Discovery:** `01-ETAPA1-Discovery/02-PASO2-Discovery/estructura-discovery.md` — **fuente única**, los 14 bloques B0-B13.
- **Skills:** `prometheo-auditoria-web`, `prometheo-discovery-transversal` + la skill vertical del rubro + la skill de formulario del rubro.

### ETAPA 2 — Diseño
Diseñar el CRM y el prompt del agente a partir de la Biblia.

- **Modelo de datos (leer primero):** `01-metodologia/02-ETAPA2-Diseno/embudos-y-tags.md` — Tags, Variables y Embudos. La regla AUREA de "una tag por dimensión" (estadío + tipo de usuario + prioridad opcional).
- **Las reglas de diseño:** `02-ETAPA2-Diseno/03-reglas-diseno-prometheo-by-aurea.md`.
- **Restricciones de plataforma:** `02-ETAPA2-Diseno/restricciones-plataforma-prometheo.md`.
- **Integraciones por rubro:** `02-ETAPA2-Diseno/integraciones-por-rubro.md`.
- **Seguimientos:** `02-ETAPA2-Diseno/framework-seguimientos.md`.
- **Excel de carga del cliente (4º output):** `02-ETAPA2-Diseno/excel-carga-clientes.md`.
- **Feedback de demo (iteración con cliente):** `02-ETAPA2-Diseno/feedback-demo-iteracion.md`.
- **Carga de datos en Prometheo:** `02-ETAPA2-Diseno/importacion-contactos.md`.
- **Skill:** `prometheo-etapa2-design` (v2 con SECCIÓN 0 — arquitectura de 3 capas).

### ETAPA 3 — Lanzamiento
Implementar lo diseñado en Prometheo y salir a producción.

- `01-metodologia/03-ETAPA3-Lanzamiento/` — protocolo de implementación y de Go-Live.
- El orden de carga (variables → tags → embudos → contactos) está en `importacion-contactos.md`.

### ETAPA 4 — Mejora continua
Monitorear y optimizar el agente ya en producción.

- `01-metodologia/04-ETAPA4-Mejora-Continua/` — protocolo de monitoreo.

---

## Reglas de oro — aplican siempre, en cualquier etapa

1. **Nunca asumir comportamiento de la plataforma Prometheo.** Lo no confirmado se valida
   con el bot oficial de Prometheo (vía WhatsApp) o con ITESA. Lo que no se pudo confirmar
   va a `02-ETAPA2-Diseno/pendientes-itesa.md`, no a las reglas.
2. **Fuente única.** Cada dato vive en un solo archivo; los demás lo referencian. Si algo
   hay que cambiarlo, se cambia en su archivo fuente. Todo cambio se registra en
   `CHANGELOG.md`.
3. **El archivo de reglas no se toca sin aprobación.** Cambiar
   `03-reglas-diseno-prometheo-by-aurea.md` requiere aprobación del consultor, regla por
   regla (camino B).
4. **MVP primero.** Mejor lanzar con poco y bien que esperar a tener todo perfecto.
5. **Trabajar en bloques con validación.** Entregables uno por uno, con aprobación entre
   cada uno. Nunca mega-entregas sin checkpoint.
6. **Cada vertical tiene su tipología macro** — no intercambiar: proyecto (desarrollista),
   línea de producto (mobiliario), categoría + tipo de cliente (insumos), propiedad
   (inmobiliaria).

---

## Para orientarte en el detalle

- **Manual completo de cada archivo:** `README.md` — qué hace cada archivo, cuándo se usa.
- **Índice maestro condensado:** `01-metodologia/00-INDEX.md`.
- **Historial de versiones:** `CHANGELOG.md`.
- **Roadmap (qué falta construir):** `01-metodologia/roadmap.md`.
