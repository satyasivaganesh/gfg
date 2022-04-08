public:
    vector<int> print_next_greater_freq(int arr[],int n)
    {
        map<int,int>dict;
        for(int i=0;i<n;i++)
        {
          dict[arr[i]]+=1;
        }
        vector<int>frq(n,0);
        for(int i=0;i<n;i++)
        {
            frq[i]=dict[arr[i]];
            //cout<<dict[arr[i]]<<' ';
        }
        stack<int>st;
        st.push(n-1);
        vector<int>ans(n,-1);
        for(int i=n-2;i>-1;i--)
        {
            if(frq[i]<frq[st.top()])
            {
                ans[i]=arr[st.top()];
                st.push(i);
            }
            else
            {
                while(!st.empty() and frq[i]>=frq[st.top()])
                    st.pop();
                if(st.empty())
                    ans[i]=-1;
                else
                    ans[i]=arr[st.top()];
                st.push(i);
            }
        }
        return ans;
        
        
    }
};
