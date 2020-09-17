#!/usr/bin/env python
# coding: utf-8

# # Information Practices Project
# # Data Analysis Videogame Data set
# # BY BHARAT KUMAR SHARMA

# # The Videogame Dataset
# Here.The Videogame Dataset is a time-series data with  information about the global sales of videogaems the different publisher the genre year the game was released in the platform the game was released for 
# 
# The data is in csv format. We will use pandas for the analysis.
# 
# 

# In[147]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


data=pd.read_csv(r'C:\Users\dell\Documents\vgsalesGlobale.csv')


# # Data

# In[8]:


data


# # Data Exploration

# In[9]:


data.info()


# In[10]:


data.describe()


# In[11]:


data.shape


# # So we have 16598 rows and 11 columns

# In[12]:


data.head()


# In[13]:


data.index


# In[14]:


data.columns


# In[15]:


data.dtypes


# In[16]:


data['Name'].unique()


# In[17]:


data['Platform'].unique()


# In[18]:


data['Year'].unique()


# In[19]:


data['Genre'].unique()


# In[20]:


data['Publisher'].unique()


# In[21]:


data['NA_Sales'].nunique()


# In[22]:


data['EU_Sales'].nunique()


# In[23]:


data['JP_Sales'].nunique()


# In[24]:


data['Global_Sales'].nunique()


# In[25]:


data.nunique()


# In[26]:


data.count()


# In[27]:


data['Name'].value_counts()


# # Data Cleaning 
# 

# In[28]:


data.isnull().sum()


# In[29]:


data1=data.drop(['Rank','NA_Sales','EU_Sales','JP_Sales','Other_Sales'],axis='columns')


# In[30]:


#data.loc[~(data==0.00).all(axis=1)]
data2=data1.dropna()


# In[31]:


data2.isnull().sum()


# # Removing outliers

# In[32]:


data3=data2[~(data1['Global_Sales']<1)]


# In[33]:


data3.shape


# In[34]:


data3


# In[35]:


a=data3['Global_Sales']
print(a)
b=round(a)
c=b
print(c)
data4=data3.drop(['Global_Sales'],axis='columns')
data4['Global_sales']=c
data4


# # Data Analysis

# # Questions 🙋
# 1. Which publisher has made most games.
# 2. Which is the most used platform .
# 3. In which Year maximum games were made.
# 4. Which platform was most used in which year.
# 5. Which year could be said the games manufacturing year.
# 6. Which genere is the most popular 
# 7. Which deacde which genre was popular
# 8. Biggest game publisher
# 9. Which deacde which genre was popular based on sales
# 10. Most sold genre
# 11. Most famous genre based on global sales.

# question 1. Which publisher has made most games?
# 

# In[36]:


data4['Publisher'].value_counts().max()


# In[37]:


data4['Publisher'].value_counts()


# # Hence Nintendo has made most games

# Question 2.Which is the most used platform ?

# In[38]:


data4['Platform'].value_counts().max()


# In[39]:


data4['Platform'].value_counts()


# # Hence PS2 is the most used platform.

# Question 3. In which Year maximum games were made?

# In[40]:


data4['Year'].value_counts().max()


# In[41]:


data4['Year'].value_counts()


# # Maximum games were made in 2008

# Question 5. Which genre is most popular.

# In[42]:


data4['Genre'].value_counts().max()


# In[43]:


data4['Genre'].value_counts()


# # Hence Action Genre is the most popular 

# # Data Visulization

# # using matplotlib for visulization

# In[84]:


import matplotlib.pyplot as plt
import numpy as np


# In[76]:


data4.boxplot()


# In[77]:


data4.hist()


# In[203]:


sns.pairplot(data4)


# In[86]:


grp=data4.groupby('Genre')
x=grp['Global_sales'].agg(np.sum)
x


# In[93]:


plt.figure(figsize=(15,10))
plt.plot(x, "ro" ,color='r')
plt.xticks(rotation=90)
plt.show()


# In[97]:


plt.figure(figsize=(18,8))
plt.plot(x,"r--",color='g')
plt.xticks(rotation=90)
plt.title("Genre wise Global sales")
plt.xlabel('Genre')
plt.ylabel('Gllobal sales in lakhs')
plt.show()


# In[100]:


grp=data4.groupby('Publisher')
y=grp['Global_sales'].agg(np.sum)
y


# In[109]:


plt.figure(figsize=(25,10))
plt.plot(y, "ro" ,color='r')
plt.xticks(rotation=90)
plt.show()


# In[107]:


plt.figure(figsize=(25,10))
plt.plot(y,"r--",color='b')
plt.xticks(rotation=90)
plt.title("Publisher wise Global sales")
plt.xlabel('Publisher')
plt.ylabel('Global sales in lakhs')
plt.show()


# In[110]:


grp=data4.groupby('Platform')
z=grp['Global_sales'].agg(np.sum)
z


# In[113]:


plt.figure(figsize=(15,5))
plt.plot(z, "ro" ,color='r')
plt.xticks(rotation=90)
plt.show()


# In[186]:


plt.figure(figsize=(15,6))
m=data4['Platform']
g=data4['Global_sales']
sns.pointplot(m,g,color='violet')

plt.ylabel('Global Sales in lakhs')
plt.xlabel('Publisher')
plt.show()


# In[172]:


plt.figure(figsize=(15,6))
m=data4['Year']
g=data4['Global_sales']
sns.jointplot(m,g,color='g')

plt.ylabel('Global Sales in lakhs')
plt.xlabel('Year')
plt.show()


# In[120]:


plt.figure(figsize=(15,6))
plt.plot(z,"r--",color='b')
plt.xticks(rotation=90)
plt.title("PLatform wise Global sales")
plt.xlabel('Platform')
plt.ylabel('Global sales in lakhs')
plt.show()


# In[145]:


plt.figure(figsize=(15,6))
m=data4['Platform']
g=data4['Global_sales']
plt.bar(m,g,color='g')
plt.xticks(m)
plt.ylabel('Global Sales in lakhs')
plt.xlabel('Platform')
plt.show()


# In[185]:


plt.figure(figsize=(15,6))
m=data4['Genre']
g=data4['Year']
sns.violinplot(m,g,color='red')

plt.ylabel('Global Sales in lakhs')
plt.xlabel('Publisher')
plt.show()


# In[169]:


plt.figure(figsize=(15,6))
m=data4['Genre']
g=data4['Global_sales']
plt.bar(m,g,color='g')
plt.xticks(m)
plt.ylabel('Global Sales in lakhs')
plt.xlabel('Genre')
plt.show()


# In[164]:


plt.figure(figsize=(10,5))
sns.heatmap(data4.corr(),annot=True,linewidth=0.5,cmap='Blues')


# In[181]:


plt.figure(figsize=(15,6))
m=data4['Platform']
g=data4['Global_sales']
sns.stripplot(m,g,color='violet')

plt.ylabel('Global Sales in lakhs')
plt.xlabel('Publisher')
plt.show()


# In[5]:


import pyfiglet
a=pyfiglet.figlet_format("COMPLETE")
print(a)


# In[12]:


import pyfiglet
a=pyfiglet.figlet_format("BY \n BHARAT \n KUMAR \n SHARMA")
print(a)


# # Source of Data - Dataworld
# 

# In[ ]:




