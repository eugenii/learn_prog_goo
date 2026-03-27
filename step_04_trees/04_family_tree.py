# 04 Семейное дерево

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solution(root, x) -> int:
    if not root:
        return 0
    if root.value == x:
        return True
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            if node.left.value == x:
                return True
            stack.append(node.left)
        if node.right:
            if node.right.value == x:
                return True
            stack.append(node.right)

    return False

if __name__ == '__main__':
    # 1. Создаем узлы
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    node4 = Node(4)
    node5 = Node(5)
    node2 = Node(2, node4, node5)
    node3 = Node(3)
    root = Node(1, node2, node3)
    print(solution(root, 3))
    