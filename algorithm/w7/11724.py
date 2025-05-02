```
방향 없는 그래프가 주어졌을 때, 
연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
```

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 그래프 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS 스택으로 구현
def dfs_stack(start):
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

# 연결 요소 세기
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs_stack(i)
        count += 1

print(count)
