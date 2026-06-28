# 📚 Casos de Estudio - Evaluación Fase 1: Fundamentos de IA

## 📋 Información General

Estos casos de estudio complementan la evaluación teórica con análisis prácticos de implementaciones reales de IA. Cada caso incluye contexto, preguntas guía y criterios de evaluación.

---

## 🏥 CASO 1: Diagnóstico Médico con IA

### 📖 Contexto

**MediScan AI** es un sistema de diagnóstico por imágenes médicas desarrollado para detectar cáncer de pulmón en radiografías de tórax. El sistema fue entrenado con 100,000 imágenes etiquetadas por radiólogos expertos de hospitales de Estados Unidos y Europa.

### 📊 Datos del Sistema

- **Precisión en pruebas**: 94%
- **Sensibilidad**: 92% (detecta correctamente casos positivos)
- **Especificidad**: 96% (identifica correctamente casos negativos)
- **Tiempo de análisis**: 5 segundos por imagen
- **Tiempo promedio radiológo**: 15-20 minutos por imagen

### 🎯 Preguntas de Análisis

1. **Clasificación del sistema** (5 puntos)
   - ¿Qué tipo de tarea de IA realiza MediScan?
   - ¿Es IA débil o fuerte? Justifica tu respuesta.
   - ¿En qué nivel de autonomía (0-5) lo clasificarías?

2. **Análisis de datos** (8 puntos)
   - ¿Qué problemas potenciales identificas en los datos de entrenamiento?
   - ¿Cómo podría afectar el sesgo geográfico a la precisión del sistema?
   - ¿Qué datos adicionales recomendarías incluir?

3. **Evaluación de métricas** (7 puntos)
   - Explica la diferencia entre sensibilidad y especificidad en este contexto.
   - ¿Qué métrica es más importante para un sistema de detección de cáncer? ¿Por qué?
   - ¿94% de precisión es suficiente para uso clínico? Justifica tu respuesta.

4. **Consideraciones éticas** (10 puntos)
   - ¿Qué responsabilidades tiene el médico al usar este sistema?
   - ¿Cómo manejarías un falso negativo (cáncer no detectado)?
   - ¿Qué información debe conocer el paciente sobre el uso de IA?

### ✅ Criterios de Evaluación

| Criterio | Excelente (4-5 pts) | Bueno (3-4 pts) | Satisfactorio (2-3 pts) | Insuficiente (0-2 pts) |
|----------|-------------------|----------------|----------------------|----------------------|
| **Comprensión técnica** | Identifica correctamente tipo de IA y limitaciones | Comprende aspectos técnicos básicos | Comprensión parcial | Confusión en conceptos técnicos |
| **Análisis crítico** | Identifica múltiples sesgos y problemas | Identifica algunos problemas importantes | Análisis superficial | No identifica problemas clave |
| **Consideraciones éticas** | Análisis profundo de implicaciones éticas | Identifica dilemas éticos principales | Consideraciones básicas | Ignora aspectos éticos |

---

## 🚗 CASO 2: Vehículo Autónomo en Situación de Emergencia

### 📖 Contexto

Un vehículo autónomo Nivel 4 circula por una calle residencial a 50 km/h cuando súbitamente un niño corre tras una pelota hacia la calle. El sistema tiene estas opciones en 0.3 segundos:

**Opción A**: Frenar bruscamente
- Probabilidad de atropello del niño: 20%
- Daño al niño si ocurre: Severo
- Riesgo para pasajeros: Mínimo

**Opción B**: Esquivar hacia la acera
- Probabilidad de atropello del niño: 5%
- Probabilidad de atropellar peatón en acera: 30%
- Daño potencial: Moderado a ambos

**Opción C**: Esquivar hacia carril contrario
- Probabilidad de atropello del niño: 2%
- Probabilidad de colisión frontal: 40%
- Daño a pasajeros: Muy severo

### 🎯 Preguntas de Análisis

1. **Análisis técnico** (8 puntos)
   - ¿Qué tipo de algoritmo de IA necesita el vehículo para esta decisión?
   - ¿Qué datos debe procesar el sistema en tiempo real?
   - ¿Cuáles son las limitaciones técnicas en esta situación?

2. **Dilema ético** (12 puntos)
   - ¿Qué opción elegirías y por qué?
   - ¿Cómo debe programarse la IA para tomar esta decisión?
   - ¿Debe considerar la edad de las víctimas potenciales?

3. **Responsabilidad legal** (8 puntos)
   - ¿Quién es responsable de las consecuencias: programador, fabricante, propietario?
   - ¿Cómo afecta esta situación a la adopción de vehículos autónomos?
   - ¿Qué regulaciones propones para estos casos?

4. **Alternativas de diseño** (7 puntos)
   - ¿Cómo podría prevenir el sistema estas situaciones?
   - ¿Qué mejoras tecnológicas reducirían estos dilemas?
   - ¿Debería el usuario poder configurar estas decisiones?

### ✅ Criterios de Evaluación

| Aspecto | Puntos | Descripción |
|---------|--------|-------------|
| **Análisis técnico** | 8 pts | Comprende limitaciones técnicas y requisitos del sistema |
| **Razonamiento ético** | 12 pts | Presenta argumentos coherentes para decisiones éticas |
| **Consideraciones legales** | 8 pts | Entiende implicaciones de responsabilidad |
| **Propuestas constructivas** | 7 pts | Sugiere mejoras técnicas y regulatorias realistas |

---

## 💰 CASO 3: Sistema de Crédito con Sesgo Algorítmico

### 📖 Contexto

**CreditoFácil** es una fintech que usa IA para aprobar préstamos personales. Después de 2 años de operación, una auditoría revela los siguientes patrones:

### 📊 Datos de Aprobación

| Grupo Demográfico | Tasa de Aprobación | Score Promedio Requerido |
|-------------------|-------------------|------------------------|
| Hombres blancos, 30-50 años | 78% | 650 |
| Mujeres blancas, 30-50 años | 71% | 670 |
| Hombres latinos, 30-50 años | 58% | 720 |
| Mujeres latinas, 30-50 años | 52% | 740 |
| Hombres afroamericanos | 45% | 750 |
| Mujeres afroamericanas | 41% | 760 |

### 🔍 Información Adicional

- Los datos de entrenamiento provenían de bancos tradicionales con historial de 20 años
- El algoritmo no usa directamente raza o género como variables
- Usa códigos postales, historial educativo y laboral como predictores
- La morosidad real es similar entre todos los grupos (3-5%)

### 🎯 Preguntas de Análisis

1. **Identificación del problema** (6 puntos)
   - ¿Qué tipo de sesgo observas en los datos?
   - ¿Cómo pudo desarrollarse este sesgo sin usar variables demográficas directamente?
   - ¿Qué son las "variables proxy" en este contexto?

2. **Análisis de causas** (10 puntos)
   - ¿Cómo contribuyen los datos históricos a este problema?
   - ¿Qué papel juegan los códigos postales en el sesgo?
   - ¿Por qué el algoritmo perpetúa discriminación histórica?

3. **Impacto social** (8 puntos)
   - ¿Cómo afecta este sesgo a las comunidades discriminadas?
   - ¿Qué consecuencias tiene para la inclusión financiera?
   - ¿Es legal este sistema? ¿Es ético?

4. **Soluciones propuestas** (12 puntos)
   - ¿Cómo modificarías el algoritmo para reducir el sesgo?
   - ¿Qué datos adicionales incluirías o excluirías?
   - ¿Cómo balancearías equidad con precisión predictiva?
   - ¿Qué procesos de monitoreo implementarías?

### ✅ Criterios de Evaluación

| Criterio | Excelente (9-12 pts) | Bueno (6-8 pts) | Satisfactorio (3-5 pts) | Insuficiente (0-2 pts) |
|----------|---------------------|----------------|----------------------|----------------------|
| **Identificación de sesgo** | Identifica claramente el sesgo y sus mecanismos | Reconoce el sesgo con comprensión básica | Identifica parcialmente el problema | No reconoce el sesgo |
| **Comprensión de causas** | Explica completamente cómo se desarrolla el sesgo | Comprende las causas principales | Comprensión superficial de causas | No comprende las causas |
| **Análisis de impacto** | Análisis profundo de consecuencias sociales | Identifica impactos importantes | Comprensión básica del impacto | Ignora las consecuencias sociales |
| **Propuestas de solución** | Soluciones comprensivas y técnicamente viables | Propuestas útiles pero incompletas | Soluciones básicas | No propone soluciones viables |

---

## 🎮 CASO 4: IA en Videojuegos - Comportamiento Emergente

### 📖 Contexto

**AlienWorld** es un videojuego de supervivencia donde NPCs (personajes no jugadores) con IA deben sobrevivir en un ecosistema. Cada NPC tiene:
- Necesidades básicas (hambre, sed, refugio)
- Personalidad (agresivo, cooperativo, cauteloso)
- Capacidad de aprendizaje de comportamientos exitosos

Después de 1000 horas de simulación, emergen comportamientos no programados:

### 🔍 Comportamientos Observados

1. **Cooperación compleja**: NPCs forman alianzas temporales para cazar
2. **Economía emergente**: Intercambian recursos sin programación explícita
3. **Cultura artificial**: Desarrollan "rituales" repetitivos sin función aparente
4. **Guerra tribal**: Grupos compiten violentamente por territorios
5. **Sacrificio altruista**: Algunos NPCs se sacrifican por el grupo

### 🎯 Preguntas de Análisis

1. **Tipos de aprendizaje** (8 puntos)
   - ¿Qué tipo de aprendizaje automático están usando los NPCs?
   - ¿Cómo se relaciona esto con aprendizaje por refuerzo?
   - ¿Qué papel juega la interacción entre múltiples agentes?

2. **Comportamiento emergente** (10 puntos)
   - ¿Qué significa "comportamiento emergente" en IA?
   - ¿Cómo surgen comportamientos no programados explícitamente?
   - ¿Qué similaridades ves con comportamientos humanos reales?

3. **Implicaciones filosóficas** (8 puntos)
   - ¿Estos NPCs muestran algún tipo de "inteligencia"?
   - ¿Qué nos dice esto sobre la naturaleza de la inteligencia?
   - ¿Pueden considerarse estos comportamientos como "creativos"?

4. **Aplicaciones prácticas** (9 puntos)
   - ¿Cómo podrían aplicarse estos principios fuera de videojuegos?
   - ¿Qué sectores se beneficiarían de comportamiento emergente?
   - ¿Qué precauciones debemos tomar con sistemas que desarrollan comportamientos impredecibles?

### ✅ Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Comprensión técnica** | 8 pts | Entiende mecanismos de aprendizaje multi-agente |
| **Análisis de emergencia** | 10 pts | Explica cómo surgen comportamientos complejos |
| **Reflexión filosófica** | 8 pts | Considera implicaciones sobre inteligencia y creatividad |
| **Visión aplicada** | 9 pts | Identifica aplicaciones prácticas y precauciones |

---

## 📱 CASO 5: Asistente Virtual con Dilemas de Privacidad

### 📖 Contexto

**VoiceHelper** es un asistente virtual doméstico que escucha constantemente para activarse con palabras clave. Para mejorar sus respuestas, analiza:

- Conversaciones familiares para entender contexto
- Patrones de sueño y actividad diaria
- Preferencias musicales y de entretenimiento
- Hábitos de compra y consumo
- Información médica mencionada casualmente

### 🚨 Situación Problemática

La empresa descubre que VoiceHelper ha:
1. Grabado conversaciones íntimas sin activación intencional
2. Detectado signos de violencia doméstica en algunos hogares
3. Identificado usuarios con posibles problemas de salud mental
4. Registrado información sensible de menores de edad

### 🎯 Preguntas de Análisis

1. **Dilemas de privacidad** (10 puntos)
   - ¿Qué información debería tener derecho a procesar el asistente?
   - ¿Cómo balancear personalización con privacidad?
   - ¿Qué consentimiento se requiere para diferentes tipos de datos?

2. **Responsabilidad social** (10 puntos)
   - Si detecta violencia doméstica, ¿debe reportarla a autoridades?
   - ¿Qué obligación tiene con la salud mental de los usuarios?
   - ¿Cómo proteger a menores sin violar privacidad familiar?

3. **Soluciones técnicas** (8 puntos)
   - ¿Qué tecnologías podrían preservar privacidad sin perder funcionalidad?
   - ¿Cómo implementar "privacidad por diseño"?
   - ¿Qué controles debe tener el usuario?

4. **Marco regulatorio** (7 puntos)
   - ¿Qué regulaciones son necesarias para estos sistemas?
   - ¿Cómo debe supervisarse el uso de datos?
   - ¿Qué derechos deben tener los usuarios?

### ✅ Criterios de Evaluación

| Aspecto | Excelente (8-10 pts) | Bueno (6-7 pts) | Satisfactorio (4-5 pts) | Insuficiente (0-3 pts) |
|---------|---------------------|----------------|----------------------|----------------------|
| **Análisis de privacidad** | Comprende completamente las tensiones entre funcionalidad y privacidad | Identifica dilemas principales | Comprensión básica de problemas | No comprende los dilemas |
| **Consideraciones éticas** | Propone frameworks éticos sólidos | Identifica dilemas éticos importantes | Consideraciones éticas básicas | Ignora dimensiones éticas |
| **Propuestas técnicas** | Soluciones técnicamente viables y efectivas | Propuestas útiles pero limitadas | Soluciones básicas | No propone soluciones técnicas |
| **Visión regulatoria** | Marco regulatorio comprensivo | Identifica necesidades regulatorias | Comprensión básica de regulación | No considera aspectos legales |

---

## 📊 Instrucciones de Evaluación

### 🎯 Selección de Casos

Para la evaluación formal, cada estudiante debe:

1. **Seleccionar 2 casos** de los 5 disponibles
2. **Justificar** su selección (¿por qué estos casos te interesan?)
3. **Completar análisis** siguiendo las preguntas guía
4. **Incluir reflexión personal** sobre aprendizajes

### ⏱️ Tiempo y Formato

- **Tiempo estimado**: 2-3 horas por caso
- **Formato**: Respuestas escritas detalladas
- **Extensión**: 1000-1500 palabras por caso
- **Entrega**: Documento digital con estructura clara

### 📋 Criterios Generales

| Criterio | Peso | Descripción |
|----------|------|-------------|
| **Comprensión técnica** | 30% | Demuestra entendimiento de conceptos de IA |
| **Análisis crítico** | 35% | Evalúa problemas y oportunidades profundamente |
| **Consideraciones éticas** | 25% | Incorpora dimensiones éticas y sociales |
| **Comunicación** | 10% | Presenta ideas claramente y argumenta bien |

### 🎓 Objetivos de Aprendizaje

Estos casos buscan que el estudiante:

- **Aplique** conceptos teóricos a situaciones reales
- **Analice** problemas complejos desde múltiples perspectivas
- **Desarrolle** pensamiento crítico sobre IA
- **Considere** implicaciones éticas y sociales
- **Proponga** soluciones constructivas y realistas

---

## 🔄 Retroalimentación y Mejora

### 📝 Autoevaluación

Después de completar los casos, reflexiona:

1. ¿Qué conceptos aplicaste de la Fase 1?
2. ¿Qué aspectos te resultaron más desafiantes?
3. ¿Cómo cambió tu perspectiva sobre la IA?
4. ¿Qué áreas necesitas reforzar?

### 🚀 Siguientes Pasos

Basado en tu desempeño:

- **Excelente**: Preparado para casos avanzados
- **Bueno**: Reforzar análisis crítico
- **Satisfactorio**: Más práctica con aplicaciones
- **Insuficiente**: Repaso de fundamentos

Estos casos de estudio te preparan para enfrentar desafíos reales en el mundo de la IA, donde las decisiones técnicas tienen profundas implicaciones humanas y sociales.