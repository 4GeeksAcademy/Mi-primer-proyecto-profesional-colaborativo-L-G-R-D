# Maison RDL — Documentación para Roger, Daniel y Lydia

Envío del 23/10/2026. Esta preparación no ha subido archivos, abierto PR ni cambiado el repositorio remoto.

Repositorio común: [Mi-primer-proyecto-profesional-colaborativo-R-D](https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-R-D).

## Empezar aquí

1. Descomprimir el ZIP completo; no trabajar desde el visor del archivo comprimido.
2. Leer [el reparto y arranque](docs/INICIO-DE-TRABAJO.md), [los requisitos](docs/requisitos.md) y [la guía visual](docs/diseno.md).
3. Daniel continúa con [INICIO-DANIEL.md](INICIO-DANIEL.md); Lydia con [INICIO-LYDIA.md](INICIO-LYDIA.md).
4. Antes de usar un asistente, darle [AGENTS.md](AGENTS.md), [CONTEXT.md](CONTEXT.md) y el [prompt maestro](PROMPT-MAESTRO.md), indicando persona y ficha.

No hace falta instalar nada para leer la documentación o ver las capturas. Abrir los Markdown en el editor habitual.

## Reparto

| Persona | Responsabilidad |
| --- | --- |
| Roger | Diseño final de cinco páginas, identidad y componentes, responsive y optimización |
| Daniel | Setup, inventario, estructura/contenido de inicio/catálogo/producto, SEO y Schema.org; preparación de publicación |
| Lydia | Estructura/contenido de carrito/checkout, formularios e importes; coordinación de QA, evidencias y README |

Cada autor comprueba y corrige su parte. Roger revisa cambios visuales de los demás; Daniel o Lydia revisan los suyos.

## Qué incorporar primero al repositorio

Daniel inicia T00 y después T01. La primera integración recomendada es una PR de preparación, revisada por Roger, sin commits de desarrollo directamente en main.

Copiar el contenido de esta carpeta en la raíz del clon del repositorio, conservando .git, el remoto, la plantilla y la documentación útil existente. Revisar colisiones antes de copiar: integrar el README e instrucciones existentes, no reemplazarlos a ciegas. Incluir las carpetas ocultas .agents y .github.

Este paquete contiene los documentos, veinte fichas y tokens; todavía no contiene las cinco páginas finales en la raíz. No confundir los HTML de la referencia con esas páginas. Roger integrará selectivamente recursos y componentes en T02; Daniel preparará los esqueletos en T01.

Las instrucciones Git describen el flujo de trabajo que se seguirá al ejecutar cada tarea. Extraer o revisar este ZIP no sube nada automáticamente. No hacer push ni publicar desde un asistente solo por haber leído estos documentos; debe formar parte de la tarea que el equipo le haya encargado.

## Referencia visual incluida

- [Portada de escritorio](docs/referencia-visual/preview/desktop.png).
- [Portada móvil](docs/referencia-visual/preview/mobile.png).
- [Página completa](docs/referencia-visual/preview/inicio-completo.png).
- [Logo e identidad](docs/referencia-visual/preview/identidad.png).
- [Cómo abrir la referencia HTML](docs/referencia-visual/README.md).

La referencia está en docs/referencia-visual con sus imágenes, fuentes, licencias, logos, CSS compilado y fuente Tailwind. Es una muestra del inicio, no la tienda terminada. npm y sus comandos, si se usan, corresponden solo a esa carpeta hasta que T01 documente los del proyecto final.

## Límites y pendientes

Solo HTML + Tailwind, sin JavaScript de aplicación, React, backend ni pagos reales. La marca es ficticia. Fecha/canal de entrega, disponibilidad, accesos, idioma/moneda, inventario final y alojamiento siguen pendientes de coordinación.

La matriz tiene los 17 criterios del campus y la entrega. Las veinte fichas continúan pendientes de integración/verificación. Consultar [la memoria](memory-bank/progress.md) para distinguir preparación y resultados acreditados.
