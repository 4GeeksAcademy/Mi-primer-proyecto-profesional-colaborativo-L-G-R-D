# Maison RDL — Contexto técnico

Actualizado: 23/10/2026. Repositorio: https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D.

HTML estático y Tailwind CSS 4.3.3 con CLI oficial. Cinco HTML en raíz, assets locales y src/styles/input.css + tokens.css como fuentes del CSS generado. Sin JavaScript de aplicación ni backend.

Comandos comprobados: npm ci, npm run build y npm start (servidor estándar de Python, puerto 8000). En Windows y Codespaces: Python disponible en PATH. No se necesita Flask. Lockfile conservado, node_modules ignorado.

Las comprobaciones Playwright se ejecutan externamente; no son dependencia del sitio. Evidencia Nu/navegador/contraste y límites en [verificación](../docs/verificacion.md). El servidor local no acredita publicación ni PageSpeed final.
