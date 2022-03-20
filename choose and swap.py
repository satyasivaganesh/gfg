#User function Template for python3


class Solution:
    def chooseandswap (self, A):
        t=[0]*26
        ch1=""
        ch2=""
        for i in A:
            t[ord(i)-97]=1
        ref=0
        for i in range(len(A)):
            for j in range(26):
                if t[j] and (ord(A[i])-97)==j:
                    t[j]=0
                elif t[j] and (ord(A[i])-97)>j:
                    ch1=A[i]
                    ch2=chr(97+j)
                    ref=1
                    break
            if ref==1:
                break
        s=''
        for i in A:
            if i==ch1:
                s+=ch2
            elif i==ch2:
                s+=ch1
            else:
                s+=i
        return s
