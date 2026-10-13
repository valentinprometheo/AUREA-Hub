// =============================================================
// Skill: prometheo-diseno-agente-ia-feedback
// Genera el Documento de Feedback de Demo (Etapa 2 — iteración).
// Uso: npm install docx && node generar_documento.js
// Salida: /mnt/user-data/outputs/
// Para personalizar por cliente, ajustar el bloque ENCABEZADO.
// =============================================================
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign,
        PageOrientation } = require('docx');
const fs = require('fs');

const MORADO   = "7C5CBF";
const NARANJA  = "E8943A";
const AZUL     = "5B8FD9";
const OSCURO   = "2D2D3D";
const GRIS     = "7A7A7A";
const NARANJA_CLARO = "FFE5C2";
const BLANCO   = "FFFFFF";
const FONT = "Calibri";

function txt(text, opts = {}) {
  return new TextRun({ text, font: FONT, size: opts.size || 22,
    bold: opts.bold || false, italics: opts.italics || false,
    color: opts.color || OSCURO });
}
function para(runs, opts = {}) {
  return new Paragraph({
    children: Array.isArray(runs) ? runs : [runs],
    spacing: { after: opts.after != null ? opts.after : 120, before: opts.before || 0, line: 276 },
    alignment: opts.alignment || AlignmentType.LEFT,
  });
}
function bullet(runs, opts = {}) {
  return new Paragraph({
    children: Array.isArray(runs) ? runs : [runs],
    bullet: { level: 0 },
    spacing: { after: opts.after != null ? opts.after : 70, line: 276 },
  });
}
function allBorders(color, size) {
  const b = { style: BorderStyle.SINGLE, size: size || 4, color: color || GRIS };
  return { top: b, bottom: b, left: b, right: b };
}
function callout(children, fill, borderColor) {
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [ new TableRow({ children: [ new TableCell({
      shading: { type: ShadingType.CLEAR, fill: fill, color: "auto" },
      margins: { top: 140, bottom: 140, left: 200, right: 200 },
      borders: allBorders(borderColor, 8),
      children: children
    })]})]
  });
}
function spacer(h) { return new Paragraph({ children: [], spacing: { after: h || 200 } }); }

const content = [];

// ENCABEZADO
content.push(para(txt("AUREA HUB × PROMETHEO", { bold: true, size: 18, color: MORADO }), { after: 50 }));
content.push(para(txt("Documento de Feedback — Iteración del Agente IA", { bold: true, size: 34, color: OSCURO }), { after: 50 }));
content.push(para([
  txt("Etapa 2 — Diseño del Agente Inteligente · ", { size: 22, color: GRIS, bold: true }),
  txt("fase de iteración del prompt.", { size: 22, color: GRIS, italics: true }),
], { after: 160 }));

// INSTRUCCIONES — bloque corto
content.push(callout([
  para(txt("CÓMO SE COMPLETA", { bold: true, size: 20, color: NARANJA }), { after: 90 }),
  bullet([ txt("Una fila por corrección. ", { bold: true }), txt("Izquierda: la captura de la respuesta del agente. Derecha: qué está mal y cómo debería responder.", {}) ]),
  bullet([ txt("Antes de capturar, ", {}), txt("subrayá o recuadrá", { bold: true }), txt(" el sector que estás criticando. La captura llega con la marca puesta.", {}) ]),
  bullet([ txt("No taches ni tapes el texto con líneas. ", { bold: true }), txt("Necesitamos leer qué respondió mal — marcá señalando, sin cubrir.", {}) ]),
  bullet([ txt("Necesitás más filas: ", {}), txt("copiá una fila en blanco y pegala al final.", { bold: true }) ], { after: 0 }),
], NARANJA_CLARO, NARANJA));

content.push(spacer(120));

// DÓNDE SE GUARDA — una línea
content.push(para([
  txt("Dónde se guarda:  ", { bold: true, size: 20, color: AZUL }),
  txt("Drive del proyecto → Etapa 2 — Diseño del Agente Inteligente → carpeta \"Iteración cliente\".", { size: 20, color: GRIS }),
], { after: 200 }));

// EL CUADRO
function headerCell(text) {
  return new TableCell({
    shading: { type: ShadingType.CLEAR, fill: OSCURO, color: "auto" },
    margins: { top: 110, bottom: 110, left: 160, right: 160 },
    verticalAlign: VerticalAlign.CENTER,
    borders: allBorders(OSCURO, 4),
    width: { size: 50, type: WidthType.PERCENTAGE },
    children: [ para(txt(text, { bold: true, size: 20, color: BLANCO }), { after: 0, alignment: AlignmentType.CENTER }) ]
  });
}
function bodyCell(children, fill) {
  return new TableCell({
    shading: fill ? { type: ShadingType.CLEAR, fill: fill, color: "auto" } : undefined,
    margins: { top: 160, bottom: 160, left: 160, right: 160 },
    borders: allBorders(GRIS, 4),
    width: { size: 50, type: WidthType.PERCENTAGE },
    verticalAlign: VerticalAlign.TOP,
    children: children
  });
}

const headerRow = new TableRow({
  tableHeader: true,
  children: [ headerCell("LA IMAGEN CRÍTICA / SITUACIÓN CRÍTICA"), headerCell("LA CORRECCIÓN") ]
});

const ejemploRow = new TableRow({
  cantSplit: true,
  children: [
    bodyCell([
      para(txt("EJEMPLO", { bold: true, size: 18, color: NARANJA }), { after: 80 }),
      para(txt("[ Captura de pantalla de la respuesta del agente, con el sector criticado ya subrayado. ]", { italics: true, color: GRIS, size: 20 }), { after: 0 }),
    ], NARANJA_CLARO),
    bodyCell([
      para(txt("EJEMPLO", { bold: true, size: 18, color: NARANJA }), { after: 80 }),
      para([ txt("Qué está mal: ", { bold: true, size: 20 }), txt("tira el precio sin antes preguntar qué busca el cliente. Suena frío.", { size: 20 }) ], { after: 60 }),
      para([ txt("Cómo debería responder: ", { bold: true, size: 20 }), txt("preguntar primero un par de cosas y recién después pasar el precio con contexto.", { size: 20 }) ], { after: 0 }),
    ], NARANJA_CLARO),
  ]
});

function emptyRow() {
  const left = [
    para(txt("[ Pegá acá la captura — con el sector criticado subrayado o recuadrado. ]", { italics: true, color: GRIS, size: 20 }), { after: 0 }),
    spacer(900),
    para([ txt("Situación: ", { bold: true, size: 20, color: GRIS }) ], { after: 0 }),
  ];
  const right = [
    para([ txt("Qué está mal: ", { bold: true, size: 20, color: GRIS }) ], { after: 700 }),
    para([ txt("Cómo debería responder: ", { bold: true, size: 20, color: GRIS }) ], { after: 0 }),
  ];
  return new TableRow({ cantSplit: true, children: [ bodyCell(left), bodyCell(right) ] });
}

const tableRows = [ headerRow, ejemploRow ];
for (let i = 0; i < 4; i++) tableRows.push(emptyRow());

content.push(new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  rows: tableRows,
}));

content.push(spacer(180));
content.push(para(txt("Equipo AUREA Hub", { bold: true, color: MORADO, size: 22 }), { after: 0 }));

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840, orientation: PageOrientation.LANDSCAPE },
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 }
      }
    },
    children: content
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/mnt/user-data/outputs/Documento de Feedback - Iteracion del Agente IA.docx", buffer);
  console.log("DOCX generado OK");
});
