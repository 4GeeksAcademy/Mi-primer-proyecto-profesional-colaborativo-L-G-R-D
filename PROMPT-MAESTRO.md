# Maison RDL — Prompt maestro corregido

Copiar el bloque siguiente al asistente de cada integrante y sustituir los campos. Las fichas contienen instrucciones específicas; no ejecutar todas las tareas en una sesión.

~~~
Proyecto: Maison RDL, prototipo de tienda de ropa de lujo con sede en Francia.
Equipo: Roger, Daniel y Lydia.
Persona de esta sesión: <NOMBRE>.
Tarea: <ID y nombre>.
Ficha: tasks/<ARCHIVO>.md.
Rama exacta: <RAMA de la ficha>.

Lee AGENTS.md, CONTEXT.md, memory-bank/projectbrief.md, techContext.md y progress.md.
Consulta docs/requisitos.md, PLAN-DE-PROYECTO.md y la ficha propia.
Si tocas HTML/CSS, aplica docs/diseno.md, src/styles/tokens.css y .agents/rules/visual-identity.md. Aplica siempre .agents/rules/project-scope.md.
Stack de la tienda: solo HTML semántico y Tailwind CSS.
Sin JavaScript de aplicación, React, otros frameworks, backend, cuentas reales ni procesamiento de pagos.
Tailwind CLI es una herramienta de desarrollo permitida por este plan para generar CSS estático; no implica añadir lógica a la tienda. Usa el método documentado en T01. No añadas bibliotecas ajenas.

RESPONSABILIDADES:
Roger diseña las CINCO páginas, mantiene los elementos visuales comunes y realiza la optimización.
Daniel construye estructura/contenido de inicio, catálogo y producto y lleva inventario, SEO/Schema.org y preparación técnica.
Lydia construye estructura/contenido de carrito y checkout y coordina QA de las cinco páginas, incidencias, evidencias y README.
La portada aceptada es base de trabajo v0.1, no aprobación final de las cinco vistas. No cambies la identidad visual por tu cuenta. Toda PR que afecte al diseño necesita revisión de Roger, excepto las propias de Roger, que revisa Daniel o Lydia.

AL EMPEZAR:
1. Comprueba git status --short --branch. Identifica cambios locales; no los borres ni hagas reset/stash automático.
2. Lee acuerdos, ficha, dependencias, archivos reservados y PR relacionadas. En el primer setup algunos documentos todavía no existen: créalos según el plan.
3. Ejecuta git fetch origin.
4. Selecciona la rama correcta: local existente, seguimiento de su rama remota si existe, o nueva desde origin/main si no existe ninguna.
5. Si hay rama remota de tarea, revisa su estado; usa integración lineal cuando proceda y coordina si diverge.
6. Incorpora origin/main expresamente a la rama de tarea. Resuelve conflictos preservando trabajo ajeno; revisa el resultado.
No ejecutes git pull origin main sin saber qué rama está activa. git status no bloquea automáticamente el trabajo por detectar cambios.

DURANTE:
Trabaja solo dentro del alcance y archivos coordinados de la tarea.
Una persona por rama y un responsable activo por archivo.
Usa la guía y fragmentos de Roger, conserva contenido y semántica.
Los cambios transversales pueden afectar varias páginas solo si se coordinan y se declaran en la PR.
No edites manualmente el CSS generado. Si cambian clases o fuentes, regenera con el método documentado.
No confundas filtros visuales o enlaces del carrito con operaciones persistentes.
En checkout no envíes datos ni habilites pagos; usa datos ficticios para las comprobaciones.

AL TERMINAR:
1. Comprueba diff y requisitos de la ficha.
2. Ejecuta verificaciones pertinentes y documenta resultados reales.
3. Actualiza tu ficha con estado, decisiones, pendiente, evidencias, reserva de archivos y PR. Daniel coordina cambios de CONTEXT.md y memoria global cuando cambian acuerdos o se integra una fase, siguiendo memory-bank/README.md. No reescribáis los tres un resumen global por sesión.
4. Añade archivos explícitos, revisa git diff --cached y crea commits por cambio lógico con mensajes claros.
5. Sube tu rama. Si cumple los criterios, abre PR con resumen, IDs de docs/requisitos.md, pruebas y capturas útiles. Usa .github/PULL_REQUEST_TEMPLATE.md.
6. Usa un cuerpo estructurado o un archivo con --body-file para descripciones multilínea.
7. Incorpora los cambios recientes de main antes de integrar; repite comprobaciones afectadas si hubo conflictos.
8. Solicita revisión al integrante indicado. Usa los estados de la ficha: Pendiente → En curso → En revisión → Integrada → Verificada; no adelantes estados sin evidencia.
No force-push, no commits de desarrollo en main, no sobrescribir trabajo ajeno ni inventar pruebas.

Si falta una dependencia, documenta qué falta y avanza solo en trabajo independiente. No sustituyas al compañero ni tomes un archivo reservado sin coordinación.
Las tareas de publicación, acceso y entrega se realizan únicamente al llegar a su fase y dentro de las instrucciones del equipo. Este prompt no concede autorización para enviar mensajes ni cambiar accesos por iniciativa propia.
~~~
