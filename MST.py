# Function to find MST using a simple greedy approach
def greedy_mst(nodes, edges):
    visited = [False] * nodes  # Tracks if a node is included in MST
    visited[0] = True  # Start with the first node (node 0)
    
    mst = []  # To store edges in MST
    total_cost = 0  # To track the total cost of MST
    
    while len(mst) < nodes - 1:  # We need (nodes-1) edges to form an MST
        min_edge = None
        min_weight = float('inf')
        
        # Find the smallest edge that connects a visited node with an unvisited one
        for u, v, w in edges:
            if (visited[u] and not visited[v]) or (visited[v] and not visited[u]):
                if w < min_weight:
                    min_edge = (u, v, w)
                    min_weight = w
        
        # If a valid edge is found, add it to MST and mark the node as visited
        if min_edge:
            u, v, w = min_edge
            mst.append(min_edge)
            total_cost += w
            visited[u] = visited[v] = True  # Mark both nodes as visited
    
    return mst, total_cost

# Function to take input from user
def take_input():
    print("Enter number of nodes and edges:")
    nodes, edge_count = map(int, input().split())

    edges = []
    print("Enter each edge as: node1 node2 weight")
    for _ in range(edge_count):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    return nodes, edges

# Main program
nodes, edges = take_input()
mst, cost = greedy_mst(nodes, edges)

# Display the MST edges and total cost
print("\nEdges in the Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")

print("\nTotal cost of MST:", cost)
