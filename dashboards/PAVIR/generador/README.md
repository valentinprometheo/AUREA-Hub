# Generador del tablero de IC · PAVIR

Arma `../Dashboard_Inteligencia_Comercial_-_Aurea_Hub_PAVIR.html` (HTML autocontenido).

```
python3 build.py
```

| Archivo | Qué tiene |
|---|---|
| `data.py` | Datos **ilustrativos (demo)**. Todos los totales se calculan acá para que ninguna cifra se contradiga entre pestañas. |
| `css.py` | Tokens de marca AUREA, modo oscuro y componentes. |
| `icons.py` | Sprite de íconos (se define una vez y se usa con `<use>`). |
| `comp.py` | Componentes: card de insight en 3 subsectores (`i3`), KPI, barras, tablas, chips de fuente y nivel. |
| `charts.py` | Gráficos SVG (barras mensuales, sparkline, torta). |
| `p_*.py` | Una función por pestaña. |

Reglas que respeta el generador:
- Básico agrega `.bsc`, Avanzado agrega `.adv`: el switch cambia algo en todas las pestañas.
- Card de insight: subsector 1 visible (sello, nombre literal, campaña › conjunto › anuncio); 2 y 3 plegados.
- Ninguna cifra suma dos fuentes: Prometheo define cuántas consultas hubo.
