class linked_node:
    def __init__(self, target):     # 在python中用类表示链表
        self.data = target
        self.next = None

class tree:
    def __init__(self, root):       # 在python中二叉树的表示方法
        self.root = root
        self.lnext = None
        self.rnext = None

class treenode:
    def __init__(self, val=0, left=None, right=None):       # 初始化二叉树
        self.val = val
        self.left = left
        self.right = right


def show(tem):
    while tem:
        print(tem.data, end=' ')
        tem = tem.next


if __name__ == "__main__":
    a = linked_node(1)
    b = linked_node(2)
    c = linked_node(3)
    a.next = b
    b.next = c
    d = treenode()
    print(d.val)
    show(a)
