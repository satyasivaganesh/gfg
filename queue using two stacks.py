def Push(x,stack1,stack2):
    stack1+=[x]
    


#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    if len(stack1)==0:
        return -1
    else:
        y=stack1.pop(0)
        return y
    
