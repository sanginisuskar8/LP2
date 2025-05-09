class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        self.parent[yroot] = xroot
        return True

def kruskal_mst(edges, n):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

def main():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))
    
    edges = []
    print("Enter each edge in the format: u v weight (1-based index)")
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((u - 1, v - 1, w))  # Convert to 0-based index

    mst, total_weight = kruskal_mst(edges, n)

    print("\nEdges in MST:")
    for u, v, weight in mst:
        print(f"{u + 1} - {v + 1}: {weight}")  # Convert back to 1-based for display

    print(f"Total weight of MST: {total_weight}")

if __name__ == "__main__":
    main()
