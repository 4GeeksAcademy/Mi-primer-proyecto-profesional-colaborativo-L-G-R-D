# Maison RDL — Fuentes de imágenes del inventario

Tarea: [T03](../tasks/T03-inventario.md). Responsable: Daniel; Roger decide la selección visual y la optimización. Actualizado: 23/10/2026.

Relaciona cada imagen local con los productos del [inventario](inventario-productos.md). La procedencia general de los recursos compartidos está en [assets/PROCEDENCIA.md](../assets/PROCEDENCIA.md); este documento no la sustituye.

## Procedencia y permiso de uso

- Las seis imágenes de `assets/images/` llegaron con la base visual de Roger (T02, commit 2b63c59) y son copias idénticas de las de [docs/referencia-visual](referencia-visual/README.md). Comprobado con `cmp` el 23/10/2026.
- Según [la procedencia](../assets/PROCEDENCIA.md) y los [recursos de la referencia](referencia-visual/docs/RECURSOS-Y-BRANDING.md), son imágenes generadas con la herramienta image_gen para esta propuesta. Los prompts están en [images.json](referencia-visual/tools/images.json) y [hero-desktop.json](referencia-visual/tools/hero-desktop.json); los originales de generación no se incluyen.
- Son **imágenes de muestra**: no son fotografías de productos reales ni de prendas que existan. Así deben presentarse.
- No se atribuye ninguna licencia de terceros que no esté acreditada. Si el equipo necesita confirmar las condiciones de uso de la herramienta de generación, queda como consulta pendiente; este documento no la resuelve.
- No se ha descargado ninguna imagen nueva en T03.

## Correspondencia con el inventario

| Archivo | Dimensiones | Peso | Qué muestra | Producto | Estado |
| --- | --- | --- | --- | --- | --- |
| assets/images/shirt.webp | 850 × 1133 (3:4) | 80 kB | Camisa marfil de manga larga y cuello clásico en una percha de madera, fondo de yeso claro | MRDL-CAM-001 Camisa de seda marfil | Propia de muestra |
| assets/images/trousers.webp | 850 × 1133 (3:4) | 95 kB | Pantalón ancho taupe de tiro alto con pinzas, colgado de una percha de madera | MRDL-PAN-001 Pantalón ancho de pinzas taupe | Propia de muestra |
| assets/images/shoes.webp | 850 × 1133 (3:4) | 99 kB | Par de mocasines de piel marrón oscuro sobre suelo de piedra clara | MRDL-CAL-001 Mocasín de piel espresso | Propia de muestra |
| assets/images/bag.webp | 850 × 1133 (3:4) | 119 kB | Bolso de piel coñac con solapa, cierre metálico en tono latón y asa superior, sobre un bloque de piedra | MRDL-ACC-001 Bolso de asa corta coñac | Propia de muestra |
| assets/images/hero.webp | 1122 × 1402 | 224 kB | Campaña vertical: dos modelos en una terraza de piedra | Ninguno (hero de inicio) | No es imagen de producto |
| assets/images/hero-desktop.webp | 1672 × 940 | 262 kB | Campaña panorámica con los mismos modelos | Ninguno (hero de inicio) | No es imagen de producto |

Las descripciones de los cuatro productos con imagen se redactaron a partir de lo que se ve en cada foto y de su prompt, para que imagen y ficha coincidan. Los textos alternativos están en cada ficha del inventario.

Nota para Roger: el [muestrario](componentes.html) declara `width="768" height="1024"` en estas cuatro imágenes; los archivos miden 850 × 1133. La proporción 3:4 coincide, así que no hay deformación. Ajustarlo o no es decisión de Roger.

## Imágenes completadas por Roger — 23/10/2026

Generadas con image_gen para cada referencia, como muestras ficticias. WebP de 850 × 1133 px, carga diferida en las tarjetas. No son fotografías de productos reales.

| Referencia | Archivo | Peso |
| --- | --- | --- |
| MRDL-CAM-002 | assets/images/productos/mrdl-cam-002.webp | 35 KiB |
| MRDL-CAM-003 | assets/images/productos/mrdl-cam-003.webp | 98 KiB |
| MRDL-CAM-004 | assets/images/productos/mrdl-cam-004.webp | 85 KiB |
| MRDL-CAM-005 | assets/images/productos/mrdl-cam-005.webp | 110 KiB |
| MRDL-PAN-002 | assets/images/productos/mrdl-pan-002.webp | 60 KiB |
| MRDL-PAN-003 | assets/images/productos/mrdl-pan-003.webp | 67 KiB |
| MRDL-PAN-004 | assets/images/productos/mrdl-pan-004.webp | 83 KiB |
| MRDL-PAN-005 | assets/images/productos/mrdl-pan-005.webp | 78 KiB |
| MRDL-CAL-002 | assets/images/productos/mrdl-cal-002.webp | 77 KiB |
| MRDL-CAL-003 | assets/images/productos/mrdl-cal-003.webp | 99 KiB |
| MRDL-CAL-004 | assets/images/productos/mrdl-cal-004.webp | 80 KiB |
| MRDL-CAL-005 | assets/images/productos/mrdl-cal-005.webp | 75 KiB |
| MRDL-ACC-002 | assets/images/productos/mrdl-acc-002.webp | 56 KiB |
| MRDL-ACC-003 | assets/images/productos/mrdl-acc-003.webp | 104 KiB |
| MRDL-ACC-004 | assets/images/productos/mrdl-acc-004.webp | 165 KiB |
| MRDL-ACC-005 | assets/images/productos/mrdl-acc-005.webp | 119 KiB |

## Portada del equipo

`hero-equipo-desktop.webp` (1672 × 940) y `hero-equipo-mobile.webp` (1122 × 1402): campaña generada con image_gen a petición de Roger, usando las cuatro fotografías personales aportadas como referencia. Conserva el traje estampado y adapta los demás conjuntos a la campaña. Son recreaciones generadas, con parecido aproximado. Los originales anteriores se conservan. Las fotografías personales de referencia no se incluyen en el repositorio.

Descripciones de generación: [manifest de imágenes](imagenes-generadas.json). Revisión y aprobación de Gaby pendientes.
