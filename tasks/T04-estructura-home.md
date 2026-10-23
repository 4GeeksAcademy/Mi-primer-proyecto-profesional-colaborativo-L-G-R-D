# T04 — Estructura y contenido de inicio

Proyecto: Maison RDL.
Estado: En revisión. Estructura integrada en la PR #8; tarjetas de los dos listados en una segunda PR pendiente de revisión.
Responsable: Daniel.
Revisor: Lydia; Roger si afecta a la composición.
Revisora de esta entrega: Gaby (revisión y aprobación de la PR). Revisión pendiente.
Rama: codex/estructura-home (creada desde origin/main f2c8b10 el 23/10/2026; integrada en la PR #8). Tarjetas: codex/tarjetas-home, creada desde origin/main 6e54093 el 23/10/2026.
Depende de: T02 y primera versión T03.
Archivos previstos: index.html y ficha propia; recursos nuevos solo coordinados.
Responsable activo de los archivos: Daniel, para index.html y esta ficha mientras dure T04. assets/css/styles.css solo se regenera con el build.
PR: #8 integrada (estructura de secciones). PR de tarjetas: ver Traspaso.

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

### Tarjetas (segunda sesión, 23/10/2026)

- Roger todavía no ha decidido sobre las dieciséis imágenes pendientes. Daniel decide mostrar en esos productos un hueco 3:4 con el texto «Imagen pendiente», sin reutilizar fotos de otros artículos. El hueco es decorativo (`aria-hidden`); el nombre del producto es el texto del enlace.
- Nuevos lanzamientos: MRDL-CAM-001 y MRDL-PAN-001 (con foto), MRDL-CAM-003 y MRDL-CAL-003 (imagen pendiente). Más vendidos: MRDL-CAL-001 y MRDL-ACC-001 (con foto), MRDL-PAN-002 y MRDL-ACC-004 (imagen pendiente). Ningún producto se repite y las cuatro categorías aparecen en el inicio.
- Tarjetas con los patrones `product-track` y `product-card` del muestrario: imagen local con width/height reales (850 × 1133), alt del inventario y `loading="lazy"`; nombre; precio con dos decimales (formato del carrito de T07, mismo valor que el inventario); enlace a producto.html.
- Cada listado indica que los datos son ficticios y que todas las tarjetas abren la misma ficha de ejemplo; Más vendidos aclara que la selección no se basa en ventas reales.
- Datos generados desde docs/inventario-productos.md con un script temporal fuera del repositorio, para evitar errores de copia.

## Pendiente

- Gaby: revisar y aprobar la PR de tarjetas.
- Roger: decidir las dieciséis imágenes pendientes; al llegar, sustituir los huecos «Imagen pendiente» por la imagen y su alt.
- D01 (Roger): acabado visual final.
- No ejecutados: navegación completa por teclado y popovers, validación HTML con validador externo.

## Comprobaciones y evidencia

23/10/2026, rama codex/estructura-home:
- npm run build: correcto (tailwindcss v4.3.3). assets/css/styles.css regenerado por las nuevas utilidades de index.html; no se edita a mano.
- Comprobación de index.html con un script Python (html.parser, no añadido al repositorio): 0 de 53 referencias rotas (href, src, srcset, popovertarget, aria-labelledby y aria-describedby, incluidas anclas); sin IDs duplicados; un h1 y un h2 por sección.
- Footer comparado con src/partials/footer.html: idéntico salvo el salto de línea final del fragmento.
- Navegador: Chromium headless ya presente en la caché del entorno, controlado por DevTools Protocol desde un script de Node sin dependencias (no añadido al repositorio), con servidor python3 -m http.server. A 375×667, 768×1024 y 1280×800: sin desbordamiento horizontal (scrollWidth igual al ancho), orden y fondos de sección correctos (ivory, olive, paper), logos e imagen de hero cargados (hero.webp en móvil/tablet, hero-desktop.webp en escritorio) y fuentes Cormorant Garamond y Manrope cargadas. Capturas revisadas localmente, no incluidas en el repositorio.
- No ejecutados: navegación por teclado y popovers, validación HTML con validador externo y pruebas de las tarjetas (todavía no existen).

23/10/2026, rama codex/tarjetas-home:
- npm run build: correcto. assets/css/styles.css regenerado; única utilidad nueva `justify-center`.
- Comprobación de index.html con script Python (html.parser, no añadido al repositorio): 66 referencias, 0 rotas (incluidas anclas y controles); sin IDs duplicados; 7 imágenes, todas con alt, width y height; un h1, 10 h2 y 8 h3 (uno por tarjeta).
- Navegador (mismo Chromium headless y script DevTools, servidor python3 -m http.server): 8 tarjetas y 7/7 imágenes cargadas. 375×667: página sin desbordamiento horizontal, una tarjeta visible por fila con desplazamiento interno. 768×1024: dos visibles con desplazamiento interno. 1280×800: cuatro visibles sin desplazamiento. Capturas revisadas localmente, no incluidas en el repositorio.

23/10/2026, resolución de conflicto en codex/tarjetas-home tras integrarse la PR #12 (producto):
- Conflicto solo en assets/css/styles.css. Se incorpora origin/main (e5c7880) con merge y se regenera el CSS con npm run build; sin marcas de conflicto y sin edición manual. El CSS contiene las utilidades del inicio y las de producto.
- Repetidas tras el merge: script Python sobre index.html (66 referencias, 0 rotas) y producto.html (51, 0 rotas); navegador a 320, 375, 768 y 1280 px sin desbordamiento, 8 tarjetas e imágenes cargadas en inicio y bloque a dos columnas en escritorio en producto.

## Traspaso y siguiente paso

PR de tarjetas presentada por Daniel para revisión de Gaby, sin fusionar. Tras integrarla, Roger recibe index.html en D01 y se libera la reserva.
