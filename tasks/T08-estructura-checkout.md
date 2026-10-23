# T08 — Estructura y contenido de checkout

Proyecto: Maison RDL.
Estado: Implementada y preparada para revisión de Gaby; comprobaciones de navegador pendientes. No integrada ni verificada.
Responsable: Lydia.
Revisora de esta entrega: Gaby (gabrielajara2982); revisión solicitada en la PR #11, todavía pendiente. Roger mantiene la dirección visual y el acabado D05.
Rama: codex/estructura-checkout.
Depende de: T02 y datos de T07.
Archivos de esta entrega: checkout.html, assets/css/styles.css generado por build y esta ficha.
Responsable activo de los archivos: Lydia para checkout.html y esta ficha, por la petición actual tras la integración de las dependencias. Sin cambios de páginas de Daniel, carrito, inventario, estilos fuente, tokens ni fragmentos compartidos.
PR: [#11, abierta hacia main](https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D/pull/11), desde codex/estructura-checkout; revisión solicitada a Gaby, sin aprobación ni merge.

La planificación inicial se conserva como historial en los apartados siguientes. El registro de implementación al final actualiza dependencias, decisiones y comprobaciones, y sustituye los bloqueos y límites de publicación de aquella preparación.

## Instrucciones

Aplicar [el prompt maestro](../PROMPT-MAESTRO.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Crear tres bloques visibles y numerados para datos personales, dirección y tarjeta.
2. Usar form, fieldset, legend, label y tipos/restricciones HTML adecuados.
3. Permitir navegación por anclas sin afirmar que valida campos o cambia un paso activo automáticamente.
4. Mantener el botón de pago deshabilitado y explicar el carácter de demostración; no enviar datos.
5. Comprobar con datos ficticios y preparar la estructura para D05.

## Criterios de cierre

- [ ] Tres bloques completos y accesibles dentro del alcance estático.
- [ ] No hay envío de formulario, cobro ni datos personales en la URL.
- [x] Comprobaciones pertinentes documentadas con evidencia real; navegador pendiente con motivo registrado.
- [ ] PR revisada por otra persona, integrada y resultado verificado.

## Decisiones

Planificación documental del 23/10/2026 junto a T07 en codex/estructura-carrito. No se inicia la implementación de T08 ni se modifica checkout.html; su futura rama seguirá siendo codex/estructura-checkout desde main actualizado, una vez integradas las dependencias.

### Tres bloques de campos previstos

Un formulario semántico con tres fieldset y legend numerados, visibles en una misma página. Cada campo tendrá label persistente asociado a un id único; los placeholders no sustituirán a las etiquetas. Propuesta de campos y restricciones para revisar antes de implementar:

| Bloque | Campos | Tipo y restricciones previstas |
| --- | --- | --- |
| 1. Datos personales | Nombre y apellidos | Dos campos text, obligatorios; admitir espacios, acentos y nombres compuestos sin patrones alfabéticos restrictivos. |
| 1. Datos personales | Correo electrónico | email, obligatorio; no se enviará ninguna confirmación. |
| 1. Datos personales | Teléfono de contacto | tel, opcional; no imponer un patrón nacional sin país acordado. |
| 2. Dirección de entrega | País | select con label; opciones por acordar con el equipo, sin afirmar cobertura de envío. |
| 2. Dirección de entrega | Calle y número | text, obligatorio. |
| 2. Dirección de entrega | Piso, puerta u otra información | text, opcional. |
| 2. Dirección de entrega | Código postal y localidad | Dos campos text, obligatorios; preservar ceros iniciales y no imponer formato postal hasta acordar país. |
| 2. Dirección de entrega | Provincia o región | text; obligatoriedad por decidir según el país de la demostración. |
| 3. Tarjeta de demostración | Titular | text, obligatorio; solo datos ficticios. |
| 3. Tarjeta de demostración | Número de tarjeta | text con inputmode numeric, nunca number; longitud y patrón por concretar para la demo, sin afirmar comprobación bancaria. |
| 3. Tarjeta de demostración | Caducidad | Mes y año con labels propios, mediante select; opciones y restricciones por concretar. Sin prometer comprobación dinámica de vencimiento. |
| 3. Tarjeta de demostración | Código de seguridad | password con inputmode numeric; longitud por concretar para la demo. No aceptar ni pedir datos reales. |

Estas restricciones se comprobarán con datos ficticios al implementar; no implican validación del pedido ni del pago.

### Navegación y seguridad de la demo

- Mantener los tres bloques visibles; anclas opcionales solo desplazan el foco o la vista según el comportamiento nativo, sin validar ni cambiar automáticamente una etapa activa.
- Aviso claro de demostración y de no introducir datos reales. Sin backend, persistencia, JavaScript de aplicación ni servicio de pago.
- Botón final de tipo button y disabled; ningún control de envío. Al implementar, impedir también el envío implícito con Enter mediante un patrón HTML nativo comprobado; no confiar únicamente en omitir action, que no impide un envío.
- Verificar en navegador, con datos ficticios, clic y Enter en los campos: no debe haber envío, petición de formulario ni datos personales en la URL. Mantener pago deshabilitado.
- Navbar, footer, campos, foco y acciones serán los de Roger, usando [guía](../docs/diseno.md) y [tokens](../src/styles/tokens.css), sin estilos alternativos. Vuelta al [carrito](../carrito.html); un resumen, si se incorpora, copiará exactamente los importes documentados en T07.

## Pendiente

- Roger: integrar T02 con navbar/footer, variante de cabecera interna y patrones de campos, foco y estado deshabilitado; coordinar después el diseño en [D05](D05-diseno-checkout.md).
- Daniel y Lydia: disponer de las tres fichas de T03, acordar cantidades y supuesto fiscal, e integrar [T07](T07-estructura-carrito.md). No inventar productos, precios, impuestos ni total de checkout.
- Equipo: confirmar país de demostración y campos condicionados por su dirección, sin inventar condiciones comerciales ni cobertura de envío.
- Daniel/Roger: confirmar liberación de checkout.html, aún reservado en la ficha T01. Lydia no toma ese archivo en esta preparación.
- Después de las dependencias: abrir la tarea de implementación en codex/estructura-checkout; concretar restricciones de tarjeta ficticia, construir el HTML y comprobar semántica, teclado, restricciones nativas, ausencia de envío y responsive. No realizarlo en esta rama.
- No se ha contactado al equipo ni cerrado acuerdos en su nombre; planificación pendiente de revisión con Lydia.

## Comprobaciones y evidencia

23/10/2026:
- Dependencias contrastadas en origin/main (6fb5fa4); evidencia de T01 integrado y de ausencia de los archivos T02/T03 en [T07](T07-estructura-carrito.md). La memoria global conserva estados antiguos y no se reescribe en esta sesión.
- checkout.html leído: esqueleto T01 con tres secciones, todavía sin campos de formulario. T07 no contiene aún productos ni importes implementados. No hay base para completar el checkout.
- Validación documental conjunta con T07: 17 enlaces locales existentes, solo las dos fichas modificadas y ningún HTML/CSS alterado; comprobación de espacios correcta reconociendo los CRLF originales mediante git -c core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol diff --check. Sin cambios de configuración Git.
- No ejecutados build, navegador, validación HTML, pruebas de formulario ni PageSpeed: no se modifica HTML/CSS. La ausencia de envío y el pago deshabilitado son criterios futuros, no pruebas ya superadas.

## Traspaso y siguiente paso

Revisar esta planificación con Lydia; T08 continúa pendiente de implementación en su propia rama tras T02/T07. Solo esta ficha queda a cargo de Lydia para la revisión, sin reservar el HTML. Tras integrar la futura estructura, liberar checkout.html para D05 de Roger. Sin commit, push, PR ni merge en esta sesión.

## Registro de implementación - 23/10/2026

### Dependencias y alcance

- Inicio en main sin cambios locales. `git fetch origin` correcto; rama codex/estructura-checkout creada desde origin/main en 6e54093. No existía previamente local ni remotamente.
- T02 integrada en la PR #4; T07 integrada en la PR #7, merge 712646d, con el commit de carrito 24188df. El inventario y carrito actuales ya fijan los datos necesarios: no se mantienen como pendientes decisiones resueltas.
- Stack real: HTML semántico y utilidades Tailwind 4.3.3 con CSS estático generado. Sin JavaScript, backend, almacenamiento de aplicación ni pagos reales. No se añaden dependencias ni herramientas.
- Se conserva navbar, popovers y footer de Roger sin cambios. Solo se completa el contenido de checkout.html y esta ficha; CSS regenerado con el build existente. No se modifican páginas de Daniel, T07, inventario, tokens, estilos fuente ni fragmentos.

### Estructura y decisiones

- Tres fieldset con legend numerados y visibles: datos personales (nombre, apellidos, email y teléfono opcional), dirección (país, calle/número, información adicional opcional, código postal, localidad y región opcional) y tarjeta ficticia (titular, número, mes, año y código de seguridad).
- Quince campos con labels persistentes e IDs únicos, usando el componente field de Roger. Nombre y apellidos admiten acentos y espacios sin patrones alfabéticos; teléfono sin patrón nacional. Código postal de tipo text para conservar ceros iniciales.
- País como texto libre en vez del select previsto: no requiere inventar un país de demostración ni una lista de destinos comerciales. Provincia/región opcional y sin formato postal nacional. Se advierte que la dirección es ficticia y no representa cobertura de envío.
- Número de tarjeta de tipo text e inputmode numeric, exactamente 16 dígitos ficticios, sin comprobación bancaria. Código de seguridad password, tres o cuatro dígitos ficticios. Selects de caducidad con meses 01-12 y años 2026-2036, sin validación dinámica de vencimiento. No se introducen ni precargan datos reales.
- Formulario con method="dialog", sin action, autocomplete="off" y sin atributos name serializables. Se usa un único botón type="submit" deshabilitado, en lugar del type="button" previsto, para que el botón de envío predeterminado bloqueado impida también el envío implícito. method="dialog" añade una defensa nativa: fuera de un dialog no produce navegación ni envío de formulario. Esta propiedad se revisa en el HTML; clic y Enter en navegador siguen pendientes de prueba.
- Aviso de demo y de no introducir datos reales antes de los campos; aviso específico de tarjeta y botón final "Pago no disponible" siempre disabled. No se promete validación al pulsar el botón deshabilitado, envío, pedido, persistencia ni confirmación.
- Layout de una columna por defecto, campos en dos columnas desde sm cuando procede y resumen lateral desde lg. min-w-0 en formulario, fieldsets y celdas; componentes de Roger sin nuevos estilos fuente. Acabado visual final para D05.

### Coherencia con T07 integrado

| Referencia | Producto | Talla | Cantidad | Importe incluido |
| --- | --- | --- | --- | --- |
| MRDL-CAM-001 | Camisa de seda marfil | M | 1 | 240,00 EUR |
| MRDL-PAN-001 | Pantalón ancho de pinzas taupe | 38 | 1 | 295,00 EUR |
| MRDL-CAL-001 | Mocasín de piel espresso | 42 | 1 | 390,00 EUR |

Resumen idéntico al carrito: subtotal sin impuestos 770,83 EUR, impuesto de simulación del 20 % incluido 154,17 EUR y total 925,00 EUR. Cálculo: 240 + 295 + 390 = 925; 925 / 1,20 redondeado a céntimos = 770,83; 925 - 770,83 = 154,17. No se suman otra vez impuestos ni se añaden portes, descuentos u otros cargos. Imágenes, textos alternativos y referencias coinciden con T07. Se indica que la selección es estática, sin transferencia ni recálculo automático.

### Comprobaciones realizadas

| Comprobación | Resultado y límite |
| --- | --- |
| `npm run build` | Correcto con Tailwind 4.3.3; CSS regenerado tras completar checkout |
| HTMLParser estándar ejecutado desde terminal, sin archivo de test | Tres fieldset/legend, 15 campos etiquetados, IDs únicos, referencias aria/for/popover resueltas y anidamiento comprobado; un header/main/footer/h1/form |
| Restricciones y seguridad por inspección del HTML | Tipos, required/opcionales y patrones presentes; método dialog, sin action ni names, autocomplete off, único submit disabled y sin scripts ni eventos de aplicación. No equivale a pruebas interactivas de validación o ausencia de envío |
| Navegación y recursos locales | 30 enlaces/anclas y cinco recursos HTML con destinos existentes; imágenes con alt y dimensiones; vuelta al carrito disponible |
| Comparación con T07 y Decimal/ROUND_HALF_UP | Tres referencias, nombres, tallas, cantidades y precios coincidentes; resumen 770,83 + 154,17 = 925,00 EUR correcto con impuesto incluido |
| Componentes compartidos | Comparación con HEAD confirma navbar, popovers y footer intactos |
| Adaptación básica por inspección estática | Rejillas sm/lg presentes en HTML y CSS compilado; no acredita renderizado, ausencia de overflow ni comportamiento del foco |
| Diagnósticos del editor | Sin errores notificados en checkout.html; no sustituye validación HTML completa |

El primer control estático se detuvo por una expectativa incorrecta del comprobador (16 campos en vez de los 15 previstos). Se corrigió solo el contador, sin modificar HTML por ese resultado; la repetición completó las comprobaciones anteriores correctamente. No se añaden tests al repositorio.

### Pendientes y traspaso

- Navegador: no hay ejecutable Chromium/Chrome/Firefox ni paquete Playwright/Puppeteer disponible en esta sesión. No se instalan herramientas ni se reparan bibliotecas. No hay capturas, pruebas interactivas, validación HTML externa ni PageSpeed nuevos.
- Probar con datos exclusivamente ficticios a 375, 768 y 1440 px: renderizado de fuentes/imágenes, legibilidad, overflow, orden de teclado, foco, labels, controles nativos y menú/popovers compartidos. Esos tamaños son pendientes, no medidas ejecutadas.
- Comprobar clic en el botón deshabilitado y Enter en campos: no debe haber envío ni datos en URL; comprobar restricciones nativas con datos ficticios sin afirmar validación bancaria o de vencimiento.
- Gaby: revisar la PR, sin aprobación atribuida. Roger mantiene revisión visual y acabado en [D05](D05-diseno-checkout.md). Tras integrar T08 con revisión ajena, liberar checkout.html para D05.
- No marcar T08 integrada ni verificada. Commit, push y PR se realizan por la autorización actual de Lydia; no se fusiona la rama.

### Publicación para revisión

Commit de implementación 43598fe: `feat: completar checkout de demostración (T08)`, con checkout.html, CSS generado y esta ficha. Rama publicada en origin/codex/estructura-checkout.

[PR #11](https://github.com/4GeeksAcademy/Mi-primer-proyecto-profesional-colaborativo-L-G-R-D/pull/11) creada abierta, no draft, contra main. GitHub confirma solicitud de revisión a gabrielajara2982 (nombre público Gaby Jara). Sin revisión aprobada ni integración. La descripción incluye requisitos, resultados de las comprobaciones y pendientes concretos de navegador y diseño D05.

Control previo a publicación: nueve enlaces locales de la ficha con destino existente, CRLF y planificación histórica conservados; `git diff --check` y comprobación del staging correctos reconociendo CRLF. Rama al día con origin/main antes del commit (0/0). Solo checkout, CSS generado y T08 modificados. Este registro de publicación se incorpora mediante un commit documental posterior; no requiere repetir el build porque no modifica HTML ni CSS.
