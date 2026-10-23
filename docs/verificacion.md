# Verificación de entrega — 23/10/2026

Rama local: `codex/imagenes-revision-visual`. Base integrada comprobada: `b5d9654`. Los cambios de esta rama no están aprobados, publicados ni integrados. Revisión manual: Gaby.

## Resultado local

- Build: `npm run build`, correcto; Tailwind CSS 4.3.3, sin dependencias de aplicación añadidas.
- Nu HTML Checker: cinco HTML enviados al validador oficial, sin mensajes. [Resultado completo](evidencias/html-validation.json).
- Chromium con Playwright externo al proyecto (Browser plugin no disponible): cinco vistas a 320, 375, 390, 768, 1024, 1280 y 1440 px. Sin desbordamiento horizontal del documento, un h1/main/header/footer por página y sin IDs duplicados.
- Cabecera fija o sticky en las cinco vistas: top 0 después de desplazar 700 px. En inicio, superpuesta sobre la foto sin franja sólida al cargar, fondo oliva profundo de marca opaco al desplazarse en navegadores con scroll-driven animations; alternativa semitransparente sin JavaScript. Anclas separadas de la cabecera.
- Búsqueda abierta/cerrada y menú móvil por encima del contenido. Recorrido real inicio → catálogo → producto → carrito → checkout en los siete tamaños; pago deshabilitado.
- Metadescripción única en las cinco páginas, idioma español, alt y dimensiones en imágenes. Organization en inicio; Product y Offer en ficha con SKU MRDL-CAM-001, nombre, imagen, descripción, material, precio 240.00 y moneda EUR coincidentes con el contenido visible.
- Contraste calculado de colores sólidos: texto principal 12.84:1, secundario/marfil 6.71:1, secundario/piedra 6.09:1, secundario del footer 8.87:1, texto sobre oliva 7.91:1; borde de controles/marfil 4.49:1. Las fotografías requieren además revisión visual y no se consideran superficies de color uniforme.
- [Comprobaciones de navegador y ratios](evidencias/evaluacion.json). Las herramientas de QA no forman parte de las dependencias del sitio.

## Matriz de evaluación

| Criterio | Evidencia y estado |
| --- | --- |
| V01 | Navbar con campo de búsqueda accesible y cuenta de demo; hero; ocho tarjetas en dos listados; footer común. Implementado y probado localmente. |
| V02 | Veinte tarjetas con imagen propia, filtros de categoría/talla y cuatro columnas en escritorio. Implementado y probado localmente. |
| V03 | Ficha con imagen/datos a dos columnas, SKU, talla, precio, cantidad, añadir, descripción, materiales y uso. Implementado y probado localmente. |
| V04 | Carrito completo, tres productos, importes por línea y resumen: 770,83 + 154,17 = 925,00 EUR. Implementado y probado localmente. |
| V05 | Tres bloques numerados: datos, dirección y tarjeta ficticia; sin envío ni pago. Implementado y probado localmente. |
| G01–G05 / E06 | GitHub confirma doce PR integradas de ramas de trabajo; autores y ramas en [evidencia](evidencias/pull-requests.json). Las PR #8 y #11 reflejan resolución de conflictos y regeneración de CSS. Esta rama aún requiere commit/PR, revisión de Gaby e integración; no se certifica ausencia absoluta de force-push a partir del historial público. |
| E01 | Cinco HTML válidos según Nu; landmarks, encabezados y etiquetas revisados. |
| E02 | Tailwind compilado y breakpoints; sin frameworks ni JavaScript de aplicación. |
| E03 | Componentes compartidos y contenido de las cinco vistas presentes. |
| E04 | Siete anchos sin overflow de página, navegación y menú probados. |
| E05 | Organization y Product/Offer incorporados y propiedades contrastadas con el DOM. Schema Markup Validator: **0 errores y 0 advertencias** en ambas páginas, con [resultado](evidencias/schema-validator.json) y capturas reales [Organization](evidencias/schema-index.png) / [Product](evidencias/schema-producto.png). No se afirma elegibilidad comercial ni aprobación de Rich Results Test. |
| E07 | **Pendiente:** PageSpeed Insights sobre la URL pública de la versión final; mínimo 80 y captura real dentro del repositorio. No se sustituye por una puntuación local. |

## Cierre pendiente

1. Gaby revisa y aprueba la PR; integrar cambios con autoría real.
2. Publicar la versión integrada en GitHub Pages o el alojamiento acordado y comprobar las cinco rutas bajo su subdirectorio.
3. Registrar aquí URL exacta, commit publicado, fecha, modo y resultado PageSpeed; guardar captura real `pagespeed-result.png` en la raíz.
4. Confirmar canal/fecha del instructor y compartir el repositorio. No se ha enviado la entrega desde esta sesión.

URL pública final: pendiente. PageSpeed: no medido. Captura de PageSpeed: pendiente. El acceso a la página privada del campus no pudo repetirse desde esta sesión; se utiliza la matriz local del enunciado previamente documentada.

## Limpieza

Retirados únicamente `README.cn.md`, `README.es.md`, `learn.json`, `server.py` (Flask) y `.vscode/rigo-baby.jpeg`, sin uso en el sitio actual. Copia recuperable fuera del repositorio. Se mantienen fuentes, lockfile, licencias, historial y documentación enlazada. `node_modules` queda ignorado y fuera del paquete de entrega. El archivo de referencia visual se conserva por trazabilidad del diseño.

Fuentes técnicas: [Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines), [Product](https://schema.org/Product), [Organization](https://schema.org/Organization), [Nu HTML Checker](https://validator.w3.org/nu/).

## SEO y publicación en la actualización única

`tools/build_site.py` prepara una carpeta pública limpia, únicamente con los cinco HTML y recursos usados. Recibe la URL real del alojamiento; añade canónicas absolutas, Open Graph y tarjeta social, robots.txt y sitemap.xml. Carrito y checkout se sirven con noindex/follow y quedan fuera del sitemap. No inventa un dominio ni publica localhost como URL final.

`.github/workflows/pages.yml` instala desde el lockfile, compila Tailwind, comprueba rutas con `tools/check_site.py`, obtiene la URL de Pages, genera el paquete y publica tras integrar en main. El administrador debe seleccionar **Settings → Pages → Source: GitHub Actions** antes de ejecutarlo. Esta sesión no cambió permisos ni habilitó Pages; la consulta pública de configuración devolvió 404. El workflow está preparado, todavía no ejecutado en GitHub.

Prueba local del paquete bajo `/tienda/`: doce comprobaciones de navegador en móvil/escritorio sin imágenes rotas, errores de carga o overflow; recorrido enlazado completo. [Resultado](evidencias/public-build.json). Los cinco HTML generados pasan Nu sin mensajes: [resultado](evidencias/public-html-validation.json). Es una prueba del paquete, no evidencia de publicación.

### Después de integrar esta única PR

1. Gaby revisa el conjunto y se integra en main.
2. Habilitar Pages con GitHub Actions y ejecutar el workflow si no se activó automáticamente; su ejecución muestra la URL real.
3. Abrir esa URL en PageSpeed Insights, confirmar mínimo 80 y guardar la captura real en `pagespeed-result.png`, registrando fecha, modo, URL y puntuación. La evidencia que aún no existe no puede incluirse por adelantado en esta actualización.

## Limpieza del paquete inicial duplicado

La captura del Codespace muestra `pquete-maison/Maison-RDL-equipo`, sin seguimiento. No existe en esta copia local ni puede eliminarse con un commit remoto. Se incluye `tools/clean_workspace.py` para retirarlo allí, con respaldo ZIP fuera del repositorio, comprobación CRC, lista cerrada de rutas y rechazo de enlaces u otros repositorios. Ambas variantes del nombre quedan ignoradas por Git. Los documentos de arranque se actualizan para que no indiquen descomprimir otra vez el paquete ni repetir tareas ya integradas.
