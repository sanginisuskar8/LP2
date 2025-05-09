def dijkstra(graph, vertices, start):
    # Initialize distances with infinity
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    visited = set()

    while len(visited) < len(vertices):
        # Select the unvisited node with the smallest distance
        min_node = None
        min_distance = float('inf')
        for v in vertices:
            if v not in visited and distances[v] < min_distance:
                min_distance = distances[v]
                min_node = v

        if min_node is None:
            break  # Remaining nodes are unreachable

        visited.add(min_node)

        for neighbor, weight in graph.get(min_node, []):
            if neighbor not in visited:
                new_dist = distances[min_node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist

    return distances

def main():
    n = int(input("Enter number of vertices: "))
    print("Enter vertex names (space separated):")
    vertices = input().split()

    graph = {v: [] for v in vertices}

    e = int(input("Enter number of edges: "))
    print("Enter edges in the format: source destination weight")
    for _ in range(e):
        u, v, w = input().split()
        w = int(w)
        graph[u].append((v, w))
        graph[v].append((u, w))  # Assuming undirected graph

    start = input("Enter starting vertex: ")

    distances = dijkstra(graph, vertices, start)

    print(f"\nShortest distances from {start}:")
    for node in vertices:
        print(f"{node}: {distances[node]}")

if __name__ == "__main__":
    main()
