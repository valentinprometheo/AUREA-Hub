# Ejemplos

Los números de los ejemplos 2, 3, 5 y 6 son ilustrativos; el ejemplo 1 sale del caso real
de consumo de tokens. No los copies como datos de un cliente.

## Buenos

**1. Corregir · AUREA**
Título: Mensajes por lead · 406 leads de una consulta recibieron 4,8 mensajes.
Contexto: mensajes del agente por lead que hizo una sola consulta / base 406 leads /
1.949 envíos (Prometheo, consumo del período).
Qué hacer: primera respuesta con la entrega pedida + una sola pregunta de calificación.
Dónde: prompt del agente, sección de primera respuesta.
Efecto: −1.118 envíos en el próximo período (de 4,8 a 2,05 mensajes por lead).
Cómo lo medimos: mensajes por lead de una consulta, misma base. Guardiana: tasa de
calificación no baja.

**2. Separar · AUREA**
Título: Consumo de no-demanda · 21% de los tokens se gastan con inmobiliarias.
Contexto: tokens del agente por tipo de contacto / base 1.320 conversaciones / Prometheo.
Qué hacer: detectar inmobiliaria en el primer mensaje, etiquetar y derivar sin calificar.
Dónde: prompt (sección de no-demanda) + tag "no-demanda: inmobiliaria".
Efecto: −18% de tokens del período. Cómo lo medimos: tokens por tipo de contacto.

**3. Proteger · Marketing**
Título: Costo por lead calificado · el conjunto "Visitantes 30d" cuesta $4.100 contra $9.800.
Contexto: costo por lead calificado por conjunto / base 312 leads calificados / Meta × Prometheo por ID de anuncio.
Qué hacer: mantener presupuesto y creativo; no incluirlo en la prueba de nuevos públicos.
Dónde: Administrador de anuncios, campaña Leads Q4.
Efecto: CPL calificado del conjunto se mantiene debajo de $5.000. Cómo lo medimos: mismo cruce.

## Malos (y por qué)

**4. "Optimizar el prompt."**
Sin dato, sin base, sin dueño, sin lugar, sin efecto. "Optimizar" no es un verbo del sello.
Versión buena: ejemplo 1.

**5. "Corregir · Meta · el CPL subió mucho, hay que bajar costos."**
"Meta" no es un dueño; "mucho" no es un dato; no dice qué conjunto ni cuánto. No tiene
denominador (¿lead o lead calificado?). Reescritura: "Corregir · Marketing · CPL calificado
del conjunto X pasó de $6.200 a $11.400 (base 140, Meta × Prometheo) → pausar los dos
anuncios con CTR menor a 0,6% en el conjunto X; efecto: CPL calificado debajo de $7.500".

**6. "Medir · AUREA · ahorrar tokens bajando la cantidad de mensajes."**
Verbo equivocado (es una corrección, no una medición) y premia la métrica sin guardiana:
cortar mensajes puede dejar leads sin calificar (Goodhart). Además no dice dónde se cambia.
