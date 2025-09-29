# 📋 Instrucciones de Ejecución
## Sistema Inteligente de Rutas de Transporte Masivo

### 🚀 Ejecución Rápida

```bash
# Ejecutar demo completo
python sistema_rutas.py

# Ver todas las opciones
python sistema_rutas.py --help
```

### 🎮 Modos de Ejecución

#### 1. Modo Demo (Recomendado para primera ejecución)
```bash
python sistema_rutas.py demo
```
- Muestra ejemplos de rutas
- Compara algoritmos A* y Dijkstra
- Incluye casos de prueba variados

#### 2. Análisis de la Red
```bash
python sistema_rutas.py analyze
```
- Muestra estadísticas de la red
- Lista estaciones y líneas disponibles
- Analiza conectividad

#### 3. Pruebas de Rendimiento
```bash
python sistema_rutas.py performance
```
- Compara velocidad de algoritmos
- Mide tiempos de ejecución
- Valida eficiencia

#### 4. Modo Interactivo
```bash
python sistema_rutas.py interactive
```
- Permite probar rutas personalizadas
- Interfaz de usuario amigable
- Ideal para exploración

### 🧪 Ejecutar Pruebas

```bash
# Ejecutar todas las pruebas
python pruebas.py

# Ejecutar prueba específica
python pruebas.py --test ruta_simple

# Demostración de pruebas
python pruebas.py --demo
```

### 📊 Casos de Prueba Disponibles

- `ruta_simple`: Ruta directa sin transbordos
- `ruta_con_transbordos`: Ruta que requiere cambios de línea
- `comparacion_algoritmos`: Compara A* vs Dijkstra
- `ruta_inexistente`: Manejo de casos sin solución
- `misma_estacion`: Origen y destino iguales
- `heuristica`: Validación de función heurística
- `rendimiento`: Pruebas de velocidad
- `metricas_completas`: Verificación de métricas

### 🔧 Configuración Avanzada

#### Cargar Datos desde CSV
```python
from sistema_rutas import KnowledgeBase, RouteSearcher

# Crear base de conocimiento
kb = KnowledgeBase()

# Cargar conexiones
kb.load_from_csv("datos/conexiones.csv")

# Cargar coordenadas
kb.load_stations_from_csv("datos/estaciones.csv")

# Usar el sistema
searcher = RouteSearcher(kb, search_type="astar")
resultado = searcher.find_best_route("Estacion_A", "Estacion_E")
```

#### Personalizar Parámetros
```python
# Crear buscador personalizado
searcher = RouteSearcher(
    kb=kb,
    transfer_penalty=5.0,      # Penalización por transbordo (minutos)
    use_heuristic=True,        # Usar heurística A*
    search_type="astar"        # "astar" o "dijkstra"
)
```

### 📁 Estructura de Archivos

```
ibero/
├── sistema_rutas.py          # Sistema principal
├── pruebas.py               # Suite de pruebas
├── README.md               # Documentación completa
├── guion_video.md          # Guión para video
├── INSTRUCCIONES.md        # Este archivo
├── datos/                  # Datos de ejemplo
│   ├── conexiones.csv      # Conexiones entre estaciones
│   └── estaciones.csv      # Coordenadas de estaciones
└── ejemplo.py              # Archivo de ejemplo (no relacionado)
```

### 🐛 Solución de Problemas

#### Error: "No module named 'sistema_rutas'"
```bash
# Asegúrate de estar en el directorio correcto
cd /ruta/al/proyecto/ibero

# Verifica que el archivo existe
ls -la sistema_rutas.py
```

#### Error: "FileNotFoundError"
```bash
# Verifica que los archivos de datos existen
ls -la datos/
```

#### Error de sintaxis
```bash
# Verifica la versión de Python
python --version  # Debe ser 3.7+

# Verifica la sintaxis
python -m py_compile sistema_rutas.py
```

### 📈 Interpretación de Resultados

#### Salida Típica
```
🚇 SISTEMA INTELIGENTE DE RUTAS DE TRANSPORTE MASIVO 🚇
Basado en Sistemas de Conocimiento y Búsqueda Heurística
================================================================================

📍 ESTACIONES DISPONIBLES:
 1. Estacion_A
 2. Estacion_B
 ...

🔍 EJEMPLO 1: Ruta de Estacion_A a Estacion_E
Usando algoritmo A* con heurística...
============================================================
RUTA ENCONTRADA
============================================================
1. Estacion_A (INICIO)
2. Estacion_B [llegó con Línea_A]
3. Estacion_C [llegó con Línea_A]
4. Estacion_D [llegó con Línea_A]
5. Estacion_E [llegó con Línea_A]

----------------------------------------
RESUMEN DEL VIAJE:
----------------------------------------
⏱️  Tiempo total: 16.0 minutos
🔄 Transbordos: 0
📏 Distancia total: 9.6 km
💰 Costo total: $8.00
🚇 Líneas utilizadas: Línea_A
============================================================
```

#### Métricas Explicadas
- **Tiempo total**: Duración del viaje en minutos
- **Transbordos**: Número de cambios de línea
- **Distancia total**: Kilómetros recorridos
- **Costo total**: Precio del viaje en dólares
- **Líneas utilizadas**: Líneas de transporte usadas

### 🎯 Casos de Uso Recomendados

#### Para Demostración
1. Ejecutar `python sistema_rutas.py demo`
2. Mostrar diferentes tipos de rutas
3. Comparar algoritmos A* y Dijkstra
4. Explicar las métricas mostradas

#### Para Análisis Técnico
1. Ejecutar `python sistema_rutas.py analyze`
2. Revisar estadísticas de la red
3. Ejecutar `python pruebas.py`
4. Analizar resultados de las pruebas

#### Para Exploración
1. Ejecutar `python sistema_rutas.py interactive`
2. Probar diferentes combinaciones de estaciones
3. Observar cómo cambian las rutas
4. Experimentar con diferentes parámetros

### 📚 Recursos Adicionales

- **README.md**: Documentación completa del proyecto
- **guion_video.md**: Guión para el video explicativo
- **pruebas.py**: Casos de prueba detallados
- **datos/**: Archivos CSV con datos de ejemplo

### 🆘 Soporte

Si encuentras problemas:
1. Revisa este archivo de instrucciones
2. Consulta el README.md para documentación completa
3. Ejecuta las pruebas para verificar el funcionamiento
4. Verifica que tienes Python 3.7+ instalado

---

*Instrucciones preparadas para el proyecto de Sistemas Inteligentes Basados en Conocimiento - Universidad Iberoamericana*
