class tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def Binary_Tree_Level_Order_Traversal_II(target):       # 利用BFS(结合队列)
    if not target:
        return []
    queue = [target]
    sum = []
    while queue:
        tem = []
        for _ in range(len(queue)):     # 此时queue的长度，用作后面queue.pop()取出的次数，就是树的一层的节点数
            node = queue.pop(0)
            tem.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        sum.append(tem)
    return sum[::-1]


if __name__ == '__main__':
    a = tree(3)
    b = tree(9)
    c = tree(20)
    d = tree(15)
    e = tree(7)
    f = tree(6)

    a.left = b
    a.right = c
    b.right = f
    c.left = d
    c.right = e

    result = Binary_Tree_Level_Order_Traversal_II(a)
    print(result)
