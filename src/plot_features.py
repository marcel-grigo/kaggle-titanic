#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 18:15:57 2021

@author: marcel
"""
import pandas as pd
df_test=pd.read_csv('../data/test.csv', delimiter=',')
df_train=pd.read_csv('../data/train.csv', delimiter=',')
df_gt=pd.read_csv('../data/gender_submission.csv', delimiter=',')

# encode strings to int
df_train = df_train.replace('male', 0, regex=True)
df_train = df_train.replace('female', 1, regex=True)


# select features to plot 
df_train = df_train[['Survived', 'Sex', 'Pclass', 'Age', 'SibSp', 'Parch']]

import seaborn as sns
sns.set()
df_train.head()
sns.pairplot(df_train, hue='Survived');