#!/usr/bin/env python3
"""
Archivo de pruebas para el Sistema Inteligente de Rutas de Transporte Masivo
Incluye casos de prueba exhaustivos y análisis de rendimiento
"""

import time
import sys
from sistema_rutas import KnowledgeBase, RouteSearcher, build_sample_kb, pretty_print_result

class TestSuite:
    """Suite de pruebas para el sistema de rutas"""
    
    def __init__(self):
        self.kb = build_sample_kb()
        self.test_results = []
        self.passed_tests = 0
        self.total_tests = 0
    
    def run_test(self, test_name, test_func):
        """Ejecuta una prueba individual"""
        print(f"\n🧪 Ejecutando: {test_name}")
        print("-" * 50)
        
        self.total_tests += 1
        start_time = time.time()
        
        try:
            result = test_func()
            execution_time = time.time() - start_time
            
            if result:
                print(f"✅ PASÓ - Tiempo: {execution_time*1000:.2f}ms")
                self.passed_tests += 1
            else:
                print(f"❌ FALLÓ - Tiempo: {execution_time*1000:.2f}ms")
            
            self.test_results.append({
                'name': test_name,
                'passed': result,
                'time': execution_time
            })
            
        except Exception as e:
            execution_time = time.time() - start_time
            print(f"💥 ERROR - {str(e)} - Tiempo: {execution_time*1000:.2f}ms")
            self.test_results.append({
                'name': test_name,
                'passed': False,
                'time': execution_time,
                'error': str(e)
            })
    
    def test_ruta_simple(self):
        """Prueba: Ruta simple sin transbordos"""
        searcher = RouteSearcher(self.kb, search_type="astar")
        result = searcher.find_best_route("Estacion_A", "Estacion_E")
        
        if not result:
            print("❌ No se encontró ruta")
            return False
        
        # Verificar que la ruta es directa (solo Línea_A)
        expected_lines = {"Línea_A"}
        actual_lines = set(result.lines_used)
        
        if actual_lines != expected_lines:
            print(f"❌ Líneas esperadas: {expected_lines}, obtenidas: {actual_lines}")
            return False
        
        # Verificar que no hay transbordos
        if result.transfers != 0:
            print(f"❌ Transbordos esperados: 0, obtenidos: {result.transfers}")
            return False
        
        print(f"✅ Ruta encontrada: {len(result.path)} estaciones")
        print(f"✅ Tiempo total: {result.total_time} minutos")
        return True
    
    def test_ruta_con_transbordos(self):
        """Prueba: Ruta que requiere transbordos"""
        searcher = RouteSearcher(self.kb, search_type="astar")
        result = searcher.find_best_route("Estacion_A", "Estacion_J")
        
        if not result:
            print("❌ No se encontró ruta")
            return False
        
        # Verificar que hay transbordos
        if result.transfers == 0:
            print("❌ Se esperaban transbordos pero no se encontraron")
            return False
        
        # Verificar que se usan múltiples líneas
        if len(result.lines_used) < 2:
            print(f"❌ Se esperaban múltiples líneas, se usaron: {len(result.lines_used)}")
            return False
        
        print(f"✅ Ruta con transbordos: {result.transfers} cambios")
        print(f"✅ Líneas utilizadas: {result.lines_used}")
        return True
    
    def test_comparacion_algoritmos(self):
        """Prueba: Comparación entre A* y Dijkstra"""
        start, goal = "Estacion_I", "Estacion_K"
        
        # A*
        searcher_astar = RouteSearcher(self.kb, search_type="astar")
        result_astar = searcher_astar.find_best_route(start, goal)
        
        # Dijkstra
        searcher_dijkstra = RouteSearcher(self.kb, search_type="dijkstra")
        result_dijkstra = searcher_dijkstra.find_best_route(start, goal)
        
        if not result_astar or not result_dijkstra:
            print("❌ Al menos un algoritmo no encontró ruta")
            return False
        
        # Verificar que ambos encuentran la misma ruta óptima
        if abs(result_astar.total_time - result_dijkstra.total_time) > 0.1:
            print(f"❌ Tiempos diferentes - A*: {result_astar.total_time}, Dijkstra: {result_dijkstra.total_time}")
            return False
        
        print(f"✅ Ambos algoritmos encuentran la misma ruta óptima")
        print(f"✅ Tiempo: {result_astar.total_time} minutos")
        return True
    
    def test_ruta_inexistente(self):
        """Prueba: Ruta a estación inexistente"""
        searcher = RouteSearcher(self.kb, search_type="astar")
        result = searcher.find_best_route("Estacion_A", "Estacion_Z")
        
        if result is not None:
            print("❌ Se encontró ruta cuando no debería existir")
            return False
        
        print("✅ Correctamente no encuentra ruta inexistente")
        return True
    
    def test_misma_estacion(self):
        """Prueba: Origen y destino iguales"""
        searcher = RouteSearcher(self.kb, search_type="astar")
        result = searcher.find_best_route("Estacion_A", "Estacion_A")
        
        if result is None:
            print("❌ No maneja correctamente origen = destino")
            return False
        
        if len(result.path) != 1:
            print(f"❌ Ruta debería tener 1 estación, tiene: {len(result.path)}")
            return False
        
        print("✅ Maneja correctamente origen = destino")
        return True
    
    def test_heuristica(self):
        """Prueba: Funcionamiento de la heurística"""
        searcher = RouteSearcher(self.kb, search_type="astar")
        
        # Verificar que la heurística devuelve valores positivos
        h1 = searcher.heuristic("Estacion_A", "Estacion_E")
        h2 = searcher.heuristic("Estacion_A", "Estacion_J")
        
        if h1 < 0 or h2 < 0:
            print(f"❌ Heurística devuelve valores negativos: {h1}, {h2}")
            return False
        
        # Verificar que la heurística es admisible (no sobreestima)
        result = searcher.find_best_route("Estacion_A", "Estacion_E")
        if result and h1 > result.total_time:
            print(f"❌ Heurística sobreestima: {h1} > {result.total_time}")
            return False
        
        print(f"✅ Heurística funciona correctamente: {h1:.2f}, {h2:.2f}")
        return True
    
    def test_rendimiento(self):
        """Prueba: Rendimiento del sistema"""
        searcher = RouteSearcher(self.kb, search_type="astar")
        
        # Casos de prueba para rendimiento
        test_cases = [
            ("Estacion_A", "Estacion_E"),
            ("Estacion_I", "Estacion_K"),
            ("Estacion_F", "Estacion_H"),
            ("Estacion_A", "Estacion_J")
        ]
        
        total_time = 0
        successful_routes = 0
        
        for start, goal in test_cases:
            start_time = time.time()
            result = searcher.find_best_route(start, goal)
            execution_time = time.time() - start_time
            
            total_time += execution_time
            if result:
                successful_routes += 1
        
        avg_time = total_time / len(test_cases)
        
        if avg_time > 0.1:  # Más de 100ms promedio
            print(f"❌ Rendimiento lento: {avg_time*1000:.2f}ms promedio")
            return False
        
        if successful_routes != len(test_cases):
            print(f"❌ Solo {successful_routes}/{len(test_cases)} rutas exitosas")
            return False
        
        print(f"✅ Rendimiento óptimo: {avg_time*1000:.2f}ms promedio")
        print(f"✅ {successful_routes}/{len(test_cases)} rutas exitosas")
        return True
    
    def test_metricas_completas(self):
        """Prueba: Verificar que todas las métricas se calculan correctamente"""
        searcher = RouteSearcher(self.kb, search_type="astar")
        result = searcher.find_best_route("Estacion_A", "Estacion_E")
        
        if not result:
            print("❌ No se encontró ruta para verificar métricas")
            return False
        
        # Verificar que todas las métricas están presentes
        required_metrics = ['total_time', 'transfers', 'total_distance', 'total_cost', 'lines_used']
        
        for metric in required_metrics:
            if not hasattr(result, metric):
                print(f"❌ Métrica faltante: {metric}")
                return False
        
        # Verificar que los valores son razonables
        if result.total_time <= 0:
            print(f"❌ Tiempo total inválido: {result.total_time}")
            return False
        
        if result.transfers < 0:
            print(f"❌ Transbordos negativos: {result.transfers}")
            return False
        
        if result.total_distance < 0:
            print(f"❌ Distancia negativa: {result.total_distance}")
            return False
        
        print("✅ Todas las métricas calculadas correctamente")
        return True
    
    def run_all_tests(self):
        """Ejecuta todas las pruebas"""
        print("🚀 INICIANDO SUITE DE PRUEBAS")
        print("=" * 60)
        
        # Ejecutar todas las pruebas
        self.run_test("Ruta Simple", self.test_ruta_simple)
        self.run_test("Ruta con Transbordos", self.test_ruta_con_transbordos)
        self.run_test("Comparación de Algoritmos", self.test_comparacion_algoritmos)
        self.run_test("Ruta Inexistente", self.test_ruta_inexistente)
        self.run_test("Misma Estación", self.test_misma_estacion)
        self.run_test("Heurística", self.test_heuristica)
        self.run_test("Rendimiento", self.test_rendimiento)
        self.run_test("Métricas Completas", self.test_metricas_completas)
        
        # Mostrar resumen
        self.show_summary()
    
    def show_summary(self):
        """Muestra resumen de las pruebas"""
        print("\n" + "=" * 60)
        print("📊 RESUMEN DE PRUEBAS")
        print("=" * 60)
        
        print(f"Total de pruebas: {self.total_tests}")
        print(f"Pruebas exitosas: {self.passed_tests}")
        print(f"Pruebas fallidas: {self.total_tests - self.passed_tests}")
        print(f"Porcentaje de éxito: {(self.passed_tests/self.total_tests)*100:.1f}%")
        
        # Mostrar pruebas fallidas
        failed_tests = [t for t in self.test_results if not t['passed']]
        if failed_tests:
            print(f"\n❌ Pruebas fallidas:")
            for test in failed_tests:
                print(f"  • {test['name']}")
                if 'error' in test:
                    print(f"    Error: {test['error']}")
        
        # Mostrar tiempo promedio
        avg_time = sum(t['time'] for t in self.test_results) / len(self.test_results)
        print(f"\n⏱️  Tiempo promedio por prueba: {avg_time*1000:.2f}ms")
        
        print("\n" + "=" * 60)
        
        if self.passed_tests == self.total_tests:
            print("🎉 ¡TODAS LAS PRUEBAS PASARON!")
        else:
            print("⚠️  ALGUNAS PRUEBAS FALLARON")
        
        print("=" * 60)

def demo_pruebas():
    """Demostración de las pruebas"""
    print("🧪 DEMOSTRACIÓN DE PRUEBAS DEL SISTEMA DE RUTAS")
    print("=" * 60)
    
    # Crear suite de pruebas
    test_suite = TestSuite()
    
    # Ejecutar todas las pruebas
    test_suite.run_all_tests()
    
    # Demostración adicional
    print("\n🎯 DEMOSTRACIÓN ADICIONAL")
    print("-" * 30)
    
    # Mostrar algunas rutas de ejemplo
    searcher = RouteSearcher(test_suite.kb, search_type="astar")
    
    print("\n📍 Ejemplos de rutas encontradas:")
    examples = [
        ("Estacion_A", "Estacion_E", "Ruta directa"),
        ("Estacion_I", "Estacion_K", "Ruta con transbordos"),
        ("Estacion_F", "Estacion_H", "Ruta en línea B")
    ]
    
    for start, goal, description in examples:
        print(f"\n🔍 {description}: {start} → {goal}")
        result = searcher.find_best_route(start, goal)
        if result:
            print(f"  ⏱️  Tiempo: {result.total_time:.1f} min")
            print(f"  🔄 Transbordos: {result.transfers}")
            print(f"  🚇 Líneas: {', '.join(result.lines_used)}")
        else:
            print("  ❌ No se encontró ruta")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Suite de pruebas para el sistema de rutas")
    parser.add_argument("--test", help="Ejecutar prueba específica")
    parser.add_argument("--demo", action="store_true", help="Ejecutar demostración")
    
    args = parser.parse_args()
    
    if args.demo:
        demo_pruebas()
    elif args.test:
        # Ejecutar prueba específica
        test_suite = TestSuite()
        test_method = getattr(test_suite, f"test_{args.test}", None)
        if test_method:
            test_suite.run_test(args.test.replace("_", " ").title(), test_method)
        else:
            print(f"❌ Prueba '{args.test}' no encontrada")
    else:
        # Ejecutar todas las pruebas
        test_suite = TestSuite()
        test_suite.run_all_tests()
