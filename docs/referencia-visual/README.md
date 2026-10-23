# Referencia visual incluida en el envío al equipo

Ejecutar los comandos de este documento desde docs/referencia-visual. No son todavía los comandos del proyecto final. Para consultar el estilo basta con abrir las capturas de preview/.

# Maison RDL — Primera propuesta del inicio

Propuesta visual para revisión de Roger, Daniel y Lydia. Incorpora las referencias compartidas y las peticiones de un hero a pantalla completa, adaptación móvil/escritorio, mayor contraste y un logo profesional.

## Verla

- Inicio: http://127.0.0.1:8047/
- Logo e identidad: http://127.0.0.1:8047/identidad.html
- [HTML del inicio](index.html)
- [Lámina de identidad](identidad.html)

Servidor local desde esta carpeta:

~~~
python -m http.server 8047 --bind 127.0.0.1
~~~

Si tu entorno usa python3, sustituir el nombre del ejecutable.

El sitio servido es HTML y CSS generado con Tailwind; no contiene JavaScript de aplicación. Las fuentes, imágenes y logos se sirven localmente.

## Construir estilos

~~~
npm install
npm run build
~~~

Tailwind CSS y su CLI 4.3.3 son dependencias de desarrollo. CSS fuente: src/input.css; CSS generado: assets/styles.css. No modificar el generado a mano. Conservar package-lock.json para reproducibilidad; usar npm ci cuando se instale desde el lockfile.

## Propuesta

- Hero de 100svh en los tamaños comprobados, con cabecera sobre la foto.
- Fotografía panorámica para escritorio y vertical para móvil/tablet.
- Paleta marfil, carbón oliva, piedra y oliva profundo; acento bronce.
- Cormorant Garamond y Manrope.
- Firma Maison RDL en SVG, iniciales RDL y favicon.
- Nuevos lanzamientos y Más vendidos en filas horizontales.
- Bloque de marca y footer con contraste.
- Menú móvil y vistas rápidas mediante controles HTML nativos.

## Alcance

Es una primera propuesta del inicio y la identidad, no las cinco vistas terminadas. Los artículos y precios son ejemplos. La búsqueda tiene sugerencias de muestra y no filtra un catálogo; no hay cuentas, compras, cobros ni persistencia.

Las vistas rápidas son parte de esta presentación visual; no sustituyen la página de producto ni el carrito completo exigidos en la entrega final. No se considera T02 finalizada hasta la revisión de Roger y la integración coordinada en el repositorio del equipo.

## Evidencias y recursos

- [Inicio de escritorio](preview/desktop.png)
- [Inicio de móvil](preview/mobile.png)
- [Inicio completo](preview/inicio-completo.png)
- [Lámina del logo](preview/identidad.png)
- [Recursos, prompts e investigación 2026](docs/RECURSOS-Y-BRANDING.md)
- [Verificación](docs/VERIFICACION.md)

Las imágenes de campaña y catálogo fueron generadas con image_gen integrado y guardadas en assets/images/. Sus prompts y rutas de los WebP incluidos están documentados; los originales de generación no se incluyen. Los logos son vectores construidos desde fuentes SIL OFL; sus licencias se incluyen.
