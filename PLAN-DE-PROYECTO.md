# Maison RDL — Plan de trabajo unificado

Fecha: 23 de octubre de 2026.
Equipo de implementación: Roger, Daniel y Lydia. Revisión y aprobación manual: Gaby.
Estado actualizado: PR #1–#12 integradas; revisión visual y preparación de entrega en codex/imagenes-revision-visual, pendiente de Gaby. Evidencia y pendientes reales: docs/verificacion.md.

Este documento sustituye al plan de trabajo anterior como referencia vigente. Integra el enunciado, el plan T00–T08 de Daniel, la revisión comparativa y las decisiones de Roger. La comparación anterior se conserva como antecedente, no como instrucciones de ejecución.

## 1. Objetivo y acuerdos

Construir un prototipo de tienda online de ropa de lujo para Maison RDL, una marca del proyecto con sede en Francia. RDL representa a Roger, Daniel y Lydia.

Acuerdos confirmados:
- Nombre: Maison RDL. Sustituye al nombre provisional anterior.
- Equipo de tres personas.
- Roger dirige y realiza el diseño de TODAS las páginas y la optimización.
- Stack de la tienda: HTML semántico y Tailwind CSS. Sin JavaScript de aplicación, React, otros frameworks, backend, base de datos ni pagos reales.
- Cinco archivos HTML obligatorios, enlazados entre sí.
- Móvil, tablet y escritorio en las cinco vistas.
- Trabajo mediante ramas, commits y PR; nada de desarrollo directo en main.
- URL pública, PageSpeed mínimo 80 y captura dentro del repositorio. Objetivo interno: superar 90.
- La ejecución del proyecto vendrá después de esta organización. Este paquete no publica, cambia permisos ni envía mensajes al equipo.

El reparto de este plan está organizado por petición de Roger; no supone que Daniel o Lydia hayan sido contactados desde este chat.

Enunciado:
https://learn.4geeks.com/es/main-cohort/spain-aie-pt-5/syllabus/command-line-git-and-github-v3/project/first-collaborative-project-tailwind-css?moduleId=2

Repositorio de entrega existente:
https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D

## 2. Reparto definitivo del plan

| Persona | Responsabilidad principal | Entregables |
| --- | --- | --- |
| Roger | Diseño e implementación visual de las cinco páginas; optimización | Identidad visual, composiciones, navbar/footer, tarjetas, botones y campos; Tailwind y responsive; imágenes y CSS optimizados; correcciones de rendimiento y conformidad visual final |
| Daniel | Estructura y contenido de inicio, catálogo y producto; SEO y Schema.org | HTML completo, inventario común, imágenes y procedencia, títulos y metadatos, Organization y Product; preparación técnica del repositorio y documentación de ejecución |
| Lydia | Estructura y contenido de carrito y checkout; QA y entrega documental | Tres productos e importes coherentes, tres bloques de formulario, navegación; pruebas de las cinco páginas, incidencias, evidencias y README con aportaciones de todos |

Daniel tiene tres vistas principalmente de contenido. Lydia tiene dos con más detalle de formularios/importes y asume las pruebas generales. Roger trabaja sobre las cinco vistas; por eso Daniel y Lydia se encargan también de SEO, documentación y verificación.

Cada persona prueba y corrige su propio trabajo. Lydia coordina las pruebas, pero no absorbe las correcciones de los demás. Roger no debe rehacer contenido incompleto ni asumir toda la documentación.

## 3. Dirección de diseño y supervisión de Roger

Roger ha aportado referencias de moda y branding. Ha aceptado la portada renderizada como buena base. La [guía visual v0.1](docs/diseno.md) fija esa dirección de trabajo: lujo editorial cálido, marfil/piedra/oliva, Cormorant Garamond y Manrope, logo SVG y hero de primera pantalla completa con versiones móvil/escritorio. Los [tokens](src/styles/tokens.css) concretan los valores. Esto no acredita aprobación final de las cinco vistas ni integración de T02.

Roger integra y mantiene la base visual ANTES de extender las estructuras a todas las páginas:
- Paleta, tipografías y tratamiento del nombre Maison RDL.
- Anchuras, espaciado, escala de títulos y composición.
- Navbar, footer y navegación móvil sin JavaScript.
- Tarjetas, botones, campos, enlaces y foco visible.
- Criterios de fotografía y adaptación a móvil, tablet y escritorio.

La guía y tokens actuales son la base común. Los estilos del plan anterior de Daniel no los sustituyen. La identidad es una decisión del equipo, no una exigencia del instructor; personalizar Tailwind está permitido dentro de esa base.

Daniel y Lydia usan la base de Roger. Cualquier PR con impacto visual requiere su revisión antes de integrarse. Las PR del propio Roger las revisa Daniel o Lydia; nadie aprueba su propio trabajo.

Supervisión no implica editar simultáneamente: Roger puede definir la composición de una página y trabajar en el diseño de otra ya integrada mientras sus compañeros completan contenido.

## 4. Cinco vistas y criterios de aceptación

### Inicio — index.html

Estructura/contenido: Daniel. Diseño: Roger.
- Navbar con logo, búsqueda y menú de cuenta.
- Hero de campaña con acceso al catálogo.
- Dos listados horizontales: Nuevos lanzamientos y Más vendidos.
- Productos con imagen, nombre, precio y enlace a la ficha de demostración.
- Footer completo.
- Organization mediante microdata, incorporada en T09.

### Catálogo — catalogo.html

Estructura/contenido: Daniel. Diseño: Roger.
- Navbar y footer.
- Filtros HTML por categoría y talla, identificados como demostración estática.
- Veinte productos como objetivo interno para cubrir la referencia 4×5 del enunciado.
- Calzado, camisas, pantalones y accesorios representados.
- Rejilla adaptable: cuatro columnas/cinco filas en escritorio; menos columnas y más filas en pantallas menores.
- Enlaces a la ficha de producto. Una ficha demostrativa es suficiente para el alcance de cinco vistas; no prometer que cada tarjeta abre un detalle distinto si no está implementado.

### Producto — producto.html

Estructura/contenido: Daniel. Diseño: Roger.
- Imagen y datos en dos columnas en escritorio; composición apilada en móvil.
- Nombre, referencia, talla, precio, cantidad y enlace/botón de navegación Añadir al carrito.
- Descripción con materiales y usos recomendados.
- Navbar y footer.
- Product y oferta mediante microdata en T09, coherentes con el contenido visible.

### Carrito — carrito.html

Estructura/contenido: Lydia. Diseño: Roger.
- Página completa, no panel lateral.
- Tres productos de ejemplo tomados del inventario común.
- Miniatura, nombre, precio unitario, cantidad y total por línea.
- Subtotal, impuestos y total coherentes y sin doble contabilización.
- Comprar enlaza al checkout.
- Navbar y footer.
- Datos estáticos: los controles no recalculan importes ni guardan productos.

El ejercicio no impone un porcentaje fiscal. Lydia documenta un supuesto de simulación en el inventario; no se presenta como asesoramiento ni como implementación fiscal real.

### Checkout — checkout.html

Estructura/contenido: Lydia. Diseño: Roger.
- Tres bloques numerados visibles en una página: datos personales, dirección de entrega y tarjeta.
- Formulario semántico con fieldset/legend, labels, tipos y restricciones HTML apropiadas.
- Enlaces de ancla opcionales para recorrer los bloques. No se afirma que validen campos ni cambien automáticamente un indicador activo.
- Nota clara de demostración, sin datos reales ni procesamiento de pago.
- El botón final de pago queda deshabilitado en este prototipo. No hay envío a un servidor ni parámetros personales en la URL.
- No se promete validación al pulsar enlaces; las restricciones nativas se documentan y se comprueban con datos ficticios en QA. Habilitar un envío o confirmación real requeriría una decisión posterior fuera de este alcance.
- Navbar y footer.

## 5. Comportamientos compartidos

Navegación principal: inicio → catálogo → producto → carrito → checkout. Debe ser posible volver al inicio y al catálogo.

Navbar y footer aparecen en las cinco páginas. Footer con:
- Categorías: calzado, camisas, pantalones y accesorios.
- Legal: términos, privacidad y sobre la marca.
- Contacto.

Los enlaces tienen destinos con contenido: secciones identificadas o HTML auxiliares si se acuerda. No dejar enlaces vacíos como si funcionasen.

La búsqueda, filtros, cuenta y selectores son controles HTML de prototipo. No hay búsqueda dinámica, autenticación, persistencia del carrito ni actualización automática de totales. Daniel y Lydia explican el alcance en README y en los puntos de la interfaz donde haga falta para entender el recorrido.

HTML puro no incluye automáticamente otros archivos HTML: los fragmentos comunes son referencias que se copian a las cinco páginas. Roger coordina y actualiza las cinco copias en la misma PR cuando cambia un elemento compartido.

## 6. Entorno, Tailwind y estructura

Cada persona usa su propio entorno local o Codespace. Los tres deben apuntar al mismo repositorio de entrega. Codespaces es opcional.

Método previsto para la entrega: CSS estático generado con Tailwind CLI oficial y enlazado desde las cinco páginas. Tailwind CLI es una herramienta de desarrollo; el sitio servido sigue siendo HTML y CSS, sin lógica JavaScript de aplicación. Daniel y Roger documentan en T01 la versión y el comando reproducible. Priorizar la CLI independiente si permite evitar un gestor de paquetes; no añadir frameworks.

El CDN de la plantilla puede servir para una prueba inicial, pero no será el mecanismo final de este plan. No cargar a la vez el CDN y el CSS generado en la entrega. Generar CSS no significa introducir React. No se prohíben configuración ni herramientas propias de Tailwind.

Estructura prevista DENTRO del repositorio cuando empiece la implementación:

~~~
index.html
catalogo.html
producto.html
carrito.html
checkout.html
assets/
  css/styles.css
  images/
src/
  styles/input.css
  styles/tokens.css
  partials/navbar.html
  partials/footer.html
AGENTS.md
CONTEXT.md
PROMPT-MAESTRO.md
PLAN-DE-PROYECTO.md
.agents/rules/
.github/PULL_REQUEST_TEMPLATE.md
memory-bank/
  README.md
  projectbrief.md
  techContext.md
  progress.md
tasks/
  T00-accesos.md ... T14-entrega.md
docs/
  inventario-productos.md
  fuentes-imagenes.md
  diseno.md
  requisitos.md
  INICIO-DE-TRABAJO.md
  verificacion.md
  evidencias/
README.md
pagespeed-result.png
~~~

El servidor Python de la plantilla o un servidor estático local sirven únicamente para ver los archivos. No se construirá un backend. Documentar el comando real del entorno; si se usa Python estándar: python3 -m http.server 8000, o python -m http.server 8000 según la instalación.

Usar rutas relativas compatibles con la subruta del repositorio si se publica en GitHub Pages. Probar enlaces e imágenes en la URL pública.

Este paquete local contiene documentos y fichas de planificación; no crea todavía esos HTML ni un proyecto ejecutable.

## 7. Inventario y acuerdos que evitan bloqueos

Daniel publica pronto una primera ficha de tres productos compartidos, antes de terminar el catálogo completo, para que Lydia pueda arrancar.

El inventario identifica nombre, referencia, categoría, tallas, precio, moneda, imagen, descripción y materiales. Lydia añade las cantidades del carrito y el supuesto de impuestos. Roger coordina el tratamiento visual y genera versiones optimizadas de imágenes.

Las imágenes del sitio serán locales, con procedencia y permiso de uso documentados. No imponer un servicio remoto de imágenes durante la implementación.

El texto usa Maison RDL de forma consistente. Idioma principal y moneda se cierran en T01; EUR y español son una propuesta, no una condición añadida por el enunciado.

## 8. Tareas, responsables, ramas y dependencias

Cada tarea tiene una ficha en tasks/ con instrucciones y criterios de cierre. Ninguna se marca terminada solo por abrir una PR.

| ID | Tarea | Responsable | Revisor | Rama | Depende de |
| --- | --- | --- | --- | --- | --- |
| T00 | Accesos y coordinación del repositorio | Daniel | Lydia | codex/coordinacion | Sin dependencia |
| T01 | Setup, documentos y método Tailwind | Daniel | Roger | codex/setup | T00 |
| T02 | Guía visual y elementos comunes | Roger | Daniel | codex/base-visual | T01 |
| T03 | Inventario y recursos | Daniel | Lydia | codex/inventario | T01; coordinar imágenes con T02 |
| T04 | Estructura de inicio | Daniel | Lydia | codex/estructura-home | T02 y primera versión T03 |
| T05 | Estructura de catálogo | Daniel | Lydia | codex/estructura-catalogo | T02 y T03 completo |
| T06 | Estructura de producto | Daniel | Lydia | codex/estructura-producto | T02 y primera versión T03 |
| T07 | Estructura de carrito | Lydia | Daniel | codex/estructura-carrito | T02 y tres productos de T03 |
| T08 | Estructura de checkout | Lydia | Daniel | codex/estructura-checkout | T02 y datos de T07 |
| T09 | SEO y Schema.org en cinco vistas | Daniel | Lydia | codex/seo-schema | Cinco estructuras y sus diseños integrados |
| T10 | QA de las cinco vistas | Lydia | Daniel; Roger para lo visual | codex/qa | T09 |
| T11 | Publicación de prueba | Daniel | Lydia | codex/publicacion | T10 sin incidencias bloqueantes |
| T12 | Optimización y PageSpeed | Roger | Daniel | codex/optimizacion | T11 y URL pública |
| T13 | Regresión final y evidencias | Lydia | Daniel | codex/evidencias | T12 publicado |
| T14 | Entrega documentada | Lydia, con aportaciones de todos | Daniel y Roger | codex/entrega | T13 |

Diseño de Roger por página, sin esperar a tener las otras cuatro:
- D01 Inicio: codex/diseno-home; depende de T04 integrado; revisa Lydia.
- D02 Catálogo: codex/diseno-catalogo; depende de T05 integrado; revisa Daniel.
- D03 Producto: codex/diseno-producto; depende de T06 integrado; revisa Daniel.
- D04 Carrito: codex/diseno-carrito; depende de T07 integrado; revisa Lydia.
- D05 Checkout: codex/diseno-checkout; depende de T08 integrado; revisa Lydia.

Todas las PR estructurales con cambios visuales relevantes pasan además por Roger. Los nombres de rama son una convención del equipo; el enunciado exige ramas por vista/funcionalidad, no un prefijo concreto.

## 9. Traspaso de archivos y trabajo simultáneo

1. Roger entrega la base visual y las composiciones de referencia.
2. Daniel o Lydia construye la estructura completa y su contenido en su rama.
3. Se revisa e integra la PR en main.
4. Roger crea la rama de diseño correspondiente desde el main actualizado.
5. El responsable de estructura no sigue editando ese archivo en una rama antigua. Coordina cualquier corrección con Roger.
6. Roger implementa el diseño, responsive y primera optimización; otro integrante revisa la PR.
7. Integrado el diseño, Daniel incorpora SEO/Schema.org en T09 y Lydia comprueba el recorrido en T10, sin cambiar la identidad visual por su cuenta.

Una persona por rama y un responsable activo por archivo. Roger puede diseñar una página mientras Daniel o Lydia construye otra. Los cambios globales que toquen las cinco páginas se coordinan como tarea transversal con los archivos reservados durante esa intervención.

Roger mantiene estilos fuente y fragmentos comunes. Regenerar styles.css cuando se añadan clases en cualquier página es un paso mecánico documentado; no implica rediseñar. El generado debe estar actualizado en cada PR y no se edita a mano. Si hay conflicto en CSS generado, resolver las fuentes y regenerar.

## 10. Git corregido: inicio y cierre de sesión

Al empezar:
1. Leer instrucciones del repositorio y comprobar git status --short --branch.
2. Si hay cambios pendientes, identificarlos y conservarlos antes de cambiar de rama o integrar cambios. No borrar, resetear ni hacer stash automáticamente.
3. Leer CONTEXT.md y la ficha de tarea. En T01 esos archivos pueden no existir aún: crearlos conforme a este plan.
4. Ejecutar git fetch origin.
5. Seleccionar la rama exacta de la tarea:
   - Si existe localmente: git switch NOMBRE.
   - Si solo existe en remoto: git switch --track origin/NOMBRE.
   - Si no existe: git switch -c NOMBRE origin/main.
6. Si existe rama remota de la tarea, comprobar su estado. Usar git merge --ff-only origin/NOMBRE para recoger cambios lineales; si diverge, coordinar la integración antes de continuar.
7. Incorporar origin/main a la rama correcta mediante una integración explícita, por ejemplo git merge --no-edit origin/main. Revisar y resolver conflictos sin sobrescribir el trabajo ajeno.

No ejecutar git pull origin main antes de saber qué rama está activa. Ese comando integra en la rama actual. git status devuelve éxito aunque haya cambios y no actúa como barrera automática.

Al terminar:
1. Revisar diff, archivos ajenos y recursos añadidos.
2. Ejecutar las comprobaciones relevantes; generar CSS si cambian clases o fuentes.
3. Actualizar solo la ficha propia con progreso, decisiones y evidencia.
4. Añadir archivos explícitos y revisar git diff --cached. Evitar git add -A indiscriminado.
5. Hacer commits pequeños y descriptivos con autoría real.
6. Subir la rama; abrir PR si cumple los criterios de la tarea.
7. Incorporar los cambios recientes de main antes de presentar/integrar la PR. Si hubo conflictos, repetir las comprobaciones afectadas.
8. Otra persona revisa antes de integrar. Si cambia el diseño, Roger revisa; si la PR es de Roger, revisa Daniel o Lydia.

No force-push ni desarrollo directo en main. No reescribir el historial publicado como rutina. Las incidencias de otras tareas se registran y se coordinan; las tareas transversales sí pueden modificar archivos de varias vistas dentro del alcance declarado.

## 11. Memoria compartida y prompts para asistentes

AGENTS.md fija el orden de lectura, límites, Git, verificación y mantenimiento. CONTEXT.md contiene acuerdos estables. Las reglas en .agents/rules separan alcance e identidad; memory-bank enlaza objetivos, técnica y progreso. La [adaptación de TrackFlow](docs/REFERENCIA-TRACKFLOW.md) explica el origen organizativo sin trasladar su stack.

Daniel coordina contexto y memoria global mediante PR al cambiar acuerdos o integrar fases. Cada integrante actualiza su ficha; no se pide a los tres reescribir un resumen global por sesión. Seguir [el procedimiento de memoria](memory-bank/README.md).

Cada ficha contiene: responsable, revisor, rama, archivos, dependencias, estado, decisiones, pendiente, comprobaciones, evidencia y PR. Cambiar responsable o estado de reserva del archivo debe quedar visible para el equipo.

El prompt maestro está en PROMPT-MAESTRO.md. Se adapta a tarea, rama y persona antes de usarlo. No autoriza a ejecutar ahora las tareas ni a publicar, invitar personas o enviar mensajes desde este chat.

El índice de fichas está en tasks/README.md. Los estados iniciales son Pendiente; no se inventan pruebas, capturas, aprobaciones ni resultados.

## 12. QA, accesibilidad y rendimiento

Lydia coordina las pruebas; cada autor corrige su parte.

Comprobar las cinco páginas:
- A 375, 768 y 1280 px como referencias y también en anchuras intermedias.
- Sin scroll horizontal de la página. Los listados horizontales internos del inicio sí pueden desplazarse.
- Con teclado, foco visible, orden lógico, etiquetas de formulario y estados de controles.
- Enlaces del recorrido, imágenes, destinos del footer y coherencia de navbar/footer.
- HTML válido, sin identificadores duplicados y con jerarquía razonable de encabezados.
- Contenido indexable, idioma, título y descripción propios por página.
- Schema.org coherente con el contenido visible. Se adopta microdata para mantener el marcado en HTML.
- Totales estáticos y supuesto de impuestos documentados.
- Limitaciones del prototipo expresadas sin prometer operaciones inexistentes.

Schema Markup Validator comprueba Schema.org; Rich Results Test comprueba funciones compatibles de Google. Una advertencia de resultados enriquecidos no equivale automáticamente a incumplir el ejercicio. No inventar reseñas ni datos para eliminar avisos. JSON-LD estático también sería un formato de datos válido, pero no se mezcla con microdata duplicando las mismas entidades sin motivo.

Roger optimiza:
- Imágenes al tamaño adecuado y formato eficiente, con width/height y alternativas responsive cuando convenga.
- Carga diferida para imágenes fuera de la primera pantalla; no aplicarla indiscriminadamente al hero o imagen principal.
- CSS de Tailwind generado y minificado; sin CDN de compilación en la entrega.
- Recursos, tipografía y prioridades según problemas medidos.
- Responsive y estabilidad visual.

PageSpeed se mide sobre la URL pública actualizada tras integrar las correcciones. Lydia puede repetir y documentar las mediciones; Roger dirige las decisiones de optimización.

Mínimo del enunciado: 80. Objetivo interno: más de 90. Medir móvil y escritorio como control interno y registrar qué página se midió. El enunciado leído no exige explícitamente una puntuación por cada una de las cinco páginas ni fija un modo; no atribuir esas condiciones adicionales al instructor.

## 13. Publicación y entrega

GitHub Pages desde main es la propuesta inicial por tratarse de un sitio estático; confirmar disponibilidad y acceso en T00. Si no es viable, documentar otro alojamiento estático sin cambiar el stack ni contratar servicios por defecto.

No hace falta ser miembro de la organización en todos los casos: comprobar permisos efectivos de los tres; pueden existir colaboradores externos. Si faltan permisos, coordinar con quien administre el repositorio. No cambiar visibilidad ni ampliar acceso de forma automática.

En T11 Daniel prepara la publicación y el equipo verifica la URL. Es una tarea futura, no una publicación realizada por este documento. Puede configurarse antes si el equipo lo necesita; se exige que funcione para PageSpeed y para la entrega.

Antes de entregar:
- Cinco HTML, estilos y recursos presentes y enlazados.
- Versión final integrada en main con PR y commits reales de los tres.
- URL pública funcionando con esa versión.
- PageSpeed al menos 80 y captura real pagespeed-result.png en el repositorio.
- docs/verificacion.md con fecha, URL, página, modo, puntuaciones y enlaces a evidencias.
- README en español: Maison RDL, equipo y reparto, stack, ejecución, generación de CSS, cinco vistas, URL pública, alcance estático y resultados.
- Entrega por el canal y fecha que indique el instructor.

No afirmar terminado un criterio sin evidencia. No retrasar la evaluación del rendimiento hasta el último momento: Roger revisa recursos desde la base y realiza la medición pública formal en T12.

## 14. Matriz final de aceptación

Las 17 casillas de la plataforma son cinco de vistas, cinco de Git y siete de evaluación. La [matriz detallada](docs/requisitos.md) conserva sus IDs V01–V05, G01–G05 y E01–E07, responsables, tareas, evidencias y diferencia entre requisitos oficiales y decisiones internas. El listado siguiente es un resumen de control con entrega adicional; no supone nuevas casillas del campus.

| Estado | Criterio | Responsable principal | Evidencia |
| --- | --- | --- | --- |
| Pendiente | Home: navbar, hero, novedades, más vendidos, footer | Daniel + Roger | index.html y capturas |
| Pendiente | Catálogo: filtros y rejilla | Daniel + Roger | catalogo.html y capturas |
| Pendiente | Producto: dos columnas, datos completos y descripción | Daniel + Roger | producto.html y capturas |
| Pendiente | Carrito completo, tres productos y totalización | Lydia + Roger | carrito.html e importes revisados |
| Pendiente | Checkout en tres bloques | Lydia + Roger | checkout.html y controles revisados |
| Pendiente | Ramas por vista/funcionalidad | Los tres | Historial Git |
| Pendiente | PR por rama con descripción antes de integrar | Los tres | Enlaces a PR |
| Pendiente | Incorporar main antes de presentar PR | Cada autor | Historial y resolución de conflictos |
| Pendiente | Resolver conflictos en equipo sin sobrescrituras indebidas | Los tres | PR e historial |
| Pendiente | Commits frecuentes, claros y por cambio lógico | Los tres | Historial con autoría real |
| Pendiente | HTML semántico | Daniel y Lydia | Validación de cinco vistas |
| Pendiente | Tailwind coherente y breakpoints | Roger | CSS/clases y capturas |
| Pendiente | Layout, componentes y contenido exigidos | Roger; contenido Daniel/Lydia | Comparación de las cinco vistas |
| Pendiente | Responsive usable sin desbordamiento de página | Roger; pruebas Lydia | Pruebas en tres tamaños e intermedios |
| Pendiente | Schema.org donde corresponda | Daniel | Organization y Product validados |
| Pendiente | Flujo Git sin trabajo prolongado directo en main | Los tres | PR e historial |
| Pendiente | PageSpeed mínimo 80 en URL pública | Roger; evidencia Lydia | Informe y pagespeed-result.png |
| Pendiente | Al menos cinco HTML enlazados y estilos compartidos | Los tres | Archivos y recorrido |
| Pendiente | Footer completo con destinos útiles | Roger + Daniel | Categorías, legal, marca y contacto |
| Pendiente | SEO: semántica, contenido indexable y buenas prácticas | Daniel; revisión conjunta | Metadatos, encabezados, alt y contenido |
| Pendiente | Repositorio entregado y captura incluida | Lydia + todos | README, captura y confirmación de entrega |

## 15. Datos pendientes y siguiente paso

Pendientes: fecha límite, disponibilidad, usuarios GitHub/accesos, idioma/moneda, inventario definitivo y disponibilidad del alojamiento propuesto. La base visual ya está definida en la guía v0.1; falta integrarla y revisar cada página. No volver a debatir el nombre ni quién dirige diseño: ya están fijados.

Orden de arranque:
1. Daniel comprueba repositorio y acceso de los tres.
2. Daniel prepara T01 y Roger revisa el método de estilos.
3. Roger integra la base visual documentada; Daniel prepara el inventario.
4. Daniel y Lydia construyen estructura/contenido y entregan páginas por PR.
5. Roger diseña las cinco vistas de forma escalonada.
6. SEO → QA → publicación → optimización → regresión/evidencias → entrega.

## 16. Referencias técnicas de las correcciones

- [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli): generación de CSS estático; CLI independiente disponible.
- [Play CDN](https://tailwindcss.com/docs/installation/play-cdn): pensado para desarrollo.
- [git pull](https://git-scm.com/docs/git-pull): integra cambios en la rama activa.
- [Optimización del contenido principal](https://web.dev/articles/optimize-lcp/): tratamiento de la imagen principal y carga diferida.
- [Formatos de datos estructurados](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data): microdata y JSON-LD.
- [Validadores de datos estructurados](https://developers.google.com/search/docs/appearance/structured-data): diferencia entre validación general y resultados enriquecidos.
- [Colaboradores externos en GitHub](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization): acceso a repositorios sin pertenencia obligatoria a la organización.
