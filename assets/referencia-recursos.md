> Antecedente de procedencia, no inventario de archivos vigentes. Algunos recursos de esta primera propuesta se retiraron; las portadas actuales son hero-equipo y los recursos usados se verifican con tools/check_site.py.

# Maison RDL — Fotografías, tipografía y logo

Las fotografías son imágenes de muestra creadas con la herramienta integrada image_gen para esta propuesta, no fotografías de productos reales ni recursos copiados de las referencias.

| Archivo servido | Uso | Tamaño aproximado |
| --- | --- | --- |
| assets/images/hero-desktop.webp | Hero panorámico, desde 1024 px | 262 kB |
| assets/images/hero.webp | Hero vertical en móvil/tablet | 224 kB |
| assets/images/shirt.webp | Camisa de muestra | 80 kB |
| assets/images/trousers.webp | Pantalón de muestra | 95 kB |
| assets/images/bag.webp | Bolso de muestra | 119 kB |
| assets/images/shoes.webp | Mocasines de muestra | 99 kB |

Las imágenes seleccionadas están guardadas dentro de esta propuesta. Los originales de generación no se incluyen en este envío. Los prompts y rutas de las versiones WebP incluidas están en [images.json](prompts-referencia.json) y [hero-desktop.json](prompt-hero-referencia.json). Se optimizaron a WebP conservando la imagen completa; la presentación usa recorte responsive con CSS. El hero panorámico se generó como reencuadre de la campaña vertical.

## Fuentes

Cormorant Garamond y Manrope, descargadas desde Google Fonts y servidas localmente. Las licencias SIL OFL acompañan los archivos en assets/fonts/. Los pesos de Manrope comparten un archivo variable; los dos estilos de Cormorant usan sus archivos correspondientes.

## Logo

Los archivos SVG de assets/brand/ están trazados en contornos, sin depender de la carga de una fuente. Se ha diseñado la composición y el espaciado sobre Cormorant Garamond y Manrope. No se presenta como una tipografía propietaria.

Variantes:
- logo-ink.svg y logo-ivory.svg: firma apilada de cabecera.
- logo-horizontal-ink.svg y logo-horizontal-ivory.svg: firma horizontal.
- monogram-ink.svg y monogram-ivory.svg: iniciales RDL.
- Variantes bronze: uso de acento sobre fondo oscuro, comprobar contraste al aplicar.
- assets/favicon.svg: R simplificada para tamaño pequeño.

Ver la lámina de identidad (antecedente en el historial Git).

## Investigación 2026

- [Adobe: Modern Retro Serif](https://www.adobe.com/express/learn/blog/microtrend-modern-retro-serif), publicado en 2026: combinación de serif clásicas y composición contemporánea.
- [Fontfabric: Typography Trends for 2026](https://www.fontfabric.com/blog/top-typography-trends-for-2026/), enero de 2026, actualizado en septiembre: protagonismo de la tipografía, serif de carácter, proporciones y ligaduras.
- [Bonhomme: Visual Codes of Luxury in 2026](https://bonhommeparis.com/en/knowledge-center/Branding-and-Luxury/Visual-Codes-of-Luxury-in-2026), actualizado el 16 de octubre de 2026: identidad tipográfica, espacio y materialidad. Es el análisis de un estudio, no una norma universal.

La propuesta elige los principios compatibles con Maison RDL y el alcance HTML/Tailwind. No reproduce logos de Prada, Chanel, Burberry ni otras marcas presentes en los moodboards de Roger.
