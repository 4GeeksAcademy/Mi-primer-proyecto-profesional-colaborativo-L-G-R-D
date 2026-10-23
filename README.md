# Maison RDL

Prototipo estático de tienda de ropa de lujo de una marca ficticia con sede en Francia. Primer proyecto profesional colaborativo de Roger, Daniel y Lydia: cinco páginas HTML enlazadas con estilos compartidos generados con Tailwind CSS.

Antes de trabajar, leer [AGENTS.md](AGENTS.md), [CONTEXT.md](CONTEXT.md), [requisitos](docs/requisitos.md) y la [ficha de la tarea](tasks/README.md).

## Estado

Las cinco páginas son esqueletos de [T01](tasks/T01-setup.md): estructura semántica, navegación entre vistas y CSS compartido. No son las vistas terminadas; su contenido y diseño llegan con T02–T08 y D01–D05.

| Página | Vista |
| --- | --- |
| [index.html](index.html) | Inicio |
| [catalogo.html](catalogo.html) | Catálogo |
| [producto.html](producto.html) | Producto |
| [carrito.html](carrito.html) | Carrito |
| [checkout.html](checkout.html) | Checkout |

## Requisitos

- Node.js y npm, solo para generar el CSS. Comprobado con Node 24.21.0 y npm 11.19.0.
- Python 3 para el servidor local.

Tailwind CSS 4.3.3 y su CLI oficial (`@tailwindcss/cli` 4.3.3) son dependencias de desarrollo con versión fija en [package.json](package.json) y [package-lock.json](package-lock.json). El sitio publicado no usa JavaScript ni el CDN de Tailwind: solo HTML y el CSS generado.

## Instalación

```bash
npm ci
```

Usar `npm ci` para instalar exactamente las versiones del lockfile. No versionar `node_modules/`.

## Generar el CSS

```bash
npm run build
```

Lee [src/styles/input.css](src/styles/input.css), que importa Tailwind y los [tokens de marca](src/styles/tokens.css), y escribe `assets/css/styles.css` minificado.

Durante el desarrollo se puede regenerar automáticamente al guardar:

```bash
npm run watch
```

- `assets/css/styles.css` es generado: no editarlo a mano. Regenerarlo y añadirlo al commit cuando cambien clases, fuentes o tokens, porque el alojamiento estático lo sirve directamente.
- Tailwind escanea los cinco HTML de la raíz, `src/partials/` y [docs/componentes.html](docs/componentes.html), declarados con `@source` en input.css. Si se crea otra página HTML, añadir su `@source`; el resto de `docs/` y la referencia visual quedan fuera.
- Si hay un conflicto en el CSS generado, resolver los archivos fuente y volver a ejecutar `npm run build`.

## Servidor local

Desde la raíz del repositorio:

```bash
python3 -m http.server 8000
```

Abrir http://localhost:8000/ (en Codespaces, desde la pestaña de puertos). No requiere instalar nada más.

Alternativa de la plantilla html-hello, con Flask en el puerto 3000:

```bash
pip3 install flask && python3 server.py
```

El servidor local sirve para desarrollo; no sustituye la URL pública ni la medición de PageSpeed exigidas en la entrega.

## Estructura

```text
index.html, catalogo.html, producto.html, carrito.html, checkout.html
assets/css/styles.css      CSS generado por Tailwind (no editar)
src/styles/input.css       Entrada de Tailwind y fuentes escaneadas
src/styles/tokens.css      Colores y tipografías de marca (Roger)
docs/                      Requisitos, guía visual y referencia visual
tasks/                     Fichas de tareas
memory-bank/               Memoria compartida del proyecto
```

`docs/referencia-visual` es una propuesta de la portada con su propio build; no forma parte del sitio entregado.

## Base visual T02

La base compartida está preparada localmente para revisión, no integrada ni verificada. Ver [muestrario de componentes](docs/componentes.html), [guía de uso y esquemas](docs/diseno.md) y [procedencia/licencias](assets/PROCEDENCIA.md). Inicio integra el hero de referencia; las páginas internas conservan sus secciones de contenido pendientes. El muestrario no sustituye esas páginas ni define el inventario.

Los [fragmentos de navbar](src/partials/navbar.html) y [footer](src/partials/footer.html) son referencias con rutas para la raíz, no includes: sus copias se mantienen coordinadas en los cinco HTML. El muestrario adapta esas rutas con `../`. Menú, búsqueda y cuenta usan HTML nativo; la búsqueda no procesa resultados y las categorías llevan al catálogo sin filtrarlo.

## Alcance

Solo HTML y Tailwind CSS, con CSS adicional si hace falta. Sin JavaScript de aplicación, frameworks, backend, persistencia ni pagos reales. Búsqueda, filtros, cuenta y carrito son demostraciones estáticas; el checkout no envía datos.

## Créditos de la plantilla

Proyecto creado a partir de la plantilla [html-hello](https://github.com/4GeeksAcademy/html-hello) de [4Geeks Academy](https://4geeksacademy.com/), realizada por [Alejandro Sanchez](https://twitter.com/alesanchezr) y [otros contribuyentes](https://github.com/4GeeksAcademy/html-hello/graphs/contributors).
