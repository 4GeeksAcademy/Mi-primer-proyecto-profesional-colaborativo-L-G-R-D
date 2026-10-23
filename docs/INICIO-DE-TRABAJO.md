# Maison RDL — Arranque común del equipo

## Antes de repartir archivos

1. Daniel comprueba T00: mismo repositorio y permisos efectivos para los tres.
2. T01 incorpora este paquete de documentos, reglas y tokens. Revisar el README existente; no sobrescribirlo sin conservar información útil. Excluir COMPARACION-PLANES.md, que es histórico.
3. Daniel documenta Tailwind y servidor reproducibles. Roger revisa que las clases de los cinco HTML y fragmentos se incluyan al compilar.
4. Roger integra T02: recursos de marca/fuentes, cabeceras, footer, controles y composiciones. La [guía visual](diseno.md) ya permite avanzar en contenido; todavía falta integrar la base en el repo.
5. Daniel publica pronto tres fichas de producto para desbloquear carrito/checkout; después completa veinte.

Leer [AGENTS.md](../AGENTS.md), [CONTEXT.md](../CONTEXT.md), [requisitos](requisitos.md), [diseño](diseno.md) y la ficha propia. Usar el [prompt de sesión](../PROMPT-MAESTRO.md) indicando persona, ID, rama y archivos.

## Qué hace cada uno

| Roger | Daniel | Lydia |
| --- | --- | --- |
| Base visual y diseño de las cinco páginas; Tailwind/responsive; recursos y optimización | Setup, inventario, estructura/contenido de inicio/catálogo/producto, SEO y Schema.org | Estructura/contenido de carrito/checkout, importes, formularios, QA y evidencias de cinco vistas, README |
| Revisa cambios visuales de los compañeros | Revisa contenido y PR asignadas; coordina acuerdos estables | Revisa PR asignadas; registra incidencias con evidencia |
| Sus PR las revisa Daniel o Lydia | Corrige los problemas de su código | No absorbe todas las correcciones del equipo |

Daniel y Lydia construyen HTML completo conforme a los componentes y composiciones de Roger. Pueden añadir las utilidades necesarias de la base; no se les pide un HTML deliberadamente sin estilos. Roger aplica el acabado visual de todas las páginas después de cada PR estructural integrada.

## Ejemplo de traspaso

Daniel completa T06 producto → PR revisada → integrada en main → ficha libera producto.html → Roger crea D03 desde main actualizado → diseño responsive → PR revisada por Daniel → integración → T09 SEO → T10 QA.

Mientras Roger diseña producto, Lydia puede construir checkout en su rama. No editar el mismo archivo a la vez. Cambios globales de navbar/footer/estilos requieren coordinar las reservas antes de empezar.

## Estilos y recursos durante T01/T02

Ubicación final prevista:
- src/styles/input.css: entrada Tailwind.
- src/styles/tokens.css: valores compartidos ya preparados.
- assets/css/styles.css: CSS generado, no editar a mano.
- assets/fonts y assets/brand: recursos trasladados de la preview.
- src/partials/navbar.html y footer.html: referencias, copiadas en las cinco páginas.

En Tailwind 4, input.css importa tailwindcss y después ./tokens.css. Registrar las fuentes HTML reales con @source si el método elegido lo requiere. No copiar las rutas de la preview sin adaptarlas: su CSS está en assets/styles.css, mientras que el repo de entrega usará assets/css/styles.css.

La preview tiene npm run build; ese comando pertenece a la preview hasta que T01 cree y documente el equivalente en el repo. No presentarlo como disponible allí todavía.

## Una sesión, una tarea

- Comprobar rama/cambios, dependencias y reservas; sincronizar según el plan.
- Modificar los archivos de la tarea; conservar las decisiones de marca.
- Verificar lo afectado y anotar resultados reales en la ficha.
- Preparar commit por cambio lógico y PR con criterios cubiertos y evidencia.
- Daniel mantiene memoria global por cambios relevantes de acuerdos o integración; no pedir a los tres que reescriban progress.md al cerrar cada sesión.
- No marcar verificada una tarea solo por terminar código o abrir una PR.

## Checklist de revisión

La [plantilla de PR](../.github/PULL_REQUEST_TEMPLATE.md) incluye alcance, IDs de requisitos, pruebas, capturas y traspaso. Es guía para la revisión; no demuestra por sí misma que las pruebas ocurrieron.

Antes de entregar, usar la matriz de requisitos y completar evidencias sobre la URL pública. No confundir la portada local aprobada como base con las cinco páginas terminadas.
