```
세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 
이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다.
```

def count_less_equal(x, n):
    count = 0
    for i in range(1, n + 1):
        count += min(n, x // i)
    return count

# 입력
n = int(input())
k = int(input())

# 이진 탐색
low = 1
high = k  # 최댓값은 N×N보다 클 수 없음

while low < high:
    mid = (low + high) // 2
    if count_less_equal(mid, n) < k:
        low = mid + 1
    else:
        high = mid

print(low)
