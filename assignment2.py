import heapq


def dijkstra(graph, start):
    n = len(graph)
    distances = [float("inf")] * n
    distances[start] = 0
    predecessors = [-1] * n
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in enumerate(graph[current_node]):
            if weight > 0:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(heap, (distance, neighbor))

    return distances, predecessors


def get_shortest_path(predecessors, destination):
    path = []
    current = destination
    while current != -1:
        path.insert(0, current)
        current = predecessors[current]
    return path


def single_source_all_destination(graph, source):
    distances, predecessors = dijkstra(graph, source)
    paths = [get_shortest_path(predecessors, i) for i in range(len(graph))]
    return distances, paths


def single_destination_all_source(graph, destination):
    reversed_graph = [list(row) for row in zip(*graph)]
    distances, predecessors = dijkstra(reversed_graph, destination)
    paths = [get_shortest_path(predecessors, i) for i in range(len(graph))]
    return distances, paths


# Example usage:
if __name__ == "__main__":
    graph = [
        [0, 3, 0, 4, 0],
        [0, 0, 7, 0, 2],
        [0, 0, 0, 0, 0],
        [0, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
    ]

    source_node = 0
    destination_node = 2

    ssad_distances, ssad_paths = single_source_all_destination(graph, source_node)
    print(
        f"Single Source All Destination from node {source_node}: \ndistances: {ssad_distances} \npath: {ssad_paths}"
    )

    sdas_distances, sdas_paths = single_destination_all_source(graph, destination_node)
    print(
        f"Single Destination All Source to node {destination_node}: \ndistances: {sdas_distances} \npath: {sdas_paths}"
    )
