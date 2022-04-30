public:
	vector<int>SolveQueris(string str, vector<vector<int>>Query){
	    vector<int>ans;
	    for(int i=0;i<Query.size();i++)
	    {
	        int r=0;
	        vector<int>frq(26,0);
	        for(int j=Query[i][0]-1;j<Query[i][1];j++)
	        {
	           
	                frq[str[j]-'a']+=1;
	                if(frq[str[j]-'a']==1) r++;
	            
	            
	        }
	    
	        ans.push_back(r);
	        
	    }
	    return ans;
	    
	}
};
