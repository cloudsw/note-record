def Find_the_Town_Judge(num, arr):
    sum_arr = [0]       # 用列表记录每个用户的投票数
    for i in range(1, num + 1):
        sum_arr.append(0)       # 初始化列表的内容都为0
    for tem in arr:
        sum_arr[tem[0]] -= 1
        sum_arr[tem[1]] += 1
    for j in range(1, num + 1):
        if sum_arr[j] == num - 1:
            return j
    return -1


if __name__ == '__main__':
    n, trust = 4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    re = Find_the_Town_Judge(n, trust)
    if re == -1:
        print('there is no judge. ')
    else:
        print('the judge is: {}'.format(re))
