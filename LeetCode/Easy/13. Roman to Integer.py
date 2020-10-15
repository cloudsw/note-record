def Roman_to_Integer(target):
    sum_res = 0
    dict_a = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    for i in range(len(target)):
        if i + 1 == len(target):
            tem1 = target[i]
            tem2 = target[i]
        else:
            tem1 = target[i]
            tem2 = target[i + 1]
        if dict_a[tem1] < dict_a[tem2]:
            sum_res = sum_res + (-dict_a[tem1])
        else:
            sum_res = sum_res + dict_a[tem1]

    return sum_res


if __name__ == '__main__':
    tar = 'MCMXCIV'
    print(Roman_to_Integer(tar))
