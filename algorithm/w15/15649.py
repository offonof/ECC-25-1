```
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
```

def backtrack(path, used):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    for i in range(1, N + 1):
        if not used[i]:
            used[i] = True
            backtrack(path + [i], used)
            used[i] = False

N, M = map(int, input().split())
used = [False] * (N + 1)
backtrack([], used)
