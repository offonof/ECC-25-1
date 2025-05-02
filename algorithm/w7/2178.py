```
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 
(N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
```

from collections import deque

# 입력 받기
n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):  # 상하좌우 4방향
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖은 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 벽(0)이면 무시
            if maze[nx][ny] == 0:
                continue

            # 처음 방문하는 길이라면, 거리 기록 후 큐에 추가
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  # 거리 누적
                queue.append((nx, ny))

    return maze[n-1][m-1]  # 도착지의 거리 리턴

# 출력
print(bfs(0, 0))
