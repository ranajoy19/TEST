e = [(0, 1), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 0)]
v = 5

# dp = [[0]* v for _ in range(v)]

# adjency matrix
# for e1, e2 in e:
#     dp[e1][e2] = 1
#     dp[e2][e1] = 1


# adjency list

graph = {}
for i in range(v):
    graph[i] = []
for e1, e2 in e:
    graph[e1].append(e2)
    graph[e2].append(e1)


# depth for search


def dfs(graph, node, visited=set()):
    print(node)
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph, child, visited)

    return visited


# print(graph)
# print(dfs(graph, 0))


# how many connected components

e = [
    ["A", "B"],
    ["A", "C"],
    ["A", "D"],
    ["D", "E"],
    ["B", "E"],
    ["F", "G"],
    ["F", "H"],
    ["I", "J"],
]
node = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
node1 = ["A", "F", "I", "K"]

# graph = {i: [] for i in node}

# # adjency list
# for e1, e2 in e:
#     graph[e1].append(e2)
#     graph[e2].append(e1)


def dfs(graph, node, visited=set()):
    visited.add(node)
    sm = 0
    for child in graph[node]:
        if child not in visited:
            sm += dfs(graph, child, visited)
    return sm + 1


# answer = []
# for n in node1:
#     answer.append(dfs(graph, n))
# print(answer)


visited = {i: False for i in range(v)}


def bfs(graph, visted, start):
    queue = []
    queue.append(start)
    visited[start] = True
    while queue:
        start = queue.pop(0)
        print(start, end=" ")
        for i in graph[start]:
            if not visited[i]:
                bfs(graph, visted, i)


bfs(graph, visited, 0)
