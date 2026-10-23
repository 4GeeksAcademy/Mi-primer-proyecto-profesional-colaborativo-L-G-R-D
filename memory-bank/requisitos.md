# Maison RDL — Requisitos y evaluación

Verificado el 23/10/2026 mediante lectura completa del [enunciado del campus](https://learn.4geeks.com/es/main-cohort/spain-aie-pt-5/syllabus/command-line-git-and-github-v3/project/first-collaborative-project-tailwind-css?moduleId=2).
Las 17 casillas son cinco vistas, cinco prácticas de Git y siete criterios de evaluación. Esta matriz resume su contenido; no sustituye al enunciado ni acredita cumplimiento.

## Fuentes y límites

- Enunciado: prototipo de tienda de ropa de una marca con sede en Francia; SEO, diseño consistente y responsive; solo HTML y Tailwind CSS.
- El texto plantea dos personas. Roger confirma que la entrega será entre Roger, Daniel y Lydia; ese es el equipo de este plan. No presentar tres como número exigido por el campus.
- Entregable: al menos cinco HTML, uno por vista, enlazados entre sí, con estilos compartidos. CSS adicional está permitido por el enunciado.
- Plantilla de partida: [html-hello](https://github.com/4GeeksAcademy/html-hello); trabajar en un repositorio propio del equipo. Ya existe el [repositorio de entrega](https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D): comprobar remotos y accesos en T00, sin crear otro por duplicado.
- Codespaces es recomendado; clonar y trabajar en local también está permitido.
- No hay puntos o porcentajes por criterio publicados en el texto leído. No inventarlos.

## Las 17 casillas

| ID | Criterio del enunciado resumido | Tareas y responsable | Evidencia que debe existir |
| --- | --- | --- | --- |
| V01 | Home: navbar, hero, novedades, más vendidos y footer compartido | T04 Daniel; D01 Roger | index.html; dos listados horizontales y navegación comprobados |
| V02 | Catálogo: filtros categoría/talla, rejilla y elementos comunes | T05 Daniel; D02 Roger | catalogo.html; 20 artículos como referencia 4×5 en escritorio; adaptación móvil |
| V03 | Producto: dos columnas, imagen/datos, descripción y elementos comunes | T06 Daniel; D03 Roger | producto.html con todos los campos del desglose inferior |
| V04 | Carrito: página completa, líneas, resumen, Comprar y elementos comunes | T07 Lydia; D04 Roger | carrito.html; tres ejemplos; precios e importes revisados |
| V05 | Checkout: datos personales, entrega, tarjeta y elementos comunes | T08 Lydia; D05 Roger | checkout.html; tres etapas representadas con campos semánticos |
| G01 | Rama por vista o funcionalidad; no desarrollar en main | Todos | Ramas y commits reales |
| G02 | PR por rama antes de integrar, con descripción | Todos | Enlaces a PR y descripción del cambio |
| G03 | Actualizar la rama con main antes de presentar PR | Cada autor | Historial de la rama; integración explícita de main |
| G04 | Resolver conflictos en equipo; no force-push ni sobrescribir sin consenso | Todos | Resoluciones revisadas si hubo conflictos; no es necesario provocarlos |
| G05 | Commits frecuentes, claros y por cambio lógico | Todos | Historial con autoría real; sin número mínimo inventado |
| E01 | HTML semántico y landmarks correctos en todas las vistas | Daniel/Lydia; QA T10 | Revisión de cinco HTML, encabezados, formularios y validación |
| E02 | Tailwind utility coherente y breakpoints; sin frameworks ajenos | Roger; setup T01 Daniel | Fuentes Tailwind, CSS generado, vistas en tres tamaños |
| E03 | Layout claro, navbar/footer reutilizados, contenido exigido por vista | Roger; contenido Daniel/Lydia | Comparación con desglose por vista y capturas |
| E04 | Cinco vistas usables; sin layout roto ni scroll horizontal de página en móvil | Roger; T10/T13 Lydia | Pruebas móvil/tablet/escritorio y anchuras intermedias |
| E05 | Schema.org donde corresponda, por ejemplo Organization y Product | T09 Daniel | Marcado acorde al contenido y resultados del validador |
| E06 | Flujo Git: ramas, PR para partes importantes, commits descriptivos | Todos | Historial y PR; complementa G01–G05 |
| E07 | PageSpeed Insights en URL pública: mínimo 80, idealmente más de 90 | T12 Roger; evidencia T13 Lydia | Informe de URL pública y captura real dentro del repo |

Estado contrastado a 23/10/2026: implementación y comprobaciones locales documentadas en [verificación](verificacion.md). Las PR previas están integradas; esta revisión aún requiere aprobación/integración. E07, URL pública final y entrega al instructor siguen pendientes. No se marca el proyecto entregado por una preview local.

## Desglose que no debe perderse al diseñar

### V01 — Inicio

- Navbar con logo, barra de búsqueda y menú de cuenta de usuario. Un icono sin acceso a un campo no cubre la búsqueda.
- Hero con campaña o productos destacados.
- Dos listados horizontales de tarjetas: Nuevos lanzamientos y Más vendidos.
- Footer: calzado, camisas, pantalones, accesorios; términos, privacidad, sobre la marca y contacto.
- Navbar y footer se repiten en las otras cuatro vistas.

### V02 — Catálogo

- Filtros por categoría y talla antes de los productos.
- Rejilla 4×5 / 20 productos como referencia del enunciado. El equipo adopta 20 para evitar dudas; las cuatro columnas no se fuerzan en móvil.
- Navbar y footer comunes.

### V03 — Producto

- En escritorio: imagen aproximadamente en la mitad izquierda; información en la derecha.
- Nombre, referencia, talla, precio, selector de cantidad y acción Añadir al carrito.
- Debajo: descripción detallada, materiales y uso recomendado.
- Navbar y footer comunes.

### V04 — Carrito

- Vista completa, no solo panel lateral.
- Miniatura, precio unitario, cantidad y total por línea.
- Subtotal, impuestos, total y Comprar.
- Tres productos de ejemplo según la referencia del enunciado, adoptados en nuestro plan.
- Navbar y footer comunes.

### V05 — Checkout

- Tres etapas: datos personales, dirección de entrega y pago con tarjeta.
- El equipo las representa como tres bloques numerados y visibles en una sola página, con anclas opcionales: adaptación al prototipo sin JavaScript.
- Navbar y footer comunes.

## Decisiones del equipo y calidad interna

No atribuir estas decisiones adicionales al instructor:

| Decisión | Aplicación |
| --- | --- |
| Maison RDL; lujo editorial cálido | Marca ficticia, guía visual y recursos propios |
| Roger diseña cinco páginas y optimiza | Revisión visual centralizada; PR de Roger revisada por otro |
| Cinco nombres de archivo en español | index, catalogo, producto, carrito, checkout |
| Sin JavaScript de aplicación ni backend | Enlaces entre vistas; controles estáticos identificados, sin persistencia |
| Checkout de demostración | Sin envío ni pagos; botón final deshabilitado; pruebas con datos ficticios |
| Tailwind compilado en CSS estático | Método reproducible T01; sin Play CDN en la entrega |
| Microdata para Schema.org | Organization y Product sin inventar reseñas o afirmaciones |
| Hero de inicio a pantalla completa | Foto panorámica/vertical; no obligatorio en páginas internas |
| Recursos locales y fuentes con licencia | Procedencia, formatos, tamaños y recortes documentados |
| QA a 375, 768 y 1280/1440 px más intermedios | Teclado, foco, labels, enlaces, imágenes y overflow |
| Medir móvil y escritorio | Control interno; el enunciado no fija modo ni exige puntuar todas las URLs |

Búsqueda, filtros y carrito se representan dentro del alcance HTML/CSS; no se promete procesamiento dinámico. Conservar el recorrido enlazado: inicio → catálogo → producto → carrito → checkout. Si el instructor concreta otro comportamiento, registrar la aclaración antes de ampliar tecnologías.

## Entrega y cierre

- [ ] Cinco HTML completos enlazados, estilos y recursos compartidos.
- [ ] 17 criterios contrastados con evidencia, no solo con declaraciones.
- [ ] Ramas/PR/commits reales de los tres e integración final revisada.
- [ ] URL pública correspondiente a la versión final.
- [ ] PageSpeed ≥80; objetivo >90, también indicado como ideal por el enunciado.
- [ ] Captura real de PageSpeed incluida en el repo; nombre de equipo: pagespeed-result.png.
- [ ] memory-bank/verificacion.md registra fecha, URL exacta, modo, resultado y evidencia.
- [ ] README final con ejecución, build, URL, alcance, equipo y aportaciones.
- [ ] Repositorio compartido por el canal y fecha del instructor; registrar la entrega solo cuando ocurra.

La captura es obligatoria; el nombre concreto del archivo es un ejemplo del enunciado adoptado por el equipo. La fecha y el canal específico siguen pendientes. Las fichas de tareas contienen los estados de trabajo; esta matriz evita duplicarlos.

## Evidencia final seleccionada por el equipo

**Evidencia final de rendimiento elegida por Roger:** Chrome DevTools Lighthouse en Codespaces, **100 en escritorio y 97 en móvil**. Capturas originales incluidas; no se presentan como informes de la web de PageSpeed Insights. Ese servicio devolvió HTTP 429. La equivalencia con el requisito específico del enunciado corresponde a la evaluación del instructor; no se atribuye una aceptación que no se ha recibido. Véanse las dos capturas originales en README. Se conserva el texto del criterio E07 del enunciado, sin reescribirlo como si exigiera otra herramienta ni atribuir una aprobación docente inexistente.
