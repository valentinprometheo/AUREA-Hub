# Protocolo de Implementación en Prometheo

> **Paso:** 5 (Implementación + Go-Live + Monitoreo)
> **Sub-fase:** Carga en Prometheo
> **Duración estimada:** 1–2 semanas
> **Pre-requisito:** Guía Implementador aprobada (Ronda 2 del Paso 2 de Etapa 2)

---

## Filosofía

La implementación es **técnica pero no improvisada**. Cada elemento se carga siguiendo la Guía Implementador, en un orden específico que minimiza errores y retrabajo.

**Regla:** no se inventa nada acá. Si la Guía no lo dice, se vuelve al consultor AUREA antes de tomar la decisión.

---

## Orden de carga en Prometheo

### Fase 1 — Estructura base (Día 1-2)

1. **Crear el embudo principal**
   - Etapas según diseño aprobado
   - Nombres exactos de la Guía
   - Color por etapa según convención

2. **Configurar el equipo humano**
   - Crear usuarios para cada vendedor
   - Asignar roles (vendedor, supervisor, admin)
   - Configurar permisos según diseño

3. **Conectar canales**
   - WhatsApp Business API
   - Otros canales activos (Instagram DM, web form, etc.)

### Fase 2 — Variables (Día 3-4)

1. **Variables de la ficha del lead** — según diseño del DOCX
2. **Variables de calificación** — específicas del rubro
3. **Variables condicionales** — para casos especiales
4. **Validación de carga** — verificar que cada variable tenga su tipo correcto (Texto, Texto largo, Link, Número, Precio, Opciones)

### Fase 3 — Smart Tags (Día 5)

1. **Smart Tags base obligatorias:**
   - `#seguimiento_activo`
   - `#derivar_a_humano`

2. **Smart Tags del cliente** — según diseño
3. **Acciones asociadas a cada tag**
4. **Validación de regla v7:** una sola Smart Tag activa por conversación

### Fase 4 — Seguimientos (Día 6-7)

1. **Cargar cada seguimiento como fórmula nativa Prometheo:**
   ```
   Tag macro + Variable router + Variable estado + Tiempo
   ```

2. **Verificar lógica AND** donde aplique
3. **Configurar mensajes con placeholders** correctos (los que Prometheo soporta nativamente)

### Fase 5 — Prompt del agente (Día 7-8)

1. **Cargar el Prompt final aprobado** en Prometheo
2. **Conectar el prompt con las variables y tags definidas**
3. **Configurar reglas de distribución** (a quién deriva cada tipo de lead)

### Fase 6 — Conectar fuentes de datos (Día 9-10)

1. **Tokko (si aplica)** — verificar conexión, sincronización de stock
2. **PrestaShop (si aplica)** — para insumos y mobiliario con catálogo digital
3. **Otras integraciones del cliente**

---

## Checklist de cierre de la implementación

Antes de pasar a Testing Interno, verificar:

- [ ] Embudo cargado con todas las etapas
- [ ] Equipo humano configurado con permisos correctos
- [ ] Todos los canales conectados y respondiendo
- [ ] Variables cargadas con tipos correctos
- [ ] Smart Tags configuradas con acciones asociadas
- [ ] Seguimientos activos con sus fórmulas
- [ ] Prompt cargado y conectado a variables/tags
- [ ] Reglas de distribución configuradas
- [ ] Tokko/otras fuentes conectadas y sincronizadas
- [ ] Cliente recibió accesos a su instancia de Prometheo

---

## Errores comunes en implementación

| Error | Síntoma | Solución |
|---|---|---|
| Variables mal tipadas | El agente no las completa correctamente | Verificar tipo (Texto / Opciones / Precio / etc.) |
| Tags con nombres muy parecidos | El agente activa la tag equivocada | Renombrar para que no haya ambigüedad semántica |
| Seguimientos sin variable router | Se envían a todos los leads, no a los que corresponden | Agregar variable router al filtro |
| Tokko desconectado | El agente inventa precios | Verificar API key y test de sincronización |
| Reglas de distribución incompletas | Leads que no caen en ningún vendedor | Revisar matriz de distribución del DOCX |

---

## Documentación interna de la implementación

Durante la implementación, el implementador mantiene un documento técnico:

**Naming:** `[CLIENTE] - Implementación - Notas Técnicas.md`

**Contenido típico:**
- Fecha de cada paso de carga
- Decisiones tomadas que no estaban explícitas en la Guía
- Bugs encontrados o limitaciones de Prometheo
- Configuraciones específicas del cliente (IDs, tokens, etc.)

**Para qué sirve:**
- Si el implementador no es el mismo que diseñó, este doc es el puente
- Si hay que hacer ajustes futuros, este doc es la referencia
- AUREA puede usarlo como input para mejorar la metodología

---

## Cuándo escalar a Prometheo (ITESA)

**Casos donde se contacta a ITESA (Martín, Juan, Pachu) vía bot oficial de WhatsApp:**

- Comportamiento no documentado de Prometheo (algo que no estaba claro en la doc oficial)
- Sintaxis específica de Smart Tags / Variables / Seguimientos
- Bugs detectados en la plataforma
- Limitaciones de plan o features que el cliente necesita

**Regla AUREA:** ante cualquier duda sobre cómo se comporta Prometheo, **preguntar al bot oficial** antes de asumir.
