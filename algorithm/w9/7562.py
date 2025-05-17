```
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

나이트의 이동 방식
(2, 1), (1, 2), (-1, 2), (-2, 1),
(-2, -1), (-1, -2), (1, -2), (2, -1)
```

from collections import deque

# 나이트가 이동할 수 있는 8가지 방향
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

# 테스트 케이스 개수 입력
t = int(input())

for _ in range(t):
    l = int(input())  # 체스판 크기
    x1, y1 = map(int, input().split())  # 시작 위치
    x2, y2 = map(int, input().split())  # 도착 위치

    visited = [[False] * l for _ in range(l)]
    distance = [[0] * l for _ in range(l)]

    queue = deque()
    queue.append((x1, y1))
    visited[x1][y1] = True

    while queue:
        x, y = queue.popleft()

        if x == x2 and y == y2:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    print(distance[x2][y2])
