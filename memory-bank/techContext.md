# Maison RDL — Contexto técnico

Actualizado: 23/10/2026.

## Stack y ubicación

HTML semántico y Tailwind CSS; CSS adicional permitido, sin JavaScript de aplicación ni frameworks. Tailwind CLI genera el CSS estático durante desarrollo/build. No hay backend.

Este directorio es el paquete local de organización. El [repositorio de entrega](https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-R-D) todavía debe recibir estos archivos en T01.

Estructura final prevista:
- Cinco HTML en la raíz: index.html, catalogo.html, producto.html, carrito.html, checkout.html.
- src/styles/input.css y tokens.css → assets/css/styles.css.
- src/partials: referencias de navbar/footer; sin includes automáticos.
- assets: imágenes, marca y fuentes locales con procedencia/licencias.
- docs, tasks, memory-bank y .agents/rules: documentación y coordinación.

Valores de marca: [tokens](../src/styles/tokens.css). Uso visual: [guía](../docs/diseno.md). No repetirlos aquí.

## Comandos y versiones

El repo de entrega aún no tiene un procedimiento de build validado en este paquete. T01 debe documentar versión, instalación, generación minificada de CSS y servidor local, y comprobar detección de clases en las cinco páginas. No afirmar que npm run build existe allí.

La preview independiente [maison-rdl-inicio-v1](../docs/referencia-visual/README.md) usa Tailwind y @tailwindcss/cli 4.3.3, npm ci, npm run build y un servidor estático. Es referencia disponible, no arquitectura transferida automáticamente.

Los tokens preparados usan sintaxis @theme de Tailwind 4. Si T01 necesita otra versión por el entorno, adaptar la configuración coordinadamente sin alterar colores ni tipografías.

El CSS generado sí debe incorporarse para permitir alojamiento estático directo, manteniéndolo actualizado y sin edición manual. No versionar node_modules, credenciales o archivos temporales. Si se usa npm, conservar package-lock.json.

## Verificación

Documentación: enlaces, rutas, coherencia y ausencia de estados inventados.
Código: build si procede, HTML, enlaces/recursos, teclado, vistas móvil/tablet/escritorio afectadas, overflow y contenido.
Entrega: cinco vistas, SEO/microdata, Git, URL pública y PageSpeed real según [requisitos](../docs/requisitos.md).

El servidor local no es evidencia de publicación. PageSpeed local no sustituye a la medición exigida sobre URL pública. Las rutas deben funcionar bajo la subruta real si se usa GitHub Pages.
