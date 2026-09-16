#!/usr/bin/env python3
"""Auditoría de la skill AUREA Estética y Documentación.
Corré esto SIEMPRE antes de empaquetar o entregar: python scripts/audit.py
Verifica estructura, empaquetado, referencias cruzadas, assets y limpieza.
"""
import os, re, base64, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ok = True
def check(cond, msg):
    global ok
    print(("  OK  " if cond else " FALLA ") + msg); ok = ok and cond

print("== estructura / empaquetado ==")
skills = glob.glob(os.path.join(ROOT,"**","SKILL.md"), recursive=True)
check(len(skills)==1, f"exactamente 1 SKILL.md (hay {len(skills)})")
fm = open(os.path.join(ROOT,"SKILL.md"),encoding="utf-8").read().split("---")[1]
name = re.search(r'name:\s*(\S+)',fm).group(1)
desc = re.sub(r'\s+',' ',fm.split('description:',1)[1]).strip().lstrip('>-').strip()
check(len(name)<=64, f"name <=64 ({len(name)})")
check(len(desc)<=1024, f"description <=1024 ({len(desc)})")

print("== referencias cruzadas ==")
txt = ""
for p in glob.glob(os.path.join(ROOT,"*.md"))+glob.glob(os.path.join(ROOT,"references","*.md")):
    txt += open(p,encoding="utf-8").read()
missing = [r for r in sorted(set(re.findall(r'(?:references/|assets/)[\w./-]+\.(?:md|css|py|txt|docx|html|svg)', txt)))
           if not os.path.exists(os.path.join(ROOT,r))]
check(not missing, "todas las referencias resuelven" + (f" (faltan: {missing})" if missing else ""))

print("== assets ==")
for f in ["assets/deck/logo.txt","assets/deck/sphere.txt","assets/deck/isotipo.txt"]:
    s=open(os.path.join(ROOT,f)).read().strip()
    m=re.match(r'data:image/([\w+.-]+);base64,(.*)',s,re.S)
    check(bool(m) and len(base64.b64decode(m.group(2)))>500, f"{f} es data URI válido")
for f in ["assets/deck/aurea-drakon.css","assets/nda/NDA-AUREA-template-base.docx",
          "assets/ejemplos/drakon-ventas-marketing.html","assets/ejemplos/guia-mia-seguimientos.html"]:
    check(os.path.exists(os.path.join(ROOT,f)), f"existe {f}")
check(os.path.getsize(os.path.join(ROOT,"assets/deck/aurea-drakon.css"))>40000, "aurea-drakon.css completo (>40KB)")

print("== limpieza ==")
junk = glob.glob(os.path.join(ROOT,"**","__pycache__"),recursive=True) + \
       glob.glob(os.path.join(ROOT,"**","*.pyc"),recursive=True) + \
       glob.glob(os.path.join(ROOT,"**",".DS_Store"),recursive=True)
check(not junk, "sin basura (pycache/pyc/DS_Store)")

print("\n" + ("AUDITORIA OK ✅" if ok else "AUDITORIA CON FALLAS ❌"))
sys.exit(0 if ok else 1)
