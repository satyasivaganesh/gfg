public:
    vector<int> subsetSums(vector<int> arr, int N)
    {
        vector<int>v;
        for(int i=0;i<pow(2,arr.size());i++)
        {
            int su=0;
            int x=i;
            int ind=arr.size()-1;
            while(x)
            {
                int r=x&1;
                if(r)
                {
                    su+=arr[ind];
                }
                x=x>>1;
                ind--;
            }
            v.push_back(su);
        }
        return v;
    }
};
