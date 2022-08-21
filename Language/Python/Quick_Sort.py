def swap(arr1, i, j):
    tem = arr1[i]
    arr1[i] = arr1[j]
    arr1[j] = tem


def pivot(arr1, low, high):  # 找基点，一般以列表的第一个元素为基点
    tem = arr1[low]
    i = low
    j = high
    while i < j:
        while arr1[j] > tem and i < j:  # 从右往左，找出小于基点的元素
            j = j - 1
        while arr1[i] < tem and i < j:  # 从左往右，找出大于基点的元素
            i = i + 1
        swap(arr1, i, j)  # 进行交换，然后进行下一次循环
    return i  # 此时i, j的索引值一样


def quick_sort(arr1, low, high):
    if low < high:
        tem = pivot(arr1, low, high)
        # print(arr)
        quick_sort(arr1, low, tem - 1)
        quick_sort(arr1, tem + 1, high)


if __name__ == '__main__':
    arr = [7, 2, 5, 9, 1, 10, 6, 54, 100, 11]
    quick_sort(arr, 0, 9)
    print(arr)
