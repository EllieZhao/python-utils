class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        last_count = 0
        count = 0
        for item in s:
            if item != ' ':
                count += 1
            else:
                if count:
                    last_count = count
                count = 0
        return count if count else last_count

s = Solution()
print s.lengthOfLastWord('helloworld     ')

