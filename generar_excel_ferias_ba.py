import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Ferias BA 2026 - AureaHub"

# Styles
header_font = Font(bold=True, color="FFFFFF", size=11)
header_fill = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
rubro_fill = PatternFill(start_color="D6E4F0", end_color="D6E4F0", fill_type="solid")
rubro_font = Font(bold=True, size=11, color="1F3864")
wrap = Alignment(wrap_text=True, vertical="top")
thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)

headers = [
    "Rubro AureaHub",
    "Feria / Evento",
    "Edición",
    "Fechas",
    "Lugar",
    "Organizadores",
    "Superficie / Stands",
    "Visitantes / Asistentes",
    "Sectores que participan",
    "Relevancia para AureaHub (1-5)",
    "Estado (pasada/próxima)",
    "Entrada",
    "Web oficial",
    "Notas",
]

for col, h in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    cell.border = thin_border

ferias = [
    # --- DESARROLLO INMOBILIARIO ---
    {
        "rubro": "Desarrollo Inmobiliario",
        "nombre": "Expo Real Estate Argentina",
        "edicion": "16ª edición",
        "fechas": "12-13 agosto 2026",
        "lugar": "Hilton Buenos Aires, Av. Macacha Güemes 351, Puerto Madero, CABA",
        "organizadores": "Expo Real Estate (by SG)",
        "superficie": "+150 stands, +500 expositores",
        "visitantes": "+10.000 visitantes estimados",
        "sectores": "Desarrolladores inmobiliarios, inversiones, crédito hipotecario, real estate internacional, fondos de inversión, PropTech",
        "relevancia": 5,
        "estado": "Próxima",
        "entrada": "Gratuita con acreditación previa",
        "web": "https://exporealestate.com.ar/",
        "notas": "El evento más importante de real estate en Argentina. +300 opciones de inversión, 60 workshops, +90 speakers. Congreso paralelo con auditorio para +1000 personas. YA ASISTIDA POR AUREAHUB: foco estratégico.",
    },
    {
        "rubro": "Desarrollo Inmobiliario",
        "nombre": "Expo Latam Real Estate",
        "edicion": "2026",
        "fechas": "Abril-Mayo 2026 (edición BA)",
        "lugar": "Hotel Madero, Buenos Aires",
        "organizadores": "Expo Latam Real Estate",
        "superficie": "~50 stands",
        "visitantes": "~3.000",
        "sectores": "Inversiones inmobiliarias regionales (Uruguay, Paraguay, Argentina, Miami), desarrolladores latam",
        "relevancia": 4,
        "estado": "Pasada",
        "entrada": "Gratuita con registro",
        "web": "https://www.eventbrite.com/e/expo-latam-real-estate-buenos-aires-2026-tickets-1985741441105",
        "notas": "Foco en inversión inmobiliaria latinoamericana. Complementa Expo Real Estate con enfoque regional.",
    },
    {
        "rubro": "Desarrollo Inmobiliario",
        "nombre": "Expo Construir Argentina",
        "edicion": "10ª edición",
        "fechas": "6-7 mayo 2026",
        "lugar": "Hilton Buenos Aires, Puerto Madero, CABA",
        "organizadores": "Expo Construir",
        "superficie": "+180 stands",
        "visitantes": "+8.000",
        "sectores": "Constructoras, desarrolladores, crédito hipotecario, materiales, tecnología constructiva, inversores",
        "relevancia": 4,
        "estado": "Pasada",
        "entrada": "Gratuita con acreditación",
        "web": "https://expoconstruir.com/",
        "notas": "Foco en negocios e innovación constructiva. +140 charlas. Cruce de desarrolladores con proveedores de insumos.",
    },
    # --- INMOBILIARIAS ---
    {
        "rubro": "Inmobiliarias",
        "nombre": "Expo Real Estate Argentina (sector inmobiliarias)",
        "edicion": "16ª edición",
        "fechas": "12-13 agosto 2026",
        "lugar": "Hilton Buenos Aires, Puerto Madero, CABA",
        "organizadores": "Expo Real Estate (by SG)",
        "superficie": "+150 stands (compartido con desarrollo inmobiliario)",
        "visitantes": "+10.000",
        "sectores": "Inmobiliarias, corredores, brokers, tasadores, administración de propiedades, tecnología inmobiliaria",
        "relevancia": 5,
        "estado": "Próxima",
        "entrada": "Gratuita con acreditación previa",
        "web": "https://exporealestate.com.ar/",
        "notas": "Principal punto de encuentro de inmobiliarias en Argentina. Sector clave para leads AureaHub.",
    },
    # --- MOBILIARIO ---
    {
        "rubro": "Mobiliario",
        "nombre": "Expo CAFIRA (edición agosto)",
        "edicion": "XXXVII edición",
        "fechas": "19-22 agosto 2026",
        "lugar": "La Rural, Pabellón Azul, Av. Sarmiento 2704, Palermo, CABA",
        "organizadores": "CAFIRA (Cámara de Fabricantes e Importadores de Artículos de Decoración, Regalos y Afines)",
        "superficie": "+150 empresas expositoras",
        "visitantes": "+15.000 visitantes profesionales",
        "sectores": "Muebles, decoración, iluminación, bazar, textiles hogar, velas y fragancias, outdoor",
        "relevancia": 5,
        "estado": "Próxima",
        "entrada": "Solo profesionales del sector (acreditación)",
        "web": "https://www.cafira.com/",
        "notas": "Feria B2B referente en mobiliario y decoración. AureaHub ya tiene base de expositores relevada. Edición marzo (Cafira Innova, 11-14 mar) ya pasada.",
    },
    {
        "rubro": "Mobiliario",
        "nombre": "Expo CAFIRA Innova (edición marzo)",
        "edicion": "2026",
        "fechas": "11-14 marzo 2026",
        "lugar": "La Rural, CABA",
        "organizadores": "CAFIRA",
        "superficie": "+120 empresas",
        "visitantes": "+10.000",
        "sectores": "Innovación en mobiliario, decoración, diseño de interiores",
        "relevancia": 4,
        "estado": "Pasada",
        "entrada": "Profesionales acreditados",
        "web": "https://www.cafira.com/",
        "notas": "Edición de apertura de temporada. Tendencias y lanzamientos.",
    },
    {
        "rubro": "Mobiliario",
        "nombre": "Feria de la Madera y el Mueble Argentino (FeMMA)",
        "edicion": "2ª edición",
        "fechas": "24-27 septiembre 2026",
        "lugar": "La Rural, Pabellón Ocre, CABA",
        "organizadores": "FAIMA (Federación Argentina de la Industria Maderera) + IMA (Instituto del Mueble Argentino)",
        "superficie": "1.450 m², sector B2B + retail",
        "visitantes": "~5.000 (estimado)",
        "sectores": "Muebles nacionales, madera, diseño argentino, carpintería industrial",
        "relevancia": 3,
        "estado": "Próxima",
        "entrada": "Abierta al público",
        "web": "https://feriadelmueble.com.ar/",
        "notas": "Única feria de mueble nacional en BA. Rondas de negocios, capacitación, venta directa. Sector B2B interesante para AureaHub.",
    },
    {
        "rubro": "Mobiliario",
        "nombre": "Electronics & Home Argentina / Artefacta",
        "edicion": "6ª edición",
        "fechas": "29 junio - 1 julio 2026",
        "lugar": "La Rural, CABA",
        "organizadores": "Grupo Eletrolar (CEO: Carlos Clur), PromArgentina",
        "superficie": "10.700 m², +200 stands, +700 marcas",
        "visitantes": "+10.000",
        "sectores": "Electrodomésticos, tecnología hogar, muebles y colchones (sector Artefacta: 4.000 m²), iluminación, bazar, textiles",
        "relevancia": 3,
        "estado": "En curso (termina 1 julio)",
        "entrada": "Profesional con acreditación",
        "web": "https://www.infobae.com/inhouse/2026/06/29/la-feria-del-hogar-y-la-tecnologia-abre-sus-puertas-en-la-rural-con-nuevas-propuestas/",
        "notas": "Incluye sector ARTEFACTA (muebles, colchones, deco) de 4.000 m². Samsung, TCL, Xiaomi, Springwall, Novatech entre expositores. Potencial para leads de mobiliario.",
    },
    # --- INSUMOS Y MATERIALES PARA LA CONSTRUCCIÓN ---
    {
        "rubro": "Insumos y Materiales para la Construcción",
        "nombre": "BATEV",
        "edicion": "31ª edición",
        "fechas": "24-27 junio 2026",
        "lugar": "La Rural, Av. Sarmiento 2704, Palermo, CABA",
        "organizadores": "CEDU+AEV, CAMARCO, EFCA",
        "superficie": "15.000 m²",
        "visitantes": "+30.000 (estimado)",
        "sectores": "Materiales de construcción, sistemas constructivos, maquinaria, herramientas, aberturas, pisos, revestimientos, pinturas, aislantes, sanitarios, griferías",
        "relevancia": 5,
        "estado": "Pasada (recién cerrada)",
        "entrada": "Gratuita con acreditación",
        "web": "https://www.batev.com.ar/web/",
        "notas": "LA feria de referencia del sector construcción en Argentina. AureaHub asistió. Lema 2026: 'Impulsando la industria'. Workshops, paneles, capacitación técnica.",
    },
    {
        "rubro": "Insumos y Materiales para la Construcción",
        "nombre": "Expo Construir Argentina",
        "edicion": "10ª edición",
        "fechas": "6-7 mayo 2026",
        "lugar": "Hilton Buenos Aires, Puerto Madero, CABA",
        "organizadores": "Expo Construir",
        "superficie": "+180 stands",
        "visitantes": "+8.000",
        "sectores": "Materiales, tecnología constructiva, sustentabilidad, eficiencia energética, herramientas",
        "relevancia": 4,
        "estado": "Pasada",
        "entrada": "Gratuita con acreditación",
        "web": "https://expoconstruir.com/",
        "notas": "Cruce de insumos con desarrolladores. +140 charlas técnicas y comerciales.",
    },
    # --- TRANSVERSALES (decoración/arquitectura con cruces) ---
    {
        "rubro": "Transversal (Inmobiliario + Mobiliario + Construcción)",
        "nombre": "Casa FOA Buenos Aires",
        "edicion": "40ª edición (aniversario)",
        "fechas": "1 octubre - 2 noviembre 2026",
        "lugar": "Madero Harbour, Puerto Madero, CABA",
        "organizadores": "FOA (Fondo de las Artes)",
        "superficie": "+5.000 m², +35 espacios diseñados",
        "visitantes": "+100.000 (históricamente)",
        "sectores": "Arquitectura de interiores, diseño, paisajismo, mobiliario, revestimientos, iluminación, grifería, materiales premium",
        "relevancia": 5,
        "estado": "Próxima",
        "entrada": "Paga (precio a confirmar)",
        "web": "https://www.casafoa.com/",
        "notas": "Evento insignia de diseño y arquitectura en Argentina. Edición 40 aniversario con concepto 'maximalismo'. ALTO IMPACTO: concentra todos los rubros de AureaHub (desarrolladores, inmobiliarias, mobiliario, materiales). Imprescindible.",
    },
    {
        "rubro": "Transversal (Inmobiliario + Mobiliario)",
        "nombre": "Estilo Pilar",
        "edicion": "20ª edición",
        "fechas": "18 marzo - 4 abril 2026",
        "lugar": "Cardinal Shopping, Domingo Prat 3426, Pilar del Este",
        "organizadores": "Amigos del Pilar Asociación Civil",
        "superficie": "~35 espacios expositivos",
        "visitantes": "+50.000 (históricamente)",
        "sectores": "Decoración, arquitectura, interiorismo, paisajismo, arte, mobiliario, materiales",
        "relevancia": 3,
        "estado": "Pasada",
        "entrada": "Paga",
        "web": "https://www.estilopilar.com.ar/",
        "notas": "Zona Norte GBA. Público ABC1. Concepto 'Boutique' en 2026. Destina recaudación a salud infantil. Buen networking con estudios de arquitectura y deco.",
    },
    {
        "rubro": "Transversal (Arquitectura + Construcción)",
        "nombre": "Bienal Internacional de Arquitectura de Buenos Aires",
        "edicion": "XX edición (aniversario)",
        "fechas": "5-10 octubre 2026",
        "lugar": "Museo Nacional de Bellas Artes + Centro Cultural Recoleta + Biblioteca Nacional + Casa Victoria Ocampo, CABA",
        "organizadores": "Bienal de Arquitectura de Buenos Aires",
        "superficie": "Múltiples sedes",
        "visitantes": "+20.000 (estimado)",
        "sectores": "Arquitectura, urbanismo, sustentabilidad, construcción, diseño urbano",
        "relevancia": 3,
        "estado": "Próxima",
        "entrada": "A confirmar",
        "web": "https://labienalarg.com.ar/",
        "notas": "20ª edición bajo el lema 'HABITAR'. Conferencias magistrales, debates interdisciplinarios. Más académica/institucional que comercial, pero excelente networking con estudios y desarrolladores.",
    },
]

row = 2
current_rubro = None
for f in ferias:
    if f["rubro"] != current_rubro:
        current_rubro = f["rubro"]

    ws.cell(row=row, column=1, value=f["rubro"])
    ws.cell(row=row, column=2, value=f["nombre"])
    ws.cell(row=row, column=3, value=f["edicion"])
    ws.cell(row=row, column=4, value=f["fechas"])
    ws.cell(row=row, column=5, value=f["lugar"])
    ws.cell(row=row, column=6, value=f["organizadores"])
    ws.cell(row=row, column=7, value=f["superficie"])
    ws.cell(row=row, column=8, value=f["visitantes"])
    ws.cell(row=row, column=9, value=f["sectores"])
    ws.cell(row=row, column=10, value=f["relevancia"])
    ws.cell(row=row, column=11, value=f["estado"])
    ws.cell(row=row, column=12, value=f["entrada"])
    ws.cell(row=row, column=13, value=f["web"])
    ws.cell(row=row, column=14, value=f["notas"])

    for col in range(1, 15):
        cell = ws.cell(row=row, column=col)
        cell.alignment = wrap
        cell.border = thin_border

    row += 1

# Column widths
col_widths = [28, 35, 14, 24, 42, 30, 25, 22, 50, 12, 16, 22, 40, 60]
for i, w in enumerate(col_widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

# Freeze header
ws.freeze_panes = "A2"

# --- HOJA 2: Calendario Timeline ---
ws2 = wb.create_sheet("Calendario 2026")

ws2.cell(row=1, column=1, value="Calendario de Ferias AureaHub - Buenos Aires 2026").font = Font(bold=True, size=14)

months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
ws2.cell(row=3, column=1, value="Feria / Evento").font = Font(bold=True)
for i, m in enumerate(months, 2):
    cell = ws2.cell(row=3, column=i, value=m)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal="center")

timeline = [
    ("CAFIRA Innova", {3: "11-14 MAR"}),
    ("Estilo Pilar", {3: "18 MAR", 4: "- 4 ABR"}),
    ("Expo Latam Real Estate", {4: "ABR-MAY"}),
    ("Expo Construir", {5: "6-7 MAY"}),
    ("BATEV", {6: "24-27 JUN"}),
    ("Electronics & Home / Artefacta", {6: "29 JUN", 7: "- 1 JUL"}),
    ("Expo Real Estate Argentina", {8: "12-13 AGO"}),
    ("Expo CAFIRA (agosto)", {8: "19-22 AGO"}),
    ("FeMMA (Madera y Mueble)", {9: "24-27 SEP"}),
    ("Casa FOA Buenos Aires", {10: "1 OCT", 11: "- 2 NOV"}),
    ("Bienal Arquitectura BA", {10: "5-10 OCT"}),
]

event_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
event_font = Font(bold=True, color="FFFFFF", size=9)

for idx, (name, month_data) in enumerate(timeline):
    r = 4 + idx
    ws2.cell(row=r, column=1, value=name).font = Font(bold=True, size=10)
    for month_col, label in month_data.items():
        cell = ws2.cell(row=r, column=month_col, value=label)
        cell.fill = event_fill
        cell.font = event_font
        cell.alignment = Alignment(horizontal="center")

ws2.column_dimensions["A"].width = 35
for i in range(2, 14):
    ws2.column_dimensions[get_column_letter(i)].width = 14

# --- HOJA 3: Próximas acciones ---
ws3 = wb.create_sheet("Próximas Acciones")

ws3.cell(row=1, column=1, value="Ferias Próximas - Acciones Prioritarias AureaHub").font = Font(bold=True, size=14)

action_headers = ["Prioridad", "Feria", "Fecha", "Acción sugerida", "Rubro", "Deadline acreditación"]
for col, h in enumerate(action_headers, 1):
    cell = ws3.cell(row=3, column=col, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.border = thin_border

actions = [
    ("1 - URGENTE", "Expo Real Estate Argentina", "12-13 ago 2026", "Acreditarse, preparar pitch para desarrolladores e inmobiliarias, agendar reuniones previas", "Desarrollo Inmobiliario + Inmobiliarias", "Ya disponible"),
    ("2 - URGENTE", "Expo CAFIRA (agosto)", "19-22 ago 2026", "Acreditarse. Actualizar base de expositores. Preparar propuesta B2B para fabricantes de mobiliario", "Mobiliario", "Ya disponible"),
    ("3 - ALTA", "FeMMA (Madera y Mueble)", "24-27 sep 2026", "Registrarse. Evaluar stand o asistencia exploratoria. Foco en mueble nacional", "Mobiliario", "Julio-Agosto 2026"),
    ("4 - ALTA", "Casa FOA Buenos Aires", "1 oct - 2 nov 2026", "Planificar asistencia múltiple (evento largo). Networking con estudios de arquitectura y marcas premium. TODOS los rubros AureaHub presentes", "Todos los rubros", "Agosto 2026"),
    ("5 - MEDIA", "Bienal Arquitectura BA", "5-10 oct 2026", "Asistencia selectiva a conferencias clave. Networking con estudios. Menos comercial, más institucional", "Transversal", "Septiembre 2026"),
]

for idx, (prio, feria, fecha, accion, rubro, deadline) in enumerate(actions):
    r = 4 + idx
    vals = [prio, feria, fecha, accion, rubro, deadline]
    for col, v in enumerate(vals, 1):
        cell = ws3.cell(row=r, column=col, value=v)
        cell.alignment = wrap
        cell.border = thin_border

ws3.column_dimensions["A"].width = 16
ws3.column_dimensions["B"].width = 30
ws3.column_dimensions["C"].width = 20
ws3.column_dimensions["D"].width = 60
ws3.column_dimensions["E"].width = 30
ws3.column_dimensions["F"].width = 22

output_path = "Ferias_BA_2026_AureaHub.xlsx"
wb.save(output_path)
print(f"Archivo generado: {output_path}")
