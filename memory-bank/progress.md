# Maison RDL — Estado contrastado

Actualizado: 23/10/2026. [Evidencia actual](verificacion.md).

La PR #13 fue aprobada por Gaby e integrada en main, commit bef45b0. GitHub Pages habilitado por autorización de Roger y publicado con éxito: [sitio](https://4geeksacademy.github.io/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D/). Cinco rutas públicas verificadas en móvil/escritorio, HTTP 200, sin recursos rotos ni overflow.

Build, HTML, microdata y QA local contrastados. E07 sigue pendiente: PageSpeed web y API responden 429 por cuota; no hay puntuación ni captura satisfactorias. Se conservan capturas de los errores como diagnóstico, no como evidencia de cumplimiento. Las evidencias de publicación se preparan para revisión de Gaby en codex/evidencias-entrega.

Roger confirma que la entrega consiste únicamente en compartir [el repositorio](https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D). No se ha enviado al instructor desde esta sesión. Cuando PageSpeed permita medir: obtener ≥80, guardar pagespeed-result.png real y registrar URL/modo/fecha/resultado.

## Consolidación de documentación

Por petición de Roger se retira docs/. Los requisitos, diseño, inventario y verificación se consolidan en esta memoria, la procedencia en assets y las pruebas en evidencias/. Se conserva copia recuperable externa y el historial Git. No se alteran los hechos de aprobación/publicación: PR #13 integrada y sitio público operativo; PR #14 documenta evidencias y esta limpieza, pendiente de Gaby. PageSpeed continúa sin puntuación válida por HTTP 429.

## Auditoría SEO pública

Lighthouse 13.5.0 sobre https://4geeksacademy.github.io/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D/ devuelve **SEO 100/100**, sin auditorías SEO fallidas. Informe real: [JSON](../evidencias/lighthouse-seo-public.json). La captura de Roger con 63 corresponde al puerto privado de Codespaces, que desde fuera redirige al inicio de sesión; no equivale a medir la web pública. Este 100 es SEO en Lighthouse CLI, no una puntuación de rendimiento de PageSpeed Insights ni cierre de E07.

Equipo final: Roger, Daniel, Lydia y Gabriela (Gaby). Gabriela se incorporó al final para revisión/aprobación de PR; reconocida en la web y la documentación. Capturas originales de Lighthouse de Codespaces aportadas por Roger guardadas en evidencias; su origen y límites se distinguen de la auditoría SEO pública de 100 y del requisito PageSpeed todavía pendiente.
