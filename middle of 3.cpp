class Solution{
  public:
    int middle(int A, int B, int C){
        int ma=max(A,max(B,C));
        int mi=min(A,min(B,C));
        return A^B^C^mi^ma;
    }
};
