#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
# libraries for making count matrix and similarity matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[4]:


df=pd.read_csv('data.csv')


# In[9]:


def content_based_recommender(winery):

    winery = str(winery)
    if winery in df['winery'].values:
        common_wineries = df
        common_wineries = common_wineries.drop_duplicates(subset=['winery'])
        common_wineries.reset_index(inplace= True)
        common_wineries['index'] = [i for i in range(common_wineries.shape[0])]
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(common_wineries['variety'])
        cosine_sim = cosine_similarity(count_matrix)
        index = common_wineries[common_wineries['winery'] == winery]['index'].values[0]
        sim_wineries = list(enumerate(cosine_sim[index]))
        sorted_sim_wineries = sorted(sim_wineries,key=lambda x:x[1],
                                      reverse=True)[1:6]

        wineries = []
        for i in range(len(sorted_sim_wineries)):
            wineries.append(common_wineries[common_wineries['index'] == sorted_sim_wineries[i][0]]['winery'].item())
        return(wineries)

    else:

        return('Cant find winery in dataset, please check spelling')


# In[10]:


content_based_recommender('Ponzi')


# In[ ]:


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend")
def recommend():
    winery = request.args.get('winery')
    rec = content_based_recommender(winery)
    wnery = winery.upper()
    if type(rec)==type('string'):
        return render_template('recommend.html',winery=winery,rec=rec,t='s')
    else:
        return render_template('recommend.html',winery=winery,rec=rec,t='wineries')



if __name__ == '__main__':
    app.run()


# In[ ]:
