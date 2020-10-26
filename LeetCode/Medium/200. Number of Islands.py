# 图


import numpy as np


def digui(grid, x, y, n, m):
    if x < 0 or y < 0 or x >= n or y >= m or grid[y][x] == 0:
        return
    grid[y][x] = 0
    digui(grid, x + 1, y, n, m)     # 使用递归，继续访问此节点的周围节点（子节点） 上，下，左，右
    digui(grid, x - 1, y, n, m)
    digui(grid, x, y + 1, n, m)
    digui(grid, x, y - 1, n, m)


def Number_of_Islands(grid):
    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    ans = 0
    for y in range(m):
        for x in range(n):
            if grid[y][x] == 1:
                ans += 1
                digui(grid, x, y, n, m)
    return ans


if __name__ == '__main__':
    arr = np.array([[1, 1, 1, 0, 1], [1, 1, 0, 1, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 0]])
    print(arr)
    print(Number_of_Islands(arr))
