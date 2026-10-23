# T02 — Guía visual y elementos compartidos

Proyecto: Maison RDL.
Estado: Pendiente.
Responsable: Roger.
Revisor: Daniel.
Rama: codex/base-visual.
Depende de: T01.
Archivos previstos: docs/diseno.md, src/styles/tokens.css, src/styles/input.css, src/partials/navbar.html, src/partials/footer.html, cinco esqueletos y CSS generado.
Responsable activo de los archivos: sin reserva todavía.
PR: pendiente.

## Instrucciones

Partir de la [guía visual v0.1](../docs/diseno.md) y los [tokens compartidos](../src/styles/tokens.css). Roger ha aceptado la portada como buena base de trabajo. Conservar esa dirección; las otras cuatro vistas requieren su diseño y revisión.

Ya existe una [primera propuesta HTML del inicio](../docs/referencia-visual/index.html) con hero a pantalla completa, imágenes para móvil/escritorio y una [lámina del logo](../docs/referencia-visual/identidad.html). Trasladar recursos y patrones de esa referencia al integrar T02. Adaptar enlaces a las cinco páginas reales y retirar la dependencia documental de la carpeta local de preview. No dar la tarea por completada por disponer de esa vista previa.

Aplicar [el prompt maestro](../PROMPT-MAESTRO.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Integrar la identidad documentada de Maison RDL y preparar composiciones de las cinco vistas, variantes de cabecera y reglas responsive. Usar utilidades Tailwind para layout/estados, sin trasladar todo el ejercicio a CSS manual.
2. Preparar navbar con logo, búsqueda y cuenta; footer con categorías, legal, marca y contacto.
3. Definir tarjetas, campos, botones, enlaces, foco y navegación móvil sin JavaScript.
4. Aplicar los elementos compartidos a los esqueletos y regenerar CSS.
5. Registrar cambios de identidad en guía/tokens dentro de la misma PR. El hero a pantalla completa es solo de inicio; las páginas internas usan cabecera clara en flujo normal.

## Criterios de cierre

- [ ] Existe guía concreta que Daniel y Lydia pueden seguir.
- [ ] Navbar/footer y controles de referencia funcionan dentro del alcance estático y se revisan en móvil y escritorio.
- [ ] Cada enlace tiene destino o un pendiente explícito que deba cerrarse antes de QA.
- [ ] Comprobaciones pertinentes documentadas con evidencia real.
- [ ] PR revisada por otra persona, integrada y resultado verificado.

## Decisiones

Sin decisiones adicionales registradas. Respetar Maison RDL y la responsabilidad de Roger sobre diseño y optimización.

## Pendiente

Integración completa en el repo, composiciones internas, componentes comunes y PR. La guía/tokens ya están preparados localmente, pero eso no cierra la tarea. Comprobar dependencias y coordinar archivos.

## Comprobaciones y evidencia

Pendiente. Registrar qué se probó, URL/archivo, tamaño de pantalla si aplica, fecha y resultado. No inventar capturas ni aprobaciones.

## Traspaso y siguiente paso

Pendiente. Al terminar, indicar qué tarea recibe el resultado y liberar la reserva del archivo.
