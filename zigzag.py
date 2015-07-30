class Solution:

    def get(self, numRows):
        res = []
        for n in range(numRows):
            x = []
            res.append(x)
        return res

    def to_string(self, res):
        s = ''
        for item in res:
            s += ''.join(item)
        return s

    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if not s:
            return ''
        res = self.get(numRows)
        while s:
            n = 0
            while n < numRows:
                res[n].append(s[0])
                n += 1
                if len(s) > 1:
                    s = s[1:]
                else:
                    return self.to_string(res)

            while n > 2:
                res[n-2].append(s[0])
                n -= 1
                if len(s) > 1:
                    s = s[1:]
                else:
                    return self.to_string(res)
        

s = Solution()
print s.convert('PAYPALISHIRING', 3) ## PAHNAPLSIIGYIR

#P   A   H   N
#A P L S I I G  
#Y   I   R
