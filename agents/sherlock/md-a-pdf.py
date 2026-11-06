"""Convierte una nota markdown del cerebro en PDF usando Microsoft Edge en modo headless.

Uso:  python md-a-pdf.py "ruta/a/Nota.md"  [ruta/salida.pdf]
Si no se da salida, el PDF queda al lado de la nota con el mismo nombre.
Solo usa la biblioteca estándar de Python + Edge (ya viene con Windows).
"""
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EDGE_CANDIDATOS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11pt; line-height: 1.5; color: #1f2328; }
h1 { font-size: 20pt; border-bottom: 2px solid #d0d7de; padding-bottom: 4px; margin-top: 0; }
h2 { font-size: 14pt; margin-top: 18px; border-bottom: 1px solid #d0d7de; padding-bottom: 2px; }
h3 { font-size: 12pt; margin-top: 14px; }
a { color: #0969da; text-decoration: none; word-break: break-all; }
code { font-family: Consolas, monospace; background: #f3f4f6; padding: 1px 4px; border-radius: 3px; font-size: 10pt; }
pre { background: #f3f4f6; padding: 8px 10px; border-radius: 4px; white-space: pre-wrap; }
pre code { background: none; padding: 0; }
blockquote { border-left: 3px solid #d0d7de; margin: 8px 0; padding: 2px 12px; color: #57606a; }
table { border-collapse: collapse; margin: 8px 0; width: 100%; font-size: 10pt; }
th, td { border: 1px solid #d0d7de; padding: 4px 8px; text-align: left; vertical-align: top; }
th { background: #f6f8fa; }
.meta { font-size: 9.5pt; color: #57606a; background: #f6f8fa; border-radius: 4px; padding: 6px 10px; margin-bottom: 14px; }
.meta b { color: #1f2328; }
.wikilink { color: #8250df; }
"""


def inline(texto: str) -> str:
    """Formato dentro de una línea: código, links, negrita, cursiva, wikilinks."""
    codigos = []

    def guardar_codigo(m):
        codigos.append(m.group(1))
        return f"\x00{len(codigos) - 1}\x00"

    texto = re.sub(r"`([^`]+)`", guardar_codigo, texto)
    texto = html.escape(texto, quote=False)
    texto = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r'<span class="wikilink">\2</span>', texto)
    texto = re.sub(r"\[\[([^\]]+)\]\]", r'<span class="wikilink">\1</span>', texto)
    texto = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', texto)
    texto = re.sub(r"(?<![\"=>])(https?://[^\s<)]+)", r'<a href="\1">\1</a>', texto)
    texto = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", texto)
    texto = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", texto)
    texto = re.sub(r"(?<!\w)_(?!\s)(.+?)(?<!\s)_(?!\w)", r"<em>\1</em>", texto)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{html.escape(codigos[int(m.group(1))])}</code>", texto)


def separar_frontmatter(md: str):
    if md.startswith("---"):
        partes = md.split("\n---", 1)
        if len(partes) == 2:
            meta = {}
            for linea in partes[0].splitlines()[1:]:
                if ":" in linea:
                    k, v = linea.split(":", 1)
                    meta[k.strip()] = v.strip()
            return meta, partes[1].lstrip("-").lstrip("\n")
    return {}, md


def md_a_html(md: str) -> str:
    lineas = md.splitlines()
    salida, i = [], 0
    parrafo = []

    def cerrar_parrafo():
        if parrafo:
            salida.append("<p>" + inline(" ".join(parrafo)) + "</p>")
            parrafo.clear()

    while i < len(lineas):
        linea = lineas[i]
        s = linea.strip()

        if s.startswith("```"):
            cerrar_parrafo()
            bloque = []
            i += 1
            while i < len(lineas) and not lineas[i].strip().startswith("```"):
                bloque.append(lineas[i])
                i += 1
            salida.append("<pre><code>" + html.escape("\n".join(bloque)) + "</code></pre>")
            i += 1
            continue

        if not s:
            cerrar_parrafo()
            i += 1
            continue

        m = re.match(r"(#{1,6})\s+(.*)", s)
        if m:
            cerrar_parrafo()
            n = len(m.group(1))
            salida.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
            i += 1
            continue

        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", s):
            cerrar_parrafo()
            salida.append("<hr>")
            i += 1
            continue

        if s.startswith(">"):
            cerrar_parrafo()
            citas = []
            while i < len(lineas) and lineas[i].strip().startswith(">"):
                citas.append(lineas[i].strip()[1:].strip())
                i += 1
            salida.append("<blockquote>" + inline(" ".join(citas)) + "</blockquote>")
            continue

        if s.startswith("|") and i + 1 < len(lineas) and re.fullmatch(r"\|?[\s:\-|]+\|?", lineas[i + 1].strip()):
            cerrar_parrafo()
            celdas = lambda l: [c.strip() for c in l.strip().strip("|").split("|")]
            filas = ["<tr>" + "".join(f"<th>{inline(c)}</th>" for c in celdas(s)) + "</tr>"]
            i += 2
            while i < len(lineas) and lineas[i].strip().startswith("|"):
                filas.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in celdas(lineas[i])) + "</tr>")
                i += 1
            salida.append("<table>" + "".join(filas) + "</table>")
            continue

        lista = re.match(r"(\s*)([-*+]|\d+[.)])\s+(.*)", linea)
        if lista:
            cerrar_parrafo()
            i = leer_lista(lineas, i, salida)
            continue

        parrafo.append(s)
        i += 1

    cerrar_parrafo()
    return "\n".join(salida)


def leer_lista(lineas, i, salida):
    """Listas con anidamiento por indentación (- , * , 1.) y casillas [ ] / [x]."""
    pila = []  # (indent, etiqueta)
    while i < len(lineas):
        m = re.match(r"(\s*)([-*+]|\d+[.)])\s+(.*)", lineas[i])
        if not m:
            if lineas[i].strip() and pila and lineas[i].startswith(" "):
                salida[-1] = salida[-1][: -len("</li>")] + " " + inline(lineas[i].strip()) + "</li>"
                i += 1
                continue
            break
        indent = len(m.group(1).replace("\t", "    "))
        etiqueta = "ol" if m.group(2)[0].isdigit() else "ul"
        while pila and indent < pila[-1][0]:
            salida.append(f"</{pila.pop()[1]}>")
        if pila and indent == pila[-1][0] and etiqueta != pila[-1][1]:
            salida.append(f"</{pila.pop()[1]}>")
        if not pila or indent > pila[-1][0]:
            pila.append((indent, etiqueta))
            salida.append(f"<{etiqueta}>")
        texto = m.group(3)
        texto = re.sub(r"^\[ \]\s*", "☐ ", texto)
        texto = re.sub(r"^\[[xX]\]\s*", "☑ ", texto)
        salida.append(f"<li>{inline(texto)}</li>")
        i += 1
    while pila:
        salida.append(f"</{pila.pop()[1]}>")
    return i


def buscar_navegador() -> str:
    for ruta in EDGE_CANDIDATOS:
        if os.path.exists(ruta):
            return ruta
    for nombre in ("msedge", "chrome"):
        if shutil.which(nombre):
            return shutil.which(nombre)
    sys.exit("No encontré Microsoft Edge ni Chrome para imprimir el PDF.")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    nota = Path(sys.argv[1]).resolve()
    pdf = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else nota.with_suffix(".pdf")

    meta, cuerpo = separar_frontmatter(nota.read_text(encoding="utf-8"))
    meta_html = ""
    if meta:
        meta_html = '<div class="meta">' + " &nbsp;·&nbsp; ".join(
            f"<b>{html.escape(k)}:</b> {inline(v.strip('[]'))}" for k, v in meta.items()
        ) + "</div>"

    cuerpo_html = md_a_html(cuerpo)
    if not cuerpo_html.lstrip().startswith("<h1>"):
        cuerpo_html = f"<h1>{html.escape(nota.stem)}</h1>\n" + cuerpo_html

    documento = (
        f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
        f"<title>{html.escape(nota.stem)}</title><style>{CSS}</style></head>"
        f"<body>{cuerpo_html.replace('</h1>', '</h1>' + meta_html, 1)}</body></html>"
    )

    with tempfile.TemporaryDirectory() as tmp:
        html_tmp = Path(tmp) / "nota.html"
        html_tmp.write_text(documento, encoding="utf-8")
        resultado = subprocess.run(
            [
                buscar_navegador(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                f"--user-data-dir={Path(tmp) / 'perfil'}",
                f"--print-to-pdf={pdf}", html_tmp.as_uri(),
            ],
            capture_output=True, text=True, timeout=120,
        )
    if not pdf.exists():
        sys.exit(f"No se generó el PDF.\n{resultado.stderr[-1500:]}")
    print(pdf)


if __name__ == "__main__":
    main()
