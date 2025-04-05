class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

class BinaryTree:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value, left, right):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        node = self.nodes[value]

        if left != '.': # 말단 노드가 아니면
            if left not in self.nodes: # 왼쪽 노드 값이 없으면
                self.nodes[left] = Node(left) # 노드 생성자를 이용해서 라이브러리?에 저장
            node.left = self.nodes[left] # 있거나... 위에서 생성한 노드를 변수에 저장

        if right != '.': # 말단 노드가 아니면
            if right not in self.nodes: # 오른쪽 노드 값이 없으면
                self.nodes[right] = Node(right) # 노드 생성자를 이용해서 라이브러리?에 저장
            node.right = self.nodes[right] # 있거나... 위에서 생성한 노드를 변수에 저장

    def preorder(self, node):
        if node:
            return node.value + self.preorder(node.left) + self.preorder(node.right)
        return ""

    def inorder(self, node):
        if node:
            return self.inorder(node.left) + node.value + self.inorder(node.right)
        return ""
        
    def postorder(self, node):
        if node:
            return self.postorder(node.left) + self.postorder(node.right) + node.value
        return ""

N = int(input())
tree = BinaryTree()

for _ in range(N):
    value, left, right = input().split()
    tree.add_node(value, left, right)

root = tree.nodes['A']
print(tree.preorder(root))
print(tree.inorder(root))
print(tree.postorder(root))