from collections import deque

def find_parents(n, edges):
    tree = {i: [] for i in range(1, n + 1)}
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    parents = {1: None} # 루트 노드 및 부모 노드 딕셔너리
    queue = deque([1]) # 탐색을 위한 큐

    while queue:
        current = queue.popleft() # 큐에서 꺼내고
        for child in tree[current]: # 연결된 이웃들 중에
            if child not in parents: # 아직 부모 기록이 없으면(방문 안햇으면)
                parents[child] = current # current가 부모
                queue.append(child) # 다음에 탐색할 큐에 추가

    for i in range(2, n+1): # 2번 노드부터 부모 출력
        print(parents[i])


N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]
find_parents(N, edges)