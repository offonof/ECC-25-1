N = int(input())
tree = {}
has_parent = [False] * (N+1)

for _ in range(N):
    node, left, right = map(int, input().split())
    tree[node] = (left, right)
    if left != -1:
        has_parent[left] = True
    if right != -1:
        has_parent[right] = True

# 부모가 없으면 루트
root = -1
for i in range(1, N+1):
    if not has_parent[i]:
        root = i
        break

column = 1
level_min = dict()
level_max = dict()

def inorder(node, level):
    global column
    if node == -1:
        return
    
    left, right = tree[node]
    inorder(left, level+1)

    # 현재 노드 column 처리
    if level not in level_min: # 방문한 적 없을 경우
        level_min[level] = column
        level_max[level] = column
    else:
        level_min[level] = min(level_min[level], column)
        level_max[level] = max(level_min[level], column)
    
    column += 1
    inorder(right, level+1)

inorder(root, 1)

# 너비 계산
max_width = 0
answer_level = 0
for level in sorted(level_min.key()):
    width = level_max[level] - level_min[level] + 1
    if width > max_width:
        max_width = width
        answer_level = level

print(answer_level, max_width)