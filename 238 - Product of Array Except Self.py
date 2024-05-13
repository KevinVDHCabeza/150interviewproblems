def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sol=[1]*len(nums)
    a=1
    for i in range(len(nums)):
        sol[i] *=a
        a *= nums[i]

    b=1
    for i in range(len(nums)-1,-1,-1):
        sol[i] *=b
        b*= nums[i]

    return sol


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(productExceptSelf(nums))


#Solucion valida pero no es rapida
#    for i,numi in enumerate(nums):
    #        num = 1
    #    for j,numj in enumerate(nums):
    #        if i!=j:
    #           num*=numj
#   sol.append(num)