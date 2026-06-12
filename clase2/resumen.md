# Resumen: Requerimientos de Software

## 1. ¿Qué es un requerimiento?
Un requerimiento es una propiedad **documentada y verificable** que un sistema debe cumplir para resolver un problema o alcanzar un objetivo.

### Niveles de abstracción
1. **Necesidad del usuario:** expresa lo que necesita.
2. **Requerimiento del sistema:** describe lo que debe hacer el sistema.
3. **Especificación técnica:** detalla cómo se implementará.

### Fuentes de requerimientos
- Usuarios finales
- Clientes o patrocinadores
- Leyes y normas
- Sistemas externos

### Características de un buen requerimiento
- Necesario
- No ambiguo
- Verificable
- Consistente
- Completo
- Atómico
- Trazable

---

## 2. Requerimientos Funcionales (RF)

Describen **qué hace el sistema**: funciones, tareas, cálculos y respuestas.

### Cómo identificarlos
- Verbos de acción (registrar, mostrar, calcular, enviar)
- Entradas y salidas
- Decisiones
- Roles de usuario

### Categorías principales
- Autenticación
- Cálculo
- Persistencia de datos
- Comunicación
- Reportes
- Validación

---

## 3. Requerimientos No Funcionales (RNF)

Describen **cómo debe funcionar el sistema**, es decir, su calidad y restricciones.

### Categorías principales
- Rendimiento
- Seguridad
- Usabilidad
- Confiabilidad
- Escalabilidad
- Mantenibilidad
- Compatibilidad
- Cumplimiento legal

### Regla importante
Todo RNF debe ser **medible y verificable** mediante métricas.

---

## 4. Atributos de Calidad

Son características generales que determinan la calidad del software según la norma **ISO/IEC 25010**.

### Principales atributos
1. Adecuación funcional
2. Eficiencia de desempeño
3. Compatibilidad
4. Usabilidad
5. Confiabilidad
6. Seguridad
7. Mantenibilidad
8. Portabilidad

### Diferencia con los RNF
- **Atributo de calidad:** concepto general.
- **RNF:** requisito específico y medible relacionado con ese atributo.

---

## 5. Historias de Usuario

Describen necesidades desde la perspectiva del usuario.

### Estructura
Como **[usuario]**  
Quiero **[funcionalidad]**  
Para **[beneficio]**

### Principios INVEST
- Independiente
- Negociable
- Valiosa
- Estimable
- Pequeña
- Testeable

### Criterios de aceptación
Se redactan con el formato:
- Dado...
- Cuando...
- Entonces...

Permiten verificar que la historia fue completada correctamente.

---

## Conclusión

Los requerimientos son la base del desarrollo de software. Los **RF** definen qué hace el sistema, los **RNF** cómo debe comportarse, los **atributos de calidad** establecen estándares de excelencia y las **historias de usuario** ayudan a expresar necesidades de forma clara y centrada en el usuario.