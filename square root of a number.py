class Solution:
    def floorSqrt(self, x): 
        i=1
        j=x
        mi=0
        while i<=j:
            m=(i+j)//2
            if m*m==x:
                return m
            elif m*m>x:
                j=m-1
            elif m*m<x:
                mi=m
                i=m+1
        return mi
