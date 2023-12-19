import heapq


def dijkstra(graph, start):
    n = len(graph)
    distances = [float("inf")] * n
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        cur_distance, cur_node = heapq.heappop(heap)
        if cur_distance > distances[cur_node]:
            continue
        for neighbor, weight in enumerate(graph[cur_node]):
            if weight > 0:
                distance = distances[cur_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
    return distances


def single_source_all_destination(graph, source):
    return dijkstra(graph, source)


def single_destination_all_source(graph, destination):
    reversed_graph = [list(row) for row in zip(*graph)]
    return dijkstra(reversed_graph, destination)


# Example usage:
if __name__ == "__main__":
    # Example adjacency matrix
    graph = [
        [0, 3, 0, 4, 0],
        [0, 0, 7, 0, 2],
        [0, 0, 0, 0, 0],
        [0, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
    ]

    source_node = 1
    destination_node = 3

    # Single Source All Destination
    ssad_result = single_source_all_destination(graph, source_node)
    print(f"Single Source All Destination from node {source_node}: {ssad_result}")

    # Single Destination All Source
    sdas_result = single_destination_all_source(graph, destination_node)
    print(f"Single Destination All Source to node {destination_node}: {sdas_result}")
