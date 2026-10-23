# Lydia — Tus primeras tareas

Leer primero [LEEME-PRIMERO](LEEME-PRIMERO.md). Referencia completa: [plan](PLAN-DE-PROYECTO.md), [requisitos](docs/requisitos.md), [guía visual](docs/diseno.md) y [fichas](tasks/README.md).

## Puedes preparar ahora

1. Ayudar a comprobar el acceso común como revisora de [T00](tasks/T00-accesos.md).
2. Definir el contenido del carrito: miniatura, nombre, precio unitario, cantidad y total por línea; subtotal, impuestos, total y acceso al checkout.
3. Organizar campos del checkout: datos personales, dirección y tarjeta, con labels persistentes y tres bloques numerados.
4. Coordinar con Daniel los tres productos y cantidades del carrito. No fijar precios distintos a su inventario ni un porcentaje fiscal como si lo exigiera el enunciado.

Preparar contenido no requiere cerrar todavía la maquetación. Las páginas dependen de la base visual compartida y de los datos indicados en sus fichas.

## Al disponer de las dependencias

- [T07: carrito](tasks/T07-estructura-carrito.md), rama codex/estructura-carrito: tres productos e importes coherentes, página completa y Comprar enlazado a checkout.
- [T08: checkout](tasks/T08-estructura-checkout.md), rama codex/estructura-checkout: tres bloques visibles, HTML semántico y navbar/footer comunes. Datos ficticios para pruebas, sin envío de información y con pago deshabilitado.

Una rama y una PR por tarea. Tras revisar e integrar la estructura, liberar el archivo para que Roger aplique el diseño. Mantener paleta, fuentes, controles y espaciados de la guía; proponer ajustes visuales a Roger.

## Responsabilidades posteriores

Coordinar [QA de las cinco vistas](tasks/T10-qa.md), [evidencias](tasks/T13-evidencias.md) y [documentación de entrega](tasks/T14-entrega.md). Cada autor corrige sus incidencias y aporta su información al README; no debes rehacer el trabajo de los demás.

Actualizar tu ficha con estado, reserva de archivos, resultados reales y pendientes. Las capturas de la referencia visual no sustituyen a las evidencias finales del proyecto.
