class treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def Path_Sum(root, sum):
    if not root:
        return False
    node = [root]
    path = [root.val]
    while node:
        que_node = node.pop(0)      # 存放节点
        que_path = path.pop(0)      # 存放当前节点到root节点的路径总和
        if not que_node.left and not que_node.right and que_path == sum:
            return True
        if que_node.left:
            node.append(que_node.left)
            path.append(que_node.left.val + que_path)
        if que_node.right:
            node.append(que_node.right)
            path.append(que_node.right.val + que_path)
    return False


if __name__ == '__main__':
    a = treenode(5)
    b = treenode(4)
    c = treenode(8)
    d = treenode(11)
    e = treenode(13)
    f = treenode(4)
    g = treenode(7)
    h = treenode(2)
    i = treenode(1)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    c.right = f
    d.left = g
    d.right = h
    e.right = i
    print(Path_Sum(a, 22))


