import sys

def dijkstra(graph, start):
    distance = {}  # Словарь для хранения расстояний от начальной вершины до остальных
    visited = set()  # Множество посещенных вершин
    for vertex in graph:
        distance[vertex] = sys.maxsize  # Инициализация расстояний как бесконечность
    distance[start] = 0  # Расстояние от начальной вершины до себя равно 0

    while len(visited) < len(graph):
        min_distance = sys.maxsize
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and distance[vertex] < min_distance:
                min_distance = distance[vertex]
                min_vertex = vertex

        visited.add(min_vertex)
        for neighbor in graph[min_vertex]:
            weight = graph[min_vertex][neighbor]
            if distance[min_vertex] + weight < distance[neighbor]:
                distance[neighbor] = distance[min_vertex] + weight

    return distance

# Пример использования
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2}
}
start_vertex = 'A'

distances = dijkstra(graph, start_vertex)

print(f"Расстояния от вершины {start_vertex} до остальных:")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")
