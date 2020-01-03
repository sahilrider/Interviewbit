'''https://www.interviewbit.com/problems/points-on-the-straight-line/'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        l = len(A)
        if l==0:
            return 0
        if l<2:
            return 1
        result = 0
        for i in range(l):
            mymap, vert, dup = {}, 0, 0
            for j in range(i+1, l):
                ax, ay = A[i], B[i]
                bx, by = A[j], B[j]
                if ax==bx:
                    if ay != by:
                        vert+=1
                    else:
                        dup+=1
                else:
                    m = float(by-ay)/float(bx-ax)
                    mymap[m] = mymap.setdefault(m,0)+1
            try:
                slopeMax = max(mymap.values())
            except:
                slopeMax = 0
            maxPointOnLine = max(slopeMax, vert)+dup
            if maxPointOnLine>result:
                result = maxPointOnLine
        return result+1
