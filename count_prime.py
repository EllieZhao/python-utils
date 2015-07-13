from math import sqrt

class Solution:
    def isPrimes(self, n):
        for i in range(2, int(sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        """
        count = 0
        for i in range(2, n):
            if self.isPrimes(i):
                count += 1
        return count
        """
        """
        count = 0
        l = range(2,n)
        for i in range(2, int(sqrt(n)+1)):
            t = i*i
            while t < n:
                if t in l:
                    l.remove(t)
                t += i
        return len(l)
        """
        count = 0
        l = [1 for _ in xrange(2, n)]
        for i in range(2, int(sqrt(n)+1)):
            if l[i-2] == 1:
                t = i * i
                while t < n:
                    l[t-2] = 0
                    t += i
        return sum(l)
            

s = Solution()

print s.countPrimes(499979) ## 41537
print s.countPrimes(20) ## 8
print s.countPrimes(100) ## 25
print s.countPrimes(5)
