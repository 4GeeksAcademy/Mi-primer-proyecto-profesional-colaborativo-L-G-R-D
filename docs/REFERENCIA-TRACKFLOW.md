# Adaptación de buenas prácticas de TrackFlow

Consulta: 23/10/2026. Repositorio de referencia: [ai-engineering-trackflow](https://github.com/rogerdevmtz/ai-engineering-trackflow), rama main.

Se revisaron AGENTS.md, CONTEXT.es.md, memory-bank/projectbrief.md, techContext.md, progress.md, .agents/rules/visual-identity.md y .agents/skills/update-project-memory/SKILL.md. CONTEXT.es.md contiene un placeholder: no debe tomarse como briefing vigente. Se reutiliza el enfoque organizativo, no datos o requisitos de TrackFlow.

| Práctica observada | Adaptación para Maison RDL |
| --- | --- |
| Lectura inicial y reglas en AGENTS.md | Orden de lectura, alcance HTML/Tailwind y reparto de tres integrantes |
| Contexto estable separado del progreso | CONTEXT.md conserva acuerdos; cada ficha recoge trabajo diario |
| Memoria de alcance, técnica y progreso | memory-bank enlaza fuentes canónicas y registra hechos, sin copiar la guía visual |
| Regla visual y tokens comunes | .agents/rules/visual-identity.md remite a docs/diseno.md y src/styles/tokens.css |
| Verificación antes de commit | Revisión de diff, comprobaciones pertinentes y evidencia honesta |
| Mantenimiento de memoria al cambiar hechos | Procedimiento en AGENTS y memory-bank/README; coordinación de Daniel para evitar conflictos |

Fuentes directas: [AGENTS](https://github.com/rogerdevmtz/ai-engineering-trackflow/blob/main/AGENTS.md), [contexto técnico](https://github.com/rogerdevmtz/ai-engineering-trackflow/blob/main/memory-bank/techContext.md), [regla visual](https://github.com/rogerdevmtz/ai-engineering-trackflow/blob/main/.agents/rules/visual-identity.md).

## Qué cambia por tratarse de otro proyecto

Maison RDL es una tienda estática de cinco vistas. No se trasladan React, TypeScript, Vite, backoffice, backend, monorepo ni carpetas de agentes de producto. Tampoco se trasladan la regla noindex, los comandos de sus aplicaciones ni sus resultados de pruebas.

No se copia su bloqueo de archivos con confirmación en cada cambio: los acuerdos ya autorizados de Roger pueden documentarse mediante la PR correspondiente. Las decisiones nuevas de marca las dirige Roger.

La skill de memoria de TrackFlow sirve como referencia de procedimiento; no se instala ni se ejecuta como una skill de Maison RDL. Aquí bastan instrucciones de mantenimiento explícitas y fichas por tarea.

## Fuente de cada regla

- Exigencias de evaluación: docs/requisitos.md, contrastadas con el enunciado de Maison RDL.
- Decisiones del equipo: CONTEXT.md y PLAN-DE-PROYECTO.md.
- Identidad: docs/diseno.md y tokens.
- Procedimiento para el asistente: AGENTS.md y reglas aplicables.
- Progreso: ficha de cada tarea; resumen global actualizado solo con hechos contrastados.

Este paquete está preparado localmente. Su presencia no demuestra que se haya incorporado al repositorio remoto ni que una entrega esté realizada.
