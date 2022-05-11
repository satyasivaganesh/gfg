{
    public:
    //Function to check whether a Binary Tree is BST or not.
    void inorder(Node* root,vector<int>&v)
    {
        if(root)
        {
            inorder(root->left,v);
            v.push_back(root->data);
            inorder(root->right,v);
        }
    }
    bool isBST(Node* root) 
    {
        vector<int>v;
        inorder(root,v);
        int ref=0;
        for(int i=1;i<v.size();i++)
        {
            if(v[i]<v[i-1])
            {
                ref=1;
                break;
            }
        }
        if(ref==0)return 1;
        return 0;
    }
};
