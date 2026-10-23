# Maison RDL — Contexto compartido

Acuerdos estables a 23/10/2026. Requisitos: [matriz](docs/requisitos.md). Ejecución: [plan](PLAN-DE-PROYECTO.md). Instrucciones de sesión: [AGENTS.md](AGENTS.md).

## Acuerdos

- Maison RDL es la marca ficticia de ropa de lujo con sede en Francia.
- Implementación: Roger, Daniel y Lydia. Gaby se incorpora exclusivamente como revisora y aprobadora manual de las PR, por decisión de Roger.
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

Roger dirige los cambios visuales; Gaby revisa y aprueba las PR, incluidas las de Roger. Una persona por rama y un responsable activo por archivo. Traspaso al diseño tras integrar la estructura.

TrackFlow aporta prácticas de documentación y memoria, adaptadas en [la referencia](docs/REFERENCIA-TRACKFLOW.md); no aporta stack ni reglas de negocio.

## Pendientes

Fecha/canal de entrega, revisión de Gaby de esta rama, publicación final y PageSpeed sobre URL pública. Idioma español, moneda EUR e inventario de veinte productos ya están definidos; ver inventario y docs/verificacion.md.

T01 y las estructuras ya están incorporadas al repositorio; esta revisión visual y de entrega sigue local. El progreso global se consulta en [memory-bank/progress.md](memory-bank/progress.md); no confundir planificación y preview con entrega.
