> Estado vigente a 23/10/2026: Implementación integrada hasta PR #13; reorganización documental en PR #14 pendiente de revisión. Los apartados de preparación y sesiones anteriores se conservan como historial. Fuente actual: [progress](../memory-bank/progress.md) y [verificación](../memory-bank/verificacion.md).

# T09 — SEO y Schema.org

Estado: Implementación integrada hasta PR #13; reorganización documental en PR #14 pendiente de revisión.
Responsable del cierre autorizado: Roger; se conserva la autoría previa del equipo.
Revisor: Gaby.
Rama: codex/imagenes-revision-visual.

Títulos y descripciones únicos, idioma y contenido semántico en las cinco páginas. Microdata Organization en inicio y Product/Offer en la ficha, con precio/moneda/SKU coherentes con el contenido visible. Schema Markup Validator devuelve cero errores y cero advertencias; evidencias en [verificación](../memory-bank/verificacion.md).

Canónicas absolutas, Open Graph, tarjeta social, robots y sitemap se generan al publicar con la URL real, mediante tools/build_site.py y el workflow de Pages. El paquete generado se probó bajo una subruta y sus cinco HTML pasan Nu. No se afirma aprobación de Google Rich Results ni indexación; son muestras ficticias.

Pendiente: revisión e integración; comprobar URL pública después de publicar. No inventar datos comerciales, reseñas ni disponibilidad para eliminar avisos de otros validadores.
