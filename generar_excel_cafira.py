import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Expositores CAFIRA 2026"

headers = ["Empresa", "Stand", "Teléfono / WhatsApp", "Email", "Sitio Web", "Instagram", "Contacto (Dueño/Gerente)", "Dirección", "Rubro"]

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

expositores = [
    ["Tienda de Costumbres", "202", "1166092892", "ventas@tiendadecostumbres.com.ar", "www.tiendadecostumbres.com.ar", "@tiendadecostumbres", "", "Regina Pacini de Alvear 892, Don Torcuato", "Alfombras, Textil Hogar"],
    ["OMA Objetos", "249", "11 5320-2300", "hello.omaobjetos@gmail.com", "www.omaobjetos.com.ar", "@oma_objetos", "", "Coronel Pringles 1645", ""],
    ["Alcarpintero", "268", "+54 9 11 5420-0863", "alcarpintero@yahoo.com.ar", "alcarpintero.com.ar", "@alcarpintero", "", "Humberto Primo 1919, Avellaneda (CP1870), Buenos Aires", ""],
    ["Maki Warmi", "264", "11 7227 1001", "info@makiwarmi", "www.makiwarmi.com", "@maki_warmi", "", "España 837, San Isidro", ""],
    ["Casa Nuñez", "152", "11 3506 4003", "rnunez@casanunez.com.ar", "www.casanunez.com.ar", "@casanunez", "", "Av. Gaona 4280, Moreno / Av. San Martín 3502, CABA", ""],
    ["Blossom Market", "KM 44", "+54 9 11 3166 3868", "", "", "", "", "KM 44 Paseo Pilar Shopping Del Viso", ""],
    ["Ganeshas", "223", "", "", "", "@ganeshas.argentinas", "", "Av. Agustín M. García 8765, Nordelta", ""],
    ["Casa Manica", "230", "3512373016", "casamanica.deco@gmail.com", "", "@casamanica", "", "9 de julio 3286, Córdoba (CP5000)", "Alfombras, Objetos Deco"],
    ["Disegno Primo", "157", "1126730866", "disegnoprimo@gmail.com", "disegnoprimo.com.ar", "@Disegnoprimo", "", "Cita previa, Don Torcuato (CP1611), Buenos Aires", "Hierro"],
    ["Bait Pisos", "128", "(+5411) 5272-5140", "info@baitpisos.com.ar", "", "", "", "Fitz Roy 2179, CABA", ""],
    ["Bonn Deco", "158", "4981-4564 / +54 9 11 4430-1750", "bonndeco@gmail.com", "bonndecomayorista.com", "@bonndeco_", "", "Pasaje King 356, CABA (CP1199)", "Cuadros y Espejos, Objetos Deco"],
    ["Oxido Pampas", "144", "+54 9 2494 63-2550 / +54 9 2494 24-8474", "oxidopampastandil@gmail.com", "oxidopampas.com", "@oxidopampasmayorista", "", "Parque Industrial, Calle 116 e/111 y 113, Tandil (CP7000)", "Hierro, Macetas y Jardín, Objetos Deco"],
    ["RHIÉ SRL", "221", "01173738716", "rhiedeco@gmail.com", "rhie.com.ar", "@rhieobjetos", "", "Avenida Centenario 1528, Beccar (CP1643)", "Velas y Esencias"],
    ["Alma Dusha", "255", "11 21828720", "alma.dusha@hotmail.com", "", "@alma_dusha", "", "Acceso Oeste y Camino del Buen Ayre, Moreno (CP1742)", "Objetos Deco"],
    ["Reina Batata Mayorista", "259", "+54 9 1147780491", "ventas@bigbudahome.com.ar", "www.bgbgift.com.ar", "@reinabatatamayorista", "", "Godoy Cruz 1457, CABA (C1414CYE)", "Bazar, Objetos Deco"],
    ["Plug Iluminación", "273", "5493412243484", "ventas@plugiluminacion.com.ar", "plugiluminacion.com.ar", "@plugiluminacion", "", "Asamblea 420, Rosario (CP2000), Santa Fe", ""],
    ["Hedan", "121", "01150641144", "hedan.decor@gmail.com", "", "@HEDAN.decor", "", "Hudson (CP1885), Buenos Aires", ""],
    ["Bosco", "271", "", "", "", "@boscoargentina", "", "", ""],
    ["GCF Empapelados", "155", "1131742347", "info@gcfdesign.com.ar", "www.gcfdesign.com.ar", "@Gcfdesign", "", "Av. Corrientes 4006, piso 1 Of. 2, Almagro", ""],
    ["Aurora House", "212", "1162829914", "Aurorahouse.ar@gmail.com", "www.aurorahouse.com.ar", "@aurorahouse.ar", "", "Buenos Aires 1398, Tigre (1648)", "Iluminación"],
    ["Component New House", "263", "4584-5953 / 5491156388499", "info@component-newhouse.com", "www.component-newhouse.com", "@component_yz", "", "Almirante Francisco Segui 2469, CABA (CP1416)", ""],
    ["Hebras Handmade", "159", "2215700991", "soyhebras@gmail.com", "hebrastejido.mitiendanube.com", "@hebras_handmade", "", "Soler 107, Chascomús (CP7130), Buenos Aires", "Iluminación"],
    ["Alchemyst Design", "278", "01169952113", "ventas@alchemystba.com", "www.alchemystba.com.ar", "@alchemystba", "", "Araoz 2437, Palermo, Buenos Aires", "Empapelados, Textil Hogar"],
    ["La Pasionaria", "249", "+54 341 4432731", "info@pasionariaargentina.com.ar", "www.pasionariaargentina.com.ar", "@lapasionariaargentina", "", "Av. Eva Perón 8960, Rosario", ""],
    ["Pachi Deco", "123", "03513890157", "pachi54@hotmail.com", "", "@Pachi_decohome", "", "Av. Los Álamos 1111 La Rufina CP 5151, La Calera, Córdoba", "Textil Hogar"],
    ["The Stampa", "147", "+54 91150130162", "hola@thestampa.com.ar", "www.thestampa.com.ar", "@thestampa", "", "", ""],
    ["Mideko Collection", "277", "11 4523-3711 / 54 9 1139157987", "clientes@midekocollection.com.ar", "midekocollection.com.ar", "", "", "Bucarelli 1162, CABA (CP1427)", "Objetos Deco"],
    ["Aldea Lobos", "148", "+54 9 11 2874-7827", "proveedores@aldealobos.com.ar", "aldealobos.com.ar", "@aldea.lobos", "", "Argerich 1480, Buenos Aires", "Iluminación, Objetos Deco"],
    ["Eukene Deco", "156", "+54 9 1134803734", "eukenedeco@gmail.com", "", "@Eukenedeco", "", "Parque Leloir, Buenos Aires", "Flores"],
    ["MBA Aprons", "229", "3515905832", "mbaconsultas@gmail.com", "mbaaprons.mitiendanube.com", "@mba_aprons", "", "Angualasto 7522, Villa Warcalde, Córdoba", "Textil Hogar"],
    ["Sincrético", "159", "11 25 99 83 72", "", "sincreticodeco.mitiendanube.com", "@sincreticodeco", "", "Galería Libertad – Libertad 1170, local 23", "Textil Hogar"],
    ["Abril Home Deco", "126", "+54 9 3516156817", "abrilhomedeco@gmail.com", "abrildeco.com", "@abrilhomedeco", "", "Av. Rafael Núñez 4565, Córdoba (CP5009)", "Objetos Deco, Plantas y Flores"],
    ["Valdense", "137", "2664154064", "administracion@valdense.com.ar", "www.valdense.com.ar", "@evelynhome&deco", "", "", "Rieles"],
    ["Mekk Home", "220", "+541161233189", "info@mekkhome.com.ar", "mekkmayorista.com.ar", "@mekk.home", "", "San Isidro, Buenos Aires", ""],
    ["AVC Interiores", "110", "+54-11-6125-5635 / +54-11-5009-5455", "ventas@avcinteriores.com.ar", "", "@avc.interiores", "", "Buenos Aires", "Muebles, Sillones"],
    ["Alamada", "201", "+54 9 1150152542", "info@alamada.com.ar", "alamada.com.ar", "@casa.alamada", "", "Ruiz Huidobro 2783, CP 1429 CABA", "Muebles, Objetos Deco"],
    ["MA-VA Cuadros", "108", "+54 9 2915439953", "mavacuadros@yahoo.com.ar", "mavacuadros.com.ar", "@mavacuadros", "", "Bahía Blanca (CP8000), Buenos Aires", "Cuadros y Espejos"],
    ["Teodoras Home", "119", "1127952502", "teodorashome@gmail.com", "teodoranordelta.mitiendanube.com", "@teodorashome", "", "Talcahuano 1201 CP 1014, Buenos Aires", "Blanquería, Textil Hogar"],
    ["Maraña Deco", "130", "+54 9 1165052654", "maraniadeco@gmail.com", "Marania.com.ar", "@maraniadeco", "", "Recoleta, CABA", "Iluminación"],
    ["Chapitadeco", "251", "+54 9 3562 56-5475", "chapitadeco@gmail.com", "chapitadeco.com.ar", "@chapitadeco", "", "España 387 CP 2421, Morteros, Córdoba", "Objetos Deco"],
    ["Alina Hegi", "276", "+54 9 4572-3954 / +54 9 1144981805", "alinahegi@yahoo.com", "alinahegi.com", "@alinahegi", "Alina Hegi", "Manuela Pedraza 6064, CP 1431, CABA", "Muebles, Objetos Deco"],
    ["Nikel Iluminación", "139", "+54 9 1146278813 / +54 9 1152282166", "ventas@nikeliluminacion.com.ar", "Nikeliluminacion.com.ar", "@Nikeliluminacionok", "", "Mons Angelelli 936 CP 1708, Morón, Buenos Aires", ""],
    ["Colombas", "232", "+5491136916804", "colombas.sp@gmail.com", "Colombas.com.ar", "@colombas_buenos_aires", "", "Buenos Aires", "Objetos Deco, Textil Hogar"],
    ["Petris", "217", "+54 9 1138651657 / +54 9 1142105434", "petrishome2@gmail.com", "Petris.com.ar", "@petris.home", "", "José A. Blanco 4238, CP 1879, Quilmes, Buenos Aires", "Bazar"],
    ["Allegra Home", "246", "03482412015", "hola@allegrahome.com.ar", "allegrahome.com.ar", "@allegrahome", "", "Roca 944, Reconquista CP 3560, Santa Fe", "Objetos Deco, Textil Hogar"],
    ["Contemporary Deco", "143", "+54 9 1151634000", "decocontemporary@gmail.com", "", "@contemporarydeco", "", "Calle del Caminante 80, apt 250, Nordelta (CP1670)", "Bazar"],
    ["Silva&Co", "254", "3525509346", "lucasmsilva75@gmail.com", "", "@silvaandco.ar", "Lucas M. Silva", "", "Iluminación, Muebles, Objetos Deco"],
    ["Alhambra", "134", "+54 9 1142023905 / +54 9 1143996590", "info@alhambra.com.ar", "alhambra.com.ar", "@alhambra.telas", "", "Gral. Villegas 1071, Remedios de Escalada (CP1826)", "Textil Hogar"],
    ["Marhaba Home", "144", "3518733702 / 3515932694", "marhaba.homeargentina@gmail.com", "marhabacarpets.com", "@marhaba_carpets", "", "Av Japón 2300, Córdoba", "Textil Hogar"],
    ["Craft Iluminación", "125", "+54 9 1166337427", "decocraft@hotmail.com", "", "@craft_dec2", "", "Itaqui 2182, CABA", "Iluminación"],
    ["Broderi Manteles", "111", "+549 1162966000", "broderidesign@gmail.com", "broderi.com.ar", "@broderi.manteles", "", "Entre Rios 2056, Olivos (CP1636), Buenos Aires", "Bazar, Platería"],
    ["Ebony", "248", "+54 9 11 45883857 / +54 9 1158423499", "administracion@e-bony.com.ar", "e-bony.com.ar", "@ebonymueblesok", "", "Paysandu 1451 CP 1416 CABA", "Muebles"],
    ["Botany Buenos Aires", "237", "+54 9 11 2280 7278", "botanybuenosaires@gmail.com", "", "@Botany.bsas", "", "Quilmes, Buenos Aires (CP1879)", "Velas y Esencias"],
    ["Datelux", "257", "4855-1212 / +54 9 1136929553", "info@datetux.com.ar", "", "@Dateluxok", "", "Scalabrini Ortiz 250, CP 1414, CABA", "Iluminación"],
    ["By Feli Deco", "268", "+54 9 1130092394", "byfelideco.tienda@gmail.com", "linktr.ee/By_felideco", "@byfelideco", "", "CABA", "Objetos Deco, Textil Hogar"],
    ["Lola Deco", "274", "+54 9 1138097211 / +54 9 1123721176", "loladecoarg@gmail.com", "lola-deco.negocio.site", "@loladecoarg", "", "El Talar CP 1617, Buenos Aires", "Sillones"],
    ["Mirador", "225", "45525055 / +54 9 1155843078", "miradorobjetos@gmail.com", "mirador.com.ar", "@miradorporelmundo", "", "Giribone 1960, CABA (CP1427)", "Objetos Deco"],
    ["Leder", "100", "+54 9 1151857964", "info@lederhd.com", "lederhd.com", "@Leder_hd", "", "Av. Libertador 13821, Martínez, Buenos Aires (CP1640)", "Alfombras, Muebles, Objetos Deco, Sillones"],
    ["Desde Asia", "214", "+54 9 1147710073 / +54 9 11 3167-4471", "consultas@desdeasia.com.ar", "desdeasia.com", "@desde_asia", "", "Malabia 1359, Palermo (CP1414), Buenos Aires", "Muebles, Objetos Deco"],
    ["Cueros Especiales", "215", "+54 9 11 64486916 / +54 9 11 42284886", "info@cuerosespeciales.com", "cuerosespeciales.com", "@cueros_especiales", "", "Pte. Perón 3145, Valentín Alsina / Av. Hipólito Yrigoyen 6602, Lanús", "Sillones"],
    ["Cadmia", "231", "+54 9 1124712225", "info@cadmia.com.ar", "cadmia.com.ar", "@cadmiahome", "", "Juncal 1115, CABA (1062)", "Textil Hogar"],
    ["Estilo Domingo", "269", "+54 9 3472 532010", "Hola@estilodomingo.com.ar", "estilodomingo.com.ar", "@estilo.domingo", "", "Córdoba", "Objetos Deco"],
    ["Ecléctica Diseño", "141", "+54 9 3516312332 / +54 9 3515936034", "Iameclectica@gmail.com", "eclecticadiseno.com.ar", "@eclectica.diseno", "", "Doctor Orlando Severo Melone 250, Córdoba (CP5000)", "Objetos Deco"],
    ["Casi un Ángel", "147", "+54 9 2215736756", "Fabivaioli@gmail.com", "casiunangeldeco.mitiendanube.com", "@Casiunangel_deco", "", "Calle 77 n°1886, La Plata (CP1900), Buenos Aires", "Borlas"],
    ["Fabric AR", "142", "+54 9 1163677970", "mrc_sofa@hotmail.com", "", "@fabricaar", "", "Martin Peschel 600, Tres de Febrero (CP1657), Buenos Aires", "Sillones"],
    ["Forevents", "207", "+54 9 11 64331266 / +54 9 1164055659", "info@forevents.com.ar", "Forevents.com.ar", "@Forevents_", "", "Hipólito Yrigoyen 1764, Garín (CP1619), Buenos Aires", "Muebles, Sillas, Sillones"],
    ["Galpón", "244", "3564 508778", "galponmuebles@gmail.com", "", "@Galponmuebles", "", "Calle 9, Frontera (CP2348), Santa Fe", "Muebles, Sillas, Sillones"],
    ["Lampsilver", "275", "+54 9 11 62446973 / +54 9 1130684132", "Lampsilver@gmail.com", "Lampsilver.com.ar", "@Lampsilver", "", "Ayacucho 662, Florida – Vte Lopez (CP1642), Buenos Aires", "Iluminación"],
    ["Ortiga", "121", "+54 9 1135914398", "Ortigacasa.ar@gmail.com", "Ortiga.com.ar", "@Ortigacasa", "", "CABA", "Vajilla"],
]

for row_idx, expositor in enumerate(expositores, 2):
    for col_idx, value in enumerate(expositor, 1):
        cell = ws.cell(row=row_idx, column=col_idx, value=value)
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)

col_widths = [25, 8, 35, 35, 30, 25, 22, 45, 30]
for i, width in enumerate(col_widths, 1):
    ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = width

ws.auto_filter.ref = f"A1:{openpyxl.utils.get_column_letter(len(headers))}{len(expositores)+1}"
ws.freeze_panes = "A2"

output_path = "/home/user/AUREA-Hub/Expositores_CAFIRA_2026.xlsx"
wb.save(output_path)
print(f"Excel generado: {output_path}")
print(f"Total expositores: {len(expositores)}")
