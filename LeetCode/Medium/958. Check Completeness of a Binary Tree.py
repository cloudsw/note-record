class treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def fun(sum):
    tem = sum[::-1]
    while tem:
        if tem[0] is None:
            tem.pop(0)
        else:
            break
    return tem[::-1]


def Check_Completeness_of_a_Binary_Tree(root, sum):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            sum.append(None)
        else:
            sum.append(node.val)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    tem = fun(sum)
    if None in tem:
        return False
    else:
        return True


if __name__ == '__main__':
    sum = []
    a = treenode(1)
    b = treenode(2)
    c = treenode(3)
    d = treenode(4)
    e = treenode(5)
    f = treenode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    print(Check_Completeness_of_a_Binary_Tree(a, sum))
