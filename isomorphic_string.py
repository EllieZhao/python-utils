class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        d = {}
        for idx, char in enumerate(s):
            if char in d:
                if t[idx] != d[char]:
                    return False
            else:
                d[char] = t[idx]
        if len(d.values()) != len(set(d.values())):
            return False
        return True

s = Solution()
print s.isIsomorphic('egg', 'add')
print s.isIsomorphic('paper', 'title')
print s.isIsomorphic('ab', 'aa')
