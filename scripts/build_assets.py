"""Genera hero y diagrama de arquitectura (claro/oscuro). Uso: python scripts/build_assets.py"""
import base64
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)
SANS = "'Segoe UI', -apple-system, 'Helvetica Neue', Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', monospace"
EMBER = "#F26A21"
# Paleta de Controla (verdes de la app)
THEMES = {
    "dark": dict(bg="#0E1F15", card="#12261A", border="#1F4030", text="#E5F6EC", muted="#8FB5A0", acc="#34C26B", chip="#1B3A29", dot="#163223", glow="#159947"),
    "light": dict(bg="#F6FAF4", card="#FFFFFF", border="#D7EADD", text="#102A1B", muted="#4E6B5A", acc="#159947", chip="#E5F6EC", dot="#DCEBDD", glow="#34C26B"),
}
ICON = base64.b64encode((Path(__file__).resolve().parent / "brand" / "controla-icon.png").read_bytes()).decode()


def chips(items, x, y, t, size=13):
    out, cx = [], x
    for it in items:
        w = int(len(it) * size * 0.58 + 22)
        out.append(f'<rect x="{cx}" y="{y}" width="{w}" height="26" rx="13" fill="{t["chip"]}"/>'
                   f'<text x="{cx + w / 2}" y="{y + 17}" text-anchor="middle" font-family="{MONO}" font-size="{size}" fill="{t["text"]}">{escape(it)}</text>')
        cx += w + 8
    return "".join(out)


def hero(t):
    w, h = 1200, 300
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><defs>'
            f'<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="{t["dot"]}"/></pattern>'
            f'<filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>'
            f'<clipPath id="c"><rect width="{w}" height="{h}" rx="24"/></clipPath></defs>'
            '<style>@keyframes d{0%,100%{transform:translate(0,0)}50%{transform:translate(60px,20px)}}.o{animation:d 12s ease-in-out infinite}</style>'
            f'<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="{t["bg"]}"/><rect width="{w}" height="{h}" fill="url(#dots)"/>'
            f'<g filter="url(#b)" opacity=".38"><circle class="o" cx="1000" cy="90" r="120" fill="{t["glow"]}"/></g></g>'
            f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="24" fill="none" stroke="{t["border"]}"/>'
            f'<clipPath id="ic"><rect x="72" y="48" width="80" height="80" rx="20"/></clipPath>'
            f'<rect x="72" y="48" width="80" height="80" rx="20" fill="#FFFFFF" stroke="{t["border"]}"/>'
            f'<image href="data:image/png;base64,{ICON}" x="72" y="48" width="80" height="80" clip-path="url(#ic)"/>'
            f'<text x="172" y="96" font-family="{MONO}" font-size="16" fill="{t["acc"]}">proyecto de grado · Universidad EAN</text>'
            f'<text x="72" y="190" font-family="{SANS}" font-size="62" font-weight="800" letter-spacing="-2" fill="{t["text"]}">Controla</text>'
            f'<text x="72" y="228" font-family="{SANS}" font-size="22" fill="{t["muted"]}">Gestión de ventas, inventario y finanzas para tiendas de barrio.</text>'
            + chips(["Flutter", "NestJS", "SQL Server", "Python · ML", "Next.js"], 72, 246, t) + '</svg>')


def box(t, x, y, w, h, title, sub, accent=False):
    stroke = t["acc"] if accent else t["border"]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{t["card"]}" stroke="{stroke}" stroke-width="{2 if accent else 1}"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 - 2}" text-anchor="middle" font-family="{SANS}" font-size="16" font-weight="700" fill="{t["text"]}">{escape(title)}</text>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 18}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{t["muted"]}">{escape(sub)}</text>')


def arrow(t, x1, y1, x2, y2, label="", dash=False):
    d = ' stroke-dasharray="6 5"' if dash else ""
    lab = (f'<text x="{(x1 + x2) / 2}" y="{(y1 + y2) / 2 - 8}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{t["acc"]}">{escape(label)}</text>' if label else "")
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{t["muted"]}" stroke-width="1.6"{d} marker-end="url(#a)"/>' + lab)


def architecture(t):
    w, h = 1200, 420
    clients = [("App móvil / escritorio", "Flutter · 19 pantallas"), ("Web app", "Flutter Web"),
               ("Consola de administración", "Next.js · React"), ("Sitio comercial", "Next.js · leads")]
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><defs>'
         f'<marker id="a" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{t["muted"]}"/></marker></defs>'
         f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="20" fill="{t["bg"]}" stroke="{t["border"]}"/>'
         f'<text x="40" y="40" font-family="{MONO}" font-size="12" fill="{t["acc"]}">CLIENTES</text>'
         f'<text x="500" y="40" font-family="{MONO}" font-size="12" fill="{t["acc"]}">API</text>'
         f'<text x="900" y="40" font-family="{MONO}" font-size="12" fill="{t["acc"]}">DATOS</text>')
    for i, (a, b) in enumerate(clients):
        y = 58 + i * 78
        s += box(t, 40, y, 300, 62, a, b) + arrow(t, 340, y + 31, 500, 170 if i < 2 else 190)
    s += box(t, 500, 110, 260, 160, "Backend NestJS", "REST · TypeORM · roles y permisos", True)
    s += arrow(t, 760, 160, 900, 110, "TypeORM")
    s += box(t, 900, 60, 260, 100, "SQL Server", "ventas · inventario · finanzas", False)
    s += box(t, 900, 230, 260, 100, "ml-service (Python)", "Prophet · reglas de reposición · lotes", True)
    s += arrow(t, 1030, 230, 1030, 160, "escribe resultados", dash=True)
    s += arrow(t, 900, 140, 760, 220, "lee pronósticos", dash=True)
    s += (f'<text x="40" y="{h - 16}" font-family="{MONO}" font-size="11" fill="{t["muted"]}">Línea punteada: flujo del módulo de IA. El servicio de ML corre por lotes y no atiende peticiones HTTP.</text></svg>')
    return s


if __name__ == "__main__":
    for n, t in THEMES.items():
        (OUT / f"hero-{n}.svg").write_text(hero(t), encoding="utf-8")
        (OUT / f"architecture-{n}.svg").write_text(architecture(t), encoding="utf-8")
    print("ok")
