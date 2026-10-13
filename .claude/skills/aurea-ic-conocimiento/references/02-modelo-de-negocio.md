# 02 · Modelo de negocio, precios y go-to-market

Leyenda de estado: **[VIGENTE]** confirmado por Valen · **[A VALIDAR]** en uso pero sin cerrar · **[REFERENCIA]** valor de referencia, no promesa · **[DEROGADO]** no usar.

## IC dentro del Ecosistema Comercial 360 con IA
Orden del círculo (siempre en este orden):
1. **Marketing · Generación de demanda.** Pauta digital (Meta Ads, Google Ads, LinkedIn Marketing, Email Marketing, WhatsApp Marketing) y generación de contenido (con IA, sin IA o híbrido; la producción la hace un partner). Servicio recurrente.
2. **Ventas · Calificación de demanda y ventas.** Consultoría e implementación de CRM con IA (Prometheo), agentes IA y chat omnicanal. Implementación de 3 meses. Opcional: Mejora Continua.
3. **Inteligencia Comercial · Métricas e insights.** Servicio recurrente.

Rol estratégico de IC: es el producto que **arrastra a los otros**. Al ver insights accionables, el cliente pide Marketing, Ventas o Mejora Continua. [VIGENTE]

Diferencial del 360 frente a la competencia: **servicios integrales, con un solo equipo**. AUREA 360 genera, convierte y mide de punta a punta; una agencia trae el clic sin saber si compró; un CRM solo guarda el contacto.

## Precios
### Inteligencia Comercial
- USD 200 por mes con un canal incluido + USD 50 por canal extra (Google Ads, Email, WhatsApp, LinkedIn). Ejemplo: Meta + Google + Email = USD 300 por mes. [A VALIDAR: se fijó sin cálculo y se busca justificarlo]
- Contrato anual sugerido; cadencia quincenal. [REFERENCIA]
- **Tensión abierta:** Mejora Continua Pro (USD 300) incluye 1 reporte mensual de IC con 2 canales de marketing. Si alguien pregunta por qué IC sola cuesta USD 200, la respuesta todavía no está cerrada. [A VALIDAR]

### Ventas (base del ecosistema)
- Consultoría e implementación: USD 850 por mes durante la implementación (3 meses). [VIGENTE]
> Fuente única de costos de plataforma, IA y Meta: skill `aurea-hub-costos-rentabilidad`
> (criterio de costos v1, 13/10/2026). Si este archivo difiere, manda esa.

- Licencia de la plataforma: **plan recomendado Enterprise, USD 149 por mes**. Planes de
  Prometheo: Basic USD 49, Pro USD 99, Enterprise USD 149; ninguno incluye IA. En piezas se dice
  "plan recomendado: Enterprise", no "desde USD 149". [VIGENTE]
- Consumo variable de IA: **desde USD 0,30 por conversación, medido por cuenta; para proyectar,
  USD 0,40** (medido en clientes: USD 0,34 a 0,48). [VIGENTE]
- Mensajes de WhatsApp: los cobra Meta directo al cliente, en pesos (respuesta ARS 37,68,
  marketing ARS 89,56, con 1.000 respuestas gratis por mes). Va aparte, como gasto de marketing. [VIGENTE]
- Escenarios mensuales (IA a USD 0,40 con 20% de margen + Enterprise, Meta aparte): 216 leads ≈
  USD 273; 433 ≈ USD 398; 866 ≈ USD 648. [REFERENCIA]
- Escenarios de bajo volumen, recalculados con el mismo criterio: 50 conversaciones por mes ≈
  USD 173; 100 conversaciones ≈ USD 197 (licencia + IA; Meta aparte). [CÁLCULO]
- Rentabilidad vs atención a mano (USD 1.200 un puesto, USD 2.400 en el escenario alto):
  **ahorro de 67% a 77%**. Rangos, no promesas. [REFERENCIA]
- [DEROGADO 13/10/2026] "Licencia USD 150" (presupuesto DRAKON), "desde USD 149" como piso,
  escenarios de USD 170 a 210 "con mensajes de Meta" y "~80% menos": calculados con USD 0,30 y
  con Meta incluido en dólares.

### Mejora Continua (opcional, recurrente o por franja de tiempo)
- **Start · Estabilidad:** USD 200 por mes. Afinar al agente, detectar errores, informe mensual, correcciones por prioridad. [VIGENTE]
- **Pro · Escalabilidad:** USD 300 por mes. Cobertura completa, reporte quincenal, funciones nuevas, más canales, **1 reporte de IC al mes con 2 canales de marketing integrados**; más canales o reportes se cobran aparte. [VIGENTE]
  - Ver hallazgo del 13/10/2026: el criterio de costos describe ese informe como "de IC del CRM (lo que el cliente contrató, no de marketing)". [A CONFIRMAR]
- **Regla de escalabilidad:** cada función nueva que se active (agendado, campañas) se comunica antes con su costo estimado en tokens y en Meta. Start tiende a bajar el gasto; Pro lo sube porque suma funciones. [VIGENTE]

### Marketing
- Precio a medida según canales y frecuencia. **No publicar precios de marketing** en piezas comerciales. [VIGENTE]

### Reglas para modelar precio y mercado [VIGENTE]
- El precio de lista contempla IVA 21% e Ingresos Brutos aunque hoy no se paguen; la diferencia se muestra como descuento. Evita arrancar con un precio bajo difícil de subir.
- El tamaño de mercado se presenta como **"estimado hoy"**.
- Los costos de construir IC los define el CTO: **no suponerlos** en proyecciones.
- Etiquetar cada número como real, de estudio, interpretación, supuesto o faltante.

## Canales de venta
- **Agencias de marketing (partners):** el canal de foco hoy. Muchas contactadas y muchas por contactar. El cliente final paga el precio real de IC; la agencia cobra una comisión por traerlo. [VIGENTE]
  - Comisión del programa "Sé Partner": Oro 20% (3 a 30 registros pagos), Zafiro 30% (31 a 200), Diamante 40% (más de 200), mensual mientras la cuenta esté activa. [REFERENCIA]
  - AUREA **no** le cobra a las agencias un precio por cliente (era un supuesto de un estudio). [DEROGADO como modelo]
  - Relato a la agencia: aliado, no sustituto. *"Vos ponés creativos y estrategia; nosotros el dato de venta que te vuelve indispensable frente a Meta y a la IA."*
- **Venta directa:** después del primer año, IC probablemente se venda también sin agencias. [VIGENTE]
- **Dueño del insight:** AUREA administra el Prometheo del cliente; si contrata el servicio, el acceso al dato de venta queda cubierto por contrato. [A VALIDAR en contrato]

## Validación y go-to-market (plan de acción)
IC ya existe a mano y tiene clientes que lo ven: el product-market fit no arranca de cero. Antes de escalar hay que probar tres cosas:
1. Que **cambia decisiones** del cliente.
2. Que **se paga** (alguien lo compra a precio de lista).
3. Que **se puede entregar sin sumar horas** (escala sin crecer el equipo al mismo ritmo).

Plan en cinco fases, cada una con una señal para avanzar y una regla para corregir. Señal de referencia de PMF: test de Sean Ellis (40% de usuarios "muy decepcionados" si dejara de existir). Defensa principal frente a agencias que repliquen el producto: el dato de venta vive en el CRM que administra AUREA, y el criterio comercial por rubro.

> El detalle de las cinco fases, la proyección de mercado y el registro de supuestos están en los documentos de la conversación "Inteligencia Comercial · Plan de acción". Integrarlos aquí cuando Valen los traiga (ver `hallazgos.md`).

## Estrategia de entrada con clientes actuales
**El informe de demanda como gancho.** Se arma con lo que ya hay en Prometheo (no depende de Meta), se muestra el valor y eso abre la puerta a pedir el export de Meta para el cruce completo. Caso: EDFAN Real Estate (ver `05-casos-y-evidencia.md`).
