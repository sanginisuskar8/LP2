# Function to find shortest paths from source using Greedy search
def greedy_shortest_path(nodes, edges, source):
    # Initialize distances to all nodes as infinity
    distance = [999999] * nodes
    distance[source] = 0  # Distance to source is 0
    visited = [False] * nodes

    while True:
        # Find the unvisited node with the smallest distance
        min_dist = 999999
        u = -1
        for i in range(nodes):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                u = i

        if u == -1:  # No unvisited nodes left
            break

        visited[u] = True  # Mark this node as visited

        # Update distance for all neighbors of u
        for edge in edges:
            a, b, w = edge
            if a == u and not visited[b]:
                if distance[u] + w < distance[b]:
                    distance[b] = distance[u] + w
            elif b == u and not visited[a]:
                if distance[u] + w < distance[a]:
                    distance[a] = distance[u] + w

    return distance

# Take input from user
def take_input():
    nodes, edge_count = map(int, input("Enter number of nodes and edges: ").split())
    edges = []
    print("Enter each edge as: node1 node2 weight")
    for _ in range(edge_count):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    source = int(input("Enter source node: "))
    return nodes, edges, source

# Main code
nodes, edges, source = take_input()
shortest = greedy_shortest_path(nodes, edges, source)

# Output result
print("\nShortest distances from node", source, ":")
for i in range(nodes):
    print(f"To node {i} : {shortest[i]}")
