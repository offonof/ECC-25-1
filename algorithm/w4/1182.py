```
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 
그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
```

def count_subsequences(N, S, numbers):
    count = 0

    def dfs(idx, current_sum):
        nonlocal count
        if idx == N:
            if current_sum == S:
                count += 1
            return
        # 포함하는 경우
        dfs(idx + 1, current_sum + numbers[idx])
        # 포함하지 않는 경우
        dfs(idx + 1, current_sum)

    dfs(0, 0)

    if S == 0:
        count -= 1

    return count

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
print(count_subsequences(N, S, numbers))
