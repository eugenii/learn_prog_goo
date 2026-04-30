# 02 Глубина норы.

class Node:
    def __init__(self, obj, left=None, right=None):
        self.obj = obj
        self.left = left
        self.right = right


def solution(root: Node) -> int:
    if root is None:
        return 0
    max_level = 0
    stack = [(root, 1)]
    while stack:
        node, level = stack.pop()

        max_level = max(max_level, level)
        
        if node.left:
            stack.append((node.left, level + 1))
        if node.right:
            stack.append((node.right, level + 1))
    return max_level


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

    