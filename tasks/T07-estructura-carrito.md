# T07 — Estructura y contenido de carrito

Proyecto: Maison RDL.
Estado: En curso (solo planificación; implementación bloqueada por T02 y T03).
Responsable: Lydia.
Revisor: Daniel; Roger si afecta a la composición.
Rama: codex/estructura-carrito.
Depende de: T02 y tres productos de T03.
Archivos previstos: carrito.html, supuesto de importes en docs/inventario-productos.md y ficha propia.
Responsable activo de los archivos: Lydia, solo esta ficha durante la preparación; sin reserva de carrito.html ni del inventario. Respetar la reserva de T01 hasta coordinar su liberación.
PR: no creada; sin commit, push ni integración por indicación de Lydia.

## Instrucciones

Aplicar [el prompt maestro](../PROMPT-MAESTRO.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Crear página completa del carrito con tres productos compartidos.
2. Mostrar miniatura, precio unitario, cantidad y total por línea.
3. Calcular y comprobar manualmente subtotal, impuestos y total conforme al supuesto documentado.
4. Añadir Comprar hacia checkout y navegación de vuelta.
5. Indicar que los datos son estáticos; coordinar con Roger la composición para D04.

## Criterios de cierre

- [ ] Importes comprobados y sin doble contabilización de impuestos.
- [ ] Carrito completo y enlazado, sin panel lateral ni cálculos dinámicos prometidos.
- [ ] Comprobaciones pertinentes documentadas con evidencia real.
- [ ] PR revisada por otra persona, integrada y resultado verificado.

## Decisiones

Preparación documental del 23/10/2026 en codex/estructura-carrito, creada desde origin/main (6fb5fa4). No se modifica el HTML ni se implementa T08 en esta rama. Stack previsto: HTML semántico y Tailwind, sin JavaScript de aplicación, backend ni persistencia.

### Campos de las tres líneas

Cada línea tomará un producto distinto del [inventario de T03](T03-inventario.md), sin reutilizar datos comerciales de la preview:

| Campo | Origen o decisión pendiente |
| --- | --- |
| Referencia y nombre | Copiar exactamente del inventario común; talla o variante solo si está documentada. |
| Miniatura y texto alternativo | Imagen local del producto con procedencia registrada por Daniel; usar el recurso y recorte acordados con Roger, con dimensiones declaradas. |
| Precio unitario y moneda | Los del inventario; confirmar si incluyen impuestos antes de calcular. |
| Cantidad | Entero positivo acordado con Daniel para cada una de las tres referencias; todavía sin valores. Mostrarla como dato estático, sin prometer actualización. |
| Total de línea | Precio unitario multiplicado por cantidad, con el mismo criterio fiscal y precisión que el resumen. |

### Esquema de importes

- Total de cada línea = precio unitario × cantidad. Los tres productos y sus cantidades quedan pendientes; no se fijan importes de ejemplo.
- Si los precios no incluyen impuestos: subtotal = suma de líneas; impuestos = suma de los importes fiscales según el supuesto acordado; total = subtotal + impuestos.
- Si los precios incluyen impuestos: total = suma de líneas; impuestos = parte incluida conforme al supuesto acordado; subtotal sin impuestos = total - impuestos. No volver a sumar los impuestos al total.
- Elegir y documentar con Daniel una sola modalidad, moneda, precisión y regla de redondeo en el inventario antes de implementar. No se presupone porcentaje fiscal por la sede francesa ni se trata el supuesto como fiscalidad real.
- No añadir portes, descuentos u otros cargos sin acuerdo. Comprobar manualmente las tres multiplicaciones y la igualdad subtotal + impuestos = total, conciliando los redondeos.

### Estructura prevista

Página completa con navbar y footer de T02, tres líneas y resumen de subtotal, impuestos y total. Comprar será un enlace a [checkout.html](../checkout.html); habrá navegación de vuelta al [catálogo](../catalogo.html). Datos estáticos sin recálculo ni guardado. Aplicar únicamente [guía visual](../docs/diseno.md), [tokens](../src/styles/tokens.css) y componentes de Roger cuando estén integrados; no crear estilos alternativos. Roger recibirá el resultado en [D04](D04-diseno-carrito.md) tras integrar T07.

## Pendiente

- Daniel: integrar tres fichas completas de T03 (referencia, nombre, talla, precio, moneda e imagen local) y su procedencia; acordar cantidades, tratamiento fiscal y redondeo. El archivo docs/inventario-productos.md todavía no existe; no crearlo ni editarlo sin coordinar su responsabilidad activa.
- Roger: integrar T02, incluidos src/partials/navbar.html, src/partials/footer.html, recursos de marca/fuentes y patrones de campos, acciones, resumen y cabecera interna. Guía y tokens existentes no sustituyen esa integración.
- Daniel/Roger: confirmar el traspaso de carrito.html; la ficha T01 todavía mantiene su reserva aunque el setup ya está integrado.
- Tras resolver las dependencias: actualizar esta rama desde origin/main, reservar el HTML, construir T07 y comprobar importes, enlaces, semántica, build y vistas afectadas. Implementación de T08 en una tarea y rama posteriores.
- No se han enviado mensajes al equipo ni acordado valores en su nombre. Revisión conjunta de esta planificación pendiente.

## Comprobaciones y evidencia

23/10/2026, comprobación previa a la edición:
- Repositorio remoto: 4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-R-D. git status --short --branch: main sin cambios locales; git fetch origin correcto; main y origin/main sin divergencia (0/0).
- T01 integrado: origin/main en 6fb5fa4 contiene el merge de la PR #2 y el commit 813b0c8. Existen package.json, package-lock.json, src/styles/input.css, assets/css/styles.css y los cinco HTML. La ficha T01 y la memoria aún conservan estados anteriores; no se actualizan archivos de Daniel ni se da por cerrada toda su verificación.
- T02/T03 no disponibles: git ls-tree de origin/main no contiene src/partials/navbar.html, src/partials/footer.html, docs/inventario-productos.md ni assets/images/. Sus fichas siguen pendientes. carrito.html conserva el esqueleto de T01, sin las líneas ni los importes.
- Validación documental: comprobación con Node de los 17 enlaces locales de ambas fichas, todos existentes; git diff --name-only HEAD confirma que solo cambian T07/T08, sin cambios en HTML, CSS ni archivos ajenos.
- Comprobación de espacios: git diff --check señaló los CRLF originales como espacios finales; repetida correctamente con git -c core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol diff --check. Formato CRLF original conservado en ambas fichas, sin cambiar la configuración del repositorio.
- No ejecutados build, navegador, validación HTML, pruebas de importes ni PageSpeed: solo cambia planificación y faltan los datos/componentes para implementar. No hay capturas ni aprobación visual nuevas.

## Traspaso y siguiente paso

Planificación preparada para revisar con Lydia; T07 no está completada. Coordinar T02/T03 y la liberación del HTML antes de implementarlo. Solo esta ficha queda a cargo de Lydia para la revisión; no se reserva trabajo de Daniel o Roger. Tras T07 integrada, pasar los datos a [T08](T08-estructura-checkout.md) y la página a D04; sin commit, push, PR ni merge en esta sesión.
