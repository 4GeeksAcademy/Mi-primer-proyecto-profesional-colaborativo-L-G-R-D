# T05 — Estructura y contenido de catálogo

Proyecto: Maison RDL.
Estado: En revisión (PR pendiente de revisión de Gaby).
Responsable: Daniel.
Revisor: Lydia; Roger si afecta a la composición.
Revisora de esta entrega: Gaby (revisión y aprobación de la PR). Revisión pendiente.
Rama: codex/estructura-catalogo (creada desde origin/main 6e54093 el 23/10/2026).
Depende de: T02 y T03 completo.
Archivos previstos: catalogo.html y ficha propia.
Responsable activo de los archivos: Daniel, para catalogo.html y esta ficha mientras dure T05. assets/css/styles.css solo se regenera con el build.
PR: pendiente.

## Instrucciones

Aplicar [el prompt maestro](../PROMPT-MAESTRO.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Añadir filtros HTML etiquetados por categoría y talla sin prometer filtrado dinámico.
2. Mostrar veinte productos con nombres, precios e imágenes del inventario.
3. Seguir la composición de Roger y preparar la rejilla adaptable.
4. Incluir navbar/footer y enlaces de producto.
5. Revisar contenido, rutas y semántica antes de entregar para D02.

## Criterios de cierre

- [ ] Veinte tarjetas y filtros completos, sin datos contradictorios.
- [ ] Las cinco filas se entienden como referencia de escritorio; no se fuerza esa altura en móvil.
- [ ] Comprobaciones pertinentes documentadas con evidencia real.
- [ ] PR revisada por otra persona, integrada y resultado verificado.

## Decisiones

Sesión del 23/10/2026. Dependencias en origin/main: T02 (PR #4/#5) y T03 completo (PR #6) integrados. Revisora de esta entrega: Gaby.

- Veinte tarjetas, una por producto del [inventario](../docs/inventario-productos.md), en su orden (camisas, pantalones, calzado, accesorios). Datos generados desde el inventario con un script temporal fuera del repositorio.
- Imágenes: los cuatro productos con foto propia la muestran con alt del inventario, width/height reales y `loading="lazy"`. Los dieciséis restantes muestran un hueco 3:4 «Imagen pendiente» (decisión de Daniel mientras Roger no decida; sin reutilizar fotos de otros artículos).
- Rejilla con el patrón del muestrario: `grid-cols-1 min-[360px]:grid-cols-2 lg:grid-cols-4`. Cuatro columnas × cinco filas en escritorio; dos columnas en tablet y móvil, una por debajo de 360 px. No se fuerza el 4×5 en pantallas pequeñas.
- Filtros estáticos sin formulario: categoría con cinco radios (`choice`, «Todas» marcada) en un fieldset; talla con un `select` (`field`) agrupado por tipo (letras, talla francesa, numeración europea, centímetros y «Única») con las tallas reales del inventario. Un texto visible, asociado con aria-describedby, aclara que no cambian los productos ni envían datos.
- Todas las tarjetas enlazan a producto.html y el texto inicial indica que abren la misma ficha de ejemplo. Precios con dos decimales, como el carrito.
- Se conservan los IDs `filtros-titulo` y `productos-titulo` (el footer enlaza a `catalogo.html#productos-titulo`). Navbar, popovers y footer sin cambios; el footer coincide con src/partials/footer.html. Se sustituyen los comentarios del esqueleto T01.

## Pendiente

- Gaby: revisar y aprobar la PR.
- Roger: decidir las dieciséis imágenes pendientes; D02 para el acabado visual.
- No ejecutados: navegación completa por teclado, validación HTML con validador externo.

## Comprobaciones y evidencia

23/10/2026, rama codex/estructura-catalogo:
- npm run build: correcto. Utilidades nuevas en el CSS generado: `gap-x-6`, `justify-center` y `mt-12`.
- Script Python (html.parser, fuera del repositorio) sobre catalogo.html: 73 referencias, 0 rotas (incluidas anclas, `for` y aria-describedby); sin IDs duplicados; 6 imágenes con alt, width y height; select con label; un h1, 20 h3 (uno por tarjeta).
- Navegador (Chromium headless del entorno vía DevTools, servidor python3 -m http.server): 20 tarjetas y 6/6 imágenes cargadas en todos los tamaños; sin desbordamiento horizontal. Columnas de la rejilla: 1 a 320×640, 2 a 375×667, 2 a 768×1024 y 4 a 1280×800. Filtros en una columna hasta 1023 px y en dos desde 1024 px. Capturas revisadas localmente, no incluidas en el repositorio.

23/10/2026, resolución de conflicto en codex/estructura-catalogo tras integrarse la PR #12 (producto):
- Conflicto solo en assets/css/styles.css. Se incorpora origin/main (e5c7880) con merge y se regenera el CSS con npm run build; sin marcas de conflicto y sin edición manual.
- Repetidas tras el merge: script Python sobre catalogo.html (73 referencias, 0 rotas) y producto.html (51, 0 rotas); navegador a 320, 375, 768 y 1280 px sin desbordamiento, 20 tarjetas, rejilla de 1/2/2/4 columnas e imágenes cargadas; producto a dos columnas en escritorio.

## Traspaso y siguiente paso

PR presentada por Daniel para revisión de Gaby, sin fusionar. Tras integrarla, Roger recibe catalogo.html en D02 y se libera la reserva.
