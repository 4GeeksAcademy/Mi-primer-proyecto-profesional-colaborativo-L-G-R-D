# Maison RDL — Continuar el proyecto

El proyecto ya tiene las cinco vistas y el inventario integrados. No vuelvas a descomprimir el paquete inicial dentro del repositorio ni repitas T01. Estado comprobado y pendientes: [verificación](docs/verificacion.md).

1. Leer [AGENTS.md](AGENTS.md), [CONTEXT.md](CONTEXT.md) y [progreso](memory-bank/progress.md).
2. Consultar [README](README.md) para ejecutar/build y [tareas](tasks/README.md) para el estado de cada bloque.
3. Trabajar en la rama exacta indicada; conservar cambios ajenos. Una PR conjunta reúne el cierre visual, SEO, limpieza y preparación de entrega.
4. Gaby revisa y aprueba manualmente. Roger conserva la dirección visual; cada autor corrige su parte.

## Limpieza del Codespace

`node_modules/` es local e ignorado; no debe subirse. Las carpetas `pquete-maison/` y `paquete-maison/` son paquetes iniciales duplicados, no parte del sitio. La herramienta comprueba rutas y crea un ZIP recuperable fuera del proyecto antes de retirarlas:

```bash
python tools/clean_workspace.py
python tools/clean_workspace.py --apply
```

La primera orden muestra qué encuentra; la segunda aplica la limpieza. Si hay enlaces simbólicos o otro repositorio dentro, se detiene para conservarlo. Mantener `.git`, `.agents`, `.github`, `.vscode`, assets, src, tools, docs, tasks y memory-bank. No borrar licencias ni archivos de contexto.

Pendientes externos: Gaby, integrar, habilitar/publicar Pages, PageSpeed real con captura y entrega al instructor. [Repositorio](https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D).
