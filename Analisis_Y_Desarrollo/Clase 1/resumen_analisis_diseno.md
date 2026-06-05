# Análisis y Diseño de Software
> Básicamente, programar sin analizar es como construir una casa sin planos. Todos saben que es mala idea pero igual lo hacen.
---
## Por que importa esto
El 66% de los proyectos de software fracasan o se entregan con problemas. Y lo mas chistoso es que casi nunca es culpa del código — es porque nadie se sentó a pensar bien qué se necesitaba desde el principio.
La frase clave:
> "El análisis define QUE se va a construir. El diseño define COMO. La programación es solo el último paso."
---
## Análisis vs Diseño
El análisis es cuando te sientas con el cliente y le preguntas qué necesita. Qué debe hacer el sistema, quién lo va a usar, qué restricciones hay. El resultado es un documento con todo eso escrito.
El diseño es cuando ya sabes qué necesitas y empiezas a planear cómo lo vas a hacer. Qué módulos va a tener, qué base de datos, cómo va a verse la interfaz. El resultado son diagramas y prototipos.
Son dos cosas distintas y hay que hacerlas en ese orden.
---
## La regla del 1-10-100
Si encuentras un error en el análisis, arreglarlo cuesta un peso. Si lo encuentras en el diseño, diez. Si lo encuentras programando, cien. Y si ya está en producción, mil o más.
O sea que vale la pena tomarse el tiempo de pensar bien antes de ponerse a codear.
---
## Ciclo de vida del software
Todo software pasa por estas fases desde que es una idea hasta que deja de usarse:

1. Análisis de requerimientos — se entiende qué necesita el cliente
2. Diseño — se planea cómo construirlo
3. Implementación — se escribe el código
4. Pruebas — se verifica que funcione bien y no tenga errores
5. Despliegue — se entrega y se pone a funcionar de verdad
6. Mantenimiento — se corrigen bugs y se agregan cosas nuevas
---
## Metodologías estructuradas
La idea es planificar todo desde el inicio y seguir el plan. Son buenas cuando sabes exactamente qué se necesita y eso no va a cambiar.
**Cascada** es la más clásica. Las fases van una tras otra y no se regresa. Fácil de administrar pero muy rígida.
**Modelo en V** es igual a cascada pero cada fase de desarrollo tiene su fase de pruebas. Más confiable en calidad.
**Espiral** hace vueltas donde cada vuelta reduce el riesgo. Como ir mejorando un borrador hasta tener el producto final.
Se usan en sistemas críticos como bancos, hospitales o aeronáutica, donde un error puede ser muy grave.
---
## Metodologías ágiles
En 2001 un grupo de desarrolladores hartos de lo rígido que era todo crearon el Manifiesto Ágil. La idea principal es entregar software funcionando rápido y poder adaptarse cuando las cosas cambian.

**Scrum** trabaja en sprints de 1 a 4 semanas. Hay reuniones diarias de 15 minutos y al final de cada sprint se le muestra al cliente lo que se hizo.
**Kanban** es un tablero con columnas de por hacer, haciendo y hecho. La regla es no empezar algo nuevo hasta terminar lo que ya está en curso.
**XP** es el más técnico. Se programa en pares, se escriben las pruebas antes que el código y se está mejorando el código constantemente.
Se usan cuando los requerimientos pueden cambiar, el equipo es pequeño o cuando se necesita lanzar rápido y mejorar después.
---
## Resumen
| | Estructuradas | Agiles |
|---|---|---|
| Planificacion | Todo al inicio | Iterativa |
| Flexibilidad | Baja | Alta |
| Documentacion | Extensa | Lo necesario |
| Entregas | Al final | Frecuentes |
| Ideal para | Sistemas criticos | Apps y productos digitales |