
# coding: utf-8

# In[2]:


import pandas
import matplotlib.pyplot as plt
from IPython.display import display


# In[3]:


adult = pandas.read_csv('adult.data',names = ["age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","GROUP"]) # import ANEW

display(adult.head())


# In[3]:


#INFORMASI STATISTIK

display(adult.describe())
display(adult.mean())
display(adult.median())


# In[4]:


display(adult.shape)


# In[4]:


#LABEL WORKCLASS

workclass = adult['workclass']
display(workclass.value_counts(dropna=False))


# In[6]:


#LABEL EDUCAITON

education = adult['education']
display(education.value_counts(dropna=False))


# In[7]:


#LABEL MARITAL_STATUS

marital_status = adult['marital-status']
display(marital_status.value_counts(dropna=False))


# In[8]:


#LABEL OCCUPATION

occ = adult['occupation']
display(occ.value_counts(dropna=False))


# In[9]:


#LABEL RELATIONSHIP

rel = adult['relationship']
display(rel.value_counts(dropna=False))


# In[10]:


#LABEL RACE

race = adult['race']
display(race.value_counts(dropna=False))


# In[11]:


#LABEL SEX

sex = adult['sex']
display(sex.value_counts(dropna=False))


# In[12]:


#LABEL NATIVE

nat = adult['native-country']
display(nat.value_counts(dropna=False))


# In[13]:


age = adult['age']
cap = adult['capital-gain']
cap_los = adult['capital-loss']
ed = adult['education-num']
fnlwgt = adult['fnlwgt']
hpw = adult['hours-per-week']


# In[14]:


#VISUALiSASI AGE

plt.figure(figsize=(14, 8))
age.hist()
plt.show()


# In[15]:


#VISUALiSASI CAPITAL-GAIN

plt.figure(figsize=(14, 8))
cap.hist()
plt.show()


# In[16]:


#VISUALiSASI CAPITAL LOSS

plt.figure(figsize=(14, 8))
cap_los.hist()
plt.show()


# In[17]:


#VISUALiSASI EDUCATION NUM

plt.figure()
ed.hist()
plt.show()


# In[18]:


#VISUALiSASI FNLWGT

plt.figure(figsize=(14, 8))
fnlwgt.hist()
plt.show()


# In[19]:


#VISUALiSASI HPW

plt.figure(figsize=(14, 8))
hpw.hist()
plt.show()


# In[ ]:


#VISUALiSASI WORKCLASS

plt.figure(figsize=(14, 8))
workclass.hist()
plt.show()


# In[ ]:


#VISUALiSASI EDUCATION

plt.figure(figsize=(14, 6))
education.hist()
plt.show()


# In[ ]:


#VISUALiSASI MARITAL

plt.figure(figsize=(14, 6))
marital_status.hist()
plt.show()


# In[ ]:


#VISUALiSASI OCUPATION

plt.figure(figsize=(14, 6))
occ.hist()
plt.show()


# In[ ]:


#VISUALiSASI RELATIONSHIP

plt.figure(figsize=(14, 6))
rel.hist()
plt.show()


# In[ ]:


#VISUALiSASI RACE

plt.figure(figsize=(14, 6))
race.hist()
plt.show()


# In[ ]:


#VISUALiSASI SEX

sex.hist()
plt.show()


# In[ ]:


#VISUALiSASI NATIONAL

plt.figure(figsize=(20, 8))
nat.hist()
plt.show()

