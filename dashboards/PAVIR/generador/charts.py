"""Gráficos en SVG inline: barras mensuales, barras apiladas, sparkline y torta."""
import math
from comp import fmt


def _ticks(mx):
    step = 10 ** math.floor(math.log10(mx))
    for m in (0.1, 0.2, 0.25, 0.5, 1, 2, 2.5, 5, 10):
        if mx / (step * m) <= 5:
            s = step * m
            break
    top = math.ceil(mx / s) * s
    return top, [s * i for i in range(int(round(top / s)) + 1)]


def bars_month(labels, series, colors, fmt_v=lambda v: fmt(v), h=230, w=1000, highlight_last=True, line=None, line_label=""):
    """series: lista de listas (apiladas). line: serie opcional de referencia (ej. objetivo)."""
    n = len(labels)
    tot = [sum(s[i] for s in series) for i in range(n)]
    mx = max(tot + (line or [0]))
    top, ticks = _ticks(mx * 1.05)
    pl, pr, pt, pb = 50, 8, 20, 24
    cw = (w - pl - pr) / n
    bw = cw * 0.58
    y = lambda v: pt + (h - pt - pb) * (1 - v / top)
    out = [f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" preserveAspectRatio="xMidYMid meet">']
    for t in ticks:
        out.append(f'<line class="gl" x1="{pl}" x2="{w - pr}" y1="{y(t):.1f}" y2="{y(t):.1f}"/>')
        out.append(f'<text x="{pl - 6}" y="{y(t) + 3:.1f}" text-anchor="end">{fmt_v(t)}</text>')
    for i in range(n):
        x = pl + cw * i + (cw - bw) / 2
        acc = 0
        for si, s in enumerate(series):
            v = s[i]
            y1, y0 = y(acc + v), y(acc)
            op = "1" if (i == n - 1 or not highlight_last) else ".55"
            rx = 3 if si == len(series) - 1 else 0
            out.append(f'<rect x="{x:.1f}" y="{y1:.1f}" width="{bw:.1f}" height="{max(y0 - y1, 0):.1f}" rx="{rx}" fill="{colors[si]}" opacity="{op}"/>')
            acc += v
        out.append(f'<text x="{x + bw / 2:.1f}" y="{h - 6}" text-anchor="middle">{labels[i]}</text>')
    if line:
        pts = " ".join(f"{pl + cw * i + cw / 2:.1f},{y(v):.1f}" for i, v in enumerate(line))
        out.append(f'<polyline points="{pts}" fill="none" stroke="var(--ink)" stroke-width="1.6" stroke-dasharray="4 3"/>')
    i = n - 1
    out.append(f'<text class="lbl" x="{pl + cw * i + cw / 2:.1f}" y="{y(tot[i]) - 6:.1f}" text-anchor="middle">{fmt_v(tot[i])}</text>')
    out.append("</svg>")
    return "".join(out)


def spark(vals, color="var(--vio)", w=96, h=26):
    mx, mn = max(vals), min(vals)
    rng = (mx - mn) or 1
    pts = [(i * (w - 6) / (len(vals) - 1) + 3, h - 4 - (v - mn) / rng * (h - 8)) for i, v in enumerate(vals)]
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    lx, ly = pts[-1]
    return (f'<svg class="spark" viewBox="0 0 {w} {h}"><polyline points="{p}" fill="none" stroke="{color}" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round"/><circle cx="{lx:.1f}" cy="{ly:.1f}" r="2.6" fill="{color}"/></svg>')


def area_hero(vals, w=600, h=150):
    mx, mn = max(vals), min(vals)
    pad = (mx - mn) * 0.15
    top, bot = mx + pad, mn - pad
    pts = [(6 + i * (w - 12) / (len(vals) - 1), 14 + (top - v) / (top - bot) * (h - 28)) for i, v in enumerate(vals)]
    line = " L ".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    lx, ly = pts[-1]
    return (f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="none" role="img"><defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'
            f'<path d="M {line} L {w - 6} {h} L 6 {h} Z" fill="url(#hg)"/>'
            f'<path d="M {line}" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>'
            f'<circle cx="{lx:.0f}" cy="{ly:.0f}" r="4.5" fill="#fff"/></svg>'), ly / h


def donut(parts, center_big, center_small, size=200, stroke=26):
    """parts: (valor, color)"""
    r = (size - stroke) / 2
    c = 2 * math.pi * r
    tot = sum(p[0] for p in parts)
    out = [f'<svg viewBox="0 0 {size} {size}"><circle cx="{size / 2}" cy="{size / 2}" r="{r}" fill="none" stroke="var(--inset)" stroke-width="{stroke}"/>']
    off = 0
    for v, col in parts:
        ln = c * v / tot
        out.append(f'<circle cx="{size / 2}" cy="{size / 2}" r="{r}" fill="none" stroke="{col}" stroke-width="{stroke}" '
                   f'stroke-dasharray="{ln:.2f} {c - ln:.2f}" stroke-dashoffset="{-off:.2f}"/>')
        off += ln
    out.append("</svg>")
    return f'<div class="donut">{"".join(out)}<div class="ctr"><b>{center_big}</b><span>{center_small}</span></div></div>'
