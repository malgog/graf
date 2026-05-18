import math


def matrix(graph, no_edge=math.inf):
    n = len(graph)
    m = [[no_edge] * n for _ in range(n)]

    for i in range(n):
        m[i][i] = 0

    for u in range(n):
        for v, w in graph[u]:
            m[u][v] = w

    return m


def from_matrix(m, no_edge=math.inf):
    n = len(m)
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and m[i][j] != no_edge:
                graph[i].append((j, m[i][j]))

    return graph


def floyd(graph, no_edge=math.inf):
    dist = matrix(graph, no_edge)
    n = len(dist)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != no_edge and dist[k][j] != no_edge:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


graph = [
    [(1, 3), (2, 8), (4, -4)],
    [(3, 1), (4, 7)],
    [(1, 4)],
    [(0, 2), (2, -5)],
    [(3, 6)]
]

distances = floyd(graph)

for row in distances:
    print(row)