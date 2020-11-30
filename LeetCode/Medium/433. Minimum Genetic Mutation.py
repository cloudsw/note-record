def Minimum_Genetic_Mutation(start, end, bank):
    count = 0
    for i in range(len(start)):
        if start[i] != end[i]:
            count += 1
    if end in bank:
        return count
    else:
        return -1


if __name__ == '__main__':
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    res = Minimum_Genetic_Mutation(start, end, bank)
    print(res)
