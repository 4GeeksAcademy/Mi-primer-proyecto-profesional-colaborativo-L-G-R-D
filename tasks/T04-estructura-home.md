# T04 — Estructura y contenido de inicio

Proyecto: Maison RDL.
Estado: En curso. Tarjetas de los dos listados bloqueadas por dependencia: falta la decisión de Roger sobre imágenes de producto (ver Pendiente).
Responsable: Daniel.
Revisor: Lydia; Roger si afecta a la composición.
Revisora de esta entrega: Gaby (revisión y aprobación de la PR). Revisión pendiente.
Rama: codex/estructura-home (creada desde origin/main f2c8b10 el 23/10/2026).
Depende de: T02 y primera versión T03.
Archivos previstos: index.html y ficha propia; recursos nuevos solo coordinados.
Responsable activo de los archivos: Daniel, para index.html y esta ficha mientras dure T04. assets/css/styles.css solo se regenera con el build.
PR: pendiente.

## Instrucciones

Aplicar [el prompt maestro](../PROMPT-MAESTRO.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Usar la guía y los fragmentos comunes de Roger.
2. Añadir campaña del hero y dos listados horizontales: Nuevos lanzamientos y Más vendidos.
3. Completar tarjetas con inventario real del proyecto y enlaces relativos.
4. Mantener HTML semántico, metadatos iniciales y alt apropiados.
5. Probar navegación y entregar por PR a Roger para D01 sin dejar contenido obligatorio vacío.

## Criterios de cierre

- [ ] La home tiene todo el contenido exigido, navbar/footer y enlaces verificables.
- [ ] No introduce una identidad visual diferente ni cambios no coordinados en estilos comunes.
- [ ] Comprobaciones pertinentes documentadas con evidencia real.
- [ ] PR revisada por otra persona, integrada y resultado verificado.

## Decisiones

Sesión del 23/10/2026. Dependencias comprobadas en origin/main: T02 integrada (PR #4 y cierre en PR #5; src/partials, docs/componentes.html y estilos presentes) y T03 integrada (PR #6; docs/inventario-productos.md y docs/fuentes-imagenes.md presentes).

- De los veinte productos del inventario, solo cuatro tienen imagen propia: MRDL-CAM-001, MRDL-PAN-001, MRDL-CAL-001 y MRDL-ACC-001. Repartirlos entre los dos listados (2 + 2, o los cuatro repetidos) o usar imágenes provisionales para otros productos depende de Roger. Daniel decide esperar esa decisión: no se añaden tarjetas en esta sesión.
- Avance independiente en index.html: orden de secciones según la composición de [docs/diseno.md](../docs/diseno.md) (hero → Nuevos lanzamientos sobre ivory → bloque Maison sobre olive → Más vendidos sobre paper → footer); títulos con el patrón compartido `section-title`, contenedor `site-container` y enlace «Ver la colección» con `text-link`; se retiran el bloque vacío y los comentarios del esqueleto T01. Cada listado tiene un comentario que marca dónde irán las tarjetas.
- Sin cambios en hero, navbar, popovers de búsqueda y cuenta, bloque Maison, footer, estilos fuente, fragmentos ni en las otras páginas. El footer coincide con src/partials/footer.html; la cabecera solo difiere en la variante sobre foto documentada para inicio.

## Pendiente

- Roger: decidir qué productos e imágenes usan los listados (ver [imágenes pendientes](../docs/fuentes-imagenes.md#imágenes-pendientes)). Después, Daniel añade las tarjetas con `product-track` y `product-card` del muestrario: imagen local con width/height y alt del inventario, nombre, precio y enlace a producto.html como ficha demostrativa compartida.
- Repetir build y comprobaciones tras añadir las tarjetas.
- Gaby: revisar y aprobar la PR. Commit, push y PR presentados por Daniel el 23/10/2026; faltan las tarjetas de los listados. Revisión pendiente.
- D01 (Roger): acabado visual final.
- Criterio de cierre «La home tiene todo el contenido exigido» no cumplido: faltan las tarjetas de los dos listados.

## Comprobaciones y evidencia

23/10/2026, rama codex/estructura-home:
- npm run build: correcto (tailwindcss v4.3.3). assets/css/styles.css regenerado por las nuevas utilidades de index.html; no se edita a mano.
- Comprobación de index.html con un script Python (html.parser, no añadido al repositorio): 0 de 53 referencias rotas (href, src, srcset, popovertarget, aria-labelledby y aria-describedby, incluidas anclas); sin IDs duplicados; un h1 y un h2 por sección.
- Footer comparado con src/partials/footer.html: idéntico salvo el salto de línea final del fragmento.
- Navegador: Chromium headless ya presente en la caché del entorno, controlado por DevTools Protocol desde un script de Node sin dependencias (no añadido al repositorio), con servidor python3 -m http.server. A 375×667, 768×1024 y 1280×800: sin desbordamiento horizontal (scrollWidth igual al ancho), orden y fondos de sección correctos (ivory, olive, paper), logos e imagen de hero cargados (hero.webp en móvil/tablet, hero-desktop.webp en escritorio) y fuentes Cormorant Garamond y Manrope cargadas. Capturas revisadas localmente, no incluidas en el repositorio.
- No ejecutados: navegación por teclado y popovers, validación HTML con validador externo y pruebas de las tarjetas (todavía no existen).

## Traspaso y siguiente paso

Cuando Roger decida sobre las imágenes, completar las tarjetas en esta rama, repetir las comprobaciones y presentar la PR para Gaby. Tras integrarla, Roger recibe index.html en D01 y se libera la reserva.
