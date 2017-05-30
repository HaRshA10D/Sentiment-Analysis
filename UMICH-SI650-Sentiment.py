# -*- coding: utf-8 -*-
"""
Created on Wed May 31 02:41:00 2017

@author: Harsha SlimShady
"""

import urllib.request

test_data_url = "https://dl.dropboxusercontent.com/u/8082731/datasets/UMICH-SI650/testdata.txt"
train_data_url = "https://dl.dropboxusercontent.com/u/8082731/datasets/UMICH-SI650/training.txt"

test_data_file_name = 'test_data.csv'
train_data_file_name = 'train_data.csv'

test_data_f = urllib.request.urlretrieve(test_data_url,test_data_file_name)
train_data_f = urllib.request.urlretrieve(train_data_url,train_data_file_name)

