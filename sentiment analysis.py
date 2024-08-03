#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request, json
with urllib.request.urlopen("https://storage.googleapis.com/wd13/lexicon.txt") as url:
  lexicon_file = url.read().decode()
lexicon = {}
for line in lexicon_file.split('\n'):
  split_line = line.split('\t')
  token = split_line[0]
  score = float(split_line[1])
  lexicon[token] = score


# In[2]:


lexicon.keys()


# In[3]:


lexicon['great']


# In[4]:


lexicon['best']


# In[5]:


lexicon["wonderful"]


# In[6]:


list_of_keys=list(lexicon.keys())


# In[7]:


#Let's write a function that takes a string and returns a sentiment score using our lexicon.

def sentiment_scoring(text,lexicon):
    if text is None:
        return 0
    
    words = text.lower().split()
    score = 0
    for word in words:
        if word in lexicon:
            score += lexicon[word]
    else:
        score += 0
    return score

    


# In[8]:


pip install google-play-scraper


# In[9]:


import google_play_scraper as gps


# In[10]:


id = 'com.netflix.mediaclient'


# In[ ]:


Netflix_reviews = gps.reviews_all(
  id,
  lang='en',
  country='ca')


# In[ ]:


Netflix_reviews[0:5]


# In[ ]:





# In[ ]:


for Netflix_review in Netflix_reviews:
    content = Netflix_review['content']
    sentiment_score=sentiment_scoring(content,lexicon)
    Netflix_review['sentiment_score']=sentiment_score


# In[ ]:


Netflix_review


# In[ ]:


# add sentiment_flag variable
# add year variable
# convert to Pandas dataframe
# calculate what percentage of reviews are postive and what percentage are negative
# show how sentiment has changed over time

for Netflix_review in Netflix_reviews:
    Netflix_review['sentiment_flag'] = 'positive' if Netflix_review['sentiment_score'] >  0 else 'negative' 
    Netflix_review['year']=Netflix_review['at'].year
    Netflix_review['month']=Netflix_review['at'].month


# In[ ]:


Netflix_review


# In[ ]:


Netflix_reviews[0:1]


# In[ ]:


pip install pandas


# In[ ]:


import pandas as pd


# In[ ]:


df = pd.DataFrame(Netflix_reviews)


# In[ ]:


df.head(1)


# In[ ]:


df.head()


# In[ ]:


df


# In[ ]:





# In[ ]:




