# 01 Считаем листья

class Node:
    def __init__(self, obj, left=None, right=None):
        self.obj = obj
        self.left = left
        self.right = right

def count_leafs(root) -> int:
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
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    print(count_leafs(root))
    