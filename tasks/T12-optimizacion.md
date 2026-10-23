> Estado vigente: evidencia final de rendimiento seleccionada por Roger, Lighthouse 100 escritorio y 97 móvil. Se conserva la procedencia Codespaces; PageSpeed Insights devolvió 429. Revisión de la actualización en PR #14 pendiente de Gaby.

# T12 — Optimización y PageSpeed

Proyecto: Maison RDL.
Estado: Evidencia final preparada por decisión de Roger; revisión e integración en PR #14 pendientes.
Responsable: Roger.
Revisor: Gaby (revisión y aprobación manual).
Rama: codex/optimizacion.
Depende de: T11 con URL pública.
Archivos previstos: Imágenes, estilos fuente y CSS generado, cinco HTML cuando proceda, memory-bank/verificacion.md y ficha propia.
Responsable activo de los archivos: sin reserva todavía.
PR: pendiente.

## Instrucciones

Aplicar [el prompt maestro](../AGENTS.md) y [el plan vigente](../PLAN-DE-PROYECTO.md).
1. Medir la versión pública y priorizar problemas observados.
2. Optimizar imágenes, dimensiones, CSS y tipografía conservando contenido y diseño.
3. No cargar de forma diferida la imagen principal si perjudica su aparición inicial; reservar lazy loading para imágenes fuera de la primera pantalla.
4. Mantener solo HTML y Tailwind, con CSS estático generado y sin CDN de compilación final.
5. Integrar, publicar de nuevo y volver a medir la versión corregida: mínimo 80, objetivo superior a 90.

## Criterios de cierre

- [ ] Puntuación mínima alcanzada y medición reproducible documentada.
- [ ] Roger revisó la coherencia visual de las cinco vistas después de optimizar.
- [ ] Comprobaciones pertinentes documentadas con evidencia real.
- [ ] PR revisada por otra persona, integrada y resultado verificado.

## Decisiones

Sin decisiones adicionales registradas. Respetar Maison RDL y la responsabilidad de Roger sobre diseño y optimización.

## Pendiente

Toda la tarea. Comprobar dependencias y coordinar archivos antes de empezar.

## Comprobaciones y evidencia

Pendiente. Registrar qué se probó, URL/archivo, tamaño de pantalla si aplica, fecha y resultado. No inventar capturas ni aprobaciones.

## Traspaso y siguiente paso

Pendiente. Al terminar, indicar qué tarea recibe el resultado y liberar la reserva del archivo.

## Actualización de Roger — 23/10/2026

Preparación autorizada en `codex/imagenes-revision-visual`; resultados y límites en [verificación](../memory-bank/verificacion.md). No se marca integrada ni entregada. Gaby revisa manualmente. PageSpeed y publicación final siguen pendientes cuando sean aplicables.

## Evidencia final elegida por Roger

**Evidencia final de rendimiento elegida por Roger:** Chrome DevTools Lighthouse en Codespaces, **100 en escritorio y 97 en móvil**. Capturas originales incluidas; no se presentan como informes de la web de PageSpeed Insights. Ese servicio devolvió HTTP 429. La equivalencia con el requisito específico del enunciado corresponde a la evaluación del instructor; no se atribuye una aceptación que no se ha recibido. Capturas enlazadas desde README y memory-bank/verificacion.md.
