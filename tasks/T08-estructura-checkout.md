# T08 — Estructura y contenido de checkout

Proyecto: Maison RDL.
Estado: Pendiente de implementación (planificación preparada; bloqueada por T02 y datos de T07).
Responsable: Lydia.
Revisor: Daniel; Roger si afecta a la composición.
Rama: codex/estructura-checkout.
Depende de: T02 y datos de T07.
Archivos previstos: checkout.html y ficha propia.
Responsable activo de los archivos: Lydia, solo esta ficha durante la preparación; checkout.html no reservado por Lydia. Respetar la reserva de T01 hasta coordinar su liberación.
PR: no creada; sin commit, push ni integración por indicación de Lydia.

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
- [ ] Comprobaciones pertinentes documentadas con evidencia real.
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
