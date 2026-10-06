---
name: aurea-ic-email-marketing
description: Métricas de campañas de email que terminan en una conversación de Prometheo, para los tableros de Inteligencia Comercial de AUREA. Define qué se mide, sobre qué base y qué puede titular una card. Usala SIEMPRE que haya que reportar o diseñar métricas de una campaña de email, newsletter, secuencia o reactivación de base propia, calcular CTR, CTOR, tasa de empalme, aperturas, bajas o rebotes, o decidir qué mostrar de un export de la plataforma de email. Activar ante "email", "campaña de mail", "CTOR", "CTR", "tasa de empalme", "apertura", "newsletter", "reactivación de base", "secuencia de emails".
---

# Métricas de email (AUREA · Inteligencia Comercial)

> BORRADOR inicial armado desde el informe de criterio comercial. Las definiciones
> marcadas `[A DEFINIR]` hay que validarlas con una campaña real. Todavía no existen
> benchmarks propios: no cites referencias de mercado como si fueran de AUREA.

En AUREA el email no termina en el clic: **el clic es el empalme**, el paso que lleva
a una conversación en Prometheo. Esta skill hereda de `aurea-ic-curaduria-del-dato` las reglas
de base, cobertura, origen y fuentes. Acá se agrega lo específico del canal.

## 1. Quién manda en cada número

| Fuente | Manda en | No manda en |
|---|---|---|
| Plataforma de email | Envíos, entregados, rebotes, aperturas, clics, bajas | Cuántas conversaciones hubo |
| Prometheo | Consultas generadas, calificación, derivación | Aperturas y clics |

Nunca sumes ni mezcles: el conteo de consultas lo define Prometheo.

## 2. Métricas y base

| Métrica | Cálculo | Base |
|---|---|---|
| Tasa de entrega | entregados / enviados | enviados |
| CTR | clics únicos / entregados | entregados |
| **CTOR** | clics únicos / aperturas únicas | aperturas únicas |
| **Tasa de empalme** | contactos que escriben a Prometheo dentro de la ventana tras el clic / clics únicos. Ventana: `[A DEFINIR]` | clics únicos |
| Calificación de lo generado | consultas calificadas (misma definición del tablero) / consultas del email | consultas del email |
| Bajas y reportes de spam | bajas / entregados | entregados |

## 3. Reglas

- **La apertura es una señal inflada** (precarga de imágenes y protecciones de
  privacidad). Nunca titula una card; va como Indicio o en modo Avanzada.
- **Titula el empalme** y, detrás, la calificación de lo que generó. CTR y CTOR leen el
  mensaje; el empalme lee el negocio.
- **CTOR además de CTR**: el CTR depende del tamaño de la lista y el CTOR mide la calidad
  del contenido entre quienes abrieron.
- **Atribución**: el link lleva un identificador de campaña. Los empalmes sin
  identificador se muestran como faltante estructural, no se reparten.
- **Base propia, no prospección fría**: no uses benchmarks de cold email.
- Aplicá la escalera de evidencia (Hecho, Señal, Indicio, No reportable) a cada métrica
  según su base y cobertura. Con n chico, no muestres porcentajes.
- Si la campaña está modelada y no corrida, decilo en el mismo bloque.

## 4. Checklist

- [ ] Cada porcentaje dice su denominador.
- [ ] La apertura no titula.
- [ ] El empalme está definido con su ventana.
- [ ] Ninguna cifra suma plataforma de email y Prometheo.
- [ ] Los empalmes sin identificador figuran como faltante.
- [ ] Sin benchmarks inventados.

## Relacionadas

`aurea-ic-curaduria-del-dato` (base y evidencia), `aurea-dashboard-design` (cómo se
ve), `emails` (diseño de secuencias, si está instalada).
