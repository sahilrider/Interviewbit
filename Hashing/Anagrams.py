'''https://www.interviewbit.com/problems/anagrams/'''

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        s = {}
        for idx, i in enumerate(A):
            t = ''.join(sorted(i))
            if t not in s:
                s[t] = [idx+1]
            else:
                s[t].append(idx+1)
        # print(s)
        return(list(s.values()))