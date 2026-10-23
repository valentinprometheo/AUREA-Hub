# Cómo poner en marcha este brain

1. **Copiar esta carpeta** a la unidad compartida de AUREA en Google Drive (por ejemplo
   `AUREA/AUREA-Brain`) y sincronizarla con Drive para escritorio en la compu que la va a usar.
2. **Instalar el plugin `brain`:**
   - Cowork: Customize → Plugins → Add marketplace → `brunogiel/agentic-second-brain` → Install.
   - Claude Code: `/plugin marketplace add brunogiel/agentic-second-brain` y
     `/plugin install brain@agentic-second-brain`.
3. **Abrir la carpeta** en Cowork o Claude Code y escribir `/brain`. El coach detecta que el
   `CLAUDE.md` ya existe y no pisa nada.
4. **Conectores** (claude.ai → Settings → Connectors): Gmail, Google Calendar y Google Drive ya están.
   Slack no hace falta. Las reuniones salen de las notas de Gemini en Drive.
5. **Rutina nocturna** (solo en la compu que queda prendida, con Claude Code):
   - Copiar `3. Recursos/config/dreaming.config.json` a `~/.config/dreaming/config.json` y poner la
     ruta real en `brain_root`.
   - Crear la tarea programada con el prompt `/brain-dreaming`, todos los días a las 05:00.
   - Pre-aprobar solo lectura de Gmail, Calendar y Drive, y escritura en la carpeta del brain.
     Nunca enviar mails, invitar ni borrar.
6. **Skills de AUREA:** subir a claude.ai los zips de `skills-corregidas/2026-10-23/` (una skill por
   zip) y desinstalar `aurea-hub-criterio-calificacion-leads` cuando esté la metodología v1.31.

Lo que falta definir: dónde viven las tareas del equipo (Notion u otra) y si el brain es uno
compartido o uno por persona (recomendado: uno compartido de AUREA).
