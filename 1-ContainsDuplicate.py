class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = {}
        for num in nums:
            if num in temp:
                return True
            temp[num] = True
        return False