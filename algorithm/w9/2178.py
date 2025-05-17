```
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 
지나야하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다.
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
```

from collections import deque

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력
n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]

# BFS 함수
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 이동 가능한 칸이고 방문하지 않았다면
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1  # 거리 누적
                    queue.append((nx, ny))

# 시작점에서 BFS 시작
bfs(0, 0)

# 도착점에 기록된 거리 출력
print(maze[n-1][m-1])
