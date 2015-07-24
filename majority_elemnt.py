class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement1(self, nums):
        d = {}
        n = len(nums)
        for item in nums:
            if item in d.keys():
                d[item] += 1
            else:
                d[item] = 1
            if d[item] > n/2:
                return item

    def majorityElement(self, nums):
        l = sorted(nums)
        return l[len(nums)/2]

s = Solution()
l = [1,2,2,1,1]
print s.majorityElement1(l)
