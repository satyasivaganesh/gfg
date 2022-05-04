vector<int> findSpiral(Node *root)
{
    if(root==NULL)return {};
    deque<Node*>q;
    vector<int>v;
    q.push_front(root);
    int fl=0;
    while(!q.empty())
    {
        int l=q.size();
        for(int i=0;i<l;i++)
        {
            if(fl)
            {
                if(q.front()->left) q.push_back(q.front()->left);
                if(q.front()->right) q.push_back(q.front()->right);
                v.push_back(q.front()->data);
                q.pop_front();
            }
            else
            {
                if(q.back()->right) q.push_front(q.back()->right);
                if(q.back()->left) q.push_front(q.back()->left);
                v.push_back(q.back()->data);
                q.pop_back();
            }
        }
        if(fl==0) fl=1;
        else fl=0;
    }
    return v;
}
