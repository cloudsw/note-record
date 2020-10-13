def two_sum(arr, target):
    count = 0
    for i in arr:
        tem = target - i
        if tem in arr[count:]:
            num = arr.index(tem)    #求出当前值在列表中的索引
            return count, num
            break
        else:
            count = count + 1


if __name__ == '__main__':
    arr = [11, 2, 7, 15, 5]
    a, b = two_sum(arr, 7)
    print("[{}, {}]".format(str(a), str(b)))
    
