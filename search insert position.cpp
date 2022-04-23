class Solution{
    public:
    int searchInsertK(vector<int>Arr, int N, int k)
    {
        int l=0;
        int u=N-1;
        while(l<=u)
        {
            int m=(l+u)/2;
            if(Arr[m]==k) return m;
            else if(Arr[m]<k)
            {
                l=m+1;
            }
            else if(Arr[m]>k) u=m-1;
        }
        return l;
    }
};
