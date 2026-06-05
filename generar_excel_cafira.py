import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Expositores CAFIRA 2026"

headers = [
    "Empresa",
    "Teléfono / WhatsApp",
    "Email",
    "Sitio Web",
    "Contacto (Dueño/Gerente)",
    "Qué venden",
    "B2B / B2C"
]

header_font = Font(name="Calibri", bold=True, color="FFFFFF", size=11)
header_fill = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
thin_border = Border(
    left=Side(style="thin"), right=Side(style="thin"),
    top=Side(style="thin"), bottom=Side(style="thin")
)

for col, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border

# [Empresa, Teléfono, Email, Web, Contacto, Qué venden, B2B/B2C]
expositores = [
    ["Tienda de Costumbres", "1166092892", "ventas@tiendadecostumbres.com.ar", "www.tiendadecostumbres.com.ar", "Silvina Lippai (Fundadora)", "Alfombras, almohadones y pies de cama tejidos 100% a mano con lana de oveja y llama", "Ambos"],
    ["OMA Objetos", "11 5320-2300", "hello.omaobjetos@gmail.com", "www.omaobjetos.com.ar", "María (Fundadora)", "Objetos de diseño artesanal, iluminación y aromatización para el hogar", "Ambos"],
    ["Alcarpintero", "+54 9 11 5420-0863", "alcarpintero@yahoo.com.ar", "alcarpintero.com.ar", "", "Muebles y objetos de carpintería artística en madera", "Ambos"],
    ["Maki Warmi", "11 7227 1001", "info@makiwarmi", "www.makiwarmi.com", "Glenda Saintotte (Fundadora)", "Alfombras artesanales de lana tejidas a mano por tejedoras del norte argentino", "Ambos"],
    ["Casa Nuñez", "11 3506 4003", "rnunez@casanunez.com.ar", "www.casanunez.com.ar", "", "Muebles de exterior y jardín en materiales resistentes a la intemperie", "B2C"],
    ["Blossom Market", "+54 9 11 3166 3868", "blossommarket@hotmail.com", "", "", "Decoración mayorista para el hogar", "B2B"],
    ["Ganeshas", "", "", "", "", "Objetos de decoración", "Ambos"],
    ["Casa Manica", "3512373016", "casamanica.deco@gmail.com", "", "Sofía Simes", "Alfombras turcas y objetos de decoración", "Ambos"],
    ["Disegno Primo", "1126730866", "disegnoprimo@gmail.com", "disegnoprimo.com.ar", "", "Objetos de diseño en hierro para decoración", "Ambos"],
    ["Bait Pisos", "(+5411) 5272-5140", "info@baitpisos.com.ar", "baitpisos.com.ar", "Diego Joel Fleisman (Dueño)", "Pisos, revestimientos, griferías, sanitarios y artículos de decoración", "Ambos"],
    ["Bonn Deco", "4981-4564 / +54 9 11 4430-1750", "bonndeco@gmail.com", "bonndecomayorista.com", "", "Espejos biselados y cuadros decorativos (mayorista)", "B2B"],
    ["Oxido Pampas", "+54 9 2494 63-2550 / +54 9 2494 24-8474", "oxidopampastandil@gmail.com", "oxidopampas.com", "Marcos Probicito, Carolina Liernur, Gonzalo Juárez (Fundadores)", "Fogones, asadores, parrillas y accesorios en hierro oxidado", "Ambos"],
    ["RHIÉ SRL", "01173738716", "rhiedeco@gmail.com", "rhie.com.ar", "", "Velas, esencias y objetos de decoración artesanal", "Ambos"],
    ["Alma Dusha", "11 21828720", "alma.dusha@hotmail.com", "", "Silvana y Leo (Fundadores)", "Objetos decorativos de chapa y hierro artesanales", "Ambos"],
    ["Reina Batata Mayorista", "+54 9 1147780491", "ventas@bigbudahome.com.ar", "www.bgbgift.com.ar", "Federico y María Eugenia (Fundadores)", "Bazar boutique, objetos de decoración y regalería", "Ambos"],
    ["Plug Iluminación", "5493412243484", "ventas@plugiluminacion.com.ar", "plugiluminacion.com.ar", "", "Luminarias y artículos de iluminación", "Ambos"],
    ["Hedan", "01150641144", "hedan.decor@gmail.com", "", "", "Objetos de decoración", "Ambos"],
    ["Bosco", "", "", "", "", "Decoración para el hogar", "Ambos"],
    ["GCF Empapelados", "1131742347", "info@gcfdesign.com.ar", "www.gcfdesign.com.ar", "", "Empapelados decorativos y vinilos de diseño", "Ambos"],
    ["Aurora House", "1162829914", "Aurorahouse.ar@gmail.com", "www.aurorahouse.com.ar", "", "Lámparas de macramé y hierro con diseños exclusivos", "Ambos"],
    ["Component New House", "4584-5953 / 5491156388499", "info@component-newhouse.com", "www.component-newhouse.com", "Pablo Rafael Pelletieri (Socio)", "Muebles de diseño", "B2B"],
    ["Hebras Handmade", "2215700991", "soyhebras@gmail.com", "hebrastejido.mitiendanube.com", "", "Lámparas y objetos tejidos artesanales", "Ambos"],
    ["Alchemyst Design", "01169952113", "ventas@alchemystba.com", "www.alchemystba.com.ar", "", "Murales y empapelados de autor, textiles para el hogar", "Ambos"],
    ["La Pasionaria", "+54 341 4432731", "info@pasionariaargentina.com.ar", "www.pasionariaargentina.com.ar", "Carina Cavazza y Mario Gerosa (Fundadores / CEO)", "Cosmética, perfumería, velas de soja y difusores para el hogar", "Ambos"],
    ["Pachi Deco", "03513890157", "pachi54@hotmail.com", "", "Pachi Grosso", "Textiles artesanales en lana de oveja del norte argentino", "Ambos"],
    ["The Stampa", "+54 91150130162", "hola@thestampa.com.ar", "www.thestampa.com.ar", "", "Cuadros y láminas decorativas", "Ambos"],
    ["Mideko Collection", "11 4523-3711 / 54 9 1139157987", "clientes@midekocollection.com.ar", "midekocollection.com.ar", "", "Objetos de decoración y regalería importada (mayorista)", "B2B"],
    ["Aldea Lobos", "+54 9 11 2874-7827", "proveedores@aldealobos.com.ar", "aldealobos.com.ar", "", "Iluminación y objetos decorativos (fabricante mayorista)", "B2B"],
    ["Eukene Deco", "+54 9 1134803734", "eukenedeco@gmail.com", "", "", "Flores artificiales y arreglos decorativos", "Ambos"],
    ["MBA Aprons", "3515905832", "mbaconsultas@gmail.com", "mbaaprons.mitiendanube.com", "", "Delantales y textiles para el hogar", "Ambos"],
    ["Sincrético", "11 25 99 83 72", "", "sincreticodeco.mitiendanube.com", "", "Alfombras, mantas, almohadones artesanales de comunidades indígenas (economía solidaria)", "Ambos"],
    ["Abril Home Deco", "+54 9 3516156817", "abrilhomedeco@gmail.com", "abrildeco.com", "", "Macetas rotomoldeadas de diseño, muebles de ratán y objetos deco", "Ambos"],
    ["Valdense", "2664154064", "administracion@valdense.com.ar", "www.valdense.com.ar", "", "Rieles de aluminio y accesorios para cortinas", "B2B"],
    ["Mekk Home", "+541161233189", "info@mekkhome.com.ar", "mekkmayorista.com.ar", "", "Objetos de decoración y hogar importados (mayorista)", "B2B"],
    ["AVC Interiores", "+54-11-6125-5635 / +54-11-5009-5455", "ventas@avcinteriores.com.ar", "", "", "Sofás, sillones y muebles para living, comedor y exterior", "B2B"],
    ["Alamada", "+54 9 1150152542", "info@alamada.com.ar", "alamada.com.ar", "", "Muebles y accesorios decorativos de diseño", "Ambos"],
    ["MA-VA Cuadros", "+54 9 2915439953", "mavacuadros@yahoo.com.ar", "mavacuadros.com.ar", "", "Cuadros, marcos y espejos artesanales", "Ambos"],
    ["Teodoras Home", "1127952502", "teodorashome@gmail.com", "teodoranordelta.mitiendanube.com", "Maryan y Jeru (Fundadoras)", "Blanquería, diseño de interiores y muebles a medida", "Ambos"],
    ["Maraña Deco", "+54 9 1165052654", "maraniadeco@gmail.com", "Marania.com.ar", "Alicita Morea, Belén y Bernardi (Fundadoras)", "Lámparas artesanales, apliques, candelabros y objetos de iluminación hechos a mano", "Ambos"],
    ["Chapitadeco", "+54 9 3562 56-5475", "chapitadeco@gmail.com", "chapitadeco.com.ar", "", "Maceteros, portamacetas, fogoneros y figuras en chapa oxidada", "Ambos"],
    ["Alina Hegi", "+54 9 4572-3954 / +54 9 1144981805", "alinahegi@yahoo.com", "alinahegi.com", "Alina Hegi (Dueña)", "Muebles de diseño y objetos decorativos", "Ambos"],
    ["Nikel Iluminación", "+54 9 1146278813 / +54 9 1152282166", "ventas@nikeliluminacion.com.ar", "Nikeliluminacion.com.ar", "", "Luminarias decorativas de diseño y fabricación propia", "B2B"],
    ["Colombas", "+5491136916804", "colombas.sp@gmail.com", "Colombas.com.ar", "", "Objetos de decoración y textiles para el hogar", "Ambos"],
    ["Petris", "+54 9 1138651657 / +54 9 1142105434", "petrishome2@gmail.com", "Petris.com.ar", "René García (Dueño)", "Vajilla y objetos de cerámica artesanal para el hogar", "Ambos"],
    ["Allegra Home", "03482412015", "hola@allegrahome.com.ar", "allegrahome.com.ar", "Carolina y Mauro (Fundadores)", "Mantelería de algodón antimanchas, regalería textil y objetos deco", "Ambos"],
    ["Contemporary Deco", "+54 9 1151634000", "decocontemporary@gmail.com", "", "", "Bazar y artículos decorativos", "Ambos"],
    ["Silva&Co", "3525509346", "lucasmsilva75@gmail.com", "", "Lucas M. Silva (Dueño)", "Iluminación, muebles y objetos de decoración", "Ambos"],
    ["Alhambra", "+54 9 1142023905 / +54 9 1143996590", "info@alhambra.com.ar", "alhambra.com.ar", "", "Telas para decoración y tapicería (distribuidora mayorista, +50 años)", "B2B"],
    ["Marhaba Home", "3518733702 / 3515932694", "marhaba.homeargentina@gmail.com", "marhabacarpets.com", "Federica Fontana y Esteban (Fundadores) / Rodo y Rochi (Socios Argentina)", "Alfombras orientales, persas, de yute, algodón y lino", "Ambos"],
    ["Craft Iluminación", "+54 9 1166337427", "decocraft@hotmail.com", "", "", "Lámparas y objetos de iluminación artesanal", "Ambos"],
    ["Broderi Manteles", "+549 1162966000", "broderidesign@gmail.com", "broderi.com.ar", "", "Manteles, caminos de mesa, artículos de bazar y platería", "Ambos"],
    ["Ebony", "+54 9 11 45883857 / +54 9 1158423499", "administracion@e-bony.com.ar", "e-bony.com.ar", "Lionel Elias Steisel (Gerente)", "Muebles clásicos artesanales tallados en cedro y roble", "Ambos"],
    ["Botany Buenos Aires", "+54 9 11 2280 7278", "botanybuenosaires@gmail.com", "", "", "Velas y esencias aromáticas", "Ambos"],
    ["Datelux", "4855-1212 / +54 9 1136929553", "info@datetux.com.ar", "datelux.com.ar", "", "Artefactos de iluminación importados y componentes", "Ambos"],
    ["By Feli Deco", "+54 9 1130092394", "byfelideco.tienda@gmail.com", "linktr.ee/By_felideco", "", "Objetos de decoración y textiles para el hogar", "Ambos"],
    ["Lola Deco", "+54 9 1138097211 / +54 9 1123721176", "loladecoarg@gmail.com", "lola-deco.negocio.site", "", "Sillones y muebles tapizados a medida", "Ambos"],
    ["Mirador", "45525055 / +54 9 1155843078", "miradorobjetos@gmail.com", "mirador.com.ar", "", "Muebles y objetos importados en madera, ratán y fibras naturales (mayorista)", "B2B"],
    ["Leder", "+54 9 1151857964", "info@lederhd.com", "lederhd.com", "", "Muebles, alfombras, sillones y marroquinería en cuero artesanal (desde 1927)", "Ambos"],
    ["Desde Asia", "+54 9 1147710073 / +54 9 11 3167-4471", "consultas@desdeasia.com.ar", "desdeasia.com", "", "Muebles y objetos decorativos orientales importados de Asia", "Ambos"],
    ["Cueros Especiales", "+54 9 11 64486916 / +54 9 11 42284886", "info@cuerosespeciales.com", "cuerosespeciales.com", "", "Sillones, sillas, almohadones y alfombras en cuero (fabricante desde 1986)", "Ambos"],
    ["Cadmia", "+54 9 1124712225", "info@cadmia.com.ar", "cadmia.com.ar", "Victoria Williams Becker (Fundadora)", "Textiles de diseño estampados a mano para el hogar", "Ambos"],
    ["Estilo Domingo", "+54 9 3472 532010", "Hola@estilodomingo.com.ar", "estilodomingo.com.ar", "Matías y Ayelén (Fundadores, arquitectos)", "Objetos de decoración en madera (maceteros, espejos, lámparas, +120 productos)", "B2B"],
    ["Ecléctica Diseño", "+54 9 3516312332 / +54 9 3515936034", "Iameclectica@gmail.com", "eclecticadiseno.com.ar", "Emilia, Eugenia y Mariangeles Alexandroff Zlateff (Fundadoras)", "Objetos de diseño en madera y cuero para hogar y gastronomía", "Ambos"],
    ["Casi un Ángel", "+54 9 2215736756", "Fabivaioli@gmail.com", "casiunangeldeco.mitiendanube.com", "", "Borlas decorativas y accesorios textiles", "Ambos"],
    ["Fabric AR", "+54 9 1163677970", "mrc_sofa@hotmail.com", "", "", "Sillones y sofás tapizados", "Ambos"],
    ["Forevents", "+54 9 11 64331266 / +54 9 1164055659", "info@forevents.com.ar", "Forevents.com.ar", "", "Muebles, sillas Tiffany y mobiliario para eventos", "B2B"],
    ["Galpón", "3564 508778", "galponmuebles@gmail.com", "", "", "Muebles, sillas y sillones", "Ambos"],
    ["Lampsilver", "+54 9 11 62446973 / +54 9 1130684132", "Lampsilver@gmail.com", "Lampsilver.com.ar", "Santiago Maldonado (Fundador)", "Lámparas artísticas y de diseño artesanal", "Ambos"],
    ["Ortiga", "+54 9 1135914398", "Ortigacasa.ar@gmail.com", "Ortiga.com.ar", "", "Vajilla y artículos de mesa", "Ambos"],
]

for row_idx, expositor in enumerate(expositores, 2):
    for col_idx, value in enumerate(expositor, 1):
        cell = ws.cell(row=row_idx, column=col_idx, value=value)
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)

col_widths = [25, 35, 35, 30, 40, 55, 12]
for i, width in enumerate(col_widths, 1):
    ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = width

ws.auto_filter.ref = f"A1:{openpyxl.utils.get_column_letter(len(headers))}{len(expositores)+1}"
ws.freeze_panes = "A2"

output_path = "/home/user/AUREA-Hub/Expositores_CAFIRA_2026.xlsx"
wb.save(output_path)
print(f"Excel generado: {output_path}")
print(f"Total expositores: {len(expositores)}")
