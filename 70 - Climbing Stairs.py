import math
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    sqrt5 = math.sqrt(5)
    fib_n = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1) #Binet formula for fibonacci
    return int(round(fib_n / sqrt5))

if __name__ == "__main__":
    n=3
    print(climbStairs(n))
