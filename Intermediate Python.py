#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Intermediate Python


# In[4]:


#basic plots with matplotlib


# In[7]:


import matplotlib.pyplot as plt
year=[1992,1993,1979,2010]
pop=[2,5,8,98]
plt.plot(year,pop)
plt.show()


# In[8]:


import matplotlib.pyplot as plt
year=[1992,1993,1979,2010]
pop=[2,5,8,98]
plt.scatter(year,pop)
plt.show()


# In[3]:


import matplotlib.pyplot as plt
value=[21,6,33,0.4,55,3,40,14,6,3.9,19]
plt.hist(value, bins=3)
plt.show()


# In[9]:


#Customization
import matplotlib.pyplot as plt
year=[1950,1951,1952 ,2100]
pop=[2.538, 2.57,2.62 ,10.85]
plt.plot(year,pop)
plt.xlabel('year')
#Add more data
year=[1800,1850,1900]+year
pop=[1.0,1.262,1.650]+pop

plt.ylabel('population')
plt.title('World population projections')
plt.yticks([0,2,4,6,8,10],
          ['0','2B','4B','6B','8B','10B'])

plt.show()


# In[ ]:




