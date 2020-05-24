#!/usr/bin/env python
# coding: utf-8

# In[34]:


file1 = open("input.txt","r")  

build=int(file1.readline()) 
 
layer=int(file1.readline()) 

pool=int(file1.readline()) 

stride=int(file1.readline()) 

epoch=int(file1.readline())

line1=file1.readline()

line2=file1.readline()

line3=file1.readline()

file1.close()


# In[37]:


file2 = open("accuracy.txt","r")

accuracy=float(file2.readline())


# In[38]:


build+=1
file3 = open("input.txt","w")  

if accuracy<=0.99:
    if build==2:
        layer+=10
        pool-=1
        stride-=1
        epoch+=1
        L=[str(build),"\n",str(layer),"\n",str(pool),"\n",str(stride),"\n",str(epoch),"\n",line1,"\n",line2,"\n",line3]
        file3.writelines(L)
    
if accuracy<=0.99:
    if build==3:
        layer+=10
        pool-=1
        stride-=1
        epoch+=1
        line1="model.add(Conv2D(50, (5, 5),padding =\"same\"))"
        line2="model.add(Activation(\"relu\"))"
        line3="model.add(MaxPooling2D(pool_size = (2, 2), strides = (2, 2)))"
        L=[str(build),"\n",str(layer),"\n",str(pool),"\n",str(stride),"\n",str(epoch),"\n",line1,"\n",line2,"\n",line3]
        file3.writelines(L)

if accuracy<=0.99:
    if build==4:
        epoch+=1
        line1="model.add(Conv2D(50, (5, 5),padding =\"same\"))"
        line2="model.add(Activation(\"relu\"))"
        line3="model.add(MaxPooling2D(pool_size = (2, 2), strides = (2, 2)))"
        L=[str(build),"\n",str(layer),"\n",str(pool),"\n",str(stride),"\n",str(epoch),"\n",line1,"\n",line2,"\n",line3]
        file3.writelines(L)

file3.close()


# In[ ]:




