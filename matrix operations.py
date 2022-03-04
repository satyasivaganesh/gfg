#User function Template for python3

class Solution:
    def endPoints(self, mat, m, n):
        i=0
        j=0
        rf=1
        df=0
        lf=0
        uf=0
        while (i<m and j<n) and (i>=0 and j>=0):
            if mat[i][j]==1:
                if rf==1:
                    mat[i][j]=0
                    df=1
                    rf=0
                    i+=1
                elif df==1:
                    mat[i][j]=0
                    lf=1
                    df=0
                    j-=1
                elif uf==1:
                    mat[i][j]k=0
                    uf=0
                    rf=1
                    j+=1
                elif lf==1:
                    mat[i][j]=0
                    lf=0
                    uf=1
                    i-=1
            else:
                if rf==1:
                    j+=1
                elif df==1:
                    i+=1
                elif lf==1:
                    j-=1
                elif uf==1:
                    i-=1
        if rf==1:
            return (i,j-1)
        elif lf==1:
            return (i,j+1)
        elif uf==1:
            return (i+1,j)
        elif df==1:
            return (i-1,j)
