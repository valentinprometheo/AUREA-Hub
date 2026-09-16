# Manifiesto de assets · verificado

Inventario de los assets de marca de la skill, con su estado. Auditado y probado
por render (headless Chromium) el 2026-09-16: el logo y la esfera se embeben y
renderizan, y las tipografías cargan.

## Assets de marca

| Archivo | Qué es | Formato | Estado |
|---|---|---|---|
| `deck/logo.txt` | Logo AUREA (wordmark "áurea" + orbe), fondo transparente | data URI PNG 460×416 | ✅ vigente, verificado por render |
| `deck/sphere.txt` | Esfera iridiscente (decoración secundaria) | data URI PNG 560×560 | ✅ vigente, verificado por render |
| `deck/aurea-drakon.css` | Sistema de diseño canónico (el de DRAKON) | CSS 43 KB | ✅ portado del DRAKON real, verificado por render |
| `ejemplos/demo-sistema-drakon.html` | Demo mínimo validado con el sistema DRAKON | HTML | ✅ renderiza con bandas, price cards e íconos |
| `deck/isotipo.svg` / `deck/isotipo.txt` | Isotipo AUREA (marca sola, sin wordmark) | SVG vectorial (+ data URI) | ✅ integrado, `ISOTIPO` en el kit, verificado por render |
| `deck/aurea_kit.py` | Motor del deck: CSS canónico, íconos SVG inline, wrappers HTML, render a PDF | Python | ✅ importa y genera HTML válido |
| `nda/NDA-AUREA-template-base.docx` | Template legal oficial (Familia B) | .docx | ✅ presente, fuente de verdad |
| `ejemplos/drakon-ventas-marketing.html` | Deck oficial real (referencia de diseño exacta) | .html con CSS + contenido | ✅ presente, con `<body>` |

## Tipografías (confirmado contra el deck real DRAKON)

- **Cuerpo y títulos:** Arimo (métricamente compatible con Helvetica). Variable `--hel`.
- **Acento en itálica:** **Fraunces**. Variable `--accent`.
- Se cargan por Google Fonts (`fonts.googleapis.com`), requieren red al momento de render.
- **Nota sobre "Rischie":** el kit y el deck real de DRAKON traen el comentario
  "swap for Rischie when available". Rischie **nunca se usó en producción**: los decks
  vigentes (DRAKON) usan Fraunces. Por lo tanto Fraunces es la tipografía de acento
  oficial de la skill y no falta ningún archivo. Si algún día se consigue el `.woff2`
  de Rischie, se agrega con `@font-face` vía `extra_css` en `aurea_page(...)` y se
  cambia `--accent`; es una mejora opcional, no un hueco.

## Cómo reemplazar un asset (si la marca actualiza)

- **Logo o esfera nuevos:** recortá el PNG/SVG con fondo transparente, convertí a data
  URI base64 y reemplazá el contenido de `logo.txt` / `sphere.txt` (una sola línea
  `data:image/png;base64,...`). Verificá con un render antes de dar por bueno.
- **Tipografía real:** `@font-face` con el `.woff2/.otf` vía `extra_css`, y ajustá la
  variable CSS correspondiente.

## Chequeo de integridad (correr si se duda)

```python
import base64, re
for f in ["deck/logo.txt","deck/sphere.txt"]:
    s=open(f).read().strip()
    m=re.match(r'data:image/(\w+);base64,(.*)', s, re.S)
    raw=base64.b64decode(m.group(2))
    assert raw[:8]==b'\x89PNG\r\n\x1a\n', f"{f} no es PNG"
    print(f, "OK", int.from_bytes(raw[16:20],'big'),"x",int.from_bytes(raw[20:24],'big'))
```
