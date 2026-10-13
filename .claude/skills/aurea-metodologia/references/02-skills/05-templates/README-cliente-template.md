# README Template para un Cliente

**README que Claude genera para que cualquier persona (consultor nuevo, AI helper) entienda el estado de un cliente al ingresar a su Project en Claude.**

Se genera cuando arrancás un Project nuevo de un cliente. Se actualiza en cada hito mayor.

---

## Estructura del README cliente

```markdown
# README — [Cliente]

**Última actualización:** [fecha]

---

## 1. Quién es el cliente

- **Nombre comercial:** [...]
- **Rubro:** [Desarrollista inmobiliario / Mobiliario / etc.]
- **Modelo de negocio:** [B2B / B2C / mixto + descripción 1 línea]
- **Tamaño del equipo:** [...]
- **Ubicación:** [...]

## 2. Estado del proyecto

- **Etapa actual:** [Pre-E1 / E1 Discovery / E2 Diseño / E3 Implementación / Soporte]
- **Sub-estado:** [...] (ej: "Ronda 1 entregada, esperando aprobación cliente")
- **Próximo hito:** [...]
- **Fecha estimada de Go-Live:** [...]
- **Bloqueantes:** [si hay, lista]

## 3. Stack técnico

- **Plan Prometheo:** [Basic / Pro / Enterprise]
- **Integraciones activas:** [Tokko / PrestaShop / ficha.info / etc.]
- **Modalidad de catálogo:** [A / B / C]
- **Canales:** [WhatsApp / Instagram / Mail / Web]

## 4. Decisiones cerradas

- [...]
- [...]

## 5. Decisiones pendientes

- [...] (pendiente de cliente)
- [...] (pendiente de bot oficial Prometheo)

## 6. Archivos clave en este Project

### Project Knowledge cargado
- [...]

### Outputs generados
- `[Cliente] - Doc 1 Sintesis.md`
- `[Cliente] - Diseño de CRM.docx`
- `[Cliente] - Prompt - V[N].md`
- `Guía para Implementador - [Cliente].md`

## 7. Links externos

- **Drive del cliente:** [link]
- **CRM Prometheo del cliente:** [link]
- **Tokko / PrestaShop:** [link]

## 8. Contactos

### Equipo cliente
- [Nombre · rol · mail · WhatsApp]

### Equipo AUREA asignado
- Responsable principal: Valentín Zas
- Otro: [...]

## 9. Notas históricas relevantes

- [Fecha] · Decisión: [...]
- [Fecha] · Hito: [...]
- [Fecha] · Cambio importante: [...]

## 10. Para retomar el proyecto

Si arrancás una conversación nueva, primero:
1. Leer este README
2. Leer Doc 1 (Síntesis del Discovery)
3. Leer último entregable (DOCX o Prompt según etapa)
4. Verificar bloqueantes y decisiones pendientes
5. Confirmar próximo hito con Valentín antes de proponer outputs
```

---

## Cuándo se actualiza el README

- Al cerrar Etapa 1 (Discovery aprobado)
- Al entregar DOCX y Prompt (Ronda 1)
- Al aprobarse Ronda 1
- Al entregar Guía (Ronda 2)
- En cada Go-Live
- Cada vez que aparece un bloqueante nuevo

---

## Reglas operativas

1. **README es la fuente de verdad del proyecto.** Más arriba que cualquier docs.
2. **Actualizarlo en mismo commit que el hito.** No dejar desactualizado.
3. **Brevedad útil.** Si el README pasa de 3 páginas, dividir en sub-archivos.
4. **Visible en raíz del Project Knowledge.** Es el primer archivo que cualquiera lee.

---

## Errores frecuentes

- README desactualizado (3 versiones atrás)
- Falta sección "Decisiones pendientes" → próximo consultor no sabe qué resolver
- Falta sección "Bloqueantes" → se pierde info crítica
- README extenso sin secciones claras → no se lee
- Olvidar actualizar al cambiar de etapa
