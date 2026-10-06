---
name: aurea-whatsapp-prometheo
description: Métricas de campañas masivas de WhatsApp enviadas desde el CRM de Prometheo, para los tableros de Inteligencia Comercial de AUREA. Define qué titula, cómo se leen la lectura y la respuesta, y cómo se tratan el tier de envío y la calidad del número como métricas de tablero. Usala SIEMPRE que haya que reportar o diseñar métricas de WhatsApp masivo, difusiones, plantillas, reactivación por WhatsApp, o auditar la salud del número. Activar ante "WhatsApp masivo", "difusión", "plantilla", "tasa de respuesta", "lectura", "tier", "calidad del número", "bloqueos", "campaña de WhatsApp".
---

# Métricas de WhatsApp masivo (AUREA · Inteligencia Comercial)

> BORRADOR inicial armado desde el informe de criterio comercial. Las definiciones
> marcadas `[A DEFINIR]` hay que validarlas con una campaña real. Todavía no existen
> benchmarks propios: no cites referencias de mercado como si fueran de AUREA.

En WhatsApp **no existe el clic**: el equivalente es la respuesta. Por eso **titula la
respuesta, no la lectura**. Esta skill hereda de `aurea-curaduria-dato` las reglas de
base, cobertura, origen y fuentes.

## 1. Quién manda en cada número

| Fuente | Manda en | No manda en |
|---|---|---|
| WhatsApp / plataforma de envío | Enviados, entregados, leídos, fallidos, tier, calidad del número | Calificación del lead |
| Prometheo | Respuestas, conversaciones, calificación, derivación | Lectura |

## 2. Métricas y base

| Métrica | Cálculo | Base |
|---|---|---|
| Tasa de entrega | entregados / enviados | enviados |
| Lectura | leídos / entregados | entregados |
| **Respuesta** (titula) | respondieron / entregados, y también respondieron / leídos | entregados y leídos (doble lectura) |
| Calificación de lo generado | respuestas calificadas (definición del tablero) / respuestas | respuestas |
| Opt-out y bloqueos | bajas o bloqueos / entregados | entregados |

## 3. Reglas

- **La lectura es subestimada**: quien desactivó la confirmación de lectura no cuenta.
  Por eso la respuesta se reporta con **doble lectura** (sobre entregados y sobre
  leídos) y la lectura nunca titula.
- **Tier de envío y calidad del número son métricas de tablero**, no detalle técnico:
  - Tier: el límite de contactos únicos que el número puede alcanzar en 24 horas.
    Define el tamaño máximo de la próxima difusión.
  - Calidad del número (indicador de la plataforma, por ejemplo alta, media, baja):
    cae con bloqueos y reportes, y puede bajar el tier o limitar envíos.
  - Mostralos con fecha de actualización y su tendencia.
- **Auditá la salud antes de escalar**: si la calidad baja, el hallazgo es ese, no la
  tasa de respuesta.
- Aplicá la escalera de evidencia. Con n chico, mostrá conteos y no porcentajes.
- Si la campaña está modelada y no corrida, decilo en el mismo bloque.
- Costo por mensaje y por categoría de plantilla: `[A DEFINIR]` según el proveedor.

## 4. Checklist

- [ ] La respuesta titula; la lectura no.
- [ ] Respuesta con doble lectura (entregados y leídos).
- [ ] Tier y calidad del número visibles, con fecha.
- [ ] Ninguna cifra mezcla plataforma de envío y Prometheo.
- [ ] Sin benchmarks inventados.

## Relacionadas

`aurea-ic-curaduria-del-dato` (base y evidencia), `aurea-dashboard-design` (cómo se
ve), `aurea-metodologia` (diseño del CRM y mensajería automatizada).
