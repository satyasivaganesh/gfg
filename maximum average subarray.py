class Solution:
    def findMaxAverage(self, arr, n, k):
        s=0
        for j in range(k):
            s+=arr[j]
        avg=s/k
        ind=0
        x=0
        for i in range(1,(n-k)+1):
            #print(i)
            s-=arr[x]
            s+=arr[(i+k)-1]
            if (s/k)>=avg:
                avg=(s/k)
                ind=i
            x+=1
        return ind
