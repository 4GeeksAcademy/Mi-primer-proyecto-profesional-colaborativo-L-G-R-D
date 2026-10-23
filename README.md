# Maison RDL

Prototipo académico de una marca de ropa ficticia con sede en Francia. Cinco páginas estáticas en HTML y Tailwind CSS, con recursos locales. Sin JavaScript de aplicación, backend, almacenamiento ni pagos reales.

## Ejecutar en Codespaces

Desde la raíz del repositorio:

```bash
npm ci
npm run build
npm start
```

Abrir el puerto **8000** desde la pestaña Puertos. Para ver el sitio sin regenerar CSS basta con `npm start`: el CSS compilado está incluido. Node.js/npm se usan para Tailwind; Python sirve los archivos sin dependencias adicionales.

## Páginas

| Página | Contenido |
| --- | --- |
| [Inicio](index.html) | Campaña del equipo, novedades y más vendidos |
| [Catálogo](catalogo.html) | Veinte productos y filtros estáticos |
| [Producto](producto.html) | Ficha de ejemplo, materiales y uso |
| [Carrito](carrito.html) | Tres productos y total de demostración de 925,00 € |
| [Checkout](checkout.html) | Tres bloques de campos y pago deshabilitado |

Búsqueda, filtros, cuenta y carrito son demostraciones identificadas. Todas las tarjetas abren la misma ficha de ejemplo. Los campos no se envían. Imágenes y datos de productos son ficticios.

## Equipo y revisión

Roger: diseño, imágenes, componentes y optimización. Daniel: inventario, inicio, catálogo, producto y preparación técnica. Lydia: carrito, checkout y coordinación de pruebas. Gabriela (Gaby): se incorporó al equipo en la fase final para la revisión manual y aprobación de PR. La actualización visual y SEO de [PR #13](https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D/pull/13) fue aprobada por Gaby e integrada; publicación comprobada en bef45b0.

## Entrega y evaluación

[Requisitos](memory-bank/requisitos.md), [verificación actual](memory-bank/verificacion.md), [guía visual](memory-bank/diseno.md), [inventario](memory-bank/inventario-productos.md) y [procedencia de imágenes](assets/fuentes-imagenes.md).

**SEO completado:** Organization y Product/Offer validados en Schema.org con cero errores y advertencias. La publicación genera canónicas, metadatos sociales, robots y sitemap con la URL real; incluye un workflow de GitHub Pages. [Procedimiento](#publicación).

**Publicación:** [Abrir Maison RDL](https://4geeksacademy.github.io/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D/). PR #13 aprobada por Gaby e integrada; workflow de Pages correcto. **Pendiente E07:** Google PageSpeed devuelve HTTP 429; aún no se acredita ≥80 ni su captura. Ver evidencia y límites en memory-bank/verificacion.md.

## Archivos necesarios

- Cinco HTML, `assets/` y `src/`: sitio, imágenes, fuentes/licencias y entrada de Tailwind.
- `package.json`, `package-lock.json`, `.gitignore`, `.vscode/`, `.github/`: instalación reproducible y trabajo del equipo.
- `memory-bank/`, `tasks/`, `.agents/` y archivos de coordinación: requisitos, diseño, inventario, acuerdos y estados. `evidencias/` conserva las pruebas y dos capturas de referencia; `assets/` conserva la procedencia. La carpeta `docs/` se retira para evitar duplicados.
- `node_modules/` se instala localmente y no se versiona ni se entrega en el ZIP. Se retiran README de plantilla en otros idiomas, servidor Flask, ficha learn.json y foto de plantilla sin uso. No se retira el historial Git.

El CSS generado no se edita a mano: modificar `src/styles/` y ejecutar `npm run build`. Si hay conflictos, resolver las fuentes y regenerar.

## Créditos

Basado en la plantilla [html-hello de 4Geeks Academy](https://github.com/4GeeksAcademy/html-hello). Fuentes Cormorant Garamond y Manrope con licencias SIL OFL incluidas. Imágenes generadas de demostración con procedencia documentada.

## Publicación

Se incluye `.github/workflows/pages.yml`. Un administrador selecciona **Settings → Pages → Source: GitHub Actions**. Tras la revisión de Gaby e integración en main, el workflow compila, genera el sitio con la URL de Pages y lo publica. No ejecuta código de aplicación en el cliente ni publica documentación, node_modules o herramientas.

Para comprobar antes de publicar:

```bash
python tools/check_site.py
python tools/build_site.py --base-url https://TU-URL-PUBLICA/ --output dist
python tools/check_site.py dist
```

Sustituir la URL por la real, incluida su subruta. `dist` debe estar vacío o no existir; el generador no borra directorios automáticamente. No se versiona `dist/`. No ejecutar el ejemplo con una URL inventada para la entrega final. La copia de desarrollo sigue abriéndose con npm start.

## Mantener el Codespace limpio

Conservar AGENTS.md, CONTEXT.md, memoria, reglas y evidencia. Si queda la carpeta inicial duplicada mostrada en el explorador, ejecutar `python tools/clean_workspace.py` y después `python tools/clean_workspace.py --apply`: crea un respaldo verificado fuera del proyecto y retira únicamente `pquete-maison/` o `paquete-maison/`. No toca .git ni cambios ajenos. node_modules sigue ignorado y se recrea con npm ci; no se sube.

## Enlace para compartir con el instructor

https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D

Roger confirma que solo debe compartirse ese enlace. La web pública se enlaza arriba. PageSpeed permanece pendiente por la limitación externa de consultas; no se inventa su resultado.

## Medir SEO en la URL correcta

La web pública obtuvo SEO 100/100 en Lighthouse 13.5.0; [informe](evidencias/lighthouse-seo-public.json). Usar GitHub Pages para evaluar la entrega. La URL temporal de Codespaces puede requerir autenticación y no representa la indexación del sitio público. La medición de rendimiento de PageSpeed sigue pendiente por HTTP 429.
