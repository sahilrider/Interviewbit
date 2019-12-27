'''https://www.interviewbit.com/problems/2-sum/'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        d = {}
        for i in range(len(A)):
            n = B - A[i]
            if n not in d:
                if A[i] not in d:
                    d[A[i]]=i
            else:
                return [d[n]+1, i+1]
        return []     