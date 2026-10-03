# Inteligencia Comercial (IC): dimensionamiento de mercado AR / UY / PY

Fecha de corte: 2026-10-03. Cada cifra lleva el código de la fila de `fuentes.csv` (F01–F76) que la respalda. Los precios de los competidores están en `competencia.csv`. Cuando un número es **supuesto** (sin fuente que lo mida), está marcado así.

---

## 1. Resumen ejecutivo

| | Conservador | Base | Optimista |
|---|---|---|---|
| **TAM** (clientes pyme de agencias que pautan en Meta y venden por WhatsApp) | 3.854 clientes · **USD 1,2 M/año** | 17.180 clientes · **USD 8,2 M/año** | 65.033 clientes · **USD 54,6 M/año** |
| **SAM** (de ese TAM, con CRM + agente IA o listos para adoptarlo) | 578 clientes · **USD 0,17 M/año** | 4.295 clientes · **USD 2,1 M/año** | 22.761 clientes · **USD 19,1 M/año** |
| **SOM** a 3 años (bottom-up por agencias socias) | 15 agencias × 3 clientes = 45 · **USD 13.500/año** | 40 × 5 = 200 · **USD 96.000/año** | 80 × 8 = 640 · **USD 537.600/año** |
| Precio a la agencia por cliente final | USD 25/mes | USD 40/mes | USD 70/mes |

**Lectura:**

1. **El mercado es chico en dólares y lo determinan los supuestos más que los datos.** El rango del TAM es de 47 veces (USD 1,2 M a 54,6 M). Tres de los seis parámetros del modelo son supuestos sin dato local: qué parte de las agencias hace performance en Meta, qué parte de sus clientes vende por WhatsApp y qué parte tiene CRM con agente.
2. **Argentina es entre el 78% y el 80% del mercado** en todos los escenarios.
3. **El SOM base (USD 96 mil/año) no sostiene solo un negocio de SaaS puro.** Tiene sentido como capa de valor (*upsell*) sobre la implementación de CRM + agente que AUREA/Prometheo ya vende, o con un componente de servicio cobrado aparte. Esa conclusión es una inferencia propia.
4. **No encontramos ningún jugador que haga lo mismo que IC:** cruzar el ad ID con la conversación calificada por un agente y con la venta, agregar recomendación comercial y venderlo a través de agencias. Los más cercanos (Tintim, Respond.io, Mercately, Kommo) llegan a la venta, pero solo devuelven la señal a Meta o un tablero, sin criterio comercial (ver §6).

---

## 2. Definiciones

- **Cliente final:** pyme que contrata a una agencia para gestionar pauta en Meta y vende o califica por WhatsApp.
- **TAM:** todos los clientes finales de las agencias digitales y de performance de AR, UY y PY cuyo canal de venta es WhatsApp, multiplicado por el precio anual de IC. Es el techo si todas las agencias pusieran IC en todos esos clientes.
- **SAM:** la parte del TAM que hoy puede usar IC. IC necesita que la conversación pase por un CRM donde un agente de IA la califica; sin eso no hay dato para cruzar.
- **SOM:** lo que AUREA puede capturar en 3 años, calculado de abajo hacia arriba como agencias socias activas × clientes activados por agencia. No es un porcentaje arbitrario del SAM.

---

## 3. Fórmula y supuestos

```
TAM = Agencias × %perf × Clientes/agencia × %WhatsApp × Precio × 12
SAM = TAM × %CRM+IA
SOM = Agencias socias × Clientes IC por agencia × Precio × 12
```

### 3.1 Universo de agencias (una sola fuente por escenario; nunca se suman)

| País | Conservador | Base | Optimista | Por qué difieren |
|---|---|---|---|---|
| AR | **2.148** · OEDE, empresas empleadoras en publicidad 2024 (F01, alto) | **4.141** · RevenueBase, "marketing agencies" (F07, medio-bajo) | **6.062** · Coresignal, "Advertising Services" (F04, medio-bajo) | El OEDE solo cuenta firmas con asalariados registrados, pero incluye agencias tradicionales y de medios. Las bases privadas clasifican por descripción web e incluyen firmas sin empleados, PR y contenido. agencias.marketing (9.280, F10) incluye freelancers y no tiene metodología, así que lo descarté. |
| UY | **535** · D&B NAICS 5418 (F08, bajo) | **737** · Coresignal (F05, medio-bajo) | **737** · Coresignal (F05) | No hay dato oficial accesible (la tabla del INE dio error 503). D&B incluye PR. Los directorios curados (Clutch ~40, GoodFirms 15) solo miden agencias visibles. |
| PY | **328** · Coresignal (F06, medio-bajo) | **328** · Coresignal (F06) | **943** · D&B NAICS 5418 (F09, bajo) | El DIRGE del INE no abre la clase 7310. D&B incluye PR y es solo un snippet de búsqueda. |

Contexto de tamaño: en Argentina, el 83% de las firmas empleadoras de publicidad tiene entre 1 y 9 empleados (F02, medio-alto), y RevenueBase da un 77% con 1 a 10 empleados (F07). El universo es mayoritariamente boutique, que es el perfil objetivo.

### 3.2 Parámetros del embudo

| Parámetro | Cons. | Base | Opt. | Respaldo | Tipo |
|---|---|---|---|---|---|
| %perf: agencias que gestionan pauta de Meta para pymes | 40% | 50% | 60% | **Sin dato local.** Indirectos: en AR lo social es el 34% de la inversión digital (F25); en UY Meta es el 82% de la inversión en redes (F34). | **Supuesto** |
| Clientes activos por agencia boutique | 8 | 12 | 20 | Global: más de la mitad de las agencias maneja 10–30 clientes (F20, medio); las micro-agencias, hasta 20 en retainer (F21, bajo); ~70% de los account managers tiene menos de 10 (F22). Sin dato AR/UY/PY. | Supuesto anclado en benchmark global |
| %WhatsApp: clientes que venden o califican por WhatsApp con pauta en Meta | 40% | 55% | 70% | 71,5% de los emprendedores de Tiendanube AR vendió por WhatsApp (F45, medio, sesgo pyme digital); 62% de los usuarios AR compró por WhatsApp (F46, medio); WhatsApp es el canal preferido del 42% en UY (F43). **Sin dato de % de anunciantes que usan CTWA.** | Supuesto anclado |
| %CRM+IA: tienen CRM con agente IA o lo adoptarían | 15% | 25% | 35% | AR: 15% usa CRM de forma centralizada (F69, **bajo**, n=21, solo construcción). Meta extendió Business AIs a pymes de LATAM en 2026 (F50). | **Supuesto** |
| Precio a la agencia por cliente | USD 25 | USD 40 | USD 70 | Piso: AgencyAnalytics USD 20/cliente; Reportei ~USD 14–37. Medio: Tintim ~USD 36–55. Techo comparable: CallRail USD 50–195 por negocio (ver `competencia.csv`). Debe caber en el fee de la agencia (§5). | Supuesto anclado |
| Agencias socias a 3 años | 15 | 40 | 80 | Equivale al 1,2% / 1,5% / 1,7% de las agencias de performance de cada escenario. | **Supuesto** |
| Clientes IC por agencia socia | 3 | 5 | 8 | Entre 25% y 40% de la cartera típica de cada escenario. | **Supuesto** |

**Advertencia de método:** los escenarios mueven todos los parámetros a la vez y en la misma dirección. Por eso el optimista es un techo poco probable y no un "caso bueno". Para planificar conviene usar el base y la sensibilidad de §4.3.

---

## 4. Resultados

### 4.1 Por país

| País | Escenario | Agencias perf. | Clientes TAM | TAM USD/año | Clientes SAM | SAM USD/año |
|---|---|---|---|---|---|---|
| AR | Cons. | 859 | 2.749 | 824.832 | 412 | 123.725 |
| AR | Base | 2.070 | 13.665 | 6.559.344 | 3.416 | 1.639.836 |
| AR | Opt. | 3.637 | 50.921 | 42.773.472 | 17.822 | 14.970.715 |
| UY | Cons. | 214 | 685 | 205.440 | 103 | 30.816 |
| UY | Base | 368 | 2.432 | 1.167.408 | 608 | 291.852 |
| UY | Opt. | 442 | 6.191 | 5.200.272 | 2.167 | 1.820.095 |
| PY | Cons. | 131 | 420 | 125.952 | 63 | 18.893 |
| PY | Base | 164 | 1.082 | 519.552 | 271 | 129.888 |
| PY | Opt. | 566 | 7.921 | 6.653.808 | 2.772 | 2.328.833 |
| **Total** | **Cons.** | 1.204 | **3.854** | **1.156.224** | **578** | **173.434** |
| **Total** | **Base** | 2.602 | **17.180** | **8.246.304** | **4.295** | **2.061.576** |
| **Total** | **Opt.** | 4.645 | **65.033** | **54.627.552** | **22.761** | **19.119.643** |

### 4.2 SOM (año 3)

| Escenario | Agencias socias | Clientes IC | Ingreso USD/año | % de clientes SAM |
|---|---|---|---|---|
| Conservador | 15 | 45 | 13.500 | 7,8% |
| Base | 40 | 200 | 96.000 | 4,7% |
| Optimista | 80 | 640 | 537.600 | 2,8% |

En el conservador, el SOM pesa 7,8% del SAM. Eso indica que, con un SAM tan chico, el cuello de botella no es la demanda sino la cantidad de pymes que ya tienen CRM con agente. Esto es una inferencia propia.

### 4.3 Sensibilidad (sobre el escenario base, un parámetro a la vez)

| Cambio | Clientes SAM | SAM USD/año |
|---|---|---|
| Base | 4.295 | 2,06 M |
| Agencias AR = OEDE 2.148 en vez de 4.141 | 2.651 | 1,27 M |
| Clientes por agencia 8 en vez de 12 | 2.863 | 1,37 M |
| %CRM+IA 15% en vez de 25% | 2.577 | 1,24 M |
| Precio USD 25 en vez de 40 | 4.295 | 1,29 M |
| Precio USD 70 en vez de 40 | 4.295 | 3,61 M |

El SAM es igual de sensible a todos los parámetros, porque el modelo es multiplicativo. El dato más barato de mejorar es **%CRM+IA**: se puede medir en la propia base de clientes de Prometheo y en las agencias socias.

### 4.4 Control de cordura (*top-down*, no se suma con el *bottom-up*)

- **Contra el universo de pymes:** los 13.665 clientes del TAM base de Argentina son el 2,5% de las 549.100 pymes empleadoras de Argentina (F71). Es un orden de magnitud razonable para pymes con agencia, pauta en Meta y venta por WhatsApp.
- **Contra la inversión en redes:** el TAM base de Argentina (USD 6,6 M) equivale a ~3% de la inversión en redes sociales que deriva de CAAM (~USD 200–235 M, F26, confianza **baja** por el tipo de cambio supuesto). Contra la estimación de Statista (~USD 500 M, F29), sería ~1,3%. Las dos bases miden cosas distintas (mercado intermediado por agencias frente a todo el gasto, incluido el autoservicio), por eso se informan como rango y no se promedian.

---

## 5. Disposición a pagar

| País | Fee mensual típico de gestión de pauta o redes (sin la pauta) | Fuente |
|---|---|---|
| AR, micro y pequeña pyme (en ARS) | ~USD 78–260 | F53, F54, F56, F57 (medio; DP Renders alto) |
| AR, cuentas más grandes (en USD) | USD 300–1.200 | F55 (medio) |
| UY | USD 100–300 (IdeasWeb); ~USD 400–1.600 en paquetes de campaña (Relevant) | F60, F61 |
| PY | ~USD 69–426 | F62, F63 |
| Fee como % de la pauta (AR) | 10–25%, decreciente con la inversión | F58 |

Tipos de cambio: ARS 1.540, UYU 40,29, PYG 5.873,69 por USD (F74–F76). Los rangos de Argentina en ARS y en USD **no se promedian**: miden segmentos distintos.

**Hallazgos:**

1. **Ninguna lista pública de AR, UY o PY cobra el reporting aparte** (F64). El reporte mensual, la analítica y los tableros vienen incluidos y se usan para justificar el plan superior. Por eso IC no puede venderse como "reporte"; tiene que venderse como algo que la agencia no puede producir hoy: el cruce del anuncio con la venta y el criterio comercial.
2. **Peso del precio sobre el fee:** con un fee típico de USD 80–300 en Argentina, IC a USD 40 representa el 13–50% del fee. Eso solo es viable si:
   - la agencia lo traslada como recargo, en línea con el +40–60% que se cobra por especializarse en Ads/Analytics (F59, bajo-medio); o
   - el cliente lo paga directo, empaquetado con el CRM.

   En micro-pymes que pagan USD 80, el precio de USD 25 (escenario conservador) es el más realista. Esto es una inferencia propia.
3. **Ahorro de tiempo de la agencia:** según la referencia global, el 73% de las agencias tarda menos de 1 hora por reporte (F65). El argumento de "ahorro de horas" es débil. El argumento fuerte es la retención: el 97% dice que reportar bien retiene clientes (F66).
4. **Costo variable de WhatsApp para el cliente:** los mensajes que entran por un anuncio CTWA tienen 72 horas gratis (F52). Fuera de esa ventana, en Argentina el marketing cuesta USD 0,0618 por mensaje y la utilidad o servicio USD 0,026 (F51). Es una referencia para el costo total del stack del cliente; no entra en el precio de IC.

---

## 6. Competencia (resumen; el detalle está en `competencia.csv`)

| Categoría | Ejemplos y precio | ¿Llega a la venta? | ¿Da criterio? | Gap frente a IC |
|---|---|---|---|---|
| Reporting para agencias | AgencyAnalytics USD 20/cliente; DashThis USD 44–429; Swydo USD 62–69; Reportei ~USD 14–37; Whatagraph desde EUR 699 | No | Visualización (algunos agregan resúmenes de IA sobre medios) | No ven la conversación ni la venta |
| Conectores + BI | Looker Studio gratis + Supermetrics USD 44–55, Porter USD 15–180, Windsor USD 19–598 | Solo si se arma a mano | No | Es el sustituto "hazlo tú mismo" de la agencia |
| CRM con reportes nativos | Kommo USD 20–45/usuario (guarda la metadata del anuncio CTWA); HubSpot Pro ~USD 800+/mes; Clientify USD 39–65 | Parcial (Kommo con filtros manuales; HubSpot sí, en Pro) | No | Falta la vista por ad ID y la recomendación |
| Revenue intelligence | Gong (mediana USD 55 mil/año), Clari (USD 76 mil), Salesloft (USD 31 mil): estimaciones de Vendr | Sí | Sí | Llamadas y email, no WhatsApp ni Meta; precio enterprise |
| Atribución por WhatsApp | Tintim ~USD 36–55 (Brasil, descuento para agencias); Respond.io Growth USD 159; Mercately USD 479–999 con CAPI; Wati USD 39–249 | Sí | **No**: devuelven la señal a Meta (CAPI) o muestran un dashboard | **Son los competidores más cercanos.** No hay evidencia de que alguno dé criterio comercial ni califique con un agente propio integrado al tablero |
| Análogo en llamadas | CallRail USD 50–195/mes | Parcial | Insights de IA sobre la conversación | Muestra que el modelo "conversación atribuida + IA" se paga USD 50 o más por negocio en EE.UU. |

**Riesgos competitivos:**

- Tintim ya tiene canal de agencias en Brasil y podría expandirse al Cono Sur.
- Meta podría ampliar sus reportes nativos de CTWA y Business AI (F50).
- Kommo es el CRM de WhatsApp más presente en Argentina y ya guarda la metadata del anuncio. Si agrega una vista por anuncio, cubriría parte del gap.

---

## 7. Contexto de demanda (no entra en el cálculo)

- **Inversión publicitaria digital:**
  - Argentina 2025: ARS 790.290 M, el 46,6% del total; dentro de digital, social es el 34% (F24, F25, alto). En USD, ~585–690 M según CAAM con un tipo de cambio supuesto (F26, bajo), frente a USD 1.880 M según Statista (F28, medio-bajo). La diferencia es de alcance: CAAM proyecta el mercado de medios intermediado por agencias en pesos nominales, mientras que Statista modela todo el gasto, incluido el autoservicio de pymes y lo pagado a plataformas en el exterior.
  - Uruguay: USD ~165 M (derivado de AUDAP, bajo) a >USD 210 M (IAB UY 2023, F33).
  - Paraguay 2025: ~USD 33 M en digital (F37). APAP probablemente subestima el autoservicio en Meta.
- **WhatsApp:**
  - Lo usa el 93–94% de los internautas en Argentina (F41), el 94% de los adultos a diario en Uruguay (F42) y el 97,5% de los internautas en Paraguay (mensajería en general, F44).
  - Los ingresos globales de CTWA crecieron 60% interanual en el 3T 2025 (F49). Meta no publica el desglose por región.
- **Alcance publicitario de Meta (DataReportal 2026):**
  - Argentina: Instagram 31,1 M, Facebook 29,3 M (F30).
  - Uruguay: Instagram 2,50 M (F36).
  - Paraguay: Facebook 3,80 M (F40).

---

## 8. Qué no se pudo verificar

1. **Uruguay, cantidad oficial de agencias:** la tabla del INE (Directorio de Empresas, división 73, 2024) existe pero no se pudo descargar (error 503 y falla de TLS). Es la prioridad para conseguir a mano, porque hoy Uruguay se apoya en bases privadas de confianza baja o media-baja.
2. **Paraguay, cantidad oficial de agencias:** el DIRGE no abre la clase 7310. Hay que pedírsela al INE.
3. **Clientes activos por agencia boutique en AR, UY o PY:** sin dato local. Solo hay benchmarks globales (Databox, Vendasta) y de Brasil (RD Station, que mide captación y no cartera).
4. **Porcentaje de agencias que gestionan pauta de Meta:** sin dato. Es un supuesto.
5. **Porcentaje de pymes con WhatsApp Business, y de anunciantes o inversión en CTWA, por país o en LATAM:** sin dato. Meta solo publica cifras globales o de EE.UU. El dato de 200 M de usuarios de la app WhatsApp Business es de 2023 y no se actualizó (F47).
6. **Adopción de CRM en pymes:** el único dato argentino (15%, F69) tiene n=21 y es solo del sector construcción. Uruguay y Paraguay: sin dato.
7. **Anunciantes activos en Meta por país:** sin dato (Meta no lo publica).
8. **Precio aparte por reporting en AR/UY/PY:** no existe en las listas públicas revisadas. El recargo de +40–60% por especialización es de un solo blog (F59).
9. **Inversión digital de Argentina en USD 2025:** CAAM no publicó el valor en USD y no se verificó el tipo de cambio promedio del BCRA para 2025. El rango F26 es una estimación propia de confianza baja.
10. **Statista y DataReportal (montos de inversión):** se tomaron de citas secundarias (byyd.me), porque las páginas de Statista están detrás de un muro de pago y las diapositivas de DataReportal no se pudieron leer como texto.
11. **Directorios (Clutch, GoodFirms, DesignRush, D&B, Sortlist):** varios conteos salen de snippets de búsqueda porque las páginas bloquean el acceso (403 o protección anti-bot). Los de Clutch son mínimos (solo la primera página).
12. **Socios de las cámaras:** no hay cifras actuales de AAP, Interact, AMDIA, IAB UY/PY, CUAM ni CAPACE. Las de AUDAP (30) y APAP (36) son de 2017.
13. **Competencia:**
    - Precios de Tintim, Porter Metrics, Pipedrive, Zoho, Triple Whale y Blip, y las alternativas de Chatfuel: vienen de terceros, no de la página oficial.
    - Gong, Clari, Salesloft y Chorus no publican precio; las cifras son estimaciones de Vendr.
    - Cliengo, Treble.ai, Hyperflow y Sirena: sin dato.
    - No se verificó si HubSpot, Pipedrive, Zoho, Clientify o Bitrix24 capturan de forma nativa el ad ID de CTWA.
    - Kommo publica dos precios distintos: USD 25/35/45 en la página de precios y USD 20/30 en el blog para clientes nuevos.
    - Las conversiones de BRL a USD usan ~5,4, un tipo de cambio supuesto y no verificado.
14. **URLs de las transcripciones de resultados de Meta** (F48, F49): se armaron siguiendo el patrón del sitio de inversores de Meta. Conviene abrirlas antes de citarlas afuera.
15. **Todos los parámetros marcados como supuesto en §3.2:** son el principal riesgo del modelo. La forma más barata de validarlos es una encuesta corta a 20–30 agencias socias o prospectas (cartera activa, % con pauta CTWA, % con CRM) y la propia base de clientes de Prometheo.


---

# Anexo A. Fuentes (fuentes.csv)

Una fila por dato. Los códigos F01–F76 son los citados en el documento.

| id | dato | valor | unidad | fuente | url | fecha | alcance | confianza |
|---|---|---|---|---|---|---|---|---|
| F01 | AR: empresas empleadoras en Servicios de publicidad (CIIU 7430) | 2148 (2024); 2196 (2023); 2110 (2022) | empresas | OEDE / Ministerio de Trabajo (SIPA) | https://www.argentina.gob.ar/sites/default/files/nacional_serie_empresas_2.xlsx | serie 1996-2024; consultado 2026-10-03 | Empresas con >=1 asalariado registrado. Incluye agencias tradicionales, de medios y digitales sin separarlas. Excluye monotributistas sin empleados | alto |
| F02 | AR: distribución por tamaño de firmas de publicidad (CLAE 731001+731009) | 1-9 empleados: 1650 (83%); 10-49: 271 (14%); 50-199: 57; 200+: 7 (total 1985 CUIT) | CUIT | CEP XXI / Ministerio de Economía (SIPA), cálculo propio sobre CSV | https://cdn.produccion.gob.ar/cdn-cep/establecimientos-productivos/distribucion_establecimientos_productivos_sexo.csv | datos 2022; recurso 2023-12-06 | Mismo universo que F01; tramo de empleo por establecimiento (tamaño de empresa queda como mínimo) | medio-alto |
| F03 | AR: establecimientos de publicidad por provincia | 2394 total; CABA 1380; PBA 383; Córdoba 151; Santa Fe 118; Mendoza 99 | establecimientos | CEP XXI / Ministerio de Economía | https://cdn.produccion.gob.ar/cdn-cep/establecimientos-productivos/distribucion_establecimientos_productivos_sexo.csv | 2022 | Establecimientos (no empresas) de empleadoras | alto |
| F04 | AR: empresas Advertising Services | 6062 | empresas | Coresignal | https://coresignal.com/discover/advertising-services/argentina/ | abr-2025 | Datos web públicos con taxonomía tipo LinkedIn; incluye firmas sin empleados | medio-bajo |
| F05 | UY: empresas Advertising Services | 737 | empresas | Coresignal | https://coresignal.com/discover/advertising-services/uruguay/ | 2025-03-25 | Ídem F04 | medio-bajo |
| F06 | PY: empresas Advertising Services | 328 | empresas | Coresignal | https://coresignal.com/discover/advertising-services/paraguay/ | 2025-03-28 | Ídem F04 | medio-bajo |
| F07 | AR: marketing agencies por tamaño | 4141 (1-10 emp: 3173; 11-50: 847; 51-200: 85; 201-500: 16; 501+: 14) | empresas | RevenueBase | https://revenuebase.ai/companies/marketing-agencies/argentina | refrescado 2026-09-05 | Clasificación por descripción pública (LinkedIn/web); incluye PR, contenido, creatividad | medio-bajo |
| F08 | UY: perfiles NAICS 5418 Advertising, PR & Related | 535 (Montevideo 271) | empresas | Dun & Bradstreet (solo snippet de búsqueda) | https://www.dnb.com/business-directory/company-information.advertising_public_relations_and_related_services.uy.html | 2026 (snippet) | Incluye relaciones públicas; página no abierta | bajo |
| F09 | PY: perfiles NAICS 5418 Advertising, PR & Related | 943 | empresas | Dun & Bradstreet (solo snippet de búsqueda) | https://www.dnb.com/business-directory/company-information.advertising_public_relations_and_related_services.py.html | 2026 (snippet) | Incluye relaciones públicas; página no abierta | bajo |
| F10 | AR: agencias en directorio agencias.marketing | 9280 | perfiles | agencias.marketing | https://agencias.marketing/directorio/argentina | 2026 | Sin metodología; incluye freelancers de 1-2 personas | bajo |
| F11 | AR: agencias Digital Marketing en Clutch | >=50 (primera página; 2-9 emp: 11; 10-49: 23; 50-249: 13) | agencias | Clutch | https://clutch.co/ar/agencies/digital-marketing | 2026-10-03 | Directorio curado de agencias visibles; total no mostrado (mínimo) | bajo (como total) |
| F12 | UY: agencias Digital Marketing en Clutch | ~40-43 (primera página) | agencias | Clutch | https://clutch.co/uy/agencies/digital-marketing | 2026-10-03 | Ídem F11 | bajo |
| F13 | PY: agencias Digital Marketing en Clutch | 35-38 (~2/3 de 2-9 empleados) | agencias | Clutch | https://clutch.co/py/agencies/digital-marketing | 2026-10-03 | Ídem F11; probablemente cercano al total visible del país | medio-bajo |
| F14 | AR / UY: agencias Digital Marketing en GoodFirms | AR 89; UY 15 | agencias | GoodFirms (snippet; sitio devuelve 403) | https://www.goodfirms.co/directory/country/top-digital-marketing-companies/ar | ago/sep-2026 | Directorio curado | medio-bajo |
| F15 | AR: agencias Digital Marketing en DesignRush | 102 | agencias | DesignRush (snippet) | https://www.designrush.com/agency/digital-marketing/ar?page=2 | 2026-04-01 | Directorio curado | medio-bajo |
| F16 | PY: empresas activas sección M (actividades profesionales, científicas y técnicas) | 66791 | empresas con RUC | INE Paraguay, DIRGE 2025 | https://www.ine.gov.py/Publicaciones/Biblioteca/documento/311/DIRGE%20Presentacion.pdf | ref. 2024 | Sección entera (abogados, contadores, etc.); NO mide agencias; solo techo de contexto | alto (dato) / no aplicable |
| F17 | UY: socios AUDAP | 30 agencias | agencias | Revista Mercado | https://mercado.com.ar/marketing/diferentes-paises-mismos-problemas | 2017-09-08 | Agencias de publicidad asociadas (dato viejo) | bajo |
| F18 | PY: socios APAP | 36 | socios | Revista Mercado | https://mercado.com.ar/marketing/diferentes-paises-mismos-problemas | 2017-09-08 | Socios de la asociación (dato viejo) | bajo |
| F19 | AR: agencias socias CAAM | 15 principales agencias de medios | agencias | Infobae | https://www.infobae.com/economia/networking/2024/09/13/la-camara-argentina-de-agencias-de-medios-renovo-su-imagen/ | 2024-09-13 | Solo grandes agencias de medios | medio |
| F20 | Global: clientes simultáneos por agencia | Más de la mitad trabaja con 10-30 clientes; 17,8% con 31-50; <10% con hasta 10 | % de agencias | Databox / ZenPilot (n=241) | https://databox.com/state-of-agency-client-collaboration | act. 2024-02-24 | Global, sin desagregar por país | medio |
| F21 | Global: clientes de micro-agencias (<=10 empleados) | hasta 20 en retainer y hasta 10 por proyecto | clientes | Databox (n=45; 14 micro) | https://databox.com/?p=155379 | 2025-07-10 | Global, muestra chica | bajo |
| F22 | Global: clientes por account manager | ~70% de agencias: <10 clientes por AM | % de agencias | Databox (n=48) | https://databox.com/how-many-accounts | 2025-07-02 | Global, muestra chica | bajo |
| F23 | AR: inversión publicitaria total en medios 2025 | 1.696.545 | millones ARS nominales | CAAM | https://www.totalmedios.com/nota/63261/caam-cuanto-crecio-la-inversion-publicitaria-en-la-argentina-durante-2025 | 2026-03-13 | Proyección de mercado de medios desde agencias socias (~58% del mercado); sin producción | alto |
| F24 | AR: inversión digital 2025 | 790.290 (46,6% del total) | millones ARS nominales | CAAM | https://agenciasdemedios.com.ar/caam-informa-la-inversion-publicitaria-en-medios-de-argentina-en-2025/ | 2026-03-13 | Digital total (social, display, programática, search) | alto |
| F25 | AR: reparto digital 2025 | Social 34%; Display 32%; Programática 19%; Search 15% | % de digital | CAAM | https://www.totalmedios.com/nota/63261/caam-cuanto-crecio-la-inversion-publicitaria-en-la-argentina-durante-2025 | 2026-03-13 | Dentro de inversión digital | alto |
| F26 | AR: inversión digital 2025 en USD (derivado) | 585-690 (social ~200-235) | millones USD | Cálculo propio sobre F24-F25 | — | 2026-10-03 | Supuesto TC promedio 2025 1.150-1.350 ARS/USD sin fuente verificada; CAAM no publicó USD 2025 | bajo |
| F27 | AR: inversión total y digital 2024 | Total 974.085 M ARS (~USD 984 M); digital 423.863 M ARS (~USD 428 M) | millones | CAAM | https://www.totalmedios.com/nota/59609/la-caam-presento-el-reporte-de-inversion-publicitaria-en-medios-al-cierre-de-2024 | 2025-03-27 | TC 989,92 ARS/USD (promedio minorista BCRA 2024 informado por CAAM); USD de digital es cálculo propio con ese TC | alto (ARS) / medio-alto (USD) |
| F28 | AR: inversión digital 2025 según Statista (vía DataReportal) | 1.880 (total publicidad 3.510) | millones USD | byyd.me citando DataReportal/Statista | https://www.byyd.me/en/blog/2026/04/digital-marketing-in-argentina-trends-2026-and-datareportal-statistics/ | 2026-04-15 | Modelo Statista: todo el gasto digital incl. autoservicio pyme y pagos al exterior; año ambiguo | medio-bajo |
| F29 | AR: social media ad spend según Statista (vía DataReportal 2025) | ~500 | millones USD | byyd.me citando DataReportal/Statista | https://www.byyd.me/en/blog/2025/07/argentinas-digital-advertising-key-trends-and-insights-for-2025/ | 2025-07-23 | Modelo Statista | bajo-medio |
| F30 | AR: alcance publicitario Meta | Facebook 29,3 M; Instagram 31,1 M | personas | DataReportal Digital 2026 Argentina | https://datareportal.com/reports/digital-2026-argentina | 2025-11-08 | Audiencia publicitaria declarada por plataforma (no usuarios únicos) | alto |
| F31 | UY: inversión publicitaria 2024 (proyectada) | 412 (2023: 355) | millones USD corrientes | AUDAP / cinve, 13° Estudio | https://audap.com.uy/wp-content/uploads/2025/02/Resumen-Ejecutivo-2024.pdf | dic-2024 | Inversión a lo largo de la cadena (no solo medios); cinve advierte que el real sería menor | medio |
| F32 | UY: internet en inversión en medios de agencias | 40% (2024); redes sociales 46% de digital | % | AUDAP / cinve | https://audap.com.uy/wp-content/uploads/2024/12/4-diciembre-2024.-Presentacion-CINVE-version-final.pdf | dic-2024 | Reparto de lo canalizado por agencias | medio |
| F33 | UY: inversión digital 2023 | > 210 | millones USD | IAB Uruguay + Grupo Radar (vía El Observador) | https://www.elobservador.com.uy/nota/record-se-estima-que-la-inversion-publicitaria-digital-en-uruguay-supero-los-us-210-millones-en-el-2023-20241811122 | 2024-01-08 | Encuesta a 27 empresas | medio |
| F34 | UY: reparto de inversión en redes | Meta 82%; LinkedIn 9%; TikTok 4%; X 4% | % de social | IAB Uruguay / Grupo Radar | https://www.elobservador.com.uy/nota/record-se-estima-que-la-inversion-publicitaria-digital-en-uruguay-supero-los-us-210-millones-en-el-2023-20241811122 | 2024-01-08 | Dentro de inversión en redes | medio |
| F35 | UY: inversión digital y social 2024 (derivado) | digital ~165; social ~76 | millones USD | Cálculo propio sobre F31-F32 | — | 2026-10-03 | Mezcla base 'toda la cadena' con reparto de agencias: solo orden de magnitud | bajo |
| F36 | UY: alcance publicitario Meta | Instagram 2,50 M; Facebook 2,15 M | personas | DataReportal Digital 2026 Uruguay | https://datareportal.com/reports/digital-2026-uruguay | 2025-11-08 | Audiencia publicitaria de plataforma | alto |
| F37 | PY: inversión en medios 2025 (proyectada) | 147 (digital 22,5% = ~33,1) | millones USD | APAP (vía Infonegocios) | https://infonegocios.com.py/nota-principal/publicidad-en-paraguay-la-inversion-superara-los-us-147-millones-este-ano-y-creceria-a-doble-digito-en-2026 | 2025-12-01 | Medios monitoreados (Kantar IBOPE/Audimedia); probablemente subestima autoservicio Meta/Google | medio-alto (total) / medio (digital) |
| F38 | PY: inversión en medios 2024 | 135,5 (digital 22,1% = ~29,9) | millones USD | APAP (vía ABC Color) | https://www.abc.com.py/negocios/2025/10/03/la-industria-de-los-medios-un-mercado-de-us-135-millones/ | 2025-10-03 | Ídem F37 | medio-alto |
| F39 | PY: reparto dentro de online | Redes 61%; programática 18%; Google 11%; sitios locales 9% | % de online | APAP (vía Hoy) | https://www.hoy.com.py/comercio-e-industrias/hubo-menos-publicidad-este-ano-rubros-que-mas-pautaron-fueron-telefonia-electronica-y-bancos | 2022-12-16 | Dato 2022 | medio (bajo como proxy 2025) |
| F40 | PY: alcance publicitario Meta | Facebook 3,80 M; Instagram 2,90 M | personas | DataReportal Digital 2026 Paraguay | https://datareportal.com/reports/digital-2026-paraguay | 2025-11-08 | Audiencia publicitaria de plataforma | alto |
| F41 | AR: usuarios de WhatsApp sobre internautas | 93,3-93,9 | % | Statista con datos DataReportal/Meltwater | https://www.statista.com/statistics/1313074/social-networks-penetration-argentina | 2T 2025; publ. 2026-02-25 | Internautas 16-64 que usan la plataforma mensualmente; inconsistencia interna gráfico/texto | alto (rango) |
| F42 | UY: usan WhatsApp a diario | 94 (99% semanal) | % de adultos | Opción Consultores para DavinciBot (vía El Observador) | https://www.elobservador.com.uy/ciencia-y-tecnologia/whatsapp-desplazo-al-telefono-como-el-canal-que-prefieren-los-uruguayos-hablar-empresas-n6051805 | 2026-07-23 | 400 adultos, encuesta telefónica | medio |
| F43 | UY: WhatsApp canal preferido para hablar con empresas | 42 (75% entre los 2 preferidos) | % de adultos | Opción Consultores (vía El Observador) | https://www.elobservador.com.uy/ciencia-y-tecnologia/whatsapp-desplazo-al-telefono-como-el-canal-que-prefieren-los-uruguayos-hablar-empresas-n6051805 | 2026-07-23 | Salto desde 4% el año anterior: tomar con cautela | medio |
| F44 | PY: internautas que usan mensajería instantánea | 97,5 | % de internautas 10+ | INE Paraguay EPH 2024 (vía ABC Color) | https://www.abc.com.py/economia/2025/06/20/cuantas-personas-usan-internet-en-paraguay-y-para-que-esta-es-la-respuesta-del-ine/ | 2025-06-20 | Mensajería en general, no solo WhatsApp | alto (como proxy) |
| F45 | AR: emprendedores que vendieron por WhatsApp | 71,5 | % de tiendas | Tiendanube, NubeCommerce 2026 | https://www.tiendanube.com/blog/como-vender-por-whatsapp/ | año 2025; act. 2026-07-20 | Solo tiendas Tiendanube (sesgo pyme digital) | medio |
| F46 | AR: usuarios que compraron un producto por WhatsApp | 62 | % de usuarios | Infobip Messaging Trends 2026 (vía Revista Mercado) | https://mercado.com.ar/tendencias/el-informe-de-infobip-describe-a-whatsapp-como-infraestructura-social-en-argentina | 2026-09-04 | Base y muestra no informadas | medio |
| F47 | Global: usuarios mensuales de la app WhatsApp Business | > 200 | millones | Meta (earnings call 2T 2023) / TechCrunch | https://techcrunch.com/2023/06/27/whatsapp-business-crosses-200m-maus-introduces-personlized-messages-feature/ | 2023-06-27 | App gratuita, global; último dato oficial | alto (desactualizado) |
| F48 | Global: run-rate de anuncios click-to-message | 10.000 | millones USD/año | Meta, earnings call 4T 2022 | https://s21.q4cdn.com/399680738/files/doc_financials/2022/q4/META-Q4-2022-Earnings-Call-Transcript.pdf | feb-2023 | Global; WhatsApp + Messenger + IG Direct; no actualizado. URL armada con el patrón del sitio de inversores de Meta (verificar) | alto |
| F49 | Global: crecimiento ingresos CTWA | +60% interanual | % | Meta, earnings call 3T 2025 | https://s21.q4cdn.com/399680738/files/doc_financials/2025/q3/META-Q3-2025-Earnings-Call-Transcript.pdf | oct-2025 | Global; sin desglose regional. URL armada con el patrón del sitio de inversores de Meta (verificar) | alto |
| F50 | Global: empresas que usan Meta Business Agents semanalmente | > 1 | millones de empresas | Meta, earnings call 2T 2026 | https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf | jul-2026 | Global; Business AIs extendidas a pymes de LATAM en 1T 2026 | alto |
| F51 | WhatsApp API: tarifa por mensaje Argentina | Marketing 0,0618; Utilidad/Autenticación/Servicio 0,026 | USD por mensaje | Meta, precios WhatsApp Business Platform | https://developers.facebook.com/docs/whatsapp/pricing | vigente desde 2026-10-01 | Mercado Argentina | alto |
| F52 | WhatsApp API: tarifa por mensaje Rest of Latin America (UY, PY) | Marketing 0,074; Utilidad/Autenticación/Servicio 0,0113 | USD por mensaje | Meta, precios WhatsApp Business Platform | https://developers.facebook.com/docs/whatsapp/pricing | vigente desde 2026-10-01 | UY (+598) y PY (+595) en Rest of LATAM; ventana gratuita 72 h al entrar por anuncio CTWA | alto |
| F53 | AR: fee de gestión Meta Ads (sin pauta) | 120.000-350.000 ARS (~USD 78-227) | ARS/mes | pointweb (guía de agencia) | https://pointweb.com.ar/guias/cuanto-cobra-una-agencia-de-marketing-digital/ | ago-2026 | Estimación de mercado de una agencia | medio |
| F54 | AR: fee de gestión Meta/Google Ads (sin pauta) | 150.000-400.000 ARS (~USD 97-260) | ARS/mes | FINMI (blog) | https://finmi.com.ar/blog/cuanto-cuesta-agencia-marketing-digital-argentina | 2026-06-02 (mod. 2026-08-12) | Estimación de mercado | medio |
| F55 | AR: fee de gestión Meta Ads cotizado en USD | 300-1.200 | USD/mes | Mind Circus (blog) | https://mindcircus.agency/blog/cuanto-cuesta-agencia-marketing-argentina | 2026-08-21 | Por cuenta, sin pauta; segmento de cuentas más grandes | medio |
| F56 | AR: lista de precios pública de agencia (CM) | 120k / 250k / 450k ARS (~USD 78 / 162 / 292) | ARS/mes | DP Renders | https://www.dprenders.com/community-manager/ | 2026 | Reporte mensual incluido en plan Inicial; Premium suma campañas pagas y reportes ejecutivos | alto |
| F57 | AR: planes de agencia redes + Meta | Inicial 200-350k; PyME 350-450k; Empresa 450k-1M+ ARS | ARS/mes | agenciadigital.com.ar, Tarifario 2026 | https://agenciadigital.com.ar/tarifario-marketing-digital-argentina/ | 2026 | Analítica y tableros incluidos sin precio aparte | medio |
| F58 | AR: fee como % de la pauta | 15-25% (20-30% si pauta <USD 5k; 10-15% si >USD 50k) | % de inversión en medios | pointweb / FINMI / Mind Circus (10-20%) | https://pointweb.com.ar/guias/cuanto-cobra-una-agencia-de-marketing-digital/ | 2026 | Alternativa al fee fijo | medio |
| F59 | AR: recargo por especialización Ads/Analytics | +40-60% sobre tarifa base | % | Aprender21, Tarifario CM 2026 | https://www.aprender21.com.ar/blog/tarifario-community-manager-argentina | mar-2026 | Freelance AR | bajo-medio |
| F60 | UY: lista de precios gestión Meta Ads | 100 / 200 / 300 (sin IVA) | USD por 30 días | IdeasWeb | https://www.ideasweb.uy/publicidad-facebook | sin fecha | 1-2 anuncios; no queda claro si incluye pauta | medio-alto |
| F61 | UY: campañas de marketing digital (agencia) | pequeñas ~16.000 UYU (~USD 397); ambiciosas 32-64k UYU (~USD 794-1.588) | UYU/mes | Relevant MKT | https://relevantmkt.com/marketing-digital-uruguay/ | 2026-07-27 | Paquete con reporte mensual incluido | medio |
| F62 | PY: lista de precios gestión de redes | 880.000 / 1.250.000 / 2.500.000 PYG (~USD 150 / 213 / 426) | PYG/mes | Setik | http://www.setik.com.py/web/social-media-management.php | sin fecha | Solo publicaciones, sin pauta ni reportes | medio-alto |
| F63 | PY: lista de precios redes | 69 / 129 / 199 (A3 incluye Ads y reportes) | USD/mes | DreamDare Studio PY | https://dreamdarestudio.com/py/marketing-publicidad-redes-sociales/ | 2025 | Paquete cerrado | medio |
| F64 | AR/UY/PY: precio separado por reporting en listas públicas | sin dato (siempre incluido en el paquete) | — | Revisión de F56, F57, F60-F63 | — | 2026 | Ausencia de precio aparte en todas las listas revisadas | alto (como ausencia) |
| F65 | Global: tiempo por reporte de cliente | 46% <30 min; 73% <1 h | % de agencias | AgencyAnalytics Benchmarks 2026 (n=494) | https://agencyanalytics.com/agency-benchmarks-2026 | 2026 | Clientes de una herramienta de automatización: probablemente subestima | medio |
| F66 | Global: frecuencia y formato de reporte | 69% mensual; 27% de clientes prefiere dashboard en vivo; 97% dice que reportar bien retiene clientes | % | AgencyAnalytics Benchmarks 2026 | https://agencyanalytics.com/agency-benchmarks-2026 | 2026 | Global | medio |
| F67 | Global: precio sugerido de reporting as a service | 50-75 / 100-150 / 200+ | USD/mes por cliente | DashboardFox (blog) | https://dashboardfox.com/blog/agency-client-reporting-revenue/ | 2026-04-05 | Recomendación del proveedor, no precio observado | bajo-medio |
| F68 | AR: pymes que pagan >=1 tecnología digital | 77,5% (e-commerce/marketing digital 28,6%) | % de empresas | Encuesta nadIA (CEPE Di Tella + Fundar, FOP, BID) | https://nadia.ar/extras/nadia_encuesta_pymesARG2026.pdf | abr-2026 (campo nov-dic 2025) | n=402; solo manufactura y software, 10-249 ocupados | alto (para ese universo) |
| F69 | AR: uso centralizado de CRM en pymes | 15% (26% Excel y mail) | % de empresas | FDS Comunicación, Monitor CRM | https://www.fdscomunicacion.com/Monitor%20Septiembre%20uso%20de%20CRM%20en%20PYMEs%20Argentinas.pdf | ago-2025 | 21 respuestas, sector construcción | bajo |
| F70 | Kommo: precio de lista nuevos clientes | Básico 20 / Avanzado 30 | USD por usuario/mes | Kommo, blog oficial | https://www.kommo.com/es/blog/actualizacion-precios-kommo/ | publ. 2026-07-30; vigente 2026-09-01 | Global (difiere de la página de precios: ver competencia.csv) | alto |
| F71 | AR: pymes empleadoras | 549.100 (micro ~468k; pequeñas 67,7k; medianas 13,6k) | empresas | Ministerio de Economía / SEPyME, Informe 2023 | https://argentina.gob.ar/sites/default/files/informe_2023_nov_2024.pdf | stock 2023, publ. nov-2024 | Empresas con empleo registrado, <200 ocupados | alto |
| F72 | UY: mipymes | ~213.800 (micro 186k; pequeñas 22,6k; medianas 5,2k) | empresas | INE Uruguay (vía La Mañana) / nota INE | https://www.gub.uy/instituto-nacional-estadistica/comunicacion/noticias/empresas-mpymes | datos 2023; publ. 2024 | Industria, comercio y servicios | medio-alto |
| F73 | PY: mipymes en base MIC | 450.167 (micro 396k; pequeñas 43,2k; medianas 10,5k) | unidades | MIC / Viceministerio de Mipymes (vía ABC) | https://www.abc.com.py/economia/2025/03/15/cuantas-mipymes-hay-en-paraguay-y-a-que-se-dedican-mic-actualizo-base-de-datos/ | 31-12-2023; publ. 2025-03-15 | Unidades formalizadas en base del MIC | medio-alto |
| F74 | Tipo de cambio ARS/USD (BNA venta) | 1.540 (MEP 1.550) | ARS/USD | Ámbito | https://www.ambito.com/finanzas/dolar-hoy-cuanto-cerro-este-viernes-2-octubre-n6329530 | 2026-10-02 | Usado para convertir fees 2026 | alto |
| F75 | Tipo de cambio UYU/USD (interbancario) | 40,29 | UYU/USD | Infobae (BEVSA) | https://www.infobae.com/noticias/2026/10/01/dolar-hoy-en-uruguay-cotizacion-de-cierre-del-1-de-octubre/ | 2026-10-01 | Usado para convertir fees UY | alto |
| F76 | Tipo de cambio PYG/USD (referencial BCP) | 5.873,69 | PYG/USD | Banco Central del Paraguay | https://www.bcp.gov.py/webapps/web/cotizacion/monedas | 2026-10-02 | Usado para convertir fees PY | alto |

---

# Anexo B. Competencia y sustitutos (competencia.csv)

Precios consultados el 2026-10-03.

| jugador | categoria | precio | url_precio | fecha_consulta | que_mide | llega_a_la_venta | criterio_o_visualizacion | gap_vs_IC | confianza_precio |
|---|---|---|---|---|---|---|---|---|---|
| AgencyAnalytics | Reporting para agencias | USD 20/cliente/mes (Core; -20% anual) | https://agencyanalytics.com/pricing | 2026-10-03 | Métricas de 85+ integraciones de medios, SEO y analítica | No | Visualización + insights/alertas de IA sobre medios | No ve WhatsApp ni CRM conversacional; su insight es de medios, no comercial | alto (visto) |
| DashThis | Reporting para agencias | USD 44 (3 dashboards) / 139 (10) / 279 (25) / 429 (50) por mes, anual | https://dashthis.com/pricing/ | 2026-10-03 | Dashboards de medios | No | Solo visualización | Sin WhatsApp, sin venta, sin criterio | alto (visto) |
| Whatagraph | Reporting para agencias | Desde EUR 699/mes anual (Max); Prime custom | https://whatagraph.com/pricing | 2026-10-03 | Medios y data warehouse | No | Visualización + resúmenes IA | Caro para pymes de la región; sin WhatsApp ni venta | alto (visto) |
| Swydo | Reporting para agencias | USD/EUR 69/mes mensual o 62 anual (10 fuentes; +4,50 por fuente) | https://www.swydo.com/pricing/ | 2026-10-03 | Medios (38+ integraciones) | No | Visualización + AI reporting | Sin WhatsApp ni venta | alto (visto) |
| Reportei (BR) | Reporting para agencias | R$74,90 / 109,90 / 199,90 por mes (~USD 14 / 20 / 37; TC 5,4 supuesto) | https://reportei.com/planos-e-precos | 2026-10-03 | 20+ integraciones (Meta, GA, HubSpot, Pipedrive) | No (trae CRM pero no la conversación) | Visualización | Ancla de precio muy baja en LATAM; sin WhatsApp | alto (visto, BRL) |
| mLabs (BR) | Gestión de redes + reportes | Desde R$29,90/mes por marca (~USD 5,5), según blog mLabs | https://www.mlabs.com.br/planos | 2026-10-03 | Posts y reportes orgánicos y de ads | No | Visualización | Herramienta de community management | medio (fuente 3ra) |
| Looker Studio | BI gratuito | Gratis (Pro ~USD 9/usuario/mes, snippet) | https://cloud.google.com/looker-studio | 2026-10-03 | Lo que se le conecte | Solo si se arma a mano el cruce con el CRM | Visualización | Sustituto hazlo-tú-mismo; requiere construir la lógica ad ID-conversación-venta | alto (gratis) / medio (Pro) |
| Supermetrics | Conector de datos | USD 55 mensual / 44 anual (Starter); 222/177 (Growth) | https://supermetrics.com/pricing | 2026-10-03 | Extrae datos de medios a Looker/Sheets/BI | No | Ninguno (tubería de datos) | Insumo, no competidor directo | alto (visto) |
| Porter Metrics (CO) | Conector de datos | USD 15 (1 conexión) / 39,99 (2-5) / 99,99 (13-20) / 180 (21-40) | https://help.portermetrics.com/en/articles/169-how-porter-metrics-pricing-model-works | 2026-10-03 | Medios a Looker/Sheets | No | Ninguno | Insumo | medio (fuente 3ra / ayuda) |
| Windsor.ai | Conector de datos | USD 23/19 (Basic) a 598/499 (Professional), mensual/anual | https://windsor.ai/pricing/ | 2026-10-03 | Medios a destino | No | Ninguno (MCP para análisis con IA) | Insumo | alto (visto) |
| Coupler.io | Conector de datos | USD 32/24 (Starter) a 259/199 (Pro) | https://www.coupler.io/pricing | 2026-10-03 | 400+ fuentes a Sheets/BI | No | Ninguno | Insumo | alto (visto) |
| Kommo | CRM de WhatsApp | USD 25 / 35 / 45 por usuario/mes (mín. 6 meses) en página de precios; blog oficial anuncia 20 / 30 para nuevos desde 2026-09-01 | https://www.kommo.com/pricing/ | 2026-10-03 | Guarda UTM y metadata del anuncio CTWA en la ficha del lead; integración CAPI | Parcial: cruza anuncio con etapa y venta, pero filtrando a mano | Visualización y filtros | Sin ROAS por ad ID ni criterio de qué anuncio trae calidad y por qué. Sustituto más cercano en AR | alto (visto; dos precios publicados distintos) |
| HubSpot | CRM + marketing | Marketing Hub Starter USD 7-20/asiento; Professional ~USD 800-890/mes (3 asientos) + USD 3.000 onboarding; Sales Pro USD 90-100/asiento | https://www.hubspot.com/pricing/marketing | 2026-10-03 | Atribución de ads a negocios cerrados (Pro); WhatsApp vía inbox o integraciones (ej. Wati) | Sí en Pro | Reportes de atribución, sin criterio sobre la conversación | Prohibitivo para pymes de la región; captura nativa del ad ID CTWA no verificada | alto (visto) |
| Pipedrive | CRM | USD 14-69/asiento anual; 19-89 mensual | https://www.pipedrive.com/en/pricing | 2026-10-03 | Embudo de ventas | No para ad ID CTWA (sin evidencia) | Visualización | Sin capa anuncio-conversación | medio (fuente 3ra; página 403) |
| Zoho CRM | CRM | USD 14 / 23 / 40 / 52 por usuario/mes anual | https://www.zoho.com/crm/zohocrm-pricing.html | 2026-10-03 | Embudo + IA Zia | No evidenciado | Predicciones genéricas | Sin cruce con anuncios CTWA | medio (fuente 3ra) |
| Clientify | CRM marketing y ventas | USD/EUR 39/mes anual o 65 mensual | https://clientify.com/precios | 2026-10-03 | CRM, WhatsApp multiusuario, landings | Parcial (sin evidencia de ad ID) | Visualización | Sin atribución por anuncio ni criterio | alto (visto) |
| RD Station CRM (BR) | CRM | R$73 / 131 por usuario/mes (~USD 13,5 / 24); Pro mín. 4 usuarios | https://www.rdstation.com/planos/crm/ | 2026-10-03 | CRM + extensión WhatsApp Web + tareas sugeridas por IA | Parcial (venta sí, ad ID no evidenciado) | Sugerencias de tareas, no de anuncios | Sin cruce de anuncio | alto (visto, BRL) |
| Bitrix24 | Suite CRM | USD 69/49 (Basic, 5 usuarios) a 289/199 (Professional), mensual/anual por organización | https://www.bitrix24.com/prices/ | 2026-10-03 | CRM, canal abierto | No evidenciado | Visualización | Sin cruce de anuncio | alto (visto) |
| Gong | Revenue intelligence | No público; mediana USD 55.346/año (Vendr) | https://www.vendr.com/marketplace/gong | 2026-10-03 | Llamadas, email, deals | Sí (pipeline) | Sí (coaching, forecast) | Sin WhatsApp ni anuncio Meta; enterprise EE.UU. | bajo-medio (estimación 3ra) |
| Clari | Revenue intelligence | No público; mediana USD 76.000/año (rango 19.065-415.001, Vendr) | https://www.vendr.com/marketplace/clari | 2026-10-03 | Forecast, pipeline | Sí | Sí | Ídem Gong | bajo-medio (estimación 3ra) |
| Salesloft | Revenue/conversation intelligence | No público; mediana USD 30.740/año (Vendr) | https://www.vendr.com/marketplace/salesloft | 2026-10-03 | Cadencias, conversaciones | Sí | Sí | Ídem Gong | bajo |
| Chorus (ZoomInfo) | Conversation intelligence | No público; sin dato propio (ZoomInfo mediana USD 33.500/año) | https://www.vendr.com/marketplace/zoominfo | 2026-10-03 | Llamadas | Sí | Sí | Ídem Gong | bajo |
| Tintim (BR) | Atribución de ventas por WhatsApp | R$197-297/mes (~USD 36-55); descuento para agencias 'desde 65% off' | https://chatfuel.com/blog/chatfuel-vs-tintim | 2026-10-03 | Lee chats, detecta venta (frase gatillo, kanban o IA con aprobación humana) y la envía a Meta por CAPI | Sí (solo texto) | No: envía señal a Meta, sin recomendación | Competidor más directo en 'llega a la venta' y con canal de agencias; no califica con agente ni recomienda; no visto operando en AR/UY/PY | medio (fuente 3ra interesada) |
| Respond.io | Inbox WhatsApp con IA | USD 79 (Starter, sin ads) / 159 (Growth, Meta y TikTok Ads + agentes IA) / 279 (Advanced) | https://respond.io/pricing | 2026-10-03 | Captura ctwa_clid y envía eventos CAPI de lead/compra por workflow | Sí (si se configura evento de compra) | Agente IA para atender; sin criterio sobre anuncios | Optimiza Meta, no le explica a dueño/agencia qué anuncio vende y por qué | alto (visto) |
| Wati | WhatsApp API | USD 49/39 (Growth) / 99/79 (Pro) / 249/199 (Business); agente IA add-on | https://www.wati.io/pricing/ | 2026-10-03 | Atribución CTWA en todos los planes; sync con HubSpot | Parcial/sí vía HubSpot | No | Sin criterio comercial | alto (visto) |
| Mercately (EC, LATAM) | CRM WhatsApp con IA | USD 299/239 (Scale IA) / 599/479 (Rocket IA) / 999/799 (Atlas IA); setup agente USD 999 | https://www.mercately.com/precios | 2026-10-03 | CRM + agente IA + Performance Hub con Meta CAPI (Rocket y Atlas) | Sí (Rocket+) | Dashboard de optimización; sin evidencia de recomendación comercial | Competidor regional más parecido en propuesta; caro (USD 479+ para CAPI); vende directo, no vía agencias | alto (visto) |
| Leadsales (MX) | CRM WhatsApp | USD 97 / 133 / 247 por mes; Lead Agent IA 87 / 297 / 793 | https://www.leadsales.io/precios | 2026-10-03 | Embudos, agente IA, CTWA | Parcial | Calificación IA sí; recomendación de anuncios no evidenciada | Sin capa de criterio anuncio-venta | alto (visto) |
| Botmaker (AR) | Bots y WhatsApp | USD 149 / 249 / 499 por mes; setup WhatsApp USD 99 | https://botmaker.com/es/precios/ | 2026-10-03 | Bots, agentes IA, conversaciones | No evidenciado | No | Sin cruce anuncio-venta | alto (visto) |
| B2Chat (CO) | Inbox WhatsApp | USD 105/84 (Básico con WhatsApp) / 187 (Premium); IA add-on ~USD 80-86 | https://www.b2chat.io/precios/ | 2026-10-03 | Inbox | No | No | Sin atribución | alto (visto) |
| Whaticket | Inbox WhatsApp | USD 49 (Básico, mín. 3 usuarios) / 109 (Pro) | https://whaticket.com/precios/ | 2026-10-03 | Inbox | No | No | Sin atribución | alto (visto) |
| Callbell | Inbox | EUR 15-20 por usuario/mes | https://callbell.eu/en/pricing/ | 2026-10-03 | Inbox | No | No | Sin atribución | alto (visto) |
| Zenvia (BR) | Customer cloud | R$600 / 1.800 / 3.900 por mes (~USD 111 / 333 / 722) | https://www.zenvia.com/precos/ | 2026-10-03 | Omnicanal, bots IA | No evidenciado | No | Sin atribución | alto (visto, BRL) |
| Blip Go! (BR) | WhatsApp para pymes | R$179,90 / 239,90 / 399,90 por mes | https://tiinside.com.br/10/08/2026/claro-empresas-e-blip-lancam-parceria-com-foco-em-pmes-pelo-whatsapp/ | 2026-10-03 | Atención, CRM kanban, agente IA | No evidenciado | No | Sin atribución | medio (fuente 3ra) |
| Chatfuel / Metrito / Chatlabs | Envío CAPI desde WhatsApp | Chatfuel USD 99; Metrito ~48; Chatlabs ~86 por mes | https://chatfuel.com/blog/tintim-alternatives | 2026-10-03 | Eventos CAPI desde WhatsApp | Sí/parcial | No | Señal para Meta, no criterio | bajo-medio (fuente interesada) |
| Cometly | Atribución de ads | No público (cotización) | https://www.cometly.com/pricing | 2026-10-03 | Atribución web y CRM | Sí (web) | No | No menciona WhatsApp | — |
| Hyros | Atribución de ads | No público; 'desde USD 69' (tercero) | https://costbench.com/software/marketing-attribution/hyros/ | 2026-10-03 | Llamadas y web | Sí | No | Sin WhatsApp | bajo |
| Triple Whale | Atribución ecommerce | Desde USD 219/mes (Foundation), 749 (Automate), compromiso 12 meses | https://venon.io/blog/triple-whale-pricing | 2026-10-03 | Ecommerce Shopify | Sí (ecommerce) | IA Moby | No sirve para venta conversacional | medio (fuente 3ra) |
| Ruler Analytics | Atribución multi-touch | USD 400/360 (Small) a 2.000/1.800 (Advanced) | https://www.ruleranalytics.com/pricing/ | 2026-10-03 | Formularios, llamadas, chat hacia CRM | Sí | No | Sin WhatsApp; caro | alto (visto) |
| CallRail | Call tracking (análogo en llamadas) | USD 50 / 95 / 150 / 195 por mes | https://www.callrail.com/pricing | 2026-10-03 | Llamada atribuida a campaña + transcripción, resumen y sentimiento IA | Parcial (etiqueta conversiones) | Insights de conversación con IA | Modelo de IC aplicado a llamadas en EE.UU.; referencia de precio por negocio | alto (visto) |
| Cliengo / Treble.ai / Hyperflow / Sirena | WhatsApp / chatbots LATAM | sin dato (404, protegido o no encontrado) | — | 2026-10-03 | — | sin dato | sin dato | No evaluable | — |
