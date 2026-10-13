# Rubro · Real estate (desarrollista: pozo, construcción, entrega inmediata)

Estado: **validado con cliente** (EDFAN Real Estate, octubre 2026). Combina con la vertical
`prometheo-vertical-real-estate` y el molde de 3 embudos de `aurea-metodologia`
(Recepción y Calificación / Venta y Cierre / B2B Inmobiliarias).

## 1. Tipo de contacto (antes de calificar)
| Valor | Qué es | Qué se hace |
|---|---|---|
| Comprador | Busca vivienda o inversión | Se califica |
| Inmobiliaria | Corredor que trae clientes | Embudo B2B (Inmo x Contactar → Inmo en Gestión → …) |
| Proveedor | Ofrece productos o servicios | Se deriva sin calificar; el tag apaga el asistente |
| Desarrollador | Otra desarrolladora (alianzas, terrenos) | Se deriva sin calificar |
**Regla del rubro:** proponer una línea de WhatsApp aparte para inmobiliarias, proveedores y
desarrolladores, atendida por el equipo y sin agente. Ahorra tokens y saca la no-demanda del
embudo de compradores. Se promueve siempre en el tablero (pestaña Consumo de Tokens - CRM).

## 2. Lead calificado · definición validada (EDFAN)
| Condición | Tipo | Variable en Prometheo | Cómo se mide |
|---|---|---|---|
| Proyecto o zona que la empresa comercializa | Obligatorio | Proyecto Interés · Zona Interés | Proyecto cargado, o zona donde hay proyecto |
| Ambientes (tipología) que existen | Obligatorio | Tipo Unidad | Tipología pedida que exista en ese proyecto (catálogo Tokko) |
| Intención de compra | Suma | Horizonte Compra | Declarada |
| Finalidad | Suma | Tipo Perfil (Vivienda / Inversión) | Declarada |
| Presupuesto o forma de pago compatible | Suma | Presupuesto · Forma de Pago | Compatible con el precio de la unidad (Tokko) |
| Estado de obra compatible | Suma | Estado Proyecto · Objeción Principal | Sin objeción por entrega |
**Regla:** todos los obligatorios + al menos 2 sumas.
**No califican:** inmobiliarias (B2B), proveedores y desarrolladores (se derivan), No Fit
(buscan algo que no hay: usado, zona sin proyectos, tipología inexistente).

## 3. Hot lead · señales validadas (EDFAN) · con 1 alcanza
| Señal | Cómo se captura |
|---|---|
| Pide visita a obra o reunión | Variable de reunión (día, hora, modalidad) o tag de visita |
| Pide precio, disponibilidad o forma de pago de una unidad concreta | Unidad nombrada (UF) en la conversación |
| Compra ya o en el corto plazo | Horizonte Compra = Inmediato o Corto plazo (**definir los días**) |
| Tiene el dinero o el anticipo, o pregunta por contado | Forma de Pago = Contado o lo declara |
| Vuelve sobre la misma unidad en más de un mensaje | Lo marca el agente (no se ve en el export) |
**Qué se hace:** tag "Hot Lead" (prioridad, fuera del embudo) con notificación según la
finalidad (EDFAN: inversión → Sebastián; vivienda → Tiago o Evelyn), prioridad en el
seguimiento y señal para la pauta.

## 4. Lo que se aprendió en EDFAN (instancia, con números)
Export al 08/10/2026, 874 consultas de compra del 04/07 al 28/09, 542 conversaron.
- Con la regla del cliente: **252 calificados**; **176** si se exige que la tipología la haya
  pedido el lead. Un criterio propio anterior ("3 de 4 datos") daba 350: sobreestimaba 98.
- Por qué no califican: 139 sin proyecto ni zona con proyecto; 66 sin tipología existente;
  85 cumplen obligatorios pero tienen menos de 2 sumas.
- **150 hot leads**; 74 sin seguimiento ni derivación; 40 hot no califican (urgencia antes de datos).
- Reuniones: 38 descritas en la variable de reunión, 8 con tag de visita, 0 en el campo nativo.
- Ruteo: los 66 contactos de inversión figuran con el mismo moderador; el ruteo por finalidad
  no queda registrado.
- "Tipo Unidad" se llenaba con lo que el agente ofrecía (131 registros con varias tipologías).
- "Tipo Perfil" mezclaba finalidad con tipo de contacto (valor "Inmobiliaria"); 6 proveedores
  quedaron como "Inmobiliaria".
- Sin el catálogo de Tokko, "zona con proyecto" y "tipología existente" se derivan del export
  (zona de cada proyecto, tipologías ofrecidas): es aproximado y se declara.

## 5. Plazos y referencias del rubro
- Anticipo típico en pozo: 30% a 40%, cuotas por CAC (ver fuentes). Pedir el anticipo
  disponible es una buena pregunta de capacidad, al final.
- Hot por plazo: referencia externa de 3 meses o menos. El cliente define su número.

## 6. Preguntas para el discovery
1. ¿Qué es para ustedes un lead calificado? (obligatorios, sumas, regla)
2. ¿Y un hot lead? ¿Cuántos días es "corto plazo"?
3. ¿A quién se avisa cada caso (por finalidad, zona o proyecto)?
4. ¿Qué tipologías y zonas tiene cada proyecto? (o acceso a Tokko)
5. ¿Qué hacen con inmobiliarias, proveedores y desarrolladores? ¿Tienen otra línea?
