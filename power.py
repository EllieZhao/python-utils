class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n < 1 :
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 2 != 0:
                return False
            n /= 2
        return True

s = Solution()
print s.isPowerOfTwo(8)
print s.isPowerOfTwo(9)
print s.isPowerOfTwo(12)
print s.isPowerOfTwo(0)
print s.isPowerOfTwo(1)
