class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []
        l = []
        begin = nums[0]
        end = begin
        for item in nums[1:]:
            if item == end + 1:
                end = item
            else:
                if begin == end:
                    l.append(str(begin))
                else:
                    l.append(str(begin) + "->" + str(end))
                begin = item
                end = begin
        if begin == end:
            l.append(str(begin))
        else:
            l.append(str(begin) + "->" + str(end))
        return l

s = Solution()
l = [0,1,2,4,5,7,8,10,15]
print s.summaryRanges(l)

