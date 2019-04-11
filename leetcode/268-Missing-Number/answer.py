class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum1 = sum(nums)
        sums = ((n+1) * n) >> 1
        return sums - sum1
