# Verificación de la primera propuesta

Fecha: 23 de octubre de 2026.
Entorno: Chrome conectado, mediante CUA y su API Playwright documentada; capturas mediante CDP en el mismo navegador.
URL: http://127.0.0.1:8047/
Flujo: inicio → Explorar la colección → novedades → vista rápida → cierre; menú móvil → novedades; apertura/cierre de búsqueda de muestra.

## Comprobaciones realizadas

| Comprobación | Resultado |
| --- | --- |
| Construcción Tailwind CLI 4.3.3 | Correcta |
| Identidad de página y contenido visible | Correctos |
| JavaScript de aplicación | Cero scripts en las dos páginas |
| Hero móvil 390×844 | 844 px de altura, fuente vertical cargada, sin desbordamiento horizontal |
| Hero móvil 375×812 | 812 px de altura, sin desbordamiento horizontal |
| Hero móvil compacto 375×667 | Altura equivalente a la pantalla con redondeo subpíxel; CTA visible antes del pie y sin desbordamiento horizontal |
| Hero tablet 768×1024 | 1024 px de altura, fuente vertical cargada, sin desbordamiento horizontal |
| Escritorio 1440×900 | Hero panorámico y paleta contrastada revisados visualmente; sin desbordamiento horizontal |
| Menú móvil | Apertura/cierre y navegación a novedades comprobados |
| Productos | Vista rápida de camisa abierta y cerrada con controles HTML |
| Búsqueda de muestra | Apertura, introducción de texto y cierre comprobados; no se afirma búsqueda dinámica |
| Imágenes en el contenido visible | Cargadas |
| Logos de la lámina de identidad | Variantes cargadas y sin desbordamiento en escritorio |
| Consola del inicio | Sin errores ni avisos relevantes capturados |
| Recursos y referencias internas de HTML | Sin archivos ausentes, IDs duplicados ni destinos inexistentes detectados |

Las capturas muestran el render real. Se usó captureBeyondViewport para evitar el escalado de la ventana física al comprobar los tamaños emulados. Se restablecen las dimensiones temporales al terminar.

## Lectura visual frente a las referencias

- Se mantienen serif editorial, fotografía cálida y espacio generoso.
- La portada dividida inicial se sustituyó por foto de pantalla completa por petición de Roger.
- Las secciones alternan marfil, oliva y piedra; el footer usa carbón oliva.
- Las fotografías son propias de la propuesta, generadas, y los productos de catálogo mantienen un encuadre común.
- La composición del logo y la paleta son propuestas para revisión; las tendencias 2026 se documentan como referencias, no como reglas.

## Límites de esta comprobación

No es una auditoría de accesibilidad completa ni una validación del proyecto entero. No se ha medido PageSpeed sobre una URL pública, no se han implementado catálogo/producto/carrito/checkout como páginas de entrega ni se ha completado la matriz académica de las cinco vistas. La versión futura necesita esas tareas y su historial de PR.
