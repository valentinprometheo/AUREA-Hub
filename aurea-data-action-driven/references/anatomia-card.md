# Anatomía de la card

Respeta la card del tablero de IC de EDFAN. Cuatro bloques, siempre en este orden:

| Bloque | Contenido | Regla |
|---|---|---|
| Sello | Verbo + dueño | Uno de seis verbos, uno de cuatro dueños |
| Título | "Tema · dato principal" | El número va en el título, no escondido |
| Contexto | Qué mide / Base / Dato (fuente) | Siempre visible, también plegada |
| Despliegue | Qué hacer / Dónde se cambia / Efecto esperado / Cómo lo medimos | En documentos estáticos va todo abierto |

En el tablero la card usa `<details>` para desplegar sin JavaScript. Superficie neutra;
el único color es el del sello (`taxonomia-verbos.md`). Modo oscuro con tokens.

## HTML de referencia

```html
<article class="act-card" data-verbo="corregir">
  <header class="act-sello">
    <span class="act-verbo">Corregir</span><span class="act-dueno">AUREA</span>
  </header>
  <h3 class="act-titulo">Mensajes por lead · 406 leads de una consulta recibieron 4,8 mensajes</h3>
  <dl class="act-contexto">
    <div><dt>Qué mide</dt><dd>Mensajes del agente por lead con una sola consulta</dd></div>
    <div><dt>Base</dt><dd>406 leads</dd></div>
    <div><dt>Dato</dt><dd>1.949 envíos <cite>Prometheo · consumo 1 al 15/10</cite></dd></div>
  </dl>
  <details class="act-accion">
    <summary>Qué hago ahora</summary>
    <dl>
      <div><dt>Qué hacer</dt><dd>Primera respuesta con la entrega + una sola pregunta</dd></div>
      <div><dt>Dónde se cambia</dt><dd>Prompt del agente, sección de primera respuesta</dd></div>
      <div><dt>Efecto esperado</dt><dd>−1.118 envíos en el próximo período</dd></div>
      <div><dt>Cómo lo medimos</dt><dd>Mensajes por lead de una consulta, misma base. Guardiana: % de calificación</dd></div>
    </dl>
  </details>
</article>
```

## CSS de referencia

```css
:root {
  --card-bg: #FFFFFF; --card-borde: #E4E7EC; --texto: #1D2939; --texto-2: #667085;
  --corregir-bg: #FDE8E4; --corregir-tx: #B42318;
  --proteger-bg: #FEF3C7; --proteger-tx: #92400E;
  --separar-bg: #E8ECF1;  --separar-tx: #344054;
  --medir-bg: #E0F2F1;    --medir-tx: #0F6E6E;
  --decidir-bg: #E9E7FB;  --decidir-tx: #3F3A9E;
  --activar-bg: #E3F4E8;  --activar-tx: #1E6B3A;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --card-bg: #161B26; --card-borde: #2A3140; --texto: #F2F4F7; --texto-2: #98A2B3;
    --corregir-bg: #3B1A16; --corregir-tx: #FDA29B;
    --proteger-bg: #3A2A0C; --proteger-tx: #FCD34D;
    --separar-bg: #252B37;  --separar-tx: #CBD5E1;
    --medir-bg: #0E2E2E;    --medir-tx: #5FD4CF;
    --decidir-bg: #23214A;  --decidir-tx: #B4AEF5;
    --activar-bg: #12301E;  --activar-tx: #7DD8A0;
  }
}
.act-card { background: var(--card-bg); border: 1px solid var(--card-borde);
  border-radius: 10px; padding: 16px; color: var(--texto); font-family: Arimo, sans-serif; }
.act-sello { display: inline-flex; gap: 8px; align-items: center; padding: 3px 10px;
  border-radius: 999px; font-size: 12px; font-weight: 700; letter-spacing: .04em;
  text-transform: uppercase; background: var(--v-bg); color: var(--v-tx); }
.act-dueno { font-weight: 400; opacity: .85; }
.act-dueno::before { content: "· "; }
.act-titulo { font-size: 16px; line-height: 1.35; margin: 10px 0 8px;
  font-variant-numeric: tabular-nums; }
.act-contexto, .act-accion dl { display: grid; gap: 4px; margin: 0; font-size: 13px; }
.act-contexto div, .act-accion dl div { display: grid; grid-template-columns: 9em 1fr; gap: 8px; }
dt { color: var(--texto-2); } dd { margin: 0; }
cite { color: var(--texto-2); font-style: normal; font-size: 12px; }
.act-accion { margin-top: 10px; border-top: 1px solid var(--card-borde); padding-top: 8px; }
.act-accion summary { cursor: pointer; font-weight: 700; font-size: 13px; }
[data-verbo="corregir"] { --v-bg: var(--corregir-bg); --v-tx: var(--corregir-tx); }
[data-verbo="proteger"] { --v-bg: var(--proteger-bg); --v-tx: var(--proteger-tx); }
[data-verbo="separar"]  { --v-bg: var(--separar-bg);  --v-tx: var(--separar-tx); }
[data-verbo="medir"]    { --v-bg: var(--medir-bg);    --v-tx: var(--medir-tx); }
[data-verbo="decidir"]  { --v-bg: var(--decidir-bg);  --v-tx: var(--decidir-tx); }
[data-verbo="activar"]  { --v-bg: var(--activar-bg);  --v-tx: var(--activar-tx); }
@media (max-width: 480px) {
  .act-contexto div, .act-accion dl div { grid-template-columns: 1fr; gap: 0; }
}
```

Para `[data-theme="dark"]` repetí el bloque oscuro bajo `:root[data-theme="dark"]`.
