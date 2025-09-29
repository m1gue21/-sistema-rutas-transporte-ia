# 🎬 Guión para Video Explicativo
## Sistema Inteligente de Rutas de Transporte Masivo

**Duración total**: 5 minutos máximo  
**Formato**: Video explicativo con demostración en vivo  
**Participación**: Presentación individual  

---

## 📋 Estructura del Video

### 🎯 **INTRODUCCIÓN** (0:00 - 0:45)
**Duración**: 45 segundos

#### Presentación Personal
- "Hola, soy Miguel Gallego y hoy presento mi proyecto de Inteligencia Artificial"
- "Desarrollé un Sistema Inteligente de Rutas de Transporte Masivo"
- "Implementé algoritmos de búsqueda heurística para optimización de rutas"

#### Contexto Académico
- "Este proyecto forma parte de la asignatura de Inteligencia Artificial Avanzada"
- "Apliqué conceptos de Sistemas Basados en Conocimiento y Búsqueda Heurística"
- "Utilicé representación del conocimiento mediante reglas lógicas"

#### Objetivo del Proyecto
- "Mi objetivo es encontrar la mejor ruta entre dos estaciones de transporte"
- "Considerando tiempo, transbordos, distancia y costo"
- "Usando algoritmos como Dijkstra y A* con heurísticas inteligentes"

---

### 🏗️ **ARQUITECTURA DEL SISTEMA** (0:45 - 1:30)
**Duración**: 45 segundos

#### Componentes Principales
- "El sistema consta de tres componentes principales"
- "KnowledgeBase: almacena hechos sobre conexiones del transporte"
- "RouteSearcher: implementa los algoritmos de búsqueda"
- "Edge y RouteResult: estructuras de datos para representar rutas"

#### Representación del Conocimiento
- "Uso reglas lógicas del tipo conecta(origen, destino, línea, tiempo)"
- "Cada conexión incluye tiempo, distancia y costo monetario"
- "Las coordenadas permiten calcular heurísticas para optimizar la búsqueda"

---

### 🔍 **DEMOSTRACIÓN EN VIVO** (1:30 - 3:30)
**Duración**: 2 minutos

#### Ejecución del Sistema
- "Ahora voy a ejecutar el sistema y mostrar cómo funciona"
- "Primero ejecuto el modo demo para ver todas las funcionalidades"

```bash
python3 sistema_rutas.py demo
```

#### Caso 1: Ruta Simple
- "Aquí vemos una ruta simple de Estacion_A a Estacion_E"
- "El sistema encuentra la ruta óptima en solo 16 minutos"
- "Sin transbordos, usando únicamente la Línea_A"

#### Caso 2: Comparación de Algoritmos
- "Ahora comparo A* vs Dijkstra para la misma ruta"
- "Ambos algoritmos encuentran la misma ruta óptima"
- "Pero A* es más eficiente gracias a la heurística"

#### Caso 3: Ruta Compleja
- "Veamos una ruta que requiere transbordos"
- "De Estacion_A a Estacion_J, el sistema encuentra la mejor combinación"
- "Considerando el costo de los transbordos en la optimización"

#### Análisis de Resultados
- "El sistema muestra métricas completas: tiempo, transbordos, distancia y costo"
- "También indica qué líneas de transporte utilizar"

---

### 🧪 **PRUEBAS Y VALIDACIÓN** (3:30 - 4:15)
**Duración**: 45 segundos

#### Suite de Pruebas
- "Implementé una suite completa de pruebas"
- "Incluye casos de rutas simples, complejas y casos límite"

```bash
python3 pruebas.py
```

#### Casos de Prueba
- "Pruebo rutas con y sin transbordos"
- "Verifico que ambos algoritmos encuentren la misma solución óptima"
- "Valido el manejo de casos sin solución"

#### Métricas de Rendimiento
- "El sistema procesa rutas en menos de 1 milisegundo"
- "A* es aproximadamente 40% más rápido que Dijkstra"
- "Todas las pruebas pasan exitosamente"

---

### 🎓 **CONCEPTOS DE IA APLICADOS** (4:15 - 4:45)
**Duración**: 30 segundos

#### Sistemas Basados en Conocimiento
- "Apliqué representación del conocimiento mediante reglas lógicas"
- "La base de hechos contiene todas las conexiones del transporte"

#### Técnicas de Búsqueda
- "Implementé búsqueda de costo uniforme con Dijkstra"
- "Y búsqueda heurística con A* para mayor eficiencia"

#### Optimización
- "La heurística se basa en distancia euclidiana entre coordenadas"
- "Garantizo que siempre encuentre la ruta óptima"

---

### 🎯 **CONCLUSIONES Y APRENDIZAJES** (4:45 - 5:00)
**Duración**: 15 segundos

#### Logros del Proyecto
- "Desarrollé un sistema funcional que resuelve un problema real"
- "Apliqué conceptos teóricos de IA en un proyecto práctico"
- "Demostré la efectividad de los algoritmos de búsqueda heurística"

#### Aprendizajes Obtenidos
- "Comprendí la importancia de la representación del conocimiento"
- "Aprendí a implementar y comparar diferentes algoritmos de búsqueda"
- "Desarrollé habilidades en programación orientada a objetos y testing"

#### Cierre
- "Gracias por su atención"
- "El código está disponible en mi repositorio Git"
- "¡Hasta la próxima!"

---

## 🎥 **INSTRUCCIONES TÉCNICAS PARA LA GRABACIÓN**

### Configuración del Video
- **Resolución**: 1920x1080 (Full HD) mínimo
- **Framerate**: 30 fps
- **Formato**: MP4
- **Audio**: Estéreo, 48kHz

### Configuración de Pantalla
- **Tamaño de terminal**: 80x24 caracteres mínimo
- **Fuente**: Monospace (Consolas, Monaco, etc.)
- **Tamaño de fuente**: 14-16pt para legibilidad

### Elementos Visuales
1. **Pantalla compartida**: Terminal con código y ejecución
2. **Cámara**: Presentador en cuadro (opcional)
3. **Diapositivas**: Para introducción y conclusiones (opcional)

### Secuencia de Grabación
1. **Grabar introducción** presentándose
2. **Grabar demostración** con pantalla compartida
3. **Grabar conclusiones** con cierre personal
4. **Editar** para unir las partes y ajustar duración

---

## 📝 **NOTAS PARA LA GRABACIÓN**

### Antes de Grabar
- [ ] Practicar el guión varias veces
- [ ] Verificar que el sistema funciona correctamente
- [ ] Preparar ejemplos de rutas para mostrar
- [ ] Configurar el entorno de grabación
- [ ] Probar la pantalla compartida

### Durante la Grabación
- [ ] Hablar claramente y a buen ritmo
- [ ] Mantener contacto visual con la cámara
- [ ] Ejecutar comandos de forma fluida
- [ ] Explicar cada paso mientras se ejecuta
- [ ] Mantener un tono profesional pero natural

### Después de Grabar
- [ ] Revisar la calidad del audio y video
- [ ] Verificar que se capturó toda la información
- [ ] Editar para ajustar duración a 5 minutos máximo
- [ ] Subir a plataforma de video (YouTube, etc.)

---

## 🎯 **OBJETIVOS DEL VIDEO**

### Objetivos Académicos
- Demostrar comprensión de Sistemas Basados en Conocimiento
- Mostrar aplicación práctica de algoritmos de búsqueda
- Explicar la implementación de heurísticas
- Validar el funcionamiento del sistema

### Objetivos Técnicos
- Mostrar la ejecución del código en tiempo real
- Demostrar diferentes casos de uso
- Comparar algoritmos de búsqueda
- Validar resultados con pruebas

### Objetivos de Comunicación
- Explicar conceptos técnicos de forma clara
- Mantener el interés del espectador
- Demostrar competencias técnicas individuales
- Mostrar resultados tangibles

---

*Guión preparado para el proyecto de Sistemas Inteligentes Basados en Conocimiento - Universidad Iberoamericana*
