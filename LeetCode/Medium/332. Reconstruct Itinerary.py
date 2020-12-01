def Reconstruct_Itinerary(arr):
    ans = 'JFK'
    res = ['JFK']
    while len(arr) > 0:
        for i in range(len(arr)):
            if arr[i][0] == ans:
                res.append(arr[i][1])
                ans = arr[i][1]
                arr.pop(i)
                break
    return res


if __name__ == '__main__':
    arr_list = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    res = Reconstruct_Itinerary(arr_list)
    print(res)
