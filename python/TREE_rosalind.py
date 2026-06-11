from rosalind_utils import read_input
import sys
sys.setrecursionlimit(10000)

def tree(n, edges: list[tuple[int, int]]):
    #returns the minimum num of edges that can be added to the graph to make a tree
    assert n <= 1000
    connected_components = 0
    visited = [False] * n
    #build the graph as an adjacency list
    graph = [[] for _ in range(n)]
    #the graph is undirected, so add each edge in both directions
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    #use depth-first search to count the number of connected components in the graph
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    #for each node, if it hasn't been visited, it's the start of a new connected component, so we increment the count and perform a DFS to mark all nodes in that component as visited
    for i in range(n):
        if not visited[i]:
            connected_components += 1
            dfs(i)
    #to make a tree, the number of edges needed is the number of connected components - 1
    return connected_components - 1
    
data = read_input("data/rosalind_tree.txt").split('\n')
n = int(data[0])
edges = []
for line in data[1:]:
    if line.strip():
        u,v = map(int, line.split())
        edges.append((u,v))
result = tree(n, edges)
print(result)