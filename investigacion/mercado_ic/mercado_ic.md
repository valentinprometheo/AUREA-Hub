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
