class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_ptr = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_ptr] = nums[i]
                unique_ptr += 1

        return unique_ptr