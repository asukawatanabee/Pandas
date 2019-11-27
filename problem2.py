#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 00:10:49 2019

@author: asukawatanabe
"""
import pandas as pd
data = pd.read_csv("cars.csv")
df = pd.DataFrame(data)
x = df[df.index%2 != 0].head()
y = df.loc[df["Model"]=="Mazda RX4"]
z = df.loc[df["Model"]=="Camaro Z28"].loc[:,["Model","cyl"]]

a = df.loc[df["Model"]=="Mazda RX4 Wag"].loc[:,["Model","cyl","gear"]]
b = df.loc[df["Model"]=="Ford Pantera L"].loc[:,["Model","cyl","gear"]]
c = df.loc[df["Model"]=="Honda Civic"].loc[:,["Model","cyl","gear"]]

print(x)
print(y)
print(z)
print(a)
print(b)
print(c)