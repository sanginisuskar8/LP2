class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))
        self.graph.append((v, u, weight))  # Since the graph is undirected

    def printMST(self, parent, key):
        print("Edge \tWeight")
        total_weight = 0
        for i in range(1, self.V):
            print(parent[i] + 1, "-", i + 1, "\t", key[i])
            total_weight += key[i]
        print("Total weight of MST:", total_weight)

    def minKey(self, key, mstSet):
        min_val = float('inf')
        min_index = -1

        for v in range(self.V):
            if not mstSet[v] and key[v] < min_val:
                min_val = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [float('inf')] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            # Go through all edges to find neighbors of u
            for edge in self.graph:
                src, dest, weight = edge
                if src == u and not mstSet[dest] and key[dest] > weight:
                    key[dest] = weight
                    parent[dest] = u

        self.printMST(parent, key)

def main():
    V = int(input("Enter number of vertices: "))
    g = Graph(V)

    E = int(input("Enter number of edges: "))
    print("Enter the edges (u v weight):")
    for _ in range(E):
        u, v, weight = map(int, input().split())
        g.add_edge(u - 1, v - 1, weight)  # Convert to 0-based index

    g.primMST()

if __name__ == '__main__':
    main()
