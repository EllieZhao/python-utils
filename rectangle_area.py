class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        s = (D - B) * (C - A) + (H - F) * (G - E)
        a = max(A, E)
        b = min(C, G)
        c = min(D, H)
        d = max(F, B)
        if b - a < 0 or c - d < 0:
            return s
        else:
            return s - (b-a) * (c-d)

s = Solution()
print s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
print s.computeArea(0, 0, 0, 0, -1, -1, 1, 1)
