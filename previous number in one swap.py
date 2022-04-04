#User function Template for python3
class Solution:
    def previousNumber (ob,s):
        s=list(s)
        ref=0
        for i in range(len(s)-2,-1,-1):
            x=s[i+1]
            if s[i]>x:
                y=i
                ref=1
                break
        if ref==0:
            return -1
        d=int(s[y])-int(s[y+1])
        j=y+1
        for k in range(j,len(s),1):
            diff=int(s[y])-int(s[k])
            if diff>0 and diff<d and s[y]!=s[k]:
                d=diff
                j=k
        s[y],s[j]=s[j],s[y]
      
        if s[0]=='0':
            return -1
        return ''.join(s)
