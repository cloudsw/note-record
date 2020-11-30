def judge_node(parent, tem):
    while tem != parent[tem]:
        tem = parent[tem]
    return tem


def Redundant_Connection(node, count):
    parent = [i for i in range(count + 1)]
    for ver in node:
        node_1 = judge_node(parent, ver[0])
        node_2 = judge_node(parent, ver[1])
        if node_1 == node_2:
            return ver
        else:
            parent[ver[1]] = ver[0]


if __name__ == '__main__':
    node = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    res = Redundant_Connection(node, 5)
    print(res)
