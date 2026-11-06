"""Saca el texto de un .docx (párrafo por línea), para leer el CV sin Word.

Uso:  python docx-a-texto.py "ruta/al/CV.docx"
Solo usa la biblioteca estándar de Python.
"""
import re
import sys
import zipfile
from html import unescape


def texto_docx(ruta):
    with zipfile.ZipFile(ruta) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    lineas = []
    for parrafo in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
        partes = re.findall(r"<w:t[^>]*>([^<]*)</w:t>|<w:tab/>", parrafo)
        linea = "".join(p if p else "\t" for p in partes).strip()
        if linea:
            lineas.append(unescape(linea))
    return "\n".join(lineas)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding="utf-8")
    print(texto_docx(sys.argv[1]))
