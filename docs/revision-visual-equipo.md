# Imágenes y revisión visual — 23/10/2026

Responsable: Roger. Rama: `codex/imagenes-revision-visual`. Revisión y aprobación de Gaby pendientes; no integrado en main.

## Cambios

- Dieciséis imágenes nuevas de producto, acordes con los nombres y descripciones del inventario; sustituidos veinte bloques de imagen pendiente entre las ocho tarjetas del inicio y las veinte del catálogo.
- Portadas de escritorio y móvil con los cuatro integrantes, conservando el traje estampado y adaptando los otros conjuntos al estilo de la referencia. El parecido facial es una recreación generada y queda sujeto a la revisión de los integrantes.
- Encuadre móvil que conserva las cuatro caras y transición inferior hacia el fondo oscuro, sin recortar lateralmente al equipo.
- Procedencia, textos alternativos y rutas registrados. Se conservan las imágenes anteriores y la referencia visual.

## Comprobaciones realizadas

Build de Tailwind correcto. Navegador Chromium mediante Playwright externo al proyecto, porque Browser plugin no está disponible. No se añadieron dependencias al proyecto ni JavaScript de aplicación.

Las cinco páginas se abrieron a 375 × 667, 390 × 844, 768 × 1024 y 1440 × 900. En las veinte combinaciones: sin desbordamiento horizontal del documento, imágenes rotas, textos alternativos ausentes, campos sin etiqueta ni errores de carga o ejecución. El desplazamiento horizontal de las filas de productos en móvil es intencional.

Se comprobaron apertura de búsqueda, cierre mediante Escape y menú móvil; CTA del inicio visible sin desplazarse en los cuatro tamaños. El checkout conserva el botón de pago deshabilitado. Revisión de capturas frente al inicio de `docs/referencia-visual`: se mantienen tipografías, paleta marfil/oliva, bandas y proporciones de tarjetas; cambian la campaña y la selección de productos del inventario actual. La referencia antigua tiene otros nombres y precios, que no sustituyen al inventario vigente.

## Límites

No acredita aprobación de Gaby, integración, publicación, auditoría completa de accesibilidad, SEO/Schema.org ni PageSpeed. Todas las tarjetas siguen abriendo la ficha única de demostración, tal como especifica el contenido integrado. Los filtros y el carrito continúan siendo estáticos.

## Ajuste posterior del menú y contraste

Cabecera pegajosa en las cinco vistas. En inicio, transparente con degradado neutro al cargar, y fondo oliva profundo de marca al desplazar mediante CSS cuando el navegador lo soporta; sin JavaScript. Textos secundarios y bordes reforzados, anclas separadas de la cabecera. Estado final y evidencia en [verificación](verificacion.md).
