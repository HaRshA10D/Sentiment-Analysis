# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 20:22:39 2017

@author: Harsha SlimShady
"""

from amazon_scraper import AmazonScraper
from textblob import TextBlob
import numpy as np
    
acess_key = 'AKIAINUJU5KTWE3LAIGQ'
secret_key = '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'
customer_tag = 'harsha10d-21'
prodName = ''
    
def initialize(prodId,prodName):
        
    
    amzn = AmazonScraper(acess_key,secret_key,customer_tag,Region='IN')
    p = amzn.lookup(ItemId=prodId)
    rs = p.reviews()
    all_on_page = list(rs)
    reviews,reviews_title = [],[]
    for r in all_on_page:
        fr = r.full_review()
        reviews.append(fr.text)
        reviews_title.append(fr.title)
    return reviews,reviews_title
    
def printAll(reviews,reviews_title):
    for i in range(len(reviews)):
        print('Review : %d'%(i+1))
        print('Title : %s'%reviews_title[i])
        print('Content : %s'%reviews[i])
        print('***--------------***') 
            
def doSentiment(reviews,reviews_title):
        
    i = 1
    x_points = []
    y_points = []
        
    all_senti = 0.0
    for rev in reviews:
        lines = rev.split('.')
        polarity = 0.0
        x = 0
        for line in lines:
            tb = TextBlob(line)
            line_pol = tb.sentiment.polarity
            polarity += line_pol
            if(line_pol!=0.0) : x += 1
        polarity += TextBlob(reviews_title[i-1]).sentiment.polarity
        total_senti = polarity/float(x+1)
        all_senti += total_senti 
        x_points.append(i)
        y_points.append(total_senti)
        print('polarity of review no: %d = %f'%(i,total_senti))
        i += 1
        
    all_senti = all_senti/float(i)
    
    y = np.tile(all_senti,(i-1,1))
    
    import matplotlib.pyplot as plt
    plt.plot(x_points,y_points)
    plt.plot(x_points,y)
    plt.xlabel('Review number')
    plt.ylabel('Polarity')
    plt.savefig(prodName)
    plt.show()
            
            