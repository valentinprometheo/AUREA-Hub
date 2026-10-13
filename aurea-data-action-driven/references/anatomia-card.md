# Anatomía de la card

Respeta la card del tablero de IC de EDFAN y le suma el score bajo el título.

| Bloque | Contenido | Regla |
|---|---|---|
| Sello | Verbo + dueño | Uno de seis verbos, uno de cuatro dueños |
| Título | "Tema · dato principal" | El número va en el título |
| Score | "85% basada en datos" + barra + etiqueta de banda | Grande, pegado al título |
| Contexto | Qué mide / Base / Dato (fuente) | Visible también plegada |
| Despliegue | Qué hacer / Dónde se cambia / Efecto esperado / Cómo lo medimos / Por qué este score | En documentos estáticos, todo abierto |

Superficie neutra. Color solo en el sello (verbo) y en la barra del score (banda).

```html
<article class="act-card" data-verbo="corregir">
  <header class="act-sello"><span>Corregir</span><span class="act-dueno">AUREA</span></header>
  <h3 class="act-titulo">Mensajes por lead · 406 leads de una consulta recibieron 4,8 mensajes</h3>
  <div class="act-score" data-banda="alta" style="--score:85">
    <strong>85%</strong><span>basada en datos</span><i aria-hidden="true"></i>
  </div>
  <dl class="act-ctx">
    <div><dt>Qué mide</dt><dd>Mensajes del agente por lead con una sola consulta</dd></div>
    <div><dt>Base</dt><dd>406 leads</dd></div>
    <div><dt>Dato</dt><dd>1.949 envíos <cite>Prometheo · 1 al 15/10</cite></dd></div>
  </dl>
  <details class="act-accion"><summary>Qué hago ahora</summary><dl class="act-ctx">
    <div><dt>Qué hacer</dt><dd>Primera respuesta con la entrega + una sola pregunta</dd></div>
    <div><dt>Dónde se cambia</dt><dd>Prompt del agente, sección de primera respuesta</dd></div>
    <div><dt>Efecto esperado</dt><dd>−1.118 envíos en el próximo período</dd></div>
    <div><dt>Cómo lo medimos</dt><dd>Mensajes por lead de una consulta. Guardiana: % de calificación</dd></div>
    <div><dt>Por qué este score</dt><dd>Base 20 · Fuente 10 · Cobertura 15 · Profundidad 20 · Evidencia 5 · Cierre 15</dd></div>
  </dl></details>
</article>
```

```css
:root{--bg:#FFF;--borde:#E4E7EC;--tx:#1D2939;--tx2:#667085;
 --alta:#1E6B3A;--media:#3F6FB0;--hipo:#B45309;--crit:#667085}
.act-card{background:var(--bg);border:1px solid var(--borde);border-radius:10px;padding:16px;
 color:var(--tx);font-family:Arimo,sans-serif;font-variant-numeric:tabular-nums}
.act-sello{display:inline-flex;gap:8px;padding:3px 10px;border-radius:999px;font-size:12px;
 font-weight:700;letter-spacing:.04em;text-transform:uppercase;background:var(--v-bg);color:var(--v-tx)}
.act-dueno{font-weight:400}.act-dueno::before{content:"· "}
.act-titulo{font-size:17px;line-height:1.35;margin:10px 0 6px}
.act-score{display:grid;grid-template-columns:auto 1fr;align-items:baseline;gap:2px 8px;margin-bottom:10px}
.act-score strong{font-size:26px;color:var(--b)}.act-score span{font-size:13px;color:var(--tx2)}
.act-score i{grid-column:1/-1;height:6px;border-radius:3px;
 background:linear-gradient(90deg,var(--b) calc(var(--score)*1%),var(--borde) 0)}
[data-banda="alta"]{--b:var(--alta)}[data-banda="media"]{--b:var(--media)}
[data-banda="hipotesis"]{--b:var(--hipo)}[data-banda="criterio"]{--b:var(--crit)}
.act-ctx{display:grid;gap:4px;margin:0;font-size:13px}
.act-ctx div{display:grid;grid-template-columns:9em 1fr;gap:8px}
dt,cite{color:var(--tx2);font-style:normal}dd{margin:0}
.act-accion{margin-top:10px;border-top:1px solid var(--borde);padding-top:8px}
.act-accion summary{cursor:pointer;font-weight:700;font-size:13px}
@media (max-width:480px){.act-ctx div{grid-template-columns:1fr;gap:0}}
```

Colores de sello por verbo (fondo / texto): corregir `#FDE8E4/#B42318`, proteger
`#FEF3C7/#92400E`, separar `#E8ECF1/#344054`, medir `#E0F2F1/#0F6E6E`, decidir
`#E9E7FB/#3F3A9E`, activar `#E3F4E8/#1E6B3A`. Se asignan con
`[data-verbo="x"]{--v-bg:...;--v-tx:...}`. Para modo oscuro, redefiní los tokens bajo
`@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){...}}` y bajo
`:root[data-theme="dark"]` (`aurea-dashboard-design`).
