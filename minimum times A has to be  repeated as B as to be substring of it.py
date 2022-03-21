
class Solution:
    def minRepeats(self, A, B):
        c=0
        y=A
        ans=-1
        for i in range(len(A)):
            if A[i]==B[0]:
                ref=0
                x=A[i::]+A[:i:]
                for j in range(len(A)):
                    if x[j]!=B[j]:
                        ref=1
                        break
                if ref==0:
                    ans=i
                    break
        if ans==-1:
            return -1
        c=1
        j=ans
        for i in range(len(B)):
            if A[j]!=B[i]:
                return -1
            else:
                j+=1
            if j>=len(A) and i!=len(B)-1:
                A=A+y
                c+=1
        return c
            
