# 03 Зеркальное дерево.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solution(root) -> bool:
    if not root:
        return True

    # Кладём ПАРУ узлов, которые должны быть зеркальны
    stack = [(root.left, root.right)]
    while stack:
        left, right = stack.pop()

        # 1. Если оба None — это симметрично, проверяем следующую пару
        if left is None and right is None:
            continue
            
        # 2. Если один None, а другой нет, ИЛИ значения разные — не симметрично
        if left is None or right is None or left.value != right.value:
            return False

        # 3. Кладём новые пары для проверки:
        # Внешние стороны: левый-левый и правый-правый
        stack.append((left.left, right.right))
        # Внутренние стороны: левый-правый и правый-левый
        stack.append((left.right, right.left))

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