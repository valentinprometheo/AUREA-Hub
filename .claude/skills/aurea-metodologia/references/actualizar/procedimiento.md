---
consultar-cuando: hay que integrar mejoras a esta skill, sacar una versión nueva, derogar o corregir doctrina, unir otra skill
disparadores: "actualizá la metodología", "integrá esto", "nueva versión", "subí estos hallazgos", "derogá", "mejora continua de la skill"
fuente-única-de: el procedimiento para actualizar esta skill sin romper lo vigente
combina-con: actualizar/protocolo-de-ingreso, metodologia-correccion-agente (términos derogados), CHANGELOG
---

# Actualizar esta skill (mejora continua)

Cada mejora entra **complementando** lo que existe, se **audita** contra la versión anterior
para no romper nada, y deja la skill lista para la próxima. El método de clasificación y
ubicación está en `references/actualizar/protocolo-de-ingreso.md`; la auditoría la hace
`scripts/auditar.py` (los dos dentro de esta misma skill). Leé el protocolo antes del paso 2.

## Paso 0 · Conseguí la versión vigente

La versión de partida es esta misma skill instalada (`/mnt/skills/*/aurea-metodologia`, solo
lectura) o el ZIP/`.skill` que te pase el usuario. Si hay las dos y difieren, preguntá cuál es la vigente.
Leé la primera entrada de `references/CHANGELOG.md` para saber en qué versión estás.

Armá dos copias de trabajo y no toques la original:
```bash
mkdir -p /home/claude/upd && cp -r <vigente> /home/claude/upd/anterior && cp -r <vigente> /home/claude/upd/nueva
```
Todo se edita en `nueva`. `anterior` queda intacta para comparar.

## Paso 1 · Inventario de la mejora

Leé todo el material que trae el usuario (si un archivo llega vacío al chat, buscalo en
`/mnt/user-data/uploads/` o pedí que lo adjunte como archivo). Hacé una lista de los
aprendizajes, uno por línea, sin agruparlos todavía.

## Paso 2 · Clasificá cada aprendizaje (protocolo, sección 1)

Para cada uno: patrón o instancia · cuántos rubros distintos · tipo · relación con lo que
existe (agregar, complementar, corregir, derogar, nada). Las **instancias no entran** a la
metodología: se lo decís al usuario y quedan en el material del cliente.

Mostrale al usuario la tabla de clasificación **antes de escribir** cuando haya alguna de
estas: una derogación, una corrección de regla oficial, una promoción a transversal, o un
archivo nuevo. Son las decisiones que cambian la doctrina. El resto podés aplicarlo directo.

## Paso 3 · Buscá si ya existe (ver protocolo, sección 4)

Antes de escribir cada ítem, buscalo en todo el skill (`grep -rni`) y leé el encabezado
`fuente-única-de` de los candidatos. Un tema tiene un solo archivo dueño. Si ya existe,
complementá ahí; si otro archivo lo repite, que apunte al dueño.

## Paso 4 · Aplicá las operaciones (ver protocolo, sección 3)

- Editá con reemplazos que verifiquen que el texto original existe exactamente una vez: si no
  aparece o aparece dos veces, frená y miralo; no reemplaces a ciegas.
- Agregar o complementar: debajo de lo existente, con la evidencia (cliente y rubro).
- Corregir: reemplazo + línea "Actualización vX: antes…, ahora…, por qué" en el mismo lugar.
- Derogar: fila nueva en la tabla de términos derogados de
  `metodologia-correccion-agente.md` + propagación a **todos** los archivos que lo nombran,
  incluidas las copias de otras skills en `references/02-skills/`.
- Archivo nuevo: solo si no hay dueño; con encabezado de auto-ruteo y su línea en `SKILL.md`
  (si cambia el ruteo), `00-CONSULTA.md` y `00-INDEX.md`.
- Usá el vocabulario de la metodología con el usuario: tags (estadío, perfil del contacto,
  excepción), embudos y variables.

Si el trabajo es largo, empaquetá un respaldo intermedio en `/mnt/user-data/outputs/` cada
tanto: el entorno se puede reiniciar entre turnos.

## Paso 5 · Versioná

- Entrada nueva **arriba de todo** en `references/CHANGELOG.md` (plantilla en el protocolo,
  sección 5). Versión menor (v1.22 → v1.23) para mejoras; anotá lo que quede pendiente.
- Si cambió el ruteo o el alcance, actualizá `SKILL.md` y su descripción. La descripción tiene
  un máximo de 1024 caracteres: medila, no la estimes.

## Paso 6 · Auditá (obligatorio, no se entrega sin esto)

```bash
python3 /home/claude/upd/nueva/aurea-metodologia/scripts/auditar.py --anterior /home/claude/upd/anterior/aurea-metodologia --nueva /home/claude/upd/nueva/aurea-metodologia
```
(Ajustá las rutas a donde quedó la carpeta `aurea-metodologia` dentro de cada copia.)

Chequea: encabezado y largo de la descripción, archivos perdidos, recortes grandes, términos
derogados vigentes, temas con dos archivos dueños, archivos nuevos sin auto-ruteo, referencias
rotas en el `SKILL.md`, entrada nueva en el CHANGELOG y largo del `SKILL.md`.

- **FALLA:** se corrige y se vuelve a correr. No se entrega con fallas.
- **ALERTA:** se corrige o se justifica en el CHANGELOG (ej. un archivo eliminado a propósito).

Después validá el formato con el validador oficial:
```bash
python3 /mnt/skills/examples/skill-creator/scripts/quick_validate.py /home/claude/upd/nueva/aurea-metodologia
```

## Paso 7 · Empaquetá y entregá

```bash
cd /mnt/skills/examples/skill-creator && python3 -m scripts.package_skill /home/claude/upd/nueva/aurea-metodologia /mnt/user-data/outputs/
```
Renombrá el `.skill` con la versión (`aurea-metodologia-vX.Y.skill`) y presentalo.

En la respuesta al usuario, corto:
1. Qué entró y dónde (por operación: agregado, complementado, corregido, derogado).
2. Qué quedó afuera por ser instancia, y dónde debería vivir.
3. El resultado de la auditoría en una línea.
4. Decisiones pendientes, como opciones A/B con recomendación.
5. Instalación: no se puede instalar desde el chat; el usuario borra la versión instalada y
   sube la nueva desde la sección de Skills de su cuenta.

## Cómo crece este procedimiento

- Si aparece un error nuevo que la auditoría no detectó, se suma un chequeo a
  `scripts/auditar.py` (y se prueba plantando ese error en una copia para confirmar que lo
  agarra).
- Si cambia la estructura de la metodología (un eje nuevo, un archivo dueño nuevo), se
  actualiza el mapa de destinos del protocolo.
- La lista de términos derogados NO vive acá: vive en `metodologia-correccion-agente.md` y el
  script la lee de ahí, así hay una sola fuente.
- Este procedimiento, el protocolo y el script viajan dentro de la skill: cada versión nueva
  trae su propia forma de actualizarse.
