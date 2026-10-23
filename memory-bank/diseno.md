> Estado actual: diseño/SEO de PR #13 aprobados e integrados; sitio publicado. Las instrucciones de traslado T01/T02 se conservan como antecedentes, no deben repetirse. Las referencias antiguas retiradas se recuperan del historial Git.

# Maison RDL — Guía visual compartida v0.1

Fecha: 23/10/2026. Responsable: Roger.
Estado: base visual T02 aprobada por Lydia e integrada en main mediante la PR #4. Verificación técnica y pendientes en [T02](../tasks/T02-base-visual.md); no equivale a aprobación final de las cinco vistas.

## Dirección

**Lujo editorial cálido:** fotografía protagonista, serif expresiva, texto funcional limpio, espacio generoso y contraste entre marfil, piedra y oliva profundo. El aspecto premium se construye con composición, legibilidad y consistencia.

La referencia concreta es la portada HTML (antecedente en el historial Git), su [captura de escritorio](../evidencias/referencia-desktop.png), su [captura móvil](../evidencias/referencia-mobile.png) y la lámina de identidad (antecedente en el historial Git). Se conservan dos capturas de la referencia en evidencias; el material histórico restante está en Git. Durante T02 trasladar los recursos necesarios al sitio final sin confundir la referencia con las cinco páginas de entrega.

Verin, Levor y las capturas aportadas inspiran tipografía editorial, fotografía cálida y sobriedad. No copiar sus logos, imágenes ni promesas comerciales. Investigación y procedencia: [recursos de la propuesta](../assets/referencia-recursos.md).

## Fuente de verdad

- Valores reutilizables: [src/styles/tokens.css](../src/styles/tokens.css).
- Esta guía define usos y composición; los tokens definen valores.
- Roger mantiene ambos. Daniel y Lydia usan sus clases, patrones y fragmentos comunes.
- La preview contiene componentes de referencia; T02 debe trasladarlos y adaptar navegación a los cinco HTML reales.
- Las propuestas para catálogo/producto/carrito/checkout de esta guía orientan estructura; Roger realiza y revisa su acabado.
- Las [exigencias del proyecto](requisitos.md) prevalecen sobre simplificaciones estéticas.

## Paleta y contraste

Los valores reproducen la portada actual. Se añaden nombres semánticos para colores que antes estaban escritos directamente en su CSS.

| Token Tailwind | Valor | Uso |
| --- | --- | --- |
| ivory | #F3F0E9 | Fondo principal; texto sobre zonas oscuras |
| ink | #262A22 | Texto principal sobre fondos claros |
| muted | #57534D | Texto secundario sobre marfil/piedra |
| sand | #E5DED1 | Apoyo cálido puntual |
| stone | #E9E5DF | Fondo neutro de imágenes |
| paper | #E7E3D9 | Sección de Más vendidos |
| olive | #343B2E | Sección de marca |
| night | #22271F | Footer |
| line | #CFC8BD | Separación decorativa en fondos claros |
| control | #746D63 | Borde de inputs/selectores |
| bronze | #7A6143 | Acento oscuro y foco sobre fondos claros |
| gold | #A89270 | Variante bronce del logo/decoración; no texto pequeño en marfil |
| on-dark-muted | #C4C7B9 | Texto secundario del footer |
| on-olive-muted | #D6D6CA | Texto secundario sobre oliva |
| dark-line | #5B6252 | Separadores del footer |
| gold-light | #D0BD99 | Etiqueta sobre oliva |

Combinaciones base: ink/ivory, ink/paper, ivory/olive, ivory/night. No usar muted sobre oliva ni gold como texto de cuerpo en fondo claro. El borde decorativo line no sustituye al borde control. Los campos usan superficie ivory con borde control (3.21:1); si se colocan directamente sobre paper, usar borde bronze, porque control/paper da 2.85:1. El foco usa bronze en claro e ivory en oscuro. Comprobar contraste real de textos, controles y foco: objetivo interno 4.5:1 texto normal, 3:1 texto grande y límites/estados relevantes. Sobre fotos, mantener la gradación oscura y comprobar cada recorte.

No añadir otros colores de marca por página. Para un estado de error, usar mensaje e indicador accesible; coordinar con Roger el color semántico si llega a implementarse.

## Tipografía y marca

- Cormorant Garamond 500 para títulos, con italic puntual en campaña.
- Manrope 400/500/600 para texto, navegación, precios, formularios y acciones.
- Servir los WOFF2 locales con sus licencias OFL; no descargar más familias por página.
- El logo es un SVG trazado: no recomponerlo con una fuente del navegador ni deformarlo.
- Variantes tinta sobre claro y marfil sobre oscuro; bronce reservado para usos que mantengan contraste.
- Logo centrado en cabecera; ancho de referencia 128 px escritorio, 116 tablet, 104 móvil. Mantener proporción y área libre de al menos un cuarto de su altura. Usar el favicon simplificado para tamaños pequeños.
- Archivos actuales: assets/brand (antecedente en el historial Git). Trasladarlos en T02 sin cambiar nombres arbitrariamente.

| Elemento | Escritorio | Tablet | Móvil |
| --- | --- | --- | --- |
| Titular de hero | clamp(84px, 7.7vw, 118px) | 88px | 58px; 52px en pantallas de poca altura |
| Título de sección | 50px | 42px | 38px |
| Texto funcional nuevo | 14–16px | 14–16px | 14–16px |
| Etiquetas editoriales | 10–12px | 10–12px | Revisar legibilidad; no usar 8–10px para campos/precios esenciales |

El hero usa interlineado 0.94 y tracking -0.04em; secciones 1.1 y -0.03em. Son estilos de titulares, no de párrafos. La preview contiene microetiquetas menores en móvil: revisarlas al integrar, sin trasladar ese tamaño a información necesaria para comprar.

## Geometría y responsive

- Contenedor: max-width 1440px; márgenes laterales 56px escritorio, 32px tablet, 20px móvil.
- Breakpoints del diseño: móvil <640px; tablet 640–1023px; escritorio ≥1024px.
- Separación vertical de colecciones: 78px arriba / 88px abajo escritorio, 60px tablet y 48px móvil.
- Espaciado ordinario: 4, 8, 12, 16, 24, 32, 48, 64px; reutilizar valores existentes.
- Tarjetas sin caja exterior, sombra fuerte ni redondeados grandes; fotos 3:4 con recorte consistente.
- Gap entre tarjetas 24px escritorio/tablet, 16px móvil.
- Filas horizontales de home: cuatro tarjetas escritorio, dos tablet, aproximadamente 78% del ancho por tarjeta móvil. Desplazamiento nativo dentro de la fila; la página no desborda.
- Catálogo: cuatro columnas escritorio, dos en tablet/móvil cuando nombres y precios quepan; bajar a una en anchuras que lo requieran.
- Acciones iconográficas: área de interacción mínima de referencia 44×44px.
- No bloquear zoom ni ocultar desbordamiento para encubrir un layout roto.

## Componentes comunes

| Componente | Regla compartida |
| --- | --- |
| Navbar | Logo, navegación, acceso a búsqueda con campo real, cuenta y carrito; misma estructura e información en cinco vistas |
| Cabecera de inicio | Superpuesta a la foto, logo marfil, gradación para legibilidad |
| Cabecera interna | En flujo normal, fondo marfil y logo tinta; no heredar posición absoluta sin una variante explícita |
| Menú móvil | details/summary o patrón HTML nativo comprobado; nombre accesible y foco visible |
| Acción principal | Rectangular; fondo ink y texto ivory sobre páginas claras; versión ivory/ink en hero; altura cómoda y foco visible |
| Acción secundaria | Enlace subrayado o borde control; no depender solo de hover |
| Tarjeta | Imagen 3:4, nombre, precio y enlace; misma alineación, espaciado y jerarquía |
| Campo | Label persistente, texto legible, borde control, estados de foco y deshabilitado; placeholder no sustituye al label |
| Resumen de compra | Importes alineados, subtotal/impuestos/total diferenciados; sin sombras o adornos nuevos por página |
| Footer | Fondo night, texto ivory y on-dark-muted, categorías/legal/marca/contacto con destinos reales |

Clases orientativas basadas en los tokens: `bg-ivory text-ink font-body`, `font-display`, `bg-olive text-ivory`, `border-control`. No copiar colores hex por cada página.

Priorizar utilidades Tailwind para layout, espaciado, breakpoints y estados. Mantener CSS adicional solo para tokens y patrones compartidos/específicos justificados. La preview es una referencia visual, no una excusa para sustituir todo el ejercicio de Tailwind por CSS manual.

Los fragmentos en src/partials son copias de referencia, no includes automáticos. Roger actualiza las cinco copias coordinadamente. El patrón compartido admite la variante clara de cabecera interna.

## Cinco composiciones

1. Inicio: hero de primera pantalla completa → Nuevos lanzamientos sobre marfil → bloque editorial oliva → Más vendidos sobre paper → footer night. Los dos listados horizontales son obligatorios.
2. Catálogo: cabecera clara → título y filtros categoría/talla → veinte productos → footer oscuro. La decoración no oculta los filtros.
3. Producto: cabecera clara → imagen/datos a dos columnas (aproximadamente 50/50) → materiales/usos → footer. En móvil, imagen y datos apilados.
4. Carrito: cabecera clara → tres líneas de producto y resumen al lado → footer. En móvil, resumen tras productos. Mantener subtotal, impuestos, total y enlace a checkout.
5. Checkout: cabecera clara → tres bloques numerados de campos → resumen opcional → footer. En móvil, una columna. Botón final deshabilitado y aviso de demo.

El hero a pantalla completa corresponde solo a inicio: height 100svh con foto panorámica en escritorio y retrato en tablet/móvil. Titular y CTA siguen siendo HTML. Mantener rostros visibles y CTA dentro de la primera pantalla incluso a 375×667; no imponer una altura mínima mayor que el viewport.

## Base reutilizable T02

Base integrada mediante la PR #4: muestrario (antecedente en el historial Git), [navbar](../src/partials/navbar.html), [footer](../src/partials/footer.html) y [entrada CSS](../src/styles/input.css). Los valores de tokens no cambian. Las fuentes se declaran en la entrada CSS; las rutas `../fonts/` se resuelven desde `assets/css/styles.css`, no desde el HTML. Recursos y licencias: [procedencia](../assets/PROCEDENCIA.md).

- `site-container`: márgenes de 20/32/56 px; `section-title`: Cormorant 38/42/50 px. `font-body`: Manrope.
- `site-header`: cabecera clara en flujo normal. Inicio añade `site-header--photo on-dark` y usa `logo-ivory.svg`; no aplicar esa variante a internas.
- `btn`, `btn--secondary`, `btn--light`, `text-link`, `field`, `choice` y `product-card`: patrones del muestrario. Layout, espaciado, rejillas y estados puntuales siguen usando utilidades Tailwind. `product-track` prepara los dos listados horizontales de T04, aún sin inventario.
- `on-dark` cambia el foco a marfil. Los paneles `surface-light` recuperan foco bronce. Deshabilitar controles con `disabled`, no solo una apariencia visual.
- Menú `details/summary` y paneles `popover` nativos, sin JavaScript. Escape cierra popovers; el menú se vuelve a cerrar con su summary. Búsqueda sin formulario ni envío; cuenta sin credenciales.
- Los fragmentos tienen rutas para HTML en la raíz: copiar su contenido, ajustar `aria-current="page"` y ajustar rutas relativas si se copian a un subdirectorio. No enlazarlos con `iframe`, `fetch` ni includes supuestos. Sincronizar siempre las cinco copias al cambiar un fragmento.
- Los enlaces de categorías llevan a la sección de productos del catálogo, no activan filtros. Los textos legales y el contacto describen solo la demo, sin domicilios o condiciones comerciales inventados.
- Hero: foto panorámica desde 1024 px, vertical por debajo; `100svh`, titular HTML de 58/88/104 px y 52 px en poca altura. Sin tipografía basada en `vw` ni tracking negativo nuevo; ajuste de legibilidad sobre la referencia, no cambio de identidad. CTA de 48 px y gradación oscura compartida.

### Esquemas de las cuatro vistas internas

Esquemas para contenido posterior, no tareas de estructura ya completadas:

| Vista | Escritorio (desde 1024 px) | Tablet y móvil | Traspaso |
| --- | --- | --- | --- |
| Catálogo | Cabecera clara → título → filtros categoría/talla en fila → rejilla `grid grid-cols-2 gap-6 lg:grid-cols-4` → footer | Filtros apilados; tarjetas con `min-w-0`, una columna si no caben nombre/precio; imágenes 3:4 | T05 añade veinte entradas del inventario T03; no duplicar ejemplos para aparentar catálogo |
| Producto | Cabecera → imagen y datos `grid gap-8 lg:grid-cols-2` → descripción/materiales/usos a ancho completo → footer | Imagen antes de datos; label visible para talla/cantidad; acción a ancho cómodo | T06 aporta nombre, referencia, precio y contenido; enlazar el recorrido a carrito sin prometer persistencia |
| Carrito | Cabecera → título → `grid gap-8 lg:grid-cols-[minmax(0,2fr)_minmax(0,1fr)]`: líneas a izquierda, resumen a derecha → footer | Líneas apiladas; resumen después, importes con `tabular-nums`; evitar tabla de ancho fijo | T07 añade tres líneas, subtotal/impuestos/total y Comprar desde inventario común |
| Checkout | Cabecera → título → tres bloques numerados en orden, columna de lectura `max-w-3xl`; resumen lateral solo si procede → footer | Una columna; campos `field`, labels persistentes, nunca ocultar una etapa tras pestañas | T08 desarrolla campos y resumen; sin formulario que envíe datos y botón final siempre deshabilitado |

Usar separadores `border-line` y superficies sin tarjetas exteriores ni sombras. En resúmenes sobre paper mantener inputs ivory; borde control solo sobre ivory, bronze si el campo se coloca directamente sobre paper.

## Recursos y comportamiento

- Fotos locales: luz cálida, materiales reconocibles y fondos sobrios. Documentar origen; no afirmar instalaciones, antigüedad o certificaciones ficticias.
- Imagen principal sin lazy loading; resto según posición. Width/height, tamaños eficientes y picture cuando haya recortes distintos.
- Sin carrusel automático, preloader, vídeo de fondo ni librería de animación. Hover discreto, foco equivalente y reducción de movimiento.
- HTML nativo para menús/paneles cuando aporte valor. Los quickviews de la preview no reemplazan producto.html ni carrito.html.
- Antes de integrar D01, sustituir los destinos de demo por enlaces reales del recorrido.
- Búsqueda/filtros/cuenta son demostraciones estáticas: explicar el alcance donde sea necesario sin prometer resultados dinámicos.
- Conservar las cinco páginas, Schema.org, semántica y datos visibles aunque la referencia visual sea más minimalista.

## Revisión por Roger

Antes de integrar una vista: misma paleta/fuentes, componentes comunes, contenido de la rúbrica completo, imágenes coherentes, foco/teclado, móvil/tablet/escritorio, ausencia de overflow y enlaces válidos.

Un cambio de marca se registra aquí y en los tokens dentro de la misma PR. Daniel y Lydia pueden proponer ajustes con una captura y motivo; no crear variantes de identidad por su cuenta. Las PR de Roger las revisa Daniel o Lydia.

## Cabecera final — 23/10/2026

Menú pegajoso. Superposición con degradado neutro al inicio de la portada; al desplazar usa night (#22271F), texto y logo marfil. Las vistas internas conservan marfil/tinta. Contraste reforzado en muted y control; los tokens son la fuente de verdad. Ver memory-bank/verificacion.md.
