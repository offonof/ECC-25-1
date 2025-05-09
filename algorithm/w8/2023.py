```
수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 
요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.

7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 
즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다! 수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.

수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. 
N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.
```
import sys
import math

# 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 백트래킹 DFS 함수
def dfs(num, length):
    if len(str(num)) == length:
        print(num)
        return
    for i in range(1, 10):
        new_num = num * 10 + i
        if is_prime(new_num):
            dfs(new_num, length)

# 입력 받기
N = int(sys.stdin.readline())

# 1자리 소수부터 시작
for start in [2, 3, 5, 7]:
    dfs(start, N)
