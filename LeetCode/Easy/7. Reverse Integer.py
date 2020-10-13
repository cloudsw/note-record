def Reverse_Integer(arr):
    arr.reverse()   # reverse()翻转本身，没有返回值
    return arr


if __name__ == '__main__':
    arr = [2, 5, 9, 45, 32]
    tem = Reverse_Integer(arr)
    print(tem)
    
