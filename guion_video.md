# 🎬 Guión para Video Explicativo
## Sistema Inteligente de Rutas de Transporte Masivo

**Duración total**: 5 minutos máximo  
**Formato**: Video explicativo con demostración en vivo  
**Participación**: Todos los integrantes del equipo  

---

## 📋 Estructura del Video

### 🎯 **INTRODUCCIÓN** (0:00 - 0:45)
**Duración**: 45 segundos

#### Presentación del Equipo
- [Integrante 1]: "Hola, soy [Nombre] y hoy presentamos nuestro proyecto de Inteligencia Artificial"
- [Integrante 2]: "Soy [Nombre] y desarrollamos un Sistema Inteligente de Rutas de Transporte"
- [Integrante 3]: "Soy [Nombre] y implementamos algoritmos de búsqueda heurística"

#### Contexto Académico
- [Integrante 1]: "Este proyecto forma parte de la asignatura de Inteligencia Artificial Avanzada"
- [Integrante 2]: "Aplicamos conceptos de Sistemas Basados en Conocimiento y Búsqueda Heurística"
- [Integrante 3]: "Utilizamos representación del conocimiento mediante reglas lógicas"

#### Objetivo del Proyecto
- [Integrante 1]: "Nuestro objetivo es encontrar la mejor ruta entre dos estaciones de transporte"
- [Integrante 2]: "Considerando tiempo, transbordos, distancia y costo"
- [Integrante 3]: "Usando algoritmos como Dijkstra y A* con heurísticas inteligentes"

---

### 🏗️ **ARQUITECTURA DEL SISTEMA** (0:45 - 1:30)
**Duración**: 45 segundos

#### Componentes Principales
- [Integrante 1]: "El sistema consta de tres componentes principales"
- [Integrante 2]: "KnowledgeBase: almacena hechos sobre conexiones del transporte"
- [Integrante 3]: "RouteSearcher: implementa los algoritmos de búsqueda"
- [Integrante 1]: "Edge y RouteResult: estructuras de datos para representar rutas"

#### Representación del Conocimiento
- [Integrante 2]: "Usamos reglas lógicas del tipo conecta(origen, destino, línea, tiempo)"
- [Integrante 3]: "Cada conexión incluye tiempo, distancia y costo monetario"
- [Integrante 1]: "Las coordenadas permiten calcular heurísticas para optimizar la búsqueda"

---

### 🔍 **DEMOSTRACIÓN EN VIVO** (1:30 - 3:30)
**Duración**: 2 minutos

#### Ejecución del Sistema
- [Integrante 1]: "Ahora vamos a ejecutar el sistema y ver cómo funciona"
- [Integrante 2]: "Primero ejecutamos el modo demo para ver todas las funcionalidades"

```bash
python sistema_rutas.py demo
```

#### Caso 1: Ruta Simple
- [Integrante 3]: "Aquí vemos una ruta simple de Estacion_A a Estacion_E"
- [Integrante 1]: "El sistema encuentra la ruta óptima en solo 16 minutos"
- [Integrante 2]: "Sin transbordos, usando únicamente la Línea_A"

#### Caso 2: Comparación de Algoritmos
- [Integrante 3]: "Ahora comparamos A* vs Dijkstra para la misma ruta"
- [Integrante 1]: "Ambos algoritmos encuentran la misma ruta óptima"
- [Integrante 2]: "Pero A* es más eficiente gracias a la heurística"

#### Caso 3: Ruta Compleja
- [Integrante 3]: "Veamos una ruta que requiere transbordos"
- [Integrante 1]: "De Estacion_A a Estacion_J, el sistema encuentra la mejor combinación"
- [Integrante 2]: "Considerando el costo de los transbordos en la optimización"

#### Análisis de Resultados
- [Integrante 3]: "El sistema muestra métricas completas: tiempo, transbordos, distancia y costo"
- [Integrante 1]: "También indica qué líneas de transporte utilizar"

---

### 🧪 **PRUEBAS Y VALIDACIÓN** (3:30 - 4:15)
**Duración**: 45 segundos

#### Suite de Pruebas
- [Integrante 2]: "Implementamos una suite completa de pruebas"
- [Integrante 3]: "Incluye casos de rutas simples, complejas y casos límite"

```bash
python pruebas.py
```

#### Casos de Prueba
- [Integrante 1]: "Probamos rutas con y sin transbordos"
- [Integrante 2]: "Verificamos que ambos algoritmos encuentren la misma solución óptima"
- [Integrante 3]: "Validamos el manejo de casos sin solución"

#### Métricas de Rendimiento
- [Integrante 1]: "El sistema procesa rutas en menos de 1 milisegundo"
- [Integrante 2]: "A* es aproximadamente 40% más rápido que Dijkstra"
- [Integrante 3]: "Todas las pruebas pasan exitosamente"

---

### 🎓 **CONCEPTOS DE IA APLICADOS** (4:15 - 4:45)
**Duración**: 30 segundos

#### Sistemas Basados en Conocimiento
- [Integrante 1]: "Aplicamos representación del conocimiento mediante reglas lógicas"
- [Integrante 2]: "La base de hechos contiene todas las conexiones del transporte"

#### Técnicas de Búsqueda
- [Integrante 3]: "Implementamos búsqueda de costo uniforme con Dijkstra"
- [Integrante 1]: "Y búsqueda heurística con A* para mayor eficiencia"

#### Optimización
- [Integrante 2]: "La heurística se basa en distancia euclidiana entre coordenadas"
- [Integrante 3]: "Garantizamos que siempre encontremos la ruta óptima"

---

### 🎯 **CONCLUSIONES Y APRENDIZAJES** (4:45 - 5:00)
**Duración**: 15 segundos

#### Logros del Proyecto
- [Integrante 1]: "Desarrollamos un sistema funcional que resuelve un problema real"
- [Integrante 2]: "Aplicamos conceptos teóricos de IA en un proyecto práctico"
- [Integrante 3]: "Demostramos la efectividad de los algoritmos de búsqueda heurística"

#### Aprendizajes Obtenidos
- [Integrante 1]: "Comprendimos la importancia de la representación del conocimiento"
- [Integrante 2]: "Aprendimos a implementar y comparar diferentes algoritmos de búsqueda"
- [Integrante 3]: "Desarrollamos habilidades en programación orientada a objetos y testing"

#### Cierre
- [Integrante 1]: "Gracias por su atención"
- [Integrante 2]: "El código está disponible en nuestro repositorio Git"
- [Integrante 3]: "¡Hasta la próxima!"

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
2. **Cámara**: Los integrantes en cuadro (opcional)
3. **Diapositivas**: Para introducción y conclusiones (opcional)

### Secuencia de Grabación
1. **Grabar introducción** con todos los integrantes
2. **Grabar demostración** con pantalla compartida
3. **Grabar conclusiones** con todos los integrantes
4. **Editar** para unir las partes y ajustar duración

---

## 📝 **NOTAS PARA LOS INTEGRANTES**

### Antes de Grabar
- [ ] Practicar el guión individualmente
- [ ] Verificar que el sistema funciona correctamente
- [ ] Preparar ejemplos de rutas para mostrar
- [ ] Configurar el entorno de grabación

### Durante la Grabación
- [ ] Hablar claramente y a buen ritmo
- [ ] Mantener contacto visual con la cámara
- [ ] Ejecutar comandos de forma fluida
- [ ] Explicar cada paso mientras se ejecuta

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
- Demostrar trabajo en equipo
- Mostrar resultados tangibles

---

*Guión preparado para el proyecto de Sistemas Inteligentes Basados en Conocimiento - Universidad Iberoamericana*
