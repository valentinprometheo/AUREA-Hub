---
name: aurea-email-prometheo
description: >-
  Métricas y lectura de campañas de email marketing cuando el email es canal de
  generación de demanda que desemboca en Prometheo. Usala al diseñar o reportar
  una campaña de email (reactivación, novedad de catálogo, lanzamiento), al armar
  la pestaña de Email Marketing de un tablero de Inteligencia Comercial, o al
  cruzar métricas de plataforma de envío con la conversación que sigue en el CRM.
  Activar ante "campaña de mail", "email marketing", "reactivación", "base
  dormida", "tasa de apertura", "rebote", "el mail cruzado con Prometheo",
  "de qué envío vino este lead".
---

# Email × Prometheo: medir una campaña que termina en una conversación

La mayoría de las métricas de email terminan en el clic. Acá no. En el modelo de
AUREA el email **genera demanda** y la conversación sigue adentro de Prometheo,
donde un agente de IA responde el mail, califica y deriva. Eso cambia qué hay que
medir: el clic deja de ser el final y pasa a ser **el empalme**.

Esta skill define las métricas de las dos mitades, el empalme entre ellas, y cómo
se muestra sin repetir información.

## Relación con otras skills

- `emails` (vendorizada, MIT) manda en **diseño de secuencia**: cuántos mails, con
  qué espaciado, qué asunto, la plantilla de re-engagement. No la reescribas acá.
- `aurea-curaduria-dato` manda en **qué número se puede afirmar**. Todo lo de base,
  cobertura, origen y confianza rige igual acá. Esta skill no la reemplaza: la
  instancia para email.
- `aurea-dashboard-design` manda en **cómo se ve**.
- `aurea-metodologia` manda en cómo se configura Prometheo para recibir el traspaso.

---

## 1. Las dos mitades y el empalme

```
PLATAFORMA DE ENVÍO          EMPALME              PROMETHEO
enviados                       clic         →     contacto creado
entregados                  (o respuesta)         mensajes del agente
aperturas                                         variables extraídas
clics                                             calificación
rebotes / bajas                                   derivación a humano
```

**Regla de fuentes (heredada de `aurea-curaduria-dato`):** cada mitad manda en lo
suyo y no opina de la otra.

| Fuente | Manda en | No manda en |
|---|---|---|
| Plataforma de envío | Enviados, entregados, aperturas, clics, rebotes, bajas | Si el lead sirve |
| Prometheo | Contactos creados, conversación, calificación, derivación | Cuántos mails salieron |
| Cálculo | Ratios de empalme y de embudo | Nada primario |

**Nunca sumes las dos mitades.** Un clic que se convirtió en contacto es **un**
evento con dos registros, no dos eventos. El conteo maestro de demanda lo define
Prometheo, igual que con la pauta.

---

## 2. Las métricas, con su denominador correcto

El error más común de los reportes de email es mostrar todo sobre "enviados". La
apertura no se calcula sobre enviados: se calcula sobre entregados.

| Métrica | Fórmula | Denominador |
|---|---|---|
| Tasa de entrega | entregados / enviados | enviados |
| Tasa de apertura | aperturas únicas / **entregados** | entregados |
| Tasa de clic (CTR) | clics únicos / **entregados** | entregados |
| **Clic sobre apertura (CTOR)** | clics únicos / **aperturas** | aperturas |
| Tasa de rebote | rebotes / enviados | enviados |
| Tasa de baja | bajas / entregados | entregados |
| **Tasa de empalme** | contactos creados en Prometheo / clics | clics |
| Tasa de respuesta al agente | respondieron / contactos creados | contactos creados |
| Tasa de calificación | calificados / contactos creados | contactos creados |

**El CTOR es la métrica que más se subusa y la que más dice.** Separa dos
problemas que la tasa de clic mezcla:

- Apertura baja + CTOR alto → el problema es el **asunto o la entregabilidad**. El
  contenido funciona, no lo toca nadie.
- Apertura alta + CTOR bajo → el problema es la **oferta o el contenido**. El
  asunto prometió algo que el cuerpo no cumplió.

Siempre reportar los dos juntos. Uno solo no permite decidir qué corregir.

### La apertura está inflada y hay que decirlo

Desde Apple Mail Privacy Protection, una parte de las aperturas las dispara el
proxy de Apple sin que nadie haya leído el mail. **La apertura es Señal, no Hecho**,
en el sentido de `aurea-curaduria-dato`: sirve para comparar envíos entre sí, no
para afirmar cuánta gente leyó. El clic sí es una acción humana.

**Consecuencia práctica:** nunca titular una card con la tasa de apertura. El
titular es el clic o lo que pasó después.

---

## 3. Benchmarks: no mezclar frío con lista propia

Es el error que arruina la lectura de una campaña de reactivación.

| | Lista fría (prospección) | Lista propia dormida (reactivación) |
|---|---|---|
| Relación previa | Ninguna | Ya compraron o se registraron |
| Apertura esperada | Baja | Bastante más alta: conocen el remitente |
| Qué significa no abrir | No le interesó | Puede ser dirección muerta o desinterés real |
| Métrica que importa | Respuesta | **Reactivación**: volvió a operar |
| Riesgo principal | Spam | Quemar una base que todavía vale |

Los benchmarks de `cold-email` del repo vendorizado (apertura 27,7%, respuesta
4 a 5,8%) son **de frío**. Aplicarlos a una base propia hace parecer excelente lo
mediocre. Si no hay benchmark propio todavía, **la comparación honesta es contra
el envío anterior de la misma base**, no contra un número de la industria.

**Regla:** el primer envío a una base no tiene benchmark. Se declara como línea
de base y se dice que lo es.

---

## 4. La reactivación se mide por reactivación, no por apertura

En una campaña de win-back a una base dormida, el éxito no es que abran. El éxito
es que **vuelvan a operar**. La escalera de compromiso, de más débil a más fuerte:

1. Entregó (la dirección vive)
2. Abrió (señal débil, inflada por proxies)
3. Clicó (acción humana, señal real)
4. **Contestó al agente** (volvió a conversar: acá empieza el valor)
5. Dejó una variable comercial (qué producto, qué volumen, qué plazo)
6. Calificó
7. Volvió a operar

El KPI titular de una reactivación es el escalón 4 o superior, nunca el 2.

**Corolario para el reporte:** el faltante importa. De 200 dormidos, si 40
contestaron, hay 160 que siguen dormidos y eso es un hallazgo con nombre, no un
hueco. Se dibuja, igual que el "sin anuncio identificado" de la pauta.

---

## 5. El empalme: la métrica propia de AUREA

Es lo que ninguna plataforma de email mide, porque termina en el clic.

> **Tasa de empalme = contactos creados en Prometheo / clics únicos.**

Qué lee:

- **Empalme alto** → el traspaso funciona. El que clicó terminó conversando.
- **Empalme bajo con CTR normal** → hay fuga entre el clic y el CRM. Puede ser el
  destino del clic (una landing que no abre conversación), una desconexión de la
  integración, o que el contacto ya existía y no se contó como nuevo.

**Ojo con el doble conteo del contacto existente.** En una reactivación de base
propia, el contacto **ya está** en el CRM. Lo que se cuenta no es "contacto
creado" sino **"contacto reactivado"**: un contacto con actividad nueva atribuible
a la campaña. Definirlo explícitamente en el tablero, o el número no se entiende.

**Atribución al envío.** Cada mail lleva su identificador de campaña y de envío en
el enlace, y Prometheo lo guarda igual que guarda el ID de anuncio de Meta. Sin
eso, la pestaña de email es un reporte de plataforma pegado al lado del CRM, no un
cruce. **El identificador de envío es a email lo que el ID de anuncio es a Meta.**

---

## 6. Qué mide cada mitad, y qué no se puede medir

Declararlo evita prometer lo que no hay.

**Se puede con la plataforma de envío sola:** entrega, apertura, clic, CTOR,
rebote duro y blando, baja, y el ranking de asuntos entre envíos.

**Se puede recién con el cruce:** calidad por envío (de este mail, cuántos
conversaron y cuántos calificaron), qué segmento reactiva mejor, qué producto
pidieron los que volvieron, y el costo por reactivación si hay costo de envío.

**No se puede sin cerrar el ciclo:** ingreso atribuido al envío, si el
distribuidor reactivado volvió a comprar de verdad. Eso depende de que se registre
la operación, no del email.

---

## 7. Cómo se muestra en la pestaña (liga con `aurea-dashboard-design`)

**Principio rector: economía de repetición.** Si un número ya se muestra arriba en
una card de insight, abajo no se repite: abajo se despliega su detalle. La pestaña
se lee de arriba abajo en tres alturas, cada una más profunda.

1. **Cards de insight cruzado.** Lo que solo se puede decir teniendo las dos
   fuentes. Cada card lleva **ícono de procedencia**: un ícono para el dato de
   email, otro para el de Prometheo, y los dos juntos cuando es cruce. La
   procedencia es información, no decoración: el cliente tiene que ver de un
   vistazo qué está viendo.
2. **Métricas desplegables (cruzadas).** Filas colapsadas que se abren para mostrar
   el detalle del embudo completo, envío por envío o segmento por segmento. Es
   donde vive el cruce fino, sin ocupar pantalla.
3. **Solo email, abajo.** Lo puramente de plataforma (entrega, rebote, baja,
   ranking de asuntos). Va último porque es lo menos accionable para el cliente y
   lo más operativo para nosotros.

Reglas que se mantienen del sistema:
- Toda card declara su base (`base: 200 dormidos`, `base: 186 entregados`).
- La apertura nunca titula.
- El embudo de email se dibuja como pasos con la tasa entre pasos como cifra
  protagonista, nunca como barras proporcionales: de 700 enviados a 12 calificados
  hay dos órdenes de magnitud.
- Si la campaña es simulada o proyectada, se dice **en el mismo bloque**, no en una
  nota al pie.

---

## 8. Checklist antes de publicar una pestaña de email

- [ ] ¿Cada tasa está sobre su denominador correcto? (apertura sobre entregados, no sobre enviados)
- [ ] ¿Está el CTOR además del CTR?
- [ ] ¿La apertura está marcada como señal inflada y no está titulando?
- [ ] ¿El benchmark es contra lista propia, o se declara que es línea de base?
- [ ] ¿La tasa de empalme está y está definida?
- [ ] ¿Se distingue contacto nuevo de contacto reactivado?
- [ ] ¿Los que no volvieron están dibujados como hallazgo?
- [ ] ¿Cada card dice de qué fuente sale, con ícono?
- [ ] ¿Algún número está repetido entre las tres alturas? (debe ser no)
- [ ] ¿Si es simulada, lo dice en el mismo bloque?

## 9. Anti-patrones

- **Apertura sobre enviados.** Infla todo y hace incomparables dos envíos con
  distinta tasa de rebote.
- **La apertura como KPI de la campaña.** Mide el asunto, no el resultado.
- **Benchmark de frío sobre lista propia.** Hace pasar por bueno un envío flojo.
- **Sumar plataforma y CRM.** 40 clics y 35 contactos no son 75 eventos.
- **La pestaña partida en dos reportes** que no se cruzan nunca. Si el email y
  Prometheo no se tocan en ninguna cifra, no hay canal integrado: hay dos anexos.
- **Repetir el mismo número en las tres alturas** en vez de profundizarlo.
- **Contar como "nuevo contacto" a alguien que ya estaba en la base.**

---

## Derivación

Escritura propia de AUREA. Toma de `emails` (Corey Haines, MIT) la doctrina de
secuencia y la plantilla de re-engagement; de `cold-email` la advertencia sobre
benchmarks; de `aurea-curaduria-dato` las reglas de base, cobertura y fuentes.
Lo propio: la escalera de compromiso de reactivación, la tasa de empalme, la
distinción contacto nuevo vs reactivado, y las tres alturas de la pestaña.
