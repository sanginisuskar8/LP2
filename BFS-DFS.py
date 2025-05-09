def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node):
    queue = []
    visited.add(node)
    queue.append(node)

    while queue:
        current = queue.pop(0)
        print(current, end=" ")
        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def build_graph():
    n = int(input("Enter number of nodes: "))
    e = int(input("Enter number of edges: "))
    graph = {i: [] for i in range(1, n + 1)}

    print("Enter each edge in the format: from to")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)  # For directed graph
        # If you want an undirected graph, uncomment the next line
        # graph[v].append(u)

    return graph

def main():
    graph = {}
    while True:
        print("\n=== Graph Traversal Menu ===")
        print("1. Build Graph")
        print("2. DFS Traversal")
        print("3. BFS Traversal")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            graph = build_graph()

        elif choice == '2':
            if not graph:
                print("Graph is empty! Build it first.")
                continue
            visited_dfs = set()
            start = int(input("Enter starting node for DFS: "))
            print("DFS Traversal:")
            dfs(visited_dfs, graph, start)
            print()

        elif choice == '3':
            if not graph:
                print("Graph is empty! Build it first.")
                continue
            visited_bfs = set()
            start = int(input("Enter starting node for BFS: "))
            print("BFS Traversal:")
            bfs(visited_bfs, graph, start)
            print()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
