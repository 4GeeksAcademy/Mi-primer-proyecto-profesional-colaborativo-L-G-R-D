> Estado vigente a 23/10/2026: Implementación integrada hasta PR #13; reorganización documental en PR #14 pendiente de revisión. Los apartados de preparación y sesiones anteriores se conservan como historial. Fuente actual: [progress](../memory-bank/progress.md) y [verificación](../memory-bank/verificacion.md).

# T06 — Estructura y contenido de producto

Proyecto: Maison RDL.
Estado: Implementación integrada hasta PR #13; reorganización documental en PR #14 pendiente de revisión.
Responsable: Daniel.
Revisor: Lydia; Roger si afecta a la composición.
Revisora de esta entrega: Gaby (revisión y aprobación de la PR). Revisión pendiente.
Rama: codex/estructura-producto (creada desde origin/main 6e54093 el 23/10/2026).
Depende de: T02 y primera versión T03.
Archivos previstos: producto.html y ficha propia.
Responsable activo de los archivos: Daniel, para producto.html y esta ficha mientras dure T06. assets/css/styles.css solo se regenera con el build.
PR: pendiente.

## Instrucciones

Aplicar [el prompt maestro](../AGENTS.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Preparar imagen y datos con estructura compatible con las dos columnas previstas por Roger.
2. Incluir nombre, referencia, talla, precio, cantidad y navegación al carrito de ejemplo.
3. Completar materiales y usos recomendados.
4. Usar controles etiquetados, imagen con alt y navbar/footer coherentes.
5. Aclarar el carácter demostrativo del carrito sin afirmar persistencia de selección.

## Criterios de cierre

- [ ] Ficha completa con contenido consistente con catálogo y carrito.
- [ ] PR estructural lista para el diseño D03.
- [ ] Comprobaciones pertinentes documentadas con evidencia real.
- [ ] PR revisada por otra persona, integrada y resultado verificado.

## Decisiones

Sesión del 23/10/2026. Dependencias en origin/main: T02 (PR #4/#5), T03 (PR #6) y T07 (PR #7) integrados.

- Producto de la ficha: MRDL-CAM-001 «Camisa de seda marfil», con foto propia y primera línea del carrito de T07. Referencia, nombre, precio (240,00 €, impuestos incluidos), imagen y alt coinciden con el [inventario](../memory-bank/inventario-productos.md) y con carrito.html; la talla M aparece seleccionada, como en la línea del carrito.
- Composición del esquema de Roger: `grid gap-8 lg:grid-cols-2`, imagen a la izquierda y datos a la derecha en escritorio; apiladas por debajo de 1024 px con la imagen primero. Imagen principal sin lazy loading, con `fetchpriority="high"` y width/height reales.
- Datos: categoría, nombre (h1), referencia, precio, talla (fieldset con radios `choice` y las tallas del inventario), cantidad (`input type="number"` 1–9 con label, patrón `field`) y «Añadir al carrito» como enlace `btn` a carrito.html, sin formulario ni envío.
- Un texto visible, asociado al enlace con aria-describedby, aclara que el carrito de ejemplo muestra una selección fija y que la talla y la cantidad no se guardan. Otro texto indica que todas las tarjetas abren esta misma ficha.
- Debajo, a ancho completo: descripción, materiales y uso recomendado del inventario (tres columnas en escritorio, una en móvil). Ruta de navegación Catálogo / Camisas.
- Navbar, popovers y footer sin cambios; el footer coincide con src/partials/footer.html. Se sustituyen los comentarios del esqueleto T01. Sin Schema.org todavía: corresponde a T09.

## Pendiente

- Gaby: revisar y aprobar la PR.
- D03 (Roger): acabado visual. T09 (Daniel): marcado Product coherente con los datos visibles.
- No ejecutados: navegación completa por teclado, validación HTML con validador externo.

## Comprobaciones y evidencia

23/10/2026, rama codex/estructura-producto:
- npm run build: correcto. Utilidades nuevas en el CSS generado: `gap-x-2`, `gap-x-6`, `mt-1` y `mt-12`.
- Script Python (html.parser, fuera del repositorio) sobre producto.html: 51 referencias, 0 rotas (incluidas `for`, aria-describedby y anclas); sin IDs duplicados; 3 imágenes con alt, width y height; campo de cantidad con label; un h1 (nombre del producto).
- Coherencia con carrito.html: misma referencia, nombre, precio, imagen, alt y talla M.
- Navegador (Chromium headless del entorno vía DevTools, servidor python3 -m http.server): sin desbordamiento horizontal a 320×640, 375×667, 768×1024 y 1280×800; 3/3 imágenes cargadas; bloque imagen/datos en una columna hasta 768 px y en dos a 1280 px. Capturas revisadas localmente, no incluidas en el repositorio. Tras la revisión visual se corrigió la mayúscula inicial de descripción y uso.

## Traspaso y siguiente paso

PR presentada por Daniel para revisión de Gaby, sin fusionar. Tras integrarla, Roger recibe producto.html en D03 y, después, T09 añade el marcado Product. Liberar entonces la reserva.
