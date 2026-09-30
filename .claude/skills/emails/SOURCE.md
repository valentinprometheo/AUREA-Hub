# emails (vendorizada)

Skill comunitaria de Corey Haines, licencia MIT.
Origen: https://github.com/coreyhaines31/marketingskills (`skills/emails`)
Commit vendorizado: `5b2c000` (2026-09-04)

## Por qué está acá

Es la skill de **diseño de secuencia de email**: cuántos mails, con qué espaciado,
qué asunto, un trabajo por mail, y las plantillas de re-engagement y win-back. Es
justo la forma de campaña que usamos para reactivar bases dormidas (caso PAVIR:
200 distribuidores pasivos sobre 700).

## Lo que aporta y usamos

- **Un mail, un trabajo. Un CTA por mail.** Ordena el concepto de cada envío.
- **Relevancia sobre volumen.** Segmentar antes que mandar más.
- **Plantilla de re-engagement**: 3 a 4 mails en 2 semanas (check-in, recordatorio
  de valor, incentivo, última chance). Es el molde de la campaña de reactivación.
- **Asunto**: claro antes que ingenioso, 40 a 60 caracteres, y el preview extiende
  el asunto en vez de repetirlo.
- **Timing B2B**: evitar fines de semana, 2 a 4 días entre mails de nurture.

## Lo que NO trae, y por eso escribimos la nuestra

1. **No tiene escalera de métricas de email.** Dice "Metrics Plan: what to measure
   and benchmarks" como título y no lo desarrolla.
2. **Los benchmarks que sí hay en el repo son de `cold-email`** (apertura 27,7%,
   respuesta 4 a 5,8%). No sirven para lista propia: un distribuidor que ya nos
   compró no se compara contra un contacto frío.
3. **No cubre el traspaso al CRM.** Termina en el clic. Todo lo que pasa después
   (el agente responde el mail, califica y deriva) es nuestro territorio y no
   existe en ninguna skill de terceros.

Eso se resuelve en `aurea-email-prometheo`, que es cruce y escritura propia.

## Skills relacionadas del mismo repo

`cold-email` (benchmarks de frío, no de lista propia), `churn-prevention`
(flujos de salvataje), `revops` (etapas que disparan secuencias), `ab-testing`.
