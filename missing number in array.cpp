class Solution{
  public:
    int MissingNumber(vector<int>& array, int n) {
        int s=0;
        int sum=n*(n+1)/2;
        for(auto it:array)
        {
            s+=it;
        }
        return sum-s;
