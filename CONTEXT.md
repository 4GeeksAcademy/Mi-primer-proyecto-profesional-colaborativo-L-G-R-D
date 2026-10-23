# Maison RDL — Contexto compartido

Acuerdos estables a 23/10/2026. Requisitos: [matriz](docs/requisitos.md). Ejecución: [plan](PLAN-DE-PROYECTO.md). Instrucciones de sesión: [AGENTS.md](AGENTS.md).

## Acuerdos

- Maison RDL es la marca ficticia de ropa de lujo con sede en Francia.
- Equipo: Roger, Daniel y Lydia; Roger confirma la entrega entre tres.
- Roger dirige y realiza el diseño de las cinco páginas y la optimización.
- Daniel: estructura/contenido de inicio, catálogo y producto; inventario, SEO/Schema.org y preparación técnica.
- Lydia: estructura/contenido de carrito y checkout; QA de cinco vistas, incidencias, evidencias y documentación.
- HTML semántico y Tailwind; sin JavaScript de aplicación, otros frameworks, backend ni pagos reales.
- Cinco HTML: index.html, catalogo.html, producto.html, carrito.html, checkout.html.
- CSS estático generado por Tailwind CLI; T01 documenta el método final. No Play CDN en entrega.
- Navbar/footer compartidos como fragmentos de referencia y copias coordinadas.
- Microdata Organization/Product coherente con el contenido visible.
- Ramas y PR revisadas, commits reales y descriptivos; sin desarrollo directo en main ni force-push.
- PageSpeed mínimo 80 sobre URL pública; objetivo >90; captura real en el repo.
- Controles y datos estáticos. Checkout con tres bloques, sin envío y pago deshabilitado.

## Base visual aceptada para trabajar

Roger acepta la portada actual como buena base. Dirección: lujo editorial cálido, marfil/piedra/oliva, serif Cormorant Garamond y texto Manrope, logo SVG Maison RDL y fotografías cálidas. Inicio con foto a pantalla completa y recortes móvil/escritorio.

Valores y reglas en [docs/diseno.md](docs/diseno.md) y [tokens](src/styles/tokens.css). Esto permite alinear el trabajo; no acredita aprobación final de cada vista ni T02 integrada.

## Coordinación y continuidad

Cada persona actualiza su [ficha](tasks/README.md), con reserva de archivos, estado, comprobaciones y PR. Daniel coordina cambios de acuerdos/memoria mediante PR; no hay que reescribir el contexto al final de cada sesión.

Roger revisa cambios visuales; otro integrante revisa sus PR. Una persona por rama y un responsable activo por archivo. Traspaso al diseño tras integrar la estructura.

TrackFlow aporta prácticas de documentación y memoria, adaptadas en [la referencia](docs/REFERENCIA-TRACKFLOW.md); no aporta stack ni reglas de negocio.

## Pendientes

Fecha/canal de entrega, disponibilidad, usuarios/accesos GitHub, idioma/moneda, inventario definitivo y alojamiento. GitHub Pages es propuesta pendiente de disponibilidad.

Este paquete local se incorporará al repo durante T01. El progreso global se consulta en [memory-bank/progress.md](memory-bank/progress.md); no confundir planificación y preview con entrega.
