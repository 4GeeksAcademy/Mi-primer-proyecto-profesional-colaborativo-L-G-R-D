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

## Imágenes pendientes

Dieciséis productos no tienen imagen propia: MRDL-CAM-002 a 005, MRDL-PAN-002 a 005, MRDL-CAL-002 a 005 y MRDL-ACC-002 a 005. En el inventario figuran como «pendiente», con una ruta prevista en `assets/images/productos/` que todavía no existe.

Pendiente de decidir con Roger:

1. **Cómo conseguir las imágenes.** Generarlas con el mismo estilo que las cuatro actuales (fondo de yeso o piedra clara, luz cálida, formato 3:4) o usar recursos con un permiso de uso comprobado. No descargar imágenes sin comprobar ese permiso. Registrar en este documento la procedencia de cada nueva imagen.
2. **Qué mostrar mientras tanto.** Si el catálogo necesita imagen antes de tenerlas, reutilizar provisionalmente la imagen de la misma categoría solo con el acuerdo de Roger. En ese caso el texto alternativo debe describir lo que se ve, no el producto de la ficha, y la tarjeta no debe dar a entender que la foto es de ese artículo.
3. **Tratamiento técnico.** Tamaño, formato, recorte y optimización corresponden a Roger (T12).

Hasta que haya decisión, los 16 productos tienen todos sus datos salvo la imagen.
