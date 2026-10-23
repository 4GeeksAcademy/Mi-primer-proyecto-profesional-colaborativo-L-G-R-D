# Maison RDL — Contexto técnico

Actualizado: 23/10/2026. Repositorio: https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D.

HTML estático y Tailwind CSS 4.3.3 con CLI oficial. Cinco HTML en raíz, assets locales y src/styles/input.css + tokens.css como fuentes del CSS generado. Sin JavaScript de aplicación ni backend.

Comandos comprobados: npm ci, npm run build y npm start (servidor estándar de Python, puerto 8000). En Windows y Codespaces: Python disponible en PATH. No se necesita Flask. Lockfile conservado, node_modules ignorado.

Las comprobaciones Playwright se ejecutan externamente; no son dependencia del sitio. Evidencia Nu/navegador/contraste y límites en [verificación](verificacion.md). El servidor local no acredita publicación ni PageSpeed final.

Publicación real comprobada: https://4geeksacademy.github.io/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D/ . Workflow de Pages exitoso, commit bef45b0. Las herramientas build_site.py y check_site.py generan y verifican el paquete público limpio. No se publica la memoria, herramientas ni evidencias. Documentación consolidada sin carpeta docs; src/styles/input.css escanea solo páginas y fragmentos utilizados.
