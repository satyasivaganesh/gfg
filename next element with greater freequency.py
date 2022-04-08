class Solution:
    def print_next_greater_freq(self,arr,n):
        dict={}
        for i in range(n):
            if arr[i] not in dict:
                dict[arr[i]]=1
            else:
                dict[arr[i]]+=1
        frq=[0]*n
        for i in range(n):
            frq[i]=dict[arr[i]]
        st=[n-1]
        ans=[-1]*n
        #print(frq)
        for i in range(n-2,-1,-1):
            #print(st)
            if frq[i]<frq[st[-1]]:
                ans[i]=arr[st[-1]]
                st+=[i]
            else:
                while len(st) and frq[i]>=frq[st[-1]]:
                    st.pop()
                if len(st)==0:
                    ans[i]=-1
                else:
                    ans[i]=arr[st[-1]]
                st+=[i]
        return ans
