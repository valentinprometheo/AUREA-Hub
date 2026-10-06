"""Datos ILUSTRATIVOS (DEMO) del tablero de PAVIR.

Todo es modelado: sirve para mostrar la estructura y las lecturas que habilita
el tablero. Los totales se calculan acá para que ninguna cifra se contradiga
entre pestañas.
"""

PERIODO = "Septiembre 2026"
PREV = "agosto"
ACT = "30 sep 2026"

# ---------- embudo de consultas (Prometheo) ----------
CONSULTAS = 4950
RESPONDIO = 4010
IDENTIFICO = 3270
CALIFICADA = 2870
DERIVADA = 2640
SEGUIMIENTO = 890
PEDIDO_TAG = 0
PEDIDO_EVID = 214
FUGA = CALIFICADA - SEGUIMIENTO  # 1.980 calificadas sin seguimiento

# detalle de la fuga (modo Avanzado)
FUGA_LINEA = [("Puertas de acero", 1030), ("Ventanas", 590), ("Pivotantes", 360)]
FUGA_TIPO = [("Consumidor final", 1640), ("Comercio que quiere revender", 250), ("Arquitecto u obra", 90)]
FUGA_ZONA = [("AMBA", 690), ("Centro", 450), ("Litoral", 330), ("Cuyo", 260), ("NOA, NEA y Sur", 250)]
FUGA_EDAD = [("Menos de 7 días", 520), ("7 a 30 días", 860), ("Más de 30 días", 600)]
FUGA_CORTE = [("Derivada, el distribuidor nunca respondió", 1120), ("Derivada, respondió sin fecha", 630), ("No se derivó: falta la zona", 230)]
FUGA_ORIGEN = [("Orgánico (Instagram y web)", 1040), ("Meta Ads", 640), ("Referido", 300)]
FUGA_URGENTE = 610

# base curada
NO_DEMANDA = [("Posventa y consulta técnica", 1089), ("Proveedores que ofrecen algo", 96), ("Búsqueda de empleo", 54), ("Número equivocado o spam", 41)]
NO_DEM_TOT = sum(v for _, v in NO_DEMANDA)  # 1.280
BASE_CURADA = CONSULTAS - NO_DEM_TOT  # 3.670

# tipo de contacto (B2B / B2C)
TIPO = [("Consumidor final", 3960), ("Comercio que quiere revender", 312), ("Arquitecto o constructora", 160), ("Distribuidor actual (pedido o reclamo)", 278), ("Sin dato", 240)]

# ---------- origen de la demanda ----------
INBOUND = [
    # grupo, canal, consultas, estado
    ("Pago", "Meta Ads", 1560, "on"),
    ("Pago", "Google Ads", 0, "off"),
    ("Orgánico", "Instagram", 1140, ""),
    ("Orgánico", "Web", 790, ""),
    ("Orgánico", "Facebook y YouTube", 345, ""),
    ("Directo", "Referido o boca a boca", 890, ""),
    ("Directo", "Sin origen identificado", 225, "miss"),
]
PUERTA = [("WhatsApp", 3020), ("Instagram Direct", 890), ("Mail", 890), ("Teléfono", 150)]

# ---------- red y venta (export de Producí) ----------
RED = 700
ACTIVOS = 500
PASIVOS = 200
PROV_ACT = 15
PROV_PAS = 7
SIN_DEUDA = 616
DEUDA_AL_DIA = 53
VENCIDOS = 31
CON_DEUDA = 84
DEUDA_M = 42.8
VENCIDO_M = 11.9
PEDIDOS = 384
COBRADOS = 341
DESPACHADOS = 335
VENTAS_M = 73.8
TOCA_COMPRAR = 126
DORMIDOS = 73
SOLO_PUERTAS = 148
RECOMPRA = 62

MESES = ["oct", "nov", "dic", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep"]
H_CONS = [4850, 4700, 3900, 3700, 4500, 5600, 5900, 6100, 5300, 5050, 4670, 4950]
H_CALIF = [2810, 2720, 2240, 2130, 2600, 3260, 3430, 3550, 3070, 2930, 2710, 2870]
H_DERIV = [2580, 2500, 2060, 1960, 2390, 3000, 3150, 3260, 2820, 2700, 2490, 2640]
H_PED = [372, 360, 300, 285, 345, 486, 512, 512, 452, 420, 352, 384]
H_VENT = [62.1, 61.0, 52.4, 50.6, 62.4, 89.9, 96.8, 98.3, 88.1, 83.2, 68.4, 73.8]
H_OBJ = [64.0, 63.0, 55.0, 53.0, 62.0, 88.0, 92.0, 94.0, 86.0, 82.0, 72.0, 77.0]
H_REC = [60, 59, 55, 54, 56, 64, 67, 66, 64, 63, 61, 62]
H_COB = [88, 87, 85, 85, 86, 90, 91, 90, 89, 89, 88, 89]
H_DEUDA = [43.0, 41.0, 38.0, 37.5, 41.5, 61.4, 59.0, 54.0, 49.0, 47.0, 44.6, 42.8]
H_VENC = [9.8, 9.1, 8.4, 8.9, 10.2, 14.6, 15.1, 13.8, 12.4, 12.0, 12.6, 11.9]
H_CDEU = [80, 78, 74, 72, 79, 98, 101, 96, 90, 87, 86, 84]
H_NVENC = [28, 27, 25, 26, 30, 38, 40, 37, 34, 33, 32, 31]
H_TERM = [88, 89, 90, 89, 87, 84, 83, 85, 86, 87, 87, 88]
H_LINEA = {  # ventas por línea, millones
    "Puertas de acero": [38.5, 37.8, 32.0, 31.1, 38.4, 55.2, 59.0, 60.1, 54.0, 51.0, 42.1, 45.0],
    "Ventanas": [15.0, 14.9, 13.0, 12.4, 15.1, 21.8, 23.6, 23.9, 21.3, 20.1, 16.4, 17.9],
    "Pivotantes": [8.6, 8.3, 7.4, 7.1, 8.9, 12.9, 14.2, 14.3, 12.8, 12.1, 9.9, 10.9],
}

# tags por embudo, últimos 4 meses (jun, jul, ago, sep)
EMBUDOS = [
    ("Recepción y calificación", "auto", "Lo conduce el agente: se carga solo", [
        ("consulta_nueva", [5300, 5050, 4670, 4950]),
        ("calificada", [3070, 2930, 2710, 2870]),
        ("derivado_distribuidor", [2820, 2700, 2490, 2640]),
        ("consulta_tecnica", [1150, 1100, 1020, 1089]),
        ("no_fit", [210, 200, 190, 205]),
    ]),
    ("Seguimiento y venta", "man", "Lo marca el equipo a mano", [
        ("pidio_cotizacion", [440, 425, 390, 410]),
        ("visita_agendada", [140, 131, 118, 126]),
        ("objecion_precio", [70, 66, 58, 61]),
        ("no_concreto", [6, 5, 3, 4]),
        ("pedido_reportado", [0, 0, 0, 0]),
    ]),
    ("Red B2B · comercios", "none", "Sin embudo propio: el tag existe, el recorrido no", [
        ("comercio", [290, 301, 285, 312]),
        ("alta_distribuidor", [3, 2, 4, 2]),
    ]),
    ("Cobranza", "man", "Lo marca administración a mano", [
        ("estado_cuenta_enviado", [52, 49, 47, 44]),
        ("pago_confirmado", [18, 15, 14, 12]),
    ]),
]
TAGS_AUTO = 15240
TAGS_MAN = 2480

# uso de cada embudo: (nombre, quién, debería, tiene, auto%)
USO_EMB = [
    ("Recepción y calificación", "Agente · automático", 4950, 4535, "auto"),
    ("Seguimiento y venta", "Equipo · manual", 2640, 520, "man"),
    ("Cobranza", "Administración · manual", 84, 56, "man"),
    ("Cierre · pedido confirmado", "Equipo · manual", 214, 0, "man"),
    ("Red B2B · comercios", "Sin embudo propio", 312, 0, "none"),
]

# ---------- corredores (moderador en Prometheo + pedidos de Producí) ----------
# nombre, zona, cartera, conversaciones, visitas marcadas, pedidos, ventas M, objetivo M,
# recompraron 30d, datos completos %, (variable que más falta, % vacía), respuesta min, vencidos
CORR = [
    ("AMBA Norte · CABA", "CABA, Vicente López, San Isidro", 52, 168, 21, 44, 9.2, 8.5, 37, 86, ("Momento de obra", 22), 6, 1),
    ("AMBA Oeste", "Morón, Merlo, Moreno", 48, 152, 18, 41, 8.4, 8.0, 33, 81, ("Cantidad de puertas", 28), 9, 2),
    ("AMBA Sur", "Lomas, Quilmes, Berazategui", 40, 121, 6, 30, 5.6, 6.5, 22, 58, ("Zona de obra", 46), 24, 4),
    ("Buenos Aires Interior", "Mar del Plata, Bahía Blanca", 36, 98, 8, 27, 5.0, 5.5, 21, 74, ("Forma de pago", 31), 14, 2),
    ("Litoral", "Santa Fe, Entre Ríos", 46, 133, 12, 34, 6.9, 7.0, 28, 77, ("Momento de obra", 35), 11, 3),
    ("Centro", "Córdoba", 44, 140, 15, 36, 7.4, 7.0, 30, 84, ("Resultado de la visita", 25), 8, 2),
    ("Cuyo", "Mendoza, San Juan", 34, 74, 3, 20, 3.9, 6.0, 15, 49, ("Resultado de la visita", 61), 38, 5),
    ("Norte", "Salta, Jujuy", 30, 92, 14, 26, 5.2, 4.5, 23, 88, ("Forma de pago", 18), 7, 1),
    ("NOA", "Tucumán, Santiago del Estero", 32, 88, 9, 25, 4.6, 5.0, 19, 72, ("Cantidad de puertas", 33), 15, 3),
    ("NEA", "Chaco, Corrientes, Misiones", 30, 61, 2, 17, 3.0, 5.0, 12, 46, ("Zona de obra", 58), 41, 5),
    ("Comahue", "Neuquén, Río Negro", 33, 104, 11, 28, 5.0, 4.6, 23, 82, ("Momento de obra", 24), 10, 2),
    ("Patagonia Sur", "Chubut, Santa Cruz", 26, 70, 7, 24, 4.5, 4.4, 17, 79, ("Cantidad de puertas", 26), 13, 1),
]
SIN_CORREDOR = 49
VARS_CORR = ["Zona de obra", "Línea", "Cantidad de puertas", "Momento de obra", "Forma de pago", "Resultado de la visita"]
# clientes que recompraron / en ventana sin pedido (muestra por corredor)
RECOMPRARON = {
    "AMBA Norte · CABA": (["Corralón Libertador", "Aberturas Núñez", "Materiales Olivos"], ["Ferretería Saavedra", "Corralón Munro"]),
    "AMBA Oeste": (["Corralón del Oeste", "Aberturas Haedo", "Materiales Merlo"], ["Corralón Paso del Rey"]),
    "AMBA Sur": (["Ferretería Banfield", "Corralón Quilmes"], ["Aberturas Adrogué", "Materiales Varela", "Corralón Burzaco"]),
    "Buenos Aires Interior": (["Aberturas MdP Centro", "Corralón Bahía"], ["Materiales Tandil", "Corralón Necochea"]),
    "Litoral": (["Aberturas Rosario", "Corralón Paraná", "Vidriería Rafaela"], ["Materiales Concordia", "Corralón Gualeguaychú"]),
    "Centro": (["Ferretería Centro", "Corralón Villa María", "Aberturas Río Cuarto"], ["Materiales Carlos Paz"]),
    "Cuyo": (["Casa Mendoza", "Corralón San Juan"], ["Aberturas Godoy Cruz", "Materiales Luján de Cuyo", "Corralón Maipú"]),
    "Norte": (["Corralón Salta Centro", "Aberturas Jujuy", "Materiales Tartagal"], ["Corralón Orán"]),
    "NOA": (["Corralón Norte", "Ferretería Yerba Buena"], ["Aberturas Santiago", "Materiales Tafí Viejo"]),
    "NEA": (["Obras y Aberturas", "Corralón Corrientes"], ["Materiales Posadas", "Aberturas Resistencia", "Corralón Oberá"]),
    "Comahue": (["Materiales Sur", "Corralón Cipolletti", "Aberturas Roca"], ["Corralón Plottier"]),
    "Patagonia Sur": (["Corralón Trelew", "Aberturas Comodoro"], ["Materiales Río Gallegos", "Corralón Madryn"]),
}

# ---------- Meta Ads: campaña › conjunto › anuncio (Meta + Prometheo) ----------
ADS = [
    dict(camp="Puertas de acero", conj="Intereses · Construcción", code="VID_PuertaClasicaSeguridad_IG", nm="Video de puerta Clásica de seguridad",
         gasto=70000, alc=96000, imp=206000, ctr=1.7, conv_meta=262, cons=240, resp=204, ident=170, calif=120, deriv=111, b2b=9, cotiz=46, seg=38, ped=9),
    dict(camp="Puertas de acero", conj="Intereses · Construcción", code="EST_PavirPremiumTerminacion_WPP", nm="Imagen de terminación PAVIR premium",
         gasto=70000, alc=74000, imp=158000, ctr=1.4, conv_meta=214, cons=200, resp=166, ident=131, calif=88, deriv=80, b2b=6, cotiz=41, seg=27, ped=6),
    dict(camp="Puertas de acero", conj="Retargeting · visitó la web", code="VID_PuertaLujanCerradura_RET", nm="Video de puerta Luján con cerradura",
         gasto=60000, alc=38000, imp=104000, ctr=2.1, conv_meta=201, cons=190, resp=175, ident=150, calif=112, deriv=106, b2b=8, cotiz=52, seg=41, ped=11),
    dict(camp="Puertas de acero", conj="Intereses · Reformas", code="CAR_PuertaAceroColores_BROAD", nm="Carrusel de colores de puerta de acero",
         gasto=60000, alc=102000, imp=212000, ctr=1.3, conv_meta=207, cons=190, resp=150, ident=118, calif=76, deriv=70, b2b=3, cotiz=24, seg=18, ped=3),
    dict(camp="Ventanas PVC", conj="Intereses · Obra nueva", code="VID_VentanaPVCAhorro_IG", nm="Video de ventana PVC y ahorro de energía",
         gasto=60000, alc=84000, imp=170000, ctr=1.5, conv_meta=181, cons=170, resp=146, ident=121, calif=88, deriv=81, b2b=5, cotiz=33, seg=22, ped=4),
    dict(camp="Ventanas PVC", conj="Broad · consumidor final", code="CAR_VentanaPVCGenerico_BROAD", nm="Carrusel de ventana PVC genérica",
         gasto=100000, alc=150000, imp=300000, ctr=1.2, conv_meta=338, cons=300, resp=198, ident=120, calif=57, deriv=49, b2b=2, cotiz=14, seg=9, ped=1),
    dict(camp="Pivotantes", conj="Intereses · Arquitectura y diseño", code="VID_PivotanteWallPanel_IG", nm="Video de pivotante Wall Panel",
         gasto=55000, alc=61000, imp=131000, ctr=1.6, conv_meta=161, cons=150, resp=128, ident=97, calif=66, deriv=58, b2b=10, cotiz=31, seg=19, ped=3),
    dict(camp="Pivotantes", conj="Lookalike · distribuidores", code="EST_PivotanteExhibidor_LAA", nm="Imagen del exhibidor de pivotantes para el salón",
         gasto=45000, alc=52000, imp=98000, ctr=1.1, conv_meta=128, cons=120, resp=108, ident=92, calif=48, deriv=19, b2b=46, cotiz=22, seg=20, ped=2),
]
for a in ADS:
    a["imp"] = round(a["imp"] / 5, -2)
    a["alc"] = round(a["alc"] / 5, -2)
    a["clics"] = round(a["imp"] * a["ctr"] / 100)
    a["frec"] = a["imp"] / a["alc"]
    a["cpc"] = a["gasto"] / a["clics"]
    a["pcal"] = round(100 * a["calif"] / a["cons"])
    a["ccal"] = round(a["gasto"] / a["calif"])

KEYS = ["gasto", "alc", "imp", "clics", "conv_meta", "cons", "resp", "ident", "calif", "deriv", "b2b", "cotiz", "seg", "ped"]


def agg(rows):
    t = {k: sum(r[k] for r in rows) for k in KEYS}
    t["pcal"] = round(100 * t["calif"] / t["cons"])
    t["ccal"] = round(t["gasto"] / t["calif"])
    t["ctr"] = 100 * t["clics"] / t["imp"]
    t["frec"] = t["imp"] / t["alc"]
    t["cpc"] = t["gasto"] / t["clics"]
    return t


META = agg(ADS)
CAMPS = {}
CONJS = {}
for a in ADS:
    CAMPS.setdefault(a["camp"], []).append(a)
    CONJS.setdefault(a["conj"], []).append(a)

# ---------- criterio comercial ----------
CRIT_BASE = 4950
CRIT_PROBLEMA = 3861
CRIT_IMPACTO = 2030
CRIT_DISPARADOR = 2722
CRIT_CAUSA = 1436
