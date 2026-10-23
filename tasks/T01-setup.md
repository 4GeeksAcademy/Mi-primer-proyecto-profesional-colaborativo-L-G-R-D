# T01 — Setup y método de Tailwind

Proyecto: Maison RDL.
Estado: En curso.
Responsable: Daniel.
Revisor: Roger.
Rama: codex/setup-tecnico (creada desde origin/main el 23/10/2026; codex/setup se usó para incorporar la documentación, PR #1 integrada).
Depende de: T00.
Archivos previstos: README.md, PLAN-DE-PROYECTO.md, CONTEXT.md, AGENTS.md, PROMPT-MAESTRO.md, memory-bank/, .agents/rules/, .github/PULL_REQUEST_TEMPLATE.md, docs/, tasks/, estructura de carpetas, esqueletos de cinco HTML, src/styles/input.css, assets/css/styles.css.
Responsable activo de los archivos: Daniel, para package.json, package-lock.json, .gitignore, src/styles/input.css, assets/css/styles.css, los cinco esqueletos HTML, README.md y esta ficha mientras dure T01.
PR: pendiente.

## Instrucciones

Aplicar [el prompt maestro](../PROMPT-MAESTRO.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Revisar instrucciones reales del repositorio. Incorporar este paquete de planificación, reglas, memoria y tokens sin sus antecedentes históricos; seguir docs/INICIO-DE-TRABAJO.md. Conservar información útil del README existente.
2. Crear cinco esqueletos HTML enlazados con idioma, charset, viewport, title y landmarks. No confundir el esqueleto con una vista terminada.
3. Preparar la generación de CSS estático con Tailwind CLI oficial; documentar versión, instalación y comando. Priorizar CLI independiente si facilita el entorno; la preview usa Tailwind 4.3.3 con npm. Los tokens usan @theme de v4: documentar versión real y adaptar configuración si fuera necesario sin cambiar identidad.
4. Comprobar que el CSS detecta clases en los cinco HTML y en los fragmentos de referencia. No usar CDN en paralelo en la entrega.
5. Documentar servidor local y resolver con el equipo idioma, moneda y fecha de entrega.

## Criterios de cierre

- [ ] Los tres pueden abrir las cinco páginas y generar el CSS con las instrucciones.
- [ ] No se han añadido frameworks ni lógica JavaScript a la aplicación.
- [ ] AGENTS, contexto, requisitos, guía, reglas, memoria y fichas están accesibles, con enlaces internos válidos; ningún resultado futuro aparece como terminado.
- [ ] Comprobaciones pertinentes documentadas con evidencia real.
- [ ] PR revisada por otra persona, integrada y resultado verificado.

## Decisiones

- Tailwind CSS 4.3.3 con @tailwindcss/cli 4.3.3 mediante npm, versiones fijas, igual que la referencia visual. Así se usan los tokens @theme sin adaptarlos.
- Entrada src/styles/input.css → salida assets/css/styles.css minificada (npm run build; npm run watch en desarrollo). El CSS generado se versiona.
- Detección explícita: @import "tailwindcss" source(none) y @source para los cinco HTML y src/partials. docs/ y la referencia visual no se escanean.
- Servidor documentado: python3 -m http.server 8000 (sin dependencias); se conserva server.py de la plantilla (Flask, puerto 3000) como alternativa.
- Esqueletos con lang="es" de forma provisional: el idioma definitivo sigue pendiente de acordar.
- Respetar Maison RDL y la responsabilidad de Roger sobre diseño y optimización: los esqueletos solo usan utilidades básicas con los tokens; no cargan fuentes, logo ni imágenes (T02).

## Cambios realizados

- package.json y package-lock.json: dependencias de desarrollo y scripts build/watch.
- .gitignore: node_modules/, ZIP, tmp/ y .DS_Store.
- src/styles/input.css: entrada de Tailwind que importa tokens.css sin modificarlo.
- assets/css/styles.css: CSS generado.
- index.html, catalogo.html, producto.html, carrito.html, checkout.html: idioma, charset, viewport, title propio, enlace de salto, header/nav/main/footer, h1 y secciones h2 con comentarios de la tarea que las completa, navegación entre las cinco vistas con aria-current en la principal.
- README.md: proyecto, estado, instalación, build, servidor, estructura y alcance; se conservan el comando de server.py y los créditos de html-hello. README.es.md y README.cn.md de la plantilla no se han tocado.

## Pendiente

- Revisión de Roger del método de Tailwind y de la detección de clases.
- Commit, push y PR: no realizados en esta sesión por indicación de Daniel, a la espera de revisar el resultado.
- Comprobar que Roger y Lydia pueden instalar, generar el CSS y abrir las cinco páginas con el README (criterio de cierre).
- Acordar idioma, moneda y fecha de entrega con el equipo.
- PLAN-DE-PROYECTO.md (sección 8) indica codex/setup para T01; actualizarlo a codex/setup-tecnico si el equipo lo confirma.
- Tras integrar: Daniel actualiza memory-bank/techContext.md con los comandos validados.
- Fuentes WOFF2, logo, favicon, navbar/footer definitivos y src/partials: T02 (Roger).

## Comprobaciones y evidencia

23/10/2026, rama codex/setup-tecnico, Node 24.21.0, npm 11.19.0:
- npm install / npm ci + npm run build: correctos (tailwindcss v4.3.3). Tras borrar node_modules y ejecutar npm ci, el CSS regenerado es idéntico byte a byte (7802 bytes). npm avisa de que no ejecutó scripts de instalación; el build funciona igualmente.
- Detección de clases: con una clase de sonda temporal en cada uno de los cinco HTML y en un archivo temporal de src/partials, las seis aparecen en el CSS compilado (salida a carpeta temporal; sondas retiradas). Utilidades presentes solo en docs/referencia-visual (por ejemplo lg:gap-28) no aparecen. Clases con tokens (bg-ivory, text-ink, font-display, bg-night, text-on-dark-muted, border-line, outline-bronze) presentes.
- python3 -m http.server 8000 y python3 server.py (Flask 3.1.3): las cinco páginas y assets/css/styles.css responden 200.
- Enlaces internos: todos los href apuntan a archivos existentes.
- html-validate 9 (npx, sin añadirlo a dependencias): 0 problemas en los cinco HTML.
- Chromium headless (Playwright, instalado fuera del repo) a 375×667, 768×1024 y 1280×800: sin scroll horizontal, sin recursos fallidos, fondo ivory, footer night, un header/main/footer y aria-current correcto en cada página. Primer Tab enfoca y muestra «Saltar al contenido». Capturas revisadas localmente; no se incluyen en el repo porque son de esqueletos.
- Sin JavaScript ni CDN en las páginas.
- No ejecutado: PageSpeed (requiere URL pública, T12), validación Schema.org (T09), revisión de Roger y de los compañeros.

## Traspaso y siguiente paso

Tras la revisión y la PR integrada, T02 (Roger) recibe los esqueletos, input.css y el método de build, y T03 puede empezar. Liberar entonces la reserva de los archivos de T01.
