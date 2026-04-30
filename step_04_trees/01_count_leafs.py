# 01 Считаем листья

class Node:
    def __init__(self, obj, left=None, right=None):
        self.obj = obj
        self.left = left
        self.right = right


def solution(root) -> int:
    if root is None:
        return 0
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        if node.left is None and node.right is None:
            count += 1
            continue
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return count

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

    # В этом дереве листья — это 4, 5 и 3 (всего 3 шт)
    result = solution(root)
    print(f"Количество листьев: {result}")
    
    # Простая проверка (assert)
    assert result == 3, f"Ожидалось 3, но получили {result}"
    print("Тест пройден успешно!")
