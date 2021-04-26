#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:54:10 2021

@author: marcel grigo
"""

import pandas as pd
df_test=pd.read_csv('../data/test.csv', delimiter=',')
df_train=pd.read_csv('../data/train.csv', delimiter=',')
df_gt=pd.read_csv('../data/gender_submission.csv', delimiter=',')

import matplotlib.pyplot as plt 
plt.close("all")
