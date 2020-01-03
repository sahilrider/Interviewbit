'''https://www.interviewbit.com/problems/longest-substring-without-repeat/'''
'''Use python2 for interviewbit submission'''

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        h = {}
        i = 0
        ans = 0
        for j, val in enumerate(A):
            if val in h:
                i = max(i, h[val])
            ans = max(ans, j-i+1)
            h[val] = j+1
        return ans
