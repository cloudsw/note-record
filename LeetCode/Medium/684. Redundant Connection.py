class Redundant_Connection:     # 采用并查集来判断是否存在环
    def __init__(self, vertex, count):
        self.vertex = vertex
        self.parent = [i for i in range(count + 1)]

    def find(self, tem):
        while tem != self.parent[tem]:
            tem = self.parent[tem]
        return tem

    def union(self):
        for ver in self.vertex:
            node_1, node_2 = self.find(ver[0]), self.find(ver[1])
            if node_1 == node_2:
                return ver
            else:
                self.parent[ver[1]] = ver[0]


if __name__ == '__main__':
    node = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    res = Redundant_Connection(node, 5)
    print(res.union())
