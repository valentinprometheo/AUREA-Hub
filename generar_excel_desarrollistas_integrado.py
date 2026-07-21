import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from collections import Counter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Directorio Desarrollistas"

header_font = Font(bold=True, color="FFFFFF", size=10)
header_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
wrap = Alignment(wrap_text=True, vertical="top")
thin_border = Border(
    left=Side(style="thin"), right=Side(style="thin"),
    top=Side(style="thin"), bottom=Side(style="thin"),
)

cat_fills = {
    "Desarrollista Boutique": PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid"),
    "Desarrollista Mediano": PatternFill(start_color="D6E4F0", end_color="D6E4F0", fill_type="solid"),
    "Desarrollista Grande": PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid"),
    "Inmobiliaria Premium": PatternFill(start_color="E4DFEC", end_color="E4DFEC", fill_type="solid"),
}

headers = [
    "Empresa", "Categoría", "Teléfono/WhatsApp", "Email", "Web",
    "Instagram", "Contacto (Dir/CEO)", "Zona/Barrios", "Qué desarrollan/venden",
    "Inmobiliaria propia", "Auditoría web (qué le serviría)", "Fuente",
]

for col, h in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    cell.border = thin_border

EXCLUIDOS = {
    "Argencons", "Quartier", "NorthBaires", "Northbaires",
    "Crea Urbana", "G&D Developers", "TKVA", "EDFAN",
}

empresas = [
    # --- DESARROLLISTAS BOUTIQUE (pedidos por el usuario + similares) ---
    ("Brody Friedman", "Desarrollista Boutique",
     "+54 11 5277-9999 / WA: +5491168934063", "info@brodyfriedman.com.ar",
     "brodyfriedman.com.ar", "@brodyfriedman",
     "Andrés Brody, Pablo Brody, Sebastián Friedman, Diego Silbert",
     "Palermo, Núñez, Belgrano",
     "Residencial premium boutique, emprendimientos de diseño",
     "No", "Tiene WhatsApp y formulario básicos, pero sin chatbot IA ni CRM para calificar y seguir leads premium automáticamente.",
     "Web + usuario"),

    ("Metrocúbico", "Desarrollista Boutique",
     "+54 9 3814 15-7526", "contacto@metrocubico.com.ar / clientes@metrocubico.com.ar",
     "metrocubico.com.ar", "",
     "Alejandro Belio (CEO, ex-CEO GCDI)",
     "Tucumán (expandiendo a Buenos Aires)",
     "Residencial premium, venta por m³ (concepto diferencial)",
     "Sí (inmobiliaria.metrocubico.com.ar)", "Solo widget flotante de WhatsApp sin automatización; al expandirse a BA necesitará CRM que unifique leads entre provincias.",
     "Web + usuario"),

    ("Oslo Propiedades", "Inmobiliaria Premium",
     "+54 11 5236-0400 / WA: +54 11 6482-0416", "consultas@oslopropiedades.com.ar",
     "oslopropiedades.com.ar", "@oslo_propiedades",
     "", "Palermo, Belgrano (Av. del Libertador 5936 P12 B)",
     "Venta/alquiler residencial, 252+ propiedades activas, 18+ años",
     "Sí", "Con 18+ años de leads acumulados, carece de CRM y chatbot IA que reactive esa base y clasifique consultas de compra/venta/alquiler.",
     "Web + Zonaprop + usuario"),

    ("Tesler Propiedades", "Inmobiliaria Premium",
     "+54 11 4781-9030 / WA: 11-6900-5239", "tesler@teslerpropiedades.com",
     "teslerpropiedades.com", "@Teslerpropiedades",
     "CUCICBA 3444/7523", "Belgrano (Juramento 2089 P7 Of 711)",
     "Venta/alquiler residencial, 30 años de trayectoria",
     "No", "Tiene alertas email y favoritos, pero ningún WhatsApp ni chatbot IA para responder consultas inmediatas de 30 años de cartera.",
     "Web + usuario"),

    ("Martin Pinus Real Estate", "Inmobiliaria Premium",
     "+54 9 11 5600-2673 / 4775-8467", "hola@martinpinus.net",
     "martinpinus.net", "@martinpinus_realestate",
     "Martin Pinus (Fundador)", "Núñez, Belgrano, Palermo, Recoleta, Las Cañitas",
     "Inmobiliaria luxury segment, desde 2015. Av. Luis María Campos 559 Of 604",
     "No", "Presencia reactiva, sin chatbot/CRM, sin atención 24/7; un funnel automatizado captaría leads de lujo fuera de horario.",
     "Web + usuario"),

    ("Grupo Chomer", "Desarrollista Boutique",
     "+54 11 2000-8569", "consultas@grupochomer.com",
     "grupochomer.com", "@grupochomer",
     "", "Olivos, Núñez, Pilar",
     "Residencial premium en corredor norte",
     "No", "Solo formulario genérico; sin funnel de WhatsApp automatizado ni CRM para nutrir leads entre sus 3 zonas.",
     "Web + audit"),

    ("Estudio Kohon", "Desarrollista Boutique",
     "+54 911 2464-8507", "contacto@estudiokohon.com",
     "estudiokohon.com", "@estudiokohon",
     "", "Caballito, Villa Urquiza, Núñez",
     "Desarrollo inmobiliario residencial",
     "No", "Tiene WhatsApp y emails departamentales sin integración; un CRM centralizado evitaría leads perdidos entre áreas.",
     "Web + audit"),

    ("ABV Arquitectura", "Desarrollista Boutique",
     "+54 11 5236-0404 / Ventas: +54 9 11 2473-0713",
     "ventas@abv.com.ar / info@abv.com.ar",
     "abv.com.ar", "@abv.arq",
     "", "Palermo, Belgrano (Av. del Libertador 6810 P20)",
     "Residencial premium, diseño y solidez",
     "No", "Sin formulario, chat ni WhatsApp en el sitio; una marca premium sin captura de leads pierde consultas a diario.",
     "Web + audit"),

    ("Crayon Desarrollos", "Desarrollista Boutique",
     "(011) 4811-1027/2035", "hola@crayondesarrollos.com.ar",
     "crayondesarrollos.com.ar", "",
     "", "Palermo (Montevideo 1669 2ºA)",
     "Desarrollos boutique residenciales",
     "No", "No tiene formulario, chat ni WhatsApp: solo teléfono y email, vacío total de automatización para un boutique.",
     "Web + audit"),

    ("ATV Arquitectos", "Desarrollista Boutique",
     "", "",
     "atvarquitectos.com", "",
     "", "Palermo",
     "Arquitectura sustentable, desarrollos residenciales",
     "No", "Solo un botón de WhatsApp; sin CRM ni chatbot IA que capture y califique consultas sobre proyectos sustentables.",
     "Web + audit"),

    ("Folken", "Desarrollista Boutique",
     "+54 11 3827-0749", "",
     "folken.com.ar", "@folken.ar",
     "", "CABA premium",
     "Desarrollos residenciales premium",
     "No", "Tiene WhatsApp y formulario, pero sin chatbot IA que precalifique consultas fuera de horario para sus desarrollos.",
     "Web + audit"),

    ("Nova Desarrollos", "Desarrollista Boutique",
     "", "",
     "novadesarrollos.com.ar", "@nova.desarrollosok",
     "", "CABA (Palermo)",
     "Desarrollos contemporáneos residenciales",
     "No", "No expone teléfono, WhatsApp ni formulario visibles; toda la captación queda solo en Instagram.",
     "Web + audit"),

    ("Sky Desarrollos", "Desarrollista Boutique",
     "+54 11 3639-7777", "",
     "skydesarrollos.com.ar", "@skydesarrollos",
     "", "CABA",
     "Desarrollos boutique premium",
     "No", "Tiene teléfono y WhatsApp pero sin formulario ni email visibles; un chatbot IA capturaría leads fuera de horario.",
     "Web + audit"),

    ("Uno en Uno", "Desarrollista Boutique",
     "+54 9 11 2058-5561", "info@grupounoenuno.com",
     "grupounoenuno.com", "@grupounoenuno",
     "", "CABA",
     "Desarrollos boutique residenciales",
     "No", "Buenos canales de contacto pero sin CRM ni chatbot IA que perfile compradores boutique antes de derivarlos a ventas.",
     "Web + audit"),

    ("Mirabilia", "Desarrollista Boutique",
     "+54 9 11 5818-7518", "",
     "mirabilia.com.ar", "@mirabiliadesarrollos",
     "", "CABA",
     "Desarrollos boutique premium",
     "No", "Solo WhatsApp y formulario genérico de inversión, sin CRM ni chatbot IA que segmente inversores de compradores finales.",
     "Web + audit"),

    ("Grupo Upgrade", "Desarrollista Boutique",
     "", "",
     "grupoupgrade.com", "@grupoupgrade",
     "", "Corredor norte",
     "Desarrollos residenciales corredor norte",
     "No", "No expone teléfono, email ni WhatsApp; solo Instagram y buscador de desarrollos. Falta embudo de captura completo.",
     "Web + audit"),

    ("Azcuy", "Desarrollista Mediano",
     "(5411) 5333-0335", "clientes@estudioazcuy.com",
     "azcuy.com.ar", "@estudioazcuy",
     "", "Caballito, Nordelta",
     "Residencial, showroom propio",
     "Sí", "Tiene newsletter, WhatsApp y showroom, pero sin CRM que integre leads entre Caballito y Nordelta en un pipeline único.",
     "Web + audit"),

    # --- DESARROLLISTAS MEDIANOS/GRANDES (del Excel existente) ---
    ("ADN Developers", "Desarrollista Mediano",
     "+54 11 4775-5158 / WA: 11-3893-3260", "info@adndevelopers.com.ar",
     "adndevelopers.com.ar", "",
     "Elbio Leandro Stoler (Fundador y Director)",
     "Palermo Hollywood",
     "Residencial (1-5 amb), oficinas, turístico. 20+ edificios, ~100.000 m². Marca DOME para torres premium",
     "Sí (Nexo Propiedades)", "Sin chatbot ni CRM automatizado; una marca con 20+ edificios necesita funnel digital para nutrir leads de múltiples proyectos.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Land Developers Group", "Desarrollista Mediano",
     "+54 11 5263-3596 / WA: +54 9 11 2240-4473", "contacto@ldgcompany.com",
     "landdevelopersgroup.com", "",
     "Gabriel Rojchman (CEO). Dir. Comercial: Hernán Comisarenco",
     "CABA + Florida, USA",
     "Townhouses exclusivos, oficinas corporativas, locales comerciales. 30+ años",
     "Sí", "Operación bi-nacional sin CRM unificado; un sistema integrado alinearía leads entre Argentina y USA.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Lepore Propiedades", "Inmobiliaria Premium",
     "+549 11 2249-3859 (Caballito HQ)", "info@lepore.com.ar",
     "lepore.com.ar", "",
     "Norberto Lepore (Presidente/Fundador)",
     "Caballito, Palermo, V. Crespo (5 sucursales, 60+ empleados)",
     "Residencial de categoría + venta/alquiler usados. Desde 1980, empresa familiar 2da gen.",
     "Sí", "5 sucursales sin CRM centralizado; un sistema unificado evitaría duplicación y mejoraría seguimiento entre sedes.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Vitrium Capital", "Desarrollista Grande",
     "+54 9 11 2152-0660", "ventas@vitriumcapital.com",
     "vitriumcapital.com", "",
     "Federico Gagliardo (Fundador y CEO)",
     "ARG, URU, PAR, USA",
     "Residencial, comercial, mixed-use premium. Forbes Top 20. Pueblo Caamaño ~US$80M",
     "Sí", "Operación multinacional con múltiples proyectos simultáneos; CRM con IA priorizaría leads por proyecto y país.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("INARCH", "Desarrollista Mediano",
     "4774-7154 / WA: +54 9 11 5740-4253", "comercial@inarch.com.ar",
     "inarch.com.ar", "",
     "Anabela Santos (CEO), Paulo González Toledo (Co-fundador). Dir. Comercial: Jeremías González Toledo",
     "Núñez, Palermo, Chacarita",
     "Residencial. Edificios 5.000-7.000 m². Parte de Grupo GTS. ~150 empleados. Desde 2007",
     "Sí (comercialización integral)", "150 empleados sin CRM reportado; automatización de WhatsApp para consultas de proyectos en construcción optimizaría conversiones.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Spazios", "Desarrollista Mediano",
     "0800-555-8289 / WA: +54 9 11 5217-5990", "info@spazios.com.ar",
     "spazios.com.ar", "",
     "Juan Manuel Tapiola (CEO y Fundador)",
     "Belgrano, Devoto, Caseros",
     "Residencial exclusivo. 39 proyectos, 1.000+ deptos. Financiación 'Más Dueños' hasta 360 cuotas",
     "Sí (Spazios Gestión Inmobiliaria)", "1.000+ departamentos con financiación propia generan alto volumen de consultas; chatbot IA filtraría leads calificados.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Grupo ECIPSA", "Desarrollista Grande",
     "+54 9 11 2789-4782 (BA) / +54 351 425-5525 (Cba)", "info@ecipsa.com",
     "ecipsa.com", "",
     "Jaime Garbarsky (Presidente), Walter Fuks (CEO). Gte. Comercial: Ezequiel Bonomo",
     "9 provincias",
     "Residencial masivo (marca Natania). MilAires CABA 6.800+ unidades. Desde 1979",
     "Sí (Natania, Natania Directa)", "Escala masiva en 9 provincias requiere CRM centralizado con WhatsApp IA para atender volumen de consultas 24/7.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Grupo Portland", "Desarrollista Mediano",
     "(+54) 11 2488-1156", "comercial@grupoportland.com",
     "grupoportland.com", "",
     "Gustavo Menayed (CEO y Fundador)",
     "Vicente López, expandiendo a Miami",
     "Residencial torres, oficinas, mixed-use. L'Avenue Libertador (Zaha Hadid). 20+ años",
     "No confirmado", "Marca premium con proyecto Zaha Hadid necesita funnel digital sofisticado para leads de ultra-lujo.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Dypsa Group", "Desarrollista Grande",
     "+54 9 11 4468-7285", "info@dypsa.com",
     "dypsa.com", "",
     "Issel Kiperszmid (CEO y Fundador). Hijo: Nicolás Kiperszmid",
     "Vicente López (Av. Libertador 174 P11)",
     "Diversificado: torres residenciales, shoppings, hoteles, barrios privados. 40+ años. Fundador de CEDU",
     "Sí", "Portafolio diversificado (residencial, comercial, hotelero) necesita CRM multi-vertical con chatbot por tipo de producto.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("GNV Group", "Desarrollista Grande",
     "WA: +54 9 11 3032-8205 / +54 9 11 6171-4976", "info@gnvgroup.com",
     "gnvgroup.com", "",
     "Alejandro Ginevra (Presidente y CEO)",
     "Puerto Madero, Punta del Este",
     "Luxury mixed-use: torres residenciales, hoteles, shoppings. Madero Harbour. SLS Hotel. 50+ años",
     "Sí (Ginevra International Realty)", "Luxury developer con inmobiliaria propia; CRM con IA calificaría inversores de alto patrimonio automáticamente.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Newland Desarrollos", "Desarrollista Mediano",
     "11 6395-3292", "info@newland.com.ar",
     "newland.com.ar", "",
     "Ernesto Davidsohn Benet (Fundador y CEO)",
     "Barracas, Palermo, Recoleta (Juncal 2082). ARG, URU, España",
     "Residencial urbano. Canvas Barracas, VitrAUx Palermo, Smart Point. 30+ edificios, 20+ años",
     "Sí", "30+ edificios en 3 países requiere CRM unificado con funnel por mercado geográfico.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Vizora Desarrollos", "Desarrollista Mediano",
     "+54 11 2182-2089 / WA inversiones: +54 9 11 2177-4302", "ventas@vizora.com.ar",
     "vizora.com.ar", "@LiveByVizora",
     "Milagros Brito (Fundadora). Gte. Ventas: Fabián Escanes",
     "Puerto Madero, Tigre",
     "Residencial premium, comercial, cultural. Remeros Beach, ZenCity. 20+ años",
     "Sí (parcial)", "Maneja varios WhatsApp y formularios sin CRM que unifique inversores de Puerto Madero y Pilar en un embudo.",
     "Desarrollistas_BA_Prospectos.xlsx + audit"),

    ("Fernández Prieto y Asoc.", "Desarrollista Grande",
     "+54 11 4589-7792", "",
     "fernandezprieto.com.ar", "",
     "Rodrigo Fernández Prieto (CEO)",
     "Puerto Madero",
     "Torres residenciales premium, comercial, industrial, obras públicas. Link Towers, ZenCity. Usa Urbania 3D",
     "Sí", "Usa Urbania 3D pero sin chatbot IA; integración CRM+3D automatizaría la calificación de leads en showroom virtual.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Grupo Monarca", "Desarrollista Grande",
     "011 2080-1800", "contacto@grupomonarca.com",
     "grupomonarca.com", "",
     "Gonzalo Monarca (CEO y Fundador)",
     "CABA (Arias 1639)",
     "Residencial. 650.000+ m², 20+ proyectos, ~500 empleados. Desde 1997. 1ra con ISO 9001",
     "Sí", "500 empleados y 20+ proyectos simultáneos; CRM con IA optimizaría coordinación comercial entre equipos.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("TGLT (ahora GCDI)", "Desarrollista Grande",
     "WA: +54 9 11 2453-5448 / Tel: +54 11 5252-5050", "ventas@tglt.com",
     "tglt.com", "",
     "Federico Weil (Fundador)",
     "CABA (Miñones 2177)",
     "Residencial y mixed-use. Marcas: Forum, Astor, Metra, Venice. 570.000+ m². Cotiza BYMA (TGLT.BA)",
     "Sí (ciclo completo)", "Cotizante en BYMA con múltiples marcas; CRM con analítica por marca mediría performance comercial de cada línea.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Consultatio", "Desarrollista Grande",
     "+54 11 4318-8000", "info@consultatio.com.ar",
     "consultatio.com.ar", "",
     "Eduardo Costantini (Fundador/Presidente), Gonzalo de la Serna (CEO)",
     "Nordelta, CABA, URU, USA",
     "Urbanizaciones (Nordelta), torres corporativas. Adquirió 51% Argencons 2025. 501-1.000 empleados",
     "Sí (Consultatio Real Estate)", "Escala enterprise con operación multinacional; integración CRM+WhatsApp IA para segmentar leads Nordelta vs CABA vs internacional.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("IRSA Propiedades", "Desarrollista Grande",
     "0800-222-2299", "Formulario web",
     "irsa.com.ar", "",
     "Eduardo Elsztain (Presidente)",
     "CABA, nacional",
     "Shoppings, oficinas, hoteles, residencial (Ramblas del Plata). Mayor inmobiliaria cotizante ARG. BYMA + NYSE",
     "Sí", "Corporación cotizante con múltiples verticales; chatbot IA en portal web captaría leads por segmento (shopping, oficinas, residencial).",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Grupo Farallón", "Desarrollista Grande",
     "WA: +54 9 11 6815-8480", "",
     "grupofarallon.com", "",
     "Gerónimo Gutiérrez de Barrio (Presidente)",
     "Pilar (Ruta Panamericana Km 49.5)",
     "Barrios privados, countries, centros comerciales, vivienda social. Desde 1985",
     "No confirmado", "Pionero de barrios privados sin CRM reportado; chatbot IA calificaría compradores por perfil (country vs social).",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Fortune International", "Desarrollista Grande",
     "BA: +5411 7700-1010 / Miami: (305) 400-6393", "info@fir.com",
     "fortuneintlgroup.com", "",
     "Edgardo Defortuna (Presidente, CEO y Fundador)",
     "Miami (oficina BA)",
     "Luxury residencial South Florida. 18 oficinas, ~1.000 asociados. Christie's International RE",
     "Sí (Christie's)", "Red global con oficina BA; CRM con IA captaría inversores argentinos interesados en Miami automáticamente.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Grupo Briones", "Desarrollista Boutique",
     "+54 9 11 2468-2070", "contacto@grupobriones.com.ar",
     "grupobriones.com.ar", "@grupobriones",
     "", "CABA",
     "Residencial en CABA",
     "Sí", "Buen formulario segmentado pero sin chatbot IA ni CRM que automatice el seguimiento de cada consulta calificada.",
     "Desarrollistas_BA_Prospectos.xlsx + audit"),

    ("Alto Grande / M&M Propiedades", "Desarrollista Mediano",
     "+11 5272-0800", "",
     "", "",
     "", "CABA",
     "Residencial. Tiene inmobiliaria propia M&M Propiedades",
     "Sí (M&M Propiedades)", "Sin presencia web visible; necesita sitio + funnel digital completo con catálogo y WhatsApp automatizado.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    ("Big Ben", "Desarrollista Mediano",
     "+54 (11) 4483-4566", "",
     "", "",
     "Andrés Castellano (CEO)", "CABA",
     "Residencial en CABA",
     "No confirmado", "Sin web ni presencia digital detectada; oportunidad de armar presencia desde cero con sitio + CRM + WhatsApp IA.",
     "Desarrollistas_BA_Prospectos.xlsx"),

    # --- INMOBILIARIAS PREMIUM ---
    ("Izrastzoff", "Inmobiliaria Premium",
     "", "",
     "izrastzoff.com.ar", "",
     "", "Corredor norte (50 años de trayectoria)",
     "Inmobiliaria tradicional premium, venta/alquiler residencial de categoría",
     "Sí", "50 años de cartera sin automatización reportada; CRM con IA reactivaría base histórica de clientes y propietarios.",
     "Web search"),

    ("Rapaport Bienes Raíces", "Inmobiliaria Premium",
     "", "",
     "rapaport.com.ar", "",
     "", "Núñez, Belgrano, Palermo",
     "500+ transacciones, residencial premium corredor norte",
     "Sí", "Alto volumen de transacciones sin CRM reportado; automatización de WhatsApp captaría consultas 24/7.",
     "Web search"),

    ("Llauro Propiedades", "Inmobiliaria Premium",
     "4816-8000", "",
     "llauro.com.ar", "",
     "", "Barrio Norte, Recoleta, Belgrano, Nordelta, Pilar",
     "Inmobiliaria premium multi-zona",
     "Sí", "Operación multi-zona (CABA + GBA) sin CRM centralizado reportado; chatbot IA unificaría consultas entre sucursales.",
     "Web search"),

    ("Soldati Propiedades", "Inmobiliaria Premium",
     "", "",
     "soldati.com.ar", "",
     "", "Palermo (Humboldt 1986). 3 unidades, 30+ años",
     "Inmobiliaria premium, venta/alquiler residencial de categoría",
     "Sí", "3 sucursales y 30+ años de operación; CRM unificado con WhatsApp IA mejoraría gestión de cartera entre unidades.",
     "Web search"),

    ("LJ Ramos", "Inmobiliaria Premium",
     "", "",
     "ljramos.com.ar", "",
     "", "CABA y GBA",
     "Inmobiliaria premium corporativa y residencial",
     "Sí", "Gran operación inmobiliaria sin chatbot IA reportado; automatización captaría leads corporativos y residenciales 24/7.",
     "Web search"),

    ("Toribio Achával", "Inmobiliaria Premium",
     "", "",
     "toribioachával.com", "",
     "", "CABA y GBA",
     "Inmobiliaria premium, venta/alquiler residencial de categoría, campos",
     "Sí", "Inmobiliaria tradicional de alto perfil; CRM con IA segmentaría leads por tipo (residencial, campo, comercial).",
     "Web search"),

    ("Miranda Bosch", "Inmobiliaria Premium",
     "", "",
     "mirandabosch.com", "",
     "", "CABA premium",
     "Inmobiliaria boutique premium, propiedades de lujo",
     "Sí", "Inmobiliaria de lujo que requiere atención personalizada; chatbot IA precalificaría compradores VIP fuera de horario.",
     "Web search"),

    ("Korn Propiedades", "Inmobiliaria Premium",
     "", "",
     "kornpropiedades.com.ar", "",
     "", "Zona norte, countries",
     "Inmobiliaria premium zona norte, countries y barrios privados",
     "Sí", "Especializada en countries y zona norte; CRM con IA clasificaría leads por tipo de propiedad y presupuesto.",
     "Web search"),

    ("Mudafy", "Inmobiliaria Premium",
     "", "",
     "mudafy.com.ar", "",
     "", "CABA y GBA",
     "PropTech inmobiliaria, compra/venta con tecnología",
     "Sí", "PropTech con base tecnológica pero sin chatbot IA propio reportado; integración CRM potenciaría su modelo digital.",
     "Web search"),
]

for idx, row_data in enumerate(empresas):
    row = idx + 2
    for col, v in enumerate(row_data, 1):
        cell = ws.cell(row=row, column=col, value=v)
        cell.alignment = wrap
        cell.border = thin_border
    cat = row_data[1]
    if cat in cat_fills:
        for col in range(1, len(headers) + 1):
            ws.cell(row=row, column=col).fill = cat_fills[cat]

col_widths = [26, 22, 32, 36, 24, 22, 38, 30, 55, 14, 60, 28]
for i, w in enumerate(col_widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

ws.freeze_panes = "A2"
ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{len(empresas) + 1}"

# --- HOJA 2: Resumen por Categoría ---
ws2 = wb.create_sheet("Resumen por Categoría")
ws2.cell(row=1, column=1, value="Desarrollistas e Inmobiliarias BA - Resumen").font = Font(bold=True, size=14)

cats = Counter(e[1] for e in empresas)
ws2.cell(row=3, column=1, value="Categoría").font = Font(bold=True)
ws2.cell(row=3, column=2, value="Cantidad").font = Font(bold=True)
ws2.cell(row=3, column=3, value="Empresas").font = Font(bold=True)

for idx2, (cat, count) in enumerate(cats.most_common()):
    r = 4 + idx2
    ws2.cell(row=r, column=1, value=cat)
    ws2.cell(row=r, column=2, value=count)
    empresas_cat = [e[0] for e in empresas if e[1] == cat]
    ws2.cell(row=r, column=3, value=", ".join(empresas_cat))
    if cat in cat_fills:
        for c in range(1, 4):
            ws2.cell(row=r, column=c).fill = cat_fills[cat]
    for c in range(1, 4):
        ws2.cell(row=r, column=c).alignment = wrap
        ws2.cell(row=r, column=c).border = thin_border

r_total = 4 + len(cats)
ws2.cell(row=r_total, column=1, value="TOTAL").font = Font(bold=True)
ws2.cell(row=r_total, column=2, value=len(empresas)).font = Font(bold=True)
for c in range(1, 4):
    ws2.cell(row=r_total, column=c).border = thin_border

ws2.column_dimensions["A"].width = 28
ws2.column_dimensions["B"].width = 12
ws2.column_dimensions["C"].width = 80

# --- HOJA 3: Excluidos ---
ws3 = wb.create_sheet("Excluidos (Clientes Prometheo)")
ws3.cell(row=1, column=1, value="Empresas excluidas (clientes actuales de Prometheo)").font = Font(bold=True, size=12, color="CC0000")

excl_headers = ["Empresa", "Motivo", "Web"]
for col, h in enumerate(excl_headers, 1):
    cell = ws3.cell(row=3, column=col, value=h)
    cell.font = Font(bold=True)
    cell.border = thin_border

excluidos_data = [
    ("Argencons / Quartier", "Cliente actual de Prometheo", "argencons.com"),
    ("NorthBaires", "Cliente actual de Prometheo", "northbaires.com"),
    ("Crea Urbana", "Cliente actual de Prometheo", "creaurbana.com.ar"),
    ("G&D Developers", "Cliente actual de Prometheo (confirmado por usuario)", "gddevelopers.com"),
    ("TKVA", "Cliente actual de Prometheo (confirmado por usuario)", ""),
    ("EDFAN Constructora/Real Estate", "Cliente actual de Prometheo (confirmado por usuario)", ""),
]

for idx3, (emp, motivo, web) in enumerate(excluidos_data):
    r = 4 + idx3
    ws3.cell(row=r, column=1, value=emp).border = thin_border
    ws3.cell(row=r, column=2, value=motivo).border = thin_border
    ws3.cell(row=r, column=3, value=web).border = thin_border
    for c in range(1, 4):
        ws3.cell(row=r, column=c).fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")

ws3.column_dimensions["A"].width = 30
ws3.column_dimensions["B"].width = 45
ws3.column_dimensions["C"].width = 25

# --- HOJA 4: Leyenda ---
ws4 = wb.create_sheet("Leyenda")
ws4.cell(row=1, column=1, value="Leyenda de colores y categorías").font = Font(bold=True, size=14)

legend = [
    ("Desarrollista Boutique", "Verde claro", "Boutique/premium de nicho, 1-5 proyectos simultáneos, corredor norte, diseño. Perfil tipo Brody Friedman."),
    ("Desarrollista Mediano", "Azul claro", "Operación mediana, 5-20 proyectos, presencia consolidada, posiblemente multi-zona."),
    ("Desarrollista Grande", "Naranja claro", "Operación grande/corporativa, 20+ proyectos, cotizantes, multinacionales."),
    ("Inmobiliaria Premium", "Violeta claro", "Inmobiliarias de alto perfil, venta/alquiler residencial premium, no desarrollan."),
]

for idx4, (cat, color, desc) in enumerate(legend):
    r = 3 + idx4
    ws4.cell(row=r, column=1, value=cat).font = Font(bold=True)
    if cat in cat_fills:
        ws4.cell(row=r, column=1).fill = cat_fills[cat]
    ws4.cell(row=r, column=2, value=color)
    ws4.cell(row=r, column=3, value=desc)
    for c in range(1, 4):
        ws4.cell(row=r, column=c).alignment = wrap
        ws4.cell(row=r, column=c).border = thin_border

ws4.column_dimensions["A"].width = 25
ws4.column_dimensions["B"].width = 15
ws4.column_dimensions["C"].width = 80

r_note = 3 + len(legend) + 2
ws4.cell(row=r_note, column=1, value="Notas:").font = Font(bold=True)
ws4.cell(row=r_note + 1, column=1, value="Fuentes:").font = Font(bold=True, size=10)
ws4.cell(row=r_note + 1, column=2, value="Web corporativas, Zonaprop, departamentosenpozo.com.ar, prensa sectorial, Instagram, datos del usuario")
ws4.cell(row=r_note + 2, column=1, value="Fecha relevamiento:").font = Font(bold=True, size=10)
ws4.cell(row=r_note + 2, column=2, value="Julio 2026")
ws4.cell(row=r_note + 3, column=1, value="Auditoría web:").font = Font(bold=True, size=10)
ws4.cell(row=r_note + 3, column=2, value="Revisión de presencia digital, canales de contacto, chatbot, CRM, WhatsApp, formularios. Orientada a detectar oportunidades para AureaHub/Prometheo.")

output = "Desarrollistas_Inmobiliarias_BA_Integrado.xlsx"
wb.save(output)

boutique = sum(1 for e in empresas if e[1] == "Desarrollista Boutique")
mediano = sum(1 for e in empresas if e[1] == "Desarrollista Mediano")
grande = sum(1 for e in empresas if e[1] == "Desarrollista Grande")
inmob = sum(1 for e in empresas if e[1] == "Inmobiliaria Premium")

print(f"Generado: {output}")
print(f"Total empresas: {len(empresas)}")
print(f"  - Desarrollistas Boutique: {boutique}")
print(f"  - Desarrollistas Medianos: {mediano}")
print(f"  - Desarrollistas Grandes: {grande}")
print(f"  - Inmobiliarias Premium: {inmob}")
print(f"Excluidos (clientes Prometheo): {len(excluidos_data)}")
