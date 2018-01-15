
# coding: utf-8

# In[1]:


from nltk import word_tokenize,ne_chunk,pos_tag,sent_tokenize


# In[12]:


import re
import faker
from faker import Factory


# In[18]:


import pandas as pd

import sys
inFile = sys.argv[1]


# In[16]:


fake=faker.Faker()


# In[328]:

with open(inFile,'r') as i:
    sample = i.readlines()
#sample="He works in IBM . My name is Atanu . My dogs name is Rocky .I live in Bangalore . I am from Paris . My Brother name is Santanu . His number is 8123650499 . My email id is atanu@gmail.com . My IP is 124.2.4.56 . "


# In[329]:

sample=str(sample)

sent_tokenize_list=sent_tokenize(sample)
sent1=[]
for sent in sent_tokenize_list:
    word_tokenzer=ne_chunk(pos_tag(word_tokenize(sent)))
    #print(type(word_tokenzer))
    sent1.append(str(word_tokenzer))


# In[330]:


def sar_name(line):
    list_name=[]
    df_name=pd.DataFrame(columns=['Field','Value','Changed_Value'])
    m=re.findall('\(PERSON (.+?)\/',line)
    for i in m:
        if i:
            list_name.append(['PERSON',i,fake.state()])
    return list_name   


# In[331]:


df_main=pd.DataFrame()
list_name=[]
for l in sent1:
    m=re.findall('\(PERSON (.+?)\/',l)
    for i in m:
        if i:
            list_name.append(['PERSON',i,fake.first_name()])
for l in sent1:
    m=re.findall('\(GPE (.+?)\/',l)
    for i in m:
        if i:
            list_name.append(['PLACE',i,fake.country()])
for l in sent1:
    m=re.findall('\(ORGANIZATION (.+?)\/',l)
    for i in m:
        if i:
            list_name.append(['ORGANIZATION',i,fake.company()])            
for l in sent1:
    m=re.findall('[0-9]{10}',l)
    for i in m:
        if i:
            list_name.append(['PHONE',i,fake.phone_number()])   
for l in sent_tokenize_list:
    m=re.findall('[\w\.-]+@[\w\.-]+',l)
    #print(l)
    for i in m:
        if i:
            #print('in here also')
            list_name.append(['EMAIL',i,fake.email()])   
for l in sent1:
    m=re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',l)
    for i in m:
        if i:
            list_name.append(['IP',i,fake.ipv4()])               


# In[332]:


#li_main_fi=[]
#for li in list_name:
#    print(li)


# In[333]:


#list_name


# In[334]:


columns1=[['Field','Value','Changed_Value']]
df_main=pd.DataFrame.from_records(list_name,columns=columns1)


# In[335]:


#df_main


# In[336]:


for ele,val in df_main.iterrows():
    #print(ele,val['Field'])
    sample=re.sub(val['Value'],val['Changed_Value'],sample)
    #print(text)


# In[337]:


for ele,val in df_main.iterrows():
    
    if val['Field']=='PERSON':
        #print(ele,val['Field'])
        sample=re.sub(val['Value'],val['Changed_Value'],sample)
        #print(text)


# In[340]:


print(sample)

