# -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:30:15 2017

@author: Harsha SlimShady
"""

import csv

filename = "tweets.csv"

rows = []
fields = []

with open(filename,'r',encoding='utf8') as csvfile:
    
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    
    
print(rows[2][1])
