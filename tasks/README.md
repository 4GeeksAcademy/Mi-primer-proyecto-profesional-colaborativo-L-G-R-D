# Maison RDL — Índice de tareas

Estado inicial: todas pendientes. Este directorio contiene fichas preparadas, no evidencia de ejecución.
Referencia: [Plan vigente](../PLAN-DE-PROYECTO.md). Inicio de sesión: [Prompt maestro](../PROMPT-MAESTRO.md).

| ID | Tarea | Responsable | Revisor | Dependencias |
| --- | --- | --- | --- | --- |
| [T00](T00-accesos.md) | Accesos y coordinación | Daniel | Lydia | Ninguna |
| [T01](T01-setup.md) | Setup y método de Tailwind | Daniel | Roger | T00 |
| [T02](T02-base-visual.md) | Guía visual y elementos compartidos | Roger | Daniel | T01 |
| [T03](T03-inventario.md) | Inventario y recursos | Daniel | Lydia; Roger para selección visual | T01; coordinar identidad con T02 |
| [T04](T04-estructura-home.md) | Estructura y contenido de inicio | Daniel | Lydia; Roger si afecta a la composición | T02 y primera versión T03 |
| [T05](T05-estructura-catalogo.md) | Estructura y contenido de catálogo | Daniel | Lydia; Roger si afecta a la composición | T02 y T03 completo |
| [T06](T06-estructura-producto.md) | Estructura y contenido de producto | Daniel | Lydia; Roger si afecta a la composición | T02 y primera versión T03 |
| [T07](T07-estructura-carrito.md) | Estructura y contenido de carrito | Lydia | Daniel; Roger si afecta a la composición | T02 y tres productos de T03 |
| [T08](T08-estructura-checkout.md) | Estructura y contenido de checkout | Lydia | Daniel; Roger si afecta a la composición | T02 y datos de T07 |
| [T09](T09-seo-schema.md) | SEO y Schema.org | Daniel | Lydia; Roger para cambios visuales | T04–T08 y D01–D05 integrados |
| [T10](T10-qa.md) | QA de las cinco vistas | Lydia | Daniel; Roger para la revisión visual | T09 |
| [T11](T11-publicacion.md) | Publicación de prueba | Daniel | Lydia | T10 sin incidencias bloqueantes |
| [T12](T12-optimizacion.md) | Optimización y PageSpeed | Roger | Daniel | T11 con URL pública |
| [T13](T13-evidencias.md) | Regresión final y evidencias | Lydia | Daniel; Roger confirma diseño y rendimiento | T12 integrado y publicado |
| [T14](T14-entrega.md) | Entrega documentada | Lydia; aportaciones de Roger y Daniel | Daniel y Roger | T13 |
| [D01](D01-diseno-home.md) | Diseño de inicio | Roger | Lydia | T04 integrado |
| [D02](D02-diseno-catalogo.md) | Diseño de catálogo | Roger | Daniel | T05 integrado |
| [D03](D03-diseno-producto.md) | Diseño de producto | Roger | Daniel | T06 integrado |
| [D04](D04-diseno-carrito.md) | Diseño de carrito | Roger | Lydia | T07 integrado |
| [D05](D05-diseno-checkout.md) | Diseño de checkout | Roger | Lydia | T08 integrado |

Los diseños D01–D05 se pueden iniciar de forma escalonada en cuanto su estructura esté integrada.
Los estados son Pendiente → En curso → En revisión → Integrada → Verificada.
Estado Bloqueada por dependencia solo describe un impedimento real y su detalle; no equivale a tarea completada.
Cambiar el responsable activo de un archivo requiere coordinación. El responsable de cada ficha actualiza su progreso.
