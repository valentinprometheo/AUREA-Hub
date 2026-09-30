---
name: aurea-whatsapp-prometheo
description: >-
  Métricas, segmentación y lectura de campañas masivas de WhatsApp hechas desde
  Prometheo (CRM → Campañas). Usala al diseñar o reportar un envío masivo, al
  armar la pestaña de WhatsApp Marketing de un tablero de Inteligencia Comercial,
  al elegir la audiencia por Smart Tag o por archivo externo, o al leer calidad
  de número, messaging tier y plantillas. Activar ante "campaña de WhatsApp",
  "envío masivo", "difusión", "plantilla aprobada", "messaging tier", "calidad
  del número", "smart tag para la campaña", "a quién le mando".
---

# WhatsApp masivo desde Prometheo

Es el canal que más se parece a Prometheo, porque **es Prometheo**: la campaña sale
de la misma base que después conversa, con el mismo agente y el mismo embudo. No hay
empalme entre dos sistemas como en email: **el canal y el CRM son el mismo lugar**.
Eso cambia qué se puede medir y qué se puede segmentar.

## Relación con otras skills

- `aurea-email-prometheo` comparte la doctrina de denominadores, escalera de
  compromiso y las tres alturas de la pestaña. **No la repitas: acá van solo las
  diferencias de WhatsApp.**
- `sms` (vendorizada, MIT) es el marco estructural más cercano: cada envío tiene
  costo real, el opt-in es el activo, cada mensaje tiene que justificarse solo, y
  la tasa de baja es el termómetro de fatiga.
- `aurea-curaduria-dato` manda en base, cobertura y origen.
- `aurea-metodologia` manda en qué Smart Tags y variables existen para segmentar.

---

## 1. Lo que la plataforma reporta, y lo que no

Prometheo actualiza por campaña, en `CRM → Campañas`:

| Reporta | No reporta |
|---|---|
| Mensajes **enviados** | Entregas confirmadas por separado del envío |
| Mensajes **visualizados** (leídos) | Clics: el mensaje no lleva tracking propio |
| **Respuestas recibidas** | Costo por conversación |
| **Rechazados con motivo** (descargable en Excel) | Atribución a la venta final |

**Consecuencia de diseño:** en WhatsApp **no existe el clic**. La escalera de
compromiso va de entregado a leído a **respondido**, y el escalón que importa es
respondido, porque abre la conversación con el agente. En email el titular es el
clic; acá es la respuesta.

El **rechazado con motivo** es dato de calidad de base, no de campaña: número sin
WhatsApp, prefijo mal cargado, baja previa. Se trata como faltante de proceso y se
devuelve al CRM para depurar.

## 2. Las restricciones de la plataforma son métricas

Lo que en otro canal es letra chica, acá es tablero. Un especialista mira esto primero.

**Plantilla aprobada.** Todo mensaje iniciado por la empresa, o posterior a las 24
horas, exige una plantilla aprobada por WhatsApp. Desde Prometheo se envía **solo
texto con variables**: no van archivos, imágenes ni documentos. Diseñar la campaña
asumiendo un PDF adjunto es diseñarla mal.

**Messaging Tier.** Es el techo diario de conversaciones:

| Tier | Conversaciones por día |
|---|---:|
| 0 | 250 |
| 1 | 1.000 |
| 2 | 10.000 |
| 3 | 100.000 |
| 4 | prácticamente ilimitado |

Sube **solo automáticamente**, por calidad de número, mensajes reales sin reportes y
actividad consistente. No se fuerza. Por eso el tier es un **activo que se construye**:
una campaña mal segmentada que genera reportes no cuesta solo esa campaña, cuesta el
techo de todas las siguientes.

**Consentimiento.** Se puede escribir a alguien que nunca habló, con plantilla
aprobada y **consentimiento previo**. Sin consentimiento baja la calidad del número y
activan restricciones.

**Verificación de la empresa y país.** Una empresa no verificada tiene limitaciones de
país, problemas para subir de tier y más chance de bloqueo.

> **Regla de la casa:** toda pestaña de WhatsApp muestra **tier actual, calidad del
> número y tasa de reporte**, aunque el cliente no los pida. Son el único indicador
> temprano de que el canal se está quemando, y cuando se nota en la conversión ya es tarde.

## 3. Las métricas, con su denominador

| Métrica | Fórmula | Denominador |
|---|---|---|
| Tasa de entrega | enviados menos rechazados / enviados | enviados |
| **Tasa de lectura** | visualizados / **entregados** | entregados |
| **Tasa de respuesta** | respondieron / **entregados** | entregados |
| Respuesta sobre lectura | respondieron / **visualizados** | visualizados |
| Tasa de calificación | calificados por el agente / respondieron | respondieron |
| Consumo de tier | conversaciones del día / tope del tier | tope del tier |

**No importes benchmarks de email.** La lectura en WhatsApp es estructuralmente alta
(el mensaje se ve en la notificación) y por eso **leído dice mucho menos que abierto**
en email: es casi un hecho, no una señal de interés. El número que separa una campaña
buena de una mala es **respuesta sobre lectura**.

**No importes benchmarks de SMS ni de difusión masiva genérica.** La comparación válida
es contra el envío anterior a una audiencia equivalente del mismo cliente.

## 4. Segmentar es el producto

En email la segmentación es una lista. Acá es una **consulta al CRM**, y por eso se
puede explicar y auditar. La audiencia sale de una de dos fuentes, y **la pestaña dice
cuál**:

| Origen | Qué es | Cuándo |
|---|---|---|
| **Smart Tag de Prometheo** | La audiencia es el resultado de un filtro sobre la base viva | Siempre que se pueda. Es auditable y se actualiza sola |
| **Archivo externo** (Excel, scraping) | Se sube una lista con encabezado en la fila 1 y prefijo correcto | Solo cuando el dato no vive en el CRM. Hay que decirlo |

Cuando la audiencia sale de un archivo externo, **es obligatorio declararlo en la
pestaña**, porque cambia la confianza del dato: esa lista no tiene historial, no tiene
consentimiento verificable y no se actualiza.

### El criterio de segmentación de AUREA: tres ejes

Una campaña dirigida se define con tres ejes, y la pestaña **muestra los tres**:

1. **Estadío de venta.** Dónde está el contacto en el embudo (activo, pasivo,
   calificado, en negociación). Define la *intención* del mensaje.
2. **Tipo de comprador.** Qué clase de cliente es (rubro, tamaño, rol en el canal).
   Define el *tono* y qué argumento aplica.
3. **Tipo de producto.** Qué compra hoy y qué no compra. Define la *oferta*.

Una campaña que no puede nombrar sus tres ejes no está segmentada: es una difusión.

**Mostrar el embudo de la segmentación, no solo el resultado.** De la base total a la
audiencia final hay filtros, y cada filtro es una decisión que el cliente tiene que
poder discutir. Un "150 distribuidores" sin el camino que llevó a 150 no se audita.

## 5. La ventana de 24 horas

Concepto propio de WhatsApp y hay que mostrarlo, porque decide el costo y la libertad
del agente. Cuando el contacto responde, se abre una ventana de 24 horas en la que el
agente conversa **libre**, sin plantilla. Pasada la ventana, para retomar hace falta
otra plantilla aprobada.

**Lectura operativa:** una respuesta no es solo una señal de interés, es **permiso para
conversar**. Por eso la métrica de respuesta manda, y por eso el seguimiento del agente
dentro de las primeras horas vale más que cualquier reenvío posterior.

## 6. Básico y Avanzada

- **Básico** responde: a quién le escribimos, cuántos leyeron, cuántos contestaron y
  qué salió de eso.
- **Avanzada** agrega lo que solo lee un especialista: consumo y techo del tier,
  calidad del número y tasa de reporte, motivos de rechazo desagregados, ventana de
  24 horas aprovechada, franja horaria de respuesta, rendimiento por variante de
  plantilla, y la matriz segmento por concepto.

Avanzada **agrega, nunca reemplaza**, y ninguna métrica cambia de nombre entre modos.

## 7. Checklist antes de publicar

- [ ] ¿Está declarado el origen de la audiencia (Smart Tag o archivo externo)?
- [ ] ¿Se ven los tres ejes de segmentación y el embudo que llevó a la audiencia final?
- [ ] ¿La lectura está sobre entregados y la respuesta también?
- [ ] ¿Está "respuesta sobre lectura", que es el número que discrimina?
- [ ] ¿Aparecen tier, calidad de número y tasa de reporte?
- [ ] ¿Los rechazados están desagregados por motivo y devueltos al CRM como tarea?
- [ ] ¿Se explica la ventana de 24 horas donde corresponde?
- [ ] ¿El titular es la respuesta y no la lectura?

## 8. Anti-patrones

- **Titular con la tasa de lectura.** En WhatsApp leer es casi automático. Titular con
  eso es vender humo.
- **Comparar contra benchmarks de email o de SMS.**
- **Una audiencia sin sus tres ejes**, presentada como campaña dirigida.
- **Esconder que la lista vino de un Excel externo.**
- **Ignorar el tier hasta que bloquean el número.** Es el único activo del canal que se
  pierde de golpe y tarda meses en recuperarse.
- **Diseñar la campaña con adjuntos**, que Prometheo no envía en masivo.
- **Tratar el rechazado como ruido** en vez de como tarea de depuración del CRM.

---

## Derivación

Escritura propia de AUREA sobre la documentación de Prometheo (`CRM → Campañas`,
envíos masivos) y las restricciones de la WhatsApp Business Platform. Toma de `sms`
(Corey Haines, MIT) el marco de costo por envío, opt-in como activo y fatiga de lista;
de `aurea-email-prometheo` la doctrina de denominadores y las tres alturas. Lo propio:
las restricciones de plataforma tratadas como métricas de tablero, los tres ejes de
segmentación con su embudo visible, y la ventana de 24 horas como métrica operativa.
