# Rutina nocturna: reuniones desde las notas de Gemini en Drive

`/brain-dreaming` espera un conector de transcripciones (Granola, Fireflies). En AUREA las reuniones
las toma **Gemini en Google Meet** y quedan en Google Drive. Este archivo reemplaza el paso 3
(reuniones) de la rutina. La config está en `config/dreaming.config.json`.

## Cómo las encuentra
- Conector: Google Drive (ya conectado).
- Búsqueda: `title contains 'Notes by Gemini' and mimeType = 'application/vnd.google-apps.document'
  and modifiedTime > '<inicio de la ventana>'`.
- Se descartan los **accesos directos** (`application/vnd.google-apps.shortcut`): Drive crea uno
  por carpeta de reunión y duplicaría todo.
- Muchas reuniones tienen **dos documentos**, "(Spanish)" y "(English)". Se procesa el de español
  y el otro se registra como visto. Si solo hay uno, se procesa ese.
- Notas de otra persona del equipo (Magalí, Rodrigo) o de un partner (Prometheo) también aparecen
  si se las compartieron a la cuenta; se procesan igual.
- Registro para no repetir: el **ID del documento de Drive** va a `reuniones-ledger.json`.

## Cómo asigna cada reunión a un cliente
1. Por el título: si contiene el nombre de un proyecto de `1. Proyectos/` (EDFAN, ZATOH, BETROX,
   MIA, TKVA, DRAKON, PAVIR, EAF, MAMUT, G&D), va a ese proyecto. "EDFAN Productos y ZATOH" va a
   los dos.
2. Si el título es genérico ("Meeting started…", "Untitled Meeting"), lee el resumen y busca el
   cliente por nombre o por el dominio de los invitados. Si no lo encuentra, va a
   `0. Inbox/reuniones-por-ubicar/` con sus temas sugeridos.
3. Reuniones de partners ("Prometheo Mensual Partners", agencias) van a `2. Áreas/partners/`.

**Recomendación:** nombrar siempre la reunión con el cliente al principio del título
("TKVA · seguimiento octubre"). Es lo que hace que se archive sola.

## Qué escribe
- En `1. Proyectos/<cliente>/log.md`: una entrada con fecha, decisiones ("Acordada" y "Requiere más
  debate" de Gemini) y próximos pasos con responsable.
- Los próximos pasos con día y hora explícitos y responsable de AUREA van al calendario propio
  (sin invitados). Los demás, como tarea o como marca en el estado del cliente.
- Nada se manda a nadie. Mails, mensajes al cliente o invitaciones quedan marcados para decidir.

## Casos que ya vimos en el Drive (octubre 2026)
- Notas vacías: "A summary wasn't produced…" (EAF, 22/10). Se registra la reunión, se marca
  "sin resumen: revisar la transcripción" y no se inventa contenido.
- Títulos sin cliente: "Meeting started 2026/10/20 08:33", "Untitled Meeting". Van al paso 2.
- Gemini resume en tercera persona y a veces deforma nombres ("Javier Esculi", "Prometeo"). Se
  corrigen contra `CLAUDE.md` antes de escribir.

## Mail
Gemini también manda las notas por mail. Para no procesar dos veces la misma reunión, la consulta de
Gmail excluye esos mails (ver `gmail.query` en la config) y la reunión sale solo de Drive.
