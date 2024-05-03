def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 1:
        return 1

    guess = x / 2
    while guess * guess > x:
        guess = (guess + x / guess) / 2 # newton-raphson

    #return guess

#other way

    n = 0
    while n * n <= x:
        n += 1
    return n-1

if __name__ == "__main__":
    x=1
    print(mySqrt(x))
