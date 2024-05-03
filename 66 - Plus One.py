def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    a = ""
    c = []
    for i in range(len(digits)):
        a += str(digits[i])
    b = str(int(a) + 1)
    for i in range(len(b)):
        c.append(int(b[i]))
    return c



if __name__ == "__main__":
    digits= [1,2,3]
    print(plusOne(digits))