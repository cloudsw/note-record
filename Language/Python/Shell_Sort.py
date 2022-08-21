def swap(arr, i, j):
    tem = arr[i]
    arr[i] = arr[j]
    arr[j] = tem


def shell_sort(arr):
    # print(len(arr))
    gap = int(len(arr) / 2)  # 靠gap的缩减慢慢进行简单排序
    while gap > 0:
        if gap > 1:
            for i in range(0, len(arr)):
                if i + gap < len(arr):
                    if arr[i] > arr[i + gap]:
                        swap(arr, i, i + gap)
        else:  # 当gap是1时，直接使用插入排序
            i = gap
            while i < len(arr):
                j = i - 1
                tem = arr[i]
                while j >= 0:
                    if arr[j] > tem:
                        arr[j + 1] = arr[j]
                        j = j - 1
                    else:
                        break
                arr[j + 1] = tem
                i = i + 1
        gap = int(gap / 2)


if __name__ == '__main__':
    arr1 = [8, 2, 5, 9, 10, 6]
    shell_sort(arr1)
    print(arr1)
