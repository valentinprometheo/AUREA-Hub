---
consultar-cuando: arrancar el diseño de CRM de una cuenta nueva, decidir cuántos embudos, qué tags y qué variables
disparadores: "diseño de CRM cuenta nueva", "cuántos embudos", "arquitectura de embudos", "qué tags le pongo", "molde de CRM"
fuente-única-de: moldes de arquitectura de CRM por rubro (embudos + dimensiones de tags + variables típicas)
combina-con: embudos-y-tags (el criterio de diseño), 06-estructura-guia-implementador, el rubro correspondiente
---

# Arquitectura de CRM por rubro (moldes de referencia)

> El criterio de diseño (embudo vs tag, padre/hija, etc.) vive en `embudos-y-tags.md`. Este
> archivo es lo otro: los **moldes concretos** que ya funcionaron, para calcar la estructura al
> arrancar una cuenta nueva del mismo rubro en vez de reinventarla. Validados en tres cuentas.
>
> **Regla de uso:** lo de acá es el ESQUELETO (patrón, sube y se reutiliza). Los valores
> concretos de cada cuenta (nombres de proyectos, catálogo, zonas, nombres del equipo) son
> INSTANCIA: viven en el material de la cuenta, no acá. Calcás la estructura, no los datos.

---

## Molde desarrollista inmobiliario (validado en EDFAN y G&D)

### Embudos — 3
1. **Recepción, Calificación y Agendamiento** (lo conduce el agente). De "Nuevo Lead" a
   "Calificado / Derivado / Agendado". Es el único embudo que el agente acciona solo.
2. **Venta y Cierre** (equipo humano). De reunión realizada a reserva/cuenta activa/no
   concretado. Mide la conversión del equipo, no del agente.
3. **Gestión Inmobiliarias B2B** (equipo humano). Ciclo propio de relación con inmobiliarias
   que traen clientes: no se las califica ni se les vende una unidad, se gestiona una relación
   recurrente.

Nota de diseño: "Nuevo Lead" conviene reservarlo para la base histórica importada (contactos que
nunca conversaron); el que escribe por primera vez entra directo a "En Conversación". Cuidado con
la superposición Calificado/Derivado: aplicar el test "¿hay un caso en Calificado pero no en
Derivado?".

### Dimensiones de tags
- **Estadío** (una por embudo): las etapas del embudo hechas etiqueta.
- **Tipología del lead** (una a la vez, excluyente): Inversor / Uso propio / Inmobiliaria /
  Desarrollador. Distinguir inversor (compra una unidad a su nombre) de desarrollador (aporta
  capital al desarrollo, se deriva sin calificar).
- **Prioridad** (opcional, combinable): Contacto VIP.

### Variables típicas
Calificación (se extraen solas): Canal Origen, Proyecto Interés (múltiple), Zona Interés
(múltiple), Tipo Unidad, Estado Proyecto, Presupuesto, Forma de Pago, Horizonte Compra. Perfil en
dos capas: Tipo Perfil / objetivo_busqueda (padre: inversión vs uso propio) + Inversión Finalidad
(hija). Acción del agente: Reunión Características, Tipo Derivación. Reconocimiento: Obra Anterior
Mencionada (múltiple). Fechas por modalidad: Reunión Física / Reunión Virtual. Estado humano:
Reasignación Moderador (por conversación). Inteligencia comercial (las 6): Objeción Principal +
Frase Literal, Pedido Fuera de Catálogo + Detalle, Dolor Principal, Disparador Compra.

---

## Molde mobiliario (validado en BETROX)

### Embudos — 4
1. **Recepción, Calificación y Agendamiento** (agente). Hasta agendar showroom/videollamada o
   pasar cotización.
2. **Venta y Cierre** (equipo). Desde que el showroom/videollamada sucede hasta la entrega
   (negociación, seña, producción, entregado).
3. **B2B Profesionales y Proyectos** (equipo). Arquitectos, decoradores, paisajistas,
   constructoras, municipios, proyectos de escala.
4. **Postventa** (equipo). Reclamos, reparaciones, mantenimiento de piezas ya entregadas: no es
   un lead nuevo, es un cliente con un problema.

Por qué 4 y no 3: el mismo corte Recepción/Venta del molde desarrollista, más B2B y Postventa
como recorridos propios. Cada embudo lleva su "Descripción para la IA" (instrucción que el modelo
lee para decidir cuándo asignar sus tags).

### Dimensiones de tags
- **Estadío** (una por embudo), con las 3 acciones de plataforma colgando de las tags de handoff
  (Apagar Asistente en Derivado / Showroom Realizado / Postventa Abierta / No Fit; Notificaciones
  en cotización, agendamientos, derivaciones, B2B).
- **Tipología** (espeja el padre de la variable Tipo Cliente): Consumidor Final / Profesional /
  Cliente Recurrente.
- **Prioridad** (opcional): Proyecto Grande.

### Variables típicas
Transversales: Canal Origen, Tipo Cliente (padre) + Tipo Profesional (hija), Línea Producto
(múltiple), Tipo Compra (estándar/configurable/a medida/proyecto), Producto Interés (múltiple),
Modelo Mencionado (texto, clave de consulta a la integración), Medida Solicitada, Ciudad Zona,
Outlet Interés. Handoff: Tipo Derivación, Contexto Derivación. Inteligencia comercial: las mismas
6, con las objeciones propias del material (Peso, Mantenimiento, Variación color).

---

## Qué se mantiene entre rubros y qué cambia

**Se mantiene (patrón transversal de arquitectura):**
- El corte Recepción (agente) vs Venta (equipo) como primeros dos embudos.
- Un embudo propio por cada canal con ciclo de vida estructuralmente distinto (B2B, postventa).
- Perfil en dos capas (variable padre única + hija condicional) con tag de tipología que espeja
  el padre.
- El estado solo en el embudo; las 6 variables de inteligencia comercial; datos vivos a la
  integración.

**Cambia por rubro (instancia):**
- La cantidad de embudos (3 desarrollista, 4 mobiliario: depende de si hay postventa/B2B con
  ciclo propio).
- Los valores de cada dimensión de tag y las variables de catálogo (líneas, tipologías,
  proyectos): son el negocio de cada cuenta.
- Las objeciones propias del rubro (las de mobiliario incluyen peso y mantenimiento; las de
  desarrollista, fideicomiso y entrega).

Para un rubro sin molde todavía (insumos, inmobiliaria tradicional): se parte del corte
Recepción/Venta y se agrega embudo propio solo donde haya un ciclo estructuralmente distinto,
aplicando la prueba embudo-vs-tag de `embudos-y-tags.md`. No se copia un molde de otro rubro sin
pasar por esa prueba.
