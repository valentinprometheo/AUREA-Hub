# Rubro · Escuelas de cursos y carreras

Estado: **propuesta a validar**. Sin caso de cliente cargado todavía (el tablero de
demostración EAF es ilustrativo, no evidencia).

## 1. Tipo de contacto (antes de calificar)
| Valor | Qué se hace |
|---|---|
| Interesado nuevo | Se califica |
| Ex alumno | Se califica con su propio recorrido (no repreguntar nivel) |
| Alumno actual (consulta administrativa) | Se deriva sin calificar |
| Docente u oferente de servicios | Se deriva sin calificar; el tag apaga el asistente |

## 2. Calificado · propuesta
| Condición | Tipo | Variable sugerida |
|---|---|---|
| Programa que la escuela dicta (curso, carrera, diplomatura) | Obligatorio | `programa` |
| Fecha de inicio o cohorte disponible | Obligatorio | `cohorte` |
| Modalidad y turno compatibles | Suma | `modalidad` / `turno` |
| Nivel o requisitos previos cumplidos | Suma | `nivel` |
| Forma de pago (cuotas, beca, empresa) | Suma | `forma_pago` |
| Quién decide o paga (la persona, la familia, la empresa) | Suma | `decisor` |
Regla sugerida: obligatorios + al menos 2 sumas. **Separar ciclos:** un curso corto se decide
cerca del inicio; una carrera tiene ciclo largo y va a nutrición.

## 3. Hot lead · señales sugeridas
Pregunta cómo inscribirse o pagar la seña · pide reservar lugar · el inicio es en menos de 2
semanas · pide hablar con alguien · ya recibió aranceles y pregunta un detalle concreto.

## 4. Criterio de oficio con fuente
- 44% de las consultas a instituciones queda sin respuesta; mediana de respuesta, 3 horas
  (UPCEA). Una conversación genuina de ida y vuelta triplica la probabilidad de inscripción.
- Responder en minutos se asocia con más inscripciones.

## 5. Malas prácticas típicas del rubro
Mandar aranceles antes de saber nivel y turno · el mismo recorrido para ex alumnos y nuevos ·
tratar la carrera con el seguimiento de 48 h de un curso corto.

## 6. Preguntas para el discovery
¿Qué es una consulta calificada para ustedes? · ¿Cuándo está caliente? · ¿Cómo se llena cada
cohorte? · ¿Qué pasa con ex alumnos?
