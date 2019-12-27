'''https://www.interviewbit.com/problems/colorful-number/'''

from functools import reduce
class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A = str(A)
        p = []
        l = len(A)
        for i in range(l):
            for j in range(i+1,l+1):
                ll = list(map(int, A[i:j]))
                product = reduce((lambda x, y: x * y), ll)
                if product in p:
                    return 0
                else:
                    p.append(product)
        return 1