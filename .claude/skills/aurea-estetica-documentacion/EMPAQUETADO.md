# Cómo empaquetar y subir esta skill a claude.ai

La metodología para que una habilidad (skill) sea válida al subirla en
**Configuración → Habilidades → Subir/Reemplazar**. Estos son los
condicionantes necesarios (el mensaje de error de la imagen, "Zip must contain
exactly one SKILL.md file", es exactamente este punto 1).

## Condicionantes necesarios (los que valida el sistema)

1. **Exactamente UN archivo llamado `SKILL.md` en el zip.** Ni cero ni más de uno.
   - El error "Currently there are 14" pasa cuando se zipean varias skills juntas
     (cada una con su `SKILL.md`). **Se sube una skill por zip, no todas juntas.**
   - Los demás `.md` (referencias, auditoría, este archivo) **no** pueden llamarse
     `SKILL.md`. Por eso acá se llaman `estetica-deck.md`, `mejora-continua.md`,
     `AUDITORIA.md`, etc. Está bien tener muchos, mientras solo uno sea `SKILL.md`.
2. **`SKILL.md` con frontmatter YAML** que incluya, sí o sí:
   - `name`: identificador en minúsculas con guiones (ej. `aurea-estetica-documentacion`),
     hasta ~64 caracteres.
   - `description`: cuándo se activa y qué hace, hasta **~1024 caracteres**. Es el
     mecanismo principal de activación: si es muy larga se rechaza o se recorta.
3. **Formato del paquete:** `.zip` o `.skill`. Las carpetas `references/`, `assets/`,
   `scripts/` viajan adentro y se cargan bajo demanda (progressive disclosure).
4. Al guardar, claude.ai **corre un escaneo de seguridad**. Sin malware ni nada que
   no se condiga con lo que la skill dice hacer.

## Anatomía (la que usa esta skill)

```
aurea-estetica-documentacion/
├── SKILL.md          ← el ÚNICO SKILL.md (frontmatter + cuerpo, < 500 líneas)
├── references/*.md   ← se leen cuando hacen falta (no se llaman SKILL.md)
├── assets/           ← binarios usados en el output (kit del deck, template NDA)
└── *.md sueltos      ← AUDITORIA, EMPAQUETADO (no se llaman SKILL.md)
```

## Empaquetar (dos caminos)

**Camino simple (zip a mano):** comprimí la carpeta de la skill en un `.zip`. Alcanza
con que adentro haya exactamente un `SKILL.md`. En este repo:

```
cd .claude/skills
zip -r aurea-estetica-documentacion.zip aurea-estetica-documentacion
```

**Camino skill-creator (genera un `.skill`):** desde el directorio del skill-creator,

```
python -m scripts.package_skill <ruta/a/aurea-estetica-documentacion>
```

Cualquiera de los dos sube en **Reemplazar / Subir habilidad**. Si vas a *reemplazar*
`aurea-metodologia`, ojo: esta es una skill **distinta** (estética + documentación),
no la metodología de consultoría. Convendría **subirla como habilidad nueva**, no
pisar `aurea-metodologia`, salvo que quieras unificarlas a propósito.

## Chequeo rápido antes de subir

- [ ] `find . -name SKILL.md` devuelve **exactamente 1**.
- [ ] El `name` está en minúsculas con guiones.
- [ ] La `description` mide ≤ 1024 caracteres.
- [ ] Ningún otro archivo se llama `SKILL.md`.
- [ ] El zip pesa lo razonable (esta skill ~1.5 MB, bien por debajo del límite).
