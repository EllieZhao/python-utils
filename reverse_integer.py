class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x < -4294967296 or x >= 4294967296:
            return 0
        s = 0
        flag = False
        if x < 0:
            x = 0 - x
            flag = True
        while x > 0:
            s = s * 10 + x % 10
            x = x/10
        if s < -4294967296 or s >= 4294967296:
            return 0
        return 0 - s if flag else s

s = Solution()
print s.reverse(1000)
print s.reverse(-123)
