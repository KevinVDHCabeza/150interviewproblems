def removeDuplicates(nums):
    i = 0
    numero_veces=0
    while i!=len(nums)-1:
        if nums[i]==nums[i+1] and numero_veces==1:
            nums.remove(nums[i])
        elif nums[i]!=nums[i+1]:
            numero_veces=0
            i+=1
        elif nums[i]==nums[i+1]:
            numero_veces=1
            i+=1


    #return len(nums)



if __name__ == "__main__":
    nums=[1,1,1,2,2,3]
    removeDuplicates(nums)
    print(nums)