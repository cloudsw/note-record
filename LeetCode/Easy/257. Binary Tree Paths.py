class treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def Binary_Tree_Paths(root, path):
    if root:
        path += str(root.val)        # 用字符串储存值
        if not root.left and not root.right:    # 判断是否为叶子节点
            sum.append(path)
        else:
            path += '->'
            Binary_Tree_Paths(root.left, path)    # 储存在path里的值，继续让递归子函数使用
            Binary_Tree_Paths(root.right, path)


if __name__ == '__main__':
    sum = []
    path = ''
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
    Binary_Tree_Paths(a, path)
    print(sum)

