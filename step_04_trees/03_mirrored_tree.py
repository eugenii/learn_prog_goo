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
    # Структура:
#      1
#     / \
#    2   2  <-- левая и правая ветки должны быть зеркальны
#   / \ / \
#  3  4 4  3

    node3_l = Node(3)
    node4_l = Node(4)
    node2_l = Node(2, node3_l, node4_l) # Левая ветка

    node4_r = Node(4)
    node3_r = Node(3)
    node2_r = Node(2, node4_r, node3_r) # Правая ветка (зеркальная!)

    root = Node(1, node2_l, node2_r) # Собираем всё под один корень

    print(solution(root)) # Должно быть True