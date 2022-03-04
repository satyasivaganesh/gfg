/User function Template for C++
class Solution{
    public:
    vector<int> canMakeTriangle(vector<int> A, int N){
        vector<int>v(N-2,0);
        int a,b,c;
        for(int i=0;i<N-2;i++)
        {
            a=A[i],b=A[i+1],c=A[i+2];
            if(a+b>c and b+c>a and a+c>b)
                v[i]=1;
        }
        return v;
