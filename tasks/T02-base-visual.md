# T02 — Guía visual y elementos compartidos

Proyecto: Maison RDL.
Estado: En curso; revisión visual manual realizada por Roger. Pruebas automáticas de navegador bloqueadas; sin integrar ni verificar.
Responsable: Roger.
Revisor: Daniel.
Rama: codex/base-visual.
Depende de: T01.
Archivos: docs/diseno.md, docs/componentes.html, README.md, src/styles/input.css, src/partials/navbar.html, src/partials/footer.html, cinco esqueletos, assets/css/styles.css y recursos de assets/ documentados en assets/PROCEDENCIA.md. src/styles/tokens.css se conserva sin cambios.
Responsable activo de los archivos: Roger durante T02; estilos compartidos, fragmentos, recursos trasladados, docs/componentes.html, docs/diseno.md, README.md y base común de los cinco esqueletos. No incluye contenido ni fichas T03/T07/T08.
PR: pendiente.

## Instrucciones

Partir de la [guía visual v0.1](../docs/diseno.md) y los [tokens compartidos](../src/styles/tokens.css). Roger ha aceptado la portada como buena base de trabajo. Conservar esa dirección; las otras cuatro vistas requieren su diseño y revisión.

Ya existe una [primera propuesta HTML del inicio](../docs/referencia-visual/index.html) con hero a pantalla completa, imágenes para móvil/escritorio y una [lámina del logo](../docs/referencia-visual/identidad.html). Trasladar recursos y patrones de esa referencia al integrar T02. Adaptar enlaces a las cinco páginas reales y retirar la dependencia documental de la carpeta local de preview. No dar la tarea por completada por disponer de esa vista previa.

Aplicar [el prompt maestro](../PROMPT-MAESTRO.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Integrar la identidad documentada de Maison RDL y preparar composiciones de las cinco vistas, variantes de cabecera y reglas responsive. Usar utilidades Tailwind para layout/estados, sin trasladar todo el ejercicio a CSS manual.
2. Preparar navbar con logo, búsqueda y cuenta; footer con categorías, legal, marca y contacto.
3. Definir tarjetas, campos, botones, enlaces, foco y navegación móvil sin JavaScript.
4. Aplicar los elementos compartidos a los esqueletos y regenerar CSS.
5. Registrar cambios de identidad en guía/tokens dentro de la misma PR. El hero a pantalla completa es solo de inicio; las páginas internas usan cabecera clara en flujo normal.

## Criterios de cierre

- [ ] Existe guía concreta que Daniel y Lydia pueden seguir.
- [ ] Navbar/footer y controles de referencia funcionan dentro del alcance estático y se revisan en móvil y escritorio.
- [ ] Cada enlace tiene destino o un pendiente explícito que deba cerrarse antes de QA.
- [ ] Comprobaciones pertinentes documentadas con evidencia real.
- [ ] PR revisada por otra persona, integrada y resultado verificado.

## Decisiones

- Trabajo de Roger en `codex/base-visual`, creada desde `origin/main` en `0a607bf`. Comprobadas por GitHub CLI las PR #2 y #3 como MERGED hacia main y su ascendencia mediante Git. No se ha hecho commit, push, PR ni merge de entrega.
- Se conservan los borrados locales previos de README.cn.md, README.es.md, learn.json y server.py, y la carpeta pquete-maison/ sin seguimiento. No se han restaurado, borrado ni guardado con stash.
- Tokens intactos. Cormorant Garamond 500 normal/italic y Manrope variable locales, con las dos licencias OFL. Logos y fotografías WebP copiados selectivamente sin modificar; procedencia en [assets/PROCEDENCIA.md](../assets/PROCEDENCIA.md).
- Cabecera clara en internas y variante superpuesta con logo marfil en inicio. Menú details/summary, búsqueda y cuenta mediante popover nativo, sin JavaScript. Búsqueda sin envío; cuenta sin registro ni credenciales.
- Navbar/footer copiados en las cinco páginas y en el muestrario; los fragmentos son referencias con rutas para la raíz, no includes. El muestrario usa rutas ../ y tiene @source explícito en Tailwind.
- Footer con categorías hacia la sección de productos, información legal de demo, marca y contacto sin datos comerciales inventados. Los enlaces de categorías no filtran.
- Controles y tarjetas de ejemplo en el muestrario; no definen inventario. Se conservan las secciones y comentarios de tareas de las páginas. No se modifican las fichas T03, T07 ni T08.
- Inicio incorpora los dos recortes del hero a 100svh, gradación oscura, texto HTML y CTA al catálogo. Ajustes de tipografía y poca altura preparados, aún pendientes de comprobación visual. Checkout conserva sus tres secciones y añade aviso de demo/botón deshabilitado, sin completar campos T08.
- Guía ampliada con patrones y esquemas de catálogo, producto, carrito y checkout. CSS adicional limitado a fuentes y patrones comunes; layout y rejillas mediante utilidades Tailwind. CSS generado exclusivamente con el build.

## Pendiente

- Desbloquear Chromium y realizar la comprobación solicitada de las seis vistas a 375×667, 768×1024 y 1440×1000; anchuras intermedias, navegación, teclado, foco, labels, contraste, recursos, overflow y CTA del hero en móvil compacto. No existen aún capturas nuevas ni resultados de estas pruebas.
- Recoger observaciones concretas y el alcance de la revisión manual de Roger si se facilitan; su confirmación no detalla páginas, tamaños, incidencias ni aprobación final. El contenido de T03–T08 y los diseños finales D01–D05 siguen pendientes.
- PageSpeed sobre URL pública corresponde a T12; no se ha ejecutado ni se atribuye una puntuación.
- Revisión de Daniel, PR e integración posteriores, solo cuando se autoricen. No marcar T02 integrada ni verificada.

## Comprobaciones y evidencia

Fecha: 23/10/2026.

### Revisión manual de Roger

Roger comunica: «He revisado visualmente la web» y confirma registrar esta revisión manual. No aporta observaciones específicas, páginas, dispositivos, tamaños de pantalla ni capturas. Se deja constancia de la revisión realizada, sin atribuir resultados concretos de navegación, teclado, foco, labels, contraste, recursos, overflow o CTA en móvil, ni aprobación final. Esta revisión no sustituye a las pruebas automáticas bloqueadas.

### Comprobaciones técnicas

- Preparación para commit, 23/10/2026: `npm run build` ejecutado de nuevo sobre los archivos actuales, correcto con Tailwind 4.3.3. Revisión del diff de T02 y comparación estática de las seis copias de navbar/footer con sus fragmentos: coinciden, incluidas variantes y rutas. Comentarios de tareas de los cinco esqueletos conservados. Esta comprobación estática no acredita comportamiento responsive ni accesibilidad en navegador; no se ha reintentado Playwright/axe en esta preparación.
- Control de espacios del staging: se respeta CRLF con `git -c core.whitespace=cr-at-eol diff --cached --check`. Dos avisos heredados de `trailing whitespace` en la línea 21 de cada licencia OFL; se conservan las licencias copiadas sin modificar. No confundir estos avisos con un fallo del build.
- Git: repositorio/remoto/estado inicial comprobados, fetch de origin, comprobación de PR #2/#3 y rama creada desde main actualizado. Cambios previos conservados.
- Build: el primer `npm run build` no pudo arrancar (`tailwindcss: not found`). Tras `npm ci`, build correcto con Tailwind 4.3.3. El último build, después de copiar los fragmentos a las seis vistas, terminó correctamente. No se añaden dependencias al proyecto ni se edita CSS generado a mano.
- Recursos: metadatos de los tres WOFF2 identificados con fc-scan; traslado selectivo de quince archivos de la referencia con copia exclusiva, sin sobrescribir existentes. La hoja fonts.css de la referencia está excluida del acceso de Copilot y no se leyó por vías alternativas; los @font-face se declararon en la entrada compartida.
- Servidor estático iniciado con `python3 -m http.server 8000`: [inicio local](http://localhost:8000/) y [muestrario local](http://localhost:8000/docs/componentes.html). La disponibilidad del servidor no acredita QA responsive.
- Navegador: Playwright y axe preparados únicamente en /tmp, sin tests ni dependencias nuevas en el repositorio. Chromium no llegó a abrir las páginas: primero faltaba `libatk-1.0.so.0`. Intento 1 de descargar bibliotecas: APT sin índices (`Unable to locate package`). Intento 2: índices y diez bibliotecas extraídos localmente sin sudo; Chromium sigue sin arrancar con `error while loading shared libraries: libdrm.so.2: cannot open shared object file: No such file or directory`. Sospecha: dependencia transitiva del paquete libgbm1. Se detienen los intentos; no se atribuyen pruebas de teclado, contraste, capturas ni ausencia de overflow.

## Traspaso y siguiente paso

Reserva de Roger mantenida hasta cerrar T02; todavía no hay traspaso integrado. Revisión visual manual de Roger registrada, sin aprobación final ni observaciones detalladas. Siguiente paso: preparar únicamente los archivos de T02 para el commit, sin crear el commit, hacer push ni abrir PR; quedan fuera pquete-maison/, node_modules/ y los borrados locales previos. Desbloquear después Chromium y ejecutar la comprobación preparada; cuando se autorice, entregar los patrones a Daniel (T04–T06) y Lydia (T07–T08). No tomar sus tareas de contenido ni cambiar sus fichas. Revisión de Daniel pendiente; sin autoaprobación.
