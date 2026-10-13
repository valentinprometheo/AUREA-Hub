# Fuentes externas · criterio de calificación

Investigación de octubre 2026. Cada cifra lleva su fuente. **[vendor]** = blog de un proveedor
de software: sirve como práctica de mercado, no como estudio. Lo que no se encontró con
fuente está listado al final: no se inventa, se calibra con datos del cliente.

## Frameworks
- **BANT** (presupuesto, autoridad, necesidad, plazo): filtra rápido, pero empieza por el
  dinero. Pensado para venta transaccional de ciclo corto. [vendor] https://www.squadstack.com/blog/useful-lead-qualification-frameworks-compared
- **ANUM** reordena BANT y deja el dinero al final; **CHAMP** arranca por el problema (venta consultiva). Misma fuente.
- **GPCTBA/C&I** (HubSpot): metas, planes, desafíos y plazo; después presupuesto y autoridad.
  Regla: el presupuesto se pregunta **después** de confirmar que se puede ayudar en el plazo. https://blog.hubspot.com/sales/gpct-sales-qualification
- **MEDDIC**: solo como referencia, para ventas enterprise con varios decisores.
- **Para un agente por WhatsApp:** orden necesidad → plazo → capacidad → presupuesto. BANT
  literal en el primer mensaje es la opción equivocada.

## Scoring: perfil, interés, negativo y decaimiento
- HubSpot separa Fit (perfil), Engagement (interacción) y Combined; admite puntos negativos y
  decaimiento periódico (ej. −30% por mes). https://www.iodigital.com/en/insights/blogs/everything-you-need-to-know-about-hubspot-new-lead-scoring-model
- Salesforce Einstein Behavior Score (0 a 100) incorpora decaimiento por recencia. https://trailhead.salesforce.com/content/learn/modules/lead-scoring-and-grading-in-account-engagement/einstein-scoring-in-account-engagement
- Separar perfil de interés evita que alguien muy activo pero sin perfil (estudiante, buscador
  de trabajo, proveedor) supere a un comprador. Piso en 0 para que pueda recalificar. https://nation.marketo.com/t5/product-discussions/can-a-lead-score-be-negative/m-p/69765
- No hay un benchmark universal de calificación: depende del ticket, el canal y la definición
  (Forrester). https://go.forrester.com/blogs/themythofthebestinclasswaterfallbenchmark/

## Hot lead y plazo
- Follow Up Boss: *Hot Prospect* = se mudaría en los próximos 3 meses; *Nurture* = más de 3.
  Variante Ylopo: A (1 a 3 meses), B (3 a 6), C (6 o más). https://help.followupboss.com/hc/en-us/articles/360012456793-Changing-a-Lead-Stage
- El plazo declarado es la variable de temperatura con más respaldo.

## Velocidad de respuesta (speed-to-lead)
- HBR 2011 (2.241 empresas): 37% respondió en menos de 1 h, 23% nunca. Contactar en menos de
  1 h dio casi **7 veces** más chances de calificar que una hora después, y más de 60 veces más
  que a las 24 h. https://hbr.org/2011/03/the-short-life-of-online-sales-leads
- MIT/InsideSales: 5 minutos contra 30 → **21 veces** más chances de calificar. https://resources.insidesales.com/?p=4167
- Velocify (3,5 M de leads): llamar en el primer minuto mejora la conversión cerca de 391%; a la
  hora, 36%. https://www.marketingcharts.com/wp/traditional/b2b-leads-once-again-speed-to-call-counts-38711/
- Son correlaciones, mayormente B2B de EE.UU. Regla práctica: respuesta inmediata del agente y
  derivación del hot lead medida en minutos.

## Conversación y cantidad de preguntas
- HubSpot (40.000 landing pages): los campos sensibles bajan la conversión (teléfono: de 19% a
  13%). https://smartbugmedia.com/blog/landing-page-best-practices-how-many-form-fields
- No hay fuente seria sobre el número óptimo de preguntas de un chatbot. Consenso [vendor]:
  pocas, repartidas, con tono de charla. https://www.giosg.com/blog/how-to-qualify-leads-with-chatbots
- Rutear la no-demanda (soporte, clientes, postulantes, proveedores) antes de calificar. [vendor] https://codewords.ai/blog/whatsapp-lead-qualification-bots

## Devolver la señal a Meta
- Conversions API para mensajería (anuncios a WhatsApp, Messenger, Instagram): `action_source:
  business_messaging`, `ctwa_clid` obligatorio; eventos LeadSubmitted, QualifiedLead, Purchase. https://developers.facebook.com/docs/marketing-api/conversions-api/business-messaging
- "Conversion Leads" (solo formularios instantáneos) pide 200+ leads por mes, una etapa que
  convierta entre 1% y 40% y que ocurra dentro de 28 días. https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration

## Por rubro
- **Desarrollos en pozo (AR):** anticipo típico 30% a 40%, cuotas en obra ajustadas por CAC. https://mudafy.com.ar/blog/post/conviene-comprar-un-departamento-en-pozo-durante-2022-en-argentina · el pozo cotiza 15% a 25% debajo de lo terminado. https://mercado.com.ar/ladrillos-y-proyectos/la-compra-de-inmuebles-en-pozo-crece-en-la-ciudad-de-buenos-aires-y-amplia-opciones
- **Crédito hipotecario (AR):** relación cuota-ingreso 25%, financiación hasta 80%, 1 año de
  antigüedad laboral. https://www.iprofesional.com/economia/420839-creditos-hipotecarios-cuales-son-principales-opciones-disponibles-enero-2025 · 40.508 hipotecas en 2025, promedio USD 90.000. https://www.forbesargentina.com/negocios/creditos-hipotecarios-realizaron-40000-operaciones-pero-mercado-entra-una-fase-mayor-cautela-n84715/amp
- **Inmobiliaria (EE.UU., referencia):** la mayoría de los compradores entrevista a un solo
  agente (73% en 2021): ser el primero importa. https://rismedia.com/?p=249450
- **Materiales:** el contratista compra volumen y repite; el particular compra una vez. https://offdeal.io/blog/everything-you-need-to-know-about-selling-a-building-materials-supply · obras perdidas por precio: 23% (2006) a 36% (2010/11), dato viejo. https://www.lek.com/sites/default/files/insights/pdf-attachments/L.E.K._Residential_Building_Contractors_Shift_Their_Buying_Behaviour_as_Slowdown_Bites.pdf
- **Mobiliario:** programas para profesionales con validación, 10% a 20% de descuento y a veces pedido mínimo. https://www.crateandbarrel.com/business-sales/ · capturar tipo de proyecto, m² y estilo antes de la cita de showroom [vendor]. https://www.agendize.com/en/blog/leviers-orchestration-rdv-cuisinistes
- **Educación:** 44% de las consultas a instituciones sin respuesta (UPCEA, dic. 2025). https://upcea.edu/wp-content/uploads/2025/11/Enrollment-Process-Review-Secret-Shopper-Analysis_December-2025.pdf · mediana de respuesta 3 h 03 min (2023). https://upcea.edu/a-look-in-the-mirror-using-inquirers-perspectives-to-understand-enrollment-funnels/ · una conversación genuina triplica la probabilidad de inscripción. https://monitor.icef.com/2021/10/mystery-shopping-study-highlights-lost-opportunity-for-enquiry-conversion

## Plataformas que documentan su criterio
HubSpot y Salesforce (scoring con perfil, interés, negativo y decaimiento), Follow Up Boss
(etapas por plazo), kvCORE (scoring por comportamiento, sin umbrales públicos), Respond.io y
Kommo (bots de WhatsApp que califican y rutean). Tokko Broker: no hay documentación pública de
scoring automático.

## No encontrado con fuente (calibrar con datos propios)
Número óptimo de preguntas de un chatbot · tasa estándar de decaimiento · tiempos de decisión
en el pozo argentino · participación del canal profesional en materiales o mobiliario ·
conversión de showroom · criterio de scoring de Tokko.
