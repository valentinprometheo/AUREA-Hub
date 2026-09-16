# QA Checklist, NDA AUREA

Lista exhaustiva para verificar antes de entregar un documento. La validación
de esquema XML no alcanza, hay que mirar el output renderizado.

## Pre-entrega

### Validación técnica

- [ ] `validate.py` reporta `All validations PASSED!`
- [ ] Conteo de párrafos coherente: no debe haber explosión (chequear delta con `pack.py`). Aumento esperado para una edición de cláusula completa: +/- 10 párrafos. Aumentos de +100 o más indican que se duplicó contenido.
- [ ] `diff` entre el XML editado y el original muestra cambios solo en las zonas tocadas. Si hay cambios en líneas que no se debieron tocar, hay un bug.

### Validación visual

Generar PDF con soffice y rasterizar:

```bash
python /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf output.docx
pdftoppm -jpeg -r 95 output.pdf page
```

Revisar cada página:

- [ ] Portada idéntica al template original. Logo, título "ACUERDO DE CONFIDENCIALIDAD" en violeta, subtítulo en itálica gris, fecha, línea horizontal divisoria.
- [ ] Barras "PARTE DIVULGANTE..." y "PARTE RECEPTORA — CLIENTE" en violeta pleno con texto blanco.
- [ ] Cajas de detalle con fondo lila claro y labels en violeta bold.
- [ ] Encabezados de cláusula en violeta `#9900ff` bold con tipografía Calibri.
- [ ] Letras a) b) c) en violeta bold dentro de las listas.
- [ ] Tabla de Condiciones Comerciales con header violeta y columnas auxiliares en itálica gris.
- [ ] Total / subtotales correctos en la tabla (re-sumar manualmente).
- [ ] Tipo de cambio + IVA en itálica gris debajo de cada tabla.
- [ ] Bloque FIRMAS con dos tarjetas: header violeta + cuerpo gris claro.
- [ ] Firma de Magalí escaneada visible en la tarjeta de la Parte Divulgante.
- [ ] Línea para firma de la Parte Receptora vacía (lista para firmar).
- [ ] Fechas consistentes en título, pie de firma Divulgante, pie de firma Receptora.
- [ ] Frase de cierre en itálica gris centrada.

### Contenido

- [ ] Razones sociales y CUITs correctos (cotejar con datos del cliente).
- [ ] Domicilios correctos.
- [ ] Nombre, DNI y carácter del representante del cliente correctos.
- [ ] Email del representante correcto.
- [ ] Considerando II refleja correctamente el negocio del cliente (no copiar el del template si tiene varias unidades de negocio).
- [ ] Si hay Cláusula de Protección de Datos extendida (Prometheo/ITESA/GDPR): completar el corchete de ley local según jurisdicción del cliente (25.326 AR, 18.331 UY, 6534/2020 PY).
- [ ] Cláusula Undécima refleja el deal real del cliente (no el placeholder del template).
- [ ] Si hay varias sociedades facturantes: una tabla por sociedad + total general.
- [ ] Forma de pago coincide con lo acordado (echeqs, mensual, único).
- [ ] Montos: confirmados reales tal cual, sugeridos con "(sugerido)", desconocidos en rojo `#C00000`.

### Reglas AUREA

- [ ] Voseo rioplatense en cuerpo que escribimos nosotros.
- [ ] Cero em-dashes (—) en cláusulas nuevas que generamos. En zonas heredadas del template tomar la decisión con Valentín.
- [ ] AUREA sin tilde en cláusulas nuevas. En barras del template heredado, no tocar a menos que Valentín lo pida.
- [ ] Nombres correctos: Magalí Domínguez, Valentín Zas, Sebastián Mato (o el que aplique).
- [ ] Placeholders en rojo bold con `color="C00000"`. NUNCA con `highlight: "yellow"`.

## Casos vistos

### Cliente EDFAN

- **Parte Receptora**: 4 marcas comerciales bajo 3 razones sociales distintas. EDFAN Real Estate → CGND S.A. + EDFAN S.R.L. BETROX, EDFAN Productos y ZATOH → BS Construcciones S.A.
- **Representante único**: Sebastián Mato como Apoderado de las tres sociedades.
- **Cláusula Undécima**: pago único (no recurrente) en 10 echeqs a 0, 10, 20, 30, 40, 50, 60, 70, 80 y 90 días. Dos tablas separadas por sociedad facturante. Total USD 4.929,10 / ARS 7.147.195 al tipo de cambio ARS 1.450.
- **Cláusula Quinta extendida**: versión Prometheo/ITESA/GDPR + Ley 25.326 (Argentina). Cinco incisos (a-e) cubriendo definición de Datos, roles responsable/encargados, estándar GDPR + ley local, acceso restringido, medidas técnicas + notificación de incidentes, devolución/eliminación a 30 días.
- **Considerando II**: ampliado de "proyectos inmobiliarios" a "distintas unidades de negocio (desarrollos inmobiliarios, mobiliario, productos e insumos para la construcción y revestimientos)" para cubrir las 4 marcas.

### Pendientes generales

- **Contrato de encargo de tratamiento de ITESA**: cuando esté disponible, reforzar la Cláusula Quinta con referencia al contrato y ubicación de servidores. Hoy es declarativa.
- **Revisión legal**: el contenido es borrador, no asesoramiento jurídico. Conviene revisión de abogado, sobre todo si hay varias sociedades obligadas con una sola firma (verificar facultades del apoderado).

## Si Valentín reporta "se ve distinto" entre lo que renderizo yo y el original

Antes de tocar nada:

1. Hacer `diff` del XML editado vs el original. Si los cambios están solo en las zonas tocadas, el archivo está bien.
2. Recordarle a Valentín que LibreOffice (`soffice`, mi motor de QA) renderiza Calibri con métricas distintas a Google Docs. Diferencias de espaciado, tamaño relativo del logo y posición del título son artefactos de rendering, no del archivo.
3. Sugerirle abrir el `.docx` en Google Docs o subir a Drive para ver el rendering real.
4. Solo si el diff XML muestra cambios fuera de las zonas esperadas, hay un bug del lado de la edición.
