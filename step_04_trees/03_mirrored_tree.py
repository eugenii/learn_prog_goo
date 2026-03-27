# 03 Зеркальное дерево.

class Node:
    def __init__(self, obj, left=None, right=None):
        self.obj = obj
        self.left = left
        self.right = right

def solution(root) -> bool:
    stack = []
    if not root:
        return
    if not (root.left and root.right):
        return False
    stack.append((root.left, root.right))
    while stack:
        node_l, node_r = stack.pop()
        if node_l is None and node_r is None:
            continue
        if node_l.obj != node_r.obj:
            return False
        if (node_l is None or node_r is None) and node_l != node_r:
            return False
        stack.append((node_l.left, node_r.right))
        stack.append((node_l.right, node_r.left))
    return True

if __name__ == '__main__':
    # 1. Создаем узлы
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    node7 = Node(7)
    node6 = Node(6)
    node4 = Node(4)
    node5 = Node(5)
    node2 = Node(2, node4, node5)
    node3 = Node(3, node6, node7)
    root = Node(1, node2, node3)

    # В этом дереве листья — это 4, 5 и 3 (всего 3 шт)
    result = solution(root)
    print(result)