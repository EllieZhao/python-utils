class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if not nums:
            return False
        d = {}
        for item in nums:
            d[item] = None
        if len(nums) > len(d):
            return True
        return False

    def split(self, nums, k):
        ls = []
        l = []
        for item in nums:
            if len(l) == k:
                ls.append(l)
                l = []
            l.append(item)
        if l:
            ls.append(l)
        return ls
        
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if not nums:
            return False
        ls = self.split(nums, k+1)
        for lindex, l in enumerate(ls):
            if self.containsDuplicate(l):
                return True
            for iindex, item in enumerate(l[1:]):
                if (lindex+1)*(k+1) >= len:
                    break
                x = nums[(lindex+1)*(k+1) : min(len(nums), (lindex+1)*(k+1)+iindex+1)]
                if item in x:
                    return True
        return False

s = Solution()
#l = [1,2,3,4,5,1]
#print s.containsNearbyDuplicate(l, 1)
#print s.containsNearbyDuplicate(l, 2)
#print s.containsNearbyDuplicate(l, 3)
#print s.containsNearbyDuplicate(l, 4)
#print s.containsNearbyDuplicate(l, 5)

#l = [-1, -1]
#print s.containsNearbyDuplicate(l, 1)

#l = [0,1,2,3,2,5]
#print s.containsNearbyDuplicate(l, 3)

#l = [0,1,2,3,4,5,6,7,8]
#print s.containsNearbyDuplicate(l, 5)

#l = [1,2,3,1,2,3]
#print s.containsNearbyDuplicate(l, 2)

l = range(10000)
ls = s.split(l,2)
