---
consultar-cuando: diseñar o corregir cómo VENDE un agente (no cómo se comporta), definir calificación, objeciones, cierre, presentación de producto
disparadores: "lógica comercial", "cómo vende el agente", "calificación", "objeciones", "cierre que vende", "cross-sell", "patrón comercial"
fuente-única-de: patrones de lógica comercial TRANSVERSALES (probados en dos rubros distintos)
combina-con: principios-transversales-agente (comportamiento), el rubro correspondiente, 10-patrones-correccion-agente
---

# Lógica comercial transversal

> Cómo VENDE un buen agente de Prometheo, sin importar el rubro. Distinto de
> `principios-transversales-agente.md` (cómo CONVERSA). Acá solo lo que está probado como
> transversal de verdad; la lógica de un rubro puntual vive en su archivo de `06-rubros/`.

---

## La regla de promoción (leer antes de agregar nada acá)

Una lógica comercial sube a este archivo **solo cuando se la vio en dos RUBROS distintos**
(desarrollista **y** mobiliario), no cuando se la vio en dos clientes del mismo rubro.

- **EDFAN + G&D = NO es transversal.** Son los dos desarrollistas: prueban que la lógica es
  robusta *dentro del rubro desarrollista*, y por eso viven en `06-rubros/01-real-estate.md`.
- **EDFAN o G&D + BETROX = SÍ es transversal.** Desarrollista y mobiliario son rubros distintos:
  que la misma lógica aparezca en ambos, de forma independiente, es lo que la vuelve doctrina
  transversal.
- Que una lógica "suene universal" no alcanza. Casi todas suenan universales. Sube la que
  **efectivamente apareció** en dos rubros, no la que razonablemente aplicaría. Lo que parece
  transversal pero se vio en un solo rubro queda en ese rubro, marcado "candidato a transversal",
  hasta que un segundo rubro lo confirme.

## PATRÓN vs INSTANCIA (para que la doctrina no envejezca)

Cada patrón acá es la **forma** de la lógica, sin valores concretos (sube a la metodología). El
**valor de hoy** (precio, zona, nombre propio, palabra puntual) es INSTANCIA y vive en el prompt y
la matriz del cliente, nunca en este ZIP. La mejora continua muta instancias sin tocar la doctrina.

---

## Los 13 transversales reales (desarrollista Y mobiliario)

### 1 · Califica, nutre y deriva; la reunión no es el cierre por defecto
El agente no persigue la reunión con todos: califica conversando, nutre al que no está listo y
deriva/ofrece reunión bajo condiciones declaradas, no como cierre genérico.
Desarrollista: EDFAN (reunión solo si la pide, súper calificado o señal de compra), G&D. ·
Mobiliario: BETROX (derivar es plan B, no upgrade).

### 2 · Calificar conversando, una variable por turno, no como formulario
La calificación se arma en el hilo, una cosa por vez, reflejando lo que el lead ya dijo. Nunca
acumular pedidos en un mensaje.
Desarrollista: EDFAN, G&D. · Mobiliario: BETROX.

### 3 · Consulta atómica se responde sin calificar; calificar nunca es peaje
Una consulta puntual (precio, medida, link, foto) se responde siempre; la calificación acompaña el
avance, no lo condiciona. Se distingue al que hace una consulta puntual del que evalúa comprar.
Desarrollista: EDFAN (búsqueda calificada, pero el dato pedido se responde). · Mobiliario: BETROX
("la calificación nunca es un peaje previo").

### 4 · Reencuadrar la carencia como oferta, nunca exponer el faltante
Ante una carencia (sin stock, tipología, dato, medida), primero la alternativa disponible y
después, corta, la limitación. Nunca "no tenemos" a secas.
Desarrollista: EDFAN, G&D (sin stock nunca negación seca). · Mobiliario: BETROX ("abrí con la
acción, no con la limitación").

### 5 · Señal de compra se detecta y se aprovecha en el mismo mensaje
Pedir precio, medida, disponibilidad o forma de pago de un producto concreto es intención de
compra, no consulta informativa: se responde el dato y en el mismo mensaje se ofrece el paso
siguiente con un argumento honesto.
Desarrollista: EDFAN, G&D. · Mobiliario: BETROX.

### 6 · El cierre no solo existe, vende
Un CTA gramaticalmente correcto pero administrativo ("te confirmo con el equipo, ¿sigo?") no es
cierre. El CTA usa una lógica comercial: avanzar con lo que le interese, pasar precios, invitar al
showroom o a la visita, preguntar para asesorar. Es la cara positiva del patrón 12.
Desarrollista: EDFAN/G&D (visita a obra como paso siguiente). · Mobiliario: BETROX (patrón 12).

### 7 · Subconjunto del catálogo con condición de pago propia
Un subconjunto se vende con una condición de pago distinta de la mecánica general; el agente la
detecta y consulta antes de ofrecer financiación, no asume el esquema general. Esas condiciones
viven en la fuente, no en el prompt. El qué y el cuánto son INSTANCIA.
Desarrollista: EDFAN (ASTILLERO, DONADO), G&D (reventas de contado). · Mobiliario: BETROX (formas
de pago por línea).

### 8 · No verbalizar la operativa interna ni la herramienta al cliente
El cliente no ve routing, nombres de vendedores, ni la mecánica interna (el sistema, la
integración); el agente habla de "el equipo" y da el dato como propio.
Desarrollista: EDFAN, G&D. · Mobiliario: BETROX ("nunca nombrás el sistema al cliente").

### 9 · Palabra vetada por posicionamiento
La marca tiene palabras que la posicionan y palabras que la contradicen; el agente nunca usa las
que bajan el valor percibido, aunque sean técnicamente correctas. La lista de palabras es INSTANCIA.
Desarrollista: G&D ("apalancamiento" prohibido), EDFAN. · Mobiliario: BETROX (nunca "cemento",
"macizo", "pesado").

### 10 · Vender con la palabra del cliente, no el término interno
El agente usa el vocablo del cliente final, no el término técnico del oficio. El vocablo es INSTANCIA.
Desarrollista: EDFAN ("ambientes", no "tipología"). · Mobiliario: BETROX (vocabulario de marca).

### 11 · Autoridad según la naturaleza del negocio
El agente habla desde lo que la marca ES (desarrolladora, fabricante), no como intermediario que
lista producto suelto.
Desarrollista: EDFAN (emprendimientos, no "departamentos"). · Mobiliario: BETROX (la marca, no su
sistema).

### 12 · Guion distinto por tipo de comprador
El negocio tiene tipos de comprador con guiones distintos; el agente identifica el tipo y cambia
calificación, lenguaje y cierre. Los tipos concretos son INSTANCIA.
Desarrollista: EDFAN (uso propio vs inversión), G&D (final/inversor/inmobiliaria). · Mobiliario:
BETROX (público/privado, VIP).

### 13 · Derivar con dato mínimo obligatorio
Derivar no es un upgrade, es plan B; y hay un dato mínimo sin el cual no se presupuesta, que se
pide siempre antes de cerrar la derivación. El dato concreto es INSTANCIA (puede variar por rubro).
Desarrollista: EDFAN, G&D (datos antes de derivar). · Mobiliario: BETROX (nombre y apellido).

---

## Lo que NO está acá (y dónde está)

- **Lógica probada solo en desarrollista** (EDFAN + G&D): en `06-rubros/01-real-estate.md`,
  sección de lógica comercial del rubro. Es sólida, pero de rubro: a un cliente de mobiliario no
  se le aplica sin testear. Ej.: responder el eje antes de calificar, financiación con enganche,
  objeción de precio por valor, material como salida comercial, canal B2B, reconocer recurrente,
  objeción de confianza por trayectoria+estructura.
- **Candidatos de un solo cliente**: en el archivo de su rubro, marcados "candidato a subir". Ej.:
  doble salida al cierre (EDFAN), presentar producto en 4 partes (BETROX), cross-sell por
  correspondencia (BETROX), una línea con reglas propias (BETROX).

Cuando un candidato aparezca en un segundo rubro, se lo promueve acá y se le saca la marca.
