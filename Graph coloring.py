def add_edge(graph, u, v):
    graph[u][v] = 1
    graph[v][u] = 1

def is_safe(node, color_to_assign, graph, color, v):
    for k in range(v):
        if graph[node][k] == 1 and color[k] == color_to_assign:
            return False
    return True

def solve(graph, m, v, node, color):
    if node == v:
        return True

    for c in range(1, m + 1):
        if is_safe(node, c, graph, color, v):
            color[node] = c
            if solve(graph, m, v, node + 1, color):
                return True
            color[node] = 0  # Backtrack

    return False

def graph_coloring(graph, m, v):
    color = [0] * v
    if solve(graph, m, v, 0, color):
        print("Color assignment to each node:")
        for i in range(v):
            print(f"Vertex {i}: Color {color[i]}")
    else:
        print("No solution exists with", m, "colors.")

def main():
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))
    m = int(input("Enter number of colors: "))

    graph = [[0 for _ in range(v)] for _ in range(v)]

    print("Enter edges (space-separated vertex pairs):")
    for _ in range(e):
        u, vtx = map(int, input().split())
        add_edge(graph, u, vtx)

    graph_coloring(graph, m, v)

if __name__ == "__main__":
    main()
