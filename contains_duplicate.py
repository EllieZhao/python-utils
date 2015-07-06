class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if not nums:
            return False
        d = {}
        for item in nums:
            d[item] = None
        if len(d) < len(nums):
            return True
        return False


s = Solution()
l = [1,2,3,4]
print s.containsDuplicate(l)
l.append(3)
print s.containsDuplicate(l)
l = None
print s.containsDuplicate(l)
