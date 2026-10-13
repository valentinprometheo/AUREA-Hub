# Ejemplos

El ejemplo 1 sale del caso real de consumo de tokens. Los demás números son ilustrativos:
no los copies como datos de un cliente.

## Buenos (de score alto a score bajo: los tres son válidos)

**1. Corregir · AUREA · 85% basada en datos**
Mensajes por lead · 406 leads de una consulta recibieron 4,8 mensajes.
Contexto: mensajes del agente por lead con una sola consulta / 406 leads / 1.949 envíos (Prometheo).
Qué hacer: primera respuesta con la entrega pedida + una sola pregunta de calificación.
Dónde: prompt del agente, sección de primera respuesta.
Efecto: −1.118 envíos en el próximo período (de 4,8 a 2,05 por lead).
Cómo lo medimos: mensajes por lead de una consulta, misma base. Guardiana: % de calificación.
Por qué: Base 20 · Fuente 10 · Cobertura 15 · Profundidad 20 · Evidencia 5 · Cierre 15.

**2. Separar · AUREA · 77% informada por datos**
Consumo de no-demanda · 21% de los tokens se gastan con inmobiliarias.
Contexto: tokens por tipo de contacto / 1.320 conversaciones / Prometheo; tipo cargado en 72%.
Qué hacer: detectar inmobiliaria en el primer mensaje, etiquetar y derivar sin calificar.
Dónde: prompt (sección de no-demanda) + tag "no-demanda: inmobiliaria".
Efecto: −18% de tokens. Guardiana: ningún comprador final etiquetado como inmobiliaria.
Por qué: Base 20 · Fuente 10 · Cobertura 7 · Profundidad 15 · Evidencia 10 (funcionó en otro cliente) · Cierre 15.

**3. Activar · Marketing · 45% hipótesis con indicio**
Creativo en video · 22 leads calificados a $5.200 contra $8.900 del carrusel.
Contexto: costo por lead calificado por creativo / 22 y 31 leads / Meta × Prometheo por ID; 70% con ID.
Qué hacer: pasar 30% del presupuesto del carrusel al video durante una quincena, como prueba.
Dónde: Administrador de anuncios, campaña Leads Q4, conjunto Visitantes 30d.
Efecto: CPL calificado del conjunto debajo de $7.000. Revisión: cierre de quincena.
Por qué: Base 8 (n chico) · Fuente 10 · Cobertura 7 · Profundidad 10 (sin aislar público) · Evidencia 0 · Cierre 10 (sin guardiana).
Es buena aunque el score sea bajo: lo declara, acota la prueba y fija la fecha (T9).

## Malos (y por qué)

**4. "Optimizar el prompt."**
No tiene dato, dueño, lugar ni efecto, y "optimizar" no es uno de los verbos del sello. El score no se puede calcular. La versión buena es el ejemplo 1.

**5. "Corregir · Meta · el CPL subió mucho, hay que bajar costos."**
"Meta" no es un dueño y "mucho" no es un dato. Tampoco dice si se mide sobre lead o sobre lead calificado. El score quedaría en 0 a 29, y la card ni siquiera lo admite.
Reescritura: "Corregir · Marketing · CPL calificado del conjunto X pasó de $6.200 a
$11.400 (base 140, Meta × Prometheo) → pausar los dos anuncios con CTR menor a 0,6%".

**6. "Corregir · AUREA · 95% basada en datos · bajar a 2 mensajes por lead para ahorrar tokens."**
El score está inflado y no trae "por qué". No hay guardiana, así que el cierre vale 10 como máximo. Además, cortar mensajes puede dejar leads sin calificar: es el caso de Goodhart (T7). Tampoco dice dónde se hace el cambio.
