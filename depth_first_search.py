# -*- coding: utf-8 -*-
"""Depth First Search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11NqZQ2hiJw1z1lGGzh8xWFQPFzRHHhW1
"""

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() 

def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("Following is the Depth-First Search")
dfs(visited, graph, '5')

from collections import deque
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
def isReachable(graph, src, dest, discovered, path):
    discovered[src] = True
    path.append(src)
    if src == dest:
        return True
    for i in graph.adjList[src]:
        if not discovered[i]:
            if isReachable(graph, i, dest, discovered, path):
                return True
    path.pop()
    return False
if __name__ == '__main__':
    edges = [
        (0, 3), (1, 0), (1, 2), (1, 4), (2, 7), (3, 4),
        (3, 5), (4, 3), (4, 6), (5, 6), (6, 7)
    ]
    n = 8
    graph = Graph(edges, n)

    discovered = [False] * n
    (src, dest) = (eval(input("Enter source: ")), eval(input("Enter destination: ")))
    path = deque()
    if isReachable(graph, src, dest, discovered, path):
        print(f'Path exists from vertex {src} to vertex {dest}')
        print(f'The complete path is', *list(path))
    else:
        print(f'No path exists between vertices {src} and {dest}')