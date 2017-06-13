# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 20:22:39 2017

@author: Harsha SlimShady
"""

from amazon_scraper import AmazonScraper
from textblob import TextBlob
import numpy as np
    
acess_key = 'AKIAINUJU5KTWE3LAIGQ'
secret_key = 'XXXXXXXXXXXXXXXXXXXXXX'
customer_tag = 'harsha10d-21'
    
def initialize(prodId):
        
    
    amzn = AmazonScraper(acess_key,secret_key,customer_tag,Region='IN')
    p = amzn.lookup(ItemId=prodId)
    rs = amzn.reviews(ItemId=prodId)
    reviews,reviews_title = [],[]
    i = 1
    for r in rs:
        fr = r.full_review()
        print_review(fr.title,fr.text,i)
        reviews.append(fr.text)
        reviews_title.append(fr.title)
        i += 1 
    prodName = p.title
    for x in range(len(prodName)):
        string = list(prodName)
        if string[x] == '.' or string[x] == '/' : string[x] = '-'
        prodName = ''.join(string)
    return reviews,reviews_title,prodName
    
def print_review(tt,tx,i):
    print('Review : %d'%(i))
    print('Title : %s'%tt)
    print('Content : %s'%tx)
    print('***--------------***') 
            
def doSentiment(reviews,reviews_title,prodName):
        
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
    prodName = prodName.replace("/","-")
    plt.savefig(prodName)
    plt.show()
            
            
