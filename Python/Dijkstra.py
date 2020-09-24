import heapq
import math

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


def init(graph, s):     # 初始化距离，起始点设为零，其他点设为无穷
    distance = {s: 0}
    tem = graph.keys()
    for i in tem:
        if i != s:
            distance[i] = math.inf
    return distance


def dijkstra(graph, s):     # 运行heapq库，可以方便的进行，最小的数的排序
    arr = []
    distance = init(graph, s)
    heapq.heappush(arr, (distance[s], s))
    parent = {s: None}
    seen = set()

    while len(arr) > 0:
        tem = heapq.heappop(arr)
        dist = tem[0]
        vertex = tem[1]
        seen.add(vertex)    # 访问完的点
        node = graph[vertex].keys()
        for w in node:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(arr, (dist + graph[vertex][w], w))
                    distance[w] = dist + graph[vertex][w]
                    parent[w] = vertex
    return parent, distance


if __name__ == '__main__':
    list1 = []
    start = input("start point:")
    end = input("end point:")
    parent, distance = dijkstra(graph, start)
    print("从{}到{}的最短距离为：{}".format(start, end, distance[end]))
    while end != None:
        list1.append(end)
        end = parent[end]
    # print(parent)
    # print(distance)
    print("路径为：", end="")
    for i in range(len(list1)):
        print(list1.pop(), end=" ")
