import math

def Longest_Common_Prefix(target):
    length = math.inf
    list_a = []
    str_a = ""
    str_b = ""
    for i in range(len(target)):
        list_a.append(target[i])
        if len(list_a[i]) < length:
            length = len(list_a[i])
            str_a = list_a[i]

    for i in range(length):
        for j in range(len(target)):
            if str_a[i] == target[j][i]:
                if j == len(target) - 1 and str_a[i] == target[j][i]:
                    str_b = str_b + str_a[i]
            else:
                break
    return str_b


if __name__ == '__main__':
    tar = ["flower", "flow", "flight"]
    print(Longest_Common_Prefix(tar))
