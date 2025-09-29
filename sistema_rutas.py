
from dataclasses import dataclass, field
import heapq
import json
import csv
import math
from typing import Dict, List, Tuple, Optional, Set

@dataclass
class Edge:
    origin: str
    dest: str
    line: str
    time: float   # minutes
    distance: float = 0.0  # km
    cost: float = 0.0  # costo monetario

@dataclass
class RouteResult:
    path: List[Tuple[str, Optional[str]]]  # list of (stop, line used to arrive to this stop)
    total_time: float
    transfers: int
    total_distance: float = 0.0
    total_cost: float = 0.0
    lines_used: List[str] = field(default_factory=list)

class KnowledgeBase:
    """
    Almacena hechos del tipo conecta(origen, destino, linea, tiempo).
    Hechos dirigidos (se asume que si hay bidireccional, se agregan ambos sentidos).
    """
    def __init__(self):
        self.edges: List[Edge] = []
        self.station_coords: Dict[str, Tuple[float, float]] = {}  # coordenadas para heurística
    
    def add_connection(self, origin: str, dest: str, line: str, time: float, 
                      distance: float = 0.0, cost: float = 0.0, bidirectional: bool = True):
        self.edges.append(Edge(origin, dest, line, time, distance, cost))
        if bidirectional:
            self.edges.append(Edge(dest, origin, line, time, distance, cost))
    
    def add_station_coords(self, station: str, lat: float, lon: float):
        """Agregar coordenadas de una estación para cálculo de heurística"""
        self.station_coords[station] = (lat, lon)
    
    def get_neighbors(self, node: str) -> List[Edge]:
        return [e for e in self.edges if e.origin == node]
    
    def all_nodes(self) -> Set[str]:
        s = set()
        for e in self.edges:
            s.add(e.origin)
            s.add(e.dest)
        return s
    
    def load_from_csv(self, filename: str):
        """Cargar datos desde archivo CSV"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    origin = row['origin']
                    dest = row['dest']
                    line = row['line']
                    time = float(row['time'])
                    distance = float(row.get('distance', 0))
                    cost = float(row.get('cost', 0))
                    bidirectional = row.get('bidirectional', 'true').lower() == 'true'
                    self.add_connection(origin, dest, line, time, distance, cost, bidirectional)
        except FileNotFoundError:
            print(f"Archivo {filename} no encontrado")
        except Exception as e:
            print(f"Error cargando CSV: {e}")
    
    def load_stations_from_csv(self, filename: str):
        """Cargar coordenadas de estaciones desde CSV"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    station = row['station']
                    lat = float(row['lat'])
                    lon = float(row['lon'])
                    self.add_station_coords(station, lat, lon)
        except FileNotFoundError:
            print(f"Archivo {filename} no encontrado")
        except Exception as e:
            print(f"Error cargando estaciones: {e}")

class RouteSearcher:
    """
    Búsqueda con costes. Usa Dijkstra y A*:
      - cost = suma de tiempos + penalty_por_transbordo * num_transbordos
    Se mantiene en el estado el (nodo_actual, linea_actual).
    """
    def __init__(self, kb: KnowledgeBase, transfer_penalty: float = 4.0, 
                 use_heuristic: bool = True, search_type: str = "astar"):
        """
        transfer_penalty: minutos extra que se suman cada vez que se cambia de linea.
        use_heuristic: si usar heurística para búsqueda A*
        search_type: "dijkstra" o "astar"
        """
        self.kb = kb
        self.transfer_penalty = transfer_penalty
        self.use_heuristic = use_heuristic
        self.search_type = search_type
    
    def heuristic(self, current: str, goal: str) -> float:
        """Heurística basada en distancia euclidiana entre coordenadas"""
        if not self.use_heuristic or current not in self.kb.station_coords or goal not in self.kb.station_coords:
            return 0.0
        
        lat1, lon1 = self.kb.station_coords[current]
        lat2, lon2 = self.kb.station_coords[goal]
        
        # Distancia euclidiana simple (aproximación)
        distance = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
        # Convertir a tiempo estimado (asumiendo velocidad promedio de 30 km/h)
        return distance * 2.0  # minutos por grado de latitud/longitud
    
    def find_best_route(self, start: str, goal: str, max_stops: int = 1000) -> Optional[RouteResult]:
        # Priority queue: (cost_estimated, total_time, transfers, total_distance, total_cost, node, current_line, path_list)
        # path_list: list of (stop, line_used_to_arrive_here), first element (start, None)
        pq = []
        # cost initially 0, at start no line (None)
        initial_heuristic = self.heuristic(start, goal) if self.search_type == "astar" else 0.0
        heapq.heappush(pq, (initial_heuristic, 0.0, 0, 0.0, 0.0, start, None, [(start, None)]))
        # visited with best cost found for (node, line)
        best_cost: Dict[Tuple[str, Optional[str]], float] = {(start, None): 0.0}
        
        while pq:
            _, total_time, transfers, total_distance, total_cost, node, cur_line, path = heapq.heappop(pq)
            if node == goal:
                # Calcular líneas utilizadas
                lines_used = list(set([line for _, line in path if line is not None]))
                return RouteResult(
                    path=path, 
                    total_time=total_time, 
                    transfers=transfers,
                    total_distance=total_distance,
                    total_cost=total_cost,
                    lines_used=lines_used
                )
            if len(path) > max_stops:
                continue
            for edge in self.kb.get_neighbors(node):
                next_node = edge.dest
                travel = edge.time
                next_line = edge.line
                # determine if transfer occurs
                additional_penalty = 0.0
                additional_transfer = 0
                if cur_line is None or cur_line == next_line:
                    # same line or start: no transfer
                    pass
                else:
                    additional_penalty += self.transfer_penalty
                    additional_transfer = 1
                
                new_total_time = total_time + travel + additional_penalty
                new_transfers = transfers + additional_transfer
                new_total_distance = total_distance + edge.distance
                new_total_cost = total_cost + edge.cost
                
                state = (next_node, next_line)
                prev_best = best_cost.get(state, float('inf'))
                if new_total_time < prev_best:
                    best_cost[state] = new_total_time
                    new_path = path + [(next_node, next_line)]
                    
                    # Calcular costo estimado para la cola de prioridad
                    if self.search_type == "astar":
                        heuristic_cost = self.heuristic(next_node, goal)
                        estimated_cost = new_total_time + heuristic_cost
                    else:  # dijkstra
                        estimated_cost = new_total_time
                    
                    heapq.heappush(pq, (estimated_cost, new_total_time, new_transfers, 
                                      new_total_distance, new_total_cost, next_node, next_line, new_path))
        return None

def build_sample_kb() -> KnowledgeBase:
    """
    Construye una base de conocimiento de ejemplo (hechos/reglas).
    Simula un sistema de transporte masivo con múltiples líneas.
    """
    kb = KnowledgeBase()
    
    # Línea A (Metro - Línea Principal)
    kb.add_connection("Estacion_A", "Estacion_B", "Línea_A", 4, 2.5, 2.0)
    kb.add_connection("Estacion_B", "Estacion_C", "Línea_A", 3, 1.8, 2.0)
    kb.add_connection("Estacion_C", "Estacion_D", "Línea_A", 5, 3.2, 2.0)
    kb.add_connection("Estacion_D", "Estacion_E", "Línea_A", 4, 2.1, 2.0)
    
    # Línea B (Bus Rápido)
    kb.add_connection("Estacion_F", "Estacion_B", "Línea_B", 6, 4.5, 1.5)
    kb.add_connection("Estacion_F", "Estacion_G", "Línea_B", 7, 5.2, 1.5)
    kb.add_connection("Estacion_G", "Estacion_H", "Línea_B", 4, 3.1, 1.5)
    kb.add_connection("Estacion_H", "Estacion_D", "Línea_B", 8, 6.0, 1.5)
    
    # Línea C (Tren Ligero)
    kb.add_connection("Estacion_I", "Estacion_C", "Línea_C", 12, 8.5, 3.0)
    kb.add_connection("Estacion_I", "Estacion_J", "Línea_C", 6, 4.2, 3.0)
    kb.add_connection("Estacion_J", "Estacion_K", "Línea_C", 9, 6.8, 3.0)
    kb.add_connection("Estacion_K", "Estacion_E", "Línea_C", 7, 5.1, 3.0)
    
    # Conexiones de transferencia (caminar)
    kb.add_connection("Estacion_B", "Estacion_F", "Transferencia_1", 10, 0.8, 0.0)
    kb.add_connection("Estacion_C", "Estacion_G", "Transferencia_2", 6, 0.5, 0.0)
    kb.add_connection("Estacion_D", "Estacion_H", "Transferencia_3", 8, 0.6, 0.0)
    kb.add_connection("Estacion_E", "Estacion_K", "Transferencia_4", 5, 0.4, 0.0)
    
    # Agregar coordenadas para heurística
    stations_coords = {
        "Estacion_A": (40.4168, -3.7038),  # Madrid centro
        "Estacion_B": (40.4200, -3.7000),
        "Estacion_C": (40.4150, -3.6950),
        "Estacion_D": (40.4100, -3.6900),
        "Estacion_E": (40.4050, -3.6850),
        "Estacion_F": (40.4250, -3.7050),
        "Estacion_G": (40.4180, -3.6920),
        "Estacion_H": (40.4080, -3.6880),
        "Estacion_I": (40.4300, -3.7100),
        "Estacion_J": (40.4350, -3.7150),
        "Estacion_K": (40.4000, -3.6800)
    }
    
    for station, coords in stations_coords.items():
        kb.add_station_coords(station, coords[0], coords[1])
    
    return kb

def pretty_print_result(res: RouteResult):
    if res is None:
        print("No se encontró ruta.")
        return
    
    print("=" * 60)
    print("RUTA ENCONTRADA")
    print("=" * 60)
    
    stop_lines = []
    for i, (stop, line) in enumerate(res.path):
        if line is None:
            stop_lines.append(f"{i+1}. {stop} (INICIO)")
        else:
            stop_lines.append(f"{i+1}. {stop} [llegó con {line}]")
    
    for line in stop_lines:
        print(line)
    
    print("\n" + "-" * 40)
    print("RESUMEN DEL VIAJE:")
    print("-" * 40)
    print(f"⏱️  Tiempo total: {res.total_time:.1f} minutos")
    print(f"🔄 Transbordos: {res.transfers}")
    print(f"📏 Distancia total: {res.total_distance:.1f} km")
    print(f"💰 Costo total: ${res.total_cost:.2f}")
    print(f"🚇 Líneas utilizadas: {', '.join(res.lines_used)}")
    print("=" * 60)

def demo():
    print("🚇 SISTEMA INTELIGENTE DE RUTAS DE TRANSPORTE MASIVO 🚇")
    print("Basado en Sistemas de Conocimiento y Búsqueda Heurística")
    print("=" * 80)
    
    kb = build_sample_kb()
    
    # Mostrar estaciones disponibles
    print("\n📍 ESTACIONES DISPONIBLES:")
    stations = sorted(kb.all_nodes())
    for i, station in enumerate(stations, 1):
        print(f"{i:2d}. {station}")
    
    print("\n" + "=" * 80)
    
    # Ejemplo 1: Ruta simple
    print("\n🔍 EJEMPLO 1: Ruta de Estacion_A a Estacion_E")
    print("Usando algoritmo A* con heurística...")
    searcher_astar = RouteSearcher(kb, transfer_penalty=4.0, use_heuristic=True, search_type="astar")
    res1 = searcher_astar.find_best_route("Estacion_A", "Estacion_E")
    pretty_print_result(res1)
    
    # Ejemplo 2: Comparar algoritmos
    print("\n🔍 EJEMPLO 2: Comparación de algoritmos")
    print("Ruta de Estacion_I a Estacion_K")
    
    print("\n--- Algoritmo A* ---")
    res2_astar = searcher_astar.find_best_route("Estacion_I", "Estacion_K")
    pretty_print_result(res2_astar)
    
    print("\n--- Algoritmo Dijkstra ---")
    searcher_dijkstra = RouteSearcher(kb, transfer_penalty=4.0, use_heuristic=False, search_type="dijkstra")
    res2_dijkstra = searcher_dijkstra.find_best_route("Estacion_I", "Estacion_K")
    pretty_print_result(res2_dijkstra)
    
    # Ejemplo 3: Ruta con múltiples transbordos
    print("\n🔍 EJEMPLO 3: Ruta compleja con transbordos")
    print("De Estacion_A a Estacion_J (requiere transbordos)")
    res3 = searcher_astar.find_best_route("Estacion_A", "Estacion_J")
    pretty_print_result(res3)
    
    # Ejemplo 4: Ruta imposible
    print("\n🔍 EJEMPLO 4: Caso sin conexión")
    print("De Estacion_A a Estacion_Z (estación inexistente)")
    res4 = searcher_astar.find_best_route("Estacion_A", "Estacion_Z")
    pretty_print_result(res4)
    
    print("\n" + "=" * 80)
    print("✅ DEMO COMPLETADA")
    print("=" * 80)

def analyze_network(kb: KnowledgeBase):
    """Analiza la red de transporte y muestra estadísticas"""
    print("\n📊 ANÁLISIS DE LA RED DE TRANSPORTE")
    print("=" * 50)
    
    stations = kb.all_nodes()
    lines = set(edge.line for edge in kb.edges)
    
    print(f"📍 Total de estaciones: {len(stations)}")
    print(f"🚇 Total de líneas: {len(lines)}")
    print(f"🔗 Total de conexiones: {len(kb.edges)}")
    
    print(f"\n🚇 Líneas disponibles:")
    for line in sorted(lines):
        line_edges = [e for e in kb.edges if e.line == line]
        print(f"  • {line}: {len(line_edges)} conexiones")
    
    print(f"\n📍 Estaciones con más conexiones:")
    station_connections = {}
    for edge in kb.edges:
        station_connections[edge.origin] = station_connections.get(edge.origin, 0) + 1
    
    sorted_stations = sorted(station_connections.items(), key=lambda x: x[1], reverse=True)
    for station, count in sorted_stations[:5]:
        print(f"  • {station}: {count} conexiones")

def run_performance_test():
    """Prueba de rendimiento comparando algoritmos"""
    print("\n⚡ PRUEBA DE RENDIMIENTO")
    print("=" * 50)
    
    kb = build_sample_kb()
    
    # Casos de prueba
    test_cases = [
        ("Estacion_A", "Estacion_E"),
        ("Estacion_I", "Estacion_K"),
        ("Estacion_A", "Estacion_J"),
        ("Estacion_F", "Estacion_H")
    ]
    
    for start, goal in test_cases:
        print(f"\n🔍 Ruta: {start} → {goal}")
        
        # A*
        import time
        start_time = time.time()
        searcher_astar = RouteSearcher(kb, search_type="astar")
        res_astar = searcher_astar.find_best_route(start, goal)
        astar_time = time.time() - start_time
        
        # Dijkstra
        start_time = time.time()
        searcher_dijkstra = RouteSearcher(kb, search_type="dijkstra")
        res_dijkstra = searcher_dijkstra.find_best_route(start, goal)
        dijkstra_time = time.time() - start_time
        
        if res_astar and res_dijkstra:
            print(f"  A*: {res_astar.total_time:.1f} min, {astar_time*1000:.2f} ms")
            print(f"  Dijkstra: {res_dijkstra.total_time:.1f} min, {dijkstra_time*1000:.2f} ms")
        else:
            print("  No se encontró ruta")

def interactive_mode():
    """Modo interactivo para que el usuario pruebe rutas"""
    print("\n🎮 MODO INTERACTIVO")
    print("=" * 50)
    
    kb = build_sample_kb()
    searcher = RouteSearcher(kb, search_type="astar")
    
    print("Estaciones disponibles:")
    stations = sorted(kb.all_nodes())
    for i, station in enumerate(stations, 1):
        print(f"{i:2d}. {station}")
    
    while True:
        try:
            print("\n" + "-" * 30)
            start = input("Estación de origen (o 'salir'): ").strip()
            if start.lower() == 'salir':
                break
            
            if start not in stations:
                print("❌ Estación no válida")
                continue
                
            goal = input("Estación de destino: ").strip()
            if goal not in stations:
                print("❌ Estación no válida")
                continue
            
            if start == goal:
                print("❌ Origen y destino son iguales")
                continue
            
            print(f"\n🔍 Buscando ruta de {start} a {goal}...")
            result = searcher.find_best_route(start, goal)
            pretty_print_result(result)
            
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "demo":
            demo()
        elif sys.argv[1] == "analyze":
            kb = build_sample_kb()
            analyze_network(kb)
        elif sys.argv[1] == "performance":
            run_performance_test()
        elif sys.argv[1] == "interactive":
            interactive_mode()
        else:
            print("Uso: python sistema_rutas.py [demo|analyze|performance|interactive]")
    else:
        demo()
