# T07 — Estructura y contenido de carrito

Proyecto: Maison RDL.
Estado: Estructura e importes preparados para revisión de Gaby; revisión visual pendiente. No integrada ni verificada.
Responsable: Lydia.
Revisora de esta entrega: Gaby; revisión pendiente. Roger mantiene la dirección del diseño y la revisión visual para D04.
Rama: codex/estructura-carrito.
Depende de: T02 y tres productos de T03.
Archivos de esta entrega: carrito.html, supuesto de demostración y acuerdos relacionados en docs/inventario-productos.md, y esta ficha; assets/css/styles.css regenerado exclusivamente con el build.
Responsable activo de los archivos: Lydia, para carrito.html y esta ficha; actualización acotada del supuesto del inventario autorizada por Lydia para coordinación con Daniel, que mantiene su responsabilidad. Sin cambios de tokens, estilos fuente, fragmentos o páginas ajenas.
PR: no creada; sin commit, push ni integración por indicación de Lydia.

La planificación previa y el registro de implementación parcial se conservan como historial, incluidos sus bloqueos y comprobaciones. El registro de cierre de importes al final actualiza el estado con las confirmaciones posteriores de Lydia; no modifica la planificación de T08 ni atribuye aprobaciones al equipo.

## Instrucciones

Aplicar [el prompt maestro](../PROMPT-MAESTRO.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Crear página completa del carrito con tres productos compartidos.
2. Mostrar miniatura, precio unitario, cantidad y total por línea.
3. Calcular y comprobar manualmente subtotal, impuestos y total conforme al supuesto documentado.
4. Añadir Comprar hacia checkout y navegación de vuelta.
5. Indicar que los datos son estáticos; coordinar con Roger la composición para D04.

## Criterios de cierre

- [x] Importes comprobados y sin doble contabilización de impuestos.
- [x] Carrito completo y enlazado, sin panel lateral ni cálculos dinámicos prometidos.
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

## Registro de implementación parcial - 23/10/2026

### Rama y dependencias comprobadas

- Inicio en main sin cambios locales. `git fetch origin` correcto; main y origin/main en f2c8b10, merge de la PR #6 del inventario.
- Reutilizada codex/estructura-carrito, en 00a36b4 y alineada con su rama remota. Actualización mediante `git merge --ff-only origin/main` hasta f2c8b10, sin conflictos ni commits nuevos. Se conserva la planificación T07/T08 ya integrada.
- T02 disponible en main mediante la PR #4: cabecera interna, footer, componentes, tokens, fuentes y recursos locales. Su integración no acredita la verificación de navegador pendiente.
- Los tres productos necesarios de T03 están integrados y disponibles en el inventario común, con imágenes propias de muestra: MRDL-CAM-001, MRDL-PAN-001 y MRDL-CAL-001. Aunque el documento aún dice borrador no integrado, su presencia en origin/main se confirma por el merge de la PR #6. Esto no cierra el inventario completo ni sus acuerdos pendientes.

### Archivos y decisiones de esta entrega

- [carrito.html](../carrito.html): página completa con tres líneas, miniatura local y alt del inventario, nombre, referencia, tallas disponibles, precio unitario propuesto, campos de cantidad y total de línea, resumen y enlace Comprar a checkout.html. Navegación de vuelta al catálogo y aviso de demostración sin persistencia ni recálculo automático.
- Precios copiados sin alterarlos: camisa 240 EUR, pantalón 295 EUR y mocasín 390 EUR; EUR sigue siendo propuesta del inventario, no acuerdo nuevo. No se elige talla ni cantidad en nombre del equipo.
- Cantidad, talla elegida, totales de línea, subtotal, impuestos y total quedan explícitamente pendientes donde corresponde. No se muestran ceros ni importes ficticios como si estuvieran confirmados. Las tallas disponibles no equivalen a una selección.
- Resumen preparado para subtotal sin impuestos + impuestos = total. Si el precio incluye impuestos, se desglosan sin volver a sumarlos; si no los incluye, se añaden una sola vez. Sin porcentaje supuesto, portes, descuentos ni cargos nuevos.
- Se reutiliza el esquema responsive de Roger: productos y resumen apilados por defecto, dos columnas desde lg, miniaturas de ancho estable y columnas de texto con minmax(0,1fr). Sin acabado D04 ni estilos alternativos.
- Navbar, popovers y footer conservados; tokens, entrada CSS, fragmentos, inventario y páginas de Daniel intactos. [checkout.html](../checkout.html) y [T08](T08-estructura-checkout.md) no se implementan ni modifican.
- assets/css/styles.css se regenera con el comando existente; no se edita a mano ni se añaden dependencias, herramientas o archivos de tests.

### Comprobaciones realizadas en esta sesión

| Comprobación | Resultado y límite |
| --- | --- |
| `npm run build` | Correcto con Tailwind 4.3.3; CSS estático regenerado para las clases del carrito |
| Parser estándar HTMLParser ejecutado desde terminal, sin archivo de test | 31 enlaces/anclas y cinco recursos HTML con destinos existentes; IDs únicos, referencias aria/for/popover resueltas, imágenes con alt y dimensiones, un header/main/footer/h1; sin formularios, scripts ni eventos de aplicación |
| Coherencia con T03 | Tres líneas con referencias, nombres, precios, rutas de imagen y alt coincidentes con sus fichas del inventario; cantidades y totales no acordados señalados como pendientes |
| Conservación de componentes | Comparación con HEAD confirma navbar, popovers y footer intactos |
| Adaptación básica por inspección estática | Rejillas móvil/escritorio presentes en HTML y CSS compilado; no acredita renderizado, recortes, ausencia de overflow, teclado o foco |
| Diagnósticos del editor para carrito.html | Sin errores notificados; no equivale a validación HTML completa |

No se pueden ejecutar las tres multiplicaciones ni conciliar el resumen hasta confirmar cantidades, modalidad fiscal, moneda, precisión y redondeo. Las fórmulas previstas no constituyen una comprobación numérica de importes finales.

No se realizaron pruebas visuales en móvil/escritorio, capturas, interacción, validación HTML externa ni PageSpeed. No hay ejecutable Chromium, Chrome o Firefox disponible en el PATH ni herramienta de navegador accesible en esta sesión; no se instala ni repara ninguna herramienta. Queda pendiente revisar renderizado a 375, 768 y 1440 px, navegación por teclado, foco, imágenes y overflow en un navegador disponible.

### Pendientes concretos y revisión

1. Lydia y Daniel: confirmar una cantidad entera positiva y una talla de las disponibles para cada referencia; confirmar si los precios incluyen impuestos, el tipo del supuesto de simulación si procede, precisión en céntimos y regla de redondeo.
2. Equipo: confirmar moneda (EUR propuesta) e idioma (español provisional). Registrar el acuerdo en la fuente común con Daniel; el inventario no se modifica unilateralmente en esta entrega.
3. Tras el acuerdo: sustituir los pendientes, comprobar precio por cantidad en las tres líneas y conciliar subtotal sin impuestos + impuestos = total, sin doble contabilización. El criterio de importes sigue sin marcar.
4. Gaby: revisar esta entrega parcial; no se atribuye revisión ni aprobación. Roger mantiene la dirección visual y recibe el acabado final en [D04](D04-diseno-carrito.md), tras la integración de estructura que corresponda.
5. Completar la revisión de navegador pendiente. T07 permanece en curso, no integrada ni verificada; no se marca ningún criterio de cierre adicional.

Entrega local preparada para revisión con los bloqueos anteriores visibles. Sin commit, push, PR ni merge a main; el único avance Git fue actualizar linealmente la rama de trabajo desde origin/main. T08 se conserva para una tarea posterior.

## Cierre de importes de demostración - 23/10/2026

Este registro sustituye los pendientes de datos e importes de la implementación parcial anterior. Lydia confirma español, EUR, una unidad por producto, tallas elegidas entre las disponibles, precios originales y un impuesto de simulación del 20 % incluido. No representa una implementación fiscal real.

### Datos aplicados y cálculo

| Referencia | Talla | Precio unitario con impuesto incluido | Cantidad | Total de línea |
| --- | --- | --- | --- | --- |
| MRDL-CAM-001 | M | 240,00 € | 1 | 240,00 € |
| MRDL-PAN-001 | 38 | 295,00 € | 1 | 295,00 € |
| MRDL-CAL-001 | 42 | 390,00 € | 1 | 390,00 € |

- Total con impuestos incluidos: 240,00 + 295,00 + 390,00 = 925,00 €.
- Subtotal sin impuestos: 925,00 / 1,20 = 770,8333...; redondeado al céntimo más próximo, con mitades hacia arriba, resulta 770,83 €.
- Impuestos incluidos por diferencia: 925,00 - 770,83 = 154,17 €.
- Conciliación: 770,83 + 154,17 = 925,00 €. El impuesto no se vuelve a sumar al total.

### Archivos y coordinación

- [Inventario común](../docs/inventario-productos.md): actualizado el supuesto de importes y las filas relacionadas de acuerdos. Se registra la confirmación de Lydia para coordinación y revisión de Daniel, responsable del documento; no se atribuye aprobación ni contacto realizado con Daniel. No se cambian las fichas de producto ni sus precios.
- [carrito.html](../carrito.html): sustituidos todos los pendientes por los datos indicados, con dos decimales y aviso explícito del impuesto de simulación incluido. Se mantienen navegación, componentes de Roger y alcance estático, sin persistencia ni recálculo automático.
- assets/css/styles.css regenerado únicamente mediante el build. T08, checkout, páginas de Daniel, tokens, estilos fuente y fragmentos compartidos sin cambios.

### Comprobaciones de esta actualización

- Parser estándar HTMLParser y Decimal con ROUND_HALF_UP, ejecutados desde terminal sin crear archivos de test: las tres tallas pertenecen a las disponibles en las fichas; las cantidades son 1; cada precio coincide con el inventario y precio por cantidad coincide con el total de línea. Subtotal, impuesto y total del HTML coinciden exactamente con 770,83 €, 154,17 € y 925,00 €. Conciliación correcta, sin doble contabilización.
- `npm run build`: correcto con Tailwind 4.3.3 en esta actualización.
- Diagnósticos del editor: sin errores notificados en carrito.html, inventario y ficha T07; no equivale a validación HTML completa ni revisión visual.
- No se han añadido funcionalidades, dependencias ni herramientas. No se repiten ni se atribuyen nuevas pruebas de navegador, capturas o PageSpeed; las comprobaciones visuales siguen pendientes por la limitación del entorno ya registrada.

### Estado para revisión

Estructura e importes completos para revisión de Gaby, todavía no realizada. No quedan cantidades, tallas ni importes pendientes de definición para esta demostración. Daniel debe revisar el registro del supuesto en la fuente común; Roger conserva la dirección del diseño y el acabado D04. La revisión de navegador sigue pendiente. T07 no está integrada ni verificada; no se marca el criterio de cierre conjunto de PR/integración/verificación.

Sin commit, push, PR ni merge en esta actualización. No se inicia T08.
