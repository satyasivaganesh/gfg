def calculate (arr, n) :
    c=0
    dict={}
    for i in arr:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    for i in dict:
        if dict[i]>1:
            x=dict[i]-1
            c+=x*(x+1)//2
    return c
            
