class treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def fun(target):
    arr = []
    arr.append(target.val)
    arr.append(target.left)
    arr.append(target.right)
    return arr


if __name__ == "__main__":
    p = treenode(1, 2, 3)
    q = treenode(1, 5, 3)
    p_arr = fun(p)
    q_arr = fun(q)
    if p_arr == q_arr:
        print("true")
    else:
        print("false")
