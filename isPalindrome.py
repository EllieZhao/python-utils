class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        ret = 0
        tmp = x
        while tmp > 0:
            ret = ret * 10 + tmp % 10
            tmp /= 10
        return x == ret
            
    def isPalindrome2(self, x):
        if x < 0 :
            return False
        div = 1
        while x / div >= 10:
            div *= 10
        while x != 0:
            l = x / div
            r = x % 10
            if l != r:
                return False
            x = (x % div) / 10
            div /= 100
        return True
            
s = Solution()
print s.isPalindrome(0)
print s.isPalindrome(-1)
print s.isPalindrome(123)
print s.isPalindrome(12321)
print s.isPalindrome(12321)
print s.isPalindrome(1234567890987654321)
print s.isPalindrome(2147483647)
print s.isPalindrome(2147483648)
print s.isPalindrome(111111111111111111111111111111111111111111111111111111111111111111111111111111111111)
