def dfs(node, dist):
    for next_node, weight in graph[node]:
        if distance[next_node] == -1:
            distance[next_node] = dist + weight
            dfs(next_node, dist + weight)

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    idx = 1
    while data[idx] != -1:
        neighbor = data[idx]
        weight = data[idx + 1]
        graph[node].append((neighbor, weight))
        idx += 2
    
# 1차 DFS: 아무 노드(1번)에서 가장 먼 노드 찾기
distance = [-1] * (V + 1)
distance[1] = 0
dfs(1, 0)
farthest_node = distance.index(max(distance))

# 2차 DFS: farthest_node에서 가장 먼 거리 구하기
distance = [-1] * (V + 1)
distance[farthest_node] = 0
dfs(farthest_node, 0)

print(max(distance))