# revops (vendored)

Community skill by Corey Haines — MIT License.
Source: https://github.com/coreyhaines31/marketingskills (`skills/revops`)

## Por qué está acá
Es la skill de **curación y auditoría** del dato comercial. Ordena la pestaña
**"Calidad de datos"** de nuestros tableros IC y el embudo por estados/tags: qué
campos deben estar completos, en qué etapa, y cómo pasar de un CRM prolijo a un
reporte confiable.

## Cómo la usamos en el tablero IC
- **Pestaña "Calidad de datos"**: la doctrina de *data hygiene* (dedupe, campos
  requeridos por etapa, progressive profiling, checklist de auditoría trimestral)
  es exactamente el marco para marcar faltantes. Ej. EDFAN: `Reuniones` 0%,
  `Presupuesto` 9%, `Tipo Perfil` 26%.
- **"Bloquear el avance de etapa si faltan campos"**: regla clave para que el agente
  de Prometheo no marque `Calificado` sin línea + zona + perfil cargados.
- **Definición de etapas del embudo** (entry/exit + dueño): traduce los tags de
  Prometheo (En Conversación → En Seguimiento → Calificado → Visita → Derivado) a un
  funnel medible, con la conversión lead → visita → reserva que hoy no se puede leer.
- **Lead scoring / calificación**: base para priorizar, adaptando los criterios de
  fit del SaaS B2B (donde nace la skill) a real estate (tipo de unidad, perfil
  inversor vs vivienda, forma de pago, horizonte).

## Adaptación necesaria
La skill es B2B SaaS de origen. Para real estate se ajustan las señales: fit por
proyecto/zona/tipología, engagement por respuesta y visita, y las variables propias
del rubro (Tokko, estado de obra). El framework de higiene y etapas se reusa tal cual.
