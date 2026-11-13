"""Build notepad.ankiaddon for AnkiWeb / Install from file.

Usage:  python build.py
Packs the code and the example templates (files at the zip root).
Never packed: meta.json (your settings) and your own templates.
"""
import os
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "notepad.ankiaddon")
FILES = ["manifest.json", "__init__.py", "config.json", "config.md", "logo.png"]

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for f in FILES:
        z.write(os.path.join(ROOT, f), f)
    z.write(os.path.join(ROOT, "user_files", "README.txt"), "user_files/README.txt")
    tdir = os.path.join(ROOT, "user_files", "templates")
    for n in sorted(os.listdir(tdir)):
        if n.startswith("_example_") and n.endswith(".txt"):
            z.write(os.path.join(tdir, n), f"user_files/templates/{n}")
print(OUT, os.path.getsize(OUT), "bytes")
