```
세준이는 크기가 N×N인 배열 A를 만들었다. 
배열에 들어있는 수 A[i][j] = i×j 이다. 
이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. 
B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다.
```

n = int(input())
k = int(input())

def count_less_equal(x):
    count = 0
    for i in range(1, n + 1):
        count += min(x // i, n)
    return count

left, right = 1, k
answer = 0

while left <= right:
    mid = (left + right) // 2
    if count_less_equal(mid) >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
