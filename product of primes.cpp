class Solution{
public:
    long long primeProduct(long long L, long long R){
        long long int ans=1;
        for(int i=L;i<=R;i++)
        {
            int ref=0;
            for(int j=2;j*j<=i;j++)
            {
                if(i%j==0)
                {
                    ref=1;
                    break;
                }
            }
            if(ref==0)
            {
                ans=(ans*i)%1000000007;
            }
        }
        return ans%1000000007;
    
    }
};
