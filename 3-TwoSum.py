class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        
        for key, num in enumerate(nums):
            search_number = target - num
            try:
                index = nums_dict[search_number]
                return key, index
            except:
                nums_dict[num] = key