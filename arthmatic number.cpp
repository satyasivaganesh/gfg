class Solution{
public:
    int inSequence(int A, int B, int C){
        if(A==B)return 1;
        if(C==0)return A==B;
        if((B-A)%C==0 and (B-A)/C>0)return 1;
        return 0;
