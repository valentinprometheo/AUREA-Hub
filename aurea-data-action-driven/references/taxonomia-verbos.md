# Taxonomía de verbos (sellos)

Seis verbos. Si una acción no entra en ninguno, la acción no está bien formulada.
Los colores son **semánticos y propios de los sellos**: no usan violeta, azul ni rosa
de marca, que en el tablero son identidad y no estado (`aurea-dashboard-design`).

| Sello | Cuándo se usa | Color (fondo / texto) | Ejemplo |
|---|---|---|---|
| **Corregir** | Algo funciona mal y cuesta: prompt, regla, campaña, dato mal cargado | `#FDE8E4` / `#B42318` | Corregir · 406 leads de una consulta recibieron 4,8 mensajes |
| **Proteger** | Algo funciona bien y está en riesgo: presupuesto, anuncio ganador, calidad del número | `#FEF3C7` / `#92400E` | Proteger · el conjunto con CPL de $1.900 no se toca en la reestructura |
| **Separar** | Hay no-demanda o mezcla que ensucia el dato: inmobiliarias, proveedores, duplicados | `#E8ECF1` / `#344054` | Separar · 18% de los leads son inmobiliarias, tag propio fuera del embudo |
| **Medir** | Falta el dato para decidir; se instrumenta con fecha | `#E0F2F1` / `#0F6E6E` | Medir · 52% de las consultas sin ID de anuncio, activar UTM |
| **Decidir** | Hay dos caminos y el dato alcanza; elige Dirección | `#E9E7FB` / `#3F3A9E` | Decidir · pausar el proyecto B o bajar su presupuesto a la mitad |
| **Activar** | Hay una oportunidad sin usar: audiencia, base dormida, seguimiento | `#E3F4E8` / `#1E6B3A` | Activar · 230 hot leads sin seguimiento en 7 días, secuencia de recontacto |

## Dueños

| Dueño | Ejecuta |
|---|---|
| **AUREA** | Prompt del agente, embudos, tags, variables, tablero |
| **Ventas** | Seguimiento, recontacto, carga de resultado de contacto |
| **Marketing** | Pauta, creativos, audiencias, campañas de email y WhatsApp |
| **Dirección** | Presupuesto, prioridad de proyectos, decisiones entre caminos |

## Reglas

- *Decidir* siempre tiene dueño Dirección y muestra las dos opciones con su costo.
- *Medir* nunca es la acción por defecto: se usa solo si el chequeo de base falla.
- Una card, un verbo, un dueño. Si hacen falta dos dueños, son dos cards.
