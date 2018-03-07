# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:38:17 2018

@author: Desna
"""
import pandas as pd
import matplotlib.pyplot as plt
producer=pd.read_excel('producer2017.xlsx')
print(producer.info())
produceryear=producer.groupby('producer')['sumvat'].sum().div(1000000).mul(6)
print(produceryear)
produceryear.plot(kind='bar')
plt.show()