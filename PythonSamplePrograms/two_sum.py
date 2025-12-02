class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(0, len(nums)):
            if target - nums[i] in nums_dict:
                return [nums_dict[target-nums[i]], i]
            else:
                nums_dict[nums[i]] = i


s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,7,11,15], 8))