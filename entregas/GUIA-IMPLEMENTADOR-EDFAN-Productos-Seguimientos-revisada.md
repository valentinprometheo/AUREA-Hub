# GUÍA DE IMPLEMENTADOR · EDFAN Productos · Insumos y materiales para construcción · agente Paula
Integración: Google Sheets (SISTEMAS_RESUMEN, SISTEMAS_COTIZACION) · Fecha: a confirmar

Nota de alcance: esta guía cubre los seguimientos automatizados por falta de respuesta, las tags de estadío de las que cuelgan (En Conversación y En Seguimiento), la tag nueva No Contactar y las plantillas de WhatsApp (Meta) asociadas. No cubre el resto de las variables, tags, embudos ni el prompt del agente: para eso, ver la guía principal de EDFAN Productos.

---

## REVISIÓN · auditada con la metodología AUREA v1.25

### Cambia
1. **Prompt de En Seguimiento.** El significado queda igual: "dejó de responder antes de quedar calificado". Se suma que la tag es obligatoria y se asigna por la falta de respuesta (unas 4 horas), salga o no un mensaje de seguimiento; el caso del lead que avisa que retoma más adelante; y el prompt dice cuándo se asigna y qué no la cambia. Reglas duras 14 y 15.
2. **Los mensajes son opcionales, la tag no.** Se aclara en la serie: si un mensaje no sale (por la condición de moderador, la ventana horaria o porque no está configurado), el lead igual queda en En Seguimiento. La prueba 1 del testing lo verifica.
3. **Mensaje del Seguimiento B.** Antes: invitaba al showroom. Ahora: mensaje general que retoma la necesidad. De un lead que no calificó solo se sabe que escribió y se calló; la invitación al showroom va en el seguimiento por Calificado (ver "Para la guía principal").
4. **Nombres de las plantillas.** Antes: `en_seguimiento_24hs` y `en_seguimiento_72hs`. Ahora: `sin_respuesta_24hs` y `sin_respuesta_72hs`, porque la plantilla no depende de qué tag la dispara.
5. **Condición de la variable en A y B.** Antes: valor sin definir. Ahora: `Contiene · No`, porque la variable tiene "No" por defecto. Queda pendiente solo qué pasa con los contactos creados antes de la variable.
6. **Pendiente de no contacto.** Antes: propuesta de usar No Fit. Ahora: tag propia "No Contactar". No Fit significa "no es un comprador posible" y no se reutiliza con otro significado (regla dura 9); además ensuciaría la medición de no-demanda en el tablero.
7. **Guiones largos.** Los títulos usaban em-dash; ahora usan "·" (regla de formato 6 de la Guía).
8. **Sin "quitala cuando" en los prompts.** La salida de cada estadío la resuelve el grupo excluyente Recepción, que la guía ya usaba: al asignarse otra tag del grupo, la anterior se quita sola. Un "quitala cuando" en una tag Dinámica puede dejar al lead sin etapa. No Contactar va en modo Fijo, así la IA no la deshace. Reglas duras 14 y 18, restricción 26.

### Se agrega
- Tag **En Conversación** con prompt de cuándo se asigna y qué no la cambia: es el ida y vuelta del que sale el lead a En Seguimiento, y su salida es la entrada de Calificado (regla dura 16).
- Tag **No Contactar**, en el grupo excluyente de Recepción, que apaga el asistente y corta toda la serie.
- Pruebas de testing: lead que posterga, lead que pide no ser contactado y la prueba que define de qué tag cuelgan B y C.
- "Para la guía principal": lo que esta guía no cubre y la metodología pide (seguimiento por Calificado y por Hot Lead).

### Queda igual (está bien, no se toca)
- El grupo excluyente **Recepción** y el modo Dinámico en los estadíos: ya estaban bien planteados.
- La variable **Reasignación A Moderador** completa: tipo, opciones, valor por defecto y prompt.
- Tiempos (4, 24 y 72 horas) y ventanas horarias (12/7 para A, 12/5 para B y C).
- "Asistente: seleccionar el agente activo" en cada seguimiento.
- Sintaxis `/Nombre` en los mensajes y `{{1}}` en las plantillas, y la nota de no editar una plantilla ya aprobada.
- Los tres seguimientos cuelgan de En Seguimiento, como estaba diseñado.
- Mensajes A y C.
- El Seguimiento C sin condición de moderador, con la decisión pendiente para la variante con gestión humana (pendiente 5).
- Pendientes 2, 3, 4 y 5.
- Formato vertical, nombres en formato natural y voseo.

---

## DATOS DE LA CUENTA Y SETUP

- Plan: Enterprise.
- Canal principal: WhatsApp (API oficial). El panel "Plantillas WhatsApp" ya está activo en la cuenta, con una plantilla cargada por el cliente (`activacion_conver`, Marketing, estado Pendiente), visto en captura real.
- Extensiones del Marketplace requeridas para lo trabajado acá: ninguna. Los seguimientos son nativos.

---

## VARIABLES (la que usan las condiciones)

Orden de carga: primero la variable, porque los seguimientos la usan como condición y no se pueden configurar sin que exista. Ya está cargada en la guía principal (variable 23).

### Reasignación A Moderador
- Tipo: Texto con Opciones
- Selección múltiple: No
- Opciones: Sí / No
- Valor por defecto: No
- Prompt de extracción:
```
Poné esta variable en "Sí" en cuanto detectes que una persona del equipo comercial (un humano, no vos) entró a responder en esta conversación: mensajes escritos por el vendedor, o cualquier señal de que la atención pasó a una persona.

Una vez en "Sí", se mantiene en "Sí" para el resto de la conversación.

Mientras la conversación la lleves únicamente vos como asistente, dejala en "No".

No le preguntes nunca al lead sobre esto: se infiere del desarrollo de la conversación, no se pregunta.
```

---

## SMART TAGS

Las tres son estadíos del Embudo 1 (Recepción, Calificación y Derivación), grupo excluyente Recepción. Comparten grupo con Calificado, Derivado y No Fit: al asignarse una, la otra se quita sola.

### En Conversación
- Dimensión: estadío del Embudo 1
- Grupo excluyente: Recepción
- Color: violeta (verificar contra la guía principal)
- Modo de asignación: Dinámico
- Prompt:
```
Asignala cuando el lead escribió y la conversación está activa, pero todavía no quedó claro si busca un producto estándar del catálogo o uno personalizado, o todavía no cumple las condiciones de Calificado.

No la quites porque el lead todavía no respondió. Los mensajes del asistente y los seguimientos automáticos no son respuestas del lead.
```
- Nota: la salida la resuelve el grupo excluyente. El lead deja En Conversación cuando entra a Calificado, Derivado, No Fit, En Seguimiento o No Contactar, según el prompt de cada una. Por eso el prompt de Calificado de la guía principal tiene que llevar la regla de EDFAN Productos palabra por palabra.
- Acción: ninguna directa. Cuando el lead deja de responder, pasa a En Seguimiento.

### En Seguimiento
- Dimensión: estadío del Embudo 1
- Grupo excluyente: Recepción
- Color: amarillo
- Modo de asignación: Dinámico
- Prompt:
```
Asignala cuando el lead venía conversando y dejó de responder antes de quedar calificado: se asigna por la falta de respuesta (unas 4 horas), le llegue o no un mensaje de seguimiento. También cuando el lead avisa que va a retomar más adelante ("lo veo y te aviso", "escribime la semana que viene").

No la quites porque el lead siga sin responder ni por mensajes del asistente o de otros seguimientos. Si solo responde para confirmar que va a retomar más adelante, mantenela.
```
- Acción: ninguna directa. De esta tag cuelgan los Seguimientos A, B y C. La tag es obligatoria; los mensajes, opcionales.

### No Contactar
- Dimensión: estadío del Embudo 1
- Grupo excluyente: Recepción
- Color: rojo (verificar que no se confunda con No Fit en el panel)
- Modo de asignación: Fijo (la IA no la puede quitar ni cambiar; solo un moderador)
- Prompt:
```
Asignala cuando el lead pide de forma explícita que no le escriban más, que lo saquen de la lista o que dejen de contactarlo.

No la asignes porque el lead tarde en responder o diga que lo va a pensar: eso es En Seguimiento.
```
- Acción: Apagar Asistente. Al compartir grupo con En Conversación y En Seguimiento, corta toda la serie.

---

## SEGUIMIENTOS AUTOMATIZADOS (por falta de respuesta)

Requieren: la variable "Reasignación A Moderador" ya cargada (ver arriba).

Cómo funciona la serie: En Conversación es el ida y vuelta. Cuando el lead deja de responder, pasa a En Seguimiento (obligatorio). Los mensajes A, B y C cuelgan de esa tag y son opcionales: si alguno no sale, el lead igual queda en En Seguimiento.

### Seguimiento A · En seguimiento · post 4hs
- Tipo: Seguimiento avanzado
- Condición Tag: En Seguimiento
- Condición Variable: Reasignación A Moderador · Contiene · No
- Tiempo de espera: 4 horas sin respuesta del lead
- Canal: WhatsApp
- Ventana horaria: Pack 12/7 (todos los días, 8 a 20hs)
- Asistente: seleccionar el agente activo (necesario para que dispare aunque el chat no esté "siendo atendido" activamente)
- Mensaje (usa sintaxis de variable con "/", NO corchetes: los corchetes se envían como texto literal):
```
Hola /Nombre, te habla Paula de EDFAN. Quedo a disposición para lo que necesites. ¿Retomamos?
```

### Seguimiento B · Sin respuesta · post 24hs
- Tipo: Seguimiento avanzado
- Condición Tag: En Seguimiento
- Condición Variable: Reasignación A Moderador · Contiene · No
- Tiempo de espera: 24 horas sin respuesta del lead
- Canal: WhatsApp
- Ventana horaria: Pack 12/5 (lunes a viernes, 8 a 20hs)
- Asistente: seleccionar el agente activo
- Plantilla: `sin_respuesta_24hs`
- Mensaje (propuesta a validar con EDFAN):
```
Hola /Nombre, soy Paula de EDFAN de nuevo. Si me contás para qué ambiente o superficie es, te recomiendo la opción que mejor te sirve. ¿Seguimos?
```

### Seguimiento C · Sin respuesta · post 72hs (cadencia larga)
No usa la variable Reasignación A Moderador: a esa altura ya no importa quién escribió último (ver pendiente 5).
- Tipo: Seguimiento avanzado
- Condición Tag: En Seguimiento
- Tiempo de espera: 72 horas sin respuesta del lead
- Canal: WhatsApp
- Ventana horaria: Pack 12/5 (lunes a viernes, 8 a 20hs)
- Asistente: seleccionar el agente activo
- Plantilla: `sin_respuesta_72hs`
- Mensaje:
```
Hola /Nombre, soy Paula de EDFAN de nuevo. Esta es mi última consulta por ahora, para no molestarte. Si seguís buscando revestimientos, ¿retomamos?
```

### Verificación de que no se pisan
Los tres cuentan el tiempo sin respuesta del lead. Cuando el lead responde, la IA le asigna En Conversación o Calificado, y si los seguimientos cuelgan de En Seguimiento, deja de cumplir la Condición Tag. Calificado, Derivado, No Fit y No Contactar comparten grupo excluyente con En Conversación y En Seguimiento: al asignarse cualquiera, la serie se corta.

---

## PLANTILLAS DE WHATSAPP (Meta) TRABAJADAS EN ESTA SESIÓN

Caso de envío: a confirmar con Prometheo para esta cuenta. En G&D se confirmó "1 a 1 manual" (Conexiones > WhatsApp > Plantillas > crear > esperar aprobación de Meta > enviar desde el chat o el lead). Queda pendiente confirmar si los seguimientos B y C, que caen fuera de la ventana de 24 hs, salen con una plantilla aprobada o como mensaje libre (ver Pendientes).

Categoría usada y su criterio:
- Marketing: reenganche de conversación colgada.

Plantillas:

### sin_respuesta_24hs (para el Seguimiento B)
- Categoría: Marketing
- Idioma: Spanish
- Formato: Solo texto
- Cuerpo:
```
Hola {{1}}, soy Paula de EDFAN de nuevo. Si me contás para qué ambiente o superficie es, te recomiendo la opción que mejor te sirve. ¿Seguimos?
```
- Variable {{1}}: Nombre. Ejemplo para Meta: Martín

### sin_respuesta_72hs (para el Seguimiento C)
- Categoría: Marketing
- Idioma: Spanish
- Formato: Solo texto
- Cuerpo:
```
Hola {{1}}, soy Paula de EDFAN de nuevo. Esta es mi última consulta por ahora, para no molestarte. Si seguís buscando revestimientos, ¿retomamos?
```
- Variable {{1}}: Nombre. Ejemplo para Meta: Martín

Nota de vinculación: al usar una plantilla en un seguimiento, cada {{n}} de la plantilla se mapea a una variable del lead desde la configuración de Prometheo. No se edita el cuerpo de la plantilla aprobada por Meta después de su aprobación. El texto del mensaje del seguimiento y el cuerpo de la plantilla tienen que ser idénticos.

Plantilla preexistente del cliente: `activacion_conver` (Marketing, Pendiente). No se vincula a este flujo.

---

## TESTING

Pruebas, en este orden:
1. **La tag no depende del mensaje.** Lead con la variable de moderador forzada a "Sí" que deja de responder: no recibe el A, pero su tag tiene que pasar a En Seguimiento. Y un lead sin forzar: a las 4 horas tiene que estar en En Seguimiento y recibir el A. Si el A no sale porque la tag todavía no se asignó, avisar a ITESA (pendiente 1).
2. Lead que no responde nunca: recibe A a las 4hs, B a las 24hs y C a las 72hs.
3. Lead que responde después del A: no recibe el B.
4. Lead con la variable forzada a "Sí": no recibe A ni B; sí recibe el C a las 72hs.
5. Lead que dice "lo veo y te aviso": pasa a En Seguimiento sin esperar al A.
6. Lead que pide no ser contactado: pasa a No Contactar, el asistente se apaga y no recibe ningún seguimiento más.
7. Que "/Nombre" llegue con el nombre real y no como texto literal. Probar con un contacto sin nombre cargado.
8. Que el A llegue como mensaje libre dentro de la ventana de 24 hs.
9. Que el B y el C esperen al lunes si su tiempo se cumple fuera de la ventana horaria (por ejemplo, un sábado a la noche).

---

## PENDIENTES Y NOTAS PARA ITESA (Prometheo)

1. **¿En qué momento exacto asigna la plataforma En Seguimiento por falta de respuesta?** El A (4 horas) tiene que encontrar la tag ya asignada. Se verifica con la prueba 1.
2. **Plantilla o mensaje libre fuera de la ventana de 24 hs** para los seguimientos B y C: confirmar con Prometheo cuál de las dos salidas usa la plataforma.
3. **Variable "/Nombre"**: confirmar que toma el nombre del contacto, y con qué variable queda asociada la {{1}} de las plantillas.
4. **Aprobación de Meta**: 24 a 48 hs, sin garantía. Las plantillas se crean antes de cargar los seguimientos B y C.
5. **Leads con Reasignación A Moderador en "Sí"**: hoy no reciben A ni B. Definir con el cliente si se quiere una variante con gestión humana, como el Seguimiento B de G&D (categoría Utility, más barata que Marketing).
6. **Condición "Contiene · No" en contactos creados antes de la variable**: pueden tenerla vacía y quedar fuera de A y B. Confirmar con ITESA si el valor por defecto se aplica a los contactos existentes.

---

## PARA LA GUÍA PRINCIPAL (fuera del alcance de esta, la metodología lo pide)

- Un seguimiento disparado solo por **Calificado** y otro solo por **Hot Lead**, con un tag disparador cada uno. Ahí va el mensaje del showroom en CABA, que habla de lo que ese estadío ya sabe del lead. Es la fuga principal en los tres tableros de IC.
- El prompt de **Calificado** con la regla literal de EDFAN Productos (obligatorios y sumas), la misma que usa la salida de En Conversación.
- Revisar el checklist "para que el tablero de IC no descubra lo previsible" de la Guía de Implementador (metodología v1.25).
