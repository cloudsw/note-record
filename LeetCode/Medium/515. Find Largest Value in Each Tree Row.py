class treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def Find_Largest_Value_in_Each_Tree_Row(root, sum):
    queue = []
    queue.append(root)
    while queue:
        tem = []
        tem_lenght = len(queue)
        for i in range(tem_lenght):     # for作用：遍历树的每一行，遍历结束后进行下一行的遍历
            que_node = queue.pop(0)
            tem.append(que_node.val)
            if i + 1 == tem_lenght:
                sum.append(max(tem))
            if que_node.left:
                queue.append(que_node.left)
            if que_node.right:
                queue.append(que_node.right)


if __name__ == '__main__':
    sum = []
    a = treenode(1)
    b = treenode(3)
    c = treenode(2)
    d = treenode(5)
    e = treenode(3)
    f = treenode(9)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    Find_Largest_Value_in_Each_Tree_Row(a, sum)
    print(sum)
