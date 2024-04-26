class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cont = 0
        for i in range(len(nums)):
            if nums[i - cont] == val:
                nums.remove(val)
                cont += 1

        return len(nums)