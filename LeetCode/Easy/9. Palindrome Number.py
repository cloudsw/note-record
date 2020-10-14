def Palindrome_Number(target):
    res = 0
    tem = target
    for i in str(tem):
        a = tem % 10
        tem = tem // 10
        res = res * 10 + a
    if res == target:
        print("This is a Palindrome Number")
    else:
        print("This isn't a Palindrome Number")


if __name__ == '__main__':
    Palindrome_Number(121)
