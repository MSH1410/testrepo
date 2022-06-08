#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=[]
n=9.0

for a in range(0,11):
    for b in range(0,11):
        while n!=1 :
            if n % 2 == 0:
                n= n // 2
            else:
                n=a* n + b
            if n==1 or n in x:
                print("converges for:",a,b)
                break
            elif len(x)>=100:
                print("does not converge:",a,b)
                break
            x.append(n)
   
        n=9.0
        x=[]

