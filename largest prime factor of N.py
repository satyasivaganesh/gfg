class Solution:
    def largestPrimeFactor (self, N):
        t=[0]*(N+1)
        t[0]=t[1]=1
        for i in range(2,N//2+1):
            for j in range(i*i,N+1,i):
                if t[j]==0:
                    t[j]=1
        for i in range(N,1,-1):
            if t[i]==0:
                if N%i==0:
                    return i
