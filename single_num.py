class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        x = 0
        for item in nums:
            x ^= item
        return x
