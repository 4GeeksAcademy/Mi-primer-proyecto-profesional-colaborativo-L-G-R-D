> Estado vigente a 23/10/2026: Implementación integrada hasta PR #13; reorganización documental en PR #14 pendiente de revisión. Los apartados de preparación y sesiones anteriores se conservan como historial. Fuente actual: [progress](../memory-bank/progress.md) y [verificación](../memory-bank/verificacion.md).

# T02 — Guía visual y elementos compartidos

Proyecto: Maison RDL.
Estado: Implementación integrada hasta PR #13; reorganización documental en PR #14 pendiente de revisión.
Responsable: Roger.
Revisión de la base: Lydia, aprobación registrada en la PR #4.
Revisor del cierre: Gaby; revisión pendiente, sin aprobación atribuida.
Rama de la base integrada: codex/base-visual.
Rama de esta corrección: codex/cierre-t02.
Depende de: T01.
Archivos: memory-bank/diseno.md, docs/componentes.html, README.md, src/styles/input.css, src/partials/navbar.html, src/partials/footer.html, cinco esqueletos, assets/css/styles.css y recursos de assets/ documentados en assets/PROCEDENCIA.md. src/styles/tokens.css se conserva sin cambios.
Responsable activo del cierre: Roger; docs/componentes.html, memory-bank/diseno.md (solo estado), README.md y esta ficha. Sin cambios de diseño, inventario ni fichas de Daniel o Lydia.
PR de la base: [#4, integrada](https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D/pull/4). PR de esta corrección: todavía no creada por instrucción de Roger.

## Instrucciones

Partir de la [guía visual v0.1](../memory-bank/diseno.md) y los [tokens compartidos](../src/styles/tokens.css). Roger ha aceptado la portada como buena base de trabajo. Conservar esa dirección; las otras cuatro vistas requieren su diseño y revisión.

Ya existe una primera propuesta HTML del inicio (antecedente en el historial Git) con hero a pantalla completa, imágenes para móvil/escritorio y una lámina del logo (antecedente en el historial Git). Trasladar recursos y patrones de esa referencia al integrar T02. Adaptar enlaces a las cinco páginas reales y retirar la dependencia documental de la carpeta local de preview. No dar la tarea por completada por disponer de esa vista previa.

Aplicar [el prompt maestro](../PROMPT-MAESTRO.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Integrar la identidad documentada de Maison RDL y preparar composiciones de las cinco vistas, variantes de cabecera y reglas responsive. Usar utilidades Tailwind para layout/estados, sin trasladar todo el ejercicio a CSS manual.
2. Preparar navbar con logo, búsqueda y cuenta; footer con categorías, legal, marca y contacto.
3. Definir tarjetas, campos, botones, enlaces, foco y navegación móvil sin JavaScript.
4. Aplicar los elementos compartidos a los esqueletos y regenerar CSS.
5. Registrar cambios de identidad en guía/tokens dentro de la misma PR. El hero a pantalla completa es solo de inicio; las páginas internas usan cabecera clara en flujo normal.

## Criterios de cierre

- [x] Existe guía concreta que Daniel y Lydia pueden seguir: memory-bank/diseno.md y docs/componentes.html, integrados en la PR #4.
- [ ] Navbar/footer y controles de referencia funcionan dentro del alcance estático y se revisan en móvil y escritorio.
- [x] Cada enlace de las seis vistas tiene destino existente: comprobación estática de enlaces/anclas realizada el 23/10/2026; no acredita navegación interactiva.
- [x] Comprobaciones realizadas y límites documentados: build, Nu HTML Checker, rutas/recursos/IDs/controles y bloqueo actual de Chromium, en el registro de cierre inferior.
- [x] Base revisada por otra persona e integrada: aprobación de Lydia y merge de la PR #4 comprobados en GitHub.
- [ ] Resultado técnico de la base verificado en las seis vistas; integración no equivale a verificación.
- [ ] Corrección de cierre revisada e integrada mediante su propia PR, aún no autorizada.

## Decisiones

- La base de Roger en `codex/base-visual` se integró en main mediante la PR #4, commit de merge `1f093aa26626f797da9a53ea72ad171b63dee6e6`. Aprobación de `LydiaBlackCat` registrada el 23/10/2026 a las 16:23:31 UTC; su revisión mantiene pendientes contenido y validación de navegador. Confirmado con GitHub CLI y ascendencia Git, sin repetir la integración.
- El cierre se trabaja en `codex/cierre-t02`, creada desde `origin/main` actualizado en ese merge. No se autoriza commit, push, apertura de PR ni merge de esta corrección.
- Se conservan los borrados locales previos de README.cn.md, README.es.md, learn.json y server.py, y la carpeta pquete-maison/ sin seguimiento. No se han restaurado, borrado ni guardado con stash.
- Tokens intactos. Cormorant Garamond 500 normal/italic y Manrope variable locales, con las dos licencias OFL. Logos y fotografías WebP copiados selectivamente sin modificar; procedencia en [assets/PROCEDENCIA.md](../assets/PROCEDENCIA.md).
- Cabecera clara en internas y variante superpuesta con logo marfil en inicio. Menú details/summary, búsqueda y cuenta mediante popover nativo, sin JavaScript. Búsqueda sin envío; cuenta sin registro ni credenciales.
- Navbar/footer copiados en las cinco páginas y en el muestrario; los fragmentos son referencias con rutas para la raíz, no includes. El muestrario usa rutas ../ y tiene @source explícito en Tailwind.
- Footer con categorías hacia la sección de productos, información legal de demo, marca y contacto sin datos comerciales inventados. Los enlaces de categorías no filtran.
- Controles y tarjetas de ejemplo en el muestrario; no definen inventario. Se conservan las secciones y comentarios de tareas de las páginas. No se modifican las fichas T03, T07 ni T08.
- Inicio incorpora los dos recortes del hero a 100svh, gradación oscura, texto HTML y CTA al catálogo. Ajustes de tipografía y poca altura preparados, aún pendientes de comprobación visual. Checkout conserva sus tres secciones y añade aviso de demo/botón deshabilitado, sin completar campos T08.
- Guía ampliada con patrones y esquemas de catálogo, producto, carrito y checkout. CSS adicional limitado a fuentes y patrones comunes; layout y rejillas mediante utilidades Tailwind. CSS generado exclusivamente con el build.

## Pendiente

- Completar la revisión interactiva de las seis vistas en navegador. Chromium sigue sin arrancar por `libatk-1.0.so.0`; no se han ejecutado pruebas responsive ni generado capturas en este cierre. Tamaños previstos, no probados: móvil compacto 375×667, tablet 768×1024 y escritorio 1440×1000, más anchuras intermedias.
- Roger confirma revisión manual de inicio, catálogo, producto, carrito y checkout, sin medir píxeles. No queda confirmada la revisión del muestrario, ni una matriz de dispositivos/tamaños ni resultados técnicos inequívocos. Los puntos manuales inferiores siguen sin acreditar; la aprobación de integración de Lydia no sustituye esas comprobaciones. No se añaden herramientas ni se continúa intentando instalar o reparar Chromium.
- Revisión de Gaby pendiente; PR propia de esta corrección solo cuando se autorice. La base ya está integrada; no marcarla verificada hasta completar las comprobaciones relevantes. La automatización de navegador no se añade como requisito del proyecto.

Contenido de T03–T08, diseños finales D01–D05, Schema.org T09 y PageSpeed público T12 siguen fuera de este cierre; no se evalúan aquí ni se les atribuye cumplimiento.

## Verificación del cierre — 23/10/2026

Entorno real: contenedor Ubuntu 24.04.5 LTS, Linux 6.8.0-1064-azure, Node 24.21.0, npm 11.19.0, Python 3.14.2 y OpenJDK 25.0.4.1. Rama `codex/cierre-t02` desde `origin/main` en `1f093aa`. Herramientas de validación solo en `/tmp/maison-cierre-t02`; sin dependencias nuevas del proyecto ni tests añadidos al repositorio.

Preparación para Gaby: se limita al build existente, revisión del diff y registro documental. Se conservan las correcciones de DOCTYPE y estado de integración. Las validaciones HTML/estáticas y el intento fallido de navegador de la tabla se realizaron anteriormente y no se presentan como repetidos en esta preparación. No se instalan herramientas, no se reintenta Chromium y no se cambia identidad, inventario ni contenido.

Ámbito: index.html, catalogo.html, producto.html, carrito.html, checkout.html y docs/componentes.html. Las comprobaciones de archivos no tienen viewport; los tamaños indicados arriba son exclusivamente pendientes de prueba en navegador.

| Comprobación ejecutada | Resultado y alcance |
| --- | --- |
| PR #4 con GitHub CLI y ascendencia Git | Estado MERGED hacia main, aprobación APPROVED de LydiaBlackCat y commit de merge confirmados; no se repite la integración |
| DOCTYPE del muestrario | Primera línea exacta `<!DOCTYPE html>` comprobada; sin cambios de composición o estilos |
| `npm run build` | Correcto con Tailwind 4.3.3; assets/css/styles.css regenerado sin diferencias respecto a main |
| `java -jar /tmp/maison-cierre-t02/vnu.jar --format json index.html catalogo.html producto.html carrito.html checkout.html docs/componentes.html` | Nu HTML Checker 26.10.12 (0a70d65): `messages: []`, sin errores ni avisos en los seis documentos |
| `python3 /tmp/maison-cierre-t02/comprobar.py` | Parsers estándar HTMLParser y tinycss2 1.5.1: 67 enlaces/anclas locales, 14 recursos únicos HTML/CSS y 56 destinos de popover o campos etiquetados; cero errores. IDs sin duplicados; referencias aria/for/list y destinos de controles existentes; imágenes con alt/dimensiones, fuentes locales referenciadas y archivos no vacíos; checkout sin formulario y botón final deshabilitado. Es una comprobación estática, no de renderizado ni interacción |
| Arranque de Chromium con Playwright | Bloqueado antes de cargar páginas: `error while loading shared libraries: libatk-1.0.so.0: cannot open shared object file: No such file or directory`. No se reintenta reparar bibliotecas ni se atribuyen pruebas Playwright/axe, capturas, contraste visual, ausencia de overflow o CTA visible |
| `git -c core.whitespace=cr-at-eol diff --check` | Correcto en los cuatro archivos de esta corrección, respetando los finales CRLF existentes |

### Lista manual pendiente

Puntos no acreditados para revisar en las seis vistas y registrar con el contexto realmente utilizado. Las resoluciones anteriores son referencias previstas, no mediciones realizadas ni requisitos nuevos del instructor:

1. Recorrer navbar, footer y enlaces; abrir/cerrar menú móvil con summary, búsqueda y cuenta con sus botones y Escape. Confirmar vuelta del foco al control que abrió cada panel y acceso a cuenta desde móvil.
2. Usar solo teclado: enlace de salto, Tab/Mayús+Tab, Enter/Espacio, orden lógico y foco visible sobre fondos claros, foto y footer. Revisar labels, lectura y contraste; la validación HTML no acredita accesibilidad completa.
3. En el muestrario, editar texto/cantidad, seleccionar opciones/radios/checkbox y comprobar controles deshabilitados. Verificar que no hay envío de datos ni se promete filtrado, registro o pago real.
4. Confirmar imágenes y fuentes cargadas, recortes móvil/escritorio y ausencia de desbordamiento horizontal. En inicio a 375×667, comprobar titular legible y CTA completo dentro de la primera pantalla, sin solapamientos.

## Comprobaciones y evidencia

Fecha: 23/10/2026.

### Revisión manual de Roger

Registro actualizado el 23/10/2026 tras solicitar confirmación antes de editar. Evidencia declarada por Roger, no obtenida mediante una prueba automática:

| Dato solicitado | Confirmación recibida |
| --- | --- |
| Páginas revisadas | Inicio, catálogo, producto, carrito y checkout |
| Muestrario docs/componentes.html | No seleccionado; revisión no confirmada |
| Tamaños en píxeles | Roger indica: «no medi pixeles»; no se asignan resoluciones ni se dan por probados los tamaños previstos |
| Dispositivo y navegador | No identificados; no se deduce cobertura de móvil, tablet o escritorio |
| Fecha exacta de ejecución y capturas | No precisadas; la fecha anterior corresponde al registro de esta declaración, no acredita el momento de la prueba. No se han aportado capturas |
| Resultados de las comprobaciones | Se confirma la revisión visual general; las respuestas no permiten acreditar resultados específicos de interacción o responsive |

Quedan sin acreditar de forma inequívoca menú móvil; apertura/cierre de búsqueda y cuenta con botones/Escape; navegación por teclado, enlace de salto, foco visible y retorno del foco; campos del muestrario; renderizado de imágenes/fuentes; contraste visual; ausencia de overflow; CTA completo en la primera pantalla móvil; y ausencia de envío de datos/pagos comprobada manualmente. Las comprobaciones estáticas anteriores conservan su propio alcance y no sustituyen esta evidencia interactiva. No se marca ningún criterio adicional como cumplido ni T02 como verificada.

### Comprobaciones técnicas de la preparación original (histórico)

- Preparación para commit, 23/10/2026: `npm run build` ejecutado de nuevo sobre los archivos actuales, correcto con Tailwind 4.3.3. Revisión del diff de T02 y comparación estática de las seis copias de navbar/footer con sus fragmentos: coinciden, incluidas variantes y rutas. Comentarios de tareas de los cinco esqueletos conservados. Esta comprobación estática no acredita comportamiento responsive ni accesibilidad en navegador; no se ha reintentado Playwright/axe en esta preparación.
- Control de espacios del staging: se respeta CRLF con `git -c core.whitespace=cr-at-eol diff --cached --check`. Dos avisos heredados de `trailing whitespace` en la línea 21 de cada licencia OFL; se conservan las licencias copiadas sin modificar. No confundir estos avisos con un fallo del build.
- Git: repositorio/remoto/estado inicial comprobados, fetch de origin, comprobación de PR #2/#3 y rama creada desde main actualizado. Cambios previos conservados.
- Build: el primer `npm run build` no pudo arrancar (`tailwindcss: not found`). Tras `npm ci`, build correcto con Tailwind 4.3.3. El último build, después de copiar los fragmentos a las seis vistas, terminó correctamente. No se añaden dependencias al proyecto ni se edita CSS generado a mano.
- Recursos: metadatos de los tres WOFF2 identificados con fc-scan; traslado selectivo de quince archivos de la referencia con copia exclusiva, sin sobrescribir existentes. La hoja fonts.css de la referencia está excluida del acceso de Copilot y no se leyó por vías alternativas; los @font-face se declararon en la entrada compartida.
- Servidor estático iniciado con `python3 -m http.server 8000`: [inicio local](http://localhost:8000/) y [muestrario local](http://localhost:8000/docs/componentes.html). La disponibilidad del servidor no acredita QA responsive.
- Navegador: Playwright y axe preparados únicamente en /tmp, sin tests ni dependencias nuevas en el repositorio. Chromium no llegó a abrir las páginas: primero faltaba `libatk-1.0.so.0`. Intento 1 de descargar bibliotecas: APT sin índices (`Unable to locate package`). Intento 2: índices y diez bibliotecas extraídos localmente sin sudo; Chromium sigue sin arrancar con `error while loading shared libraries: libdrm.so.2: cannot open shared object file: No such file or directory`. Sospecha: dependencia transitiva del paquete libgbm1. Se detienen los intentos; no se atribuyen pruebas de teclado, contraste, capturas ni ausencia de overflow.

## Traspaso y siguiente paso

La base ya está disponible en main para Daniel (T04–T06) y Lydia (T07–T08): fragmentos src/partials/navbar.html y footer.html con copias en las cinco páginas; navbar clara/sobre foto, menú móvil nativo, búsqueda/cuenta de demo, footer, tarjetas, botones, campos, selectores, hover/foco/deshabilitado; tokens y entrada de src/styles/, assets/css/styles.css, fuentes/logos/imágenes con licencias y procedencia; muestrario docs/componentes.html y esquemas en memory-bank/diseno.md. Los fragmentos no son includes automáticos.

Roger deja la corrección de cierre preparada en su rama para revisión de Gaby, todavía no realizada. Sin commit, push, PR ni merge en esta sesión. Fuera del cierre: inventario y contenido T03–T08, diseños finales D01–D05, Schema.org T09 y PageSpeed T12. No se toman sus fichas ni se declara terminado su trabajo. Se conservan fuera de los cambios pquete-maison/, node_modules/ y los cuatro borrados locales previos.
