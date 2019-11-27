#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:02:58 2019

@author: asukawatanabe
"""
import pandas as pd
data = pd.read_csv('cars.csv')
df = pd.DataFrame(data)
x = df.head()
y = df.tail()
print(x)
print(y)