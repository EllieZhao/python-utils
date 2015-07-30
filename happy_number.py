class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        l = []
        while True:
            s = 0
            while n > 0:
                s += (n%10) * (n%10)
                n = n/10
            n = s
            if n == 1:
                return True
            if n in l:
                return False
            l.append(s)

s = Solution()
print s.isHappy(7)
