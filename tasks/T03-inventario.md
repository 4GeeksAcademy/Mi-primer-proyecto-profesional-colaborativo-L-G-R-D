# T03 — Inventario y recursos

Proyecto: Maison RDL.
Estado: En curso.
Responsable: Daniel.
Revisor: Lydia; Roger para selección visual.
Revisora de esta entrega: Gaby (revisión y aprobación de la PR; no implementa cambios). Revisión pendiente.
Rama: codex/inventario (creada desde origin/main dae031c el 23/10/2026).
Depende de: T01; coordinar identidad con T02.
Archivos previstos: docs/inventario-productos.md, docs/fuentes-imagenes.md, assets/images/.
Responsable activo de los archivos: Daniel, para docs/inventario-productos.md, docs/fuentes-imagenes.md y esta ficha mientras dure T03. La sección de importes del inventario se completa con Lydia (T07).
PR: pendiente.

## Instrucciones

Aplicar [el prompt maestro](../PROMPT-MAESTRO.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Entregar pronto tres productos completos para que Lydia arranque carrito y checkout.
2. Completar veinte productos con referencia, categoría, talla, precio, moneda, imagen y descripción.
3. Representar calzado, camisas, pantalones y accesorios.
4. Registrar origen y permiso de uso de imágenes locales. Roger coordina su tratamiento y optimización.
5. Acordar con Lydia cantidades e importes de demostración y documentar el supuesto de impuestos.

## Criterios de cierre

- [ ] Inventario completo y tres productos de carrito sin datos contradictorios.
- [ ] Imágenes utilizables, identificadas y documentadas.
- [ ] Comprobaciones pertinentes documentadas con evidencia real.
- [ ] PR revisada por otra persona, integrada y resultado verificado.

## Decisiones

Sesión del 23/10/2026 en codex/inventario. Solo documentación: no se modifican HTML, CSS, tokens, componentes ni fichas de Lydia, y no se ejecuta el build porque ningún archivo modificado lo requiere.

- [Inventario](../docs/inventario-productos.md) con veinte productos ficticios, cinco por categoría (camisas, pantalones, calzado y accesorios). Referencias `MRDL-<CAM|PAN|CAL|ACC>-<número>`.
- Tres productos propuestos para el carrito, todos con imagen propia de muestra: MRDL-CAM-001, MRDL-PAN-001 y MRDL-CAL-001.
- Las cuatro imágenes de producto existentes se asignan a los productos -001 de cada categoría; sus descripciones se redactaron a partir de lo que muestra cada foto. Los dieciséis restantes quedan con imagen pendiente y ruta prevista que todavía no existe. Correspondencia y procedencia en [fuentes de imágenes](../docs/fuentes-imagenes.md).
- Moneda: se usa el euro como **propuesta**, no como acuerdo. Idioma: español, provisional como en T01. Ambos siguen pendientes en CONTEXT.md.
- No se fija tratamiento de impuestos, porcentaje, cantidades ni talla de las líneas del carrito: quedan pendientes de coordinar con Lydia en la sección «Supuesto de importes» del inventario.

## Pendiente

- Lydia: acordar cantidades, talla de cada línea, inclusión o no de impuestos, porcentaje del supuesto de simulación (si se aplica), precisión y redondeo; anotarlos en el inventario.
- Equipo: confirmar idioma y moneda. Si la moneda no es el euro, actualizar todos los precios en un mismo cambio.
- Roger: decidir cómo obtener las dieciséis imágenes pendientes y si se usan imágenes provisionales mientras tanto; revisar la selección visual de las cuatro asignadas. No descargar imágenes sin permiso comprobado.
- Gaby: revisar y aprobar la PR. Commit y push realizados el 23/10/2026 a petición de Daniel para abrir la PR; revisión pendiente, sin aprobación atribuida.
- Criterios de cierre sin marcar: el inventario no está cerrado mientras falten imágenes, el supuesto de importes y la revisión.

## Comprobaciones y evidencia

23/10/2026, rama codex/inventario creada desde origin/main (dae031c), sin cambios locales previos; git fetch origin correcto.
- Script de comprobación (Python, ejecutado desde el terminal, no añadido al repositorio) sobre docs/inventario-productos.md: 20 filas y 20 referencias únicas; 5 productos por cada una de las cuatro categorías; 20 fichas con categoría, descripción, materiales, uso recomendado, tallas, precio, imagen y texto alternativo; nombre, categoría, tallas y precio idénticos entre el resumen y las fichas; los tres productos del carrito coinciden con sus fichas; precios en formato `NNN €`, entre 140 € y 690 €. 0 errores.
- Imágenes: las cuatro rutas marcadas como propias existen; ninguna ruta pendiente existe. Las seis imágenes de assets/images son idénticas a las de docs/referencia-visual (cmp). Dimensiones con `file`: productos 850 × 1133, hero 1122 × 1402 y 1672 × 940. Las cuatro fotos de producto se revisaron visualmente para redactar descripción y texto alternativo.
- Enlaces relativos y anclas de inventario-productos.md, fuentes-imagenes.md y esta ficha: todos existen.
- No ejecutados: build (no cambian clases ni HTML), navegador y validación HTML (no cambia ninguna página).

## Traspaso y siguiente paso

PR presentada por Daniel; Gaby la revisa. Una vez integrada: T07 (Lydia) usa los tres productos del carrito cuando se acuerde el supuesto de importes; T04 y T06 pueden usar el inventario; T05 necesita las imágenes pendientes o la decisión de Roger sobre las provisionales. Liberar entonces la reserva de los archivos de T03, salvo la sección de importes, que se completa con Lydia.
